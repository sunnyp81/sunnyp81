---
name: schema-advanced
description: Generate complete JSON-LD schema for any page type — Product, LocalBusiness, Event, VideoObject, Course, Recipe, SpeakableSpecification, ItemList, and more.
user-invocable: true
allowed-tools: Read, Write, WebSearch
argument-hint: "[URL or content file]"
version: 1.0.0
---

# Advanced Schema Generator

Generate comprehensive JSON-LD schema covering the full schema.org vocabulary — beyond basic Article/FAQ.

## Portfolio Context

All 44 SEO sites in the portfolio should follow these schema standards:

- **Astro/CF Pages data sites** (catchment.school, wagearea.com, postcode.page, carehome.page, radon.tips, epc.report, rentalyield.uk, gathrd.co.uk): WebSite+SearchAction on homepage, Article on blog/guide pages, Dataset or DataCatalog on data pages, BreadcrumbList on all pages, FAQPage where FAQ sections exist.
- **Affiliate sites** (bestreviews.co.uk, bestvibrationplates.co.uk, bestturbotrainers.uk, mugscafe.org, techloved.com): Product+Offer+AggregateRating on review pages, ItemList on category/roundup pages, Article on editorial content.
- **Service sites** (sunnypatel.co.uk, seo.associates): LocalBusiness+Service on service pages, Person on about page, ProfessionalService as primary type.
- **Tool/calculator sites** (calculator.place, reportbolt.com, clearnote.app): SoftwareApplication on tool pages, WebSite+SearchAction on homepage.
- **Directory sites** (planningleads.org, complain.report): Organization on listing pages, ItemList on index pages.

## Process

1. **Detect** page type from content or URL pattern
2. **Select** all applicable schema types (primary + secondary)
3. **Generate** complete JSON-LD with all recommended + optional properties
4. **Validate** output structure against schema.org and Google requirements
5. **Output** ready-to-paste `<script type="application/ld+json">` blocks plus validation notes

## Schema Type Matrix

| Page Type | Primary Schema | Secondary Schema |
|---|---|---|
| Homepage (all sites) | WebSite + SearchAction | Organization or Person, SiteNavigationElement |
| Content/blog page | Article | FAQPage, BreadcrumbList, SpeakableSpecification |
| Product review page | Product + Offer | AggregateRating, Review, Brand, BreadcrumbList |
| Category/roundup page | ItemList + CollectionPage | BreadcrumbList, Organization |
| Local business page | LocalBusiness | openingHoursSpecification, geo, areaServed, hasOfferCatalog |
| Multi-location | Organization + LocalBusiness[] | areaServed per location |
| Event page | Event | Offer, Place, Performer, EventAttendanceMode |
| Video page | VideoObject | SpeakableSpecification, BreadcrumbList |
| Course/training | Course | CourseInstance, Offer, Organization |
| Recipe page | Recipe | NutritionInformation, AggregateRating, HowToStep |
| Job listing | JobPosting | Organization, Place, MonetaryAmount |
| How-to guide | HowTo + HowToStep | FAQPage, SpeakableSpecification |
| FAQ page | FAQPage | WebPage, SpeakableSpecification |
| Glossary/lexicon | DefinedTerm + DefinedTermSet | WebPage |
| Person/bio page | Person | sameAs, worksFor, knowsAbout |
| Software/SaaS tool | SoftwareApplication | Offer, AggregateRating, Review |
| Podcast | PodcastSeries + PodcastEpisode | Person, Organization |
| Data page (pSEO) | Dataset or DataCatalog | BreadcrumbList, Place (for location data) |
| Calculator/tool | WebApplication | Offer (free), SoftwareApplication |
| Service page | Service + provider | areaServed, Offer, FAQPage |

## Common Schema Patterns for Our Stack

### Homepage (every site)
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "[Site Name]",
  "url": "https://[domain]/",
  "description": "[Meta description]",
  "publisher": { "@type": "Organization", "name": "[Site Name]" },
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://[domain]/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### Article (blog/guide pages)
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[H1]",
  "description": "[Meta description]",
  "datePublished": "[ISO 8601]",
  "dateModified": "[ISO 8601]",
  "author": { "@type": "Person", "name": "[Author]" },
  "publisher": { "@type": "Organization", "name": "[Site Name]" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "[URL]" },
  "image": "[og:image URL]"
}
```

### Data/pSEO page (location data sites)
```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "[Page-specific dataset name]",
  "description": "[What data this page covers]",
  "spatialCoverage": { "@type": "Place", "name": "[Location]" },
  "temporalCoverage": "[Data date range]",
  "isPartOf": { "@type": "DataCatalog", "name": "[Site Name]" }
}
```

## Schema for AI Extraction — Critical Rules

Research from SearchVIU (tested across 5 AI systems) confirmed:

**Schema-only content fails completely.** In one test, product ratings existed only in schema (not visible HTML) — 0 out of 5 AI systems extracted them. With identical schema PLUS visible HTML, ChatGPT surfaced the ratings. The same information was always in the schema — schema changed whether AI *noticed* the visible content.

**The rule:** Everything important must exist in visible HTML first. Schema reinforces and guides extraction of what's already visible — it does not substitute for it.

**Why schema still matters for AI:**
- Acts as an attention mechanism — doesn't provide new info but helps AI notice and extract structured content
- Guides chunking — `FAQPage` schema keeps Q&A pairs together; `Product` schema keeps attributes together
- Enables relationship mapping between entities via `@graph` + `@id`

### @graph / @id Relationship Pattern

Connect entities explicitly rather than using isolated schema blocks:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#org",
      "name": "Brand Name",
      "sameAs": ["https://linkedin.com/...", "https://twitter.com/..."]
    },
    {
      "@type": "WebPage",
      "@id": "https://example.com/page/",
      "publisher": { "@id": "https://example.com/#org" },
      "author": { "@id": "https://example.com/#author" }
    },
    {
      "@type": "Person",
      "@id": "https://example.com/#author",
      "name": "Author Name",
      "worksFor": { "@id": "https://example.com/#org" }
    }
  ]
}
```

Use consistent `@id` values everywhere — they are the "locked drawer" that Google uses to connect your entity across the web.

## Key Properties Often Missed

- `SpeakableSpecification`: Marks sections AI can extract/speak. Add to every informational page.
- `mainEntityOfPage`: Connects schema to the page's primary topic. Required on Article pages.
- `sameAs`: Array of ALL profile URLs (critical for entity recognition). Use on Person and Organization.
- `alternateName`: All name variations (abbreviations, former names).
- `lastReviewed` / `dateModified`: Freshness signals for AI citation. Always include.
- `isPartOf`: Connect pages to parent site/series. Important for pSEO sites with thousands of pages.
- `areaServed`: Required for service and local business pages. Use GeoCircle or Place.
- `potentialAction`: SearchAction on WebSite schema enables Google sitelinks search box.

## Validation

- **Primary**: `validator.schema.org` (Knowledge Graph completeness)
- **Secondary**: Google Rich Results Test (SERP feature eligibility)
- **Checks**: No missing required properties, no conflicting types, valid URLs in all link fields, datePublished/dateModified in ISO 8601, image URLs resolve

## Output Format

For each page analyzed, output:

1. **Page type identified**: What type of page this is and why
2. **Schema types selected**: Primary and secondary with rationale
3. **Complete JSON-LD block**:
```html
<script type="application/ld+json">
[Generated schema here]
</script>
```
4. **Validation notes**: Warnings, missing optional properties worth adding, Google rich result eligibility
5. **Integration note**: Where to place in Astro layout (typically in `<head>` via `<Fragment slot="head">`)

## Integration with Other Skills

- `/meta-generate` — generates title/description that should match schema headline/description
- `/launch-seo` — includes schema as part of day-one checklist
- `/programmatic-seo` — auto-generates schema per page type at scale
- `/gbp-optimizer` — generates LocalBusiness schema aligned with GBP data
