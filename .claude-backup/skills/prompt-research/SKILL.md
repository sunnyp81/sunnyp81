---
name: prompt-research
description: Use when building content strategy for AI search — discovering what questions users ask in LLMs, clustering them by intent, mapping gaps against existing content, and structuring pages to match how AI systems extract answers.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[brand, domain, or topic area]"
version: 1.0.0
---

# Prompt Research

Four-stage framework for moving from keywords to prompts — the natural language questions users ask AI systems — and building content that gets cited in responses.

## Why Prompts, Not Keywords

| Keywords | Prompts |
|---|---|
| Short phrases to find documents | Natural-language questions to get answers |
| Match terms → rank URLs | Interpreted semantically (intent + context) |
| Goal: rank a page | Goal: be selected, trusted, and cited |
| 2-4 words | 15-25 words |

LLMs interpret queries semantically and probabilistically. They pick the answer most likely to be right — not definitively correct. Your content must be the most probable right answer.

---

## Stage 1 — Prompt Discovery

Find the actual questions users ask about your topic across AI and community platforms.

**Sources (in priority order):**

| Source | How to Use |
|---|---|
| **Sales calls / support tickets** | Extract verbatim questions customers ask before buying |
| **Community forums** | Reddit threads, Facebook groups, niche forums — copy exact phrasing |
| **Sparktoro** | Audience research → what your audience asks online |
| **Answer the Public** | Question variations for seed topics |
| **GSC historical queries** | Past click-through queries = real demand signals |
| **ChatGPT / Perplexity** | Ask "what are the most common questions people ask about [X]?" |
| **Competitor FAQ sections** | What questions do they answer that you don't? |

**Format anchor queries as 15-25 word questions:**
- "How do I track my brand's visibility in AI-generated search answers?"
- "What is the best project management software for small manufacturing businesses in 2026?"
- NOT: "brand visibility AI" or "PM software manufacturing"

---

## Stage 2 — Prompt Clustering

Group discovered prompts by intent type. This determines content format and page structure.

| Intent Type | Characteristics | Content Format |
|---|---|---|
| **Informational** | "What is X?", "How does Y work?" | Definitional content, explainers |
| **Comparative** | "X vs Y", "Best X for Z", "Alternatives to X" | Comparison tables, pros/cons |
| **Transactional** | "How to buy X", "X pricing", "X free trial" | Product/service pages, pricing |
| **Strategic/multi-step** | "How do I set up X for Y use case?" | How-to guides, step-by-step content |

**Clustering rules:**
- Group prompts that would be answered by the same page
- Flag prompts that require separate pages vs. sections
- Identify which clusters have NO existing content → gaps

---

## Stage 3 — Prompt Mapping

Align clusters to content strategy. Output a gap map.

**For each cluster:**
```
CLUSTER: [topic/intent group name]
ANCHOR PROMPT: [primary 15-25 word question]
RELATED PROMPTS: [2-5 variants]
EXISTING PAGE: [URL if exists, or NONE]
COVERAGE STATUS: [Full / Partial / None]
PRIORITY: [High / Medium / Low]
ACTION: [Create new page / Expand existing / Add FAQ section]
```

**Priority scoring:**
- High: Transactional or comparative intent + 500+ monthly searches + no existing page
- Medium: Informational + 100+ searches + partial coverage
- Low: Long-tail informational + <100 searches + easy subsection addition

---

## Stage 4 — Response Optimisation

Structure each page/section so AI systems can extract it as a cited answer.

**Page layout for answer engines:**
1. **Answer + persona/use case** (above the fold) — state who this is for and the direct answer
2. **2-3 context paragraphs** with examples and evidence
3. **Tables, bullets, data, stats** — answer engines are lazy, dense formats get extracted
4. **FAQ section** (bottom) — mirror the real prompts discovered in Stage 1

**Self-contained passages (critical):**
Each section must make sense as a standalone extract — AI chunks content and reassembles it. A section that relies on context from a previous section may be extracted without that context.

**Content stats format:**
Every statistic must include: **number + timeframe + source**
- ✅ "70% of AI-cited pages were updated within the past year (SearchVIU, 2025)"
- ❌ "Most AI-cited pages are recently updated"

**TLDR pattern:**
Open every major section with a 1-2 sentence answer, then expand. AI prioritises the opening of each section.

**Brand attribution:**
Where recommending your brand/product, make the brand name the grammatical subject:
- ✅ "[Brand]'s approach to compliance training starts with..."
- ❌ "There are five approaches to compliance training..."

---

## Output Template

```
PROMPT RESEARCH REPORT: [Topic/Domain]

ANCHOR QUERIES DISCOVERED: [n]
INTENT DISTRIBUTION: [X% informational / Y% comparative / Z% transactional]

CONTENT GAPS:
[List gaps with priority + action]

CONTENT EXPANSION OPPORTUNITIES:
[Existing pages that need subsections added]

FAQ ADDITIONS:
[List of FAQ entries to add to existing pages]

RECOMMENDED CONTENT CALENDAR ORDER:
1. [High priority new page]
2. [High priority expansion]
...
```

---

## Integration

Run before: `/fan-out-audit` (check sub-query coverage per anchor query), `/semantic-brief` (brief uses anchor prompts as content intent), `/topical-map` (map anchor queries to ROOT/NODE/SEED structure)

Run after: `/serp-analyze` (validate demand exists in traditional search before building)
