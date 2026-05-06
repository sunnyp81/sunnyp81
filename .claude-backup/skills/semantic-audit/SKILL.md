---
name: semantic-audit
description: Audit content against Koray's micro-semantic standards and algorithmic authorship rules. Use when reviewing content for compliance with semantic SEO methodology.
user-invocable: true
allowed-tools: Read
argument-hint: "[file-path]"
version: 1.0.0
---

# Semantic Content Audit

Audit content against Koray's micro-semantic standards with zero tolerance for non-compliance.

## Arguments

- `file` (optional): Path to content file to audit
- If no file provided, expects content to be pasted

---

## Audit Process

### 1. Read Content
Read file or accept pasted content.

### 2. Core Compliance Checks

#### A. Sentence Structure Analysis
Count by type: imperative (`Plan X`), specification (`X ranges from Y to Z`), benefit (`This helps you X`), other.
**Target:** 80-90% approved patterns. Report counts + percentages per type.

#### B. Start-With-Answer Rule
Count sentences starting with answer/subject/action vs preamble.
**Target:** 95%+ start with answer.
Failures: "It's important to remember..." / "When it comes to X..."

#### C. Comma Rule
Count: no commas, commas in enumerations/ranges only, commas in clauses.
**Target:** 95%+ compliant (no commas or enumeration-only).

#### D. LLM Fluff Detection
Prohibited (zero tolerance): "delve/delving", "unlock", "embark", "seamless/seamlessly", "elevate", "it's worth noting", "it's important", "when it comes to", "in today's", "the key to"

#### E. Contextual Hierarchy
Verify: one H1 only, H2s in logical order, H3s nested under H2s, no heading jumps.

#### F. Entity & Relevance
Central entity in H1, content stays focused on entity-attribute-context, no context dilution.

### 3. Advanced Semantic Dimensions

#### G. Contextual Flow (KB-14)
- First heading connects to last heading thematically
- Each H2 transitions smoothly to next (shared terms/concepts)
- No jarring topic jumps. Anchor segments between sections.
- Report: straight vector maintained, anchor segments found, topic jumps detected.

#### H. Contextual Coverage (KB-14)
- Word count per H2 section. Heaviest section = macro context.
- Flag sections >30% of total (dilution risk) or <5% tied to query interpretations (weakness risk).

#### I. Heading Vector Validation (KB-13, KB-12)
- Title tag and H1 comply. Every heading focuses on DIFFERENT information.
- Similar ideas grouped. Headings with other entities link to them.
- Subordinate content uses right format (lists/tables/definitions).

#### J. Internal Link Quality (KB-11, KB-12)
- No links in first paragraph of any section
- Max 1 link per heading section, at least one heading apart
- Top 10 headings: NO internal links unless competitors do same + strong lexical relation
- Anchor text matches target seed query, not used >3 times for different targets
- Supplementary content has MORE links than main content
- Cautious/Intelligent Surfer compliance

#### K. Macro/Micro Semantics (KB-10)
- N-gram consistency with site patterns. Context terms match query context.
- First words of paragraphs answer questions (not rhetoric without information).
- No paragraphs linking out without giving an answer first.
- Macro context (title + H1) reflected throughout document.

#### L. Discourse Integration (KB-4)
- Mutual words between consecutive paragraphs (anchor segments)
- Sentence-to-sentence contextual connection. 3+ examples per section.
- Image qualification: preceding/following paragraph qualifies images.

#### M. Question-Answer Pairing (KB-13)
- Each heading's subordinate text answers directly. First sentence matches heading structure.
- No delayed answers. Boolean questions answered yes/no before expansion.

#### N. Information Redundancy (KB-7)
- Cross-section facts consistent, no contradictions.
- Key intro propositions reflected in body. Supplementary aligns with main content.

#### O. Ranking Signal Dilution (KB-8)
- No cannibalization with other site pages for same canonical query.
- Distinctive search intent. Best format on most relevant page, not in supplementary.

---

## 4. Compliance Report Template

```markdown
# SEMANTIC CONTENT AUDIT REPORT

**Content**: [title/filename]
**Date**: [date]
**Word Count**: [X words]

## OVERALL SCORE: [X/100]

### Core Checks
- Sentence Structures: [X%] (Target: 80%+)
- Start-With-Answer: [X%] (Target: 95%+)
- Comma Rule: [X%] (Target: 95%+)
- LLM Fluff: [X] occurrences (Target: 0)
- Heading Hierarchy: [PASS/FAIL]
- Entity Clarity: [PASS/FAIL]

### Advanced Dimensions
- Contextual Flow: [PASS/FAIL]
- Contextual Coverage: [PASS/FAIL]
- Heading Vectors: [PASS/FAIL]
- Internal Link Quality: [PASS/FAIL]
- Macro/Micro Semantics: [PASS/FAIL]
- Discourse Integration: [PASS/FAIL]
- Question-Answer Pairing: [PASS/FAIL]
- Information Redundancy: [PASS/FAIL]
- Ranking Signal Dilution: [PASS/FAIL]

## VERDICT: APPROVED / NEEDS REVISION

---

## DETAILED FINDINGS

[Full breakdown per dimension — list specific sentences/issues]

## REQUIRED FIXES

**Priority 1 (Must Fix):**
1. [Specific fix with line reference]

**Priority 2 (Should Fix):**
1. [Specific fix]

**Priority 3 (Nice to Have):**
1. [Suggestion]

## FEEDBACK FOR REVISION

**Line [X]**: Current: "[sentence]"
**Issue**: [What's wrong]
**Fix**: "[corrected sentence]"

## NEXT STEPS

**If APPROVED**: Ready for meta tag generation and publication
**If NEEDS REVISION**: Return to Writing Agent with fixes above
**Iteration**: [v1/v2/v3] — if v3 fails, recreate Writing Agent with refined instructions
```

---

## Scoring System

| Score | Rating | Action |
|---|---|---|
| 90-100 | Excellent | Minor tweaks only |
| 80-89 | Good | Few revisions needed |
| 70-79 | Fair | Multiple issues, needs revision |
| <70 | Poor | Major rewrite required |

## Auto-Fail Conditions

- >10 LLM fluff words
- <80% start-with-answer or comma compliance
- Major heading hierarchy issues
- Significant context dilution
- Broken contextual flow (topic jumps between consecutive H2s)
- Links in first paragraph of any section
- Contradictory information between sections
- Cannibalization with another known page on same site

---

## Tone

Be ruthless with quality, specific with feedback. This is quality control, not creative writing class.

Good: `Line 47: "When it comes to budget planning, it's important to consider your total costs" → "Plan your budget including total costs"`

Bad: `"The writing could be more concise and direct"`
