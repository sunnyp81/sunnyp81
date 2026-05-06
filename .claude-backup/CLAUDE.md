# Sunny Patel — Global Claude Preferences

## Who I Am
Solo operator: SEO consultant + indie dev. Running a 44-site SEO portfolio, MBA side projects, and one retained client (Hummingbird). Target: £2,000/mo by Dec 2026.

## Communication Style
- **Terse.** One sentence per update. No trailing "here's what I did" summaries — I can read the diff.
- **No emojis** unless I ask.
- **No multi-paragraph docstrings or comment blocks.** One short line max if needed.
- When referencing code, include `file_path:line_number`.
- For exploratory questions, give a 2-3 sentence recommendation + the main tradeoff. Don't implement until I agree.

## Platform
- Windows 11, PowerShell 5.1 — use PowerShell syntax (`$env:VAR`, backtick continuation, no `&&` chaining).
- Git Bash / Bash tool available for POSIX scripts.
- Shell CWD resets to `G:\` between PowerShell calls — use absolute paths or chain into one call.

## Revenue Rules
- Every action needs a clear £ path. Ship over plan.
- Fix existing sites before building new ones.
- Content must pass `/semantic-audit` before publish.
- Validate with Ahrefs + GSC data first; don't guess traffic.

## Deploy Rules
- **ALL projects deploy via GitHub** — no direct uploads to Cloudflare or Vercel.
- Vercel deploy: `cd <project-path> && npx vercel --prod` — always after `git push`.
- Cloudflare Pages: connect repo in dashboard, build `npm run build`, output `dist`, NODE_VERSION=22.

## Default Tech Stack
- Static sites: **Astro 5** + **Tailwind 4**
- App/SaaS: **Next.js** (App Router) on Vercel
- Edge workers: **Cloudflare Workers** via Wrangler
- Schema: JSON-LD inline per-page (not injected globally)
- Images: Satori for OG generation

## Active Client
**Hummingbird** — content retainer via Mike.
- All deliverables go in **Google Docs**, never WP staging (Mike's hard rule).
- Tracker: Google Sheets (service account `claude-sheets@sunny-seo-tools`).
- Credentials in: `C:\Users\sunny\.claude\projects\G--\memory\reference_hummingbird_credentials.md`

## Key Paths
| Resource | Path |
|----------|------|
| SEO workspace | `G:\My Drive\SEO\` |
| Client work | `G:\My Drive\clients\` |
| TheTutorLink | `G:\My Drive\TheTutorLink\` |
| SunnyPatel.co.uk | `C:\Users\sunny\Desktop\sunnypatel-nextjs\` |
| Shared skills | `G:\My Drive\_SHARED\skills\` |
| Memory system | `C:\Users\sunny\.claude\projects\G--\memory\` |
| Master builds table | `C:\Users\sunny\.claude\projects\G--\memory\master-builds.md` |

## Memory System
Persistent memory lives in `C:\Users\sunny\.claude\projects\G--\memory\MEMORY.md`. Check it at session start for the current action queue and project state. Save new facts there — don't rely on conversation context carrying over.

## Security
- Never commit `.env`, `.credentials.json`, `*.jsonl`, API keys, or OAuth tokens.
- Scan before pushing if in doubt: `AIzaSy`, `sk-ant-`, `ghp_`, `GOCSPX-`, `1//` patterns.
- nano-banana skill: `.env` and `.config.json` contain a live Gemini key — never include in git.
