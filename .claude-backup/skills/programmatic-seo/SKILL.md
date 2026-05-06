---
name: programmatic-seo
description: Generate unique SEO pages at scale from structured datasets and templates. Includes quality checks, schema generation, and publishing velocity control.
user-invocable: true
allowed-tools: Read, Write, WebSearch, WebFetch
argument-hint: "[dataset CSV + template]"
version: 1.0.0
---

# Programmatic SEO Page Generator

Generate hundreds/thousands of unique, SEO-optimized pages from structured data + templates.

## Portfolio Context — Proven at Scale

We have built and deployed multiple large-scale pSEO sites, all using Astro SSG on Cloudflare Pages (Wrangler CLI):

| Site | Pages | Data Source | Template Pattern | Status |
|---|---|---|---|---|
| wagearea.com | 140,000+ | ONS ASHE salary data | Job title x Location | LIVE |
| catchment.school | 27,783 | School/catchment data | School pages + area pages | LIVE |
| carehome.page | 19,111 | Care home registry data | Care home x Area | LIVE |
| postcode.page | 14,397 | Postcode/geodata | Postcode x Area | LIVE |
| radon.tips | 2,374 | Radon measurement data | Area-level radon pages | LIVE |
| epc.report | 2,741 | EPC certificate data | Property x Street x Area | LIVE |
| rentalyield.uk | 2,355 | Rental yield data | Area x City x Region | LIVE |
| gathrd.co.uk | 1,676 | Venue/event data | Venue x Area | LIVE |
| planningleads.org | 572 | Planning application data | Council x Area | LIVE |

**Standard stack**: Astro 5/6 + Tailwind + static site generation (SSG). Deploy via Wrangler CLI to Cloudflare Pages. GitHub repo required (no direct uploads).

## Process Steps

1. **Identify pattern** — What repeating data x dimension combination creates unique pages?
   - Location-based: [entity] in [city/area/region]
   - Comparison: [entity A] vs [entity B]
   - Category: [entity] for [use case/industry]
   - Data: [metric] for [entity/location/time period]

2. **Source data** — Gather structured dataset
   - Government open data (ONS, HESA, planning portals)
   - Scraped/enriched datasets (with legal compliance)
   - API data (postcode.io, Google Places, etc.)
   - Format: CSV or JSON with one row per page

3. **Build template** — Create Astro page template with dynamic slots
   - `[...slug].astro` or `[location].astro` pattern
   - Slots for: H1, meta title, meta description, unique intro, data tables, FAQ, schema
   - Internal links: programmatic links to related pages (nearby, parent, children)

4. **Enrich content** — Add unique value beyond raw data substitution
   - AI-generated unique intro per page (min 100 words, contextual)
   - Local/entity-specific facts: population, landmarks, regional stats
   - FAQ section: 3-5 questions unique to the data row combination
   - Comparison/context: how does this data compare to national/regional averages?
   - Internal links to related pages in the same dataset

5. **Validate quality** — Run quality gates before build
   - Every page must pass the quality gate thresholds below
   - Spot-check 10 random pages manually before deploying full set
   - Check for empty data fields that produce broken/thin pages

6. **Generate and deploy**
   - `npm run build` to generate static pages
   - Verify build output: correct page count, no build errors
   - Deploy: `npx wrangler pages deploy out/ --project-name=[project]`
   - Submit sitemap to GSC and Bing after deploy

## Template Structure

```astro
---
// [entity].astro
export async function getStaticPaths() {
  const data = await loadData(); // CSV/JSON
  return data.map(row => ({
    params: { slug: row.slug },
    props: { ...row }
  }));
}
const { title, description, uniqueIntro, faqItems, relatedPages, schemaData } = Astro.props;
---
<Layout title={title} description={description}>
  <h1>{title}</h1>
  <p>{uniqueIntro}</p> <!-- Unique per page, not boilerplate -->

  <!-- Data section: tables, stats, visualizations -->
  <!-- FAQ section: 3-5 unique questions -->
  <!-- Internal links: related/nearby pages -->
  <!-- Schema: auto-generated JSON-LD -->
</Layout>
```

## Enrichment Rules

- Every page needs minimum 300 words of UNIQUE content (not shared boilerplate)
- Add local context: nearby landmarks, regional stats, neighbourhood references
- Add entity-specific facts: population, climate, industry data
- FAQ section: 3-5 questions unique to the data row combination
- Internal links to related pages in the same dataset (city → nearby cities, service → related services)
- No "lorem ipsum" or placeholder text — every field must have real data or the page should not be generated

## Quality Gates

| Check | Threshold | Action if Failed |
|---|---|---|
| Unique content ratio | >60% unique vs template | Add more enrichment |
| Word count | >500 words per page | Expand FAQ or add sections |
| Cross-page similarity | <30% shared sentences | Rewrite shared passages |
| Title tag uniqueness | 100% unique across all pages | Fix template variables |
| Meta description uniqueness | 100% unique | Fix template |
| Cannibalization | No 2 pages targeting same query | Merge or differentiate |
| Empty data fields | 0 empty required fields | Skip page or source data |
| Broken internal links | 0 broken links | Fix link generation logic |
| Schema validity | Valid JSON-LD per page | Fix schema template |

## Publishing Velocity

- **New site**: Start with 20-50 pages, then 50-100/day
- **Established site**: Up to 500/day if existing authority supports it
- Never publish >1,000 pages in a single day on a new domain
- Submit sitemap to GSC after each batch
- Monitor indexing rate — slow indexing = quality signal issue
- If <50% indexed after 2 weeks, investigate quality issues before adding more pages

## Schema Per Page

Auto-generate per page type:
- `Dataset` + `spatialCoverage` for data/location pages
- `LocalBusiness` + `areaServed` for business location pages
- `Service` + `provider` for service pages
- `Product` + `Offer` for product pages
- `FAQPage` for all pages with FAQ sections
- `BreadcrumbList` for all pages
- `WebSite` + `SearchAction` on homepage only

## Deployment Checklist

1. Build locally: `npm run build`
2. Check page count: `ls out/ | wc -l` matches expected
3. Spot-check 10 random pages in browser
4. Deploy: `npx wrangler pages deploy out/ --project-name=[project]`
5. Verify live: check 3 random URLs
6. Submit sitemap: GSC + Bing Webmaster Tools
7. Monitor indexing: check coverage report after 48 hours

## Key Rules

- Quality > quantity. 500 good pages beat 5,000 thin pages.
- Every page must answer a real search query (verify with autocomplete/GSC data)
- Noindex pages that fail quality gates until fixed
- Monitor for manual actions monthly
- UK spelling and conventions for all UK-market sites
- All repos must be on GitHub — no direct uploads to Cloudflare

## Integration with Other Skills

- `/keyword-cluster` — identifies the keyword patterns that drive page generation
- `/topical-map` — defines site architecture that pSEO pages slot into
- `/schema-advanced` — generates schema templates for each page type
- `/internal-link-mapper` — audits linking between generated pages at scale
- `/launch-seo` — post-deploy checklist for new pSEO sites
- `/index-push` — batch submit new pages to Google/Bing indexing APIs
- `/content-visuals` — generate inline SVGs for data visualization on pSEO pages
- `/site-health` — ongoing monitoring of pSEO site quality signals
