---
name: semantic-brief
description: Generate detailed content briefs following Koray Tugberk Gubur's semantic SEO methodology. Use when creating content briefs for SEO articles.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[keyword or query]"
version: 1.0.0
---

# Semantic Content Brief Generator

Generate detailed content briefs following Koray's semantic SEO methodology.

## Arguments

- `query` (required): The target search query to analyze
- `perspective` (optional): Target audience (beginner/intermediate/advanced)
- `word_count` (optional): Target word count for content

## British English Requirement

For .co.uk sites, add at top of brief:
> **LOCALE: British English required. -ise not -ize, -our not -or, -re not -er, £ for prices, UK vocabulary (GP, autumn, shop, maths).**

Extract and replicate British English patterns from UK-ranking SERP pages.

---

## Process

### 0. Task Decomposition

Before analyzing SERPs, decompose the topic into **task variants**. The same entity with different user tasks requires completely different content structures.

**Step 1:** Identify the core entity in the query.
**Step 2:** Map all task variants the user might perform:

| Task | Example Query | Content Structure |
|------|--------------|-------------------|
| Choose | "best [entity]", "which [entity]" | Comparison table + weighted criteria + verdict |
| Compare | "[entity A] vs [entity B]" | Side-by-side feature grid + use-case recommendations |
| Learn | "what is [entity]", "how does [entity] work" | Definition → mechanism → examples → implications |
| Do | "how to [verb] [entity]" | Numbered steps + visuals + common mistakes |
| Switch | "migrate from [A] to [B]", "replace [entity]" | Migration checklist + data transfer + gotchas |
| Fix | "[entity] not working", "[entity] error" | Diagnostic flow → cause → solution → prevention |
| Buy | "[entity] price", "buy [entity]" | Pricing breakdown + trust signals + CTA |

**Step 3:** Confirm with SERP — does Google treat these as separate intents? (Different pages ranking = separate intents = separate briefs needed.)

**Step 4:** If the user's query maps to ONE task, proceed with brief for that task. If it maps to MULTIPLE tasks, flag to the user: "This topic needs [X] separate pages, one per task type. Which task should I brief first?"

**Decision rule:** One user task = one page. Never combine "choose a CRM" and "set up CRM workflows" on the same page.

### 1. SERP Analysis
- Search Google for target query, analyze top 10-20 results
- Extract: bold text from meta descriptions (Google's recognized answers), verbs (relevance vs responsiveness), nouns (relevance vs responsiveness), sentence structures/patterns, quality metrics ("best", "complete"), order of statements, perspectives, helpful elements (tables, checklists, calculators)

### 2. Query Template Classification
Identify template (e.g., "How to {do} X", "Best {product} for {use case}") and apply template-specific rules.

### 3. Generate Brief

```markdown
# SEMANTIC CONTENT BRIEF
**Query**: [target query]
**Query Template**: [identified template]
**Word Count Target**: [based on competitor analysis]

## SERP ANALYSIS
### Bold Text Patterns
[Google's recognized answers from meta descriptions]
### Verb Analysis
**Relevance**: [from query] | **Responsiveness**: [answer-specific actions]
### Noun Analysis
**Relevance**: [from query] | **Responsiveness**: [answer-specific]
### Sentence Structures
[Common patterns with examples and frequency]
### Quality Metrics / Order of Statements / Perspectives
[Quality phrases, typical flow, audience level]

## CONTEXTUAL HIERARCHY
### H1
`[Exact H1 — entity + attribute + perspective]`
### H2 Structure (EXACT Order)
**H2-1**: [Title] - Purpose: [why] - Domain: [context] - Bridge to next: [shared terms]
[Continue for all sections]
### H3 Subsections
[H3s under each H2]

## CONTEXTUAL STRUCTURE
### Introduction (200-250 words)
1. Definition (75-100w) 2. Representative Answer (50-75w) 3. Supporting Evidence (50-75w) 4. Summary (25-50w)
### H2-1: [Title] - [X words]
**Representative Answer**: [1-2 sentences]
**Supporting Evidence**: [2-4 sentences]
**Required Elements**: [specific nouns, verbs, metrics]
[Repeat per H2]

## QUERY COLUMNS
### Column 1 (Ranking Authority)
Source: [URL] | Queries: [ordered by ranking]
### Column 2 (Classification Target)
Source: [URL] | Context Terms: [terms to adopt]
### Column 3 (Phrase Taxonomy)
Phrase Variations: [by volume] | Internal Link Targets: [destinations]

## CONTEXTUAL BORDER
**Main Content ends after**: [Last H2 of macro context]
**Bridge Heading**: [transitional H2]
**Grouper Question**: [bridging question]
**Supplementary Content begins at**: [First H2 of micro context]

## MICRO-SEMANTIC REQUIREMENTS
### Sentence Structures (Use ONLY These)
1. `[Pattern]` - Frequency: [X%]
### Sentence Rules
- 95%+ start with answer | 95%+ no commas (except enumerations) | imperative verbs for advice | clear ranges for specifications
### Verbs/Nouns to Use
**Primary Verbs**: [top 5-10] | **Secondary**: [next 10]
**Primary Nouns**: [top 5-10] | **Secondary**: [next 10]

## WHAT TO AVOID
Prohibited fluff: delve, unlock, embark, seamless, elevate, "it's worth noting", "when it comes to"
Prohibited structures: burying answers, comma-heavy sentences, >2 items with and/or

## WRITING AGENT INSTRUCTIONS
Execute with ZERO deviation. Follow structures exactly. Use ONLY specified verbs/nouns. Apply 95% rules. Write from Google's POV. Do not "improve" — execute as engineering instructions.
```

---

## KB Reference — Brief Construction Rules

| KB | Concept | Key Principle |
|---|---|---|
| KB-13 | Question Types | **Boolean**: yes/no, bottom of vector, voice search. **Definitional**: define something, top of sections. **Grouping**: multiple instances, ordered lists. **Comparative**: superlative/comparative, specific attributes. |
| KB-13 | Question Placement | End of section signals next heading. H1 = unification of all H2s. Shorter questions usually better. |
| KB-14 | Contextual Flow | Order of headings CHANGES relevance. First-to-last heading = straight vector. Anchor segments between sections. Intro reflects H2 order. |
| KB-14 | Contextual Coverage | Heavy processing dilutes other sections. Light processing of query-related sections decreases relevance. Specify coverage % per section. |
| KB-1 | Contextual Border | Slow transition from main to supplementary. Uses grouper question (most important common question related to H1 + each main heading). |
| KB-14 | Contextual Bridge | First heading after main content. "How" question for deeper look. Use lexicosemantics to expand (e.g., human body → animal bodies). |
| KB-8 | Context Qualifiers | Adverbials/propositions dividing contextual domain further. Qualifier + knowledge domain = contextual domain. |
| KB-1 | 3-Column Method | Col 1: ranking authority page queries (most weight). Col 2: classification target (consensus). Col 3: phrase taxonomy (internal links). |

## Introductory Section Rules (KB-4)

Combines extractive + abstractive summary. Process: write abstractive summary → write intro → after full article, recheck intro. Start with entity definition (better than competitors). After definition: representative answer → evidence. Be summary-like — do NOT expand lexical relations in intro. Everything in intro WILL be processed throughout the page.

## Main vs Supplementary Content (KB-7, KB-10)

**Main:** Macro context, major query needs, all main entities. NO sub-contexts, minimal internal links. Upper page = more Google weight.

**Supplementary:** Micro contexts, MORE internal links, contextual bridges. NOT "less important" — passes PageRank + collects historical data from different verticals. Use antonyms, boolean H4s, expanded word sequences. Best format reserved for most relevant page, not supplementary.

## Contextual Structure (KB-3)

Use preceding questions inside subsections for Featured Snippets (answer representative question, then ask more specific connected question). Keep sections balanced — too-long sections disconnect H1 from main content.

---

## Output

Provide complete brief as markdown with: word count targets (total + per section with coverage %), 3-column query analysis, contextual border/bridge marked, flow annotations between H2s, question types labeled, main/supplementary boundary, compliance checklists.

The brief must be so detailed that Writing Agent cannot fail.
