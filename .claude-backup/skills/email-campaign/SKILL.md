---
name: email-campaign
description: Generate complete email drip sequences with subject lines, body copy, CTAs, and send timing. Supports nurture, re-engagement, promo, and welcome flows.
user-invocable: true
allowed-tools: Read, Write
argument-hint: "[campaign type] [audience] [offer]"
version: 1.0.0
---

# Email Campaign Generator

Generate complete email sequences optimised for open rates, click-through, and conversion.

## Portfolio Context

- **Email capture:** Portfolio sites use StaticForms (staticforms.xyz) for form handling. No ESP (Mailchimp, ConvertKit, etc.) integration yet — sequences are manual or via Mailshake for outreach.
- **Mailshake:** Used for cold outreach campaigns (API key in MEMORY.md). Campaign ID 1506609.
- **UK market:** Use British English for UK-facing sites (optimise, favour, colour, etc.). American English only for explicitly US-targeting sites.
- **Key sites with email capture:** calculator.place, deadhangs.com, epc.report, punchfoods.com, complain.report, planningleads.org, redlighttherapy.expert
- **Current state:** Email addresses are collected but not yet fed into an ESP. Sequences generated here should be ready to paste into any ESP when one is adopted.

## Process Steps

1. **Define the goal:** What action should the subscriber take by the end of the sequence? (purchase, book a call, visit a page, share, etc.)
2. **Identify the audience:** Who is receiving this? What do they know? What are their objections? What triggered their signup?
3. **Choose campaign type:** Match from the table below.
4. **Map the sequence:** Define number of emails, cadence, and the narrative arc (education → trust → conversion).
5. **Write each email:** Use the per-email template below. Always provide 2 subject line variants for A/B testing.
6. **Review the arc:** Ensure each email builds on the previous one. No email should repeat the same value prop.
7. **Output the complete sequence** in a single deliverable file.

## Campaign Types

| Type | Emails | Cadence | Goal |
|---|---|---|---|
| **Welcome** | 5-7 | Days 0, 1, 3, 5, 7, 10, 14 | Onboard + first conversion |
| **Nurture** | 5-8 | Weekly | Build trust + educate |
| **Re-engagement** | 3-4 | Days 0, 3, 7, 14 | Win back inactive subscribers |
| **Promo/Launch** | 4-5 | Announcement, reminder, last chance, follow-up | Drive sales |
| **Post-purchase** | 3-4 | Days 1, 7, 14, 30 | Retain + upsell |
| **Lead magnet delivery** | 3-5 | Days 0, 1, 3, 5, 7 | Deliver asset → nurture → convert |

## Per Email Output Template

```markdown
## Email [X] of [Y] — Send: [Day/Timing]

**Subject Line A:** [under 50 chars, personalisation token]
**Subject Line B:** [A/B variant, different angle]
**Preview Text:** [under 90 chars, complements subject — not a repeat]

---

**Body:**

[Opening hook — 1 sentence, ties to previous email or trigger]

[Value section — 2-3 short paragraphs, one idea each]

[CTA — single clear action, button text suggestion]

[P.S. line — secondary hook or urgency element]

---

**Word Count:** [150-300]
**CTA Button Text:** [action verb + benefit]
**CTA URL:** [landing page or resource URL]
**Goal of this email:** [1 sentence — what should the reader do/feel after reading?]
```

## Complete Sequence Output Format

```markdown
# Email Campaign: [Campaign Name]

**Type:** [Welcome/Nurture/Re-engagement/Promo/Post-purchase/Lead magnet]
**Audience:** [description]
**Goal:** [end action]
**Total Emails:** [X]
**Sequence Duration:** [X days]
**Language:** [British English / American English]

---

[Per-email blocks as above]

---

## Sequence Summary

| Email | Day | Subject | Goal | CTA |
|---|---|---|---|---|
| 1 | 0 | [subject] | [goal] | [CTA text] |
| 2 | 1 | [subject] | [goal] | [CTA text] |
| ... | ... | ... | ... | ... |
```

## Subject Line Rules

- Under 50 characters (mobile truncation)
- Personalisation token in first 3 words when possible
- Question OR number OR curiosity gap — not all three
- Never ALL CAPS, never more than 1 emoji
- A/B test: always provide 2 variants per email
- British English spelling for UK audiences

## Copy Rules

- One idea per email. One CTA per email.
- First sentence = hook (not "Hi [Name], I hope you're doing well")
- Short paragraphs (1-3 sentences max)
- Write at 6th-8th grade reading level
- Match brand voice guide if provided
- British English for all UK-facing sites
- Include a P.S. line in every email — it's the second most-read element after the subject line
- Never use "unsubscribe" threats as urgency tactics

## StaticForms Integration Note

Sites currently collect emails via StaticForms but have no automated sending. When generating campaigns:
- Structure output so it can be copy-pasted into any ESP (Mailchimp, ConvertKit, Brevo)
- Include plain-text versions alongside HTML suggestions
- Note any personalisation tokens used (e.g., `{{first_name}}`) so they can be mapped in the ESP
