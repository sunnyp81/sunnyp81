---
name: ctr-rewrite
description: Batch CTR title and meta description rewriter from GSC data. Use when asked to fix low CTR, rewrite titles, optimise meta descriptions, or improve click-through rates across a site or list of pages. Pulls live GSC data, analyses competitor SERP titles, and outputs bulk rewrites with before/after comparison. Serves Hummingbird retainer CTR deliverables.
version: 1.0.0
user-invocable: true
allowed-tools: mcp__gsc__*, WebSearch, Read, Write
argument-hint: "[sc-domain:example.com or page-list.csv] [--pages N] [--min-impressions N]"
---

# CTR Rewrite — Batch Title & Meta Optimiser

Pull low-CTR pages from GSC, analyse what's winning in the SERP, and output ready-to-deploy title/meta rewrites with uplift rationale.

## Arguments

- `property` (required): GSC property e.g. `sc-domain:bestreviews.co.uk`
- `--pages N` (optional): Max pages to rewrite. Default: 10
- `--min-impressions N` (optional): Only include pages above this impression threshold. Default: 200
- `--ctr-threshold N` (optional): Only include pages below this CTR %. Default: 3.0
- `--output` (optional): File path to save output. Default: `G:\My Drive\SEO\reports\ctr-rewrites-{domain}-{date}.md`

## Phase 1: Pull GSC Data

Call GSC to get pages sorted by impressions with CTR below threshold:

```
Call: mcp__gsc__get_advanced_search_analytics
Params: {
  siteUrl: "{property}",
  startDate: "{28 days ago}",
  endDate: "{today}",
  dimensions: ["page"],
  rowLimit: 500
}
```

Filter results to pages where:
- `impressions >= min-impressions`
- `ctr < ctr-threshold / 100`
- `position <= 30` (ranking but not clicking)

Sort by `impressions DESC` — highest volume opportunities first. Take top N pages.

## Phase 2: Get Current Titles & Queries Per Page

For each page, find its top driving query:

```
Call: mcp__gsc__get_search_by_page_query
Params: {
  siteUrl: "{property}",
  page: "{page_url}",
  startDate: "{28 days ago}",
  endDate: "{today}"
}
```

Also attempt to read the current `<title>` and `<meta name="description">` from the live page:

```
Call: mcp__gsc__inspect_url_enhanced
Params: { siteUrl: "{property}", inspectionUrl: "{page_url}" }
```

If you can't fetch live page content, note "title unknown — rewrite based on URL + query".

## Phase 3: SERP Competitor Analysis

For each page's top query, run a web search and extract the top 5 organic result titles:

```
WebSearch: "{top query}" site:not:{domain}
```

Analyse the SERP titles for:
- **Number patterns**: "7 Best…", "Top 10…", "£X–£Y"
- **Power words**: "Best", "Cheap", "Fast", "Reviewed", "UK", current year
- **Question formats**: "What Is…", "How to Choose…"
- **Urgency/recency signals**: "2026", "Updated", "Tested"
- **Pain point targeting**: "for Small Kitchens", "Under £50", "for Beginners"
- **UK specificity signals** (if .co.uk site): £, UK, British

Identify the dominant pattern for that SERP — replicate it.

## Phase 4: Write Rewrites

For each page produce:

### Title Rewrite Rules
- Max 60 characters (Google truncates at ~580px width)
- Lead with the primary keyword or a number
- Include a differentiator (year, UK, "Reviewed", price range)
- No all-caps, no keyword stuffing
- Match the dominant SERP pattern you identified
- British English for .co.uk domains

### Meta Description Rewrite Rules
- 140–155 characters
- Open with an action verb or key benefit
- Include the primary keyword naturally once
- End with an implicit CTA ("Find the right X for your needs")
- No "Click here" or "Learn more" fillers
- Answer the searcher's implied question in one sentence

Produce **2 variants per page** (A: conservative match SERP pattern, B: more differentiated).

## Phase 5: Output Report

```markdown
# CTR Rewrite Report — {domain}
**Generated**: {date} | **Period analysed**: {date range}
**Pages audited**: {N} | **Avg CTR before**: {X}% | **Est. CTR after** (conservative): {Y}%

---

## Page Rewrites

### {page_url}
**Top query**: {query}
**Impressions**: {N} | **Current CTR**: {X}% | **Current position**: {P}
**SERP dominant pattern**: {e.g. "Top N listicle with year"}

| | Title | Meta Description | Length |
|--|-------|-----------------|--------|
| **Current** | {current title} | {current meta} | {len chars} |
| **Variant A** | {rewrite A} | {meta A} | {len chars} |
| **Variant B** | {rewrite B} | {meta B} | {len chars} |

**Why this will improve CTR**: {1–2 sentence rationale}

---

(repeat for each page)

## Implementation Notes
- Deploy via WordPress Yoast/Slim SEO, Keystatic frontmatter, or CMS meta fields
- Monitor in GSC: allow 14–28 days before comparing CTR
- If CTR doesn't improve in 28 days, try Variant B
- Re-run this skill in 30 days to track progress
```

## Hummingbird Retainer Usage

When running for Mike Lovatt's sites (T1-T8 pages), cross-reference the client tracker at `G:\My Drive\clients\hummingbird\` and update the deliverables log after output is approved.

## Notes

- This skill identifies and rewrites. It does NOT deploy — deploy separately via CMS or WP API.
- CTR improvement estimates are directional (+30–80% on pages <1% CTR is common)
- A 1% → 3% CTR lift on a 10,000 impression page = +200 clicks/month with zero new rankings
