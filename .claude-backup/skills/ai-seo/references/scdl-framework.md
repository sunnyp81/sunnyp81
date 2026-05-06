# SCDL Framework — Entity Layer Deep Dive

*Based on Hobo: Strategic AiSEO 2025 by Shaun Anderson*

## The Synthetic Content Data Layer (SCDL)

AI engines don't just crawl your site — they build a **fog of understanding** about your entity from fragmented web data, inferences, and sometimes fabrications. This is your Synthetic Content Data Layer. If you don't fill it with your verified narrative, it gets filled by competitors, negative sentiment, or hallucinations.

**The SCDL Opportunity Gap** = what AI should know about you minus what it actually knows (or believes incorrectly).

## Phase 1: AI Footprint Audit

Before any content work, discover your current SCDL state:

1. Query Gemini Pro Deep Research, ChatGPT, Perplexity, and Google AIO with customer-like questions:
   - "What is [brand/site]?"
   - "Who runs [brand]?"
   - "What does [brand] cover / specialise in?"
   - "Is [brand] reliable/trustworthy?"
2. Document every inaccuracy, gap, false inference, and entity confusion
3. Note which sources AI is citing — these are your competitor SCDL inputs
4. **Watch for Third Point Emergence Failures** — AI incorrectly merging your identity with a namesake, competitor, or wrong niche

## Phase 2: Build Your Canonical Source of Ground Truth

Your website is your Single Source of Truth (SSoT). Every entity fact AI knows about you should originate here.

**Create a definitive "About" / Ground Truth page that explicitly states:**
- Founder name, founding date, location
- What the site covers (and what it does NOT cover)
- Specific credentials, experience, achievements (with evidence links)
- Any necessary disambiguation (e.g., "Not affiliated with [similar name]")

Publish this at `/about/` and link to it from every page footer.

## Phase 3: Publish Disambiguation Factoids

If there's any risk of entity confusion (similar brand name, common niche terms, namesake individual), publish a **Structured Disambiguation Assertion (SDA)**:

> "[Full name/brand], founded [date] in [location], is [precise description]. This entity is not affiliated with [commonly confused entity] and does not [false association]."

Place in:
- About/author pages
- `Organization` or `Person` Schema markup
- Author bio blocks

Deploy within 24-48 hours of detecting an AI error. After publishing: post on LinkedIn linking to the updated page (triggers fresh crawl), then monitor for AI to update.

## Phase 4: Inference Optimisation

AI can accurately answer infinite long-tail questions about you **without you writing a page for each**, IF you give it enough entity building blocks. Called "Super Topicality."

**The Cyborg Workflow for Ground Truth Content:**
1. Gather internal authoritative facts (product specs, FAQs, case studies, support logs, credentials)
2. Feed to Gemini Pro as raw inputs, ask it to draft exhaustive documentation
3. **Human fact-check every word** — no exceptions
4. Publish to your canonical source
5. Repeat

**Inference Saturation Point** — stop before you create overlapping/duplicate content. Some facts are best left in the AI layer as positive probabilities; you don't need to write a page for every inference.

## The Mentions Economy

For AI citation, **authoritative mentions > links**. AI Overviews use RAG (Retrieval Augmented Generation) — they need corroboration from multiple independent sources, not one powerful backlink.

Gary Illyes (Google): "E-E-A-T is largely based on links and mentions on authoritative sites."

**Branded search bonus**: The Panda patent describes a ratio of branded/navigational queries to all queries as a site quality signal. Mentions that drive branded searches are doubly valuable.

**Pursue mentions via:**
- HARO / journalist requests with expert quotes
- Original research that others cite
- Industry publication guest posts
- Local: chamber listings, local news, community blogs (for geo-targeted AI citation)
- **Avoid**: fake expert networks, mention directories, AI-generated forum spam = "Mention Pollution" → Entity Trust Penalty (near-impossible to recover from)

## AI Reputation Watchdog Role

Establish a recurring routine (weekly minimum):
1. **Detect** — query AI tools for brand/founder/product names + negative associations
2. **Diagnose** — identify source document AI is pulling from
3. **Treat** — update canonical page with explicit correction + link to evidence
4. **Inoculate** — publish disambiguation factoid proactively before the next error

**New KPIs to track:**
- Citation frequency in AI-generated answers (not just rankings)
- Branded/navigational search volume (feeds site quality score)
- SCDL accuracy score (manual audit quarterly)

## Understanding Query Fan-Out

A single user query is decomposed by AI into dozens/hundreds of sub-queries executed in parallel. You're not competing for one keyword — you're competing to be relevant to **hidden machine-generated sub-queries**.

**Implication**: Small specialist sites can now compete with major domains IF they provide the definitive answer to specific AI sub-queries. Authority is becoming granular, not just site-wide.

Build topical depth across a subject cluster — not just individual keyword pages.

## What to AVOID (Entity Layer)

- Pasting AI output directly to your site without substantial human editing → duplicative content penalty
- Treating social media as your canonical source — it's "borrowed land" with platform-controlled visibility
- Publishing past Inference Saturation Point → overlapping/doorway content
- Ignoring disambiguation risks proactively — correct before an AI error damages reputation
- Mention Pollution tactics → Entity Trust Penalty is predicted to be catastrophic
- Generic About pages / thin trust signals → E-E-A-T is primary framework for AI source selection
