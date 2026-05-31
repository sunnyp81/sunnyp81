---
name: Live-Site Content Approval Gate — Implementation Spec
description: The propose→approve→log gate for content-mutating actions on revenue sites. In-repo half is done in the seo-monitor-loop skill (v1.1.0). This spec covers the out-of-repo half — Hermes VPS cron, sites-registry.json, agent-core 5th CONSTRAINT — for review before applying.
type: spec
date: 2026-05-31
status: PROPOSAL — not applied to VPS/agent-core/registry
---
# Live-Site Content Approval Gate — Implementation Spec

**Goal:** no content-mutating action ships to a live revenue site without an explicit `/approve` token. Reuses primitives you already built (`/approve` TTL tokens, `mode` column, action records, 3-loop verification) — no new infra.

**Why:** shecookssheeats second collapse (May 23). The `seo-monitor-loop` playbook already said "don't touch content during Recovery/cliff" — the **Hermes VPS enrichment cron** ignored it and ran unreviewed edits during a quality dip. The gate makes that a hard mechanism, not guidance.

---

## Part A — DONE (in this repo, branch `claude/hermes-agent-lessons-UiZ4q`)

`skills/seo-monitor-loop` bumped to v1.1.0:
- New **Step 3.5 — Approval Gate** in `references/loop-steps.md` (action classes + token flow + hard blocks).
- 3 new guard-rail rows + `PROTECTED` config field in `SKILL.md`.
- Loop digraph routes `Classify state → Approval gate → (Dispatch | Queue proposal)`.

This governs RemoteTrigger / `/seo-monitor-loop` runs. It does **not** by itself change the VPS cron — Parts B–D do that.

---

## Part B — sites-registry.json (`C:\Users\sunny\.claude\projects\G--\memory\sites-registry.json`)

Add one field per site:

```json
{
  "site": "shecookssheeats.co.uk",
  "monetization": "adsense",
  "protected": true,          // NEW — gate content edits behind /approve
  "monthly_revenue_gbp": 0,
  "...": "..."
}
```

**Default rule:** `protected = true` if `monthly_revenue_gbp > 0` OR site has known organic traffic (in the "5 sites with traffic" set from session-may23). Throwaway / pre-launch / 0-traffic sites = `protected: false` — these are the boring-reliability sandboxes where content experiments are fine.

**Initial protected set (turn the gate on here first):** shecookssheeats.co.uk, waterhard.uk, bestvibrationplates.co.uk, theseshbars.com, redlighttherapy.expert, + any SEO-portfolio earner. Everything else `false` and shadow-only until it earns traffic.

---

## Part C — Hermes VPS cron (the actual fix for the shecooks incident)

The autonomous loop on the VPS (`/root/.hermes/` action runner, actions `ctr_rewrite | faq_schema | content_enrich | indexnow | internal_link`) must gate before it mutates a repo.

**Action-class map (mirror of skill Step 3.5):**
- Safe → ship as today: `faq_schema`, `indexnow`, `internal_link`, redirects, schema, noindex-thin.
- Content-mutating → gated on protected sites: `ctr_rewrite`, `content_enrich`, content refresh, new-content.

**Hook (pseudocode, drop in before the deploy step):**

```python
action_class = classify(action)                  # "safe" | "content"
site = registry[site_id]

if action_class == "content" and site["protected"]:
    if state == "recovery" or within_14d_of_cliff(site):
        log_action(site, action, status="blocked_recovery")   # hard block
        return SKIP
    token = pending_approvals.get(site_id, action)
    if not token or token.expired or token.consumed:
        tok = issue_token(site_id, action, ttl="24h")          # reuse /approve TTL tokens
        telegram_send(approval_card(site, action, diagnosis, tok))
        log_action(site, action, status="pending_approval", token=tok.id)
        return SKIP                                            # do NOT deploy
    token.consume(approver=token.approved_by, ts=now_iso())    # standing authority never granted
    log_action(site, action, status="approved", token=token.id)
# safe action, unprotected site, or freshly-consumed token → proceed to existing 3-loop verify + deploy
```

**`/approve <token>` handler** (extend the existing mobile-safety `/approve` command): mark the matching `pending_approvals` row consumed, stamp approver + ISO time, and let the next heartbeat pick it up. One token = one action = one cycle. Never a standing grant.

**`pending-approvals.json` schema** (new, in memory dir + synced):
```json
{ "id":"tok_…","site":"shecookssheeats.co.uk","action":"content_enrich",
  "pages":["/x/","/y/"],"issued":"2026-05-31T…Z","ttl_h":24,
  "consumed":false,"approved_by":null,"approved_at":null }
```

**Kill the standing enrichment cron on protected sites.** The shecooks cron that batch-enriched 222 stubs should not exist as an unattended job on a protected site — it becomes proposal-only under this gate.

---

## Part D — agent-core 5th CONSTRAINT (`G:\My Drive\_SHARED\agent-core\`)

The 4 existing constraints protect the agent from editing *itself*. Add a 5th protecting *your sites*:

> **5. No live-site content mutation without approval.** A content-mutating action (title/meta/CTR rewrite, content enrichment, refresh, or new content) targeting a site flagged `protected` may not be deployed without a redeemed, unexpired, single-use `/approve` token. Approval is per-action and never standing. Content mutation is hard-blocked while the site is in Recovery or within 14d of a traffic cliff, regardless of token.

---

## Rollout (boring-reliability order)

1. Apply Part A (done) — review the diff.
2. Add `protected` to registry (Part B), set the initial protected set only.
3. Ship Part C hook to VPS in **shadow** first: log `would_block` / `would_propose` for 7d, send the cards, but still let current behaviour run on non-protected sites. Confirm the cards are sane.
4. Flip protected sites live; kill the shecooks enrichment cron.
5. Add Part D constraint once C is proven.

**Done = ** a `content_enrich` on shecookssheeats during Recovery is hard-blocked, and any CTR rewrite on a protected site waits in `pending-approvals.json` for a one-time `/approve` token before it can deploy.
