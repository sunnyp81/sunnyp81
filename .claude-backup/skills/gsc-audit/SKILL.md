---
name: gsc-audit
description: Comprehensive Google Search Console SEO audit for agencies. Use when asked for "GSC audit", "Search Console analysis", "CTR optimization", "content decay", "keyword cannibalization", "striking distance keywords", or SEO opportunities from GSC data. Requires GSC MCP connection.
version: 1.0.0
user-invocable: true
allowed-tools: mcp__gsc__*, Read, Write, WebSearch, WebFetch
argument-hint: "[GSC property e.g. sc-domain:example.com]"
---

# GSC SEO Audit

Generate a comprehensive SEO audit report from Google Search Console data. Analyzes 7 key areas and produces actionable recommendations.

## What This Audit Covers

| Analysis | What It Finds |
|----------|---------------|
| **Index Coverage** | % pages indexed, time to index, crawl frequency — THE primary KPI |
| CTR Optimization | Pages ranking well but getting fewer clicks than expected |
| Content Decay | Pages losing traffic vs previous period |
| Quick Wins | Keywords at positions 11-20 with decent volume |
| Cannibalization | Multiple pages competing for same keyword |
| Mobile/Desktop Gap | Pages performing differently across devices |
| Dead Pages | Pages that dropped to zero traffic |
| Brand vs Non-Brand | Traffic dependency on branded searches |
| Query Diversity | How many unique queries each page attracts |

## Prerequisites

Requires **GSC MCP server**. First time? Read `references/setup-guide.md`. If "GSC tools not found" errors, check troubleshooting in that file.

## Workflow

### Phase 0: Property Selection
Call `mcp__gsc__list_properties`, present list, ask which to audit.

### Phase 1: Configuration
Ask user (with defaults): brand terms, analysis period (default: 28d), which analyses (default: all), high-value URL patterns (default: `/pricing`, `/demo`, `/contact`, `/buy`, `/signup`).

### Phase 2: Data Collection

Run these MCP calls (show progress to user):

| Purpose | MCP Call | Key Params |
|---------|----------|------------|
| **Index Coverage** | `get_sitemaps` + `inspect_url_enhanced` (sample 20 URLs) | Check indexed vs submitted ratio |
| **Query Diversity** | `get_advanced_search_analytics` | dimensions: "query,page", row_limit: 5000, sort_by: "impressions" desc |
| CTR + Quick Wins | `get_advanced_search_analytics` | dimensions: "page", row_limit: 2000, sort_by: "impressions" desc |
| Content Decay + Dead | `compare_search_periods` | period1: last 28d, period2: previous 28d, dimensions: "page", limit: 500 |
| Cannibalization | `get_advanced_search_analytics` | dimensions: "query,page", row_limit: 5000, sort_by: "impressions" desc |
| Mobile/Desktop | `get_advanced_search_analytics` | dimensions: "page,device", row_limit: 1000, sort_by: "impressions" desc |
| Brand vs Non-Brand | `get_advanced_search_analytics` | dimensions: "query", row_limit: 2000, sort_by: "clicks" desc |

### Phase 3: Analysis

Process data per analysis section below.

### Phase 4: Report Delivery

1. Present summary with counts and top-line metrics
2. Ask if user wants full report
3. Offer CSV export for any section

---

## Analysis Logic

### 0. Index Coverage (PRIMARY KPI)

Search volume is unreliable. Index coverage is the real signal of semantic traction.

**Step 1:** Get sitemap URLs count via `mcp__gsc__get_sitemaps`
**Step 2:** Sample 20 URLs across site sections via `mcp__gsc__inspect_url_enhanced`
**Step 3:** Calculate metrics:

| Metric | How to Calculate | Health Threshold |
|--------|-----------------|-----------------|
| % Pages indexed | (indexed URLs / total sitemap URLs) x 100 | >80% = healthy, 50-80% = concern, <50% = critical |
| Time to index | Check last crawl date on recently published pages | <7 days = fast, 7-30 = normal, >30 = slow |
| Query diversity per page | Unique queries / indexed pages (from query+page data) | >5 queries/page = strong, 2-5 = average, <2 = thin |
| Crawl frequency | Last crawl dates across sample — look for pattern | Weekly = active, monthly = low priority, >60d = abandoned |
| Index coverage by directory | Group by URL path prefix → % indexed per section | Identify sections Google ignores |

**Output (show FIRST in report — this is the lead metric):**
```
INDEX HEALTH: [HEALTHY/CONCERN/CRITICAL]
- Pages submitted: [X] | Pages indexed: [X] ([Y]%)
- Avg queries per page: [X]
- Avg time to index: [X] days
- Crawl frequency: [pattern]

Worst sections (by index rate):
| Directory | Submitted | Indexed | Rate | Issue |
```

**Diagnosis:**
- Low index rate + high crawl frequency = quality issue (Google sees but rejects)
- Low index rate + low crawl frequency = discovery issue (Google doesn't visit)
- High index rate + low queries/page = thin content (indexed but not ranking)

### 1. CTR Optimization
Filter pages: position < 20, impressions > 50. Look up expected CTR from `references/ctr-benchmarks.md`. Flag where `actual_ctr < expected_ctr * 0.7`. Calculate `potential_clicks = impressions * ctr_gap`. Sort by potential_clicks desc.

Output: `| Page | Position | Impressions | Actual CTR | Expected CTR | Gap | Potential Clicks |`

### 2. Content Decay
Calculate `pct_change = (new_clicks - old_clicks) / old_clicks`. Flag pages with >25% loss. Diagnose: position dropped >2 = "Position decay", CTR dropped = "CTR decay", both = "Full decay". Sort by absolute click loss.

Output: `| Page | Old Clicks | New Clicks | % Change | Old Pos | New Pos | Diagnosis |`

### 3. Quick Wins (Striking Distance)
Filter query+page: position 11-20, impressions >= 100. Sort by impressions desc. Group by page.

Output: `| Query | Page | Position | Impressions | Clicks | CTR |`

### 4. Cannibalization
Group query+page by query. Filter queries with 2+ pages. Exclude brand terms. Sort by total impressions. Within groups, sort by position.

Output per group:
```
**Query: "keyword"** (X pages competing, Y total impressions)
| Page | Position | Impressions | Clicks |
*Recommendation: [consolidate/differentiate]*
```

### 5. Mobile vs Desktop Gap
Pivot page+device data to desktop/mobile per page. Flag pages with `ctr_ratio > 2` OR `pos_gap > 5`. Diagnose: mobile CTR lower = "Mobile UX issue", mobile position worse = "Mobile content issue".

Output: `| Page | Desktop CTR | Mobile CTR | Ratio | Desktop Pos | Mobile Pos | Gap | Issue |`

### 6. Dead Pages
From period comparison: previous clicks > 0, current clicks = 0, exclude <10 previous clicks. Auto-inspect top 5 via `mcp__gsc__inspect_url_enhanced`.

Diagnose by index status: "Submitted and indexed" = traffic shifted, "Crawled - currently not indexed" = quality issue, "Discovered - currently not indexed" = crawl budget, "URL is not on Google" = blocked/noindex, "Page with redirect" = check chain.

Output: `| Page | Previous Clicks | Previous Impressions | Index Status | Last Crawl | Issue |`

### 7. Brand vs Non-Brand
Classify queries as brand/non-brand. Calculate totals (clicks, impressions, avg CTR, position). Health: >60% non-brand = Healthy, 40-60% = Moderate, <40% = Needs work. Include top 10 non-brand queries.

### 8. Query Diversity
From the query+page data collected in Phase 2, calculate unique queries per indexed page.

| Metric | Calculation | Threshold |
|--------|-------------|-----------|
| Queries per page (avg) | Total unique queries / total pages with impressions | >5 = strong, 2-5 = average, <2 = thin |
| Pages with 0 queries | Pages in sitemap but no GSC impressions | Flag for content quality review |
| Pages with 50+ queries | Pages ranking for many terms | Potential split candidates |

Output: `| Page | Unique Queries | Total Impressions | Avg Position | Assessment |`

Flag: pages with high impressions but low query diversity = narrow content. Pages with low impressions but high diversity = emerging authority.

### 9. Bing Index Status
Check Bing indexation (critical for Copilot/AI search visibility):

- Use `mcp__bing__get_url_info` to sample 10-20 URLs
- Or use `mcp__bing__get_page_stats` for overall site stats
- Calculate % of pages indexed in Bing vs Google

| Bing Status | Meaning | Action |
|-------------|---------|--------|
| Not in Bing at all | Site not verified/submitted | Submit via `/index-push --bing-only` |
| <50% of Google pages | Partial indexation | Submit sitemap + batch URLs |
| >80% of Google pages | Good parity | Monitor quarterly |

**Why:** Copilot relies entirely on Bing index. Sites missing from Bing are invisible to ~30% of AI search.

---

## Report Format

```markdown
# GSC Audit Report: [domain]
**Generated:** [date] | **Period:** [start] to [end]

## Index Health: [HEALTHY/CONCERN/CRITICAL]
- Pages indexed: X/Y ([Z]%)
- Avg queries per page: [X]
- Crawl frequency: [pattern]
- Time to index: [X] days

## Executive Summary
- X CTR opportunities (+Y potential clicks/month)
- X content decay pages (lost Y clicks)
- X striking distance keywords
- X cannibalized queries
- X mobile issue pages
- X dead pages
- Non-brand health: [status]
- Query diversity: [avg queries/page]

## 0-8. [Each analysis section with tables]
```

## CSV Export

Format each section as CSV with headers on request.

## Error Handling

| Error | Response |
|-------|----------|
| GSC MCP not found | Offer setup guidance via `references/setup-guide.md` |
| No properties | Check Google account has verified properties |
| Insufficient data (<100 impressions) | Warn audit may not be meaningful, ask to continue |
| Rate limiting | Wait 30s and retry |
