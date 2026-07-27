"""Daily GSC snapshot puller.

For each account:
  - list all verified sites
  - for each site:
      - list sitemaps (captures errors + warnings)
      - search_analytics(last 28 days, per-page + per-query top rows)
      - (optional) URL Inspection on the top N declining URLs

Writes JSON snapshots under data/gsc/YYYY-MM-DD/. Emits a _summary.json.
Safe to re-run; overwrites the day's files.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

# Allow running as `python pullers/gsc_pull.py` from repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from googleapiclient.errors import HttpError

from config import ACCOUNTS, GSC_SCOPES, Account, is_blacklisted
from shared.google_auth import build_service
from shared.logging import die, log
from shared.paths import snapshot_path, summary_path, today_utc


def _svc(account: Account):
    try:
        return build_service(account, "gsc", "searchconsole", "v1", GSC_SCOPES)
    except RuntimeError as e:
        die("missing_creds", account=account.key, error=str(e))


def _write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, default=str))


def _pull_site(svc, account: Account, site_url: str, days: int, day: str) -> dict:
    stats: dict = {"account": account.key, "site": site_url}

    try:
        sitemaps = svc.sitemaps().list(siteUrl=site_url).execute().get("sitemap", [])
    except HttpError as e:
        stats["sitemaps_error"] = str(e)
        sitemaps = []
    stats["sitemap_count"] = len(sitemaps)
    stats["sitemap_errors"] = sum(int(s.get("errors", 0) or 0) for s in sitemaps)
    stats["sitemap_warnings"] = sum(int(s.get("warnings", 0) or 0) for s in sitemaps)
    _write(snapshot_path("gsc", account.key, site_url, "sitemaps", day), {"sitemaps": sitemaps})

    end = date.today()
    start = end - timedelta(days=days)
    body = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "rowLimit": 1000,
        "type": "web",
    }
    for report, dims in [
        ("query", ["query"]),
        ("page", ["page"]),
        ("country", ["country"]),
        ("device", ["device"]),
        ("date", ["date"]),
    ]:
        try:
            resp = (
                svc.searchanalytics()
                .query(siteUrl=site_url, body={**body, "dimensions": dims})
                .execute()
            )
            _write(snapshot_path("gsc", account.key, site_url, f"searchanalytics_{report}", day), resp)
            stats[f"rows_{report}"] = len(resp.get("rows", []))
        except HttpError as e:
            stats[f"searchanalytics_{report}_error"] = str(e)

    return stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--account", help="Only run for this account key (default: all)")
    args = ap.parse_args()

    day = today_utc()
    accounts = [a for a in ACCOUNTS if not args.account or a.key == args.account]
    log("gsc_pull_start", day=day, accounts=[a.key for a in accounts])

    summary = {"day": day, "accounts": {}}
    for account in accounts:
        try:
            svc = _svc(account)
            sites = svc.sites().list().execute().get("siteEntry", [])
        except HttpError as e:
            log("gsc_list_sites_error", account=account.key, error=str(e))
            summary["accounts"][account.key] = {"error": str(e)}
            continue

        per_site = []
        for entry in sites:
            site_url = entry.get("siteUrl")
            if not site_url:
                continue
            if entry.get("permissionLevel") == "siteUnverifiedUser":
                continue
            if is_blacklisted(site_url):
                log("gsc_skip_blacklisted", account=account.key, site=site_url)
                continue
            log("gsc_pull_site", account=account.key, site=site_url)
            per_site.append(_pull_site(svc, account, site_url, args.days, day))

        summary["accounts"][account.key] = {
            "email": account.email,
            "site_count": len(per_site),
            "total_sitemap_errors": sum(s.get("sitemap_errors", 0) for s in per_site),
            "total_sitemap_warnings": sum(s.get("sitemap_warnings", 0) for s in per_site),
            "sites": per_site,
        }

    summary_path("gsc", day).write_text(json.dumps(summary, indent=2, default=str))
    log("gsc_pull_done", day=day, summary_path=str(summary_path("gsc", day)))


if __name__ == "__main__":
    main()
