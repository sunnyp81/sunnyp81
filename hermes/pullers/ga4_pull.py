"""Daily GA4 snapshot puller.

For each account:
  - list account summaries (accounts + property summaries)
  - for each property:
      - core traffic report (sessions/activeUsers/engagementRate by pagePath)
      - country breakdown
      - source/medium breakdown
      - date time series
      - conversions if configured

Writes JSON snapshots under data/ga4/YYYY-MM-DD/. Emits _summary.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from googleapiclient.errors import HttpError

from config import ACCOUNTS, GA4_SCOPES, Account
from shared.google_auth import build_service
from shared.logging import log
from shared.paths import snapshot_path, summary_path, today_utc


REPORTS = [
    ("traffic", ["pagePath"], ["sessions", "activeUsers", "engagementRate"]),
    ("country", ["country"], ["sessions", "activeUsers"]),
    ("source_medium", ["sessionSourceMedium"], ["sessions", "activeUsers"]),
    ("date", ["date"], ["sessions", "activeUsers", "engagementRate"]),
    ("conversions", ["eventName"], ["conversions", "eventCount"]),
]


def _services(account: Account):
    # Raise, don't die(): sys.exit skips the caller's per-account
    # isolation and takes the other account (and _summary.json) with it.
    data = build_service(account, "ga4", "analyticsdata", "v1beta", GA4_SCOPES)
    admin = build_service(account, "ga4", "analyticsadmin", "v1beta", GA4_SCOPES)
    return data, admin


def _write(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, default=str))


def _pull_property(data, account: Account, property_name: str, days: int, day: str) -> dict:
    stats: dict = {"account": account.key, "property": property_name}
    body_base = {
        "dateRanges": [{"startDate": f"{days}daysAgo", "endDate": "today"}],
        "limit": 1000,
    }
    for report, dims, metrics in REPORTS:
        try:
            resp = (
                data.properties()
                .runReport(
                    property=property_name,
                    body={
                        **body_base,
                        "dimensions": [{"name": d} for d in dims],
                        "metrics": [{"name": m} for m in metrics],
                    },
                )
                .execute()
            )
            _write(snapshot_path("ga4", account.key, property_name, report, day), resp)
            stats[f"rows_{report}"] = len(resp.get("rows", []))
        except HttpError as e:
            stats[f"{report}_error"] = str(e)
    return stats


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--account", help="Only run for this account key (default: all)")
    args = ap.parse_args()

    day = today_utc()
    accounts = [a for a in ACCOUNTS if not args.account or a.key == args.account]
    log("ga4_pull_start", day=day, accounts=[a.key for a in accounts])

    summary = {"day": day, "accounts": {}}
    for account in accounts:
        try:
            data, admin = _services(account)
            summaries = (
                admin.accountSummaries().list().execute().get("accountSummaries", [])
            )
        except Exception as e:  # bad/expired token must not kill other accounts
            log("ga4_list_accounts_error", account=account.key, error=str(e))
            summary["accounts"][account.key] = {"error": str(e)}
            continue

        properties: list[dict] = []
        for a in summaries:
            for p in a.get("propertySummaries", []) or []:
                name = p.get("property")
                if not name:
                    continue
                log("ga4_pull_property", account=account.key, property=name)
                stats = _pull_property(data, account, name, args.days, day)
                stats["displayName"] = p.get("displayName")
                properties.append(stats)

        summary["accounts"][account.key] = {
            "email": account.email,
            "property_count": len(properties),
            "properties": properties,
        }

    summary_path("ga4", day).write_text(json.dumps(summary, indent=2, default=str))
    log("ga4_pull_done", day=day, summary_path=str(summary_path("ga4", day)))


if __name__ == "__main__":
    main()
