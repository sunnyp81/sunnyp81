---
name: outreach-composer
description: Generate personalized link building and digital PR outreach emails. Research prospects, craft hooks, and create follow-up sequences.
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write
argument-hint: "[target page URL] [outreach type]"
version: 1.0.0
---

# Outreach Composer

Generate genuinely personalized outreach emails for link building and digital PR.

## Portfolio Context

- **Sender:** hello@sunnypatel.co.uk (Sunny Patel, SEO consultant based in Reading, UK)
- **Portfolio:** 44 SEO sites across UK niches (property, education, health, finance, tools)
- **Mailshake integration:** Campaign ID 1506609, API key stored in MEMORY.md. Note: API cannot set email content — paste manually in Mailshake UI
- **Market:** UK-focused. Use British English in all outreach copy (favour, optimise, colour, etc.)
- **Prospect CSV:** `C:\Users\sunny\Desktop\prospects.csv` (current list: 35 prospects in Berkshire, Surrey, Hampshire, Oxfordshire, Bucks)
- **Cold email copy reference:** `C:\Users\sunny\Desktop\sunnypatel-nextjs\cold-email-campaign.md`

## Outreach Types

| Type | When to Use | Hook Strategy |
|---|---|---|
| **Guest post** | Building authority links | Pitch unique angle they haven't covered |
| **Resource link** | Their page lists resources in your niche | Show your page fills a gap in their list |
| **Broken link** | Their page has dead outbound links | Offer your content as replacement |
| **Digital PR** | You have data/research to share | Lead with the surprising finding |
| **Brand mention** | They mentioned you without linking | Thank them, ask for link |
| **HARO/expert** | Journalist seeking sources | Lead with credentials + concise quote |
| **Cold outreach** | Agency/client prospecting | Lead with a specific problem you can solve for them |

## Prospect Research Process

1. **Identify target:** URL, domain, or niche provided by user
2. **Research the person:** Find their name, role, recent articles (last 3 months), social profiles
3. **Audit their site:** Check for content gaps, broken links, missing resources, or unlinked brand mentions relevant to our portfolio
4. **Find the hook:** One specific, genuine reference to their work — not generic flattery
5. **Check existing outreach:** Cross-reference against `prospects.csv` to avoid duplicate contact
6. **Select outreach type:** Match the best type from the table above to the opportunity
7. **Draft the sequence:** Initial email + 2 follow-ups (see templates below)

## Email Output Template

For each outreach, output the complete sequence in this format:

```
PROSPECT: [Name] — [Role] — [Company]
EMAIL: [their email address]
OUTREACH TYPE: [from table above]
HOOK: [1-line summary of the personalisation angle]

---

EMAIL 1 — Initial Contact

Subject: [under 50 chars, specific reference + value hint]

Hi [First Name],

[Personalised hook referencing their specific article/work — 1-2 sentences]

[What you have and why it's relevant to their audience — 2-3 sentences]

[Clear, low-friction ask — 1 sentence]

Cheers,
Sunny Patel
SEO Consultant — sunnypatel.co.uk

Word count: [must be under 150]

---

EMAIL 2 — Follow-up 1 (send Day 4)

Subject: [different angle, under 50 chars]

Hi [First Name],

[New value proposition or additional resource — NOT "just following up"]

[Brief, single ask]

Cheers,
Sunny

Word count: [must be under 100]

---

EMAIL 3 — Follow-up 2 (send Day 11)

Subject: [social proof or data angle, under 50 chars]

Hi [First Name],

[Social proof, new data point, or time-sensitive element]

[Graceful close — make it easy to say no]

All the best,
Sunny

Word count: [must be under 80]
```

## Follow-up Sequence Rules

- **Follow-up 1** (3-5 days later): Different angle, new value proposition. NOT "just following up."
- **Follow-up 2** (7-10 days later): Social proof or new data point. Last attempt — graceful close.
- Never send more than 3 total emails per prospect.
- Never use guilt, urgency, or manipulation tactics.
- Space the sequence across 2 weeks maximum.

## Key Rules

- Reference something SPECIFIC from their recent content (last 3 months)
- No mass-email language ("I came across your site", "I'm reaching out because", "I hope this email finds you well")
- Keep initial email under 150 words, follow-ups progressively shorter
- One clear ask per email
- Personalisation must be genuine, not templated feel
- British English throughout for UK prospects (American English only if targeting US sites)
- Always include the sender sign-off as Sunny Patel with sunnypatel.co.uk
- If prospect is a local business in the Home Counties, reference their area specifically

## Mailshake Workflow

1. Generate the sequence using this skill
2. Copy each email into Mailshake campaign UI (API cannot set content due to Vercel bot protection)
3. Set send timing to match the cadence above
4. Ensure hello@sunnypatel.co.uk is configured as sender in Mailshake before sending
