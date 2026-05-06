# Loop Steps 1–8 — Implementation Playbook

Read this after Steps 0 / 0.3 / 0.5 have run (those live in `SKILL.md`). This file is the action-execution playbook.

## Step 1 — Pull Data (parallel)

Run simultaneously using MCP tools (prefer MCP over curl in local sessions):
- `mcp__gsc-sunnypat81__get_performance_overview` — last 14 days (use `mcp__gsc-2012infinite__*` for 2012.infinite properties)
- `mcp__gsc-sunnypat81__compare_search_periods` — 7d vs prior 7d (dimensions: page, then query)
- `mcp__gsc-sunnypat81__get_search_analytics` — 28d by date (trend line)
- `mcp__gsc-sunnypat81__check_indexing_issues`
- `mcp__bing-webmaster__get_crawl_stats`
- `mcp__bing-webmaster__get_rank_and_traffic_stats` (skip if unavailable)

In RemoteTrigger agents (no MCP access): use curl to GSC API with OAuth refresh token from `infrastructure.md`.

If any GSC call errors after one retry, mark data **partial** and flag in the log. Still diagnose with what's available — don't abort.

## Step 2 — Diagnose

Compute signals:

| Signal | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| 7d clicks vs prior 7d | ±10% | −10% to −30% | < −30% |
| 28d trend slope | flat/up | mild decay | cliff (>50% drop in <7d) |
| Avg position drift | ±2 | +2 to +8 | > +8 (worse) |
| Bing InIndex trend | growing | flat | shrinking |
| CTR on money pages | > 2% | 0.5–2% | < 0.5% |
| Top page position | < 20 | 20–35 | > 35 |

Classify **site state**:
- **Recovery** — clicks < 50% of 28d peak OR cliff detected. Priority: trust signals, schema, internal links, unique content on hubs.
- **Growth** — clicks trending up, positions 15–35. Priority: striking-distance wins, FAQ schema, new page types.
- **Maintenance** — clicks stable, top pages pos < 15. Priority: freshness, new specialism pages, backlinks.
- **Stable-no-action** — no Warning/Critical signals. Skip action. Just log + reschedule.
- **Restricted** — set by Step 0.3 (Core Update window OR portfolio cliff). Technical-only actions allowed.
- **Monetize** — traffic trending up AND site lacks ads/affiliate coverage per `sites-registry.json` `monetization` field. Overrides Growth/Maintenance priority.

**Per-template split (mandatory on programmatic sites):** group GSC page data by URL pattern (`/city/*`, `/county/*`, `/guides/*`, etc.). Classify each template separately. Target the action at the **worst-affected template**, not the site average — one template can be collapsing while others grow, and site-wide averages hide it.

## Step 3 — Select Action (one per iteration)

Pick the top-ranked action for the current state and map it to the specific skill to invoke. **Drop any action blacklisted or marked inconclusive by Step 0.5** and walk down the ranking until you hit one that has either a proven win or no prior negative result.

**Playbook lookup:** before picking, read `C:\Users\sunny\.claude\projects\G--\memory\seo-playbook.json`. Filter entries to this site's type (programmatic/blog/directory/tool) and state. If a proven-winning action exists (Δ clicks ≥ +10% over 14d on a similar site) and isn't blacklisted here, promote it to the top of the ranking. Portfolio learning > per-site learning.

### Recovery
1. Fix broken redirects / 404s in top-traffic URLs → manual edit + `/index-push`
2. Add missing schema to top-impression pages → `/schema-advanced`
3. Improve internal linking to demoted hubs → `/internal-link-mapper`
4. Unique intros/sections on templated hub pages → `/content-writer` + `/semantic-audit`
5. Noindex thin pages (< 150 words AND 0 impressions/14d) → manual robots/meta

### Growth
1. CTR rewrite striking-distance pages (pos 8–20, CTR < 0.5%) → `/ctr-rewrite` — **max 5 pages/iter, respect WEEKLY_CTR_BUDGET**
2. Add FAQ / HowTo schema → `/schema-advanced`
3. Internal links from authority pages → striking-distance pages → `/internal-link-mapper`
4. Unique intros on templated hub pages → `/content-writer` + `/semantic-audit`
5. New page type from demand gap → `/demand-map` + new generators

### Maintenance
1. Content refresh on pages > 90 days old → `/content-decay`
2. New page type from high-impression zero-click queries → `/demand-map` + `/content-calendar`
3. CWV check on top templates (LCP > 2.5s) → `/technical-seo-checker`
4. IndexNow push on recently updated pages → `/index-push`

### Monetize
1. Add Amazon affiliate / display ads / CTAs to top-impression pages → `/monetize-audit` → `/affiliate-content`
2. If crossed traffic threshold (e.g. > 3K clicks/mo), apply for AdSense / Ezoic / Mediavine → `/ad-rpm-optimizer`
3. Email capture / lead magnet on top pages → `/lead-magnet`
4. Schema for rich results (Review, Product, AggregateRating) → `/schema-advanced`

### Restricted
Technical only: redirects, sitemap, schema, IndexNow, CWV. No title/meta/content edits.

### Stable-no-action
Skip to Step 6. Log reason: *"no action — [specific stable signals]"*.

## Step 4 — Dispatch Improvement Agent

Use `Agent` with `subagent_type=general-purpose`, foreground (block until done). Brief:

```
Site:    [SITE_URL]
Repo:    [REPO_PATH]
State:   [recovery | growth | maintenance]
Action:  [chosen action]
Skill:   [exact /skill from Step 3]
Context: [paste top URLs, positions, queries driving this decision]

Guard rails:
- CTR rewrites: max 5 pages this iter; honour WEEKLY_CTR_BUDGET; never on >500-page programmatic templates
- Never overwrite existing WP pages via REST — drafts only (feedback_never_overwrite_wp)
- Deploy via git push → CF Pages wrangler (feedback_autonomous_deploy); CF token from master-builds.md
- Build must pass file-count guard before deploy
- Invoke /pre-completion-validation before reporting done (feedback_pre_completion_validation)
- Absolute ISO dates in any logs written

Execute. Commit with descriptive message. Deploy. Confirm live URLs. Report commit hash + URLs + validation score.
```

Wait for the agent's result.

## Step 5 — Deploy + Validate

Before marking deployed:
- [ ] `git push` succeeded
- [ ] Build file count within previous deploy's range (no silent page loss)
- [ ] `curl -sI` on 3 affected URLs returns 200
- [ ] No new 404s on changed URL patterns
- [ ] `/pre-completion-validation` score ≥ 85 on modified content (MANDATORY)
- [ ] **Playwright MCP visual check** (if running in local Claude Code session — skip in RemoteTrigger agents which use curl only):
  - `browser_navigate` → one affected URL
  - `browser_console_messages` → zero errors
  - `browser_take_screenshot` → confirm page renders (hero, nav, main content visible)

If any fail, revert the commit and log the failure honestly. Do not claim success.

**Auto-rollback on harm:** at the start of each iteration, check the prior iteration's action (only after attribution cooldown has elapsed, i.e. 7d+). If signal delta on that action's URL set is ≤ −20% clicks or ≥ +5 position drift vs pre-action baseline, auto-revert that commit (`git revert <hash>`), redeploy, log `reverted: [hash] — [reason]`, and blacklist the action for this site. Blacklisting alone lets harmful commits stay live for weeks; revert closes the loop.

## Step 6 — Log Iteration

Append to `C:\Users\sunny\.claude\projects\G--\memory\seo-monitor-log.md` using absolute ISO dates:

```markdown
## [SITE] — 2026-04-18 — Iteration N

State:             recovery | growth | maintenance | stable-no-action
GSC 7d clicks:     X (prior 7d: Y, ±Z%)
Avg position:      X.X (drift ±N)
Bing InIndex:      X (trend)
Action:            [one line — or "no action: [reason]"]
Skill invoked:     [/skill or "none"]
Commit:            [hash or "none"]
Files changed:     [list or "none"]
Validation score:  [X/100 or "n/a"]
Weekly CTR usage:  M/20
Next check:        2026-04-19
Prior learnings:   [blacklisted actions | proven wins | patterns spotted]
Signal delta vs last iter: clicks [±X], position [±Y], CTR [±Z]
Notes:             [anomalies, flags, MCP issues]
```

The `Signal delta vs last iter` line is what makes log review in Step 0.5 possible — future iterations read it to judge whether prior actions actually moved the needle.

Also update the site's one-line entry in `MEMORY.md` with current state + next check date.

**Playbook write:** if this iteration's action had a computed positive delta (≥ +10% clicks over 14d, cooldown elapsed), append or update an entry in `C:\Users\sunny\.claude\projects\G--\memory\seo-playbook.json`:

```json
{"site_type":"programmatic","state":"growth","action":"/ctr-rewrite","delta_clicks_pct":+18,"delta_position":-2.1,"sample_site":"carehome.page","iso":"2026-04-18"}
```

Similarly append a negative entry for ≤ −10%. This is the portfolio learning asset — read by Step 3 on future iterations for this and other sites.

## Step 7 — Portfolio Digest

Instead of one email per iteration (44 daily emails = ignored), append to a single daily digest file:

`C:\Users\sunny\.claude\projects\G--\memory\seo-digest-YYYY-MM-DD.md`

Entry format:
```
- [HH:MM] [SITE] — [state] — clicks X (±Y%), pos X.X — [action or "unchanged"] — commit [hash|none]
```

At 20:00 UTC (end-of-day ScheduleWakeup), the final iteration of the day emails the whole digest to `EMAIL` with subject `SEO portfolio digest — YYYY-MM-DD — N sites, M actions, K flags`.

**Exception — immediate email:** any iteration that triggers an escalation (see Escalation section in SKILL.md) sends its own email at once with `ESCALATE:` prefix. Don't wait for the digest — harm signals need same-day attention.

## Step 8 — Reschedule

Cadence by state:

| State | Delay | Reason |
|-------|-------|--------|
| Recovery | 24h | Fast iteration while re-establishing signals |
| Growth | 24h | Catch striking-distance wins quickly |
| Maintenance | 72h | No urgency; reduce churn |
| Stable-no-action (3+ consecutive) | 7d | Daily loop adds no value |

```
ScheduleWakeup(
  delaySeconds: [from table],
  reason:       "SEO monitor: [SITE] iter N+1 — [state]",
  prompt:       "/seo-monitor-loop [SITE_URL]"
)
```

On escalation (see SKILL.md Escalation section), do **not** reschedule — wait for Sunny.
