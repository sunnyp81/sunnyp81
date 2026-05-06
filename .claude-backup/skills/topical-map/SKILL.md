---
name: topical-map
description: Generate a complete ROOT/NODE/SEED topical map using Koray's semantic SEO methodology. Use when planning content architecture or mapping topical authority.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[domain or niche]"
version: 1.0.0
---

# Topical Map Architect

Generate a complete ROOT/NODE/SEED topical map using Koray's semantic SEO methodology.

## Arguments

- `domain` (required): Website domain or business name
- `niche` (required): Industry/category (e.g., "motorhome sales UK")
- `competitors` (optional): Competitor URLs, comma-separated

## Workflow

1. **Load methodology**: Read `G:\My Drive\Claude Code Work\SEO_Agents\01_Project_Manager_Agent_Instructions.md`
2. **Analyze source context**: Research niche, identify entity types/attributes, map semantic landscape
3. **Define central elements**: Central Entity, Central Search Intent, supporting intents
4. **Build topical map**: 1 ROOT → 5-10 NODEs → 50-200 SEEDs with proper hierarchy
5. **Competitive analysis** (if competitors provided): Map coverage, identify gaps, find differentiation
6. **Publication schedule**: Apply Vastness-Depth-Momentum, prioritize by business goals, estimate hours (1hr/500 words)
7. **Save output**: `G:\My Drive\Claude Code Work\Topical_Maps\{domain}_topical_map.md`

---

## Core Concepts

### Core vs Outer Section

| | Core Section | Outer Section |
|--|-------------|---------------|
| Focus | MAIN attribute of central entity — goes DEEP | MINOR attributes — stays FLAT |
| Purpose | Monetization | Trust/relevance propagation to core |
| URL structure | FLAT (close to root) | DEEPER (more directory levels) |
| Linking | Receives links from outer | Links TO core + between outer articles |

**Rule:** Put most important attribute at top of each section (topic distillation patent).

### ROOT Page Rules
- Independent page (not core or outer section)
- Connected to/from every attribute-related document
- **First heading = most important heading in entire topical map**
- H1 connects to Central Search Intent
- Most important attributes linked at top, less important at bottom

### Attribute Classification

**3 Criteria:** Prominence (removing it changes what entity IS), Popularity (search demand), Relevance (against SOURCE CONTEXT, not entity)

**3 Types:** Root attributes (in ALL entries of class), Rare (not in all), Unique (only in ONE entry — highest priority)

### Vastness-Depth-Momentum

| Lever | Meaning | Compensates For |
|-------|---------|----------------|
| Vastness | Breadth of topics covered | Lack of depth |
| Depth | Comprehensiveness per topic | Lack of breadth |
| Momentum | Speed of publication/updates | Gaps in both |

New sites benefit from high momentum. Established sites benefit from steady depth.

### Key Structural Concepts

**Topical Gap:** Contextual disconnectedness. Build contextual bridges using terminology from both clusters + internal links.

**Nesting vs Connecting:** Nest pages with shared purpose (URL hierarchy). Connect across paths via internal links (phrase-taxonomy).

**Topical Consolidation:** Deepen expertise for single vertical. Stay in context while defining concepts. Irrelevant rankings may dissolve overall relevance.

**Topical Coverage:** Not measured by page count. Measured by complete, structured processing of information around possible search activities. If you didn't define X or connect X to Y, you didn't cover it.

**Quality Nodes:** Extremely detailed pages proving authority. Should appear on/linked from homepage. Triggers deeper crawling.

---

## Output Template

```markdown
# Topical Map: [Domain]
Generated: [date]

## Source Context
Industry: [Category]
Entity Type: [What the business is]
Core Attributes: [Key characteristics]

## Central Entity & Intent
Central Entity: [Main subject]
Central Search Intent: [Primary user goal]
Supporting Intents: [Secondary goals]

## ROOT/NODE/SEED Architecture

### ROOT (1 page)
**[Title]** — [word count], establishes topical authority, links to all NODEs

### NODE Pages ([X] pages)
1. [Title] - [Intent]
...

### SEED Pages ([X] pages, grouped by NODE)
**Under "[NODE title]":**
1. [SEED title]
...

## Publication Strategy
Phase 1: Vastness (Weeks 1-4) — foundational NODEs, [X] pages
Phase 2: Depth (Weeks 5-12) — expand SEEDs, [X] pages
Phase 3: Momentum (Ongoing) — update ROOT/NODEs, add SEEDs, [X] pages/week

## Content Priorities
[Pages in publication order with priority, type, target query, word count, dependencies]

## Semantic Triples
{Entity} {Relation} {Attribute}
```

## Site Maturity Decision Framework

The topical map structure MUST adapt to the site's maturity stage:

### New Sites (<6 months, <1000 indexed pages)
- **Strategy:** Granular, tightly scoped pages for initial traction
- Publish more SEEDs with narrow intent — each page targets a single decision
- Higher page count, shallower depth per page (800-1200 words)
- Goal: earn initial indexation and query associations
- **Publishing cadence:** 5-10 core pages first → wait for crawl/index/impressions → then 2-3 pages/week

### Established Sites (6+ months, indexed, earning impressions)
- **Strategy:** Consolidate into fewer, deeper, entity-rich pages
- Merge cannibalizing SEEDs into comprehensive NODEs
- Lower page count, greater depth per page (2000-4000 words)
- Goal: win featured snippets, build topical authority
- **Decision rule:** If the user intent is ONE decision → one page. If MULTIPLE decisions → split.

### Revisit Trigger (Every 3-6 Months)
1. Pull GSC data: which pages cannibalize? (same queries, 2+ pages)
2. Check: any pages with impressions but 0 clicks? → merge into stronger page
3. Check: any page ranking for 50+ diverse queries? → split into focused pages
4. Run `/demand-map` to find new clusters not covered by current architecture
5. Update topical map and republish consolidated/split pages

## Quality Checklist

- [ ] ROOT establishes topical identity; first heading is most important in map
- [ ] 5-10 NODEs covering major variations; 50+ SEEDs for long-tail
- [ ] Every SEED → NODE → ROOT linking chain
- [ ] Core section: DEEP content, FLAT URLs (monetization)
- [ ] Outer section: FLAT content, DEEPER URLs (trust propagation)
- [ ] Attributes classified by Prominence × Popularity × Relevance
- [ ] Topical gaps identified with contextual bridges
- [ ] Publication follows Vastness → Depth → Momentum
- [ ] Quality nodes identified near homepage
- [ ] Competitive gaps identified (if competitors provided)
- [ ] Site maturity assessed — granular (new) or consolidated (established) strategy applied
- [ ] Cannibalization check scheduled for 3-6 month revisit

## Integration

After generating: copy to Project Manager Agent → request content → track progress → update quarterly.

## Related Skills

- `/semantic-brief` — briefs for individual pages
- `/semantic-audit` — verify published content matches intent
- `/meta-generate` — meta tags aligned with topical strategy
