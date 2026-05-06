---
name: launch-seo
description: Day-one SEO launch checklist for new sites. Covers indexing submissions, E-E-A-T schema, internal link equity, OG images, CWV font loading, cross-site backlinks, and crawl architecture. Run this after first deploy.
user-invocable: true
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
argument-hint: "[site URL or project path]"
version: 1.0.0
---

# Launch SEO — Day One Ranking Accelerator

Run this skill immediately after deploying a new content site. Covers everything that helps Google discover, crawl, index, and rank your pages faster.

## Arguments

- `site` (required): Site URL (e.g. https://selflandlord.com) or local project path
- `priority-pages` (optional): Comma-separated list of most important URLs to push first

## Pre-Flight Checks

Before running the checklist, verify:
1. Site is live and accessible (curl the homepage)
2. Sitemap exists and is valid XML
3. robots.txt allows crawling
4. Build completes without errors

## Launch Checklist

Execute each section in order. Skip items marked [MANUAL] — flag them to the user.

---

### 1. Indexing Submissions

**Google Search Console:**
- Add site property via GSC MCP (`mcp__gsc__add_site`)
- Submit sitemap (`mcp__gsc__submit_sitemap`)
- If sitemap fails (unverified): flag user to add DNS TXT record
- Submit priority URLs via Google Indexing API (service account at `C:\Users\sunny\Downloads\claudeindex-6b5681c013d4.json`)

**Bing Webmaster Tools:**
- Add site via Bing MCP (`mcp__bing__add_site`)
- Submit sitemap (`mcp__bing__submit_sitemap`)
- Batch submit priority URLs (`mcp__bing__submit_url_batch`)
- If unverified: flag user for CNAME/meta tag verification

**Ping services:**
```
GET https://www.google.com/ping?sitemap={sitemap_url}
GET https://www.bing.com/ping?sitemap={sitemap_url}
```

### 2. Crawl Architecture

**A-Z / HTML Sitemap page:**
- Create a hub page that links to EVERY page on the site
- Add it to the footer for sitewide crawl access
- This gives crawlers 1-hop discovery of all content

**Internal link equity from stubs:**
- Even placeholder/stub pages should contain 2-3 contextual links to full-content pages
- Each stub should link to the most topically relevant full pages
- This passes link equity from the topical map to your money pages from day one

**Footer links:**
- Include links to all major sections (guides hub, tools hub, compare hub)
- Include links to 5-6 top content pages
- Include A-Z hub link

**Verify no orphan pages:**
- Every page must have at least one inbound internal link
- Check: compare sitemap URLs against pages linked from the A-Z hub

### 3. E-E-A-T Signals

**Author schema (Person entity):**
- Article schema author should be `@type: Person` (not Organization)
- Include: name, url, jobTitle, sameAs (LinkedIn, personal site)
- This connects content to a real person in Google's Knowledge Graph

**Publisher schema (Organization entity):**
- Include founder field linking to the Person entity
- Include logo, description, url

**About page:**
- Real author name and bio (not generic "our team")
- Specific expertise claims ("I self-manage my own rentals")
- Editorial standards section ("content is checked against current legislation")
- Link to author's external profiles (personal site, LinkedIn)

**AboutPage schema:**
- `@type: AboutPage` with mainEntity pointing to Organization
- Organization includes founder Person entity with knowsAbout array

### 4. Technical SEO

**OG / Social images:**
- Create a default 1200x630 OG image with site name and tagline
- Set as fallback in BaseLayout when no page-specific image exists
- SVG → PNG conversion (use sharp-cli)

**Font loading for CWV:**
- Preconnect to font CDN
- Preload font stylesheet
- Use `media="print" onload="this.media='all'"` pattern for non-blocking load
- Noscript fallback

**WebSite schema with SearchAction:**
- Add to homepage for sitelinks search box potential
- `potentialAction.target.urlTemplate` should point to a search/filter page

**404 page:**
- Custom 404 with links to popular pages
- Helps recover crawl equity from broken links
- Set noIndex on 404

**Canonical URLs:**
- Every page must have a canonical tag
- Trailing slash consistency (match trailingSlash config)

**robots.txt:**
- Allow all crawlers
- Reference sitemap URL

### 5. Cross-Site Backlinks

**[MANUAL] Link from existing properties:**
- Identify sites in the user's portfolio that are topically related
- Add a contextual link from a relevant page (not just footer spam)
- Example: SEO agency site → "We also built [SelfLandlord](https://selflandlord.com) for UK landlords"
- Even 1-2 links from established domains massively accelerate initial authority

**[MANUAL] Directory submissions:**
- If the site has a business entity: submit to relevant directories
- For SaaS: Product Hunt, AlternativeTo, G2
- For content sites: niche directories in the vertical

### 6. Wave Publishing Protocol

Google needs to "learn" your site. Publishing everything at once confuses crawl patterns.

**Phase 1: Core Pages (Week 1)**
- Publish 5-10 core pages only (ROOT + top NODEs)
- These must be your highest-quality, most entity-rich pages
- Submit to GSC + Bing immediately
- Wait for: crawl → index → first impressions (typically 1-2 weeks)

**Phase 2: Controlled Expansion (Weeks 2-6)**
- Publish 2-3 new pages per week
- Each batch should be topically related to existing indexed pages
- Update 1-2 older pages weekly (add internal links, expand sections)
- Monitor: crawl frequency increasing? New queries appearing in GSC?

**Phase 3: Steady State (Week 7+)**
- Maintain 2-3 new pages/week cadence
- Weekly updates to existing pages (signals "human effort" to Google)
- Google builds a crawl habit based on your publishing cadence — consistency matters more than volume

**Why this works:** Google assigns crawl budget based on observed publishing patterns. Dumping 500 pages day one means most won't be crawled for weeks. Controlled waves train Google to return frequently.

**For pSEO sites (100+ pages):**
- Still launch with 5-10 core hand-crafted pages
- Deploy template pages in batches of 50-100 per week
- Ensure each batch has unique content enrichment, not just template swaps
- Update the A-Z hub and internal links with each batch

### 7. Human Effort Signals

Google rewards evidence of multi-disciplinary work. After launch, ensure:

- [ ] Pages updated at least weekly (even small improvements count)
- [ ] Mix of content types: text + tables + visuals + interactive elements
- [ ] Clear UX improvements over time (not just content dumps)
- [ ] Structured data added progressively (not all at once)
- [ ] Internal linking reflects real user journeys, not just SEO convenience

### 8. Content Readiness

**Verify semantic SEO compliance on priority pages:**
- Run `/semantic-audit` on each full-content page
- Score must be 90+ before considering it "launched"

**Verify schema validation:**
- Spot-check 2-3 pages in Google Rich Results Test
- Check for errors/warnings in structured data

**Meta tags:**
- Every page has unique title and description
- Title format: `{Page Title} | {Site Name}`
- Description under 160 chars

---

## Output

Generate a launch report:

```markdown
# SEO Launch Report: {site_name}

## Indexing
- GSC: [added/verified/pending]
- Bing: [added/verified/pending]
- Sitemap submitted: [yes/no]
- URLs pushed via Indexing API: [count]
- Ping sent: [yes/no]

## Architecture
- Total pages: [count]
- A-Z hub page: [created/existing]
- Orphan pages: [count]
- Footer links to top pages: [yes/no]

## E-E-A-T
- Author Person schema: [yes/no]
- About page with real bio: [yes/no]
- Editorial standards: [yes/no]
- External author links: [count]

## Technical
- OG image: [yes/no]
- Font preloading: [yes/no]
- WebSite SearchAction: [yes/no]
- 404 page: [yes/no]
- robots.txt: [yes/no]

## Manual Actions Needed
1. [list items flagged as MANUAL]
```

## When to Use This Skill

Run `/launch-seo` immediately after:
- First deploy of any new content site
- Migrating a site to a new domain
- Major redesign/rebuild that changes URL structure

Do NOT use for:
- Ongoing SEO maintenance (use `/gsc-audit` or `/site-health` instead)
- Content writing (use `/semantic-brief` → `/content-writer` → `/semantic-audit`)
- Schema generation for individual pages (use `/schema-advanced`)
