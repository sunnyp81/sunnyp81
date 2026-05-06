---
name: ai-seo
description: AI search presence strategy — build citation-worthiness across ChatGPT, Perplexity, Google AI Overviews, Copilot, and Claude. Covers entity optimization, SCDL management, disambiguation, mentions economy, third-party presence, and citation monitoring.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write, mcp__gsc__*
argument-hint: "[domain or URL to analyze]"
version: 1.0.0
---

# AI SEO — Search Presence Strategy

Build and monitor your site's presence across AI search platforms. Two complementary layers:

1. **Content layer** — structure, authority signals, content types that get cited
2. **Entity layer** — what AI engines "know" about you, disambiguation, reputation

While `/geo-optimizer` optimizes individual content, this skill focuses on **overall presence strategy**.

## When to Use

- Planning which content types to create for AI citation
- Auditing what AI currently "thinks" about a site/brand (SCDL audit)
- Building third-party presence (where AI engines find you)
- Fixing AI misrepresentation or entity confusion
- Setting up citation monitoring
- Deciding content strategy for new or existing sites

## Reference files (load on demand)

- `references/scdl-framework.md` — Entity Layer deep-dive: SCDL theory, 4-phase build process, mentions economy, query fan-out, watchdog role. **Read when:** auditing entity presence, fixing AI misrepresentation, planning the canonical source / disambiguation strategy.
- `references/audit-process.md` — Full audit checklist (Entity E1-E5 + Technical T1-T6) plus the AI READINESS SCORE output template. **Read when:** running an audit and producing the scored report.
- `references/monitoring-and-tools.md` — AI bot crawl verification, manual citation test protocol, comparison vs `/geo-optimizer`, monitoring tools. **Read when:** setting up ongoing tracking or comparing tooling options.

## Key Statistics

- AI Overviews appear in **~45% of Google searches**
- They reduce website clicks by up to **58%**
- Brands are **6.5x more likely** cited via third-party sources than their own domains
- Optimized content gets cited **3x more often**
- Statistics and citations boost visibility **40%+**
- Schema markup improves AI visibility by **30-40%**

## Three Pillars

### 1. Structure — Make Content Extractable
AI engines extract **passages**, not pages. Structure for passage-level extraction:
- Clear definitions in opening sentences (40-60 words)
- Step-by-step blocks with numbered lists
- Comparison tables with clear column headers
- FAQ sections with concise answers
- Statistic blocks with attributed sources
- Summary boxes / key takeaways at section level

### 2. Authority — Become Citation-Worthy

| Method | Visibility Boost |
|---|---|
| Add cited sources (hyperlinked) | **+40%** |
| Add statistics with attribution | **+37%** |
| Add expert/study quotes | **+30%** |
| Write with authoritative tone | **+25%** |
| Write clearly (8th grade intro) | **+20%** |

### 3. Presence — Appear Where AI Looks

| Source | Citation Share | Action |
|---|---|---|
| Wikipedia | 7.8% of ChatGPT citations | Edit relevant articles with your data/citations |
| Reddit | 1.8% of ChatGPT citations | Genuine community participation, not spam |
| Industry publications | High | Guest posts, expert quotes, contributed articles |
| Review sites | Medium | Get listed on niche review/comparison sites |
| YouTube | Growing | Create video content, optimize descriptions |
| Quora | Low but steady | Answer questions authoritatively in your niche |

**For our portfolio**: Reddit + industry forums + niche directories. Wikipedia editing only where genuinely warranted.

## Content Types by AI Citation Share

Prioritise (ranked by how often AI cites them):

| Content Type | Citation Share | Priority for Portfolio |
|---|---|---|
| **Comparison articles** (X vs Y) | ~33% | HIGH — create for affiliate sites |
| **Definitive guides** | ~15% | HIGH — pillar content for all sites |
| **Original research / data** | ~12% | HIGH — data sites (wagearea, catchment, postcode) have this |
| **Best-of / listicles** | ~10% | MEDIUM |
| **Product pages** | ~10% | MEDIUM — affiliate product reviews |
| **How-to guides** | ~8% | MEDIUM — calculator.place, bookkeepingflow |
| **Opinion / analysis** | ~10% | LOW — unless backed by data |

## Schema Markup for AI Visibility

These schema types improve AI citation probability by 30-40%:
- `Article` / `BlogPosting` — every content page
- `HowTo` — process/tutorial content
- `FAQPage` — Q&A sections
- `Product` + `Review` / `AggregateRating` — product/review pages
- `ItemList` — listicles and comparison pages
- `Organization` — about/company pages
- `SpeakableSpecification` — key answer sections

## Audit workflow

When asked to audit a site for AI search readiness:
1. Read `references/audit-process.md` for the E1-E5 + T1-T6 checklist and the scored output template
2. If the site has entity-confusion or AI misrepresentation issues, also read `references/scdl-framework.md` for the canonical source / disambiguation playbook
3. If the user wants ongoing monitoring after the audit, read `references/monitoring-and-tools.md`

## Common Mistakes to Avoid

- Treating AI SEO as separate from traditional SEO — they overlap 80%
- Blocking AI bots in robots.txt (many hosts do this by default)
- Writing for algorithms not humans — AI engines reward natural, authoritative content
- Ignoring freshness — stale content gets dropped from AI citations fast
- Gating content behind JS rendering walls (our Astro SSG sites are fine)
- Keyword stuffing — measured **-10% penalty** in AI visibility
- Ignoring third-party presence — brands are 6.5x more likely cited via third parties
- Generic content without data — original data/stats are citation magnets
