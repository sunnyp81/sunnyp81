---
name: ai-tool-scout
description: >
  Discover, assess, and integrate the latest AI apps, wrappers, connectors, and developer tools.
  Use when the user asks to find new AI tools, evaluate a specific tool, scout what's trending in
  AI tooling, or wants to know what to add to their stack. Covers: MCP servers, Claude integrations,
  API wrappers, n8n/Zapier connectors, browser extensions, VS Code plugins, CLI tools, and SaaS
  AI products. Produces a scored shortlist with a clear "add to stack / skip / watch" verdict per tool.
version: 1.0.0
---

# AI Tool Scout

Discover the latest AI tools → score them against Sunny's live stack → output actionable add/skip verdicts.

## Sunny's Stack Context (always use to score relevance)

| Domain | Current Tools | Gaps / Wins |
|--------|--------------|-------------|
| SEO / GSC | GSC MCP, SEOgets MCP, Bing Webmaster MCP | Ranking-change alerts, bulk schema gen |
| Content | Claude Code + skills, semantic-brief skill | Auto-publish, image gen pipeline |
| Web deploy | CF Pages, Vercel, Wrangler | One-command multi-site deploy |
| Affiliate | Amazon Associates, AWIN | Auto-link insertion, price tracking |
| Analytics | GA4 MCP | Anomaly alerting |
| Email | Gmail MCP, StaticForms, Listmonk | Triggered sequences |
| CMS | WordPress REST API, Astro | Headless content sync |
| Automation | Claude Code hooks, RemoteTrigger, GH Actions | Visual workflow builder |
| Ecommerce | WooCommerce, Stripe, LemonSqueezy | Abandoned-cart, inventory alerts |
| Research | WebSearch, WebFetch | Scheduled digest |

## Phase 1 — Discover

Search these sources in parallel (use WebSearch for each):

```
sources:
  - site:producthunt.com "AI" "launch" after:2026-01-01
  - site:news.ycombinator.com "Show HN" AI tool
  - site:github.com/modelcontextprotocol/servers (MCP registry)
  - "new AI connector" OR "AI wrapper" site:dev.to OR site:hashnode.com
  - "@aitopreview" OR "new AI tool" on X (last 7 days)
  - site:theresanaiforthat.com newest
  - site:futurepedia.io newest
```

Collect 15–30 raw candidates. For each capture: name, URL, one-line description, category (MCP / API wrapper / SaaS / CLI / plugin / connector).

## Phase 2 — Score

Score each tool 1–5 on three axes. Read `references/scoring-rubric.md` for detailed criteria.

| Axis | Weight | Question |
|------|--------|----------|
| **Relevance** | 40% | Does it plug a gap or amplify a tool Sunny already uses? |
| **Leverage** | 35% | Does it save >30 min/week OR unlock a revenue stream? |
| **Friction** | 25% | Can it be wired up in <2 hours with existing stack? (invert: low friction = high score) |

**Weighted score** = (Relevance×0.4) + (Leverage×0.35) + (Friction×0.25)

Verdicts:
- **ADD NOW** — score ≥ 4.0: clear win, ship this session
- **WATCH** — score 3.0–3.9: promising but needs a trigger (e.g. once a specific site hits traffic threshold)
- **SKIP** — score < 3.0: not worth context

## Phase 3 — Output

Present results as a scored table, then expand each ADD NOW item with an integration plan.

### Output format

```
## AI Tool Scout — [date]

### ADD NOW
| Tool | Score | Category | Why it fits | Integration time |
|------|-------|----------|-------------|-----------------|
| ...  |       |          |             |                 |

### WATCH
| Tool | Score | Trigger to revisit |
|------|-------|--------------------|

### SKIP (one-line reason each)
- ToolName — reason
```

### Integration plan (per ADD NOW tool)

```
**[Tool Name]** — [URL]
- What: one sentence
- Hook into: which existing tool/site it connects to
- Setup steps: numbered, <5 steps
- Expected win: concrete (e.g. "saves 45 min/week on X", "unlocks affiliate on Y")
- Action: exact command or URL to start
```

## Phase 4 — MCP tools (special handling)

If any ADD NOW tool is an MCP server:
1. Check if it's already in `C:\Users\sunny\.claude\claude_desktop_config.json` — if yes, mark "already installed"
2. Output the exact JSON block to add under `mcpServers`
3. Note restart requirement

## Constraints

- Only tools that are **free tier, open-source, or already in Sunny's paid stack** qualify for ADD NOW unless the ROI case is explicit (e.g. saves ≥£50/mo)
- Do not recommend tools that duplicate existing MCP servers already working
- Prioritise tools that serve multiple active sites over single-site tools
- Flag any tool that requires sharing client data externally (GDPR / confidentiality risk per `feedback_never_leak_client_discovery.md`)

## Optional Flags

The user can narrow the scout by passing a focus area:
- `/ai-tool-scout mcp` — MCP servers only
- `/ai-tool-scout seo` — SEO/GSC tooling only  
- `/ai-tool-scout content` — content creation/publishing
- `/ai-tool-scout affiliate` — affiliate / ecommerce
- `/ai-tool-scout automation` — no-code automation / connectors
- `/ai-tool-scout [tool-name]` — assess a specific named tool only (skip Phase 1)
