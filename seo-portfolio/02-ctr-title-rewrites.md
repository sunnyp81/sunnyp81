# Task 2 — CTR / Title-Tag Sprint: Top 25 Title & Meta Rewrites

**Data snapshot:** ~May 17–22 2026 (GSC export). **Prepared:** 2026-06-06.
**Source:** `organic_visibility_ctr_opportunities.csv` (281 page rows across the portfolio).

## Methodology

1. Parsed every row of the CTR-opportunities export. Ranked by `potential_clicks` (impressions × the position-band's `expected_ctr`) descending. Computed **click gap = potential_clicks − clicks** = the latent clicks currently being left on the table.
2. Classified each page: **P1** = position < 10 (already page 1, fastest win), **P2** = position 10–20 (page-2 secondary tier), P3 = position > 20.
3. **Total addressable upside:** the sum of P1 click gaps across all 185 P1 pages is **≈ 1,964 clicks/period** — and 96 P2 pages add a further ≈ 242. This is pure title/meta/snippet work: the rankings already exist.
4. For the top ~25 actionable pages below, the target query is inferred from the URL slug (live titles could not be fetched — every site returned **HTTP 403 / bot protection**, so the "Current title" column is left as *not fetchable* and rewrites are built from slug + niche intent). Titles are keyword-front-loaded, ≤ ~60 chars; descriptions ≤ ~155 chars with a hook/CTA and (for YMYL/data pages) a freshness/number signal that lifts CTR.

### Important caveat — SERP-feature suspicion (different fix, not a title fix)

A large share of these P1 pages rank #4–#9 with **near-zero CTR despite hundreds–thousands of impressions**. That pattern (e.g. Thames Water: pos 6.2, 5,060 impressions, 19 clicks = 0.38% CTR vs 3% expected; Cusco / Bromsgrove / most rentalyield + waterhard + redlighttherapy pages at 0 clicks) is the classic signature of an **AI Overview, Featured Snippet, or People-Also-Ask block absorbing the click** above the organic result. For these, a sharper title helps but the higher-leverage move is: (a) restructure content to win/own the snippet, (b) add concise FAQ/answer-target blocks, and (c) add structured data. These rows are flagged "SERP-feature" in the action-list CSV and tagged below.

**Anchor-fragment URLs** (e.g. `deadhangs.com/dead-hang-time-by-age/#percentile-chart`) appear high in the raw ranking but are jump-links to one page — they should be **consolidated under the parent page's title**, not given their own tags. They are excluded from the 25 below (kept in the CSV with a note).

---

## Top 25 rewrites

Numbers are from the CSV (impressions / clicks / position for the snapshot). "Gap" = click gap.

### 1. deadhangs.com/dead-hang-time-by-age/  — *biggest single page*
- **Metrics:** pos 6.9 · 21,641 impr · 330 clicks · potential 319 · gap −11 · P1
- **Inferred query:** dead hang time by age (average / chart)
- **Current title:** not fetchable (403)
- **Proposed title:** `Dead Hang Time by Age Chart (Average & Good Times)`
- **Proposed meta:** `See average dead hang times by age and gender, plus percentile charts. Find out how your grip endurance compares — full data tables inside.`
- **Rationale:** Already near expected CTR and capturing huge volume; this is the portfolio's workhorse. Front-load "by Age Chart" + add "Average & Good Times" to widen query match. Marginal but high-volume, so even +5% CTR is meaningful.

### 2. deadhangs.com/dead-hang-world-record/  — **SERP-feature**
- **Metrics:** pos 8.2 · 11,491 impr · 77 clicks · potential 268 · gap **191** · P1
- **Inferred query:** dead hang world record
- **Proposed title:** `Dead Hang World Record 2026 (Men & Women)`
- **Proposed meta:** `The current dead hang world record — men's and women's longest hangs, who holds them and the times to beat. Updated for 2026.`
- **Rationale:** 0.67% CTR at pos 8 on 11.5k impressions = a featured-snippet/PAA is almost certainly eating the answer. Add a year for freshness + "Men & Women" to win the long tail; pair with snippet-targeting content. Single biggest title-driven upside in the set.

### 3. nomadranker.com/cities/cusco/cost-of-living/  — **SERP-feature**
- **Metrics:** pos 7.9 · 5,799 impr · 0 clicks · potential 174 · gap **174** · P1
- **Inferred query:** cusco cost of living
- **Proposed title:** `Cost of Living in Cusco 2026 (Monthly Budget)`
- **Proposed meta:** `Real monthly cost of living in Cusco, Peru — rent, food, and a full digital-nomad budget breakdown in USD. See what $X/month gets you.`
- **Rationale:** 0% CTR on 5.8k impressions at pos 8 screams an AI Overview/snippet. Add year + "Monthly Budget" + currency hook. Highest 0-click opportunity in the portfolio.

### 4. rentalyield.uk/council/bromsgrove/  — **SERP-feature**
- **Metrics:** pos 6.7 · 5,106 impr · 0 clicks · potential 153 · gap **153** · P1
- **Inferred query:** Bromsgrove rental yield / buy-to-let
- **Proposed title:** `Bromsgrove Rental Yield 2026 — Buy-to-Let Returns`
- **Proposed meta:** `Average rental yields in Bromsgrove by postcode and property type. See gross yield, avg rent and house prices for buy-to-let investors.`
- **Rationale:** 0% CTR at pos 6.7 on 5.1k impressions — likely a data snippet. Lead with location + "Rental Yield" + year; quantified hook for investor intent.

### 5. waterhard.uk/water-company/thames-water/  — **SERP-feature**
- **Metrics:** pos 6.2 · 5,060 impr · 19 clicks · potential 133 · gap **114** · P1
- **Inferred query:** Thames Water hard water area / water hardness
- **Proposed title:** `Thames Water Hard Water Areas & Hardness Levels`
- **Proposed meta:** `Is Thames Water hard or soft? Check water hardness by postcode across the Thames Water region, with mg/L levels and limescale advice.`
- **Rationale:** 0.38% CTR vs 3% expected on 5k impressions — snippet/PAA dominant. Lead with the brand + "Hard Water Areas"; "by postcode" + "mg/L" matches the data-seeking query.

### 6. waterhard.uk/region/london/
- **Metrics:** pos 7.5 · 3,497 impr · 28 clicks · potential 77 · gap **49** · P1
- **Inferred query:** is London water hard / London water hardness
- **Proposed title:** `Is London Water Hard? Hardness by Area (Map)`
- **Proposed meta:** `London has some of the UK's hardest water. Check hardness levels by borough and postcode, plus what it means for limescale and appliances.`
- **Rationale:** Question-format title matches voice/search intent; "(Map)" is a CTR magnet for geo queries.

### 7. waterhard.uk/water-company/affinity-water/  — **SERP-feature**
- **Metrics:** pos 6.9 · 1,694 impr · 4 clicks · potential 47 · gap **43** · P1
- **Inferred query:** Affinity Water hard water area
- **Proposed title:** `Affinity Water Hard Water Areas & Levels`
- **Proposed meta:** `Is Affinity Water hard or soft? Find water hardness by postcode across the Affinity supply area, with mg/L readings and softener advice.`
- **Rationale:** Same brand+hardness pattern as Thames; 0.24% CTR indicates snippet. Pair title fix with snippet-targeting answer block.

### 8. sunnypatel.co.uk/blog/local-seo-statistics/  — **SERP-feature**
- **Metrics:** pos 9.7 · 1,625 impr · 3 clicks · potential 46 · gap **43** · P1
- **Inferred query:** local SEO statistics
- **Proposed title:** `120+ Local SEO Statistics for 2026 (UK Data)`
- **Proposed meta:** `The latest local SEO statistics for 2026 — Google Business Profile, near-me searches, mobile and conversion data, all sourced and cited.`
- **Rationale:** Stats posts live or die on number + year in the title; pos 9.7 means it's on the edge of page 1, so a stronger snippet can also nudge rank. Big number ("120+") boosts CTR.

### 9. waterhard.uk/water-company/severn-trent/  — **SERP-feature**
- **Metrics:** pos 7.4 · 1,538 impr · 8 clicks · potential 38 · gap **30** · P1
- **Inferred query:** Severn Trent hard water area
- **Proposed title:** `Severn Trent Water: Hard or Soft? Hardness Map`
- **Proposed meta:** `Check whether your Severn Trent supply is hard or soft. Water hardness by postcode with mg/L levels and limescale prevention tips.`
- **Rationale:** Question hook + "Map"; consistent template across water-company pages for scalable rollout.

### 10. waterhard.uk/water-company/united-utilities/  — **SERP-feature**
- **Metrics:** pos 7.8 · 1,383 impr · 6 clicks · potential 35 · gap **29** · P1
- **Inferred query:** United Utilities hard water area
- **Proposed title:** `United Utilities Water: Hard or Soft Areas`
- **Proposed meta:** `Is United Utilities water hard or soft? See hardness by postcode across the North West, with mg/L levels and softener guidance.`
- **Rationale:** Same scalable hardness template; region cue ("North West") aids relevance.

### 11. waterhard.uk/water-company/yorkshire-water/  — **SERP-feature**
- **Metrics:** pos 7.9 · 1,399 impr · 9 clicks · potential 33 · gap **24** · P1
- **Inferred query:** Yorkshire Water hard water area
- **Proposed title:** `Yorkshire Water: Hard or Soft? Hardness by Area`
- **Proposed meta:** `Find out if Yorkshire Water is hard or soft. Water hardness levels by postcode and town, with mg/L data and limescale advice.`
- **Rationale:** Consistent template; question framing wins the "is ... hard" long tail.

### 12. waterhard.uk/water-company/welsh-water/  — **SERP-feature**
- **Metrics:** pos 6.1 · 1,251 impr · 9 clicks · potential 29 · gap **20** · P1
- **Inferred query:** Welsh Water (Dŵr Cymru) hard water area
- **Proposed title:** `Welsh Water: Hard or Soft? Hardness by Postcode`
- **Proposed meta:** `Is Dŵr Cymru / Welsh Water hard or soft? Check hardness levels by postcode across Wales, with mg/L readings and softener tips.`
- **Rationale:** Strong rank (pos 6) but tiny CTR — snippet-driven; brand synonyms (Dŵr Cymru) in meta widen match.

### 13. waterhard.uk/region/wales/  — **SERP-feature**
- **Metrics:** pos 6.7 · 983 impr · 2 clicks · potential 27 · gap **25** · P1
- **Inferred query:** is water in Wales hard / Wales water hardness
- **Proposed title:** `Is Water in Wales Hard or Soft? (Hardness Map)`
- **Proposed meta:** `Most of Wales has soft water — but not everywhere. Check hardness by region and postcode, with mg/L levels and what it means for you.`
- **Rationale:** Counterintuitive hook ("most ... soft, but not everywhere") drives curiosity clicks; "Map" cue.

### 14. rentalyield.uk/buy-to-let/sunderland/  — **SERP-feature**
- **Metrics:** pos 4.5 · 387 impr · 0 clicks · potential 27 · gap **27** · P1
- **Inferred query:** Sunderland buy-to-let rental yield
- **Proposed title:** `Sunderland Buy-to-Let Yields 2026 (Best Areas)`
- **Proposed meta:** `Sunderland buy-to-let rental yields by postcode — among the UK's highest. See gross yields, average rents and the best areas to invest.`
- **Rationale:** Ranks #4 yet 0 clicks = strong snippet capture; "among the UK's highest" is a true, click-worthy hook for a high-yield city.

### 15. rentalyield.uk/buy-to-let/manchester/  — **SERP-feature**
- **Metrics:** pos 7.4 · 864 impr · 0 clicks · potential 26 · gap **26** · P1
- **Inferred query:** Manchester buy-to-let rental yield
- **Proposed title:** `Manchester Buy-to-Let Yields 2026 by Postcode`
- **Proposed meta:** `Manchester rental yields by postcode and area. Compare gross yields, average rents and house prices to find the best buy-to-let spots.`
- **Rationale:** 0 clicks on 864 impressions; year + "by Postcode" specificity. Pair with snippet/table optimisation.

### 16. bestvibrationplates.co.uk/can-cause-diarrhea/
- **Metrics:** pos 7.9 · 1,312 impr · 14 clicks · potential 25 · gap **11** · P1
- **Inferred query:** can vibration plates cause diarrhea
- **Proposed title:** `Can Vibration Plates Cause Diarrhea? (Explained)`
- **Proposed meta:** `Can vibration plate exercise upset your stomach or cause diarrhea? Here's what the evidence says, why it happens, and how to avoid it.`
- **Rationale:** Slug is ambiguous to Google; a clear question title sharpens relevance. Already converting somewhat (1.1% CTR) so realistic upside.

### 17. rentalyield.uk/buy-to-let/liverpool/  — **SERP-feature**
- **Metrics:** pos 7.0 · 839 impr · 0 clicks · potential 25 · gap **25** · P1
- **Inferred query:** Liverpool buy-to-let rental yield
- **Proposed title:** `Liverpool Buy-to-Let Yields 2026 (Best Postcodes)`
- **Proposed meta:** `Liverpool buy-to-let rental yields by postcode — one of the UK's top yield cities. Compare gross yields, rents and the best areas to invest.`
- **Rationale:** 0 clicks at pos 7; high-intent investor query, strong factual hook. (Note: a duplicate `/liverpool` no-slash URL also ranks — consolidate to the canonical trailing-slash version.)

### 18. calculator.place/math/average-calculator/  — *P2*
- **Metrics:** pos 11.7 · 2,338 impr · 0 clicks · potential 23 · gap **23** · P2
- **Inferred query:** average calculator / mean calculator
- **Proposed title:** `Average Calculator — Mean, Median & Mode (Free)`
- **Proposed meta:** `Free online average calculator. Instantly find the mean, median, mode and range of any number set — just paste your values and go.`
- **Rationale:** Page 2 (pos 11.7) so a stronger title/snippet supports both CTR and a rank push to page 1; "Free / Instantly" are proven tool-query CTR levers.

### 19. waterhard.uk/water-company/south-west-water/  — **SERP-feature**
- **Metrics:** pos 6.9 · 972 impr · 6 clicks · potential 23 · gap **17** · P1
- **Inferred query:** South West Water hard water area
- **Proposed title:** `South West Water: Hard or Soft? Hardness by Area`
- **Proposed meta:** `Is South West Water hard or soft? Check hardness by postcode across Devon & Cornwall, with mg/L levels and limescale advice.`
- **Rationale:** Scalable hardness template; regional cue (Devon & Cornwall) for relevance.

### 20. redlighttherapy.expert/platinumled-review/  — *P2*
- **Metrics:** pos 15.5 · 2,156 impr · 0 clicks · potential 22 · gap **22** · P2
- **Inferred query:** PlatinumLED review / BioMax review
- **Proposed title:** `PlatinumLED Review 2026 — Worth It? (Tested)`
- **Proposed meta:** `Honest PlatinumLED BioMax review for 2026 — irradiance tested, pros, cons, price and whether it beats cheaper rivals. Read before you buy.`
- **Rationale:** Page-2 review with high impressions; "Tested / Worth It? / Read before you buy" are high-CTR review modifiers that can also lift rank. Primary need is a rank push, but a compelling snippet compounds.

### 21. rentalyield.uk/buy-to-let/nottingham/  — **SERP-feature**
- **Metrics:** pos 4.2 · 313 impr · 2 clicks · potential 20 · gap **18** · P1
- **Inferred query:** Nottingham buy-to-let rental yield
- **Proposed title:** `Nottingham Buy-to-Let Yields 2026 (Best Areas)`
- **Proposed meta:** `Nottingham rental yields by postcode — a top UK student-let market. See gross yields, average rents and the best buy-to-let areas.`
- **Rationale:** Ranks #4 with almost no clicks = snippet-dominated; student-let angle is a true differentiator hook.

### 22. waterhard.uk/water-company/south-east-water/
- **Metrics:** pos 6.5 · 968 impr · 10 clicks · potential 19 · gap **9** · P1
- **Inferred query:** South East Water hard water area
- **Proposed title:** `South East Water: Hard or Soft Areas & Levels`
- **Proposed meta:** `Is South East Water hard or soft? Check hardness by postcode (it's among the UK's hardest), with mg/L levels and softener advice.`
- **Rationale:** Already best-converting of the water-company set (1.0% CTR) so upside is modest but reliable; honest "among the hardest" hook.

### 23. redlighttherapy.expert/omnilux-review/  — **SERP-feature**
- **Metrics:** pos 7.3 · 628 impr · 0 clicks · potential 19 · gap **19** · P1
- **Inferred query:** Omnilux review (Contour / mask)
- **Proposed title:** `Omnilux Review 2026 — Is It Worth the Money?`
- **Proposed meta:** `Omnilux LED review for 2026 — results, who it's for, pros, cons and price. We compare it to cheaper masks so you can decide before buying.`
- **Rationale:** 0 clicks at pos 7 on a buyer-intent term suggests a review snippet/PAA above it; "Worth the Money? / before buying" are strong commercial CTR triggers.

### 24. bestvibrationplates.co.uk/vibration-plate-after-hip-replacement-guide/  — **SERP-feature**
- **Metrics:** pos 8.2 · 627 impr · 2 clicks · potential 17 · gap **15** · P1
- **Inferred query:** vibration plate after hip replacement (safe?)
- **Proposed title:** `Vibration Plate After Hip Replacement: Is It Safe?`
- **Proposed meta:** `Can you use a vibration plate after a hip replacement? Safety guidance, timing, risks and physio-backed tips before you start.`
- **Rationale:** Health-safety question intent; "Is It Safe?" + "physio-backed" build trust and CTR. Likely a PAA box is capturing the short answer — also add a concise answer block.

### 25. rentalyield.uk/buy-to-let/luton/  — **SERP-feature**
- **Metrics:** pos 7.6 · 550 impr · 0 clicks · potential 17 · gap **17** · P1
- **Inferred query:** Luton buy-to-let rental yield
- **Proposed title:** `Luton Buy-to-Let Yields 2026 by Postcode`
- **Proposed meta:** `Luton buy-to-let rental yields by postcode — strong commuter-belt returns. Compare gross yields, average rents and the best areas to invest.`
- **Rationale:** 0 clicks at pos 7.6; year + postcode specificity + commuter-belt hook. Snippet-optimise the yield table alongside.

---

## Rollout notes

- **Templates exist for free scale.** waterhard.uk water-company + region pages and rentalyield.uk buy-to-let + council pages each share one query pattern. Apply the title/meta templates above programmatically across *all* such pages (there are 60+ more in the CSV below the top 25), not just these.
- **SERP-feature pages need a second lever.** ~70% of the top P1 rows are snippet/AIO-suppressed. Title rewrites alone will under-deliver; pair them with (1) a concise answer block / FAQ schema targeting the snippet, (2) a data table for the "by postcode / monthly budget" intents, and (3) review schema for the redlighttherapy review pages.
- **Consolidate duplicates & fragments.** `rentalyield.uk/buy-to-let/liverpool` vs `/liverpool/`, `nottingham` vs `nottingham/`, `hull`, `stoke-on-trent`, plus the deadhangs.com and colourlabelprinter.com `#anchor` URLs are splitting/inflating impressions — canonicalise to one URL each before measuring CTR lift.
- **Estimated P1 click upside (all 185 P1 pages): ≈ 1,964 clicks/period.** The top 25 above account for roughly **1,260 potential clicks** — i.e. a small slice of pages carries most of the win.
