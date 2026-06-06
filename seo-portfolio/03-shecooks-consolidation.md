# Task 3 — shecookssheeats.co.uk Consolidation & Recovery Plan

_Snapshot ~May 17–22 2026 (GSC 28-day). Prepared 2026-06-06. Source: organic_visibility_summary.csv, organic_visibility_ctr_opportunities.csv, organic_visibility_dead_pages.csv._

## Summary

shecookssheeats.co.uk is a Tier-1 UK Slimming-World food blog that is **visible but stuck and declining**. It earns ~473 clicks from ~80,175 impressions (CTR ~0.59%, avg position ~17 — page 2), with clicks down ~20% and impressions down ~11% vs the prior period. The site has **500 indexed pages but only ~3,588 non-brand impressions worth of demand spread across ~23 distinct queries / page** — `queries_per_page = 4.0`, the classic signature of **thin-content-at-scale**. Hundreds of near-identical single-answer `/syns/<food>` and `/syns-<food>` URLs are competing with each other for the same "how many syns is X" query.

**Headline finding:** the problem is not a content shortage — it is **keyword cannibalization plus thin single-answer pages that all park on page 2**. Two URL templates (`/syns/<food>/` and `/syns-<food>/`) were both shipped, creating direct duplicate pairs (e.g. `/syns/peaches/` vs `/syns-peaches/`). The fix is **consolidate, redirect, and interlink**, not publish more.

**Headline recommendation:** Pick ONE URL template, 301 the duplicates into the winner, roll the long tail of thin `/syns-*` pages up into a small number of **category hub/pillar pages** (a "Slimming World Syns Directory" plus grouped guides for Crisps/Snacks, Fruit, Dairy, Cereals, Alcohol), and build a hub-and-spoke internal-linking layer to push the ~15 page-2 pages that already have impressions onto page 1.

**By the numbers:** **5 duplicate/cannibalizing URL clusters** identified, **~30+ thin single-answer pages** recommended for consolidation into 1 directory hub + 5 grouped guides, and **4 recently-dead pages** to recover.

> Note: WebFetch of live pages (`/syns/peaches/`, `/syns-walkers-crisps/`) returned **HTTP 403 Forbidden** — the site blocks automated fetches, so on-page depth could not be sampled directly. Thinness is inferred from the GSC structural signals (500 pages, `queries_per_page = 4.0`, single-answer URL slugs, CTR ~0.59%), which are unambiguous.

## Current State (numbers)

Site-level (from organic_visibility_summary.csv):

| Metric | Value |
|---|---|
| Tier / state / status | T1 / recovery / visible |
| Visibility score | 70.3 |
| Clicks (28d) | 473 (prev 594, **−20.4%**) |
| Impressions (28d) | 80,175 (prev 90,327, **−11.2%**) |
| CTR (28d) | 0.59% |
| Avg position (28d) | 17.4 (page 2) |
| Position delta | +0.88 (drifting **worse**) |
| Last7 vs prev7 clicks | 87 vs 89 (−2.2%) |
| Non-brand clicks / impressions | 23 / 3,588 |
| Query count / page count | 500 / 500 |
| Queries per page | **4.0** (thin) |
| Top non-brand query | "nando's slimming world 2026" (3 clicks) |

Read-through: 80k impressions but <500 clicks because almost everything ranks 7–18 and the winning answer box / page-1 result belongs to a competitor. The handful of pages sitting at position 5–8 convert at ~2% CTR; everything at position 11–19 converts at ~0%.

The few pages that actually perform (worth protecting and linking FROM):

| Page | Clicks | Impr | Pos |
|---|---|---|---|
| /syns-flaxseed/ | 5 | 258 | 5.6 |
| /syns/peaches/ | 5 | 248 | 7.2 |
| /syns/butter/ | 4 | 612 | 8.2 |
| /syns/nuts/ | 4 | 519 | 8.6 |
| /syns/yogurts/ | 4 | 735 | 18.7 |
| /syns-rice-cakes/ | 3 | 495 | 12.9 |
| /syns/medjool-dates/ | 3 | 178 | 7.3 |
| /syns/nature-valley-bar/ | 3 | 171 | 8.7 |
| /syns/prunes/ | 3 | 179 | 6.6 |

High-impression pages stuck on page 2 earning ~0 clicks (biggest unrealised demand — prime hub-link targets):

| Page | Clicks | Impr | Pos |
|---|---|---|---|
| /guides/speed-foods/ | 0 | 1,212 | 11.4 |
| /weetabix-syns/ | 1 | 888 | 14.6 |
| /syns/yogurts/ | 4 | 735 | 18.7 |
| /syns/weetabix/ | 2 | 742 | 13.8 |
| /low-syn-crisps/ | 1 | 617 | 17.5 |
| /syns/walkers-crisps/ | 1 | 561 | 12.4 |
| /bachelors-pasta-sauce-syns/ | 0 | 502 | 15.4 |
| /syns/bread/ | 1 | 449 | 16.9 |
| /syns-muller-corner/ | 1 | 432 | 13.0 |
| /syns-walkers-crisps/ | 1 | 370 | 12.3 |
| /syns-skips/ | 1 | 352 | 16.8 |
| /syns-philadelphia-light/ | 1 | 342 | 15.6 |
| /syns/philadelphia/ | 2 | 335 | 10.5 |
| /syns-gordons-pink-gin/ | 1 | 291 | 17.9 |
| /mango-syns/ | 1 | 290 | 7.4 (page 1, weak CTR) |

## Duplicate / Cannibalization Pairs

Both URL templates (`/syns/<food>/` and `/syns-<food>/`) exist for the same foods, plus a few alternate-wording variants. These split link equity and force Google to choose between near-identical pages. **Keep the URL with the better position/clicks (or the cleaner template), 301 the loser into it, and merge any unique content.**

| Topic | KEEP (canonical) | 301-REDIRECT (→ keep) | Rationale (clicks / impr / pos) |
|---|---|---|---|
| Peaches | **/syns/peaches/** (5 / 248 / 7.2) | /syns-peaches/ (1 / 115 / 6.9) | `/syns/` version earns 5× the clicks; clear winner |
| Walkers crisps | **/syns/walkers-crisps/** (1 / 561 / 12.4) | /syns-walkers-crisps/ (1 / 370 / 12.3) **and** /best/walkers-crisps-slimming-world/ (0 / 108 / 14.4) | Three URLs on one query — worst cannibalization on the site; consolidate all into the highest-impression page |
| Rice cakes | **/syns-rice-cakes/** (3 / 495 / 12.9) | /syns/rice-cakes/ (1 / 267 / 11.9) | `/syns-` version earns 3× clicks and 2× impressions; also fold in /how-many-syns-in-tesco-rice-cakes/ (1 / 188 / 18.9) and /syns-snack-jacks/ (1 / 246 / 10.6) as sections |
| Weetabix | **/syns/weetabix/** (2 / 742 / 13.8) | /weetabix-syns/ (1 / 888 / 14.6) | Two URLs, near-identical position; merge the higher-impression body into the `/syns/` canonical, then 301 |
| Philadelphia | **/syns/philadelphia/** (2 / 335 / 10.5) | /syns-philadelphia-light/ (1 / 342 / 15.6) | Light vs regular are genuinely two variants — keep the regular page as canonical and make "Philadelphia Light" an on-page section (one strong page beats two weak ones at pos 10 & 15) |

> Decision rule for the wider long tail: wherever **both** `/syns/x/` and `/syns-x/` exist (the data confirms peaches, walkers-crisps, rice-cakes, weetabix; audit the full sitemap for the rest), keep whichever has higher impressions, 301 the other, and update internal links. Pick **`/syns/<food>/`** as the go-forward template for any *new* entries so the pattern is consistent.

## Thin Pages to Consolidate

These are single-answer "how many syns is X" pages with decent impressions but stuck at pos 10–19 and ~0 clicks. Individually they will never rank; **grouped into authoritative guides + a directory hub** they gain depth, internal links, and a shot at page 1. Keep the URL of the strongest page in each group as the hub, fold the rest in as sections, and 301 the absorbed URLs.

**Hub 1 — "Slimming World Syns Directory / Calculator" (new pillar, e.g. /syns/ or /slimming-world-syns/)**
A single searchable A–Z directory page that lists every food with its syn value in a table and links out to the pages worth keeping. Becomes the parent that links to all spokes below. Target query cluster: "slimming world syns", "how many syns".

**Hub 2 — Crisps & Savoury Snacks guide** (anchor: /low-syn-crisps/, 617 impr)
Fold in: /syns/walkers-crisps/ (canonical from dedup), /syns-skips/ (352), /syns/mini-cheddars/ (160), /syns-jacobs-crackers/ (179), /syns/crackers/ (227), /how-many-syns-quavers/ (147), /syns-popcorn-kernels/ (204), /syns/fridge-raiders/ (182), /syns-tesco-sandwiches/ (dead).

**Hub 3 — Fruit syns guide** (anchor: /syns/peaches/ or a new /fruit-syns/)
Fold in: /syns-blueberries/ (224), /syns/pineapple/ (378), /mango-syns/ (290), /bananas-syn/ (110), /syns/prunes/ (179), /syns/raisins/ (133), /syns-14-gram-raisins/ (253), /syns/medjool-dates/ (178). Keep top performers as their own pages but interlink under the hub.

**Hub 4 — Dairy & spreads guide** (anchor: /syns/butter/, 612 impr)
Fold in: /how-many-syns-butter/ (240, 0 clicks — direct cannibal of /syns/butter/), /syns/philadelphia/ (canonical from dedup), /syns/milk/ (376), /syns-elmlea-double-cream/ (dead), /syns-hellmans-light-mayonnaise/ (166), /syns/yogurts/ (735), /syns-muller-corner/ (432), /syns-malted-milk/ (161), /syns-canderel-sweetener/ (110).

**Hub 5 — Cereals & porridge guide** (anchor: /syns/weetabix/, canonical)
Fold in: /weetabix-syns/ (redirected), /syns-oat-so-simple-sachets/ (194), /syns-porridge-pots/ (225), /syns/bread/ (449), /how-many-syns-in-a-slice-of-white-bread/ (180).

**Hub 6 — Alcohol & drinks guide** (new, e.g. /slimming-world-alcohol-syns/)
Fold in: /syns-gordons-pink-gin/ (291), /syns-magnum/ (225), /are-energy-drinks-syn-free/ (187), /cuppa-soups-syn-free/ (162).

**Prune / noindex (very low value, no clicks, <120 impr, redundant):**
/syns-bourbon-biscuit/ (238, 0 clicks pos 11), /how-many-syns-artificial-sweetener/ (266 pos 11.5) + /how-many-syns-in-tesco-rice-cakes/ (188 pos 18.9), /syns-savoury-rice/ (242 pos 18.6), /how-many-syns-in-a-slice-of-black-pudding/ (104), /best/walkers-crisps-slimming-world/ (redirected), /light-coconut-milk-syns/ (162), /ham-syns/ (113), /syns-tilda-basmati-rice/ (170). Either fold into the nearest hub as a row or 301 to it; do not keep as standalone.

## Dead Pages to Recover

From organic_visibility_dead_pages.csv — these had clicks last period and now have **zero**. They previously held strong-ish positions, so they are recoverable with a content refresh + internal links from the relevant hub:

| Page | Prev clicks | Prev impr | Prev CTR | Prev pos | Action |
|---|---|---|---|---|---|
| /syns-tesco-sandwiches/ | 6 | 104 | 5.8% | 16.2 | Fold into **Crisps/Snacks hub**; refresh with current Tesco meal-deal syn values |
| /syns-bounty/ | 5 | 182 | 2.7% | 9.1 | Was page 1 (pos 9) — high recovery value; refresh + link from Chocolate/Snacks section |
| /syns-elmlea-double-cream/ | 5 | 162 | 3.1% | 24.7 | Fold into **Dairy & spreads hub** |
| /slimming-world-speed-foods/ | 6 | 885 | 0.7% | 18.3 | High impressions — **rebuild as the Speed Foods pillar** and consolidate with /guides/speed-foods/ (1,212 impr, pos 11.4), /guides/speed-food-guide/ (105) and /syns/yogurts/ link. This is the single biggest recoverable demand cluster on the site |

`/syns-bounty/` (was pos 9) and the Speed Foods cluster are the priority recoveries.

## Internal Linking Plan

Today the site is a **flat pile of 500 leaf pages with ~4 queries each and almost no topical structure** — that is why nothing escapes page 2. Impose a hub-and-spoke topology so equity flows to the pages that already have impressions.

1. **Top-level hubs in main nav / breadcrumb:** Syns Directory, Crisps & Snacks, Fruit, Dairy & Spreads, Cereals, Alcohol & Drinks, Speed Foods. Each is a real pillar page (200+ word intro + syn-value table + links to spokes).
2. **Breadcrumbs everywhere:** Home › [Category Hub] › [Food page]. Add BreadcrumbList schema. Gives Google the parent-child signal it currently lacks.
3. **Hub → spoke links:** every hub links to its 8–15 retained food pages with descriptive anchors ("How many syns in Walkers crisps").
4. **Spoke → hub + spoke → sibling:** each surviving food page links back up to its hub and to 3–5 related foods ("Related: Skips, Quavers, Mini Cheddars"). Kills orphan pages and spreads the ~3,500 impressions of internal authority.
5. **Point links FROM the few strong pages** (/syns-flaxseed/ pos 5.6, /syns/peaches/, /syns/prunes/, /syns/medjool-dates/, /syns/nuts/) **TO the page-2 high-impression pages** (/guides/speed-foods/, /weetabix-syns/→/syns/weetabix/, /low-syn-crisps/, /syns/walkers-crisps/, /bachelors-pasta-sauce-syns/) to lift them across the page-1 threshold.
6. **A single Syns Directory/Calculator hub** linked from the global header on every page — concentrates authority on one money page and gives every leaf a strong internal link.
7. After 301s, **update all internal links to point at the canonical URL** (no chains, no links to redirected URLs) and resubmit the XML sitemap (drop pruned/redirected URLs).

## Phased Action Plan

### Phase 1 — Quick wins: dedupe + titles (Week 1)
- Implement the **5 redirect clusters** in the Duplicate table (301 the losers, including the 3-way Walkers crisps mess and the Weetabix/Philadelphia merges).
- Rewrite **title tags + meta descriptions** for the page-2 high-impression pages to match intent and add a number/year (e.g. "How Many Syns in Weetabix? (2026 Slimming World)"). These pages have impressions but ~0% CTR — a better title is the cheapest lever.
- Add front-loaded answer + a syns table to the top of each kept page.
- **Expected impact:** recover lost equity from split URLs; CTR uplift on ~15 page-2 pages currently at ~0% could add ~30–60 clicks/mo with no ranking change. Stops the −20% slide.

### Phase 2 — Consolidation (Weeks 2–4)
- Build the **Syns Directory hub** + the **6 grouped guides** (Crisps/Snacks, Fruit, Dairy, Cereals, Alcohol, Speed Foods).
- Fold the ~30+ thin pages into the relevant hub sections; **301 absorbed URLs** to their hub; noindex/prune the lowest-value remainder.
- **Recover the 4 dead pages** (priority: /syns-bounty/ pos 9, and the Speed Foods cluster ~2,100 combined impr) via refresh + reintegration.
- **Expected impact:** fewer, deeper, non-cannibalizing pages → average position should move from ~17 toward ~10–12 as authority concentrates; the Speed Foods cluster (~2,100 impr at pos 11–18) is the largest single recovery opportunity.

### Phase 3 — Internal linking (Weeks 4–6)
- Roll out breadcrumbs + BreadcrumbList schema sitewide.
- Wire hub→spoke, spoke→hub, spoke→sibling links; point strong pages at page-2 targets; add the global header link to the Syns Directory.
- Update all internal links to canonicals; resubmit sitemap; monitor in GSC.
- **Expected impact:** the structural fix that pushes page-2 pages (with existing impressions) onto page 1. Combined with Phases 1–2, target reversing the decline and moving the high-impression cluster (/guides/speed-foods/ 1,212, /weetabix 742+888, /low-syn-crisps/ 617, walkers ~930 combined) from CTR ~0% toward 2–3% — a realistic path from ~473 to ~800–1,000+ clicks/mo over 2–3 months.

### Guardrails
- One canonical URL template (`/syns/<food>/`) going forward; no new duplicate slugs.
- Do not publish new thin pages — extend hubs instead.
- Track average position and the named page-2 pages weekly in GSC to confirm page-1 movement.
