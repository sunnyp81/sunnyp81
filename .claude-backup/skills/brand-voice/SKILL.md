---
name: brand-voice
description: Enforce brand voice and style guide across content. Score compliance, flag violations, and output corrected versions.
user-invocable: true
allowed-tools: Read, Write
argument-hint: "[content file] [style guide file]"
version: 1.0.0
---

# Brand Voice Enforcer

Score content against a brand style guide. Flag violations, suggest corrections, ensure consistency.

**Note:** This skill focuses on TEXT compliance (tone, vocabulary, style). For visual identity (logos, colours, typography, imagery), use `/brand` instead.

## Process Steps

1. **Load style guide:** Read the brand style guide file. If none provided, infer voice from the brand's existing published content (read 3-5 pages to establish baseline).
2. **Load content:** Read the content file or text to be audited.
3. **Analyse dimensions:** Score each of the 5 dimensions below independently.
4. **Flag violations:** Identify every specific violation with line reference, the offending phrase, and the applicable guide rule.
5. **Calculate overall score:** Weighted average across dimensions (see table).
6. **Generate corrected version:** Rewrite the content with all violations fixed, preserving the original structure and meaning.
7. **Output report:** Use the output template below.

## Scoring Dimensions

| Dimension | Weight | What to Check |
|---|---|---|
| **Tone** | 25% | Formal/casual/technical — matches guide? Consistent throughout? |
| **Vocabulary** | 25% | Approved terms used? Prohibited terms absent? Industry jargon appropriate? |
| **Sentence style** | 20% | Length, complexity, active/passive matches guide? Varied rhythm? |
| **Reading level** | 15% | Grade level matches target audience? Flesch-Kincaid within range? |
| **Formatting** | 15% | Heading style, list usage, paragraph length per guide? Consistent capitalisation? |

## Scoring Rubric (per dimension, 0-100)

| Score | Meaning |
|---|---|
| 90-100 | Fully compliant. No violations. Reads as if written by brand team. |
| 70-89 | Minor violations. 1-3 small deviations that don't undermine brand feel. |
| 50-69 | Moderate violations. Noticeable tone drift or vocabulary issues. Needs editing. |
| 30-49 | Significant violations. Content feels off-brand. Major rewrite needed. |
| 0-29 | Non-compliant. Wrong tone, wrong vocabulary, wrong audience level entirely. |

## Common Violations

- **Tone drift**: Casual content for a professional brand (or vice versa)
- **Jargon overuse**: Technical terms where guide specifies plain language
- **Prohibited phrases**: Brand-specific blacklist words/claims
- **Inconsistent terminology**: Using different terms for the same concept across pages
- **Regulatory flags**: Unsubstantiated claims, missing disclaimers
- **American vs British English**: Using "optimize" when brand is UK-facing (should be "optimise")
- **Passive voice overuse**: When guide specifies active, direct voice
- **Exclamation marks**: Overuse in professional/technical brands

## Output Template

```markdown
# Brand Voice Audit Report

**Content:** [file name or description]
**Style Guide:** [guide name or "Inferred from published content"]
**Date:** [YYYY-MM-DD]

## Overall Score: [X/100]

| Dimension | Score | Weight | Weighted |
|---|---|---|---|
| Tone | [X]/100 | 25% | [X] |
| Vocabulary | [X]/100 | 25% | [X] |
| Sentence Style | [X]/100 | 20% | [X] |
| Reading Level | [X]/100 | 15% | [X] |
| Formatting | [X]/100 | 15% | [X] |

## Violations Found: [X]

| # | Line | Violation | Rule | Fix |
|---|---|---|---|---|
| 1 | [line #] | "[offending phrase]" | [guide rule] | "[corrected phrase]" |
| 2 | [line #] | "[offending phrase]" | [guide rule] | "[corrected phrase]" |

## Tone Analysis
- **Detected:** [Formal/Casual/Technical/Conversational]
- **Target:** [from guide]
- **Match:** [Yes/No — explanation if no]

## Reading Level
- **Detected:** Grade [X] (Flesch-Kincaid)
- **Target:** Grade [Y]
- **Match:** [Yes/No]

## Corrected Version
[Full corrected text with all violations resolved]

## Summary
[2-3 sentences: what's working, what needs attention, priority fix]
```

## Key Rules

- Style guide is law. Do not "improve" beyond what the guide specifies.
- Flag but don't auto-fix regulatory/legal claims — escalate to human.
- When no style guide is provided, infer from the brand's existing published content.
- For UK-facing sites in the portfolio, British English is mandatory unless the style guide explicitly states otherwise.
- This skill audits text only. For visual brand compliance, use `/brand`.
- Always provide the corrected version — don't just list problems without solutions.
- Preserve the original content's meaning and structure when correcting. Fix voice, not substance.
