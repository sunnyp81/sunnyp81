---
name: meta-generate
description: Generate SEO-optimized meta tags following semantic SEO principles. Use when creating title tags, meta descriptions, and schema markup.
user-invocable: true
allowed-tools: Read, WebSearch
argument-hint: "[file-path]"
version: 1.0.0
---

# Meta Tag Generator

Generate SEO-optimized meta tags following semantic SEO principles.

## Arguments

- `file` (optional): Path to content file. If no file, expects content pasted.

## Instructions

You are the **Ops Manager Meta Tag Specialist**. Generate all meta tags for publication-ready content.

### Process:

**1. Read Content** — Extract H1 (main topic), central entity + main attribute, key points/benefits, quality metrics/unique value props.

**2. Generate Title Tag**

**Format**: `[Main Keyword] - [Benefit/Modifier] | [Brand Name]`

**Rules**:
- 50-60 characters (including spaces)
- Include central entity + main attribute pair
- Front-load most important terms
- Use responsive terms (not just relevance terms from query)
- Include year if relevant (2026)
- Brand name optional (use if space allows)

**Title Tag Methodologies (KB-2)**:
1. **Conjunctive word method**: Use "and" to connect conditional synonyms. E.g., "German Singers: Their Works and Awards"
2. **Plural noun + set method**: Reflect a set for both noun and attribute. E.g., "Famous German Singers: Their Works and Awards"
3. **Hypernym-hyponym pair method**: E.g., "German Celebrities: Famous Poets, Authors, Actors and Musicians"

**Site-Wide Frequency Rule (KB-2)**: Search engines aggregate sitewide title tags to understand average topicality. Repeat key word types and lemmatizations across titles in the core section.

**Title-URL Alignment**: Title tags must align with URLs. Changes to one require changes to the other.

**3. Generate Meta Description**

**Format**: `[Representative Answer] [Supporting benefit or CTA]`

**Rules (KB-3)**:
- 150-160 characters
- START with answer (no preamble)
- Repeat the title with variation, then expand with article content
- Expand with heading concepts in order (H2-1, H2-2, etc.)
- Include context terms and topical entries
- Include quality metric ("complete guide", "best way")
- No commas except enumerations
- Responsive terms > Relevance terms
- CTA or benefit at end

**4. Generate URL Slug**

**Format**: `/category/main-attribute-modifier`

**Rules**:
- Shorter = better rankings
- No word repetition across segments
- Single or two words per segment max
- Most important attributes closer to root
- No stop words
- Core section (NODE): flatter structure. Outer section (SEED): deeper.

**5. Generate Image Alt Texts**

**Format**: `[Entity] [Attribute] [Context/Modifier]`

**Rules (KB-3)**:
- Alt tag = variation/expansion of image URL
- Image URL max 3 words
- Core section: enriching/longer alts. Outer section: shorter/concise
- No complete sentences; use conjunctive words and context terms
- Featured image alt = shorter version of H1
- Use brand logo and unique images to show human effort

**Image SEO extras**: Use EXIF/IPTC metadata. Google distinguishes object entity (what's in image) vs attribution entity (who created it). Bing indexes every page image.

**6. Schema Markup Recommendations**

Suggest appropriate schema based on content type: Article, FAQPage, HowTo, Product, Organization, Person, DefinedTerm.

**Critical distinction**: Validate at `validator.schema.org` for Knowledge Graph compliance. Use Google Rich Results Test only for rich results eligibility. These are different.

**Schema rules**:
- JSON-LD format (Google preferred), place in `<head>` or end of `<body>`
- `@id` must match Entity Home schema across all pages
- `alternateName` includes all name variations
- `sameAs` includes all verified profile URLs
- Entity Home schema is NOT sitewide — only on About page
- Full entity schema examples: see `/entity-authority` and `/schema-advanced` skills

---

## Output Template

```markdown
# META TAGS - [Page Title]

**Generated**: [Date] | **For**: [Filename/URL]

---

## TITLE TAG
`[Your title tag]`
**Length**: [X/60] | **Status**: Optimized

**Checks**: Central entity: Y/N | Main attribute: Y/N | Responsive: Y/N | Length optimal: Y/N

---

## META DESCRIPTION
`[Your meta description]`
**Length**: [X/160] | **Status**: Optimized

**Checks**: Starts with answer: Y/N | Quality metric: Y/N | CTA/benefit at end: Y/N | No improper commas: Y/N | Length optimal: Y/N

---

## URL SLUG
**Recommended**: `domain.com/[slug]`
**Alternatives**: `[alt-1]`, `[alt-2]`
**Depth**: Appropriate for NODE/SEED

**Checks**: No word repetition: Y/N | Appropriate depth: Y/N | No stop words: Y/N

---

## IMAGE ALT TEXTS
**Primary (Featured)**: `[alt — shorter H1]` | **URL**: `[max-3-words].jpg`
**Supporting**: 1. `[alt]` 2. `[alt]` 3. `[alt]`

**Checks**: Alt varies image URL: Y/N | URL max 3 words: Y/N | Featured alt = shorter H1: Y/N | No sentences: Y/N

---

## SCHEMA MARKUP
**Required**: [Schema types needed]
**JSON-LD**: [Ready to copy-paste code block]
**Validate at**: validator.schema.org (KG) + Google Rich Results Test (rich results)

---

## PUBLICATION CHECKLIST
- [ ] Title tag in CMS
- [ ] Meta description in CMS
- [ ] URL slug configured
- [ ] Image alt texts on all images
- [ ] Schema in page <head>
- [ ] Schema validated
- [ ] URL submitted to GSC
```

---

## Quality Standards

| Element | Requirements |
|---------|-------------|
| Title tag | Central entity included, under 60 chars, responsive language |
| Meta description | Starts with answer, under 160 chars, quality metric or benefit |
| URL slug | Short, no word repetition, appropriate depth for page type |
| Alt texts | Descriptive, natural, entity relationships, no keyword stuffing |
| Schema | JSON-LD, all required properties, @id consistent with Entity Home |

These meta tags determine CTR from SERPs, how Google understands the page, rich results eligibility, and AI citation likelihood.
