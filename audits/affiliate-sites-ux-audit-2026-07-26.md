# Affiliate Sites UX Audit: quick-scan content, UGC references, image references

Date: 2026-07-26
Method: multi-model. Sonnet x3 and Opus x2 ran the scans (source-level, read-only clones), Fable verified every load-bearing finding against source and made the verdicts. No live-site fetches were possible (session network policy blocks outbound), so findings are from repo source, which for these static Astro sites is the deployed artifact. Scores use the /ugc-review rubric (threshold 80/100), adapted site-level.

## Coverage

| Site | Repo | Audited | Why not |
|------|------|---------|---------|
| thebestmowers.co.uk | sunnyp81/thebestmowers | YES (full, 3 agents) | |
| towrating.org | sunnyp81/towrating | YES (full, 2 agents) | |
| bestvibrationplates.co.uk | private | NO | repo private, outside session scope; live fetch blocked |
| techloved.com | sunnyp81/techloved-rebuild | NO | same |
| redlighttherapy-expert | private | NO | same |
| mugscafe.org | unknown repo | NO | same |

To audit the remaining four the same way: approve the list_repos/add_repo prompts in a session, or run from an environment whose network policy allows outbound fetches.

---

## thebestmowers.co.uk: 48/100, NO-GO (blocker)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC authenticity | 0 (14 base, minus 20 fabrication deduction) | 40 |
| Quick-scan / semantic | 17 | 25 |
| Table and technical | 21 | 25 |
| British English | 10 | 10 |

### BLOCKER: OwnerVoices is fabricated UGC (verified)

`src/data/ownerVoices.ts:1-3` states the 25 statements are "representative of recurring owner feedback", i.e. authored paraphrases. `src/components/OwnerVoices.astro:26-27` renders them in quotation marks with a cite element naming real publishers (Which?, Trusted Reviews, Ideal Home, DIY Garden). That is synthesised text presented as verbatim quotes from named third parties, live on all three primary money hubs (best-lawn-mowers, cordless-lawn-mowers, best-battery-powered-lawn-mower-reviews-uk) plus 6 review pages. Supporting tells, all verified: zero first-person voice across 25 quotes, uniform house-style units across 13 supposedly different publishers, manufacturer trademark language ("ProSilence", "LeafCollect") attributed to Which?, a "gripe" that is a spec-sheet comparison (`ownerVoices.ts:66`), an unsourced "3.9 / 5 across UK reviews" aggregate (`:39`). The Voice type has no field for username, URL or date, so real attribution is structurally impossible. `CLAUDE.md:22` also claims PistonHeads as a source; it appears nowhere in the data.

Decision: remove or rebuild before any other work on this site. Either (a) delete OwnerVoices from all 9 pages, or (b) re-source it with real verbatim quotes carrying source + username/author + link + date, using the inline Reddit system as the template. Do not reword the citations to keep the text: the text itself is authored.

### UGC that passes: the inline Reddit system

17 blockquotes on 4 review pages (husqvarna-automower-305, mountfield-sp46, bosch-rotak-32-review, gtech-clm50), all with username + linked thread. Authenticity signals are strong (first-person, hedging, off-topic drift, thread IDs chronologically consistent, quotes against commercial interest). Defects: 0/17 dated; gtech page is effectively one thread presented as a survey (thread 1jye93e carries 5 of 17 quotes); `gtech-clm50/index.astro:131` missing space corrupts a username ("u/UsefulAd8513on"); `:122` claims r/lawncare as a source with zero quotes from it. Site-wide distinct forum sources: 3 vs the 5+ standard.

Other UGC fails: only 12 of 95 pages carry any UGC; 15 of 24 reviews have none; the only AVOID section (`cordless-lawn-mowers/under-200/index.astro:117-121`) names McGregor, Sovereign and Challenge negatively with zero citations, while `brands/mcgregor/` runs a positive hub for one of them. Methodology pages (`about/index.astro:40-46`, HowWeResearch) do not mention forums or Reddit at all, contradicting what is shipped.

### Image references: FAIL on truthfulness, PASS on hygiene (verified)

No real product photography exists. Roughly 15 generic stock or AI images (gen-ai-images.py prompts literally say "generic unbranded") are reused across 24 reviews keyed loosely by category:

- `compact_robotic_lawn_mower.webp` represents 4 different brands (Husqvarna, Bosch, Mammotion, Worx)
- `top_8_large_lawnmowers.webp`, a listicle graphic, is the Product schema image for 4 different ride-on mowers
- Mountfield SP46 (petrol) uses `powerful_electric_lawn_mower.webp` on-page and in `productReviewSchema` (`reviews/mountfield-sp46/index.astro:31,45`)
- No disclosure anywhere that images are illustrative, while alt text asserts brand and model specificity

Passing hygiene: 42/42 img tags have alt, width, height, loading; zero broken refs; zero placeholders; no hotlinking (the gitignored Amazon Creators API image path is ToS-compliant by design); all files under 300KB. Bloat: ~76 of 105 webp files are orphaned WP-migration leftovers, 18 byte-identical duplicate groups.

Decision: stop passing generic images into Product schema immediately (wrong-image structured data on review pages is a rich-results accuracy risk). Then either extend the existing Amazon Creators image pipeline to review heroes, or add an "illustrative image" disclosure and de-specify the alt text.

### Quick-scan content: PARTIAL

Strong: zero em dashes, zero LLM fluff, zero markdown tables, dense specific numbers, UK English clean, TOC injected site-wide, every review has a spec table, answer-first bullet pattern in reviews.
Gaps, verified: no colour-coded verdict badge system anywhere (PickCard rank and tier labels all one green, `PickCard.astro:31,43`, `brands/index.astro:58`); 8-column comparison table exceeds the 3-5 standard with no concluding sentence (`best-battery-powered-lawn-mower-reviews-uk/index.astro:184-205`); compare table with no framing sentence above or below (`compare/cordless-vs-petrol/index.astro:48-68`); H2s almost never question-phrased (3 of ~35 sampled); extractive openings run 57-75 words vs the 40-50 target and rarely name product + price in sentence one; review spec tables lack thead (24 pages); no min-width on any buy column.

---

## towrating.org: 53/100, NO-GO (blockers)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC authenticity / provenance | 2 | 40 |
| Quick-scan / semantic | 23 | 25 |
| Table and technical | 18 | 25 |
| English (US site, section waived) | 10 | 10 |

### BLOCKER 1: "Verified Specs" is unsubstantiated on a safety topic (verified)

Every trim page title and H1 carries "(Verified Specs)" (`TrimPage.astro:23`). No verification step exists anywhere in the pipeline. The 750-trim dataset is hand-authored literals in `scripts/build-hero-data.mjs` with a single free-text sourceNotes blob never rendered on any page; `sourceUrl` is always null on the hero path (`merge-lib.mjs:5-12`), so the source-citation line is dead code on every high-value page. Two of five "spec fields" are formulas, not data: tongueWeight = round(maxTow x 0.10) and hitchClass from a threshold, 750/750 records (`build-hero-data.mjs:25-26`), which also makes the quality gate largely self-satisfying (`quality-gate.ts:3-9`). Year-over-year spec sets are heavily duplicated across separately indexed year URLs (4Runner: 12 years, 3 distinct sets). The same footer sentence claims "verified" and "as-is" (`Footer.astro:27`). This is uncited towing-capacity data presented as verified, where a wrong number has real-world consequences.

Decision: remove "(Verified Specs)" from titles, H1s, homepage, WebSite JSON-LD and llms.txt until a per-record source field exists and renders. Spot-check the hero dataset against real manufacturer tow guides before re-adding any verification language. All 2026 model-year figures for 20 nameplates need checking; they were all populated as of lastUpdated 2026-04-27 with no citations.

### BLOCKER 2: fabricated evidence items (verified)

- `weight-distribution-hitches.mdx:154-172`: a "Real-World Scenario" with measurement-language specifics (910 lbs measured at 11.7%, 1.8 inch fender drop) backed by nothing in the repo. Rewrite as a worked example or delete.
- `j2807-towing-standard.mdx:14,156`: unattributed claim that documented owner-run Davis Dam climbs exist on truck forums, serialised into FAQPage JSON-LD. Cite a real thread or remove.
- Product + Offer schema with availability InStock pointing at a CarGurus affiliate search URL for vehicles the site does not sell (`schema.ts:21-29`, emitted per trim page). Remove the Offer or the whole Product block; structured-data misuse risk at ~1,216-page scale.
- Uncited legal claim repeated on every trim page and in FAQ JSON-LD: "most US states legally require trailer brakes above 3,000 lbs" (`prose.ts:35,52`); thresholds vary by state. Verify or soften.

### Quick-scan content: mostly PASS, one bad template defect

Data pages lead with the concrete tow figure, no preamble; zero em dashes; zero fluff. Defects, verified: `commonMistakes()` ignores its vehicleClass parameter and ships 5 identical sentences under an entity-specific H2 on every trim page site-wide (`prose.ts:31-39`), textbook duplicate content at scale; `TrimComparisonTable.astro:29` renders a stray ", " when hitchClass is null; that table is 6 columns; tables in `VehicleTypeHub.astro:23` and `UseCaseCrossroad.astro:22` lack the overflow-x-auto wrapper the other two table sites have; no TOC on 1,400-word guides; no safety disclaimer in Trim/Year page bodies (footer only), while `UseCaseCrossroad.astro:20` asserts "safely with margin to spare".

### Trust and consistency fixes

- Header brands the site "towrating.net" on every page; site is .org (`Header.astro:10`). Also the scraper UA.
- Affiliate disclosure names Amazon, CarGurus, TrueCar, eTrailer, MoneyGeek, CarShield (`affiliate-disclosure.astro:8`); only CarGurus and Amazon have call sites. Trim the list.
- Zero images site-wide (only og-default.png). Image standard is vacuously clean, but a car site with no vehicle imagery and one shared OG image for ~1,216 pages is a CTR and trust gap, noted not scored.
- No about, methodology, or contact page at all; no author entity. Nothing fabricated, but zero E-E-A-T surface on a safety topic.
- Frontier record's wikipediaUrl points to Nissan Navara (`hero-models.json:10087`).
- Affiliate CTAs exist only on TrimPage and YearPage; hubs and all 5 guides have zero monetisation.

---

## Blocked sites: what the vault already documents

Not audited this session (no repo access). Known standing issues from memory notes, to be confirmed when access is available:

- techloved.com: last note (May 11) says UGC quotes for top 10 pages still unsourced and `placeholder={true}` images not yet replaced. If still true it fails the UGC and image standards outright. Amazon links added Jun 11.
- bestvibrationplates.co.uk: top affiliate earner. Personas are fictional (standing rule: no real headshots), which is the same authenticity class of risk as the OwnerVoices blocker; worth an access-granted audit of how personas and any review schema present. Prior live conflict-marker corruption from the Hermes stash-pop cron is a content-integrity risk to re-check.
- redlighttherapy-expert: Review + Product JSON-LD added May 26 on auto-published content; verify the Review markup is backed by real reviews.
- mugscafe.org: Amazon UK/US tags configured; no audit data at all.

## Portfolio decisions (priority order)

1. thebestmowers: kill or re-source OwnerVoices (3 money hubs are exposed). Same session: fix the u/UsefulAd8513 spacing bug, remove the r/lawncare claim, add dates to the 17 Reddit citations.
2. thebestmowers: stop feeding generic images into productReviewSchema; add illustrative-image disclosure or wire real product images.
3. towrating: strip "(Verified Specs)" everywhere until per-record sourcing exists; delete or rewrite the WDH scenario; remove the InStock Offer schema; fix commonMistakes to actually use vehicleClass.
4. towrating: fix .net/.org branding, stray comma cell, disclosure partner list, add trim-page safety disclaimer.
5. Get access to the four private-repo sites and repeat this audit; techloved is the likeliest fail on all three standards per its own backlog notes.

Live-forum verification queue (needs network): the 9 Reddit threads behind the 17 mower quotes, the Davis Dam claim, and manufacturer tow-guide spot-checks for the towrating hero dataset.
