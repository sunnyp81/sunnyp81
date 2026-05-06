---
name: content-config
description: Iterative content optimization based on search engine feedback. Covers content configuration, historical data rules, re-ranking triggers, publication frequency, internal link auditing, and query network monitoring.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[domain or URL to optimize]"
version: 1.0.0
---

# Content Configuration

Optimize and reconfigure content iteratively based on search engine feedback — changed semantic distances, query shifts, re-ranking patterns, and historical data.

## Arguments

- `url` (optional): Specific URL or domain to analyze
- `mode` (optional): "audit" | "plan" | "monitor"
- `gsc-data` (optional): Path to GSC export file

---

## Content Configuration Methodology (KB-1)

**Definition:** Optimizing Relevance and Responsiveness continuously according to changed semantic distances and similarities of query terms.

### When to Configure
- Query semantics changed (new queries appearing, old dropping)
- Semantic distances shifted (after BCAUs or seasonal changes)
- Competitors published new content changing landscape
- Content ranks for unexpected queries (opportunity or misalignment)

### Configuration Actions
1. **Add information** — Expand sections for emerging query contexts
2. **Remove sections** — Cut content diluting relevance or competing with other pages
3. **Change internal links** — Redirect equity to match current semantic priorities
4. **Reorder sections** — Adjust contextual flow to match updated query importance
5. **Update contextual vectors** — Modify headings to align with changed intent

### Configuration Process
1. **Check ranking state**: New queries (expand), lost queries (investigate), shared queries (cannibalization risk). Prioritize by query movement.
2. **Analyze macro context alignment**: Keep distribution of semantics consistent. Bring pages together in macro context direction.
3. **Bulk changes for feedback**: Keep brief templates similar across SCN so changes apply in bulk (30+ articles) for meaningful SE feedback.
4. **If already Topical Authority**: Focus on competitor movements.

---

## Historical Data Rules (KB-12)

**Definition:** Amount of user engagement over time. NOT about "time" — about engagement quality.

| Type | Signals |
|---|---|
| Positive | Clicks, long dwell, return visits, scroll depth, text selection, interaction |
| Neutral | Impressions, brief visits, mouse-overs |
| Negative | Pogo-sticking, immediate back-clicks, no engagement, clickless searches |

### Key Rules
- **6-Month Lag**: Lost rankings today = bad historical data ~6 months ago. Recovery requires stronger positive signal over sustained period.
- **Testing Threshold**: New sites have low threshold — advantage. SE won't let one source take all rankings in one day, but high quality = fast positive historical data.
- **Fresh > Old**: Fresh engagement gradually overwrites old negative signals.

### Methods for Better Historical Data
- Clear internal link circulation (no redirects, no link rot)
- Clear indexing signals for all URLs
- Low-cost crawl paths for SE crawlers
- Distinctive but adjacent content with contextual relevance
- Discover ALL topically relevant content in one day (initial crawl)
- Static HTML, light CSS, minimal JS for main content
- Clear title tags, contextual vectors, and hierarchy

---

## Re-Ranking Triggers (KB-9)

**Definition:** Changing a document's ranking based on user feedback, relevance evaluation, and quality algorithms.

### Controllable Triggers

| Level | Triggers |
|---|---|
| Website | New content, updated content, structure changes, technical improvements |
| Web-page | Content additions/removals, heading restructuring, internal link changes, schema updates |
| Intersection | Anchor text changes, related page updates, SCN changes |

### Uncontrollable Triggers
Trending news, query demand changes (seasonal), algorithm updates (BCAUs), SE bugs, competitor actions.

### Timeline
Shortened with actual traffic + positive historical data. Re-ranking of link SOURCE impacts ranking of link TARGET.

---

## Publication Frequency & Momentum (KB-8)

### Core Rules
1. **Be patternless** — Publish different numbers on different days. SEs detect and devalue patterned publishing.
2. **Avoid algorithmic seasons** — Don't publish during BCAUs. Publish during flat states.
3. **Crawl budget advantage** — More frequent crawling than competitors = competitive advantage.
4. **Quality threshold breaking** — Every crawl should find increased quality, triggering ranking improvements.
5. **Outranking requirements** — Higher relevance, responsiveness, coverage, depth, quality than existing ranked sites.

### Launch Strategy
Can't publish 300 articles suddenly. Balance looking human with signaling site change.
- **Recommended**: Publish first 20 articles together to signal change, then continue steadily
- Alternative: 2 articles/day or 5 per 10 days, distributed without pattern
- Go for most important topics first, fix internal links after initial batch
- If NO history on topic: publishing most of SCN at once has advantages (faster indexing/understanding)

### Ongoing Balance
Content count is NOT a ranking factor. Fewer comprehensive authoritative articles > many thin ones (better for crawl budget, PageRank distribution, cannibalization prevention).

---

## Broad Index Refresh (KB-8)

SE periodically refreshes ranked documents for query networks — removes lesser quality, adds new qualifying resources. After refresh: previously non-ranking content may qualify, borderline content may get pushed out. Monitor for sudden ranking changes not tied to your actions. Topical consolidation helps survive refreshes.

Google uses Complex Adaptive System — every signal matters (search demand, mentions, social, code structure, design).

---

## Internal Link Auditing & Reconfiguration

### When to Audit
After publishing new content, after ranking changes, after content configuration changes, quarterly maintenance.

### Audit Checklist

**Structural:** No internal redirects | No broken links | Important pages within 3 clicks of homepage | Quality nodes close to homepage

**Relevance:** Anchor text matches target seed query | Anchor text not used >3 times for different targets | First link/anchor correctly weighted | Contextual relevance (not just navigational) | Surrounding text supports connection

**Prominence:** Important pages linked from H2 level | Supplementary uses H3-H4 | No links in first paragraph | Max 1 link per heading section | At least one heading between links

**PageRank Flow:** Outer section links TO core | Core links between related core pages | First link passes PageRank, subsequent pass relevance only | Header/footer use different anchors than main content | Total internal links <150/page

**Network:** Concepts defined consistently across pages | Macro context maintained | Root page anchor text matches seed page H1 patterns

### Reconfiguration Actions
1. Add links to new high-quality pages from relevant content
2. Remove links to low-performing/off-topic pages
3. Change anchor text to match target's current seed query
4. Reposition links between main/supplementary based on importance
5. Update surrounding text to strengthen contextual connection

---

## Query Network Monitoring

### What to Monitor

| Type | Definition | Action |
|---|---|---|
| Correlative (KB-8) | Queries searched TOGETHER with yours | Expanding = add sections/pages. Losing = context drift. |
| Query Paths (KB-8) | Queries searched AFTER yours | Content should anticipate next step. Internal links follow these paths. |
| Sequential (KB-8) | Related queries in same context across sessions | Validate topical map structure. Indicate SE-recognized topic boundaries. |

### Monitoring Cadence
- **Weekly**: Check GSC for new queries per page
- **Bi-weekly**: Compare query lists across pages for cannibalization
- **Monthly**: Analyze query path patterns
- **After BCAU**: Full query network audit — expect significant semantic distance changes

### Cannibalization Fix (KB-8)
Create distinctive pages for different intents. Consolidate overlapping content. Use internal linking to signal primary answer. Differentiate via macro context even if topic overlaps.

---

## Configuration Workflow — Quarterly Cycle

| Week | Phase | Actions |
|---|---|---|
| 1 | Data Collection | Export GSC data, map queries to pages, identify new/lost/shared queries |
| 2 | Analysis | Detect cannibalization, context drift, expansion opportunities, competitor movements |
| 3 | Planning | Configuration plan per page, internal link changes, new content gaps, prioritize by business impact |
| 4 | Execution | Execute bulk changes (min 10-15 pages), update links, publish new content, submit to GSC |
| 5-8 | Monitor | Track ranking changes, compare before/after query assignments, document learnings |

---

## Integration with Other Skills

`/topical-map` → plan architecture before configuration | `/semantic-brief` → briefs for new content | `/semantic-audit` → verify configured content | `/content-writer` → execute updates | `/meta-generate` → update meta tags | `/entity-authority` → entity consistency

---

> Content Configuration is NEVER "set and forget." The source that monitors, adapts, and reconfigures fastest while maintaining topical consistency will maintain topical authority.

---

## Page Experiment Framework

Treat every page as an experiment. Run controlled tests to find what Google rewards for YOUR site in YOUR niche.

### Experiment Types

| Version | Structure | Best For |
|---------|-----------|----------|
| A: Entity-Dense | Long-form, comprehensive, entity-rich prose | Established authority sites |
| B: Modular Interactive | Short sections, comparison tables, step-by-step visuals, collapsible FAQs | New sites, tool-like content |
| C: Hybrid | Prose intro → interactive middle → summary | Sites testing which format Google prefers |

### Running an Experiment

**Step 1: Select test pages** — Pick 3-5 pages targeting similar query types (e.g., all "how to" pages or all "best X" pages). Apply different structures to each.

**Step 2: Measure over 4-8 weeks** (minimum 2 crawl cycles):

| Metric | How to Check | Success Signal |
|--------|-------------|----------------|
| Impression growth | GSC → compare 4-week periods | >15% increase |
| Query expansion | GSC → unique queries per page | More queries = Google understands page better |
| CTR from SERP | GSC → CTR column | Higher CTR = better title/snippet match |
| Indexation speed | GSC → URL Inspection → last crawl date | Faster re-crawl = Google values updates |
| Position movement | GSC → average position trend | Upward trend over 4+ weeks |
| Semantic adjacent queries | GSC → new queries not in original target | Page ranking for related queries = topical expansion |

**Step 3: Log results** in `G:\My Drive\SEO\experiments\{domain}_experiments.md`:
```
## Experiment: [Name]
Date: [start] → [end]
Pages tested: [URLs]
Hypothesis: [what you expected]
Result: [what happened — with data]
Winner: [Version A/B/C]
Applied to: [which pages got the winning treatment]
```

**Step 4: Roll out winner** — Apply the winning structure to all similar pages on the site. Log the change in content-config for the next quarterly cycle.

### Experiment Ideas for Portfolio

| Site Type | Test | Hypothesis |
|-----------|------|-----------|
| pSEO sites (wagearea, catchment) | Add unique intro paragraphs vs template-only | Unique content improves index rate |
| Affiliate sites (bestreviews, techloved) | Comparison table above fold vs after intro | Tables increase CTR from SERP |
| Calculator sites (calculator.place) | Add FAQ schema vs without | FAQ schema increases impressions |
| Content sites (redlighttherapy) | Long-form (3000w) vs modular (1500w + tables) | Modular improves scroll depth + time on page |
