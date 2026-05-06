---
name: client-report
description: Generate professional client-facing SEO performance reports for retainer clients. Use when producing monthly reports for agency clients (e.g. Hummingbird/Mike Lovatt). Pulls GSC data, documents deliverables completed, writes an executive narrative, and outputs a clean shareable report. Distinct from revenue-report (internal) and portfolio-report (all sites).
version: 1.0.0
user-invocable: true
allowed-tools: mcp__gsc__*, Read, Write, Glob
argument-hint: "[client-name] [sc-domain:property] [--month YYYY-MM]"
---

# Client Report — Professional SEO Performance Report

Generate a client-facing monthly SEO report: what happened, why, what's next. Professional narrative format suitable for sending directly to a client.

## Arguments

- `client` (required): Client name e.g. `hummingbird`
- `property` (required): GSC property e.g. `sc-domain:hummingbirddigital.co.uk`
- `--month` (optional): Target month YYYY-MM. Default: previous complete month
- `--output` (optional): Save path. Default: `G:\My Drive\clients\{client}\reports\{month}-report.md`

## Step 1: Load Client Context

Read the client file at `G:\My Drive\clients\{client}\` — look for:
- `CLAUDE.md` or `brief.md` — client goals, KPIs, deliverables
- `reports\` folder — previous month reports for comparison baseline
- Any tracker spreadsheet references

For Hummingbird specifically: read `G:\My Drive\_SHARED\memory\client-work.md` for current targets and deliverables tracker.

## Step 2: Pull GSC Data

### Overview metrics (current month vs prior month)
```
Call: mcp__gsc__get_search_analytics
Params: {
  siteUrl: "{property}",
  startDate: "{month start}",
  endDate: "{month end}",
  dimensions: []
}
```

### Top pages by clicks
```
Call: mcp__gsc__get_advanced_search_analytics
Params: {
  siteUrl: "{property}",
  startDate: "{month start}",
  endDate: "{month end}",
  dimensions: ["page"],
  rowLimit: 20
}
```

### Top queries
```
Call: mcp__gsc__get_advanced_search_analytics
Params: {
  siteUrl: "{property}",
  startDate: "{month start}",
  endDate: "{month end}",
  dimensions: ["query"],
  rowLimit: 20
}
```

### Compare to prior period
```
Call: mcp__gsc__compare_search_periods
Params: {
  siteUrl: "{property}",
  startDate1: "{month start}",
  endDate1: "{month end}",
  startDate2: "{prior month start}",
  endDate2: "{prior month end}",
  dimensions: ["page"]
}
```

## Step 3: Identify Key Movements

From the data, identify and note:
- **Biggest winners**: Pages that gained the most clicks vs prior month
- **Biggest decliners**: Pages that lost clicks vs prior month
- **CTR opportunities**: Pages with impressions >500 but CTR <2%
- **Quick win positions**: Queries ranking 11–20 (one step from page 1)
- **New rankings**: Queries appearing this month that weren't in prior month

## Step 4: Deliverables Log

Ask or read from the client tracker: what was delivered this month?

Format: "In {month}, we delivered: [list]"

Examples:
- Published X new pages
- Rewrote titles/meta on X pages
- Fixed X technical issues
- Built X backlinks
- Set up Google Business Profile

Cross-reference against the agreed scope/retainer deliverables.

## Step 5: Write the Report

### Report Format

```markdown
# SEO Performance Report — {Client Name}
**Period**: {Month Year} | **Prepared by**: Sunny Patel, sunnypatel.co.uk
**Report date**: {date}

---

## Executive Summary

{2–3 sentence narrative. What was the headline result? Was it up or down? Why? What's the focus for next month?}

Example: "Organic clicks grew 18% month-on-month to 612, driven by the 7 new service pages published in the first week of March. Impressions held steady at 28k, and average CTR improved from 0.23% to 0.31% following title rewrites on the top 8 pages. Next month's focus is pushing 6 pages from position 12–18 onto page 1."

---

## Traffic Overview

| Metric | {Month} | {Prior Month} | Change |
|--------|---------|--------------|--------|
| Total Clicks | {N} | {N} | {+/-N} ({+/-X}%) |
| Total Impressions | {N} | {N} | {+/-N} ({+/-X}%) |
| Average CTR | {X}% | {X}% | {+/-X}% |
| Average Position | {X} | {X} | {+/-X} |

**Trend**: {Up / Down / Stable} — {one sentence context}

---

## Top Performing Pages

| Page | Clicks | Change vs Prior |
|------|--------|-----------------|
| {page} | {N} | {+/-N} |
| {page} | {N} | {+/-N} |
| {page} | {N} | {+/-N} |
| {page} | {N} | {+/-N} |
| {page} | {N} | {+/-N} |

---

## Top Queries

| Query | Clicks | Position | CTR |
|-------|--------|----------|-----|
| {query} | {N} | {X} | {X}% |
| {query} | {N} | {X} | {X}% |
| {query} | {N} | {X} | {X}% |
| {query} | {N} | {X} | {X}% |
| {query} | {N} | {X} | {X}% |

---

## Wins This Month

{3–5 bullet points. Be specific. Use numbers.}

- **Page published**: "/seo-peterborough" published and indexed within 72 hours — now ranking position 24 for "SEO agency Peterborough" (1,600 searches/mo)
- **CTR improvement**: Rewrote titles on T1–T8 pages; avg CTR on those pages moved from 0.27% to 0.41%
- **Quick win**: "digital marketing Northampton" moved from position 16 → 11 after on-page optimisation

---

## Issues / Watch List

{1–3 items requiring attention. Don't hide problems — call them out professionally.}

- **{page}**: Lost 23% of clicks — likely seasonal dip, monitoring
- **Position regression**: "SEO agency Reading" dropped from 8 → 12 after a competitor published a new page — refreshing this page next month

---

## Deliverables Completed

| Deliverable | Status | Notes |
|------------|--------|-------|
| {deliverable} | ✅ Done | {notes} |
| {deliverable} | ✅ Done | {notes} |
| {deliverable} | ⚠️ Partial | {reason} |

---

## Focus for Next Month

1. **{Priority 1}** — {why + expected impact}
2. **{Priority 2}** — {why + expected impact}
3. **{Priority 3}** — {why + expected impact}

---

## Appendix: Quick Wins Identified

Pages ranking 11–20 that could reach page 1 with targeted optimisation:

| Page | Query | Position | Impressions | Opportunity |
|------|-------|----------|-------------|-------------|
| {page} | {query} | {X} | {N} | {specific action} |

---

*Report generated by Claude Code + GSC MCP. Data source: Google Search Console.*
*Questions? hello@sunnypatel.co.uk*
```

## Step 6: Save & Confirm

- Save to `G:\My Drive\clients\{client}\reports\{YYYY-MM}-report.md`
- Confirm: "Report saved to {path}. Ready to copy into email / Google Doc / PDF."
- Offer: "Want me to format this as HTML for email, or generate a PDF-ready version?"

## Notes

- Keep the tone professional but not robotic — write like a trusted advisor, not an analytics tool
- Always acknowledge problems honestly; clients respect transparency
- British English throughout (this is a UK business)
- The "Executive Summary" is the most important section — clients read it first; make it clear and actionable
- For Hummingbird: retainer target is 550+ clicks and 0.30%+ CTR for March 2026
