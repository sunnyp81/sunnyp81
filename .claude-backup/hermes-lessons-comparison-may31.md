---
name: Hermes Reddit Lessons — Comparison vs Actual Setup
description: Maps the 10 "controlled Hermes Agent workflow" lessons from Reddit against Sunny's live Hermes/Claude/VPS stack. Gap analysis + proposals (not auto-applied).
type: analysis
date: 2026-05-31
---
# Hermes Reddit Lessons vs Sunny's Actual Stack

Source: Reddit thread "Lessons learned so far building a controlled Hermes Agent workflow" (10 lessons).
Compared against: this `.claude` config (CLAUDE.md, MEMORY.md, master-builds.md, 50 skills, MCP config) + the Hermes VPS ops described across the topic files.

Verdict in one line: **the stack already implements ~7 of the 10 lessons, sometimes better than the post. The gaps are all in the same place — broad authority granted before reliability was proven, and one monolithic memory file doing five jobs.**

Format per lesson: what the post says → what you already do → gap/risk → proposal. Proposals are NOT applied; they're for review (per Lesson 4).

---

## 1. Boring reliability before expanded authority

- **Post:** start with one workflow, make it boring, then expand.
- **You do:** 3-loop verification gate on all 70 loop sites, per-site rules, auto-revert on fail (`hermes-3loop-verification-may17`). Cooldowns (5d). 15-turn caps.
- **Gap — this is the weakest area.** Authority was scaled to 70 sites + enrichment crons before stability was proven on one. Direct evidence in your own logs:
  - **shecookssheeats: enrichment cron caused a SECOND traffic collapse** (5-6k→1.5k impr/day, pos 13→24+). MEMORY backlog item 12 + `hermes-guardrails-may24`. The autonomous edit loop actively damaged a live revenue site.
  - **Hermes promoted T4→T1 on multiple sites in a single session** (redlighttherapy.expert May 26, theseshbars May 25) — authority expansion faster than results came back.
- **Proposal:** adopt the post's framing explicitly — a site earns autonomy tier by *demonstrated* stable results (e.g. N cycles, no regression, GSC trend flat-or-up), not by being onboarded. Make T1 promotion gated on a metric, not a session decision. The shecooks incident is the case study for why.

## 2. One main operator, specialized agents only when justified

- **Post:** one coordinator; sub-agents only for a real reason (domain/model/tools/memory/permission/access boundary).
- **You do:** main Claude operator + Hermes (autonomous) + a fleet of Paperclip "companies"/agents: AAA-Sales, Tutor-CEO, Tutor-CMO, Lead-CEO, Lead-Citation, ClaudeWorker, ClaudeReviewer, sp-citation-displacement, keyword-shipper drafter, job-search routine...
- **Gap:** this is drifting toward the "profile sprawl" the post warns against. Several agents are draft-only single-purpose routines that could be skills/crons under one operator rather than standing "companies." `paperclip-50-use-cases` plans up to 50 — that's a sprawl roadmap.
- **Each agent does mostly clear the post's bar** (different model tier / access boundary / cadence), so it's not wrong — but there's no register of *why each one earns its place*. Proposal: a one-line justification column per agent (which of the 6 criteria justifies it). Kill any that fail all 6. `agent-core` (May 24) is the right home for this register.

## 3. Checklist Manifest instead of giant repeated chat checklists

- **Post:** external manifest file per project; chat shows only a compact progress summary.
- **You do:** `MEMORY.md` is your manifest — action queue, per-site status, "next check" dates. Plus per-project topic files (`project_*.md`).
- **Gap:** `MEMORY.md` is **382 lines and doing five jobs at once** (revenue dashboard + action queue + job search + per-site log + topic-file index). It is exactly the "giant checklist" the post says to avoid, just moved out of chat. It's also the file the session-start protocol says to read *first* every time — so it's loaded in full constantly.
- **Proposal:** split it. Keep `MEMORY.md` as a thin index + top-5 action queue (the compact summary). Move per-site status into per-site manifest files (you already have the topic files — make them the source of truth and have MEMORY link, not duplicate). This matches the post's "compact summary in chat, durable detail in files" exactly, and cuts per-session context load.

## 4. Proposal free, authority controlled, execution logged

- **Post:** agent proposes freely; human approves exact change; agent applies only that; logs it.
- **You do:** **this is your strongest match — arguably ahead of the post.** `agent-core` has 4 hard CONSTRAINTS (no self-modify / no self-validate / no blind-ingest / no silent-overwrite). Structured action records, snapshot cron to Drive, `/approve` + TTL approval tokens, mobile-safety gating (`hermes-mobile-safety-may27`). Shadow mode (proposals only) used on carehome.page.
- **Gap:** small — the shecooks enrichment cron ran *executing* edits, not proposing them, which is how it caused harm. The constraints exist but weren't applied to the enrichment loop.
- **Proposal:** extend the "propose → approve → log" gate to content-enrichment actions on live revenue sites, not just governance/self-modification. The 4 CONSTRAINTS protect Hermes from editing itself; they don't yet protect your sites from Hermes.

## 5. Keep SOUL.md / AGENTS.md / memory / skills / project files separate

- **Post:** identity vs rules vs durable facts vs procedures vs work records — keep distinct or it drifts.
- **You do:** mostly separated already. `SOUL.md` exists (wired into shecooks + Telegram), `AGENTS.md` per Paperclip company, `MEMORY.md` for facts, 50 skills (audited down from 60, `skills-audit-may2`), `project_*.md` work logs.
- **Gap:** (a) `CLAUDE.md` blends three layers — identity ("Who I Am"), rules (revenue/deploy/security), and reference (key paths). (b) `MEMORY.md` blends durable facts with live work records (see Lesson 3). The separation is good at the file-name level but leaky at the content level.
- **Proposal:** move the path/reference tables out of `CLAUDE.md` into a reference file; keep `CLAUDE.md` to identity + standing rules only. This is low-risk and improves the exact drift the post flags.

## 6. Time awareness

- **Post:** long workflows need a real time anchor — date, tz, last checkpoint, idle time, stale "tonight/tomorrow."
- **You do:** heavy date use — "next check June X" everywhere, domain expiry table, cooldown windows, dated topic files, scheduled triggers in UTC.
- **Gap:** plenty of timestamps, no *staleness handling*. MEMORY is full of dated checkpoints ("Monitor GSC June 6", "recheck May 11-15") with nothing that flags them as due/overdue. The figment-discipline rule (no approvals 08:00-18:00 M-F UK) is the one real time-aware guard.
- **Proposal:** a "due/overdue" pass — anything with a "next check" date older than today surfaces in the compact summary. Cheap to add to the snapshot cron; turns a pile of dead dates into an action list.

## 7. Checkpointed autonomy, not unlimited freedom

- **Post:** work to the next approved checkpoint, update manifest, report, continue only if next step is pre-authorized and in scope.
- **You do:** strong — 15-turn caps, 1-site-per-heartbeat, 2-consecutive-fails before "down" alert, auto-revert, evening-executor 600s timeout flagged as highest risk (`hermes-guardrails-may24`).
- **Gap:** the guardrails are mostly *resource* limits (turns/time/sites), not *outcome* checkpoints. shecooks again: it stayed within turn caps and still degraded the site over days because nothing checkpointed "did the last batch help or hurt?"
- **Proposal:** add an outcome checkpoint to the loop — before continuing a multi-cycle action on a site, check the metric the last cycle was supposed to move. If flat/down N cycles, stop and report instead of continuing. This is the post's "continue only if authorized AND in scope" applied to results, not just steps.

## 8. Cheap models as workers, strong model as boss

- **Post:** strongest model = operator/governance/final review; cheap cloud = workers/bulk; local = private/offline.
- **You do:** **textbook match.** Haiku for job-search/classification/bulk, Sonnet for drafts, Opus for final drafts + drafter role, `claude_local` = £0 marginal, Hermes on local Qwen 2.5 32B for zero-cost reasoning. Morning-ops uses a Claude→Haiku chain.
- **Gap:** none material. One watch item: Hermes' autonomous edits run on *local Qwen*, i.e. your cheapest model has write access to live sites — which is the opposite of "cheap models don't make the big decisions." The shecooks damage was a cheap model executing unreviewed.
- **Proposal:** keep Qwen for classification/proposal generation; route the *decision to ship to a live revenue site* through a stronger model or a human gate. Aligns the model tiering with the authority tiering.

## 9. Dashboard worth watching, CLI is the reliable path

- **Post:** dashboard is promising; CLI stays primary for serious work.
- **You do:** **exact match.** Built `hermes.aifor.tech:8443` dashboard (May 17) but operate via CLI / PowerShell / Telegram. Dashboard is read-only status; control is CLI.
- **Gap:** none. This is already your posture.

## 10. Build like it matters next year

- **Post:** controlled growth, clear authority levels, compact checkpoints, durable files, human approval for major changes, no silent self-mod, no sprawl.
- **You do:** snapshot cron, secret redaction in shared memory, `leak-scan` skill, `.gitignore` standardised across 57 repos, master-builds secrets shown as `[REDACTED]` in this repo.
- **Gap:** the durability is real; the "controlled growth / no sprawl" half is where the misses cluster (Lessons 1, 2, 3). The infrastructure to do it right exists (agent-core, guardrails, verification gate) — it's just not consistently *gating* expansion.

---

## Net assessment

**Already ahead of the post:** governance constraints (4), model tiering (8), dashboard-vs-CLI (9), durable files/secret hygiene (10).

**The three real gaps, all related:**
1. **Authority before reliability** (Lessons 1, 7) — sites/crons got write access to live revenue before stable results were proven. Cost: shecookssheeats second collapse.
2. **Monolithic memory** (Lessons 3, 5) — `MEMORY.md` is the "giant checklist" moved to a file; it does 5 jobs and is read in full every session.
3. **Authority not tied to model tier or outcome** (Lessons 2, 8) — cheapest model (local Qwen) can ship to live sites; agents proliferate without a per-agent justification.

**Single highest-leverage change (proposal):** apply the existing `agent-core` "propose → approve → log" gate to *content edits on live revenue sites*, not just to Hermes editing itself. That one move directly prevents a repeat of the shecooks incident and is the post's Lessons 1, 4, and 7 in a single change. Everything else (splitting MEMORY, the agent justification register, the staleness pass) is cleanup, not risk reduction.

*Nothing here has been applied. Pick the items you want and I'll draft the exact changes for approval.*
