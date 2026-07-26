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

---

# Appendix: the five previously-blocked sites (2026-07-26, access granted)

Method unchanged from the main report: per-site Sonnet/Opus scanners over read-only source, Fable verified every load-bearing finding against source before it was recorded here, scores on the /ugc-review rubric (threshold 80/100) adapted site-level. Repo source is the deployed artifact for these static sites. Network note: reddit.com is blocked at the session proxy, so the mower-quote live re-verification queued in the main report is still outstanding; PubMed IS reachable, and was used to verify the redlighttherapy-expert citation finding directly (see below).

Coverage delta from the main report: the four sites listed there as "NO, repo private" are now audited (bestvibrationplates, techloved, redlighttherapy-expert, mugscafe), plus one not previously on the list, towerfanreviews, added this session.

| Site | Score | Verdict | Primary blocker |
|------|-------|---------|-----------------|
| redlighttherapy.expert | 34/100 | NO-GO | Fabricated PMIDs on YMYL + fictional medical reviewer in schema |
| bestvibrationplates.co.uk | 33/100 | NO-GO | Fictional personas live as named medical experts + fabricated studies |
| mugscafe.org | 41/100 | NO-GO | Fabricated lab tests + broken legal pages + rel/disclosure gaps |
| techloved.com | 48/100 | NO-GO | Unsubstantiated testing baked into schema + sitewide broken hub nav |
| towerfanreviews.uk | 73/100 | NO-GO | Hardcoded GA4 tracker contradicts the site's own privacy page |

---

## redlighttherapy.expert: 34/100, NO-GO (blockers)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC / review authenticity | 2 | 40 |
| Quick-scan / semantic | 14 | 25 |
| Table and technical | 12 | 25 |
| English (US audience, adapted) | 6 | 10 |

### BLOCKER: fabricated PMIDs on a YMYL health site (verified against PubMed)

879 PMID citations across 76 content files. I resolved a sample of 12 against PubMed: 8 point to entirely unrelated papers while the author/year/journal text next to them is often correct, i.e. a real citation with a hallucinated id number bolted on. According to PubMed, verified directly this session:

- `conditions/arthritis/index.md:280` cites PMID 28462276 as Hamblin's "Mechanisms and applications of the anti-inflammatory effects of photobiomodulation" (AIMS Biophys 2017). PMID 28462276 is actually "Emergency Presentation and Short-Term Survival Among Patients With Colorectal Cancer... Puerto Rico" ([DOI](https://doi.org/10.1177/2333392816646670)). The correct id for that Hamblin paper is 28748217 ([DOI](https://doi.org/10.3934/biophy.2017.3.337)), which the site cites correctly elsewhere, so the number was simply wrong here. The same page at `:29` also mislabels the journal as *BBA Clinical*.
- `science/670nm/index.md:147` cites PMID 16007521 for Karu on cytochrome c oxidase; it is actually "Increased risk of common infections in patients with... diabetes mellitus" ([DOI](https://doi.org/10.1086/431587)).
- `conditions/tinnitus/index.md:30` cites PMID 22913654 for an 830 nm cochlear-hair-cell study; it is "Effect of sex and estrogens on neuronal activation in an animal model of migraine" ([DOI](https://doi.org/10.1111/j.1526-4610.2012.02249.x)).
- `conditions/weight-loss/index.md:70` cites PMID 23566380 for "McRae and Boris (2013)" LLLT Zerona trial; it is "Polymer-coated nanoparticles interacting with proteins and cells" (ACS Nano) ([DOI](https://doi.org/10.1021/nn3059295)).
- Controls confirmed correct: PMID 24049929 (Avci, LLLT in skin) and PMID 28748217 (Hamblin, PBM anti-inflammatory), proving the errors are not a systematic offset. (Citation checks per PubMed.)

If the sampled error rate holds across 879 citations, several hundred references on a YMYL health site route readers to unrelated oncology/IVF/nanoparticle papers. This is the single most serious defect in the portfolio and it directly contradicts the site's own stated "every claim traced to its primary source" rule.

### BLOCKER: fictional "Dr. Maya Hollander, PhD" as medical reviewer in schema and on-page

`src/layouts/Article.astro:89` emits `author: { '@type': 'Person', name: 'Dr. Maya Hollander', jobTitle: 'Photobiomodulation researcher' }` on all ~230 pages, again as the nested `Review` author at `:112`, and renders an on-page "Medically reviewed / Dr. Maya Hollander, PhD" trust badge at `:144-156` (also `index.astro:69-70`, `public/llms.txt:9`). The byline is unconditional: there is no reviewed flag, so it appears even on pages nobody claims were reviewed. An invented person asserted as a PhD medical reviewer in machine-readable data on YMYL health content is the same fraud class as the OwnerVoices and bestvibrationplates persona issues.

### BLOCKER: fabricated first-party measurements and testing narratives

- `src/content/products/rle-pro-led-mask.mdx:63`: "Verified 35 mW/cm2 at contact. Independently measured with a Solar Light PMA2100 radiometer, our test unit, our methodology, our data." The product is `inStock: false`, `stockCount: 0`, no Stripe price id: it has never been sourced. Same file asserts "FDA-listed Class II medical device", a 12-month warranty, and a US fulfilment centre for hardware that does not exist.
- `ihome-mask-review/index.md:3-4` (the site's top-traffic page) H1/meta promise an "8-Week Test With Irradiance Measurements"; the body contains no such test, and its irradiance section at `:103` is honestly labelled a desk estimate. The claim is in the title and meta, not the body.
- 15 further review pages carry "we tested / we measured" in title or meta (`hooga-hg200-review:2`, `newkey-mask-review:3`, `lumebox-review:3`, `best-amazon-red-light-therapy:3`, and others). `public/llms.txt:8` tells AI crawlers devices are "independently tested for irradiance with a calibrated spectrometer"; no such instrument or data exists in the repo.

### Other verified findings

UGC: 6 "What Real Users Say" blocks, all attributed by source-category and year only, none with username, permalink, or exact date. A real named dermatologist (Dr. Whitney Bowe) is given a verbatim 4-sentence quote with no source (`ihome-mask-review:236`); Consumer Reports and Fortune are quoted/cited uncited (`:232`, `novaalab-review:219`). Product `ratingValue` is a hardcoded editorial number (`products.ts`, 12 literals) with no rubric. Images: the only raster image in the repo is of the non-existent RLE Pro product; zero images in 229 content files; Product schema never emits an image (the Amazon-image JSON is gitignored and absent). Content: 5,210 em dashes and 3,424 en dashes against the global no-dash rule; 58 of 96 affiliate pages carry no inline disclosure; tables have no overflow container (mobile converts ~3.5x desktop here). Passing: affiliate rel is correct on 157/157 links; no git conflict markers; prose register is genuinely good; the daily-publish pipeline indexes existing drafts, it does not generate content, so these fabrications are hand-committed March/April content, not accruing daily.

Decision: this site should be depublished from indexing or gated until (1) every PMID is re-verified against PubMed or removed, (2) the Maya Hollander persona is stripped from schema and page chrome, and (3) all "we tested/measured" claims and the RLE Pro spec/FDA/warranty claims are removed. The PMID fix gates the rest.

---

## bestvibrationplates.co.uk: 33/100, NO-GO (blockers)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC / persona authenticity | 2 | 40 |
| Quick-scan / semantic | 14 | 25 |
| Table and technical | 12 | 25 |
| British English | 5 | 10 |

### BLOCKER: the fictional personas are still live as named human experts (verified)

The repo's own CLAUDE.md claims the Jun 20 remediation moved authorship to Organization. That fix reached `Base.astro` only; the personas remain throughout content, frontmatter, and the homepage. Verified:

- `src/content/posts/about-us.md:29-55`: full fabricated bios with credentials ("Jasmine Sinclair... MCSP-registered physiotherapist with twelve years of clinical practice"; "Dr Ruth Pemberton... GP... Reviews every health-claim article before publication").
- ~20 YMYL health pages carry a "Reviewed by Dr Ruth Pemberton, GP, [date]" sign-off, e.g. `vibration-plate-blood-clots.md:124`, `vibration-plate-pregnancy-safety.md:104`, `vibration-plate-pacemaker.md:108`, plus physio-authored sign-offs (`vibration-plate-benefits-elderly.md:201`).
- 42 content files carry persona `@id` references in page JSON-LD (`#jasmine`, `#david`, `#dr-ruth`), including nested per-product `Review` ratings authored by the fake coach (`best-vibration-plates-weight-loss-uk.md:306`). A grep for `"@type": "Person"` across `src/` returns zero, so every one of those 88 `@id` references is also a dangling node: fictional AND broken.
- 49 files still carry `authored_by`/`contributors` persona frontmatter (`gravit8-review.md:7`); `Base.astro` currently ignores it, so it is dormant, but one template change re-publishes fake authorship.

### BLOCKER: fabricated first-party research and statistics (verified)

- `src/pages/index.astro:423`: "Our audit of 84 UK buyers found: oscillating plates show zero mechanical failures within 5 years..."; `:422`: "User Adherence Reality (18-Month UK Study, n=156)"; `:228`: "A 2023 NHS trial found..." (all uncited).
- The Jul 20 fabricated-statistics strip missed the worst offenders: `are-good-fibromyalgia.md` alone carries six invented studies with sample sizes (`:241` n=74, `:247` n=156, `:270` n=64, `:274` n=42, `:283` n=147, `:279`); `best-vibration-plates-seniors-elderly-uk.md` (a page that pass explicitly touched) carries six more (`:350` n=427, `:354` n=156, `:385` an invented ADASS care-home audit); plus an invented quote attributed to the real charity Action for M.E. (`are-good-fibromyalgia.md:231`).

### Other verified findings

UGC: 105 Reddit quotes, zero with a username, permalink, or date, though the underlying pull in `ugc-reddit-data.md` does hold real permalinks that were dropped on the way to the page; quotes are recycled across unrelated conditions and mismatched to subreddits (a fibromyalgia testimonial sourced to r/lipedema, `are-good-fibromyalgia.md:311`); seven "User Feedback Summary" blocks are editorial prose in user-voice framing. Implied hands-on measurement the site cannot have done ("chassis flex, deck deflection, temperature consistency across continuous 20-minute sessions", `reviews.md:66`). Scores are unsupported and self-contradictory (homepage "4.8 across 47 plates" derives from no repo data; LifePro Waver appears as 4.2, 4.4 and 4.6 on three pages; "47 plates compared" vs "16 reviewed"). Images: only 2 `<img>` tags sitewide, broken site-wide OG reference (`og-default.jpg` absent, only `.svg` exists), 6 product photos for the whole catalogue. Content: 926 em + 721 en dashes, plus orphaned hyphens where a prior dash sweep stripped a dash mid-word ("About Us-The Team", `about-us.md:2`). Technical: 107 of 225 Amazon links missing `sponsored`+`noreferrer`; 56 of 86 affiliate pages with no in-body disclosure; affiliate links generated from non-product room-layout headings ("View Council Flat Lounge on Amazon", `best-compact-vibration-plates-small-spaces-uk.md:232`); 5 broken internal links to a non-redirected slug. Passing: no git conflict markers (the Jun 9 regression has not recurred); wide money-page tables are overflow-wrapped. British English: US-spelled slug/title/meta on a YMYL page (`can-cause-diarrhea.md`), scattered americanisms, GBP/EUR currency mixing.

Decision: same class as the OwnerVoices blocker but larger. Strip all three personas from bios, sign-offs, frontmatter, and every JSON-LD `@id`; delete the fabricated homepage and per-page studies; the dash and rel/disclosure sweeps are secondary.

---

## mugscafe.org: 41/100, NO-GO (blockers)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC / review authenticity | 6 | 40 |
| Quick-scan / semantic | 16 | 25 |
| Table and technical | 11 | 25 |
| English | 8 | 10 |

### BLOCKER: sitewide fabricated testing, including an invented lab protocol (verified)

Every brand-review meta and body asserts hands-on testing the repo cannot support. The worst is a fabricated lab test with invented instrumentation-grade precision, `best-insulated-coffee-mugs.astro:100-101`: "We filled each mug with freshly brewed coffee at 82C and measured temperature at 30, 60, 90, and 120 minutes in a room at 21C. The YETI consistently delivered drinkable coffee (55C+) at 90 minutes." Also `jot-coffee-review.astro:189-192` (invented "Four testers preferred Jot... Three preferred Javy"), `stumptown-coffee-review.astro:149` ("pulled at 19g in / 38g out over 28 seconds"), and `black-rifle-coffee-review.astro:33`, where a fabricated "consistently score well in blind taste tests" claim ships inside FAQPage JSON-LD, eligible for rich results as fact. 16+ pages carry "we tested/brewed" meta descriptions.

### BLOCKER: footer links to three pages that do not exist, sitewide

`src/components/Footer.astro:81-83` links `/privacy-policy/`, `/affiliate-disclosure/`, and `/about/` on every page; none of those files exist in `src/pages/`. On an affiliate site, a 404 affiliate-disclosure link sitewide is both a trust and an FTC-compliance defect.

### Other verified findings

135 invented ratings (18 Review-schema `ratingValue` + 117 `rating:` props) with no stated methodology; no fake personas (author is correctly Organization, the one thing done right). Same ASIN `B07BWQP2J3` behind three differently-named, differently-priced Bones flavours (`bones-coffee-review.astro:52,65,78`). Affiliate hygiene: 13 review pages render `rel` missing `sponsored` (the `BrandCard` `sponsored` prop defaults false), and 18 raw `<a>` affiliate links bypass the sanctioned components entirely (the documented `BuyButton` has zero usages); the homepage renders affiliate cards with no `AffiliateDisclaimer`. Images: `og-default.png` and `favicon-32x32.png` are referenced but absent (every page emits a 404 OG image); 49 real local WebP images exist (contradicting the repo TODO), not hotlinked, with clean alt/dimensions. 390 em + 155 en dashes (no explicit dash rule in this repo, reported as data). Passing: tables are overflow-wrapped with thead; no git conflict markers; British English consistent.

Decision: create the three legal/about pages (or remove the footer links), strip the fabricated lab test and taste-test schema claim, fix the 13-page `rel` default and route affiliate links through the components, add the missing OG/favicon assets.

---

## techloved.com: 48/100, NO-GO (blockers)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC / review authenticity | 12 | 40 |
| Quick-scan / semantic | 15 | 25 |
| Table and technical | 12 | 25 |
| English | 9 | 10 |

Stack note (changes what "deployed" means): the `src/**` Astro tree is dead code. `package.json` build is `node build.mjs`, which copies nine raw-HTML directories into `dist/` verbatim (commit `10ae24c` "Switch build to static HTML copy (drop Astro)"). So the May-11 `placeholder={true}`/`UgcQuote.astro` concern is moot (that component is not built), but every finding below is from the actual deployed HTML.

### BLOCKER: unsubstantiated first-person testing baked into Article JSON-LD

The deployed pages carry specific hands-on "testing" data with false precision, several duplicated into `Article` schema `description` so they are asserted as structured fact. `wearables/oura/track-steps/index.html:303` (and FAQ schema `:22`): "Across about 60 walks... 3,840 steps / 4,020 steps / -4%..."; `wearables/oura/vs-whoop/index.html:303`: "Six months of dual-wear data, comparing both devices against a Polar H10 chest strap..."; `wearables/whoop/waterproof/index.html:303`: "40+ pool sessions... 4 ocean swims at UK beaches...". The byline author "Sunny Patel" is the real site owner (so this is unsubstantiated, not fabricated-persona), but the schema points every page's author URL at `https://techloved.com/about/`, which does not exist in the deployed site (only dead `src/pages/about.astro`).

### BLOCKER: core hub/breadcrumb navigation 404s sitewide

None of the hub index pages exist on disk (`wearables/index.html`, `wearables/oura/index.html`, `gadgets/index.html`, `fix/index.html`, `tools/index.html`, etc.), yet they are linked from breadcrumbs and nav on nearly every page (`/tools/` linked from 46 files, `/wearables/` from 12, `/fix/` from 15). The site's primary internal navigation is broken everywhere.

### Other verified findings

UGC is genuinely the strongest in the portfolio in places: a real `UGC_SOURCING.md` playbook (permalink + username + subreddit + date) is followed on 10 pages (15 quotes). But the 4 model-specific spoke pages it explicitly requires have zero quotes (`onewheel/tire-pressure/{gt,pint,pint-x,xr}`), two quotes share one submission-level URL for different usernames, and several quotes are 21-36 months old against the playbook's own 6-month freshness rule. Images: zero `<img>` tags anywhere and no `og:image` sitewide (a device-review site with no device photography). 888 em dashes against the portfolio no-dash convention (this repo has no local rule stating it). Passing: affiliate hygiene is clean (17/17 correct rel, single `techloved-21` tag, disclosure on every affiliate page); no git conflict markers; no LLM-fluff; UK English consistent.

Decision: build the missing hub pages (or fix the links) and either substantiate or reframe the schema-embedded testing narratives; the UGC system is close to a pass and is the model the other sites should copy.

---

## towerfanreviews.uk: 73/100, NO-GO (one blocker; otherwise the healthiest site in the portfolio)

| Dimension | Score | Max |
|-----------|-------|-----|
| UGC / review authenticity | 29 | 40 |
| Quick-scan / semantic | 21 | 25 |
| Table and technical | 13 | 25 |
| British English | 10 | 10 |

This site had its own audit and remediation pass on Jul 10 and it largely held: re-verified this session, the fabricated-testing rewrite, the /how-we-rate/ rename, the disclosure-above-first-CTA gate, ad-slot gating, computed hero stats, the Dyson AM07 merge, and self-hosted fonts all check out. Zero "we tested/measured/hands-on/lab" hits, zero fabricated statistics, zero UGC presented as verbatim quotes (owner sentiment is consistently paraphrased as "owners report", the correct pattern), zero em/en dashes (verified with a UTF-8 locale; the repo's own documented grep false-alarms under a C locale, worth knowing), zero broken internal links, correct rel on every affiliate CTA. The author entity is the real site operator, not an invented persona, and /how-we-rate/ honestly discloses that ratings are editorial judgment.

### BLOCKER: hardcoded GA4 tracker contradicts the site's own privacy page (verified)

`src/layouts/Base.astro` contains two GA4 blocks: the intended env-gated one (`{GA4_ID && ...}`, lines 66-76) and, directly below it at lines 77-84, an unconditional hardcoded tracker for `G-DQ0N4L2LC8` added by commit `62428c9` on Jul 11, one day after the audit pass. `src/pages/privacy.astro:18` branches on the same `GA4_ID` constant, and with `PUBLIC_GA4_ID` unset at build time the privacy page renders "We do not run any analytics or tracking scripts on this site, and we set no analytics cookies" while every page loads the tracker. There is no consent mechanism anywhere in the repo (zero grep hits). A live misrepresentation on the privacy page plus an unconsented analytics cookie is a UK GDPR/PECR exposure and, for this audit's purposes, a trust-page truthfulness failure. The fix is one of two single-line changes: delete the hardcoded block and set `PUBLIC_GA4_ID` in the build env, or keep the hardcoded block and hardcode the privacy page to disclose analytics.

### Remaining findings (verified)

- One residual testing-implication phrase survived the Jul 10 rewrite: "cross-referenced across multiple seasons to weed out models that start quiet but degrade" (`best-quiet-tower-fans.md:39`) on a site launched 2026-06-21. It is the exact phrase the repo's own AUDIT.md flagged as the canonical bad example. Reword to attribute the multi-season signal to owner reviews explicitly.
- Review schema `ratingValue` is a hardcoded editorial number per product; mitigated by the honest /how-we-rate/ disclosure, but a dormant `ratingBreakdown` field (per-axis Airflow/Noise scores, populated on 21 of 22 products, rendered nowhere) would resemble measured sub-scores if a future template change ships it without that context. Delete it or render it with the disclosure attached.
- 0 of 22 products have a real ASIN, so every CTA is a tagged Amazon search link (known open item, not a regression). No product photography exists; the honest generic SVG illustration is used sitewide, which passes the truthfulness standard but is a CTR gap.
- 9 meta descriptions run 161-165 chars; `SpecBox.astro:14` lacks loading/decoding attributes on a currently-dormant image path.

Decision: fix the GA4/privacy contradiction immediately (it is a one-line change either way), reword the one residual phrase, delete or properly contextualise ratingBreakdown. With those done this site re-scores in the low 80s and becomes the first GO in the portfolio; its research-led framing and honest methodology page are the template the other six should copy.

---

# Portfolio decisions, updated after the appendix (priority order)

1. redlighttherapy-expert: depublish or gate until PMIDs are re-verified or removed, the Maya Hollander persona is stripped from schema and page chrome, and the RLE Pro "verified 35 mW/cm2" / FDA / warranty claims are deleted. Worst site in the portfolio; YMYL with wrong citations.
2. bestvibrationplates: strip all three personas everywhere (bios, sign-offs, frontmatter, JSON-LD @id), delete the fabricated homepage and per-page studies. The Jun 20 "fix" only reached Base.astro; treat the CLAUDE.md claim as unreliable and re-verify after fixing.
3. mugscafe: remove fabricated lab tests and taste-test schema claims, create the three 404ing legal pages, fix the BrandCard rel default and raw affiliate links.
4. techloved: restore the missing hub index pages (sitewide nav 404s), substantiate or reframe the schema-embedded testing narratives, decide whether the real-owner testing claims are true (only Sunny knows).
5. towerfanreviews: fix the GA4/privacy contradiction and the one residual phrase; then it is the portfolio's first GO and its template.
6. Standing tooling shipped this session (sunnyp81/sunnyp81, branch claude/affiliate-ux-audit-fixes-87gc78): content guardrail CI (hermes/guardrail/), daily watchdog with Telegram heartbeat (portfolio-status.yml), four-layer propose/verify/guardrail/human-merge rollout (ux-audit.yml + hermes/ARCHITECTURE.md), weekly Claude sweep Routine. Adopt the guardrail caller workflow on each site repo as fixes merge.
7. Not yet audited: the ~10 recently-active affiliate repos identified this session (bestchainsaw-uk, bestcordlessdrills, topsewingmachines, bestturbotrainers, crosstrainerhome, dashboardcamreviews, e-bikereview, lockyourbike, colourlabelprinter, deadhangs-com) and the bestreviews-* network. Second wave.
