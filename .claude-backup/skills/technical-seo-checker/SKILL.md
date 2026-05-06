---
name: technical-seo-checker
description: Scored technical SEO audit (0-100) across 8 areas — crawlability, indexability, Core Web Vitals, mobile, security, structured data, URLs, and international SEO. Produces prioritised fix list with affected page counts.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write, Bash, mcp__gsc__*
argument-hint: "[domain URL to audit]"
version: 1.0.0
---

# Technical SEO Checker

Comprehensive technical SEO audit producing a scored health report (0-100) with issue triage, affected page counts, and a phased implementation roadmap.

## When to Use

- New site launches (run before GSC submission)
- Diagnosing ranking drops
- Pre/post migration audits
- Regular health checks (quarterly for portfolio sites)
- Core Web Vitals issues
- Crawl or indexation problems

## 8 Audit Areas

### 1. Crawlability (15 pts)

**Check:**
- `robots.txt` — fetch and review for unintended blocks
- XML sitemap — fetch, validate format, check page count vs actual pages
- Site hierarchy — important pages within 3 clicks of homepage
- Crawl budget — no infinite URL patterns, faceted nav handled
- Internal linking — no orphan pages, strategic link distribution

**Common issues in our portfolio:**
- Missing or outdated sitemaps (many Astro sites need sitemap regeneration)
- robots.txt blocking AI bots (check GPTBot, ClaudeBot, PerplexityBot)

### 2. Indexability (15 pts)

**Check:**
- Index coverage via GSC (if available) or `site:domain.com` search
- Canonical tag consistency (HTTP/HTTPS, www/non-www, trailing slashes)
- Redirect chains (max 1 redirect, never >2)
- Duplicate content — check for parameter-based duplicates
- `noindex` tags — verify intentional, not accidental
- Bing indexation — check `site:domain.com` on Bing (many portfolio sites missing)

**Known portfolio issues:**
- Trailing slash inconsistency on several Astro sites
- Many sites not submitted to Bing Webmaster Tools

### 3. Site Speed / Core Web Vitals (15 pts)

**Check (use PageSpeed Insights API or WebFetch the URL):**
- **LCP** (Largest Contentful Paint): target < 2.5s
- **INP** (Interaction to Next Paint): target < 200ms
- **CLS** (Cumulative Layout Shift): target < 0.1
- **TTFB** (Time to First Byte): target < 800ms
- Image optimization — WebP/AVIF format, responsive `srcset`, lazy loading
- Font loading — `font-display: swap`, preload critical fonts
- JS/CSS — minified, tree-shaken, no render-blocking resources

**Portfolio note:** Our Astro SSG sites on Cloudflare Pages should score well here. Flag any that don't.

### 4. Mobile-Friendliness (10 pts)

**Check:**
- Viewport meta tag present
- Touch targets minimum 48x48px
- No horizontal scroll
- Font size minimum 16px for body text
- Hamburger nav working (we've added this to most sites)
- Content not truncated on mobile

### 5. Security (10 pts)

**Check:**
- HTTPS enforced (HTTP → HTTPS redirect)
- HSTS header present
- No mixed content warnings
- Security headers: `X-Content-Type-Options`, `X-Frame-Options`, CSP
- SSL certificate valid and not expiring soon

### 6. Structured Data (15 pts)

**Check:**
- JSON-LD schema present and valid
- Appropriate schema types used (Article, FAQPage, HowTo, Product, Organization, WebSite, BreadcrumbList)
- `dateModified` present on content pages
- No schema errors (validate against schema.org)
- `SpeakableSpecification` on key answer sections (for AI citation)

**Portfolio standard:** Every site should have at minimum WebSite + SearchAction schema on homepage, Article/WebPage on content pages.

### 7. URL Structure (10 pts)

**Check:**
- Clean, descriptive URLs (no IDs, query strings, excessive depth)
- Consistent trailing slash policy
- No `-uk` suffix on `.co.uk` domains (portfolio rule)
- Breadcrumb navigation matching URL hierarchy
- 404 page exists and returns proper status code
- No redirect loops or chains

### 8. International SEO (10 pts)

**Check (only if applicable):**
- `hreflang` tags for multi-language/region content
- Correct `hreflang` values (e.g., `en-gb` not `en-uk`)
- Self-referencing hreflang
- `x-default` specified
- Content actually localised (not just translated)

**For most portfolio sites:** Score full marks if single-language UK English with correct `lang="en-GB"` attribute. Deduct only if lang attribute is missing.

## Audit Process

### Step 1: Fetch Key Resources
```
- GET {domain}/robots.txt
- GET {domain}/sitemap.xml (or sitemap-index.xml)
- GET {domain}/ (homepage)
- GET 2-3 key content pages
```

### Step 2: Check Each Area
Run through all 8 areas systematically. For each issue found, record:
- What the issue is
- How many pages are affected (or estimate)
- Severity (Critical / High / Medium / Low)

### Step 3: Score and Report

## Output: Technical SEO Report

```markdown
# TECHNICAL SEO AUDIT: {domain}
**Date**: {date}
**Audited by**: Claude Code Technical SEO Checker

## HEALTH SCORE: {X}/100

| Area | Score | Max | Status |
|------|-------|-----|--------|
| Crawlability | {X} | 15 | {icon} |
| Indexability | {X} | 15 | {icon} |
| Core Web Vitals | {X} | 15 | {icon} |
| Mobile | {X} | 10 | {icon} |
| Security | {X} | 10 | {icon} |
| Structured Data | {X} | 15 | {icon} |
| URL Structure | {X} | 10 | {icon} |
| International | {X} | 10 | {icon} |

Status icons: Pass (13+/15, 8+/10) | Warn (8-12/15, 5-7/10) | Fail (<8/15, <5/10)

## CRITICAL ISSUES (Fix immediately)
| # | Issue | Area | Pages Affected | Fix |
|---|-------|------|---------------|-----|
| 1 | {issue} | {area} | {count} | {specific fix} |

## HIGH PRIORITY (Fix this week)
| # | Issue | Area | Pages Affected | Fix |
|---|-------|------|---------------|-----|

## MEDIUM PRIORITY (Fix this month)
| # | Issue | Area | Pages Affected | Fix |
|---|-------|------|---------------|-----|

## LOW PRIORITY (Nice to have)
| # | Issue | Area | Pages Affected | Fix |
|---|-------|------|---------------|-----|

## IMPLEMENTATION ROADMAP

### Week 1: Critical fixes
- [ ] {task}

### Week 2: High priority
- [ ] {task}

### Week 3: Medium priority
- [ ] {task}

### Week 4: Polish
- [ ] {task}

## AI BOT ACCESS
| Bot | Status |
|-----|--------|
| GPTBot | ✓/✗ |
| ChatGPT-User | ✓/✗ |
| ClaudeBot | ✓/✗ |
| PerplexityBot | ✓/✗ |
| Google-Extended | ✓/✗ |
| Bingbot | ✓/✗ |
```

## Scoring Guidelines

### Crawlability (15 pts)
- 15: robots.txt clean, sitemap valid and complete, good internal linking
- 10: Minor sitemap issues or some orphan pages
- 5: Significant crawl barriers, missing sitemap, or excessive blocked paths
- 0: robots.txt blocking Googlebot or critical crawl failures

### Indexability (15 pts)
- 15: All important pages indexed in Google AND Bing, clean canonicals
- 10: Mostly indexed but some gaps, minor canonical issues
- 5: Significant indexation gaps, redirect chains, or canonical conflicts
- 0: Widespread indexation failures

### Core Web Vitals (15 pts)
- 15: All CWV pass on mobile and desktop
- 10: CWV pass on desktop, minor mobile issues
- 5: 1-2 CWV failing
- 0: All CWV failing

### Mobile (10 pts)
- 10: Fully responsive, good touch targets, readable
- 5: Mostly mobile-friendly with minor issues
- 0: Major mobile usability problems

### Security (10 pts)
- 10: HTTPS enforced, security headers present, valid SSL
- 5: HTTPS works but missing some headers
- 0: No HTTPS or mixed content

### Structured Data (15 pts)
- 15: Complete schema coverage, all valid, dateModified present
- 10: Basic schema present but gaps
- 5: Minimal or invalid schema
- 0: No structured data

### URL Structure (10 pts)
- 10: Clean URLs, consistent policy, proper 404, no redirect chains
- 5: Minor issues (some inconsistency)
- 0: Major URL problems

### International (10 pts)
- 10: Correct lang attribute, hreflang if multi-region (or N/A — full marks for single-language sites with correct lang)
- 5: Missing lang attribute
- 0: Incorrect hreflang implementation causing issues

## Portfolio Quick-Scan Mode

When auditing multiple portfolio sites, use a condensed format:

```
| Site | Score | Critical Issues | Top Fix |
|------|-------|----------------|---------|
| techloved.com | 72 | Missing Bing index | Submit to Bing WMT |
| bestreviews.co.uk | 65 | No schema, stale content | Add Article schema |
| calculator.place | 85 | None | Add FAQ schema |
```
