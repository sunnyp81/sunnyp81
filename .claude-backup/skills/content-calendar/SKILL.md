---
name: content-calendar
description: Generate quarterly content calendars from keyword data, seasonality, and competitor publishing cadence. Feeds into the semantic brief pipeline.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[niche or domain] [quarter]"
version: 1.0.0
---

# Content Calendar Generator

Create a data-driven editorial calendar with topics, dates, formats, and dependencies.

## Portfolio Context

- **44 SEO sites** across UK niches: property (rentalyield.uk, selflandlord.com), education (catchment.school, thetutor.link), health (deadhangs.com, redlighttherapy.expert), finance (bookkeepingflow.com, wagearea.com), tools (calculator.place, epc.report), and more.
- **Stack:** Astro 5/6 or Next.js on Cloudflare Pages or Vercel. Content is typically markdown or MDX.
- **SEO methodology:** Koray Tugberk's semantic SEO — topical maps, entity coverage, NODE/SEED/SUPPORT page hierarchy.
- **Pipeline integration:** This calendar feeds into `/semantic-brief` (for individual article briefs) → `/content-writer` (for draft generation). Plan here, brief there, write there.
- **Prioritisation:** Sites should be prioritised by revenue potential. Focus publishing effort on sites that are closest to monetisation (AdSense threshold, affiliate readiness, client acquisition).
- **UK market:** British English. Consider UK-specific seasonal events (bank holidays, school terms, tax year April-March, etc.).

## Process Steps

1. **Gather inputs:**
   - Domain/niche to plan for
   - Target quarter (Q1-Q4 + year)
   - Available keyword data (GSC export, Ahrefs, or manual list)
   - Current content inventory (what's already published)
   - Publishing capacity (how many pieces per week)

2. **Pull search data:**
   - Use GSC MCP tools to get current performance data for the site
   - Identify keyword gaps: terms with impressions but no dedicated page
   - Identify underperforming pages: high impressions, low CTR (candidates for rewrite, not new content)

3. **Cluster keywords into topical pillars:**
   - Group related keywords using `/keyword-cluster` logic
   - Identify NODE (pillar), SEED (supporting), and SUPPORT pages per Koray's methodology
   - Map entity relationships between clusters

4. **Map seasonal opportunities:**
   - Check Google Trends for seasonal patterns in the niche
   - Identify UK-specific timing: tax year (April), school admissions (autumn), property market cycles, etc.
   - Note industry events, awareness weeks/months relevant to the niche

5. **Score and prioritise topics:**
   - Apply the priority scoring formula below
   - Rank all topics by score
   - Select topics that fit the publishing capacity for the quarter

6. **Assign to dates:**
   - Follow the scheduling rules below
   - Ensure pillar pages publish before their supporting pages
   - Cluster related content within 2-week windows

7. **Output the calendar** using the format below

## Calendar Entry Structure

```markdown
| Date | Topic | Primary Keyword | Volume | Type | Funnel | Words | Status | Dependencies | Internal Links | Assigned |
|---|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | [Title] | [keyword] | [vol] | [Guide/Comparison/How-to/Listicle/Product/FAQ] | [TOFU/MOFU/BOFU] | [X] | [Not started] | [Publish after: X] | [Link to/from: X] | [writer] |
```

## Priority Scoring

Score each topic: `(Search Volume x Business Relevance x Feasibility) / Competition`

| Factor | Scale | Description |
|---|---|---|
| **Search Volume** | Raw number | Monthly search volume from Ahrefs/GSC |
| **Business Relevance** | 1-5 | 5 = directly monetisable (affiliate, ad revenue, client acquisition) |
| **Feasibility** | 1-5 | 5 = easy to produce, data available, no expert review needed |
| **Competition** | 1-5 | 5 = very competitive (high DR competitors, featured snippets dominated) |

## Scheduling Rules

- **Pillar pages first:** Publish NODE/ROOT pages before their SEED pages
- **Cluster batches:** Publish 3-5 related pieces within a 2-week window for topical signal
- **Patternless cadence:** Vary number of posts per week (matches `/content-config` momentum rules)
- **Seasonal lead time:** Publish seasonal content 6-8 weeks before peak search demand
- **No publishing during BCAUs:** Leave buffer weeks around known algorithm update windows
- **Rewrite vs new:** If a page exists with high impressions but low CTR, schedule a rewrite instead of a new page

## Output Format

```markdown
# Content Calendar: [Site/Niche] — [Quarter Year]

## Quarterly Summary

| Metric | Value |
|---|---|
| Total planned pieces | [X] |
| New content | [X] |
| Rewrites/updates | [X] |
| By type | Guide: X, How-to: X, Comparison: X, Listicle: X, FAQ: X |
| By funnel stage | TOFU: X, MOFU: X, BOFU: X |
| Estimated hours | [X] (1hr per 500 words) |
| Revenue-critical pieces | [X] (pieces directly tied to monetisation) |

## Calendar

[Full table with all entries per the structure above]

## Topical Clusters

### Cluster 1: [Topic]
- NODE: [pillar page] — publish [date]
- SEED: [supporting page 1] — publish [date]
- SEED: [supporting page 2] — publish [date]

### Cluster 2: [Topic]
...

## Seasonal Notes
- [Date range]: [seasonal opportunity and why it matters]
- [Date range]: [seasonal opportunity]

## Dependencies & Risks
- [Any blockers, data needs, or capacity constraints]
```

## Key Rules

- Always check what's already published before planning new content — avoid cannibalisation
- Prioritise revenue-generating content over vanity traffic
- Every piece should have a clear internal linking plan
- British English for UK-facing sites
- Calendar should be exportable as CSV for project management tools
