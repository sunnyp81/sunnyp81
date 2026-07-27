"""Daily SEO Gets snapshot puller — GSC + GA4 data with zero Google OAuth.

SEO Gets (Pro plan) already aggregates Search Console + Analytics for
every site added there, and its hosted MCP endpoint auths with a plain
API key. That sidesteps the whole Google consent-screen/refresh-token
dance, so this puller only needs `SEOGETS_API_KEY`.

The tool catalog on the server can change, so this puller is
self-discovering rather than hardcoded:

  1. `initialize` + `tools/list` — snapshot the catalog itself.
  2. Call every tool with no required params (site lists, account
     overviews, etc.).
  3. Harvest site/domain identifiers from those responses.
  4. Call every tool whose required params we can fill (a site-ish
     param, plus date-ish params derived from `--days`) once per site.

Writes JSON under data/seogets/YYYY-MM-DD/. Emits _summary.json.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import is_blacklisted
from shared.logging import die, log
from shared.mcp_client import McpError, McpHttpClient
from shared.paths import snapshot_path, summary_path, today_utc

DEFAULT_URL = "https://app.seogets.com/mcp"

SITE_PARAM_RE = re.compile(r"^(site|domain|property|website|host)(_?url|_?id|name)?$", re.I)
# SEO Gets' own list_sites keys each entry's identifier as plain "id".
SITE_KEY_RE = re.compile(r"^(site|domain|property|website|host|siteUrl|url|id)$", re.I)
# GSC domain-properties come back as "sc-domain:example.com", not a URL shape.
DOMAIN_RE = re.compile(r"^(?:https?://|sc-domain:)?[a-z0-9][a-z0-9.-]*\.[a-z]{2,}(?:/.*)?$", re.I)

MAX_SITES = 250
MAX_CALLS = 2000


def _write(service_args: tuple[str, str, str, str], day: str, payload: Any) -> Path:
    service, account_key, site, report = service_args
    p = snapshot_path(service, account_key, site, report, day)
    p.write_text(json.dumps(payload, indent=2, default=str))
    return p


def _required_params(tool: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    schema = tool.get("inputSchema") or {}
    return list(schema.get("required") or []), dict(schema.get("properties") or {})


def _date_fill(name: str, prop: dict[str, Any], days: int) -> Any | None:
    """Best-effort value for a date-ish param; None if not date-ish."""
    n = name.lower()
    start = (date.today() - timedelta(days=days)).isoformat()
    end = date.today().isoformat()
    if n in ("days", "numdays", "num_days", "lastdays", "last_days"):
        return days
    if n in ("startdate", "start_date", "datefrom", "date_from", "from", "since"):
        return start
    if n in ("enddate", "end_date", "dateto", "date_to", "to", "until"):
        return end
    if n in ("daterange", "date_range", "period", "range"):
        enum = prop.get("enum")
        if enum:
            # Prefer a ~28-day-ish option if the server offers presets.
            for want in ("28d", "30d", "last28days", "last30days", "month"):
                for e in enum:
                    if want in str(e).lower().replace(" ", ""):
                        return e
            return enum[0]
        return f"{start}..{end}"
    return None


def _misc_fill(name: str, prop: dict[str, Any]) -> Any | None:
    """Safe default for pagination/filter params some servers mark required."""
    n = name.lower()
    t = prop.get("type")
    if n == "page" and t in ("integer", "number"):
        return 1
    if n in ("page_size", "pagesize", "per_page", "page_limit"):
        return 1000
    if n in ("crawled_days_ago",):
        return 0
    if t == "array":
        return []
    return None


def _plan_args(tool: dict[str, Any], days: int) -> tuple[str | None, dict[str, Any], bool]:
    """(site_param_name, prefilled_args, fully_fillable) for one tool."""
    required, props = _required_params(tool)
    site_param: str | None = None
    args: dict[str, Any] = {}
    for name in required:
        if site_param is None and SITE_PARAM_RE.match(name):
            site_param = name
            continue
        prop = props.get(name) or {}
        val = _date_fill(name, prop, days)
        if val is None:
            val = _misc_fill(name, prop)
        if val is None:
            return site_param, args, False
        args[name] = val
    # Fill helpful optional date params too, so defaults match --days.
    for name, prop in props.items():
        if name in args or name in required:
            continue
        val = _date_fill(name, prop or {}, days)
        if val is not None:
            args[name] = val
    return site_param, args, True


def _harvest_sites(data: Any, found: dict[str, None]) -> None:
    """Collect site/domain identifiers from a tool response, in order."""
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, str) and SITE_KEY_RE.match(k) and DOMAIN_RE.match(v):
                found.setdefault(v, None)
            else:
                _harvest_sites(v, found)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str) and DOMAIN_RE.match(item):
                found.setdefault(item, None)
            else:
                _harvest_sites(item, found)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--url", default=os.environ.get("SEOGETS_MCP_URL", DEFAULT_URL))
    opts = ap.parse_args()

    api_key = os.environ.get("SEOGETS_API_KEY", "")
    if not api_key:
        die("missing_seogets_api_key", hint="Set SEOGETS_API_KEY env var.")

    day = today_utc()
    log("seogets_pull_start", day=day, url=opts.url, days=opts.days)

    summary: dict[str, Any] = {"day": day, "tools": [], "sites": [], "errors": []}
    calls = 0

    try:
        client = McpHttpClient(opts.url, api_key)
        server_info = client.initialize()
        tools = client.list_tools()
    except (httpx.HTTPError, McpError) as e:
        die("seogets_connect_error", error=str(e))

    _write(("seogets", "meta", "server", "catalog"), day, {
        "serverInfo": server_info,
        "tools": tools,
    })
    summary["tool_count"] = len(tools)
    summary["tools"] = [t.get("name") for t in tools]
    log("seogets_catalog", tool_count=len(tools), tools=summary["tools"])

    sites: dict[str, None] = {}

    # Pass 1 — everything callable with no site context.
    for tool in tools:
        name = tool.get("name") or ""
        site_param, args, fillable = _plan_args(tool, opts.days)
        if site_param is not None or not fillable:
            continue
        if calls >= MAX_CALLS:
            summary["errors"].append({"tool": name, "error": "dropped: MAX_CALLS"})
            continue
        calls += 1
        try:
            data = client.call_tool(name, args)
        except (httpx.HTTPError, McpError) as e:
            summary["errors"].append({"tool": name, "error": str(e)})
            continue
        _write(("seogets", "all", name, "result"), day, {"tool": name, "args": args, "data": data})
        _harvest_sites(data, sites)
        log("seogets_global_tool", tool=name)

    skipped = [s for s in sites if is_blacklisted(s)]
    for s in skipped:
        log("seogets_skip_blacklisted", site=s)
    site_list = [s for s in sites if not is_blacklisted(s)][:MAX_SITES]
    if len(sites) - len(skipped) > MAX_SITES:
        log("seogets_sites_capped", found=len(sites) - len(skipped), kept=MAX_SITES)
    summary["sites"] = site_list
    log("seogets_sites", count=len(site_list))

    # Pass 2 — per-site tools for every harvested site.
    for tool in tools:
        name = tool.get("name") or ""
        site_param, args, fillable = _plan_args(tool, opts.days)
        if site_param is None or not fillable:
            continue
        for site in site_list:
            if calls >= MAX_CALLS:
                summary["errors"].append({"tool": name, "site": site, "error": "dropped: MAX_CALLS"})
                continue
            calls += 1
            try:
                data = client.call_tool(name, {**args, site_param: site})
            except (httpx.HTTPError, McpError) as e:
                summary["errors"].append({"tool": name, "site": site, "error": str(e)})
                continue
            _write(("seogets", "sites", site, name), day, {
                "tool": name, "site": site, "args": args, "data": data,
            })
        log("seogets_site_tool_done", tool=name, sites=len(site_list))

    client.close()

    summary["call_count"] = calls
    summary["error_count"] = len(summary["errors"])
    summary_path("seogets", day).write_text(json.dumps(summary, indent=2, default=str))
    log(
        "seogets_pull_done",
        day=day,
        calls=calls,
        sites=len(site_list),
        errors=len(summary["errors"]),
        summary_path=str(summary_path("seogets", day)),
    )


if __name__ == "__main__":
    main()
