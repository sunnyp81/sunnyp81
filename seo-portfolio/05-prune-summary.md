# Task 5 — Prune the Dead-Weight (T4 / Low-Visibility Sites)

Snapshot: ~May 17-22 2026 | Generated 2026-06-06
Source: organic_visibility_summary.csv (file_id 1al1-QlBd4BtrEhXde8yHpx-X7qFIxmga)

## Decision counts

| Decision | Count |
|----------|-------|
| CUT | 22 |
| CONSOLIDATE / MERGE | 1 |
| KEEP (WATCH) | 4 |
| **Total weak sites reviewed** | **27** |

Weak = status == "low_visibility" OR (clicks_28d < 5 AND impressions_28d < 500 AND visibility_score < 30).
Cutting 22 sites removes the same number of annual domain renewals (and any associated hosting) and de-clutters GSC/reporting so attention concentrates on the T1-T3 growers.

## Duplicate GSC properties (call-out)

Only one duplicate property was found across all rows:

- **sc-domain:towrating.org** is shared by TWO site rows: **towrating.org** and **towrating.net**.
  - Both are completely dead (0 pages / 0 impressions / 0 queries). The .net is redundant by definition — it reports against the .org property.
  - Action: keep ONE domain (towrating.org as canonical), 301-redirect towrating.net to it, then drop the .net registration. Since the .org itself has shipped no content, it is also a CUT candidate unless content is imminent.

No other gsc_property value appears on more than one site row.

## CUT list (22) — one-line reasons

- techloved.com (T2) — 0 clicks, impressions falling, 41 pages but no query traction; saturated tech-review niche.
- aifor.tech (T3) — 2 pages / 2 queries / 15 imp; essentially empty.
- towrating.org (T3) — canonical of the towrating pair but 0 pages / 0 imp; nothing shipped.
- aifor.property (T4) — 2 pages, 52 imp, 0 clicks; thin tool, no traction.
- areaiq.uk (T4) — 1 page, 11 imp, 0 clicks.
- auditweb.site (T4) — 1 page, imp -58%, 0 clicks.
- carrecallhq.com (T4) — 6 pages, 14 imp declining, 0 clicks; OEM/gov-dominated niche.
- claimwatt.com (T4) — 1 page, 1 imp, 0 queries; no content.
- clinicaltrialhub.org (T4) — imp -52%, weak YMYL niche lacking E-E-A-T.
- fixerror.dev (T4) — 1 page, 6 imp, 0 clicks.
- formhq.org (T4) — 24 pages but 2 queries, position delta -57.9 (ranking deteriorating).
- generator.express (T4) — imp -97%, 0 queries; dead.
- mobileautomechanic.uk (T4) — 1 page, 17 imp; no depth for a local-service play.
- postcode.page (T4) — 39 pages but imp -97%, ranking lost; giant-dominated niche.
- punchfoods.com (T4) — 21 pages, imp -78%, 0 clicks; saturated calorie niche.
- radon.tips (T4) — imp -98% (3912 to 69); lost prior ranking, no recovery.
- scopepitch.com (T4) — 4 pages, imp -81%, 0 clicks.
- template.how (T4) — 1 page, 0 queries, 3 imp.
- text.taxi (T4) — 2 pages, imp -90%, 0 clicks.
- wagearea.com (T4) — 159 queries but imp -99%, position -19; likely deindexed/penalized.
- zoningbase.com (T4) — 1 page, 0 queries, 8 imp.
- merch.observer (T4) — 0 pages / 0 imp / no sitemap; never launched.

## CONSOLIDATE list (1)

- **towrating.net → towrating.org** — duplicate domain on the same GSC property; 301-redirect and drop the .net. Keep towrating.org as the canonical domain.

## KEEP (WATCH) list (4) — the signal that earns runway

- **bookkeepingflow.com** — 92 pages indexed at scale with impressions **+694%** (254 vs 32) and 10 queries forming. Runway: re-evaluate in 90 days.
- **breedhealth.org** — 448 pages, 59 queries, 1205 imp with **+73%** impression growth; ranking maturing. Runway: re-evaluate in 90 days.
- **checkamover.com** — impressions **+85%** (475 vs 257), 9 queries across 20 pages; clean upward trend. Runway: re-evaluate in 90 days.
- **complain.report** — impressions **+30%** (209 vs 161), 12 queries on only 8 pages (good queries/page efficiency). Runway: re-evaluate in 90 days.

## What to do operationally

- **Let expire (no redirect):** domains with no content and no inbound equity — aifor.tech, areaiq.uk, claimwatt.com, fixerror.dev, generator.express, template.how, text.taxi, zoningbase.com, aifor.property, mobileautomechanic.uk, carrecallhq.com, merch.observer, scopepitch.com. Simply do not renew; nothing of value is lost and there is no link equity to preserve.
- **Redirect (301):** towrating.net to towrating.org. Use 301 where a same-topic stronger sibling exists; none of the other CUTs has a relevant sibling to absorb them, so redirects elsewhere are not warranted.
- **noindex first, then expire:** sites that DID rank and may still leak crawl budget / brand confusion — wagearea.com, postcode.page, radon.tips, punchfoods.com, formhq.org, clinicaltrialhub.org, techloved.com. Add `noindex` (or remove from sitemap and 410 the pages) to cleanly drop them from the index, confirm de-indexing in GSC, then let the domain lapse at renewal. wagearea.com specifically warrants a quick manual-action / deindex check before discarding, given its -99% impression cliff.
- **Watch bucket:** leave the 4 KEEP sites untouched, set a 90-day calendar review, and at that point promote (invest) or demote to CUT based on whether clicks materialize.
