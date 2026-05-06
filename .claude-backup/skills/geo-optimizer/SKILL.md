---
name: geo-optimizer
description: Optimize content for AI citation by Google AI Overviews, ChatGPT, Perplexity, and Copilot. Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO).
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write, Bash, Grep
argument-hint: "[URL or content file]"
version: 1.0.0
---

# GEO / AEO Optimizer

Restructure content so AI platforms cite it. Combines Generative Engine Optimization (GEO) with Answer Engine Optimization (AEO).

## Process

1. **Fetch & analyze content** for citation readiness (WebFetch the URL or Read the file)
2. **Check AI crawler access** — fetch robots.txt, verify all 6 AI bots are allowed
3. **Score** against 9 Princeton GEO methods (with measured visibility boosts)
4. **Rewrite** flagged sections into citation-ready format
5. **Add** schema and structural elements that improve AI extraction
6. **Platform-specific checks** — verify content meets each AI engine's citation criteria
7. **Output** optimized content + GEO scorecard + platform readiness matrix

## 9 Princeton GEO Methods (Measured Visibility Impact)

| Method | Visibility Boost | Implementation |
|---|---|---|
| **Cite Sources** | **+40%** | Add "According to [Source]..." with hyperlinks. Every stat needs attribution |
| **Statistics Addition** | **+37%** | Add numbers, percentages, dates, study references. 2-3 stats per H2 section |
| **Quotation Addition** | **+30%** | Include expert quotes, study conclusions, official statements |
| **Authoritative Tone** | **+25%** | Write definitively, not tentatively. "X is" not "X might be" |
| **Easy-to-understand** | **+20%** | Plain language first, then technical detail. 8th grade reading level for intros |
| **Technical Terms** | **+18%** | Use precise domain terminology. Don't dumb down after the intro |
| **Unique Words** | **+15%** | Avoid generic phrasing. Use specific, descriptive language |
| **Fluency Optimization** | **+15-30%** | Natural flow, proper transitions, no awkward constructions |
| **Keyword Stuffing** | **-10%** | NEGATIVE impact. Never force keywords unnaturally |

## Citation-Ready Content Format

- **First paragraph**: Direct answer in 1-2 sentences (the extractable citation)
- **Second paragraph**: Supporting evidence with named source + statistic
- **Third paragraph**: Expanded context with technical detail
- Every H2 section follows this pattern independently (passage-level extraction)
- Optimal citation passage length: **40-60 words** per extractable block

## AI Crawler Access Check

Fetch the site's `robots.txt` and verify these are **NOT blocked**:

| Bot | Platform | User-Agent String |
|---|---|---|
| GPTBot | OpenAI/ChatGPT | `GPTBot` |
| ChatGPT-User | ChatGPT Browse | `ChatGPT-User` |
| ClaudeBot | Anthropic/Claude | `ClaudeBot` |
| PerplexityBot | Perplexity | `PerplexityBot` |
| Bingbot | Microsoft Copilot | `Bingbot` |
| Google-Extended | Gemini | `Google-Extended` |
| Googlebot | Google AI Overviews | `Googlebot` |

Also verify:
- Main content is NOT behind JS rendering walls (SSG/SSR preferred — our Astro sites are fine)
- No `noai` or `noimageai` meta tags blocking AI training/citation
- Content is NOT gated behind login/paywall

## Platform-Specific Citation Criteria

### Google AI Overviews
- E-E-A-T signals are critical — author bios, credentials, cited sources
- Structured data (FAQ, HowTo, Article schema) directly impacts AIO inclusion
- Topical authority: sites covering a topic comprehensively get cited more
- Authoritative citations boost visibility by **+132%**

### ChatGPT (GPTBot)
- **Branded domain authority matters**: 11% citation advantage for established brands
- Content updated within **30 days** gets **3.2x more citations**
- Backlinks matter: sites with >350K referring domains average 8.4 citations
- For our portfolio: focus on freshness signals and `dateModified` in schema

### Perplexity
- Allow `PerplexityBot` in robots.txt (many sites block it)
- FAQ Schema significantly increases Perplexity citations
- Host downloadable PDF documents (Perplexity indexes and cites PDFs)
- Semantic relevance > domain authority for Perplexity

### Microsoft Copilot / Bing
- Content MUST be indexed in Bing (submit via Bing Webmaster Tools)
- Page speed under 2 seconds required
- Microsoft ecosystem signals help (LinkedIn mentions, GitHub)
- For our portfolio: check Bing indexation — many of our sites are missing from Bing

### Claude AI
- Uses Brave Search index — verify site is indexed in Brave
- Factual density and source attribution are prioritised
- Structural clarity: clean heading hierarchy, logical flow
- No special schema needed beyond standard best practices

## Schema for AI Citation

Add `SpeakableSpecification` to key answer sections:
```json
{
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".answer-section", ".key-takeaway"]
  }
}
```

Add `FAQPage` schema for all Q&A sections. Add `HowTo` for process content.

Always include `dateModified` — it directly affects citation probability.

## Scorecard Output

```
GEO/AEO READINESS: [X/100]

Princeton GEO Methods:
- Cited sources:        [X/15] (+40% visibility)
- Statistics density:   [X/15] (+37% visibility)
- Quotation authority:  [X/12] (+30% visibility)
- Authoritative tone:   [X/12] (+25% visibility)
- Easy-to-understand:   [X/10] (+20% visibility)
- Technical terms:      [X/10] (+18% visibility)
- Unique language:      [X/8]  (+15% visibility)
- Fluency:              [X/8]  (+15-30% visibility)
- Keyword stuffing:     [✓ Clean / ✗ Over-optimized] (-10% penalty)
- Passage length:       [X/10] (target: 40-60 word blocks)

AI Crawler Access: ✓/✗ (list any blocked bots)
Schema Coverage: [X] types implemented
Citation-Ready Sections: [X/Y]
dateModified present: ✓/✗

PLATFORM READINESS:
- Google AI Overviews: [Ready/Needs Work] — [issues]
- ChatGPT:            [Ready/Needs Work] — [issues]
- Perplexity:         [Ready/Needs Work] — [issues]
- Copilot/Bing:       [Ready/Needs Work] — [issues]
- Claude:             [Ready/Needs Work] — [issues]
```

## Ghost Citations — The Hidden Problem

A ghost citation occurs when your URL passes the retrieval threshold (appears as a source) but your brand is NOT recommended. The AI already knew which brands to recommend from parametric data before it retrieved sources. Your page ends up in the bibliography of an answer that recommended someone else.

**Two distinct thresholds:**
1. **Retrieval threshold** — Was your page relevant enough to surface?
2. **Brand selection threshold** — Did the AI recall your brand name when choosing what to recommend?

Most GEO work only addresses threshold 1. You need both.

**Fixes:**
- Make your brand name the grammatical subject of key claims: NOT "there are five approaches to X" → YES "[Brand]'s approach to X starts with..."
- Put brand + claim in the same 40-60 word extractable passage
- Ensure brand appears inside FAQ answer text, not just the question

## Fan-out Coverage Audit

LLMs don't run one query — they break a user query into multiple parallel sub-queries (fan-out), run them independently, then merge results. A page covering only the seed query can be completely absent from the final response.

**Check coverage before writing:**
```
site:yourdomain.com [sub-query]
```
If a page appears → expand it with more angles. If no page → create one.

**Prioritisation:**
- Sub-query with 500+ searches/month → dedicated article
- Sub-query with 50 searches/month → 200-word subsection in main content

**Check Gemini fan-out specifically:** Use aistudio.google.com to run the target prompt and see which sub-queries it generates.

**Fan-out example** — "Is Japan expensive?" fans out into: average flights, hotel prices, rail pass cost, food costs, best budget seasons, Japan vs Europe comparison. A page that only answers the parent query misses all six sub-queries.

## Key Rules

- Answer-first, always. AI extracts the first clear statement per section.
- Every claim needs a source. Unsourced claims don't get cited.
- Freshness matters: pages updated within 6 months get 2.5x more citations. 70% of AI-cited pages were updated within the past year.
- `dateModified` in schema directly affects citation probability.
- LLMs cite only 2-7 domains per response — you must be definitively better than alternatives.
- Statistics improve citation rates by +41%. Credible quotations improve visibility by +28%. Keywords make it worse.
- 85% of brand mentions in AI search come from third-party sources — authority is off-site.
- For our 44-site portfolio: prioritise sites with existing traffic first (techloved, bestreviews, carehome.page, wagearea).
- Always check Bing indexation — many portfolio sites are only in Google.
- ChatGPT listicle citations decreased 30% (Dec 2025→Jan 2026). Wikipedia and Reddit are replacing listicle citation share. Don't rely solely on listicle-format content.
