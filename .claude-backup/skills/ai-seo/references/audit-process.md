# AI SEO Audit Process & Scoring Rubric

Run both layers when auditing a site for AI search readiness.

## ENTITY LAYER AUDIT

### Step E1: AI Footprint Audit
Query Gemini Deep Research, ChatGPT, Perplexity with: "What is [brand]?", "Who runs [brand]?", "What does [brand] cover?"
Document every inaccuracy, false inference, entity confusion.

### Step E2: SCDL Gap Analysis
Compare what AI says vs. what is true. List:
- Facts AI doesn't know (gaps)
- Facts AI has wrong (errors)
- Identity confusion risks (Third Point Emergence Failures)

### Step E3: Canonical Source Audit
Does the site have an explicit About/Ground Truth page? Does it state: founding date, location, founder, what it covers, what it doesn't?

### Step E4: Disambiguation Check
Any risk of being confused with another entity? If yes, is there a Structured Disambiguation Assertion on the About page AND in Schema markup?

### Step E5: Mentions Audit
Search for domain mentions on: Reddit, industry publications, local press, Quora. Count authoritative independent mentions.

## TECHNICAL LAYER AUDIT

### Step T1: Crawl Access
Fetch `{domain}/robots.txt` — check all 6 AI bots are allowed (GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Bingbot)

### Step T2: Bing Indexation
Check if site is indexed in Bing (many portfolio sites aren't). Copilot relies entirely on Bing index.

### Step T3: Content Type Audit
Categorise existing content by type. Identify gaps — most sites lack comparison articles (the #1 cited type).

### Step T4: Schema Audit
Check which schema types are implemented. Flag missing Article/FAQ/HowTo schema.

### Step T5: Freshness Check
Pull GSC data or check `dateModified` on key pages. Flag anything older than 6 months.

### Step T6: Citation Test
Search the site's primary topics in ChatGPT, Perplexity, and Google. Note if the site appears in AI responses.

## Output Template: AI SEO Audit Report

```markdown
# AI SEO AUDIT: {domain}
**Date**: {date}

## AI READINESS SCORE: {X}/100

### ENTITY LAYER: {X}/35

#### SCDL Accuracy: {X}/15
- AI Footprint Audit run: ✓/✗
- Inaccuracies found: {list}
- Entity confusion risk: Low/Medium/High
- Third Point Emergence Failures: {list or "None found"}

#### Canonical Source: {X}/10
- Explicit About/Ground Truth page: ✓/✗
- States: founder, date, location, scope: ✓/✗
- What site does NOT cover: ✓/✗
- Disambiguation factoids present: ✓/✗
- Organization/Person schema: ✓/✗

#### Mentions Economy: {X}/10
- Authoritative independent mentions: {count}
- Reddit: {count}
- Industry publications: {count}
- Local press/directories: {count}
- Branded search evidence: ✓/✗

### TECHNICAL LAYER: {X}/65

#### Crawl Access: {X}/10
- GPTBot: ✓/✗
- ChatGPT-User: ✓/✗
- ClaudeBot: ✓/✗
- PerplexityBot: ✓/✗
- Google-Extended: ✓/✗
- Bingbot: ✓/✗

#### Content Structure: {X}/15
- Citation-ready passages (40-60 words): {count}
- FAQ sections with schema: {count}
- Comparison tables: {count}
- Step-by-step blocks: {count}

#### Authority Signals: {X}/15
- Pages with cited sources: {X}/{total}
- Pages with statistics: {X}/{total}
- Pages with expert quotes: {X}/{total}
- dateModified present: {X}/{total}

#### Content Type Coverage: {X}/15
- Comparison articles: {count} [GAP if 0]
- Definitive guides: {count}
- Original data/research: {count}
- How-to content: {count}
- Listicles: {count}

#### Third-Party Presence: {X}/10
- Review site listings: {count}
- Wikipedia references: {count}

## PRIORITY ACTIONS
1. [Most impactful action with specific page/content reference]
2. [Second action]
3. [Third action]

## SCDL FIXES NEEDED
- [List specific AI inaccuracies to correct on canonical source]

## CONTENT GAPS
- Missing content types to create
- Topics where AI currently cites competitors instead

## MONITORING SETUP
- Queries to track in AI platforms
- SCDL re-audit schedule (recommend quarterly)
- Recommended check frequency
```
