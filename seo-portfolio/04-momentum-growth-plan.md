# Task 4 — Feed the Momentum Sites (Growth Plan)

Snapshot: ~17–22 May 2026 (28-day window). Prepared 2026-06-06.
Data: `organic_visibility_summary.csv`, `organic_visibility_ctr_opportunities.csv` (Google Drive).

## How the momentum set was identified

Programmatic rule: include a site if `status == "growing"` **OR** (`click_delta_pct >= 0.30` **AND** `clicks_28d >= 20`).

Result: **7 sites**, all of which carry `status == "growing"`. No "non-growing but high-delta" site cleared the clicks>=20 floor.

| Rank | Site | Clicks 28d | Δ clicks | Impr 28d | CTR | Avg pos | Brand share | Pages |
|---|---|---|---|---|---|---|---|---|
| 1 | catchment.school | 4,091 | +110% | 121,497 | 3.37% | 9.2 | 85% | 500 |
| 2 | waterhard.uk | 1,013 | +71% | 56,465 | 1.79% | 8.0 | 78% | 500 |
| 3 | deadhangs.com | 411 | +33% | 34,151 | 1.20% | 7.5 | 3% | 17 |
| 4 | chargefinder.uk | 92 | +4,500% (+45x) | 4,693 | 1.96% | 29.0 | 80% | 500 |
| 5 | nomadranker.com | 69 | +306% (+3x) | 38,499 | 0.18% | 11.6 | 0% | 500 |
| 6 | heatpumpchecker.co.uk | 48 | +100% | 13,502 | 0.36% | 25.3 | 0% | 500 |
| 7 | solarhq.uk | 27 | +145% | 18,328 | 0.15% | 44.5 | 0% | 500 |

Borderline (noted, not core): **drugnote.com** — 23 clicks, prev_clicks = 0 so `click_delta_pct` is undefined (shows as blank/infinite), status "visible". A genuine emerging site (impressions 12,859, +4,285%) but too raw and high-position (51.6) to be a "feed the winner" target this cycle. **redlighttherapy.expert** was explicitly excluded: clicks −25.5%, it is declining, not momentum.

---

## Where to invest next (ranked by incremental clicks per unit effort)

The biggest, fastest incremental clicks come from sites that **already convert impressions to clicks** and have a **large untapped impression base sitting on page 1–2**. Use that lens, not raw growth %.

1. **waterhard.uk — #1 priority.** It already ranks page-1 (avg pos 8.0) across a huge programmatic estate, but **78% of clicks are brand**. The CTR-opportunity file shows ~60 non-brand region/company/area pages at positions 5–8 capturing only 1–9 clicks each against 100–5,060 impressions. These are page-1 positions leaking clicks. A title/meta + internal-link pass here is the single highest-yield move: real non-brand demand, already-ranking pages, double-digit "potential_clicks" on dozens of URLs (e.g. /water-company/thames-water/ shows potential_clicks 132.8 vs 19 actual; /region/london/ 76.9 vs 28). Estimated capture: **+150–300 non-brand clicks/28d** (inference from potential_clicks deltas).

2. **catchment.school — protect + widen the moat.** The star (4,091 clicks, +110%). But 85% brand and a slightly worsening position trend (position_delta −1.93 = improving avg actually; clicks 7-day delta −6%, a cooling signal). Highest *absolute* base, so even a small CTR/coverage lift is large. The CTR file surfaces council/area hub pages (Swansea, Cardiff, Milton Keynes, Solihull, Wokingham) at pos 6–10 — building county/council hubs to lift these page-1.x pages is high yield. Estimated: **+100–200 clicks/28d** plus durability against the cooling.

3. **deadhangs.com — de-risk the concentration, then expand.** 411 clicks but **96% from 2 URLs** (dead-hang-time-by-age = 330 clicks, dead-hang-world-record = 77). Massive single-page-of-keywords concentration risk. The same two pages also have huge anchored-section impressions earning zero clicks (e.g. #average-times 1,274 impr / 0 clicks). Both pages already rank pos ~7–8 with strong CTR. Cheapest incremental clicks = spin the proven topic into a cluster (calculator, by-sport, grip/forearm training) and interlink. Estimated: **+80–150 clicks/28d**, and it lowers portfolio risk.

Sites 4–7 (chargefinder, nomadranker, heatpumpchecker, solarhq) are earlier-stage: high impressions but low CTR and/or page-2+ positions. They are **second-wave** — worth title fixes (cheap) now, but content/link investment after the top 3.

---

## catchment.school

- **Snapshot:** 4,091 clicks (+110%), 121,497 impr (+113%), CTR 3.37%, avg pos 9.2, 500 pages, ~4 queries/page, brand share 85%, top non-brand query "eltham cofe primary school". Last-7 clicks −6% vs prior 7 (early cooling).
- **Strengths:** Largest absolute traffic and impression base in the portfolio; strong 3.4% CTR shows the format works; broad school/area/council page structure already indexed.
- **Risks:** 85% brand-dependent (mostly individual school-name searches); 7-day click delta is slightly negative — momentum may be plateauing; reliant on Google surfacing school pages.
- **Content plays:** Build **council and area hub pages** to capture the head terms that feed the long tail — the CTR file shows /council/swansea/ (7 clicks, pos 6.7), /area/cardiff/ (4, pos 7.2), /area/swansea/, /council/wokingham/, /council/solihull/ all at pos 6–10. Adjacent clusters inferred from existing patterns: "best primary schools in [town]", "[town] school admissions 2026/2027", catchment-appeal guides, the existing /guides/school-admissions-timeline/ (pos 9.8) suggests a guides cluster worth expanding (oversubscription criteria, in-year transfers, grammar-school catchment).
- **Internal links / hub structure:** Link every school page up to its area page and area→council page, and cross-link sibling schools within a catchment. This concentrates authority on the council/area hubs sitting at pos 6–10 to push them onto page-1 proper, and creates non-brand entry points that reduce brand dependence.
- **Link/promo play:** Data-PR angle — an annual "most oversubscribed primary schools in [region] 2026" study from your own catchment data. School-admissions season is a guaranteed local-news hook (BBC local, regional papers) and earns local-authority citations.
- **Expected impact:** +100–200 clicks/28d from hub uplift; primary value is **defending and diversifying** the 4,091-click base away from brand (inference).

## waterhard.uk

- **Snapshot:** 1,013 clicks (+71%), 56,465 impr (+110%), CTR 1.79%, avg pos 8.0, 500 pages, brand share 78%, top non-brand "soft water areas uk". Last-7 clicks +27%.
- **Strengths:** Visibility score 97 (highest in portfolio); already page-1 across a wide region/water-company/area estate; non-brand demand is real and ranking.
- **Risks:** 78% brand-dependent. Many high-impression pages convert poorly relative to position — clicks are being left on the table at page-1 positions.
- **Content plays:** This is primarily a **CTR-capture** site, not a content-gap site. The opportunity file lists dozens of page-1 pages with large potential_clicks gaps: /water-company/thames-water/ (19 clicks vs 132.8 potential, pos 6.2), /region/london/ (28 vs 76.9, pos 7.5), /water-company/affinity-water/ (4 vs 46.8), /water-company/severn-trent/ (8 vs 38.1), /water-company/yorkshire-water/ (9 vs 33.0). Add high-intent adjacent pages off the top non-brand theme: "soft water areas UK map", "is my water hard or soft by postcode", "limescale [city]", water-softener-need-by-area.
- **Internal links / hub structure:** Build region → county → area → postcode breadcrumb hubs and link water-company pages to the regions they serve. Lifting the many pos 9–10 pages (e.g. /water-company/scottish-water/ pos 10.4, /region/south-east/ pos 9.6) into the top 5 is where the CTR jump lives.
- **Title-fix overlap (Task 2):** The gap between actual and potential clicks at fixed positions is a classic title/meta-CTR problem — coordinate with Task 2 so the title rewrites for these ~60 pages are batched with the internal-link pass.
- **Link/promo play:** "Hard water map of the UK" interactive/data study — highly linkable by plumbing, appliance, and home-reno sites; pitch to water-softener retailers and regional press.
- **Expected impact:** Highest in the set — **+150–300 non-brand clicks/28d** from closing position-held CTR gaps (inference from summed potential_clicks deltas).

## deadhangs.com

- **Snapshot:** 411 clicks (+33%), 34,151 impr, CTR 1.20%, avg pos 7.5, only 17 pages, ~70 queries/page, brand share 3% (almost pure non-brand), top non-brand "dead hang time by age and gender" (27 clicks). Last-7 clicks +11%.
- **Strengths:** Nearly all non-brand traffic (resilient, no brand dependence); two pages rank pos ~7–8 with healthy CTR; high queries-per-page means each page harvests a wide tail.
- **Risks:** **Severe concentration** — /dead-hang-time-by-age/ (330 clicks) + /dead-hang-world-record/ (77) = ~96% of all clicks across just 17 pages. Any single-page ranking loss is an existential hit. Anchored sub-sections show large impressions with zero clicks (e.g. /dead-hang-time-by-age/#average-times 1,274 impr / 0 clicks; #percentile-chart 1,327 / 0) — Google is fragmenting impressions across jump-links.
- **Content plays:** Productize the winning topic into a **cluster**: dead-hang-time calculator/percentile tool, dead hang by sport/bodyweight, grip-strength + forearm training guides, "how to improve dead hang time", dead-hang-vs-pull-up. /deadhang-guide/ already exists at pos 13 — strengthen and interlink it to ride the two winners' authority.
- **Internal links / hub structure:** Create a hub linking the two power pages to the new cluster pages so their authority spreads; this both diversifies the click base and gives the page-2 guide a lift.
- **Title-fix overlap (Task 2):** The zero-click anchored sections are a SERP-presentation issue (jump-links) more than a title issue, but the /deadhang-guide/ at pos 13 is a candidate for the Task 2 title/meta review.
- **Link/promo play:** Fitness data study — "dead hang times by age and gender" percentile dataset (you already own the #1 query). Pitch to fitness/calisthenics publications and r/bodyweightfitness-adjacent blogs; the dataset is inherently citable.
- **Expected impact:** +80–150 clicks/28d from the new cluster, and — more importantly — converts a fragile 2-URL site into a defensible cluster (inference).

## chargefinder.uk

- **Snapshot:** 92 clicks (+45x), 4,693 impr (+658%), CTR 1.96%, avg pos 29.0, 500 pages, brand share 80%, top non-brand "de16 postcode". Last-7 clicks 76 vs prior-7 of 3 (explosive recent ramp).
- **Strengths:** Fastest grower in the portfolio; CTR already ~2% despite a poor avg position; programmatic estate of 500 pages just starting to index/rank.
- **Risks:** Avg position 29 = mostly page 3 — traffic is early and fragile; 80% brand-dependent on a brand-new brand; tiny absolute base (92 clicks).
- **Content plays:** It's an EV-charging finder. Lean into location/postcode pages (the top query is a postcode). Add charge-network comparison pages, "EV charging near [town]", connector-type and cost-per-kWh guides to broaden non-brand intent.
- **Internal links / hub structure:** Region → town → postcode hubs to help the 500 pages cross page-2 into page-1. At pos 29, the lever is rankings (links + internal structure), not CTR yet.
- **Link/promo play:** EV/charging directory citations and listing in EV community resources; a "UK public charger price index" data hook for EV press.
- **Expected impact:** Second-wave. With 500 pages at pos 29, ranking gains could multiply the small base quickly, but it needs link/authority to move — defer heavy investment until positions improve (inference).

## nomadranker.com

- **Snapshot:** 69 clicks (+306%), **38,499 impr** (+274%), CTR **0.18%** (lowest in set), avg pos 11.6, 500 pages, brand share 0%, top non-brand "digital nomad barcelona".
- **Strengths:** Enormous, fast-growing impression base (38.5k) with 100% non-brand demand; positions (avg 11.6) are right on the page-1/2 boundary; cost-of-living city pages have clear intent.
- **Risks:** **CTR is the problem, not traffic** — 0.18% means the impressions exist but almost nothing clicks. One page alone, /cities/cusco/cost-of-living/, has 5,799 impressions and **0 clicks** (pos 7.9, potential_clicks 174). City pages cluster at pos 6–10 with near-zero CTR.
- **Content plays:** Content is secondary here; the city-template already harvests impressions. If anything, ensure each city has the full sub-page set (cost-of-living, internet, safety) and add comparison pages ("Barcelona vs Lisbon for digital nomads").
- **Internal links / hub structure:** Region/continent hubs linking cities, plus "best nomad cities" ranking pages to funnel the impression base.
- **Title-fix overlap (Task 2 — PRIMARY lever):** This is the textbook Task 2 case. 38,499 impressions at 0.18% CTR with page-1 positions on pages like Cusco (5,799 impr, 0 clicks) means the **titles/meta/SERP snippet are not earning the click**. A title/meta rewrite across the city templates is the single highest-leverage action for this site and should be owned by Task 2. Even lifting CTR from 0.18% to a modest 1.5% on the current impression base implies roughly **+500 clicks/28d** (inference: 38,499 × ~1.3pp uplift).
- **Link/promo play:** Digital-nomad cost-of-living data study / "cheapest nomad cities 2026" index — naturally linkable by nomad and remote-work publications.
- **Expected impact:** Largest *latent* upside in the set via CTR fix (potentially several hundred clicks), but realized only through the Task 2 title work — flagged as cross-task dependency (inference).

## heatpumpchecker.co.uk

- **Snapshot:** 48 clicks (+100%), 13,502 impr (+48%), CTR 0.36%, avg pos 25.3, 500 pages, ~2.3 queries/page, brand share 0%, top non-brand "do you need bigger radiators with air source heat pump".
- **Strengths:** 100% non-brand; growing impressions; strong UK heat-pump policy tailwind; informational top query shows genuine intent.
- **Risks:** Avg pos 25 (page 2–3) and 0.36% CTR — early stage; low queries-per-page (2.3) suggests thin templates not yet harvesting tail.
- **Content plays:** The top query is a question — build a Q&A/guide cluster around heat-pump sizing, radiator upgrades, running costs, grant eligibility (BUS scheme), and "is my home suitable for a heat pump". Adjacent to existing checker tool.
- **Internal links / hub structure:** Link guides to the checker tool and to regional/installer pages to lift the page-2 estate.
- **Title-fix overlap (Task 2):** Worth including the highest-impression pages in the Task 2 title pass, but the bigger blocker is position (25), so rankings come first.
- **Link/promo play:** Heat-pump grant/cost data explainer; pitch to home-energy and retrofit blogs; MCS/installer directory citations.
- **Expected impact:** Second-wave; needs ranking gains before CTR work pays off (inference).

## solarhq.uk

- **Snapshot:** 27 clicks (+145%), 18,328 impr (+37%), CTR **0.15%**, avg pos **44.5** (deepest in set), 500 pages, brand share 0%. Top non-brand query is a scraped advanced-operator string (data-quality note — treat the literal value with caution).
- **Strengths:** Large impression base and 100% non-brand; strong solar-market demand; full 500-page estate.
- **Risks:** Avg position 44 = page 4–5, so impressions are mostly low-value; 0.15% CTR; the earliest-stage site in the set with the smallest realized base.
- **Content plays:** Solar quotes/cost/savings calculators, "solar panel cost [region] 2026", payback-period and battery-storage guides, installer-comparison pages — broaden intent off residential-solar-installation theme.
- **Internal links / hub structure:** Regional hubs + link calculators/guides together to build topical depth and push pos-44 pages toward page 1–2.
- **Link/promo play:** "Solar payback by UK region 2026" data study; renewable-energy and home-improvement link targets; installer directory citations.
- **Expected impact:** Lowest near-term return (positions far from page 1). Keep publishing/interlinking, but it is the **last** investment priority among the seven (inference).

---

## Summary of recommended sequencing

1. **waterhard.uk** — batch title/meta + internal-link pass on ~60 page-1 non-brand pages (with Task 2). Highest incremental clicks, fastest.
2. **catchment.school** — build council/area hubs to lift page-1.x pages and diversify off 85% brand; defend the largest base.
3. **deadhangs.com** — cluster-out the two power pages to de-risk 96% concentration and add clicks.
4. **nomadranker.com** — Task 2 title rewrite on city templates (largest latent CTR upside on 38.5k impressions).
5. **chargefinder.uk / heatpumpchecker.co.uk / solarhq.uk** — second wave; ranking-building (links + internal structure) before CTR work, in that order of current proximity to page 1.

Notes: percentages and snapshot figures are from the source CSVs (28-day window). Expected-impact ranges and any "potential" capture figures are **inferences** derived from the `potential_clicks`/CTR gaps in `organic_visibility_ctr_opportunities.csv` and are labelled as such.
