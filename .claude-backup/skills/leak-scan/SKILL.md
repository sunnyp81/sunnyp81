---
name: leak-scan
description: >-
  Continuously scan Sunny's stack for leaked secrets, exposed credentials,
  public-facing vulnerabilities, and config mistakes. Use BEFORE every git
  push/commit, BEFORE every public deploy, when reviewing any new repo or
  site, after onboarding any third-party integration, or when the user says
  "is this safe / leak / vuln / secret check / security". Covers: hardcoded
  API keys/tokens, .env files committed, exposed admin endpoints, public S3/CF
  buckets, GitHub repo public-vs-private mismatch, npm/pip vuln deps, exposed
  Wrangler/Vercel/Brevo/Stripe keys, robots.txt + .git directory exposure,
  JWT/OAuth misconfig, weak CORS, missing CSP/HSTS, public DB connection
  strings, SSRF-prone endpoints, unauth'd API routes.
version: 0.1.0
---

# Leak & Vulnerability Scan

Sunny's surface area is large: 44 SEO sites + 12+ active builds across Cloudflare Pages, Vercel, WordPress, GitHub repos (`sunnyp81/*`), VPS, Brevo, Stripe/LemonSqueezy, Google APIs, Bing, Pinterest, Activepieces. One leaked token = portfolio-wide blast radius.

## When to run

**Mandatory** before any of:
- `git push` to a new or public repo
- `git commit` that touches `.env`, `wrangler.toml`, `*.secrets`, `config*.js`, `*-config.md`, anything matching `*token*`/`*key*`/`*secret*`
- Connecting a new third-party integration (Brevo/Stripe/LS/MCP)
- Making a private repo public
- Onboarding a new site to the portfolio
- Deploy from a fresh local clone

**Proactive triggers** (run unprompted when these happen):
- User mentions a new API integration
- User pastes any string matching common token shapes (sk-…, ghp_…, csk_…, pk_live_…, AKIA…, eyJ…)
- User asks "is this safe / secure / production-ready / leaky"
- After running `npm install` / `pnpm install` on a new project (vuln deps)

## The 6-step scan

### 1. Repo-level secret scan
- `git log --all --full-history -- .env .env.local .env.production credentials.json *.pem *.key wordpress-config.md` — anything tracked = LEAK, must rotate + history-rewrite or treat repo as compromised.
- Grep working tree for hardcoded patterns:
  ```
  (sk-ant-|sk-proj-|ghp_|gho_|github_pat_|csk_|pk_live_|sk_live_|AIza[0-9A-Za-z\-_]{35}|AKIA[0-9A-Z]{16}|xox[baprs]-|hf_[A-Za-z0-9]{34,}|brevo|sendgrid|tokens?\s*[:=]\s*['""][A-Za-z0-9_\-]{20,}|password\s*[:=]\s*['""])
  ```
- Check `.gitignore` covers: `.env*`, `*.pem`, `*.key`, `node_modules`, `dist`, `.wrangler`, `.vercel`, `.next/cache`, `wordpress-config.md`, `master-builds.md`.
- Run `git status --ignored` — anything sensitive that's NOT ignored = risk.

### 2. Public-facing surface scan
- `https://<domain>/.git/config` (200 = full history exposed)
- `https://<domain>/.env`, `/.env.production`, `/wp-config.php.bak`, `/config.json`, `/composer.json`, `/package.json` with secrets
- `https://<domain>/admin`, `/wp-admin`, `/api/admin*` — check auth required
- `robots.txt` for accidentally listed sensitive paths
- `sitemap.xml` for unintended URLs (staging, drafts, internal)
- Check open ports if VPS: `nmap` or `curl http://<ip>:<common-port>` for 22/80/443/3000/8080/27017/6379/5432.

### 3. Cloudflare / Vercel / hosting config
- CF Pages: confirm preview deploys aren't indexed (`X-Robots-Tag: noindex` on `*.pages.dev`).
- CF Workers: check Wrangler `[vars]` aren't secrets (use `wrangler secret put` instead).
- Vercel: env vars scoped correctly (Preview ≠ Production), no `NEXT_PUBLIC_*` containing secrets.
- WordPress: `wp-config.php` not readable, `xmlrpc.php` disabled, REST `/users` not exposing emails.

### 4. Dependency vuln scan
- `npm audit --audit-level=high` (or `pnpm audit`) — fail on high/critical.
- `npx better-npm-audit audit` for nuanced view.
- Astro/Next: check `astro.config` / `next.config` for unsafe `dangerouslyAllowSVG`, wide `images.domains`, weak `headers()`.

### 5. API / endpoint hardening
- Every `/api/*` route: auth required? rate-limited? input validated?
- Workers `fetch` handlers: accept arbitrary URLs? (SSRF) — see `aiagentic-news` `/trigger` flagged Apr 27.
- CORS: not `*` for credentialed routes.
- Headers: CSP, HSTS, X-Frame-Options, Referrer-Policy.
- JWT: signed with strong secret, exp claim set, alg pinned (no `alg: none`).

### 6. Cross-stack token hygiene
- `master-builds.md` should NEVER be in a public repo. Confirm it's gitignored or in a private location.
- `wordpress-config.md`, `.claude/.env` for skill API keys — same.
- Brevo / Stripe / LS / GSC / Bing / GitHub PAT tokens: verify scope is minimum-required. GSC tokens with full Drive scope = over-privileged.
- IndexNow keys: public by design, but the verification file location matters.

## Output format

When scan finds issues, report as a prioritised table:

```
| Severity | Finding | File/URL | Fix |
|----------|---------|----------|-----|
| CRITICAL | sk-ant key in commit a1b2c3 of sunnyp81/foo | foo/src/lib.js:12 | rotate now, rewrite history, force-push |
| HIGH | .git exposed at site.com/.git/config | https://site.com/.git/config | block in CF page rules |
| MED | npm dep `xyz` has CVE-2025-... | package.json | bump to 1.2.4 |
| LOW | CSP header missing | _headers | add policy |
```

CRITICAL = rotate + assume compromised. HIGH = fix today. MED = fix this week. LOW = backlog.

## Hard rules

- **Never paste secrets back to the user in plaintext.** Mask: `sk-ant-***...***xY12`.
- **Never commit a "fix" that just removes the secret without rotating it** — git history retains it.
- If a token IS leaked: rotation order is (1) revoke old, (2) issue new, (3) update all consumers, (4) verify old fails. Don't reverse.
- Treat any repo with `master-builds.md` or `wordpress-config.md` content as **must-be-private**. Verify on github.com directly — `gh repo view --json visibility` if available, else manual check.
- Don't run destructive history rewrites without explicit user approval.

## Sunny-specific checklist

- `master-builds.md` location: `G:\My Drive\SEO\` (Drive, not git) — confirm never copied into a repo.
- `wordpress-config.md`: Drive-only.
- `.claude/.env` (skill API keys): user-level, not project, never committed.
- 44-site portfolio: spot-check 3 random sites per scan for `.git` exposure + `.env` leak.
- AAA Inbound Leads Paperclip company: token boundary between Sunny's Anthropic key + agent's outbound email creds.
- agenticai.associates `/trigger` worker endpoint flagged Apr 27 as unauth'd — verify status.

## Quick-fire one-liners

```bash
# Scan repo for known token shapes
git ls-files | xargs grep -nE '(sk-ant-|ghp_|sk_live_|AIza[A-Za-z0-9\-_]{35}|AKIA[0-9A-Z]{16})' 2>/dev/null

# Check .git exposure across portfolio (one-shot)
for d in site1.com site2.com; do curl -sI "https://$d/.git/config" | head -1; done

# npm audit, fail on high
npm audit --audit-level=high --omit=dev

# Wrangler check secrets (not vars)
wrangler secret list --name <project>
```
