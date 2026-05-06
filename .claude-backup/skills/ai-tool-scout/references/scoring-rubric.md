# Scoring Rubric — AI Tool Scout

## Relevance (1–5)

5 — Directly plugs a known gap in Sunny's stack (e.g. MCP server for a service already in use, affiliate auto-linker for existing sites)
4 — Amplifies an active revenue stream or deployed site
3 — Useful for a planned site/stream (backlog item)
2 — Generic AI tool with indirect benefit
1 — No clear fit with current or planned work

## Leverage (1–5)

5 — Saves >2 hrs/week OR unlocks a revenue stream estimated ≥£50/mo
4 — Saves 1–2 hrs/week OR unblocks a current bottleneck
3 — Saves 30–60 min/week or removes friction from a recurring task
2 — Nice-to-have, marginal time/money benefit
1 — Novelty only, no measurable leverage

## Friction (1–5) — INVERTED (5 = easy, 1 = hard)

5 — Zero-config: install via npm/pip or paste JSON block into claude_desktop_config.json, works in <15 min
4 — Simple API key + one config file, working in <1 hour
3 — Requires account + some wiring, working in 1–2 hours
2 — Needs custom integration, code changes, or new service account: 2–4 hours
1 — Complex setup, unclear docs, or requires infrastructure not in Sunny's stack

## Category Bonuses (add to weighted score before applying verdict thresholds)

+0.3 — MCP server that connects to a service Sunny pays for
+0.2 — Open-source with active GitHub (>100 stars, commits in last 30 days)
+0.2 — Works across multiple of Sunny's 44 portfolio sites simultaneously
-0.3 — Requires sharing client/user data with a third-party server
-0.2 — Vendor lock-in risk (proprietary format, no export)
-0.5 — Duplicate of an already-working MCP server or tool

## Worked Example

**Hypothetical: "Ahrefs MCP Server"**
- Relevance: 5 (SEO is core, Ahrefs already paid)
- Leverage: 5 (replaces manual keyword research, saves 3hr/week)
- Friction: 4 (API key + JSON block)
- Weighted: (5×0.4)+(5×0.35)+(4×0.25) = 2.0+1.75+1.0 = 4.75
- Bonus: +0.3 (paid service MCP)
- **Final: 5.05 → ADD NOW**
