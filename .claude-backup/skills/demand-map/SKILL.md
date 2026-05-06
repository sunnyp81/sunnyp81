---
name: demand-map
description: GSC-first demand mapping that replaces keyword research. Clusters real search queries by entity+attribute+task to reveal actual user behavior, seasonal patterns, and emerging demand. Use before topical-map or content-calendar on any site with 3+ months GSC data.
version: 1.0.0
user-invocable: true
allowed-tools: mcp__gsc__*, Read, Write, WebSearch, WebFetch
argument-hint: "[GSC property e.g. sc-domain:example.com]"
---

# Demand Map — GSC-First Content Strategy

Replace keyword tool estimates with real demand signals from Google Search Console.

## Why This Exists

Keyword tools miss 70-90% of long-tail and emerging queries. GSC shows what Google **actually associates** with your site. This skill builds content strategy from observed behavior, not estimated volume.

## Arguments

- `property` (required): GSC property (e.g. `sc-domain:example.com`)
- `period` (optional): Analysis window. Default: `16 months` (captures full seasonal cycle)
- `focus` (optional): Specific entity/section to zoom into

## Prerequisites

Requires **GSC MCP server**. Site must have 3+ months of data for meaningful patterns.

---

## Workflow

### Phase 1: Extract Raw Demand

Pull GSC data across the full period:

```
mcp__gsc__get_advanced_search_analytics:
  dimensions: "query"
  row_limit: 5000
  sort_by: "impressions" desc
  date_range: last 16 months
```

Also pull by page to see what Google already associates:
```
mcp__gsc__get_advanced_search_analytics:
  dimensions: "query,page"
  row_limit: 5000
  sort_by: "impressions" desc
```

### Phase 2: Entity-Attribute-Task Clustering

Do NOT cluster by keyword similarity. Cluster by **meaning structure**:

**Step 1 — Extract entities**
Every query contains an entity (the thing). Group queries that reference the same entity.
- "best CRM for small business" → entity: CRM
- "CRM vs spreadsheet" → entity: CRM
- "salesforce pricing 2026" → entity: Salesforce (sub-entity of CRM)

**Step 2 — Extract attributes**
Each entity has attributes the user cares about. Map queries to attributes.
- "CRM pricing" → attribute: cost
- "CRM integrations" → attribute: compatibility
- "easiest CRM to use" → attribute: usability

**Step 3 — Extract tasks**
The action the user wants to perform. This determines content structure.

| Task Type | Signal Words | Content Structure |
|-----------|-------------|-------------------|
| Choose | best, top, recommended, which | Comparison table + criteria |
| Compare | vs, difference, alternative, or | Side-by-side + verdict |
| Learn | what is, how does, meaning, explained | Definition + guide |
| Do | how to, steps, tutorial, setup | Step-by-step + visuals |
| Switch | migrate, move from, switch, replace | Migration guide + checklist |
| Fix | not working, error, problem, troubleshoot | Diagnostic flow + solution |
| Buy | price, cost, deal, buy, where to get | Pricing + CTA + trust signals |

**Step 4 — Form clusters**
One cluster = one entity + one task type. Same entity with different tasks = different clusters = different pages.

```
Cluster: "Choose a CRM" (entity: CRM, task: choose)
  - best crm for small business (2,400 imp)
  - top crm software uk (890 imp)
  - which crm should i use (340 imp)
  - recommended crm tools (120 imp)
  Total demand: 3,750 impressions

Cluster: "Compare CRMs" (entity: CRM, task: compare)
  - hubspot vs salesforce (1,800 imp)
  - crm comparison chart (450 imp)
  ...
```

### Phase 3: Demand Pattern Analysis

For each cluster, analyze:

**1. Demand trajectory**
- Compare impressions: months 1-4 vs months 5-8 vs months 9-12 vs months 13-16
- Flag: Rising (>20% growth), Stable, Declining (>20% drop), Seasonal (spikes in specific months)

**2. Seasonal patterns**
- Pull monthly breakdown: `mcp__gsc__get_advanced_search_analytics` with monthly date ranges
- Mark peak months per cluster
- Flag clusters that spike >3x their baseline

**3. Emerging demand**
- Queries that appeared in months 13-16 but NOT in months 1-8
- These are new associations Google is testing — high-priority content opportunities

**4. Query diversity score**
- Count unique queries per cluster
- High diversity (20+ queries) = broad demand, build comprehensive page
- Low diversity (3-5 queries) = specific demand, build focused page

### Phase 4: Demand-Content Gap Analysis

Cross-reference clusters against existing pages:

| Status | Meaning | Action |
|--------|---------|--------|
| Served | Cluster has a ranking page with CTR >2% | Optimize existing page |
| Underserved | Page exists but CTR <2% or position >20 | Rewrite/restructure |
| Unserved | No page ranks for cluster queries | Create new content |
| Oversaturated | 2+ pages compete for same cluster | Consolidate |

### Phase 5: Priority Scoring

Score each cluster for content planning:

```
Priority = (Total Impressions / 1000) x Task Multiplier x Trajectory Multiplier

Task Multiplier:
  Buy: 4x | Choose: 3x | Compare: 3x | Switch: 2x | Do: 1.5x | Fix: 1.5x | Learn: 1x

Trajectory Multiplier:
  Rising: 2x | Emerging: 2x | Stable: 1x | Seasonal (in-season): 1.5x | Declining: 0.5x
```

---

## Output Format

```markdown
# Demand Map: [domain]
**Generated:** [date] | **Period:** [start] to [end]
**Total queries analyzed:** [X] | **Clusters formed:** [X]

## Executive Summary
- [X] unserved clusters (new content needed)
- [X] underserved clusters (rewrite needed)
- [X] emerging demand signals (new queries appearing)
- [X] seasonal clusters peaking in [months]
- Top entity: [entity] ([X] impressions across [X] clusters)

## Demand Clusters (sorted by priority)

### Cluster: "[Name]" — Priority: [score]
- **Entity:** [entity] | **Task:** [task type] | **Status:** [served/unserved/etc]
- **Demand:** [total impressions] | **Trajectory:** [rising/stable/declining/seasonal]
- **Query diversity:** [count] unique queries
- **Peak months:** [if seasonal]
- **Top queries:**
  - [query] ([impressions] imp, pos [X])
  - ...
- **Action:** [Create/Rewrite/Consolidate/Optimize]
- **Content structure:** [based on task type]
- **Existing page:** [URL or "none"]

---

## Emerging Demand (new in last 4 months)
| Query | Impressions | Nearest Cluster | Action |
|-------|-------------|-----------------|--------|

## Seasonal Calendar
| Month | Clusters Peaking | Prep Deadline |
|-------|-----------------|---------------|

## Content Gap Summary
| Status | Clusters | Total Impressions | % of Demand |
|--------|----------|-------------------|-------------|
| Served | [X] | [X] | [X]% |
| Underserved | [X] | [X] | [X]% |
| Unserved | [X] | [X] | [X]% |
| Oversaturated | [X] | [X] | [X]% |
```

Save to: `G:\My Drive\Claude Code Work\Demand_Maps\{domain}_demand_map.md`

---

## Integration

- **Output feeds into** `/topical-map` — clusters define NODE/SEED architecture
- **Output feeds into** `/content-calendar` — priority scores + seasonal data drive scheduling
- **Output feeds into** `/semantic-brief` — each cluster becomes a brief with task-appropriate structure
- **Replaces** `/keyword-cluster` for sites with GSC data — keyword-cluster remains useful for NEW sites without GSC history
- **Input from** `/gsc-audit` — audit flags issues, demand-map reveals opportunities

## When NOT to Use

- Site has <3 months GSC data → use `/keyword-cluster` with third-party tools instead
- Single page optimization → use `/serp-analyze` or `/content-config`
- Technical issues → use `/gsc-audit` or `/technical-seo-checker`
