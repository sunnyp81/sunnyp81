---
name: gbp-optimizer
description: Audit and optimize Google Business Profile. Generate posts, review responses, FAQ content, and local schema.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[business name] [location]"
version: 1.0.0
---

# Google Business Profile Optimizer

Audit GBP completeness, generate optimized content, and manage review responses.

## Portfolio Context

GBP is set up for:
- **SunnyPatel.co.uk** — SEO consultant, Reading, Berkshire. Primary category: SEO Service. Entity Home: sunnypatel.co.uk. GBP verified. Next: 5 more Google reviews to trigger star rating in local pack.
- **seo.associates** — SEO agency brand. GBP setup needed. Expires May 8.

Target markets: Reading, Berkshire, Surrey, Hampshire, Oxfordshire, Buckinghamshire, London fringe. All local SEO work should reinforce these geo signals.

## Process Steps

1. **Audit existing GBP** — Score each element against the checklist below (0-100 total)
2. **Optimize business info** — Name, categories, description, services, attributes, hours
3. **Generate posts** — 30-day post calendar with copy, image prompts, and CTAs
4. **Write FAQ content** — Pre-answer top 10 questions for Ask Maps / Gemini
5. **Create review response templates** — Personalized responses for positive, neutral, and negative reviews
6. **Add local schema** — Generate LocalBusiness JSON-LD matching GBP data exactly
7. **NAP audit** — Check consistency across all directories and citations
8. **Output report** — Scored audit with prioritized action items

## Audit Checklist & Scoring

| Element | Weight | Check | Score |
|---|---|---|---|
| Business name | 10% | Matches Entity Home exactly (no keyword stuffing) | 0-10 |
| Categories | 15% | Primary + 5-9 secondary categories selected | 0-15 |
| Description | 10% | 750 chars, keywords naturally integrated, matches Entity Home | 0-10 |
| Services/Products | 10% | All services listed with descriptions and prices where applicable | 0-10 |
| Attributes | 5% | All applicable attributes checked (online appointments, etc.) | 0-5 |
| Photos | 10% | Logo, cover, interior, exterior, team, product photos (min 10) | 0-10 |
| Posts | 10% | Active posting (weekly minimum), mix of post types | 0-10 |
| Reviews | 15% | Response rate >90%, response time <24hrs, 5+ reviews for stars | 0-15 |
| Q&A | 10% | Top 10 questions pre-answered | 0-10 |
| Hours | 5% | Accurate including holidays/special hours | 0-5 |
| **Total** | **100%** | | **0-100** |

## Output Template: GBP Audit Report

```
# GBP Audit Report: [Business Name]
Date: [Date]
Overall Score: [X]/100

## Scores by Element
- Business Name: [X]/10 — [pass/fail notes]
- Categories: [X]/15 — Primary: [cat], Secondary: [list]
- Description: [X]/10 — [current char count], [keyword coverage]
- Services: [X]/10 — [count listed], [missing services]
- Attributes: [X]/5 — [checked/available]
- Photos: [X]/10 — [count by type]
- Posts: [X]/10 — [last post date], [frequency]
- Reviews: [X]/15 — [count], [avg rating], [response rate]
- Q&A: [X]/10 — [answered/unanswered]
- Hours: [X]/5 — [accuracy check]

## Priority Actions
1. [Highest-impact fix]
2. [Second fix]
3. [Third fix]

## Generated Content (below)
```

## Post Calendar (30 Days)

Generate 8-12 posts per month mixing these types:

| Type | Frequency | Purpose | CTA |
|---|---|---|---|
| **What's New** | 2-3/month | Business updates, new services, case studies | Learn More |
| **Events** | 1-2/month | Upcoming events, webinars, promotions | Sign Up / Book |
| **Offers** | 2-3/month | Special deals with clear deadline | Call Now / Order |
| **Tips/Education** | 2-3/month | Industry advice positioning expertise | Read More |

### Post Template
```
Week [X] — [Post Type]
Title: [5-8 words, local keyword included]
Body: [150-300 words, conversational, local references]
Image prompt: [Description for AI image generation or photo suggestion]
CTA: [Button text] → [URL]
Local keyword: [target keyword]
```

### Monthly Schedule Example
- Week 1: What's New + Tip
- Week 2: Offer + Education
- Week 3: What's New + Event
- Week 4: Tip + Offer

## Review Response Templates

**Positive (4-5 stars)**: Thank by name → acknowledge specific detail they mentioned → reinforce the service/product → invite back. Keep under 100 words.

**Negative (1-2 stars)**: Empathize → take responsibility (no excuses) → offer offline resolution → provide contact info. Keep under 100 words. Never argue.

**Neutral (3 stars)**: Thank → ask what could improve → offer to discuss offline. Keep under 75 words.

**Rules**:
- Never use the same response twice. Personalize every reply referencing their specific comments.
- Respond within 24 hours.
- Include a local keyword naturally in 50% of responses (e.g., "SEO services in Reading").
- Never be defensive. Even unfair reviews get a professional, empathetic response.

## FAQ Content for Ask Maps / Gemini

Pre-answer the top 10 questions Gemini might generate about the business:

1. What services do you offer?
2. What are your hours?
3. How much does [primary service] cost?
4. Do you serve [nearby area]?
5. What makes you different from [competitor type]?
6. How long have you been in business?
7. Do you offer free consultations?
8. What industries do you specialize in?
9. Can I see examples of your work?
10. How do I get started?

Format: Clear, factual, 2-3 sentence answers. Facts must match Entity Home exactly.

## NAP Consistency Audit

Check Name, Address, Phone across:
- Website footer + contact page
- Google Business Profile
- Yelp, Yell.com (DA55), Bark.com (DA68)
- Thames Valley Chamber (DA50+)
- Clutch, DesignRush, GoodFirms
- Social profiles (LinkedIn, Twitter/X, Facebook)
- Industry directories

Flag ANY inconsistency — even minor formatting differences (e.g., "Rd" vs "Road") hurt local rankings.

## LocalBusiness Schema Output

Generate JSON-LD that matches GBP data exactly:
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "[Exact GBP name]",
  "url": "[Entity Home URL]",
  "telephone": "[GBP phone]",
  "address": { "@type": "PostalAddress", ... },
  "geo": { "@type": "GeoCoordinates", "latitude": "X", "longitude": "Y" },
  "areaServed": [{ "@type": "Place", "name": "[Area]" }],
  "openingHoursSpecification": [...],
  "sameAs": ["[all profile URLs]"],
  "hasOfferCatalog": { "@type": "OfferCatalog", "itemListElement": [...] }
}
```

## Integration with Other Skills

- `/schema-advanced` — generates the LocalBusiness schema block
- `/entity-authority` — Entity Home and corroboration strategy feed into GBP optimization
- `/geo-optimizer` — local AI citation strategy complements GBP presence
- `/outreach-composer` — review request emails to clients
- `/launch-seo` — GBP setup is part of new site launch checklist for service businesses
