---
name: monetize-audit
description: Scan a site for monetization gaps — missing affiliate links, ad placements, schema markup, CTAs, and revenue opportunities. Use when assessing a site's monetization readiness.
user-invocable: true
allowed-tools: mcp__gsc-sunnypat81__*, mcp__gsc-2012infinite__*, mcp__playwright__*, WebSearch, WebFetch, Read, Write, Glob
argument-hint: "[domain e.g. colourlabelprinter.com]"
version: 1.0.0
---

# Monetize Audit — Revenue Gap Scanner

Analyze a site for monetization opportunities and gaps. Combines traffic data, content inventory, and competitive analysis to produce an actionable monetization plan.

## Arguments

- `domain` (required): The site domain (e.g. `colourlabelprinter.com`)
- `output` (optional): File path to save report. Defaults to `G:\My Drive\SEO\sites\{domain}\monetization-audit.md`

## Instructions

You are a **Monetization Strategist** performing a revenue gap analysis. Your job is to identify every missed monetization opportunity on the site.

### Process:

**Phase 1: Traffic & Rankings Pull**
- Pull GSC data using `sc-domain:{domain}` for last 28 days
- Get top queries by clicks and impressions
- Get top pages by clicks
- Identify high-CTR queries (>5%) — these are the best monetization targets
- Calculate total monthly traffic estimate

**Phase 2: Content Inventory**
- Use Playwright MCP to crawl the site's main pages: `browser_navigate` → `browser_snapshot` (DOM) + `browser_take_screenshot` per page. Start from homepage, follow nav links, check sitemap URL if available.
- For each page, note:
  - Page type (homepage, category, product review, blog post, info page)
  - Whether it contains product mentions or recommendations
  - Whether it has affiliate links (check for Amazon, ShareASale, CJ, etc.)
  - Whether it has display ad placements
  - Whether it has CTAs (email signup, contact form, booking)
  - Whether it has schema markup (Product, Review, FAQ, LocalBusiness)

**Phase 3: Competitive Monetization Analysis**
- WebSearch the site's top 3 queries
- Check how competing sites monetize (affiliate links, ads, lead forms)
- Note monetization methods the site is missing

**Phase 4: Revenue Model Classification**

Classify the site into one or more revenue models:

| Model | Best For | Signs |
|-------|----------|-------|
| **Amazon Associates** | Product review/comparison sites | Product mentions, "best X" queries |
| **Display Ads (AdSense/Mediavine)** | Content/info sites with traffic | High page views, informational queries |
| **Lead Generation** | Service/directory sites | Location queries, "near me" queries |
| **Digital Products** | Authority/niche sites | Engaged audience, how-to queries |
| **Sponsored Content** | Local/industry sites | Business listings, brand queries |
| **YouTube Revenue** | Video content sites | YouTube channel linked, video embeds |

**Phase 5: Generate Report**

```markdown
# MONETIZATION AUDIT: {domain}

**Date**: {date}
**Monthly Traffic**: ~{X} clicks (GSC 28d)
**Current Revenue**: £0 (no monetization detected)

## TRAFFIC SNAPSHOT

| Metric | 28-day Value |
|--------|-------------|
| Total Clicks | X |
| Total Impressions | X |
| Avg CTR | X% |
| Avg Position | X |

### Top Revenue-Potential Queries
| Query | Clicks | Impressions | CTR | Position | Revenue Potential |
|-------|--------|-------------|-----|----------|------------------|
| ... | ... | ... | ... | ... | High/Medium/Low |

### Top Pages
| Page | Clicks | Has Affiliates? | Has Ads? | Has Schema? |
|------|--------|-----------------|----------|-------------|
| ... | ... | Yes/No | Yes/No | Yes/No |

## RECOMMENDED REVENUE MODEL

**Primary**: {model} — {reason}
**Secondary**: {model} — {reason}

### Estimated Revenue Potential
| Model | Monthly Estimate | Assumptions |
|-------|-----------------|-------------|
| {model} | £X-£Y | Based on {traffic} clicks, {conversion}% conversion |

## MONETIZATION GAPS

### Missing Affiliate Links
- [ ] {page} mentions {products} but has no affiliate links
- [ ] {page} ranks for "{buying query}" but has no product recommendations

### Missing Ad Placements
- [ ] No ads.txt file found
- [ ] No display ad code detected on any pages
- [ ] High-traffic pages have no ad placements

### Missing Schema Markup
- [ ] No Product schema on product review pages
- [ ] No Review/Rating schema on comparison pages
- [ ] No FAQ schema on informational pages
- [ ] No LocalBusiness schema (if applicable)

### Missing CTAs
- [ ] No email signup form
- [ ] No contact/inquiry form (if lead gen applicable)
- [ ] No clear next-step for visitors

## ACTION PLAN

### Quick Wins (This Week)
1. {specific action with page/query reference}
   - **Revenue Impact**: £X-Y/month
   - **Effort**: Low

### Short Term (This Month)
1. {action}
   - **Revenue Impact**: £X-Y/month
   - **Effort**: Medium

### Medium Term (Next Quarter)
1. {action}

## ADS.TXT CONTENT

Generate the following ads.txt file for the site:
```
google.com, pub-XXXXXXXXXX, DIRECT, f08c47fec0942fa0
```
(Replace with actual AdSense publisher ID once approved)

## SCHEMA RECOMMENDATIONS

For each page type, recommend specific schema:
- Product review pages: Product + Review schema
- Comparison pages: ItemList + Product schema
- FAQ/info pages: FAQPage schema
- Local/directory pages: LocalBusiness schema
```

**Phase 6: Save Report**
- Save to specified output path or default `G:\My Drive\SEO\sites\{domain}\monetization-audit.md`
- Create site directory if needed

### Revenue Estimation Guidelines:

**Amazon Associates (UK)**
- Average commission: 1-10% depending on category
- Electronics/tech: 3-4%
- Sports/fitness: 4-5%
- Home/kitchen: 4-8%
- Assume 2-5% click-to-purchase conversion from affiliate links
- Formula: Monthly clicks to product pages × click-through to Amazon (30-50%) × conversion (2-5%) × avg product price × commission rate

**Display Ads (AdSense)**
- Typical RPM: £2-8 for niche content
- Formula: (Monthly pageviews / 1000) × RPM
- Higher RPM for: finance, health, tech, B2B

**Lead Generation**
- Typical lead value: £5-50 depending on industry
- Healthcare/legal: £20-50 per lead
- Home services: £10-30 per lead
- Formula: Monthly relevant clicks × conversion to inquiry (5-15%) × lead value
