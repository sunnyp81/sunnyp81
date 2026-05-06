---
name: site-health
description: Comprehensive site health check combining GSC data, SERP analysis, and content audit into a single diagnostic report with prioritized action items.
user-invocable: true
allowed-tools: mcp__gsc__*, WebSearch, WebFetch, Read, Write
argument-hint: "[site-url e.g. sc-domain:goldpenguin.org]"
version: 1.0.0
---

# Site Health Check

Comprehensive site health assessment combining GSC performance data, SERP analysis, and content quality evaluation.

## Arguments

- `site` (required): The GSC property URL (e.g. `sc-domain:goldpenguin.org`)
- `focus` (optional): Specific area to deep-dive (traffic, rankings, content, indexing)
- `output` (optional): File path to save report. Defaults to `G:\My Drive\SEO\sites\{domain}\health-report.md`

## Instructions

You are a **Senior SEO Strategist** performing a comprehensive site health assessment. Combine multiple data sources into a single, actionable report.

### Process:

**Phase 1: GSC Performance Pull**
- Pull last 90 days vs previous 90 days performance data
- Get top 50 queries and pages by clicks
- Identify all declining queries (>20% click loss)
- Identify all declining pages (>20% click loss)
- Check indexing status if tools available

**Phase 2: SERP Presence Analysis**
For the top 5-10 declining queries:
- Search Google for each query
- Check where the site currently ranks (if visible)
- Identify what types of content are ranking (format, length, structure)
- Note any SERP feature changes (AI overviews, featured snippets, PAA)
- Identify if competitors have overtaken with better content

**Phase 3: Content Quality Spot-Check**
For the top 3-5 declining pages:
- Fetch the page content via WebFetch
- Assess against Koray's micro-semantic standards:
  - Does it start with answers?
  - Is the heading hierarchy clean?
  - Are there signs of thin/outdated content?
  - Is the topical focus clear?
- Note any obvious technical issues (slow load, broken elements)

**Phase 4: Diagnosis & Report**

```markdown
# SITE HEALTH REPORT: {domain}

**Date**: {date}
**Assessment Period**: Last 90 days vs previous 90 days

## HEALTH SCORE: {X}/100

### Score Breakdown
- Traffic Trend: {X}/25
- Ranking Stability: {X}/25
- Content Quality: {X}/25
- Technical Health: {X}/25

## EXECUTIVE SUMMARY

[2-3 sentences: What's happening, why, and what to do about it]

## TRAFFIC ANALYSIS

### Overall Trend
| Metric | Current 90d | Previous 90d | Change |
|--------|------------|-------------|--------|
| Clicks | X | X | +/-X% |
| Impressions | X | X | +/-X% |

### Traffic Classification
- **[Growing/Stable/Declining/Critical]**
- Decline started approximately: [date estimate if declining]
- Likely triggers: [algorithm update, content decay, competition, etc.]

## RANKING ANALYSIS

### Position Changes
- Queries improving: X
- Queries stable: X
- Queries declining: X
- Queries lost (dropped off page 1): X

### Key Ranking Losses
| Query | Old Pos | New Pos | Monthly Clicks Lost |
|-------|---------|---------|-------------------|
| ... | ... | ... | ... |

### SERP Landscape Changes
[For each checked query, note SERP feature changes]

## CONTENT QUALITY ASSESSMENT

### Pages Audited
For each declining page:
- **URL**: [url]
- **Issue**: [what's wrong]
- **SERP Gap**: [what competitors do better]
- **Fix Priority**: [High/Medium/Low]

## PRIORITIZED ACTION PLAN

### Critical (Do This Week)
1. [Specific action with URL/query reference]
   - **Impact**: [estimated click recovery]
   - **Effort**: [Low/Medium/High]

### Important (Do This Month)
1. [Action]

### Strategic (Next Quarter)
1. [Action]

## MONITORING PLAN
- Re-check these metrics in [X] days
- Key queries to watch: [list]
- Key pages to watch: [list]
```

**5. Save Report**
- Save to specified output path or default
- Create site directory if needed

### Scoring Guidelines:

**Traffic Trend (25 pts)**
- 25: Growing >10%
- 20: Stable (-5% to +10%)
- 15: Mild decline (-5% to -20%)
- 10: Significant decline (-20% to -50%)
- 5: Critical decline (>-50%)

**Ranking Stability (25 pts)**
- 25: Most queries improving or stable
- 15: Mixed — some improving, some declining
- 5: Widespread ranking losses

**Content Quality (25 pts)**
- 25: Content meets semantic SEO standards, fresh, comprehensive
- 15: Some content issues, needs updates
- 5: Major quality gaps, thin content, outdated

**Technical Health (25 pts)**
- 25: No issues found
- 15: Minor issues (some indexing problems)
- 5: Major issues (widespread indexing/crawling problems)
