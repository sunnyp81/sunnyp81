"""Remote HTTP MCP for Google Search Console.

Auth to Google = OAuth refresh-token flow (client_id + client_secret +
refresh_token stored as Fly secrets). Auth to this server = bearer token
in `MCP_API_KEY`.

The refresh token is seeded once via `seed_oauth.py` from Sunny's laptop.
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

SCOPES = ["https://www.googleapis.com/auth/webmasters"]

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "")
REFRESH_TOKEN = os.environ.get("GOOGLE_REFRESH_TOKEN", "")

_service = None
_service_lock = threading.Lock()
_service_expires_at = 0.0


def _get_service():
    """Cache the discovery-built service across requests; refresh on TTL."""
    global _service, _service_expires_at
    with _service_lock:
        if _service is not None and time.time() < _service_expires_at:
            return _service
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
        _service = build(
            "searchconsole",
            "v1",
            credentials=creds,
            cache_discovery=False,
        )
        # Refresh well before Google's 60min access-token TTL.
        _service_expires_at = time.time() + 50 * 60
        return _service


mcp = FastMCP(
    "gsc",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)


@mcp.tool()
def list_sites() -> list[dict[str, Any]]:
    """Every property this OAuth account can see in Search Console."""
    svc = _get_service()
    resp = svc.sites().list().execute()
    return resp.get("siteEntry", [])


@mcp.tool()
def search_analytics(
    site_url: str,
    start_date: str,
    end_date: str,
    dimensions: list[str] | None = None,
    row_limit: int = 1000,
    search_type: str = "web",
    dimension_filter_groups: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Query the Search Analytics report for a property.

    dimensions: any of ["date", "query", "page", "country", "device", "searchAppearance"].
    Dates are YYYY-MM-DD.
    """
    svc = _get_service()
    body: dict[str, Any] = {
        "startDate": start_date,
        "endDate": end_date,
        "rowLimit": row_limit,
        "type": search_type,
    }
    if dimensions:
        body["dimensions"] = dimensions
    if dimension_filter_groups:
        body["dimensionFilterGroups"] = dimension_filter_groups
    return svc.searchanalytics().query(siteUrl=site_url, body=body).execute()


@mcp.tool()
def list_sitemaps(site_url: str) -> list[dict[str, Any]]:
    """All submitted sitemaps for a property, with errors/warnings counts."""
    svc = _get_service()
    resp = svc.sitemaps().list(siteUrl=site_url).execute()
    return resp.get("sitemap", [])


@mcp.tool()
def get_sitemap(site_url: str, feedpath: str) -> dict[str, Any]:
    """Detailed status for one sitemap, including per-content-type counts."""
    svc = _get_service()
    return svc.sitemaps().get(siteUrl=site_url, feedpath=feedpath).execute()


@mcp.tool()
def submit_sitemap(site_url: str, feedpath: str) -> dict[str, str]:
    """(Re)submit a sitemap URL to Search Console."""
    svc = _get_service()
    svc.sitemaps().submit(siteUrl=site_url, feedpath=feedpath).execute()
    return {"ok": "submitted", "feedpath": feedpath}


@mcp.tool()
def delete_sitemap(site_url: str, feedpath: str) -> dict[str, str]:
    """Remove a sitemap from Search Console."""
    svc = _get_service()
    svc.sitemaps().delete(siteUrl=site_url, feedpath=feedpath).execute()
    return {"ok": "deleted", "feedpath": feedpath}


@mcp.tool()
def inspect_url(site_url: str, inspection_url: str) -> dict[str, Any]:
    """Live URL Inspection: index status, coverage, robots, canonical, mobile."""
    svc = _get_service()
    body = {"inspectionUrl": inspection_url, "siteUrl": site_url}
    return svc.urlInspection().index().inspect(body=body).execute()


@mcp.tool()
def portfolio_errors(include_warnings: bool = True) -> dict[str, Any]:
    """Aggregate sitemap-level errors across every verified GSC property.

    Fast portfolio-wide sweep. For each site: list sitemaps, sum errors
    (+ warnings if `include_warnings`), and surface any sitemap whose
    status is `isPending=true` or whose lastDownloaded date is stale.
    Returns a dict keyed by site URL.
    """
    svc = _get_service()
    sites = svc.sites().list().execute().get("siteEntry", [])
    out: dict[str, Any] = {}
    for entry in sites:
        site_url = entry.get("siteUrl")
        if not site_url:
            continue
        if entry.get("permissionLevel") == "siteUnverifiedUser":
            out[site_url] = {"skipped": "unverified"}
            continue
        try:
            sitemaps = (
                svc.sitemaps().list(siteUrl=site_url).execute().get("sitemap", [])
            )
        except HttpError as e:
            out[site_url] = {"error": str(e)}
            continue
        total_errors = 0
        total_warnings = 0
        broken: list[dict[str, Any]] = []
        for s in sitemaps:
            errs = int(s.get("errors", 0) or 0)
            warns = int(s.get("warnings", 0) or 0)
            total_errors += errs
            if include_warnings:
                total_warnings += warns
            if errs or (include_warnings and warns) or s.get("isPending"):
                broken.append(
                    {
                        "path": s.get("path"),
                        "errors": errs,
                        "warnings": warns,
                        "isPending": s.get("isPending", False),
                        "lastSubmitted": s.get("lastSubmitted"),
                        "lastDownloaded": s.get("lastDownloaded"),
                    }
                )
        out[site_url] = {
            "sitemap_count": len(sitemaps),
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "broken_sitemaps": broken,
        }
    return out


@mcp.tool()
def inspect_urls_bulk(
    site_url: str,
    urls: list[str],
) -> list[dict[str, Any]]:
    """Run URL Inspection on a list of URLs and return each verdict.

    Bounded by GSC's 2000/day inspection quota per property.
    """
    svc = _get_service()
    results: list[dict[str, Any]] = []
    for u in urls:
        try:
            body = {"inspectionUrl": u, "siteUrl": site_url}
            resp = svc.urlInspection().index().inspect(body=body).execute()
            idx = resp.get("inspectionResult", {}).get("indexStatusResult", {})
            results.append(
                {
                    "url": u,
                    "verdict": idx.get("verdict"),
                    "coverageState": idx.get("coverageState"),
                    "robotsTxtState": idx.get("robotsTxtState"),
                    "indexingState": idx.get("indexingState"),
                    "lastCrawlTime": idx.get("lastCrawlTime"),
                    "pageFetchState": idx.get("pageFetchState"),
                    "googleCanonical": idx.get("googleCanonical"),
                    "userCanonical": idx.get("userCanonical"),
                }
            )
        except HttpError as e:
            results.append({"url": u, "error": str(e)})
    return results


async def _health(_request):
    return JSONResponse({"ok": True, "server": "gsc"})


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
