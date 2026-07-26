"""Remote HTTP MCP for Bing Webmaster Tools.

Wraps the public Bing Webmaster Tools JSON API. Auth = single API key
in `BING_API_KEY`. Client-side auth to this server = bearer token in
`MCP_API_KEY`.
"""

from __future__ import annotations

import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from starlette.responses import JSONResponse
from starlette.routing import Route

from auth import BearerAuth

BING_BASE = "https://ssl.bing.com/webmaster/api.svc/json"
BING_API_KEY = os.environ.get("BING_API_KEY", "")

# DNS-rebinding protection off — we front with a bearer token, and
# blocking the Fly hostname prevents any remote client from connecting.
mcp = FastMCP(
    "bing-webmaster",
    transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
)


def _client() -> httpx.Client:
    if not BING_API_KEY:
        raise RuntimeError("BING_API_KEY env var not set")
    return httpx.Client(timeout=30.0)


def _get(path: str, params: dict[str, Any] | None = None) -> Any:
    p = {"apikey": BING_API_KEY, **(params or {})}
    with _client() as c:
        r = c.get(f"{BING_BASE}/{path}", params=p)
        r.raise_for_status()
        return r.json().get("d")


def _post(path: str, body: dict[str, Any]) -> Any:
    with _client() as c:
        r = c.post(
            f"{BING_BASE}/{path}",
            params={"apikey": BING_API_KEY},
            json=body,
        )
        r.raise_for_status()
        try:
            return r.json().get("d")
        except ValueError:
            return {"ok": True}


@mcp.tool()
def list_sites() -> list[dict[str, Any]]:
    """List every site verified in this Bing Webmaster Tools account."""
    return _get("GetUserSites") or []


@mcp.tool()
def get_url_info(site_url: str, url: str) -> dict[str, Any]:
    """Bing's known info for a single URL on the given site."""
    return _get("GetUrlInfo", {"siteUrl": site_url, "url": url}) or {}


@mcp.tool()
def get_page_stats(site_url: str) -> list[dict[str, Any]]:
    """Per-page traffic and impression stats for a site."""
    return _get("GetPageStats", {"siteUrl": site_url}) or []


@mcp.tool()
def get_query_stats(site_url: str) -> list[dict[str, Any]]:
    """Search-query performance for a site."""
    return _get("GetQueryStats", {"siteUrl": site_url}) or []


@mcp.tool()
def get_rank_and_traffic_stats(site_url: str) -> list[dict[str, Any]]:
    """Historical rank + traffic time series for a site."""
    return _get("GetRankAndTrafficStats", {"siteUrl": site_url}) or []


@mcp.tool()
def get_crawl_stats(site_url: str) -> list[dict[str, Any]]:
    """Bingbot crawl activity time series for a site."""
    return _get("GetCrawlStats", {"siteUrl": site_url}) or []


@mcp.tool()
def get_crawl_issues(site_url: str) -> list[dict[str, Any]]:
    """Crawl errors Bingbot encountered on this site."""
    return _get("GetCrawlIssues", {"siteUrl": site_url}) or []


@mcp.tool()
def get_url_submission_quota(site_url: str) -> dict[str, Any]:
    """Remaining daily + monthly URL submission quota."""
    return _get("GetUrlSubmissionQuota", {"siteUrl": site_url}) or {}


@mcp.tool()
def submit_url(site_url: str, url: str) -> dict[str, Any]:
    """Submit a single URL to Bing for indexing."""
    return _post("SubmitUrl", {"siteUrl": site_url, "url": url})


@mcp.tool()
def submit_url_batch(site_url: str, urls: list[str]) -> dict[str, Any]:
    """Submit up to 100 URLs at once to Bing for indexing."""
    return _post("SubmitUrlbatch", {"siteUrl": site_url, "urlList": urls})


@mcp.tool()
def get_deep_crawl_urls(site_url: str) -> list[dict[str, Any]]:
    """Bing's deep-crawl URL list for a site."""
    return _get("GetDeepCrawlUrls", {"siteUrl": site_url}) or []


@mcp.tool()
def portfolio_errors() -> dict[str, Any]:
    """Aggregate crawl issues across every verified Bing site.

    Returns a dict keyed by site URL with counts and the first ten
    issues per site. Meant for a fast 'anything broken?' sweep.
    """
    sites = _get("GetUserSites") or []
    out: dict[str, Any] = {}
    for s in sites:
        site_url = s.get("Url") or s.get("SiteUrl")
        if not site_url:
            continue
        try:
            issues = _get("GetCrawlIssues", {"siteUrl": site_url}) or []
        except httpx.HTTPError as e:
            out[site_url] = {"error": str(e)}
            continue
        out[site_url] = {
            "count": len(issues),
            "sample": issues[:10],
        }
    return out


async def _health(_request):
    return JSONResponse({"ok": True, "server": "bing-webmaster"})


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
