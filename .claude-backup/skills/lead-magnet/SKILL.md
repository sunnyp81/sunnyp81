---
name: lead-magnet
description: Generate complete lead magnets (ebooks, checklists, templates, quizzes) with opt-in page copy and email nurture sequence.
user-invocable: true
allowed-tools: Read, Write, WebSearch
argument-hint: "[type] [topic] [audience]"
version: 1.0.0
---

# Lead Magnet Generator

Create a complete lead magnet package: content + opt-in page + delivery email + nurture sequence.

## Portfolio Context

- **Email capture:** Sites use StaticForms (staticforms.xyz) for form handling. No ESP integration yet — nurture sequences are stored as templates until an ESP is adopted.
- **Best format for SEO authority sites:** PDF lead magnets (checklists, guides, cheat sheets) work well. They build email lists and reinforce topical authority.
- **Key sites for lead magnets:** calculator.place (calculators → PDF guides), reportbolt.com (SEO report templates), sunnypatel.co.uk (SEO audit checklists for prospects), deadhangs.com (workout plans), planningleads.org (planning application guides).
- **Stack:** Astro/Next.js on Cloudflare Pages or Vercel. PDFs hosted on the same domain or via a CDN.
- **UK market:** British English for UK-facing sites. Use £ not $ for pricing examples.

## Process Steps

1. **Define the audience:** Who is this for? What problem do they have right now? What's their awareness level?
2. **Choose the format:** Match from the type table below. Shorter formats (checklist, cheat sheet) convert better than longer ones (ebook).
3. **Create the content:** Write the full lead magnet in markdown, structured for the chosen format. Must deliver genuine standalone value.
4. **Write opt-in page copy:** Headline, subheadline, bullet points, CTA, social proof — using the template below.
5. **Write delivery email:** Short, immediate gratification, sets expectations for what comes next.
6. **Write nurture sequence:** 3-5 emails that build from the lead magnet topic toward the paid offer or desired action.
7. **Output everything** in a single deliverable file using the templates below.

## Lead Magnet Types

| Type | Best For | Length | Conversion Rate |
|---|---|---|---|
| **Checklist** | Action-oriented audiences | 1-2 pages | Highest |
| **Cheat sheet** | Quick-reference seekers | 1 page | Highest |
| **Template** | Professionals saving time | 1-3 pages | High |
| **Ebook/guide** | Education-focused nurture | 10-25 pages | Medium |
| **Quiz/assessment** | Lead qualification + segmentation | 10-15 questions | High |
| **Calculator** | Data-driven decisions | Interactive HTML | High |
| **Swipe file** | Creative professionals | 10-20 examples | Medium |
| **Free tool/widget** | SaaS/tech audiences | Interactive | Highest |

## Output Template

### 1. Lead Magnet Content

```markdown
# [Title — Specific + Benefit-Driven]

## About This [Type]
[1-2 sentences: what it is, who it's for, what outcome it delivers]

## [Content sections structured for the format]
- Checklists: numbered actionable items with checkboxes
- Cheat sheets: categorised quick-reference blocks
- Templates: fill-in-the-blank sections with instructions
- Ebooks: chapters with subheadings, key takeaways per section
- Quizzes: questions with scoring logic and result descriptions

## Next Steps
[Brief pointer to the paid offer or deeper engagement]
```

### 2. Opt-in Page Copy

```markdown
**Headline:** [Benefit-driven, under 10 words]
**Subheadline:** [What they'll get + how fast — "Download the free X and [outcome] in [time]"]

**Bullet Points (3-5 specific outcomes):**
- [Outcome 1 — specific, measurable if possible]
- [Outcome 2]
- [Outcome 3]

**CTA Button:** [Action verb + what they get: "Download the Free Checklist"]
**Social Proof:** [X people downloaded / expert endorsement / "Used by [audience type]"]

**Form Fields:** Name + Email only (minimum friction)
**Privacy Note:** "No spam. Unsubscribe anytime."
```

### 3. Delivery Email

```markdown
**Subject:** Here's your [Lead Magnet Name]

[1 sentence: enthusiasm + download link]

[1 key insight from the magnet — give them a reason to open it NOW]

[What to expect next: "Over the next week, I'll send you [X] that builds on this."]

[Sign-off]

Word count: under 100
```

### 4. Nurture Sequence (3-5 emails)

```markdown
**Email 1 (Day 1):** Expand on the lead magnet topic. Deliver more value. No pitch.
- Subject: [related insight or tip]
- CTA: Read/watch/try [related free content]

**Email 2 (Day 3):** Case study or social proof. Show the outcome in action.
- Subject: [result or transformation story]
- CTA: See how [person/company] achieved [result]

**Email 3 (Day 5):** Address the main objection. Why they haven't taken action yet.
- Subject: [objection as a question]
- CTA: [Remove the objection — free trial, guarantee, FAQ link]

**Email 4 (Day 7):** Soft pitch. Position the paid offer as the logical next step.
- Subject: [bridge from free content to paid value]
- CTA: [Learn more / Book a call / Start free trial]

**Email 5 (Day 10):** Direct pitch with urgency. Last email in sequence.
- Subject: [deadline or scarcity — genuine, not manufactured]
- CTA: [Buy / Sign up / Book now]
```

## Key Rules

- Title must promise a specific outcome, not a vague topic ("The 7-Point SEO Audit Checklist" not "SEO Guide")
- Content must deliver genuine value — not a sales pitch disguised as a resource
- Keep checklists/cheat sheets to 1-2 pages (shorter = higher completion rate)
- Quiz results should segment leads for targeted follow-up
- British English for UK-facing sites
- All content must be accurate and actionable — no filler
- Nurture sequence should have a clear narrative arc, not disconnected emails
- StaticForms note: delivery email must be sent manually or via ESP — StaticForms only captures the submission, it does not send follow-ups
