---
name: entity-authority
description: Build entity authority and Knowledge Panel presence using Jason Barnard's Kalicube framework integrated with Koray's semantic SEO. Covers Entity Home, corroboration, Knowledge Graph mechanics, lexicon pages, vector bending, and entity schema.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[brand or entity name]"
version: 1.0.0
---

# Entity Authority Builder

Generates a complete entity authority strategy: Entity Home setup, corroboration plan (30+ sources), Knowledge Graph entry, lexicon pages network, entity schema, and phased rollout.

## Arguments

- `entity` (required): Brand, person, or organization name
- `type` (optional): "organization" or "person" (default: organization)
- `domain` (optional): Primary website domain
- `industry` (optional): Industry/vertical

---

## Core Philosophy

**"Educate the Child That Is Google."** Five building blocks: Consistency, Authority, Corroboration, Recency, Depth.

---

## The 3-Step Framework

### Step 1: Entity Home

The authoritative source of truth (typically the About page). The Entity Home URL and kgmid form a "locked drawer" in Google's Knowledge Graph — extremely difficult to change once set.

**Requirements:** Modular description (100-150 words: what it is, what it does, who it serves, differentiators), semantic HTML5, Organization/Person schema (JSON-LD), machine-readable facts.

**Entity Home Schema Properties:**

| | Organization Essential | Organization Later | Person Essential | Person Later |
|---|---|---|---|---|
| | @type, name, alternateName, url, logo, description, foundingDate, founder, sameAs, contactPoint | award, alumni, memberOf, hasOfferCatalog, review, event, areaServed, numberOfEmployees | @type, name, alternateName, url, image, description, sameAs, jobTitle | award, alumniOf, memberOf, hasOccupation, worksFor, knowsAbout, publishingPrinciples |

**Critical Rules:**
- `@id` must be consistent across the entire web (use Entity Home URL)
- `alternateName` must include ALL variations (abbreviations, former names, misspellings)
- `sameAs` must list every verified profile URL
- Validate at `validator.schema.org` (NOT Google Rich Results Test)

### Step 2: Corroboration

Target ~30 independent sources stating the same facts consistently.

**5-Tier Hierarchy:**
1. **Platform Knowledge Graphs** — Wikidata (critical), Crunchbase, Google Books/Scholar
2. **Social Platforms** — LinkedIn (personal + company + articles), YouTube, Twitter/X, Facebook, Instagram
3. **Industry Directories** — G2/Capterra/TrustRadius, BBB/Yelp/Trustpilot, Clutch/GoodFirms, industry-specific
4. **Media & Editorial** — Guest articles, interviews, podcasts, press releases
5. **General Web** — Blog mentions, forums, Wikipedia (only if notable — don't rush)

**Wikidata Critical Properties:**
- Org: P1448 (official name), P1813 (short name), P31 (instance of), P17 (country), P571 (inception), P856 (website), P973 (described at), P159 (HQ), P112 (founder), P452 (industry), social media properties
- Person: P735/P734 (name), P569 (DOB), P19 (birthplace), P27 (citizenship), P106 (occupation), P108 (employer), P856 (website), social media properties

**Key Rule:** Every source must state facts CONSISTENTLY with the Entity Home.

### Step 3: Signposting

Create an "eternal loop": Entity Home > Wikidata/Crunchbase > third-party mentions > content pages > Entity Home. Each profile links back; content pages reference Entity Home; lexicon pages link to entity definitions.

---

## Knowledge Graph Mechanics

**Locked drawers** (hard to change): name, kgmid, Entity Home URL. **Unlocked drawers** (algorithmic): description, photos, dates, social links, related entities.

**Knowledge Verticals** (easier entry points that feed into the Knowledge Vault): Google Books (KDP/IngramSpark/Google Play), Podcasts, Google Scholar, Google Maps/GBP, YouTube Music, Google Shopping. Enter through Verticals first.

**Entity connections** must be close (same industry), strong (well-established entities), and long/permanent (founder-of, industry-member, headquartered-in).

---

## Lexicon Pages Strategy

Concept definition pages that position your entity as the defining authority for domain terms.

**Two-Part Definition:** Each page has a Consensus Definition (commonly accepted, builds trust) and a Proprietary Definition (your unique expansion, adds Information Gain). The proprietary definition must be genuinely unique.

**Structure:** Term > Consensus Definition (50-100 words) > [Entity]'s Definition (100-200 words) > Where We Use [Term] > Related Concepts (links to other lexicon pages) > Further Reading

**URL:** `/lexicon/`, `/definitions/`, or `/glossary/` parent path. Each page gets DefinedTerm schema.

**Internal linking:** Each lexicon page links to 3-5 related lexicon pages and 2-3 content pages. Content pages link back to lexicon definitions on first mention. Creates bidirectional semantic web.

| Lexicon Pages | Blog Content |
|---|---|
| Define concepts | Apply concepts |
| Evergreen, rarely updated | Time-sensitive, regularly refreshed |
| Short (300-600 words) | Long (1500+ words) |
| Build semantic authority | Build topical authority |

---

## Vector Bending & Semantic Centroid

Google's `site2vecEmbeddingEncoded` creates a vector for every site with site radius (topical width) and topical density (concentration).

When you define 20-50 core concepts via lexicon pages, your site's vector becomes the CENTROID for that concept cluster. Competitors without definitions are pushed to the periphery.

**5-Step Process:** Choose knowledge domain > Identify 20-50 core terms > Create consistent entity identifiers > Build lexicon network with interlinks > Get external corroboration (guest posts, citations)

---

## EAV Triples

Entity-Attribute-Value triples must be consistent everywhere (Entity Home, profiles, interviews, bios):

- [Entity] is-a [type], founded-in [year], headquartered-in [location], specializes-in [competency], serves [audience]
- [Person] is-a [role], works-at [org], expertise-in [domain], created [work], based-in [location]

---

## Entitization (KB-12)

Giving a brand actual meaning and connections to a search engine. Being an entity (not just a website) improves rankings.

**How:** Wikipedia/Wiki Fandom (if notable) > increase mentions/news/third-party articles > create relevant annotations between brand and industry > consistent naming across platforms.

**ROOT-SEED-NODE integration:** ROOT = Entity Home, SEED = sub-pages (products, services, team), NODE = entity-mentioning content (blogs, guides).

**Attribute Filtration:** Filter by Prominence (removing it changes what entity is), Popularity (search demand), Relevance (to source context).

---

## Phased Rollout

### Phase 1: Entity Foundation (Month 1-2)
- [ ] Create/optimize Entity Home with modular description
- [ ] Implement Organization/Person schema with consistent @id
- [ ] List all alternateName variations
- [ ] Prepare 100-150 word reusable description

### Phase 2: Structured Data Platforms (Month 2-3)
- [ ] Wikidata entry with all critical properties
- [ ] Crunchbase, GBP, YouTube, LinkedIn, Podcasts, Google Books (as applicable)

### Phase 3: Industry Corroboration (Month 3-4)
- [ ] 10-15 industry directories (complete ALL fields, identical description)
- [ ] 5-10 media mentions (guest posts, interviews, press)

### Phase 4: Content & Authority (Month 5-6)
- [ ] First 10-20 lexicon pages with DefinedTerm schema
- [ ] Internal linking between lexicon and content
- [ ] External link building to Entity Home

### Phase 5: Signposting & Maintenance (Month 7+)
- [ ] Complete eternal loop, quarterly consistency audit
- [ ] Expand to 30-50 lexicon pages, monitor Knowledge Panel
- [ ] Continue publishing to Knowledge Verticals

---

## Success Metrics

| Stage | Indicators |
|-------|-----------|
| Early (1-3mo) | Entity Home indexed, schema validated, 10+ consistent profiles, branded sitelinks |
| Mid (4-8mo) | Knowledge Panel sprout, autocomplete presence, Wikidata live (10+ props), 20+ sources |
| Mature (9-12mo+) | Full Knowledge Panel, related entity suggestions, lexicon in featured snippets |
| Ongoing | Consistency audit %, KP accuracy %, corroboration count, lexicon coverage % |

---

## AI Brand Selection — Two-Threshold Model

Entity authority now needs to address two distinct AI thresholds, not one:

**Threshold 1 — Retrieval:** Was your page relevant enough to surface as a source? (Traditional SEO + GEO fixes this)

**Threshold 2 — Brand selection:** Did the AI *recall* your brand name when deciding what to recommend? This comes from parametric (trained) knowledge — what the model learned during training, not what it retrieves at query time.

You can pass threshold 1 (appear as a citation source) but fail threshold 2 (never get named). This is a Ghost Citation.

### How Different LLMs Build Brand Associations

| LLM | Citation Bias | How to Win |
|---|---|---|
| **ChatGPT** | Established brands, mainstream consensus | Mainstream publications, large comparison sites, popular review platforms |
| **Perplexity** | Recent, cited sources | Recent press coverage + high-authority backlinks |
| **Gemini** | Google-indexed presence, rich structured data | Google ecosystem visibility — GBP, YouTube, Shopping, Scholar |
| **Claude** | Hedged, range of options | Factual density, multiple independent corroborating sources |

### Steps to Win Brand Selection (Threshold 2)

1. **Standardise brand-category naming** — use the same phrase for your category across all PR, homepage, guest posts, and metadata. Consistency trains the model.
2. **Third-party citation building** — industry publications, comparison sites, roundup articles, niche blogs. 85% of AI brand mentions come from off-site sources.
3. **Own the core category questions** — "What is best X?", "How does Y work?", "Difference between A and B?" — these are the prompts that surface brand recommendations.
4. **Freshness** — update content every 6 months. 70% of AI-cited pages were updated within the past year.
5. **Omni-presence for training data** — be present across the web in indexed, crawlable form. This shapes future model training, not just current RAG.

## 10 Common Mistakes

1. Claiming sprout panels too early
2. Inconsistent descriptions across platforms
3. Neglecting alternateName variations
4. Too much schema too soon (start with Entity Home only)
5. No Entity Home (About page is the foundation)
6. Self-promotional lexicon definitions (consensus first)
7. Ignoring Knowledge Verticals (books, podcasts, videos are easier entry)
8. No signposting (links must loop, not just go outward)
9. Non-unique proprietary definitions
10. Forgetting person-entity connections (founders, leaders)

---

---

## E-E-A-T Systematic Checklist

Use this checklist when auditing or building E-E-A-T signals for any site. Score each section 0-25 for a total E-E-A-T score out of 100.

### Experience (0-25)
- [ ] First-person experience evident in content ("I tested", "we measured", "in my experience")
- [ ] Original photos/screenshots (not stock images)
- [ ] Specific details that demonstrate hands-on use (model numbers, measurements, timeframes)
- [ ] Case studies or real examples from actual work
- [ ] Process documentation showing methodology
- [ ] Date stamps on experiences (recency matters)

### Expertise (0-25)
- [ ] Author has credentials/qualifications in the topic area
- [ ] Author bio with specific expertise claims (not generic)
- [ ] Lexicon pages defining domain terms (vector bending)
- [ ] Content demonstrates technical depth (not surface-level)
- [ ] knowsAbout schema property on Person entity
- [ ] Published in recognised industry sources (guest posts, conferences)

### Authoritativeness (0-25)
- [ ] Entity Home established with consistent @id
- [ ] 10+ corroborating sources stating same facts
- [ ] Wikidata entry (if eligible)
- [ ] Industry directory listings (Clutch, G2, niche-specific)
- [ ] Backlinks from authoritative domains in the niche
- [ ] sameAs links to verified profiles (LinkedIn, Twitter, etc.)
- [ ] Knowledge Panel or branded sitelinks appearing

### Trustworthiness (0-25)
- [ ] About page with real person/team details
- [ ] Editorial standards or methodology page
- [ ] Contact information (real address, phone, email)
- [ ] HTTPS everywhere, no mixed content
- [ ] Privacy policy and terms of service
- [ ] Reviews/testimonials from real customers
- [ ] Transparent disclosure (affiliate, sponsored, etc.)
- [ ] Consistent NAP (Name, Address, Phone) across the web

### Scoring Guide
| Score | Rating | Action |
|-------|--------|--------|
| 80-100 | Strong E-E-A-T | Maintain, expand lexicon pages |
| 60-79 | Moderate | Fill gaps in weakest pillar first |
| 40-59 | Weak | Prioritise Entity Home + corroboration sprint |
| 0-39 | Critical | Full E-E-A-T rebuild needed before content investment |

---

## Integration

Use with: `/topical-map` (semantic content network), `/semantic-brief` (entity-consistent briefs), `/content-writer` (maintain entity consistency), `/meta-generate` (entity schema), `/content-config` (search feedback optimization)
