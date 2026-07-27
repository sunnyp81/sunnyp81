"""Daily digest + trend rollups over the hermes snapshot corpus.

Runs inside the workflow's commit step, AFTER today's fresh pulls have
been merged over the hermes-snapshots branch checkout — so it sees the
full day-partitioned history. Deliberately stdlib-only and standalone
(no config import): at that point in the job the working tree is the
snapshots branch, which contains no other hermes code.

Outputs, all inside the data dir so they ride along in the snapshot
commit:

  digest/YYYY-MM-DD.md      human one-pager: alerts first, then totals
  digest/YYYY-MM-DD.json    same, machine-readable
  trends/bing.csv           day,site,crawl_issues
  trends/seogets.csv        day,site,clicks,impressions,ctr,position
  trends/gsc.csv            day,account,site,sitemap_errors,sitemap_warnings

Alert rules (tuned for signal over noise):
  - Bing crawl issues increased on a site
  - SEO Gets 28d clicks dropped >=30% vs previous snapshot (min 10 clicks)
  - GSC sitemap errors appeared on a site that had none
  - A previously-seen site vanished from a service's pull
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

CLICK_DROP_PCT = 30
CLICK_DROP_MIN = 10


def days_of(service_dir: Path) -> list[str]:
    if not service_dir.is_dir():
        return []
    return sorted(d.name for d in service_dir.iterdir() if d.is_dir() and len(d.name) == 10)


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return None


# -- per-service extractors: {site: metrics} for one day -----------------


def bing_issues(data_dir: Path, day: str) -> dict[str, int]:
    s = load_json(data_dir / "bing" / day / "_summary.json") or {}
    out = {}
    for site in s.get("sites", []):
        if site.get("site"):
            out[site["site"]] = int(site.get("rows_crawl_issues", 0) or 0)
    return out


def seogets_perf(data_dir: Path, day: str) -> dict[str, dict]:
    """Parse each get_gsc_performance snapshot's TSV blob."""
    out = {}
    day_dir = data_dir / "seogets" / day
    if not day_dir.is_dir():
        return out
    for f in day_dir.glob("sites__*__get_gsc_performance.json"):
        doc = load_json(f) or {}
        site = doc.get("site")
        tsv = ((doc.get("data") or {}).get("data")) if isinstance(doc.get("data"), dict) else None
        if not site or not isinstance(tsv, str):
            continue
        lines = [l for l in tsv.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        nums = [x for x in lines[-1].split("\t") if x.strip() != ""]
        try:
            vals = [float(x) for x in nums]
        except ValueError:
            continue
        if len(vals) >= 4:
            out[site] = {
                "clicks": vals[0], "impressions": vals[1],
                "ctr": vals[2], "position": vals[3],
            }
    return out


def gsc_sitemap_errors(data_dir: Path, day: str) -> dict[str, dict]:
    s = load_json(data_dir / "gsc" / day / "_summary.json") or {}
    out = {}
    for acct_key, acct in (s.get("accounts") or {}).items():
        for site in acct.get("sites", []) or []:
            if site.get("site"):
                out[site["site"]] = {
                    "account": acct_key,
                    "sitemap_errors": int(site.get("sitemap_errors", 0) or 0),
                    "sitemap_warnings": int(site.get("sitemap_warnings", 0) or 0),
                }
    return out


# -- trends --------------------------------------------------------------


def upsert_trend(path: Path, header: list[str], day: str, rows: list[list]) -> None:
    """Idempotent per day: re-running replaces that day's rows."""
    path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[list[str]] = []
    if path.exists():
        with path.open() as f:
            r = list(csv.reader(f))
        existing = [row for row in r[1:] if row and row[0] != day]
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(existing)
        w.writerows(rows)


# -- digest --------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="Path to the hermes data dir")
    args = ap.parse_args()
    data_dir = Path(args.data)

    all_days = sorted(set(sum((days_of(data_dir / s) for s in ("bing", "seogets", "gsc", "ga4")), [])))
    if not all_days:
        print("digest: no data days found, nothing to do")
        return
    today = all_days[-1]
    prev = all_days[-2] if len(all_days) > 1 else None

    bing_now, bing_prev = bing_issues(data_dir, today), (bing_issues(data_dir, prev) if prev else {})
    sg_now, sg_prev = seogets_perf(data_dir, today), (seogets_perf(data_dir, prev) if prev else {})
    gsc_now, gsc_prev = gsc_sitemap_errors(data_dir, today), (gsc_sitemap_errors(data_dir, prev) if prev else {})

    alerts: list[str] = []
    notes: list[str] = []

    # Bing: crawl issues rising
    for site, n in sorted(bing_now.items(), key=lambda kv: -(kv[1] - bing_prev.get(kv[0], 0))):
        delta = n - bing_prev.get(site, 0)
        if prev and delta > 0:
            alerts.append(f"Bing crawl issues up on {site}: {bing_prev.get(site, 0)} -> {n} (+{delta})")

    # SEO Gets: click drops
    for site, m in sg_now.items():
        pm = sg_prev.get(site)
        if not pm:
            continue
        was, now = pm["clicks"], m["clicks"]
        if was >= CLICK_DROP_MIN and now < was * (1 - CLICK_DROP_PCT / 100):
            alerts.append(f"Clicks down {(1 - now / was) * 100:.0f}% on {site}: {was:.0f} -> {now:.0f} (28d window)")

    # GSC: new sitemap errors
    for site, m in gsc_now.items():
        prev_err = (gsc_prev.get(site) or {}).get("sitemap_errors", 0)
        if m["sitemap_errors"] > 0 and m["sitemap_errors"] > prev_err:
            alerts.append(f"GSC sitemap errors on {site}: {prev_err} -> {m['sitemap_errors']} ({m['account']})")

    # Vanished sites
    if prev:
        for label, now_set, prev_set in (
            ("Bing", set(bing_now), set(bing_prev)),
            ("SEO Gets", set(sg_now), set(sg_prev)),
        ):
            gone = sorted(prev_set - now_set)
            if gone and len(gone) <= 15:
                for site in gone:
                    notes.append(f"{label}: {site} missing from today's pull")
            elif gone:
                notes.append(f"{label}: {len(gone)} sites missing from today's pull")

    # Totals
    totals = {
        "bing_sites": len(bing_now),
        "bing_crawl_issues": sum(bing_now.values()),
        "seogets_sites": len(sg_now),
        "seogets_clicks_28d": round(sum(m["clicks"] for m in sg_now.values())),
        "gsc_sites": len(gsc_now),
        "gsc_sitemap_errors": sum(m["sitemap_errors"] for m in gsc_now.values()),
    }
    prev_totals = {
        "bing_crawl_issues": sum(bing_prev.values()) if prev else None,
        "seogets_clicks_28d": round(sum(m["clicks"] for m in sg_prev.values())) if prev else None,
        "gsc_sitemap_errors": sum(m["sitemap_errors"] for m in gsc_prev.values()) if prev else None,
    }

    # Trends
    upsert_trend(data_dir / "trends" / "bing.csv", ["day", "site", "crawl_issues"], today,
                 [[today, s, n] for s, n in sorted(bing_now.items())])
    upsert_trend(data_dir / "trends" / "seogets.csv",
                 ["day", "site", "clicks", "impressions", "ctr", "position"], today,
                 [[today, s, m["clicks"], m["impressions"], m["ctr"], m["position"]]
                  for s, m in sorted(sg_now.items())])
    upsert_trend(data_dir / "trends" / "gsc.csv",
                 ["day", "account", "site", "sitemap_errors", "sitemap_warnings"], today,
                 [[today, m["account"], s, m["sitemap_errors"], m["sitemap_warnings"]]
                  for s, m in sorted(gsc_now.items())])

    # Markdown
    lines = [f"# Hermes digest — {today}", ""]
    if not prev:
        lines += ["_First snapshot day — no comparison baseline yet._", ""]
    if alerts:
        lines += ["## 🚨 Alerts", ""] + [f"- {a}" for a in alerts] + [""]
    else:
        lines += ["## Alerts", "", "- Nothing tripped today.", ""]
    if notes:
        lines += ["## Notes", ""] + [f"- {n}" for n in notes] + [""]
    lines += ["## Totals", "", "| metric | previous | today |", "|---|---|---|"]
    for key, label in (
        ("bing_crawl_issues", "Bing crawl issues"),
        ("seogets_clicks_28d", "SEO Gets clicks (28d, all sites)"),
        ("gsc_sitemap_errors", "GSC sitemap errors"),
    ):
        p = prev_totals.get(key)
        lines.append(f"| {label} | {p if p is not None else '—'} | {totals[key]} |")
    lines += ["", f"Sites covered: Bing {totals['bing_sites']}, SEO Gets {totals['seogets_sites']}, GSC {totals['gsc_sites']}.", ""]

    digest_dir = data_dir / "digest"
    digest_dir.mkdir(parents=True, exist_ok=True)
    (digest_dir / f"{today}.md").write_text("\n".join(lines))
    (digest_dir / f"{today}.json").write_text(json.dumps({
        "day": today, "previous_day": prev, "alerts": alerts, "notes": notes,
        "totals": totals, "previous_totals": prev_totals,
    }, indent=2))

    print(f"digest: {len(alerts)} alert(s), {len(notes)} note(s) -> digest/{today}.md")


if __name__ == "__main__":
    main()
