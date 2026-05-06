---
name: ugc-affiliate
description: Generate authentic UGC-style affiliate content using real user opinions from Reddit, forums, and review sites. Creates review pages, comparison articles, and buying guides with genuine community voice.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[product/topic] [--type review|comparison|guide]"
version: 1.0.0
---

# UGC Affiliate Content Generator

Generate 800+ word affiliate content based entirely on real forum discussions, Reddit threads, and user feedback. Includes mobile-responsive comparison tables with authentic user quotes.

## Arguments

- `domain` (required): WordPress site domain
- `page-id` / `page-url` (optional): WordPress page to update
- `category` (required): Product category to research
- `affiliate-tag` (optional): Amazon affiliate tag (defaults to site config)
- `word-count` (optional): Target word count (default: 800, min: 500)

## Core Principles

**ALL content must reflect real UGC sources:** Forums (AVForums, MoneySavingExpert, DIYnot, PistonHeads), Reddit (r/AskUK, category subs), YouTube experts (RTINGS, Which?), expert testing reports.

**NEVER:** Make up quotes/experiences, use generic marketing speak, copy manufacturer descriptions, use LLM fluff ("delve", "unlock", "seamlessly", "it's worth noting").

---

## Process

### 1. UGC Research

**Search queries:** `"[product] reddit UK"`, `"best [product] forum UK"`, `"[product] vs [competitor] forum"`, `"avoid [product] reddit"`, `"[brand] customer service forum"`

**For each product, document:**
- Forum mention count, sentiment, price range
- Verbatim user quotes with attribution (forum name, username)
- Key points: features, complaints, price comparisons, alternatives
- Source URLs or descriptions

**Minimums:** 5+ forum sources per category, 3+ quotes per recommended product, at least 1 AVOID product, specific price comparisons from users, 60%+ thread consensus patterns.

### 2. Content Structure

**H1:** `[Category] UK: What Forum Users Recommend`

**Opening (40-50 words, extractive):** Top product + price + key benefit. Alternative + savings vs expensive option. Avoid warning with source. Key buying test.

**UGC Comparison Table (3+ products):**
- 5 columns max: Model, Price, Verdict, User Quote, CTA
- Gradient header (purple→blue), color-coded badges
- Amazon links with `white-space:nowrap;display:inline-block` on `<a>` tag
- CSS: `overflow-x:auto`, `min-width` on columns, `@media(max-width:768px)` responsive
- Buy column: always `min-width:140px`
- Badges: Green (#4CAF50) = REDDIT FAVORITE / BEST VALUE, Orange (#FF9800) = ALTERNATIVE, Red (#f44336) = AVOID

**H2: Forum Consensus: What [X]+ Threads Say** — Patterns across forums, % mentions, price comparisons.

**H3: Why Users Choose [Top Product]** — Benefits with sources, prices, features, quotes. Bullet format: `[Benefit] saves £[X] annually versus [alt]`

**H3: [Alternative]: The [Comparison] Alternative** — User comparisons, real quote (blockquote), savings, performance.

**H3: Why Forum Users Avoid [Bad Product]** — Complaints with thread counts, issues, pricing, service warnings.

**H2: [Technical/Cost Comparison]** — Data table with user-reported metrics and sources.

**H2: Installation/Setup** — User-reported time, difficulty, mistakes, professional costs.

**H2: Common Problems Forum Users Solve** — 2-3 issues with user solutions.

**H2: FAQ** — 3-5 H3 questions from forum consensus, cite sources.

**Closing (40-60 words):** Reinforce consensus, top pick + price, alternative, avoid warning.

### 3. Semantic SEO Compliance

Before deploying, verify:

- **Start-With-Answer (95%+):** Every sentence starts with answer/subject/action. No preamble.
- **Comma Rule (95%+):** Commas ONLY for lists/enumerations/ranges. No clause commas.
- **No LLM Fluff (0 instances):** delve, unlock, embark, seamless, elevate, "it's worth noting", "when it comes to"
- **Sentence Patterns (80%+):** Imperative, Specification, Benefit, User statement
- **Entity Clarity:** H1 includes entity + "UK" + "Forum Users". Context maintained throughout.
- **UGC Authenticity:** All claims backed by sources. Real verbatim quotes. Specific forums cited.

### 4. WordPress Deployment

Get credentials from `G:\My Drive\SEO\sites\[domain]\wordpress-config.md` or ask user.

**Backup first:** Save to `G:\My Drive\SEO\sites\[domain]\backups\page-[id]-[date].html`

**Format as Gutenberg blocks:** `<!-- wp:heading -->`, `<!-- wp:paragraph -->`, `<!-- wp:html -->` (tables), `<!-- wp:list -->`, `<!-- wp:quote -->`

Deploy via WP REST API: `curl -X POST "https://[domain]/wp-json/wp/v2/pages/[id]"`

### 5. Deployment Report

Generate report with: domain, page, category, word count, status, content structure summary, UGC source counts, semantic SEO score, and monitoring plan (Week 1: check Amazon CTR + GA + GSC; Week 2-4: weekly tracking).

---

## Quality Standards

| Aspect | Requirement |
|--------|-------------|
| Word count | 800+ minimum |
| User quotes | 15+ real, verbatim, attributed |
| Forum sources | 5+ cited by name |
| Content basis | 100% UGC (no invented experiences) |
| Table | 3-5 products, 1+ AVOID, mobile responsive, working affiliate links |
| Backup | Created before deployment |
| Blocks | Properly formatted WordPress Gutenberg |

## Error Handling

| Issue | Action |
|-------|--------|
| Insufficient UGC | Expand to US forums, YouTube experts. Lower to 3 sources minimum (note in report) |
| Product unavailable on Amazon | Use search URL or alternative retailer. Note "Check availability" |
| WordPress API fails | Save to file with manual paste instructions |

## Remember

**This skill builds TRUST through authenticity.** Position site as consumer advocate, not affiliate marketer.

Always include: 1+ AVOID product with warnings, real forum quotes (exact, attributed), honest quality warnings, user-made price comparisons, forum consensus percentages.

Generic: "The BWT WS555 is an excellent water softener with advanced smart technology..."
UGC: "Harvey quoted £2,500. I chose BWT for £500 instead and it's worked brilliantly for 4 years." - PistonHeads Forum User
