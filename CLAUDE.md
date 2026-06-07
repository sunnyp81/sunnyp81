# CLAUDE.md — shared memory

This file is the **central memory shared between Claude Code on the terminal and on the web.**
Both environments auto-load it from the repo root at session start. It is the only durable,
synced channel between them (the web container is ephemeral and does not see your local
`~/.claude/CLAUDE.md`), so **keep persistent context here and commit + push after updating it.**

> Maintenance rule for Claude: when you learn a durable fact, preference, or decision that
> should outlive the session, append it to the relevant section below, then commit and push.
> Keep it concise — this loads into every session's context.

## Owner
- Sunny Patel — 2012.infinite@gmail.com
- Runs a large portfolio (~100+) of niche / programmatic SEO sites.

## Repo purpose
`sunnyp81/sunnyp81` is used as a working space for SEO portfolio analysis and planning.
Primary working branch for recent work: `claude/beautiful-feynman-WAwRQ` (PR #5 → `main`).

## Active work — SEO portfolio remediation
Deliverables live in [`seo-portfolio/`](seo-portfolio/) — start at `seo-portfolio/README.md`.
Five workstreams: (1) May-crash diagnosis, (2) CTR/title sprint, (3) shecookssheeats
consolidation, (4) momentum growth plan, (5) prune dead-weight.

### Data sources (Google Search Console exports in Google Drive)
Read via the `mcp__Google_Drive__read_file_content` tool. **The tool returns markdown-escaped
text** — treat `\_` as `_` and `\#` as `#` when parsing.

| File | Drive file_id |
|------|---------------|
| organic_visibility_summary.csv | `1al1-QlBd4BtrEhXde8yHpx-X7qFIxmga` |
| organic_visibility_ctr_opportunities.csv | `1cWg715Psn2zzOlwf8A9SyRh1YI37xQEf` |
| organic_visibility_dead_pages.csv | `1XYt1j3AFQ4YChQyoZxXz-bnP5ZnNmqzR` |
| organic_visibility_decays.csv | `1nqhKPL2pMWiuMa87PBtrIrtQYlM9ZUxW` |
| ga4-growth-monetisation-scorecard-2026-05-17.csv | `1MHJMPHwE-F8chYMS2L_QB693FYGUbOVF` |

### Known facts / caveats
- Latest GSC snapshot is a 28-day window ~May 17–22 2026; captured mid-rollout of Google's
  May 2026 Core Update (May 21–Jun 2), so drop magnitudes are overstated until ~June 9.
- Live page titles cannot be fetched — all sites return HTTP 403 to bots; title rewrites are
  inferred from URL slugs.
- Lost access to Google account `sunnyshares.com@gmail.com` — some GSC properties are
  disconnected until it is reconnected.
- Cloudflare MCP is connected but **needs owner OAuth** before zone/domain inventory can be
  pulled (cross-check still pending).

## Conventions / preferences
- Be candid and evidence-based; never fabricate metrics. Quote real numbers.
- Do not create PRs unless explicitly asked.
- Commit messages: clear and descriptive.
