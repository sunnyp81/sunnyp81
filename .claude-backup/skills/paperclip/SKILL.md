---
name: paperclip
description: Set up and operate Paperclip — open-source orchestration layer that runs a "company" of AI agents (Claude Code, Codex, etc.) with heartbeats, tickets, budgets, and an org chart. Use when the user asks to install Paperclip, configure a `claude_local` adapter, wire Claude Code into a Paperclip company, set up multi-agent autonomous workflows, manage agent budgets/heartbeats, or troubleshoot Paperclip + Claude Code integrations.
version: 0.1.0
---

# Paperclip + Claude Code

Paperclip (paperclip.ing, `npx paperclipai`) is a control plane that schedules autonomous agents on heartbeats, persists session state, enforces token budgets, and routes tasks through an org chart. It does **not** replace Claude Code — it spawns the `claude` binary (or hits an HTTP agent) and drives it on a schedule.

The user's existing **AAA Inbound Leads** Paperclip company is documented in `paperclip-aaa-inbound-leads-apr30.md` — read that file first if the task is about that specific company.

## When to use this skill

- Installing Paperclip or onboarding a new company
- Configuring a `claude_local` (or `codex_local`) adapter
- Writing/structuring `instructionsFilePath`, `CLAUDE.md`, `AGENTS.md`, `.claude/agents/*.md` for agents that run under Paperclip
- Choosing models, billing mode (API key vs subscription), heartbeat cadence, budgets
- Debugging "agent never wakes / runs out of turns / loses context across heartbeats"
- Designing failover (Claude → Codex → local) via multiple adapters

## Install + onboard (canonical sequence)

```bash
# 1. Claude Code on PATH
npm install -g @anthropic-ai/claude-code
claude auth login           # subscription billing
# OR: claude auth login --console   # API-key billing

# 2. Paperclip
npx paperclipai onboard --yes
# → embedded Postgres, UI on http://localhost:3100
```

Manual: clone repo, `pnpm install && pnpm dev`.

Verify before configuring an adapter: `claude --version`, `claude auth status`, `which claude`.

## `claude_local` adapter config

Paperclip's process adapter spawns `claude` as a child. Canonical config:

```json
{
  "adapterType": "claude_local",
  "adapterConfig": {
    "command": "claude",
    "cwd": "/workspace/<project>",
    "instructionsFilePath": "/workspace/<project>/AGENTS.md",
    "model": "claude-sonnet-4-6",
    "effort": "medium",
    "maxTurnsPerRun": 50,
    "timeoutSec": 900,
    "graceSec": 15,
    "env": { "ANTHROPIC_API_KEY": "sk-ant-..." }
  }
}
```

Key fields:
- `cwd` — directory-scoped sessions; same `cwd` + saved `sessionId` resumes context across heartbeats. Don't change it casually.
- `instructionsFilePath` — system prompt for the agent. Point at `AGENTS.md` (or a file that references it).
- `model` — default to Sonnet for cost. Use Opus only for the "final draft" step, Haiku for cheap research/triage. Use the latest model IDs (Opus 4.7 `claude-opus-4-7`, Sonnet 4.6 `claude-sonnet-4-6`, Haiku 4.5 `claude-haiku-4-5-20251001`).
- `maxTurnsPerRun` — hard cap on Claude turns per heartbeat. Tune to keep heartbeats bounded.
- `extraArgs` — pass-through CLI flags (e.g. permission mode).
- `env.ANTHROPIC_API_KEY` — present = API billing. Omit = subscription billing on the local login.

**Billing rule of thumb:** subscription is cheaper for sustained dev work; API is required for headless servers / shared machines / per-agent token accounting via Anthropic Console.

## Adapter types

- **`claude_local`** — local `claude` CLI process (most common).
- **`codex_local`** — OpenAI Codex CLI; same shape, different `command`. Useful as failover when subscription tokens run out.
- **HTTP adapter** — POSTs to a remote agent gateway (OpenClaw-style); Paperclip injects a `paperclip` payload block. Use for distributed/remote agents.
- **Generic process adapter** — any CLI that reads stdin / writes stdout (e.g. Snowflake Cortex Code, custom scripts).

Mix freely — one company can have Claude engineers, a Codex backup, and a Bash ops agent.

## Instructions: AGENTS.md vs CLAUDE.md vs `.claude/agents/`

Paperclip is unopinionated; Claude Code reads:
- `CLAUDE.md` — project-level instructions (always loaded by `claude` in that cwd).
- `.claude/agents/<name>.md` — subagent definitions (model, tools, scope per agent).
- `AGENTS.md` — emerging cross-tool standard. Claude Code doesn't read it natively; reference it from `CLAUDE.md` (or symlink).

**Recommended layout for a Paperclip-driven repo:**
```
<repo>/
├── AGENTS.md              ← single source of truth, point Paperclip's instructionsFilePath here
├── CLAUDE.md              ← short, says "see AGENTS.md"
└── .claude/agents/
    ├── ceo.md
    ├── engineer.md
    └── researcher.md      ← mirror Paperclip roles 1:1
```

Each agent file: `## Role`, `## Protocol` (research/sales/dev/etc.), `## Tools`, `## Output format`. Keep tight — these are loaded every turn.

## llms.txt + MCP for self-serve docs

Paperclip publishes `https://paperclip.ing/llms.txt`. Wire it into agents via an MCP docs server (e.g. `mcpdoc`) so Claude can pull Paperclip docs on demand instead of stuffing them into `instructionsFilePath`.

## Operational patterns

- **Heartbeats** — agents wake on schedule (every 30m / 4h / 12h). Tune to task latency tolerance. Don't run dev agents every 5m — you'll burn budget on no-ops.
- **Tickets** — every task is a ticket with owner + threaded history. Auditable.
- **Budgets** — per-agent token cap. 80% = warn, 100% = auto-pause. Set these *before* unleashing autonomy.
- **Org chart** — assign Claude agents titles (CEO/CTO/Engineer/Researcher). Delegation flows along reporting lines.
- **Governance gates** — hires, strategy changes, sensitive config require board approval. Use for anything that touches prod / spends money / sends external messages.
- **Session resumption** — same `cwd` + `sessionId` continues the conversation. New `cwd` = fresh chat. Switching cwd mid-project loses context.

## Weekly use-case scan

Remote routine `paperclip-usecase-scan` (`trig_01MhsLQ1abSG1aL1sqVU9JFZ`, Mondays 09:00 UTC) emails one curated, stack-relevant Paperclip use case to 2012.infinite@gmail.com under Gmail label `paperclip-usecases`.

When the user asks **"what's new in Paperclip"** or is designing a new Paperclip company, **first query Gmail** via the Gmail MCP for `label:paperclip-usecases` (or subject `Paperclip weekly:`) — that's the live archive. Don't rely on local files for use-case history; the routine doesn't write to disk. Local `references/usecases-log.md` and `scan-protocol.md` are reference only (the protocol the routine follows).

## Common use cases

1. **Autonomous dev** — Claude as CTO/Engineer, working tickets in a repo across heartbeats. Tests + commits inline.
2. **Content/SEO/marketing org** — writer + SEO analyst + social agent on 4–12h heartbeats.
3. **Inbound leads / sales** — research agent (Haiku) drafts dossier, sales agent (Sonnet/Opus) drafts outbound email, human approves send.
4. **Failover** — primary Claude `claude_local`, secondary Codex `codex_local`, route on quota exhaustion.
5. **Data ops** — Claude + Snowflake Cortex Code via process adapters in the same org.

## Token-efficiency defaults

- One agent per role, not one-per-task.
- Haiku for research/triage drafts, Sonnet for production work, Opus only for final-draft polish on high-value output.
- `maxTurnsPerRun` low (20–50). Long heartbeats = runaway cost.
- Draft-only mode (no auto-send) until the protocol is validated on ≥5 tickets.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Agent restarts fresh every heartbeat | `cwd` changed, or `sessionId` not persisted |
| "No claude binary found" | `command` path wrong, or PATH not inherited — set absolute path |
| Auth error despite `claude auth status` OK | Paperclip running as different user; pass `ANTHROPIC_API_KEY` in `env` instead |
| Burns budget instantly | `maxTurnsPerRun` too high, heartbeat too frequent, or model = Opus by default |
| Agent ignores instructions | `instructionsFilePath` not pointing at the right file, or `CLAUDE.md` overriding it |

## Limitations

- Process adapter is local-only — distributed setups need HTTP adapters.
- Anthropic ToS: launching the real `claude` binary is fine; proxying OAuth tokens (OpenClaw-style) is not. Paperclip stays compliant by spawning the binary.
- Headless servers: avoid Chrome/browser integrations; set `chrome: false` if exposed.

## Reference: key Claude CLI commands Paperclip drives

- `claude` — interactive session in cwd
- `claude "task"` — seed initial prompt
- `claude -p "query"` — one-shot, exit
- `claude -c` / `claude -c -p` — continue most recent session in cwd
- `claude -r "<id>" "query"` — resume specific session
- `claude mcp ...` — manage MCP servers
- In-session: `/clear`, `/branch`, `/rewind`, `/schedule`, `/sandbox`

Paperclip itself doesn't send slash commands — teach Claude to use them via `AGENTS.md`/`CLAUDE.md`.
