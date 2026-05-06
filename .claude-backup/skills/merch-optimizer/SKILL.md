---
name: merch-optimizer
description: Merch by Amazon listing optimizer and niche researcher. Use when researching new MBA niches, creating design briefs, optimising existing ASIN listings, triaging a portfolio of designs, or planning new print-on-demand products. Covers niche research, BSR analysis, design brief generation, listing copy (title/bullets/keywords), and portfolio triage.
version: 1.0.0
user-invocable: true
allowed-tools: WebSearch, Read, Write
argument-hint: "[niche or keyword or ASIN] [--mode research|brief|listing|triage]"
---

# Merch Optimizer — MBA Niche Research, Design Briefs & Listing Copy

Full-stack Merch by Amazon workflow: find profitable niches, create design briefs, write optimised listings, and triage your portfolio.

## Arguments

- `input` (required): A niche keyword ("funny camping mug"), an ASIN to optimise, or "triage" to audit the portfolio
- `--mode` (optional):
  - `research` — Niche viability analysis + sub-niche breakdown
  - `brief` — Design brief for a specific niche
  - `listing` — Optimised listing copy for an ASIN or niche
  - `triage` — Portfolio triage across all designs
  - Default: runs all applicable modes for the input

## Workspace

Merch workspace: `G:\My Drive\MerchByAmazon\`
Read `G:\My Drive\MerchByAmazon\CLAUDE.md` for platform rules, active niches, and current design count before starting.

---

## Mode: RESEARCH — Niche Viability Analysis

### Step 1: Search Signal Analysis

Search Amazon UK and Amazon US for the niche keyword to assess:

```
WebSearch: site:amazon.co.uk "{niche}" t-shirt
WebSearch: site:amazon.com "{niche}" t-shirt best seller
```

Assess:
- **BSR (Best Seller Rank)**: Top sellers' BSR — under 100k = healthy demand; over 500k = slow market
- **Review counts**: Top 10 designs — if they have <50 reviews, niche is early/accessible
- **Design quality bar**: Are the top sellers mediocre? If yes, a better design wins
- **Price range**: What are top sellers charging? MBA norm is £15.99–£19.99 UK / $16.99–$21.99 US

### Step 2: Sub-Niche Breakdown

Identify 5–8 sub-niches with lower competition. Pattern: `[occupation/hobby] + [occasion/identity] + [humour/sentiment]`

Examples from "camping":
- Camping + retirement gift
- Camping + dog owner
- Camping + nurse hobby
- Camping + birthday

For each sub-niche rate:
| Sub-Niche | Demand | Competition | Design Bar | Verdict |
|-----------|--------|-------------|-----------|---------|
| ... | High/Med/Low | High/Med/Low | High/Med/Low | ✅ Target / ⚠️ Risky / ❌ Skip |

### Step 3: Trend Signals

Search for trend signals:
```
WebSearch: "{niche}" gift ideas 2026
WebSearch: "{niche}" t-shirt trending
```

Flag if: seasonal (Christmas, Valentine's, graduation), evergreen, or declining.

### Output: Research Report

```markdown
# Niche Research: {niche}
**Date**: {date} | **Markets**: UK + US

## Verdict: {✅ Pursue / ⚠️ Proceed with caution / ❌ Skip}
**Reason**: {1-sentence summary}

## Market Signals
- BSR range (top 10): {X}k–{Y}k
- Review barrier: {low/medium/high}
- Price range: £{X}–£{Y} UK / ${X}–${Y} US
- Trend: {evergreen/seasonal/rising/declining}

## Top Sub-Niches to Target
1. **{sub-niche}** — {why}
2. **{sub-niche}** — {why}
...

## Suggested First Design
{specific niche + sentiment + text idea}
```

---

## Mode: BRIEF — Design Brief

Produce a complete design brief for a graphic designer or AI image tool (Gemini/nano-banana).

### Design Brief Format

```markdown
# Design Brief: {niche}
**Product type**: T-shirt (also suitable for: hoodie, mug, tote)
**Target buyer**: {demographic — e.g. "nurse who loves hiking, buys as gift"}
**Primary text**: "{main slogan or quote}"
**Secondary text** (optional): "{sub-line, e.g. 'Established 1987'}"

## Visual Direction
- **Style**: {e.g. vintage badge / minimalist text / cartoon illustration / retro sunset}
- **Colour palette**: {primary: #hex} + {secondary: #hex} on {white/black/navy} base
- **Font mood**: {serif classic / bold sans / hand-lettered / typewriter}
- **Illustration** (if any): {specific description — e.g. "simple tent outline with moon and stars, line art"}
- **Layout**: {centred stack / left-aligned / arch text above illustration}

## Text Placement
- Top: {text or empty}
- Centre: {main visual or text}
- Bottom: {text or empty}

## MBA-Specific Rules
- No celebrity names, brand logos, or trademarked phrases
- No copyrighted characters or imagery
- Keep all text within the safe print zone (no closer than 1 inch from edge)
- Transparent background PNG, 4500×5400px, 300 DPI
- File: sRGB colour profile

## Comparable Designs (reference, don't copy)
{3 ASIN links or descriptions of similar successful designs}
```

---

## Mode: LISTING — Optimised Listing Copy

Write the full MBA listing: title, bullet points, and backend keywords.

### MBA Listing Rules

**Title** (max 60 chars visible, 200 char limit):
- Lead with the gift occasion or recipient: "Funny Camping Gift for Men"
- Include product type: "T-Shirt" or "Tee"
- Add key identity: "Camper", "Nurse", "Dad"
- No ALL CAPS, no special characters except hyphens

**Bullet Points** (5 bullets, 256 chars each):
- Bullet 1: Gift occasion + recipient ("Perfect gift for the camping enthusiast in your life")
- Bullet 2: Product quality signals ("Printed on premium soft cotton, built to last wash after wash")
- Bullet 3: Design description + text on shirt ("Features bold text reading '...' with a {style} graphic")
- Bullet 4: Fit/sizing guidance ("Available in a range of sizes, slim to relaxed fit")
- Bullet 5: Cross-sell / brand signal ("Great for birthdays, Christmas, Father's Day and just because")

**Backend Keywords** (250 chars, space-separated, no commas, no repeats from title):
- Mix: gift keywords, occasion keywords, identity keywords, synonym phrases
- Include misspellings if volume exists (e.g. "campingn")
- No competitor brand names

### Output Format

```markdown
# MBA Listing: {niche}

**TITLE** ({N} chars):
{title}

**BULLET 1** ({N} chars):
{bullet}

**BULLET 2** ({N} chars):
{bullet}

**BULLET 3** ({N} chars):
{bullet}

**BULLET 4** ({N} chars):
{bullet}

**BULLET 5** ({N} chars):
{bullet}

**BACKEND KEYWORDS** ({N}/250 chars):
{keyword string}
```

---

## Mode: TRIAGE — Portfolio Audit

Read the portfolio data from `G:\My Drive\MerchByAmazon\` and triage all designs.

For each ASIN (or niche cluster), classify:

| Status | Criteria | Action |
|--------|----------|--------|
| ✅ Keep & Promote | BSR < 200k, any sales last 90 days | Add to more products (hoodie, mug, tote) |
| 🔄 Refresh | Design looks dated, no sales but niche still viable | Redesign — same niche, new visual |
| ⚠️ Monitor | New design (<90 days), no sales yet | Wait 90 days before decision |
| ❌ Sunset | BSR >500k or 0 sales >180 days in dead niche | Remove or leave (no cost to keep) |

Output:
```markdown
# MBA Portfolio Triage — {date}
**Total ASINs**: {N} | **Active earners**: {N} | **Dead weight**: {N}

## Action Required

### Promote to more products ({N} ASINs)
- {ASIN / niche}: BSR {X}k, {N} sales/mo → add to hoodie + mug

### Refresh designs ({N} ASINs)
- {ASIN / niche}: niche viable but design quality low → new brief

### Sunset candidates ({N} ASINs)
- {ASIN / niche}: {reason}

## Quick Wins
1. {Specific action — e.g. "Add mugscafe US tag to coffee mug ASINs"}
2. {Specific action}
```

---

## Notes

- MBA does not provide live BSR in a public API — BSR assessments use search result signals and manual checks
- UK and US listings are separate — always write two listings if selling both markets
- MBA royalty calculator: at £15.99 UK standard shirt, royalty ≈ £2.00–£2.50
- Target: 20 sales/mo per ASIN = £40–£50/mo; 10 strong ASINs = £400–£500/mo passive
