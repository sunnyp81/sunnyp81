---
name: keyword-cluster
description: Cluster raw keyword lists by semantic similarity and search intent. Groups thousands of keywords into actionable topic clusters with content recommendations.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[CSV file path or keyword list]"
version: 1.0.0
---

# Semantic Keyword Clusterer

Group raw keyword exports into intent-labeled topic clusters with content format recommendations.

## Portfolio Context

Clustering is used across the 44-site portfolio for:
- **New site planning**: Cluster keywords before building topical maps (e.g., redlighttherapy.tech, aifor.tech)
- **Content gap analysis**: Cluster GSC queries to find unserved clusters on existing sites
- **Cannibalization detection**: Find competing pages on large sites (wagearea.com 140K pages, catchment.school 27K pages)
- **Affiliate content planning**: Cluster commercial keywords for bestreviews.co.uk, mugscafe.org, techloved.com
- **Service page expansion**: Cluster service keywords for sunnypatel.co.uk (61K monthly search volume in keyword file)

Input sources: GSC exports (via MCP), Ahrefs CSVs, Semrush exports, or pasted keyword lists. UK market focus — use UK search volumes and UK spelling conventions.

## Process Steps

1. **Ingest** keyword list (CSV from GSC, Semrush, Ahrefs, or pasted list)
   - Accept columns: keyword, volume, position, clicks, impressions, CTR, URL
   - Normalize: lowercase, trim whitespace, remove duplicates
   - Note the source (GSC vs third-party) as volume accuracy differs

2. **Classify intent** per keyword
   - Apply intent rules from the table below
   - When ambiguous, check SERP composition (informational SERPs = mostly guides, commercial = mostly product pages)

3. **Cluster by semantic similarity**
   - Group keywords that would be satisfied by the SAME page
   - Primary signal: keywords sharing 3+ SERP results belong in the same cluster
   - Secondary signal: lexical overlap + modifier patterns (e.g., "best X", "X vs Y", "X review" = same cluster)
   - One cluster = one page — never split what Google treats as one intent

4. **Assign cluster metadata**
   - Cluster name = highest-volume keyword in the group (canonical query)
   - Total cluster volume = sum of all keyword volumes
   - Recommended content format based on dominant intent
   - Recommended URL: existing page (if one ranks) or "NEW"
   - Priority score: volume x business relevance (affiliate/lead gen potential)

5. **Detect cannibalization**
   - Flag clusters where 2+ existing URLs rank for keywords in the same cluster
   - Identify which URL is stronger (more keywords, better positions)
   - Recommend: consolidate into stronger URL, or differentiate intent

6. **Output** structured cluster map

## Intent Classification Rules

| Intent | Signals | Content Format | Monetization |
|---|---|---|---|
| **Informational** | what, how, why, guide, tutorial, does, can, meaning, explained | Long-form guide, FAQ, how-to | AdSense, email capture |
| **Commercial** | best, top, review, vs, compare, alternative, worth it | Comparison, listicle, review | Affiliate links, product cards |
| **Transactional** | buy, price, cost, cheap, deal, coupon, near me, hire, book | Product page, landing page, pricing | Direct sale, lead form |
| **Navigational** | brand name, login, site name, [domain] | Homepage, brand page | N/A |

## Clustering Method — Detailed

**Step 1: Seed grouping**
- Sort keywords by volume descending
- Take highest-volume keyword as first cluster seed
- Scan remaining keywords: if a keyword shares 3+ SERP results with the seed, add to cluster
- If no SERP data available, use lexical rules: same head term + different modifiers = same cluster

**Step 2: Merge small clusters**
- Clusters with <3 keywords: attempt to merge into a larger related cluster
- Solo keywords with <50 volume: mark as "long-tail" and assign to nearest cluster

**Step 3: Split over-broad clusters**
- Clusters with mixed intent (informational + transactional keywords): split by intent
- Clusters where the top keyword has >10x the volume of all others combined: check if it's truly one topic

## Output Format

```
# Keyword Cluster Report: [Site/Project]
Date: [date]
Total keywords: [X]
Clusters formed: [X]
Unclustered (long-tail): [X]

---

## Cluster: [Canonical Query] ([Total Volume])
Intent: [Informational/Commercial/Transactional]
Keywords: [count]
Format: [Guide/Comparison/Product/FAQ/Landing Page]
Recommended URL: [existing URL or "NEW — /suggested-slug"]
Priority: [1-5 based on volume x business relevance]
Monetization: [AdSense/Affiliate/Lead Gen/Email Capture]

Keywords in cluster:
- [keyword] ([volume]) [intent]
- [keyword] ([volume]) [intent]
...

---
```

## Cannibalization Detection

Flag clusters where 2+ existing URLs compete:
```
CANNIBALIZATION: "[cluster name]"
  - URL 1: [url] (ranks for X keywords, avg position Y)
  - URL 2: [url] (ranks for Z keywords, avg position W)
  Action: Consolidate into [stronger URL] — 301 redirect [weaker URL]
  OR: Differentiate — URL 1 targets [intent A], URL 2 targets [intent B]
```

## Priority Scoring

Calculate priority for each cluster:

```
Priority = (Total Volume / 1000) x Relevance Multiplier

Relevance Multiplier:
- 3x: Directly monetizable (affiliate, lead gen, transactional)
- 2x: Commercial investigation (comparison, review)
- 1x: Informational (guides, how-to)
- 0.5x: Navigational or branded
```

Score 1-5:
- 5: Priority > 10 (do immediately)
- 4: Priority 5-10 (this month)
- 3: Priority 2-5 (next 30 days)
- 2: Priority 1-2 (backlog)
- 1: Priority < 1 (low value, skip unless easy)

## When to Use This vs `/demand-map`

| Use This (`/keyword-cluster`) | Use `/demand-map` Instead |
|---|---|
| **New site** with no GSC data yet | Site has 3+ months GSC data |
| Working from Ahrefs/Semrush exports | Working from real user behavior data |
| Client keyword research (third-party data) | Your own portfolio sites |
| Broad niche exploration | Targeted content strategy for existing site |

**Rule:** For sites with GSC history, `/demand-map` gives more accurate demand signals because it uses real queries Google associates with your site, not tool estimates.

## Integration with Other Skills

- **Output feeds into** `/topical-map` — clusters become NODE and SEED topics in the topical architecture
- **Output feeds into** `/semantic-brief` — individual clusters become content briefs
- **Cannibalization flags feed into** `/content-config` — for content reconfiguration and consolidation
- **Input from** `/gsc-audit` — GSC query data is the best clustering input for existing sites
- **Input from** `/content-decay` — declining keywords may need reclustering
- **Complements** `/content-calendar` — prioritized clusters drive the publishing schedule
- **Superseded by** `/demand-map` for sites with GSC data — demand-map clusters by entity+task, not just keyword similarity
