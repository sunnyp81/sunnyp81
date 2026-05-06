---
name: internal-link-mapper
description: Map a site's internal link graph, find orphan pages, identify linking gaps, and generate contextual link insertion recommendations. Use when running an internal link audit, fixing crawl-depth issues, surfacing orphan or underlinked pages, planning hub/cluster reorganisation, or when GSC shows pages with low impressions despite published content. Triggers on "internal links", "orphan pages", "link graph", "site architecture audit".
user-invocable: true
allowed-tools: Read, Write, WebSearch, WebFetch
argument-hint: "[domain or sitemap URL]"
version: 1.0.0
---

# Internal Link Mapper

Analyze a site's internal link structure. Find orphans, hubs, and gaps. Generate link insertion recommendations.

## Portfolio Context

Internal linking is especially critical for our large pSEO sites:

| Site | Pages | Risk | Notes |
|---|---|---|---|
| wagearea.com | 140,000+ | HIGH — orphan risk at scale | Salary data pages need city↔region↔national linking |
| catchment.school | 27,783 | HIGH — school↔area↔county links | Each school page should link to nearby schools + area page |
| carehome.page | 19,111 | HIGH — care home↔area↔region | Similar structure to catchment.school |
| postcode.page | 14,397 | MEDIUM — postcode↔area linking | Cluster by district code, link to nearby postcodes |
| radon.tips | 2,374 | MEDIUM | Area pages need cross-links to nearby areas |
| epc.report | 2,741 | MEDIUM | Property↔street↔area hierarchy |
| rentalyield.uk | 2,355 | MEDIUM | Area↔city↔region yield comparison links |
| planningleads.org | 572 | LOW | Council↔area links |
| signforge.org | 27 | LOW — small site, easy to audit manually | Blog↔pillar linking |

For small editorial/affiliate sites (bestreviews, mugscafe, deadhangs, calculator.place), focus on pillar↔cluster and hub↔spoke patterns.

## Process Steps

1. **Crawl/read sitemap** — Parse sitemap.xml or page list to get all URLs
2. **Build link graph** — For each page, extract all internal links (href values). Record source URL, target URL, anchor text, link position (nav/footer/body)
3. **Identify orphan pages** — Pages with zero inbound internal links from body content (nav/footer links don't count for this)
4. **Identify dead-end pages** — Pages with zero outbound internal links in body content
5. **Identify thin hubs** — High-authority pages (homepage, category pages) with fewer than 3 outbound body links
6. **Analyze anchor text** — Check for dilution, conflicts, and generic anchors
7. **Find linking gaps** — Topically related pages that don't link to each other
8. **Generate insertion recommendations** — Specific link placements with anchor text
9. **Output report** — Full link map with prioritized actions

## Structural Analysis

| Issue | Definition | Fix | Priority |
|---|---|---|---|
| **Orphan pages** | No inbound internal links from body content | Add links from topically related pages | Critical |
| **Dead-end pages** | No outbound internal links in body | Add links to related content | High |
| **Thin hubs** | High-authority pages with <3 outbound body links | Add outbound links to distribute equity | High |
| **Deep pages** | >3 clicks from homepage | Create shorter click paths via hub pages | Medium |
| **Over-linked pages** | >150 internal links on one page | Prune low-value links, consolidate | Medium |
| **Broken internal links** | 404 targets | Fix or redirect | Critical |

## Anchor Text Audit

- Flag anchor text used for >3 different target URLs (dilution)
- Flag target pages with conflicting inbound anchor text (confuses topic signal)
- Flag generic anchors ("click here", "read more", "this article", "learn more")
- Verify anchor text matches target page's seed query
- Check that annotation text (surrounding sentence) supports the contextual connection
- For pSEO sites: verify template-generated anchors are specific, not generic (e.g., "EPC data for {street}" not "view data")

## Link Insertion Recommendations

Per recommendation:
```
Source: [page URL]
Target: [page URL to link to]
Anchor Text: [recommended text — must match target's seed query]
Location: [which section/heading to place the link]
Context: [why this link makes sense contextually]
Annotation: [suggested surrounding sentence]
Priority: [Critical/High/Medium/Low]
```

## Rules (from Koray KB-11)

These are non-negotiable for all content on all sites:

1. **No links in first paragraph** of any section
2. **Max 1 link per heading section** (the space between two headings)
3. **Minimum 1 heading distance** between internal links — never link in consecutive sections
4. **Top 10 headings**: avoid links unless there is a strong lexical relation between source heading topic and target page
5. **Supplementary content sections**: more links allowed here, in lower heading hierarchy (H3, H4)
6. **First link to a page** = passes PageRank + relevance; subsequent links to same page = relevance only
7. **Header/footer links**: use different anchor text than main content body links to the same page
8. **Anchor text** should target the seed query of the linked page, not the source page's topic
9. **Annotation text** (surrounding text) must support the contextual connection — the sentence should make sense with or without the link

## Output Template

```
# Internal Link Audit: [domain]
Date: [date]
Pages analyzed: [count]

## Link Graph Summary
- Total pages: [X]
- Total internal links (body): [X]
- Total internal links (nav/footer): [X]
- Average body links per page: [X]
- Orphan pages: [X]
- Dead-end pages: [X]
- Deepest page depth: [X clicks from homepage]

## Critical Issues
[Orphans and broken links listed first]

## Structural Issues (prioritized)
| Page | Issue | Fix | Priority |
|---|---|---|---|

## Link Insertion Recommendations
[Top 20 recommendations with full detail per the format above]

## Anchor Text Report
- Diluted anchors: [list]
- Conflicting anchors: [list]
- Generic anchors to replace: [list]

## pSEO Template Fixes (if applicable)
[Changes to Astro templates that fix linking at scale]
```

## pSEO-Specific Guidance

For sites with 1,000+ pages generated from templates:

- Fix linking in the **template**, not page by page — one template change fixes thousands of pages
- Ensure each generated page links to its parent (area→region), siblings (nearby areas), and children (sub-pages)
- Use data-driven link selection: link to the 3-5 most geographically or topically proximate pages
- Verify no template produces orphan pages (every page type must be linked from at least one other page type)
- Add breadcrumb navigation that reflects the site hierarchy

## Integration with Other Skills

- `/topical-map` — the topical map defines the linking hierarchy (ROOT→NODE→SEED)
- `/semantic-audit` — audits whether internal links follow Koray KB-11 rules
- `/content-config` — internal link auditing is part of content configuration
- `/programmatic-seo` — template-level linking is built during pSEO page generation
- `/site-health` — link issues surface in site health checks
- `/launch-seo` — internal link equity distribution is part of launch checklist
