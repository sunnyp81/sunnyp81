"""Daily Bing Webmaster snapshot puller.

Single account (Bing Webmaster API is keyed, not OAuth). For every
verified site:
  - page stats
  - query stats
  - crawl issues
  - rank + traffic stats

Writes JSON snapshots under data/bing/YYYY-MM-DD/. Emits _summary.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import BING_API_KEY
from shared.logging import die, log
from shared.paths import snapshot_path, summary_path, today_utc

BASE = "https://ssl.bing.com/webmaster/api.svc/json"


def _get(client: httpx.Client, path: str, params: dict | None = None):
    p = {"apikey": BING_API_KEY, **(params or {})}
    r = client.get(f"{BASE}/{path}", params=p, timeout=30.0)
    r.raise_for_status()
    return r.json().get("d")


def _write(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, default=str))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.parse_args()

    if not BING_API_KEY:
        die("missing_bing_api_key", hint="Set BING_API_KEY env var.")

    day = today_utc()
    log("bing_pull_start", day=day)

    account_key = "bing"
    summary: dict = {"day": day, "sites": []}

    with httpx.Client() as client:
        try:
            sites = _get(client, "GetUserSites") or []
        except httpx.HTTPError as e:
            die("bing_list_sites_error", error=str(e))

        for s in sites:
            site_url = s.get("Url") or s.get("SiteUrl")
            if not site_url:
                continue
            log("bing_pull_site", site=site_url)
            per_site: dict = {"site": site_url}
            for report, path in [
                ("page_stats", "GetPageStats"),
                ("query_stats", "GetQueryStats"),
                ("crawl_issues", "GetCrawlIssues"),
                ("crawl_stats", "GetCrawlStats"),
                ("rank_traffic", "GetRankAndTrafficStats"),
                ("quota", "GetUrlSubmissionQuota"),
            ]:
                try:
                    resp = _get(client, path, {"siteUrl": site_url}) or []
                    _write(snapshot_path("bing", account_key, site_url, report, day), {"data": resp})
                    per_site[f"rows_{report}"] = len(resp) if isinstance(resp, list) else 1
                except httpx.HTTPError as e:
                    per_site[f"{report}_error"] = str(e)
            summary["sites"].append(per_site)

    summary["site_count"] = len(summary["sites"])
    summary["total_crawl_issues"] = sum(s.get("rows_crawl_issues", 0) for s in summary["sites"])
    summary_path("bing", day).write_text(json.dumps(summary, indent=2, default=str))
    log("bing_pull_done", day=day, summary_path=str(summary_path("bing", day)))


if __name__ == "__main__":
    main()
