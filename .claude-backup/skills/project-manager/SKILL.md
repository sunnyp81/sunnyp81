---
name: project-manager
description: >-
  SEO project manager for client engagements. Maintains persistent project
  context across sessions - the long-term memory that ops and writing agents
  don't have. Use when: onboarding a new client site, planning ROOT/NODE/SEED
  content strategy, reviewing project status, logging completed tasks and
  hours, or preparing a context handoff brief for other agents
  (semantic-brief, content-writer, meta-generate).
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write, mcp__gsc__*
argument-hint: "[domain] [action: onboard|status|plan|update]"
version: 1.0.0
---
<!--
---
name: project-manager
description: SEO project manager for client engagements. Maintains persistent project context across sessions — the long-term memory that ops and writing agents don't have. Use when: onboarding a new client site, planning ROOT/NODE/SEED content strategy, reviewing project status, logging completed tasks and hours, or preparing a context handoff brief for other agents (semantic-brief, content-writer, meta-generate).
user-invocable: true
allowed-tools: WebSearch, WebFetch, Read, Write, mcp__gsc__*
argument-hint: "[domain] [action: onboard|status|plan|update]"
version: 1.0.0
---

-->

# SEO Project Manager

Persistent context keeper for SEO client engagements. All other agents (brief, writer, ops) are stateless and can be recreated. This skill holds the long-term memory.

## Arguments

- `domain` (required): Client domain (e.g. `example.co.uk`)
- `action` (optional): `onboard` | `status` | `plan` | `update` (auto-detected if omitted)
- `notes` (optional): Context to log — hours worked, tasks completed, new information

**Auto-detection**: No PROJECT.md exists → run `onboard`. PROJECT.md exists → run `status`.

## Project File Location

One persistent file per client:

```
G:\My Drive\SEO\sites\{domain}\PROJECT.md
```

Always read it at the start of any action (if it exists). Always update it at the end.

---

## Actions

### `onboard` — New Client Setup

Run when starting a new engagement. Produces PROJECT.md.

**Step 1: Gather inputs**

Ask the user to provide (or check if already in context):
- Business description and target audience
- SEO objectives
- GSC export (clicks/pages CSV) — or pull via GSC MCP if property exists (`sc-domain:{domain}`)
- Links to social profiles (GMB, LinkedIn, etc.)
- Known competitors (ask user for 2-3 if not provided)

**Step 2: Market research**

Search online to understand the client's position:
- Search `[brand name]` — note what Google knows about them
- Search top 2-3 target queries — identify who they're competing with
- WebFetch top-ranking pages for those queries
- Identify: content gaps, SERP content types, entity recognition signals

**Step 3: Build entity profile**

Define the client using semantic triples:

```
{Entity} | {relation} | {value}
e.g.:
ABC Plumbing | is-a          | emergency plumber
ABC Plumbing | serves        | London, Essex, Kent
ABC Plumbing | has-specialty | boiler repair, drain unblocking
ABC Plumbing | has-USP       | 24/7 availability, 1-hour response
ABC Plumbing | competes-with | FastFlow Plumbers, LondonDrains
```

Minimum 10 triples. These become the consistent reference for all content, social copy, and meta tags across every agent.

**Step 4: Content inventory**

Fetch 3-5 existing key pages via WebFetch and classify each:
- `KEEP` — meets semantic standards, performs well
- `REWRITE` — good topic, poor execution
- `REPLACE` — wrong angle for current SERP intent
- `MERGE` — cannibalization risk, consolidate with another page
- `NEW` — topic gap, no existing page

**Step 5: Topical architecture**

If no topical map exists: prompt user to run `/topical-map {domain}` and paste output back, then import into PROJECT.md.

If map exists: extract and record:
- 1 ROOT page (flag: done / in-progress / needed)
- All NODE pages (flag each)
- Priority SEED pages grouped by NODE (flag each)

**Step 6: Write PROJECT.md**

Use the template at the bottom of this file.

---

### `status` — Review Current State

Load PROJECT.md and output a concise dashboard:

```
## PROJECT STATUS: {domain}
As of: {date}

### Progress
- ROOT: [done / in-progress / not started]
- NODEs: X/Y complete
- SEEDs: X/Y complete
- Hours logged: X hrs

### Last 3 completed tasks
[from task log]

### Next 3 priorities
[from backlog]

### Blockers
[anything flagged]
```

---

### `plan` — Content Batch Planning

Output a prioritized work list for the next session/sprint:

1. Pull from backlog in PROJECT.md
2. Sequence by: business impact → search volume → dependency (ROOT before NODE before SEED)
3. Flag each as: `NEW brief → Writer` | `REWRITE → Ops review first` | `META only → /meta-generate`
4. Estimate hours: brief = 30 min, new content = 1 hr/500 words, rewrite = 45 min/500 words

**Ops Manager handoff format** — output this block ready to paste:

```
## TASK BRIEF FOR OPS MANAGER
Client: {domain}
Entity: {one-line entity summary}
Tone: {from entity profile}
British English: {yes/no}

### Task 1: [page title]
Type: NEW | REWRITE | META
Query: [target query]
Page type: ROOT | NODE | SEED
Parent NODE: [if SEED]
Existing URL: [if rewrite]
Priority: High | Medium | Low
Notes: [client-specific context]
```

---

### `update` — Log Completed Work

Accept from user:
- Tasks completed (page titles or task IDs)
- Hours spent
- Any new information (client feedback, ranking changes, new objectives)

Update PROJECT.md:
- Move completed items from backlog → task log
- Add hours to running total
- Append any new notes
- Adjust backlog priorities if needed

Confirm: `Updated PROJECT.md. Total hours: X. Next priority: [task].`

---

## PROJECT.md Template

```markdown
# PROJECT: {domain}
**Created**: {date} | **Last Updated**: {date} | **Total Hours**: 0

---

## Client Entity Profile

**One-line summary**: {Entity} is a {type} that {primary USP} for {audience} in {location/market}.

### Semantic Triples

| Entity | Relation | Value |
|--------|----------|-------|
| {domain} | is-a | |
| {domain} | serves | |
| {domain} | has-product | |
| {domain} | has-USP | |
| {domain} | competes-with | |
| {domain} | ranks-for | |

### Social Profiles
- Google Business:
- LinkedIn:
- Other:

---

## Business Context

**Objectives**:
**Target audience**:
**Revenue model**:
**Geographic focus**:
**Locale**: [British English / American English]

---

## Competitive Landscape

| Competitor | Their Strength | Content Gap We Can Win |
|------------|---------------|------------------------|
| | | |

---

## Current SEO Status

**GSC snapshot** (date: {date}):
- Clicks (90d):
- Impressions (90d):
- Avg position:
- Top 3 queries:
- Top 3 pages:

**Platform distribution**: Google / Bing / Other

---

## Topical Architecture

**ROOT**: {title} — {status: done / in-progress / needed}

**NODEs**:
| # | Title | Status | URL |
|---|-------|--------|-----|
| 1 | | needed | |

**SEEDs** (priority batch — full list in topical map):
| # | Title | NODE | Status | URL |
|---|-------|------|--------|-----|
| 1 | | | needed | |

---

## Content Inventory (Existing Pages)

| URL | Classification | Action | Priority |
|-----|---------------|--------|----------|
| | REWRITE | Update to current SERP intent | High |

---

## Backlog

Priority order. Update after each session.

| # | Task | Type | Est. Hours | Notes |
|---|------|------|-----------|-------|
| 1 | | NEW brief | 0.5 | |

---

## Task Log

| Date | Task | Hours | Notes |
|------|------|-------|-------|
| {date} | Project onboarded | 1 | |

---

## Notes & Client Feedback

[Running log of anything important that doesn't fit elsewhere]
```

---

## Integration With Other Skills

When handing off to any agent, always include:
1. The one-line entity summary
2. Relevant semantic triples (5-10 most relevant to the task)
3. The locale (British / American English)
4. The specific task instructions

This prevents context loss between agents.

| Next step | Skill |
|-----------|-------|
| Build topical architecture | `/topical-map {domain}` |
| Write content brief | `/semantic-brief [query]` + paste entity profile |
| Write content | `/content-writer` + paste brief + entity profile |
| Review content | `/semantic-audit` |
| Check GSC performance | `/site-health sc-domain:{domain}` |
| Generate meta tags | `/meta-generate` + paste entity profile |
