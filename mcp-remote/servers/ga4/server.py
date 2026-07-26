"""Remote HTTP MCP for Google Analytics 4.

Auth to Google = OAuth refresh-token flow. Auth to this server = bearer
token in `MCP_API_KEY`.

Refresh token is seeded once via `seed_oauth.py` from Sunny's laptop.
Scope: `https://www.googleapis.com/auth/analytics.readonly`.
"""

from __future__ import annotations

import os
import threading
import time
from typing import Any

from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.responses import JSONResponse
from starlette.routing import Route

from auth import BearerAuth

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
REFRESH_TOKEN = os.environ.get("GOOGLE_REFRESH_TOKEN", "")

_lock = threading.Lock()
_data_service = None
_admin_service = None
_expires_at = 0.0


def _build_creds() -> Credentials:
    if not (CLIENT_ID and CLIENT_SECRET and REFRESH_TOKEN):
        raise RuntimeError(
            "GOOGLE_CLIENT_ID / GOOGLE_CLIENT_SECRET / "
            "GOOGLE_REFRESH_TOKEN env vars must be set"
        )
    creds = Credentials(
        token=None,
        refresh_token=REFRESH_TOKEN,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri="https://oauth2.googleapis.com/token",
        scopes=SCOPES,
    )
    creds.refresh(GoogleRequest())
    return creds


def _services():
    global _data_service, _admin_service, _expires_at
    with _lock:
        if _data_service and _admin_service and time.time() < _expires_at:
            return _data_service, _admin_service
        creds = _build_creds()
        _data_service = build(
            "analyticsdata", "v1beta", credentials=creds, cache_discovery=False
        )
        _admin_service = build(
            "analyticsadmin", "v1beta", credentials=creds, cache_discovery=False
        )
        _expires_at = time.time() + 50 * 60
        return _data_service, _admin_service


mcp = FastMCP(
    "ga4",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)


def _property_id(property_id: str | int) -> str:
    s = str(property_id)
    return s if s.startswith("properties/") else f"properties/{s}"


@mcp.tool()
def list_account_summaries() -> list[dict[str, Any]]:
    """Every GA4 account + child property this OAuth account can see."""
    _, admin = _services()
    resp = admin.accountSummaries().list().execute()
    return resp.get("accountSummaries", [])


@mcp.tool()
def get_property(property_id: str) -> dict[str, Any]:
    """Details for a single GA4 property."""
    _, admin = _services()
    return admin.properties().get(name=_property_id(property_id)).execute()


@mcp.tool()
def run_report(
    property_id: str,
    metrics: list[str],
    dimensions: list[str] | None = None,
    start_date: str = "7daysAgo",
    end_date: str = "today",
    row_limit: int = 100,
    order_by_metric: str | None = None,
    dimension_filter: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Run a GA4 report.

    `metrics` and `dimensions` are GA4 API names, e.g. ["sessions", "activeUsers"],
    ["pagePath", "country"]. Dates accept ISO (YYYY-MM-DD) or NdaysAgo / today / yesterday.
    """
    data, _ = _services()
    body: dict[str, Any] = {
        "dateRanges": [{"startDate": start_date, "endDate": end_date}],
        "metrics": [{"name": m} for m in metrics],
        "limit": row_limit,
    }
    if dimensions:
        body["dimensions"] = [{"name": d} for d in dimensions]
    if order_by_metric:
        body["orderBys"] = [{"metric": {"metricName": order_by_metric}, "desc": True}]
    if dimension_filter:
        body["dimensionFilter"] = dimension_filter
    return (
        data.properties()
        .runReport(property=_property_id(property_id), body=body)
        .execute()
    )


@mcp.tool()
def run_realtime_report(
    property_id: str,
    metrics: list[str],
    dimensions: list[str] | None = None,
) -> dict[str, Any]:
    """Real-time report — active users in the last 30 min etc."""
    data, _ = _services()
    body: dict[str, Any] = {"metrics": [{"name": m} for m in metrics]}
    if dimensions:
        body["dimensions"] = [{"name": d} for d in dimensions]
    return (
        data.properties()
        .runRealtimeReport(property=_property_id(property_id), body=body)
        .execute()
    )


@mcp.tool()
def portfolio_traffic(days: int = 7) -> dict[str, Any]:
    """One-shot sweep: sessions + engagement per property, last N days."""
    _, admin = _services()
    data, _ = _services()
    summaries = admin.accountSummaries().list().execute().get("accountSummaries", [])
    out: dict[str, Any] = {}
    for account in summaries:
        for prop in account.get("propertySummaries", []) or []:
            name = prop.get("property")
            if not name:
                continue
            try:
                body = {
                    "dateRanges": [
                        {"startDate": f"{days}daysAgo", "endDate": "today"}
                    ],
                    "metrics": [
                        {"name": "sessions"},
                        {"name": "activeUsers"},
                        {"name": "engagementRate"},
                    ],
                    "limit": 1,
                }
                r = (
                    data.properties()
                    .runReport(property=name, body=body)
                    .execute()
                )
                rows = r.get("rows", [])
                vals = rows[0].get("metricValues", []) if rows else []
                out[prop.get("displayName", name)] = {
                    "property": name,
                    "sessions": vals[0].get("value") if len(vals) > 0 else None,
                    "activeUsers": vals[1].get("value") if len(vals) > 1 else None,
                    "engagementRate": vals[2].get("value") if len(vals) > 2 else None,
                }
            except HttpError as e:
                out[prop.get("displayName", name)] = {"error": str(e)}
    return out


async def _health(_request):
    return JSONResponse({"ok": True, "server": "ga4"})


def build_app():
    app = mcp.streamable_http_app()
    app.router.routes.insert(0, Route("/health", _health))
    app.add_middleware(BearerAuth)
    return app


app = build_app()


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
