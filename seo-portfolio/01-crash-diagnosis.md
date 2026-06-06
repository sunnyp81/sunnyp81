# Task 1 — Diagnosis: The May 2026 Traffic Crash & Recovery

_Prepared 2026-06-06. Data sources: `organic_visibility_summary.csv`, `organic_visibility_dead_pages.csv`, `organic_visibility_decays.csv` (GSC exports). The 28-day snapshot was taken ~May 17–22 2026; a separate Apr 3 – Jun 5 dashboard shows partial recovery._

## Summary

The portfolio suffered a sharp, mid-May 2026 visibility crash concentrated on a handful of sites, with the two flagship victims (`carehome.page`, `wagearea.com`) losing ~99% of clicks and impressions, then partially recovering by early June. The timing is an almost exact match for the **Google May 2026 Core Update**, which Google confirmed rolled out **May 21 → June 2, 2026**, with peak SERP volatility on **May 23 and May 30–31** ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119), [Search Engine Journal](https://www.searchenginejournal.com/googles-may-core-update-complete-after-volatile-rollout/577704/)).

**Lead hypothesis (high confidence): the crash is the live rollout of the May 2026 core update, captured mid-flight by a snapshot taken during the most volatile window; the "recovery" is normal post-rollout settling.** Two secondary factors plausibly amplify or distort the picture: (a) the lost `sunnyshares.com@gmail.com` Google account disconnecting GSC properties so some sites under-report or stop receiving fresh indexing/coverage signals, and (b) known GSC reporting bugs in May 2026 that depressed impressions/Discover metrics. The deepest single-page evidence — pages that previously ranked position < 5 with double-digit CTR vanishing to zero clicks — is consistent with a re-evaluation/quality event rather than a slow content decay.

**Important caveat on the data window:** Google explicitly advised that **June 9 is the earliest "clean" comparison window** in Search Console because of rollout volatility ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119)). The May 17–22 snapshot sits squarely inside the noisiest period, so the magnitude of the recorded drops is likely overstated versus the settled state. Treat absolute crash numbers as a worst-case mid-rollout reading, not a final verdict.

---

## Sites Hit

All sites in the summary with `click_delta_pct <= -0.5` **OR** `impression_delta_pct <= -0.5`, ranked by absolute clicks lost (`prev_clicks_28d − clicks_28d`). "Recovered?" reflects the June dashboard signal noted in the brief (only carehome and wagearea were independently confirmed there; others are inferred/unknown).

| Site | Prev clicks | Now clicks | Clicks lost | Click % drop | Impr % drop | Tier | Recovered? |
|---|---|---|---|---|---|---|---|
| carehome.page | 533 | 2 | 531 | -99.6% | -99.3% | T2 | Y (~307 clicks per June dashboard) |
| signalcheck.org | 65 | 7 | 58 | -89.2% | -59.8% | T4 | Unknown |
| wagearea.com | 38 | 0 | 38 | -100% | -99.0% | T4 | Y (~14 clicks per June dashboard) |
| radon.tips | 37 | 0 | 37 | -100% | -98.2% | T4 | Unknown |
| gathrd.co.uk | 7 | 2 | 5 | -71.4% | -60.6% | T4 | Unknown |
| auditweb.site | 1 | 0 | 1 | -100% | -57.9% | T4 | Unknown |
| postcode.page | 1 | 0 | 1 | -100% | -96.8% | T4 | Unknown |
| punchfoods.com | 0 | 0 | 0 | n/a (0→0) | -77.9% | T4 | Unknown |
| generator.express | 0 | 0 | 0 | n/a (0→0) | -96.6% | T4 | Unknown |
| text.taxi | 0 | 0 | 0 | n/a (0→0) | -89.7% | T4 | Unknown |
| clinicaltrialhub.org | 1 | 1 | 0 | +0% clicks | -51.6% | T4 | Unknown |
| thetutor.link | 2 | 6 | -4 (gained) | +200% clicks | -51.7% | T4 | n/a (impr-only drop) |

Notes:
- **carehome.page is by far the most material loss** (531 clicks, a T2 property; prev 198,038 impressions → 1,413). Everything else is small in absolute terms.
- `signalcheck.org`, `radon.tips`, `wagearea.com` are the next clearest full collapses but are all low-traffic T4 sites.
- The "0→0 clicks, large impression drop" group (`punchfoods`, `generator.express`, `text.taxi`, `clinicaltrialhub`) are tiny sites where the impression decline is real but click impact is negligible — likely the same algorithmic pullback at the bottom of the long tail.
- `formhq.org` was **not** included: its impressions actually rose (+56.6%); its only red flag is a large negative `position_delta` (-57.9), so it is a position-only shuffle, not a crash.

---

## Page-Level Evidence

### Dead pages (lost all clicks) — the "vanished from a strong position" signal

These are the highest-confidence indicators of a quality/re-ranking event rather than gradual decay, because they previously ranked **position < 5** and/or had **CTR > 10%** and dropped to zero:

| Site | Page | Prev pos | Prev CTR | Prev clicks → now |
|---|---|---|---|---|
| carehome.page | /care-home/beaconsfield-house-weston-super-mare/ | **2.6** | **33.3%** | 15 → 0 |
| carehome.page | /care-home/northway-lodge-guildford/ | **3.86** | **22.7%** | 22 → 0 |
| carehome.page | /care-home/pendale-lodge-york/ | **4.32** | **20.0%** | 25 → 0 |
| wagearea.com | / (homepage) | **1.67** | **15.2%** | 33 → 0 |
| shecookssheeats.co.uk | /syns-tesco-sandwiches/ | 16.16 | 5.8% | 6 → 0 |
| shecookssheeats.co.uk | /syns-bounty/ | 9.08 | 2.7% | 6 → 0 |
| sunnypatel.co.uk | /blog/seo-statistics-uk | 8.99 | 0.6% | 6 → 0 |
| catchment.school | /school/st-bartholomews-school-137465/ | 5.25 | 9.4% | 6 → 0 |
| redlighttherapy.expert | /lightstim-review/ | 16.43 | 0.9% | 5 → 0 |

The **carehome.page and wagearea.com pages losing position 1.6–4.3 rankings with 15–33% CTR is the single strongest piece of evidence.** Losing top-of-page-1 placements with very high CTR overnight is the classic fingerprint of an algorithmic quality re-assessment (or a coverage/indexing break), not slow content rot. Note these are **deep programmatic detail pages** (individual care homes, a homepage) — exactly the page type core updates target when they re-evaluate "helpful, people-first" thin/templated content at scale.

### Decaying pages — partial declines, consistent with the same event

The decays file shows the same sites bleeding rank across many pages rather than a single URL problem:
- **shecookssheeats.co.uk**: ~16 "syns-*" pages each dropping ~50–87% of clicks, prev positions clustered 5–10 (e.g. `/pizza-express-syns/` 9.4→11.4, clicks 10→3, -70%). This is broad, site-wide erosion of a programmatic content set — a hallmark of a core-update hit, though note its summary row is only -20% clicks overall (state already flagged `recovery`).
- **redlighttherapy.expert**: `/ihome-mask-review/` 74→29 clicks (-61%), `/best-red-light-therapy-wraps/` 19→10 (-47%) — review pages losing roughly half their clicks while positions held steady (7.3, 9.0), meaning the loss is impression/visibility-driven, again consistent with a SERP-feature/core reshuffle.
- **catchment.school**: several council/area/school pages down 32–55% from prev positions 3–8 — but its summary row is strongly **positive** overall (+110% clicks, 1,945→4,091), so this site is a **net winner** of the update with a few losing pages. Good counter-evidence that the event was algorithmic and bidirectional, not a portfolio-wide technical outage.

### Cross-check: clear winners exist in the same snapshot

`catchment.school` (+110% clicks), `waterhard.uk` (+71%), `nomadranker.com` (+206%), `chargefinder.uk` (+45x), `tradecost.uk` (new traffic) all grew in the same window. **A portfolio-wide technical failure (hosting/robots/account) would not produce big winners alongside the losers.** This pattern of simultaneous winners and losers is the textbook signature of a core algorithm update.

---

## Hypotheses (ranked, with confidence)

### H1 — May 2026 Core Update rollout, captured mid-flight (Confidence: HIGH)
Google confirmed the **May 2026 Core Update ran May 21 → June 2, 2026**, its second core update of the year, with peak volatility May 23 and May 30–31 ([Search Engine Land](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119); [Search Engine Journal](https://www.searchenginejournal.com/googles-may-core-update-complete-after-volatile-rollout/577704/)). This matches the crash-then-recover shape exactly: the May 17–22 snapshot caught the rollout as it began thrashing rankings; the early-June dashboard shows settling. The presence of both severe losers and strong winners in the same snapshot, the bidirectional page-level moves, and the hit landing on deep programmatic/thin-template pages all support this. **This is the primary explanation.** Verified: the update is real and confirmed by Google. Unverified: that these specific sites were demoted *on merit* vs. caught in transient volatility — Google's own guidance says wait until **June 9** for a clean read.

### H2 — Lost `sunnyshares.com@gmail.com` account degrading GSC/indexing signals for affected properties (Confidence: MEDIUM)
The owner lost access to a Google account, disconnecting some GSC properties. If `carehome.page`/`wagearea.com` were verified under that account, the consequences could include: stale/halted coverage and indexing-status feedback, no ability to request indexing or fix coverage issues, and lapsed sitemap processing. This would not by itself remove rankings (verification ≠ ranking), but it would (a) blind the owner to the real cause and (b) let indexing/coverage regressions go unfixed during the volatile window, deepening and prolonging the dip. **Cannot be verified from the CSVs** — the data does not record which account verifies each property. Worth noting: every property shows `sitemap_indexed = 0` and `sitemap_index_rate = 0` across the *entire* portfolio, which is suspicious and could indicate a sitemap/coverage reporting break tied to account or a GSC quirk (see H4). This is the most actionable lever even if it is not the root cause.

### H3 — Thin / programmatic-content classification (overlaps H1) (Confidence: MEDIUM)
The worst-hit sites are large programmatic builds: `carehome.page` (302 indexed pages, one care home per page), `wagearea.com` (salary-by-area), `catchment.school` (school catchments). Core updates explicitly target scaled, low-differentiation content. The fact that `carehome.page` had a high page count but `queries_per_page` of only 0.65 (thin demand per page) fits a thin-content demotion. This is really a *mechanism* under H1 rather than an independent cause, hence not ranked higher. Verified: page structure from the data. Unverified: that Google classified it as thin (no manual-action data available).

### H4 — Known May 2026 GSC reporting bugs inflating the apparent drop (Confidence: LOW–MEDIUM, partial)
Google had multiple Search Console data issues in this window: a year-long impressions logging bug (May 2025–Apr 27 2026, fixed forward-only) and a **Discover reporting bug that decreased clicks/impressions for May 21, 2026** ([Search Engine Land](https://searchengineland.com/google-discover-performance-reporting-bug-in-search-console-477230)). These affect *reported* metrics, not real rankings, and could make the snapshot's drop look worse than reality — partly explaining the "recovery" (data correcting, not traffic returning). It does **not** explain the page-level position drops (a bug wouldn't move a page from position 2 to gone). So at most a distortion amplifier, not the cause.

### Ruled down: Manual action / penalty (Confidence: LOW)
No manual-action data is in the CSVs, and the simultaneous-winners pattern + confirmed core update make a manual penalty unlikely. **Unverifiable from the data — must be checked directly in GSC > Security & Manual Actions.** Cannot be excluded, only deprioritized.

---

## Recovery Checklist (prioritized)

**Priority 0 — Regain control (do first; unblocks everything else)**
1. **Recover the `sunnyshares.com@gmail.com` Google account** via Google Account Recovery (account recovery form, recovery email/phone, prior passwords). If unrecoverable, **re-verify every affected GSC property under an account you control** (DNS TXT / domain verification is best for `sc-domain:` properties so it survives future account loss). Add a second owner/email to every property now to prevent recurrence.
2. Inventory which properties were verified under the lost account vs. which you still control — start with `carehome.page` and `wagearea.com`.

**Priority 1 — Confirm the cause before acting (avoid over-reacting to volatility)**
3. **Do not draw final conclusions until June 9+** (Google's stated clean-comparison date). Pull a fresh GSC Performance report comparing a post-June-2 week to a pre-May-21 baseline; compare by page, query, country, device, and search type rather than single days.
4. In GSC, check **Security & Manual Actions → Manual actions** for `carehome.page` and every hit site (rules out H-penalty definitively).
5. Check **Performance → Search type = Discover** separately to isolate any Discover-bug distortion (H4).

**Priority 2 — Indexing / coverage diagnostics on the worst-hit pages**
6. Run **URL Inspection** on the specific dead pages with the strongest prior rankings:
   - `carehome.page/care-home/beaconsfield-house-weston-super-mare/` (was pos 2.6, 33% CTR)
   - `carehome.page/care-home/northway-lodge-guildford/` (pos 3.86)
   - `carehome.page/care-home/pendale-lodge-york/` (pos 4.32)
   - `wagearea.com/` (homepage, pos 1.67)
   Confirm: indexed status, canonical, last crawl date, "Page is indexed" vs "Crawled – currently not indexed"/"Discovered – not indexed". A coverage state change here points to indexing breakage (H2); "indexed but not ranking" points to algorithmic demotion (H1/H3).
7. Review **Indexing → Pages (Coverage)** for trend changes in "Indexed" counts around mid-May, especially for `carehome.page` (302 pages) and `radon.tips`/`signalcheck.org`.

**Priority 3 — Sitemaps & technical hygiene**
8. The data shows `sitemap_indexed = 0` / `sitemap_index_rate = 0` for the *entire portfolio* — investigate whether this is a real sitemap-processing failure or just a reporting gap. **Re-submit sitemaps** for all hit sites and confirm Google reports them as "Success" with non-zero discovered/indexed URLs.
9. Verify `robots.txt` and `<meta robots>` on hit sites are not blocking/`noindex` (quick regression check; cheap to rule out a technical cause).
10. Confirm hosting/uptime and `Settings → Crawl stats` show no spike in server errors or crawl-rate collapse mid-May.

**Priority 4 — Content remediation (only if H1/H3 confirmed after June 9)**
11. For confirmed core-update losers (`carehome.page`, `wagearea.com`, `radon.tips`, `signalcheck.org`): apply Google's core-update recovery guidance — improve depth/uniqueness/E-E-A-T on the thin programmatic templates, consolidate near-duplicate detail pages, and add genuine differentiating value per page (`carehome.page` has 0.65 queries/page, a thin-demand signal).
12. Track `last7_clicks` vs `prev7_clicks` weekly as the leading recovery indicator (e.g. carehome currently 0/0 last7 in-snapshot; expect this to climb as June data settles, consistent with the dashboard's ~307-click recovery).

**Priority 5 — Resilience**
13. Add redundant GSC ownership + Bing Webmaster Tools; export GSC data on a schedule so future account loss does not blind you; set up alerting on >50% week-over-week click drops per property.

---

### Confidence & unverifiable items recap
- **Verified:** May 2026 Core Update existence, dates (May 21–Jun 2), peak volatility days, and the May 2026 GSC/Discover reporting bugs (all cited above). All click/impression/position numbers quoted are directly from the provided CSVs.
- **Inferred from data:** which sites were hit and their page-level before/after states; the winners-and-losers bidirectional pattern.
- **Unverifiable from the supplied data:** whether a manual action exists; whether the lost account verified the hit properties; whether the sitemap `index_rate = 0` is a real failure or reporting artifact; the *settled* (post-June-9) magnitude of each drop. These require live GSC access and are the first things the checklist resolves.

#### Sources
- [Search Engine Land — May 2026 core update rollout complete](https://searchengineland.com/google-may-2026-core-update-rollout-is-now-complete-479119)
- [Search Engine Journal — May core update complete after volatile rollout](https://www.searchenginejournal.com/googles-may-core-update-complete-after-volatile-rollout/577704/)
- [Search Engine Roundtable — May core update volatility June 2nd](https://www.seroundtable.com/google-may-core-update-volatility-41434.html)
- [Search Engine Land — Discover performance reporting bug in Search Console](https://searchengineland.com/google-discover-performance-reporting-bug-in-search-console-477230)
- [Search Engine Land — Google fixes Search Console's year-long data logging issue](https://searchengineland.com/google-fixes-search-consoles-year-long-data-logging-issue-well-kind-of-476442)
