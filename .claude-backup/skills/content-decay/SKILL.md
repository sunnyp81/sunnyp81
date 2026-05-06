---
name: content-decay
description: Detect declining content from GSC data, score decay severity, and generate refresh briefs. Catches pages before they fall off page 1.
user-invocable: true
allowed-tools: Read, Write, WebSearch, mcp__gsc__*
argument-hint: "[GSC data CSV or domain]"
version: 1.0.0
---

# Content Decay Monitor

Detect pages losing rankings/traffic, prioritize by business impact, generate refresh actions.

## Process

1. **Ingest** GSC data (minimum 6 months, ideally 16 months)
2. **Calculate** decay score per page (0-100)
3. **Classify** decay cause
4. **Prioritize** by business impact (traffic × conversion value)
5. **Generate** refresh brief per decaying page
6. **Output** decay dashboard + refresh queue

## Decay Score Calculation

Score each page 0-100 based on:
- **Impressions trend** (25 pts): Compare last 3 months vs prior 3 months
- **Position trend** (25 pts): Average position movement
- **CTR trend** (25 pts): CTR change relative to position
- **Click trend** (25 pts): Absolute click volume change

| Score | Severity | Action |
|---|---|---|
| 0-25 | Healthy | Monitor |
| 26-50 | Early decay | Schedule refresh within 30 days |
| 51-75 | Active decay | Refresh within 14 days |
| 76-100 | Critical | Immediate refresh or consolidate |

## Decay Cause Classification

| Cause | Signals | Fix |
|---|---|---|
| **Freshness** | Content >12 months old, competitors updated | Update stats, add new sections |
| **Intent shift** | New SERP features, different page types ranking | Restructure content format |
| **Competition** | New competitors ranking, existing ones improved | Deepen coverage, add unique value |
| **Cannibalization** | Another page on same site gaining for same queries | Consolidate or differentiate |
| **Technical** | Slower load, mobile issues, indexing problems | Technical fixes |

## Refresh Brief Output

Per decaying page:
```
## Refresh: [Page Title]
URL: [url]
Decay Score: [X/100] — [Severity]
Cause: [Classification]
Current Position: [X] (was [Y])
Traffic Loss: [X] clicks/month

### Refresh Actions
1. [Specific action — e.g., "Update statistics in Section 3 to 2026 data"]
2. [Specific action — e.g., "Add FAQ section targeting new PAA queries"]
3. [Specific action — e.g., "Add comparison table competitors now have"]

### New Queries to Target
- [query] ([volume]) — appeared in SERP since last update
- [query] ([volume])

### Estimated Recovery: [X-Y weeks after refresh]
```

## Key Rules

- Prioritize pages with highest (traffic × conversion value) first
- Pages that lost Featured Snippets get highest urgency
- Content refreshed every 3-6 months maintains AI citation eligibility
- Feed refresh briefs into `/content-writer` for execution
