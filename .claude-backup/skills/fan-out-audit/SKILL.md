---
name: fan-out-audit
description: Use when planning or auditing content for AI search visibility — especially before creating new pages, when a site isn't being cited in AI responses, or when checking whether existing content covers the sub-queries LLMs generate for a topic.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[URL, domain, or topic]"
version: 1.0.0
---

# Fan-out Audit

Map the sub-queries LLMs generate for a topic, check which ones your site covers, and output a prioritised content plan.

## Core Concept

LLMs don't run one query. They break a user prompt into multiple parallel sub-queries (fan-out), run them independently, then merge results into a synthesised response. A page that only covers the seed query can be completely absent from the final answer — even if technically relevant.

**Example fan-out** — "Is Japan expensive to visit?" generates ~6 sub-queries simultaneously:
- average flight cost to Japan (US/Europe origins)
- hotel prices in Tokyo per night
- cost of Japan Rail Pass
- average daily food cost for tourists
- cheapest time to visit Japan
- Japan vs Europe travel cost comparison

A site with one page titled "Is Japan Expensive?" misses all six.

## Process

### Step 1 — Define the Anchor Query
Write the primary question as a 15-25 word natural language prompt (not a keyword).

Example: "What is the best project management software for small manufacturing businesses?"

### Step 2 — Expand Fan-out Sub-queries
Generate the sub-queries the LLM will run in parallel. Categories to cover:

| Fan-out Type | Example |
|---|---|
| **Cost/budget** | "how much does [X] cost" |
| **Comparison** | "[X] vs [Y]" |
| **Use case / vertical** | "[X] for [audience/industry]" |
| **Feature-specific** | "[X] with [specific capability]" |
| **Temporal** | "best [X] 2026" |
| **Negative** | "problems with [X]", "[X] alternatives" |
| **How-to** | "how to use [X] for [task]" |
| **Social proof** | "[X] reviews", "is [X] worth it" |

Use aistudio.google.com (Gemini) and Perplexity to check which sub-queries are actually generated for your topic.

### Step 3 — Coverage Check
For each sub-query, search:
```
site:yourdomain.com [sub-query]
```

| Result | Action |
|---|---|
| Page found, covers topic well | No action needed |
| Page found, partial coverage | Expand with 200-word subsection |
| No page found + sub-query 500+ searches/mo | Create dedicated article |
| No page found + sub-query 50-499 searches/mo | Add 200-word subsection to closest existing page |
| No page found + sub-query <50 searches/mo | Add FAQ entry only |

### Step 4 — Output Content Plan

For each gap, output:

```
SUB-QUERY: [the sub-query]
MONTHLY SEARCHES: [volume estimate]
ACTION: [new page / subsection / FAQ entry]
TARGET PAGE: [URL to create or edit]
SUGGESTED H2: [heading text]
WORD COUNT TARGET: [500+ for new page / 200 for subsection / 50 for FAQ]
PRIORITY: [High / Medium / Low]
```

## Query Augmentation (Bonus Layer)

Before retrieval, LLMs also rewrite queries to be more semantically precise. "treatment for high blood sugar" becomes "management of hyperglycemia in type 2 diabetes lifestyle changes medication insulin thresholds symptoms".

Optimise for augmentation compatibility:
- Use precise domain terminology (your page needs to use the words the augmented query contains)
- State entities and relationships explicitly
- Write self-contained passages that make sense without surrounding context

## Topical Granularity Pattern

Add attributes to root topics to reduce competition and improve specificity match:

| Level | Example |
|---|---|
| ROOT | Project Management Software |
| + Audience | Project Management Software for Manufacturing |
| + Qualifier | Best Project Management Software for Manufacturing |
| + Third-party | "What are the best PM tools for Manufacturing in 2026?" |

Each attribute level changes RAG logic. More specific = fewer competitors = higher citation probability.

## Tools

| Tool | Use |
|---|---|
| aistudio.google.com | Enter prompt → see Gemini's actual sub-queries |
| Perplexity | Run prompt → inspect "Sources" section for sub-query signal |
| GSC | Historical query data reveals what people actually searched before clicking |
| `site:domain.com [query]` | Quick coverage check |

## Integration

Run before: `/semantic-brief` (ensures briefs cover all fan-out angles), `/topical-map` (ensures map addresses sub-query clusters), `/content-writer` (brief writer with fan-out aware structure)

Run alongside: `/geo-optimizer` (optimise each page for citation once coverage is confirmed)
