---
name: Master Builds Sheet
description: All web builds with hosting platform, account, deploy commands, API keys, and credentials
type: reference
originSessionId: b08af4a2-2ba1-485c-bfbd-fca3c09fe9a5
---
# Master Builds Sheet

> Quick-access reference for all web projects â€” platform, account, deploy method, credentials.

---

## CLOUDFLARE PAGES

| Site | CF Account Email | CF Account ID | Project Name | Repo | Local Path | Status | Deploy |
|------|-----------------|--------------|--------------|------|------------|--------|--------|
| mobileautomechanic.uk | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | mobileautomechanic-uk | sunnyp81/mobileautomechanic-uk (private) | `C:\Users\sunny\Desktop\mobileautomechanic-uk\` | LIVE scaffold â€” Phase 1 content next | **GitHub auto-deploy (main branch)** |
| postcode.page | sunnypat81@gmail.com | â€” | postcode-page | postcode.page (local) | `G:\My Drive\SEO\postcode-page\` | LIVE | Wrangler CLI |
| catchment.school | sunnypat81@gmail.com | â€” | catchment-school | sunnyp81/catchment-school (private) | `C:/Users/sunny/projects/catchment-school` | LIVE â€” 27,783 pages | **GitHub auto-deploy** |
| punchfoods.com | sunnypat81@gmail.com | â€” | â€” | sunnyp81/punchfoods (private) | â€” | LIVE â€” 29 chains | Wrangler CLI |
| deadhangs.com | fiedss47hh637@gmail.com | `d2373b6986cd74e0f99d4927b57e8d46` | deadhangs-com | â€” | `G:/My Drive/archive/deadhangs_site` | LIVE | Wrangler CLI |
| calculator.place | calculator.place@gmail.com | `eb99db98fa1c13f8065b381bd324af54` | calculator-place | calculator-place (private) | `C:/Users/sunny/projects/calculator.place` | LIVE (shell) | Wrangler CLI |
| wagearea.com | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | wagearea-com | sunnyp81/wagearea-com (private) | `C:/Users/sunny/Desktop/wagearea-com` | LIVE â€” Phase 1 (83 pages) | Wrangler CLI |
| radon.tips | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | radon-tips | sunnyp81/radon-tips (private) | `C:/Users/sunny/projects/radon-tips` | LIVE â€” 2,359 pages | Wrangler CLI |
| aifor.fitness | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | aifor-fitness | sunnyp81/aifor-fitness (private) | `C:/Users/sunny/projects/aifor-fitness` | LIVE â€” 180 pages | Wrangler CLI |
| text.taxi | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | text-taxi | sunnyp81/text-taxi (private) | `C:/Users/sunny/projects/text-taxi` | Deployed (e97d8665) | Wrangler CLI |
| salarycareer.com | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | salarycareer | sunnyp81/salarycareer (private) | `C:/Users/sunny/Desktop/careerdata-site` | LIVE â€” 2,653 pages | Wrangler CLI |
| agenticai.associates | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | agenticai-associates | sunnyp81/agenticai-associates (public) | `C:/Users/sunny/Desktop/agenticai-associates` | LIVE â€” 76 pages | Wrangler CLI |
| selflandlord.com | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | selflandlord | sunnyp81/selflandlord (private) | `C:/Users/sunny/projects/selflandlord` | LIVE â€” Astro + CF Pages Functions, Brevo email | Wrangler CLI |

### Cloudflare API Tokens

| Account | Email | Account ID | Global API Key |
|---------|-------|------------|----------------|
| Main (sunnypat81) | sunnypat81@gmail.com | `aba0a6722a4510842ca473315a8ba13e` | `[REDACTED-CF-GLOBAL-KEY]` |
| calculator.place | calculator.place@gmail.com | `eb99db98fa1c13f8065b381bd324af54` | â€” |
| deadhangs | fiedss47hh637@gmail.com | `d2373b6986cd74e0f99d4927b57e8d46` | â€” |

| Site | API Token |
|------|-----------|
| deadhangs.com | `[REDACTED-CF-TOKEN]` |
| calculator.place | `[REDACTED-CF-TOKEN]` |
| sunnypat81 programmatic sites (Pages Write + Read) | `[REDACTED-CF-TOKEN]` |

### GitHub Personal Access Token (sunnyp81 account)

| Token | Scope | Use |
|-------|-------|-----|
| `[REDACTED-GITHUB-PAT]` | repo + workflow (read/write) | Clone/push private repos incl. workflows |

Usage: `git clone https://[REDACTED-GITHUB-PAT]@github.com/sunnyp81/REPO.git`

### Cloudflare Deploy Commands

```bash
# radon.tips
cd "C:/Users/sunny/projects/radon-tips"
npm run build && git add -p && git commit -m "message" && git push
npx wrangler pages deploy dist --project-name radon-tips --commit-dirty=true

# postcode.page
npx wrangler pages deploy dist --project-name postcode-page
# (uses sunnypat81@gmail.com account)

# catchment.school
# Auto-deploys via GitHub push to sunnyp81/catchment-school

# deadhangs.com (FULL SEQUENCE)
cd "G:/My Drive/archive/deadhangs_site"
CLOUDFLARE_API_TOKEN=[REDACTED-CF-TOKEN] CLOUDFLARE_ACCOUNT_ID=d2373b6986cd74e0f99d4927b57e8d46 npx wrangler pages deploy . --project-name deadhangs-com --commit-dirty=true

# calculator.place (FULL SEQUENCE)
# NOTE: Live site uses calculator-place project in SUNNYPAT81 account (not calculator.place@gmail.com account)
# DNS zone: 20cf7e8dc6d5bbfc6d3b317bbed4b2c7 (sunnypat81 account), CNAME â†’ calculator-place-eg3.pages.dev
# GitHub Actions (deploy.yml) now auto-deploys on push to main â€” secrets CF_API_TOKEN + CF_ACCOUNT_ID set correctly
# Manual deploy only needed if GitHub Actions fails:
cd "C:/Users/sunny/projects/calculator.place"
npm run build && git add -p && git commit -m "message" && git push
CLOUDFLARE_API_TOKEN=[REDACTED-CF-TOKEN] CLOUDFLARE_ACCOUNT_ID=aba0a6722a4510842ca473315a8ba13e WRANGLER_CACHE_DIR=/tmp/wrangler-sunnypat npx wrangler pages deploy dist --project-name calculator-place --commit-dirty=true
```

> **Note:** GitHub push auto-deploys calculator.place (GH Actions fixed Apr 10). deadhangs still needs manual wrangler after push.

# IMPORTANT: Wrangler account cache fix (sunnypat81 account)
# The wrangler-account.json at ~/node_modules/.cache/wrangler/ caches the WRONG account (deadhangs).
# Always use WRANGLER_CACHE_DIR to bypass it:
#
# Standard deploy command for ALL sunnypat81 programmatic sites:
# CLOUDFLARE_API_TOKEN=[REDACTED-CF-TOKEN] WRANGLER_CACHE_DIR=/tmp/wrangler-cache npx wrangler pages deploy dist --project-name <name> --commit-dirty=true

---

## VERCEL

**Account email:** `sunnypatel.co.uk@gmail.com`
**Git author email must match** or Vercel blocks deployment.

| Site | Domain | Repo | Local Path | Status | Deploy |
|------|--------|------|------------|--------|--------|
| sunnypatel.co.uk | sunnypatel.co.uk | sunnypatel-nextjs (public) | `C:\Users\sunny\Desktop\sunnypatel-nextjs\` | Built, not deployed | git push â†’ npx vercel --prod |
| seo.associates | seo.associates | seo-associates (private) | `C:\Users\sunny\Desktop\seo-associates\` | LIVE | git push â†’ npx vercel --prod |
| reportbolt.com | reportbolt.com | reportbolt (private) | `C:\Users\sunny\Desktop\reportbolt\` | Not deployed | git push â†’ npx vercel --prod |
| ownedwork | ownedwork.com | â€” | `C:\Users\sunny\Desktop\ownedwork` | Unknown | git push â†’ npx vercel --prod |
| signforge | signforge.org | â€” | Unknown | Unknown | git push â†’ npx vercel --prod |
| stackswitch.co | stackswitch.co | sunnyp81/stackswitch.co (private) | `C:\Users\sunny\projects\stackswitch.co` | Unknown | git push â†’ npx vercel --prod |
| thetutor.link (app) | thetutor.link | sunnyp81/tutor-next (private) | â€” | LIVE â€” auto-deploys | GitHub push to master |
| blog.thetutor.link | blog.thetutor.link | tutor-blog (not yet created) | `C:\Users\sunny\Desktop\tutor-blog\` | NOT deployed | gh repo create â†’ git push â†’ npx vercel --prod |

### Vercel Deploy Command (all projects)
```bash
cd <project-path>
git push
npx vercel --prod
# Wait for: "Aliased: https://domain.com"
# Errors: npx vercel inspect <deployment-url> --logs
```

### DNS â€” thetutor.link
- A record â†’ `76.76.21.21`
- www CNAME â†’ `cname.vercel-dns.com`
- Need to switch Hostinger nameservers to `ns1/ns2.vercel-dns.com`

---

## HOSTINGER VPS â€” thetutor.link App

| Item | Value |
|------|-------|
| IP | `141.136.36.136` |
| SSH user | root |
| SSH password | `[REDACTED-SSH-PASSWORD]` |
| API URL | `https://app.thetutor.link:8000` |
| MongoDB | `mongosh tutor` (local, no auth) |
| PM2 processes | tutor-client (80/443), tutor-server (8000), tutor-admin (8080) |
| Server cwd | `/root/tutor/server/` (dotenv requirement) |

### PM2 Fix Command
```bash
pm2 delete tutor-server && cd /root/tutor/server && pm2 start index.js --name tutor-server && pm2 save
```

---

## WORDPRESS SITES

### thetutor.link (WordPress Blog)
| Item | Value |
|------|-------|
| Base URL | `https://thetutor.link/wp-json/wp/v2` |
| Auth | `Buffer.from('Kelly:[REDACTED-WP-APP-PASSWORD]').toString('base64')` |
| SEO plugin | Slim SEO (`meta.slim_seo.title`, `.description`, `.noindex`) |
| Featured image ID | 2373 |
| Homepage ID | 2256 |

---

## API KEYS & CREDENTIALS

### Google / GCP
| Service | Key / Credential | Location |
|---------|-----------------|----------|
| GSC MCP token | OAuth token | `C:\Users\sunny\.gsc-mcp\token.json` |
| Sheets API token | OAuth token | `C:\Users\sunny\.gsc-mcp\sheets_token.json` |
| Sheets client secrets | OAuth creds | `C:\Users\sunny\.gsc-mcp\sheets_client_secrets.json` |
| GCP project (SEO tools) | `sunny-seo-tools` | â€” |
| GCP project (indexing) | `claudeindex` | SA key: `C:\Users\sunny\Downloads\claudeindex-6b5681c013d4.json` |
| GCP project (GA4 MCP) | `ga4-mcp-488300` | ADC: `C:\Users\sunny\AppData\Roaming\gcloud\application_default_credentials.json` |
| GCP indexing script | `C:\Users\sunny\submit-index.py` | â€” |

### Bing Webmaster Tools
| Item | Value |
|------|-------|
| API Key | `[REDACTED-BING-KEY]` |
| MCP server | `G:\My Drive\_SHARED\mcp-servers\bing\mcp_server_bwt` |

### Brevo (Email Marketing â€” SelfLandlord)
| Item | Value |
|------|-------|
| Account email | hello@selflandlord.com |
| API Key | `[REDACTED-BREVO-KEY]` |
| Contact list | "SelfLandlord Subscribers" (ID: 3) |
| Templates | Email 1-5 created (IDs 2-6) â€” 14-day welcome sequence |
| Plan | Free (300 emails/day) |

### Mailshake (Cold Outreach)
| Item | Value |
|------|-------|
| API Key | `[REDACTED-MAILSHAKE-KEY]` |
| Campaign ID | `1506609` |
| Sender email | hello@sunnypatel.co.uk |
| Email copy | `C:\Users\sunny\Desktop\sunnypatel-nextjs\cold-email-campaign.md` |
| Prospect CSV | `C:\Users\sunny\Desktop\prospects.csv` |

### Amazon Associates
| Site | Tag | Market |
|------|-----|--------|
| mugscafe.org | `mugscafeuk-21` | UK (`amazon.co.uk/dp/ASIN?tag=mugscafeuk-21`) |
| mugscafe.org | `mugacafeus-20` | US (`amazon.com/dp/ASIN?tag=mugacafeus-20`) |

---

## DOMAIN EXPIRY DATES

| Domain | Expires |
|--------|---------|
| seo.associates | May 8, 2026 |
| calculator.place | May 11, 2026 |
| aifor.* | Aug 29, 2026 |
| redlighttherapy.tech/.skin | Sep 2, 2026 |

---

## STACKS AT A GLANCE

| Site | Stack |
|------|-------|
| calculator.place | Astro 5 + Preact islands + Tailwind v4 |
| stackswitch.co | Astro 5 + Tailwind |
| seo.associates | Next.js 16 + Tailwind v4 (83 static pages) |
| ClearNote.app | Next.js 16 + React 19 + Tailwind v4 + Tiptap + Dexie + Gemini |
| reportbolt.com | Next.js + Neon DB |
| thetutor.link (app) | Next.js (tutor-next) â†’ Vercel |
| catchment.school | Static (Cloudflare Pages) |
| deadhangs.com | Static HTML |
| punchfoods.com | Static (Cloudflare Pages) |

---

## MONETIZATION MODELS

| Site | Model | Target |
|------|-------|--------|
| calculator.place | AdSense display ads | Â£50-100/mo |
| ClearNote.app | LemonSqueezy â€” Â£25 one-time Pro | Â£500/mo (20 sales) |
| seo.associates | Lead gen / client magnet | Via SunnyPatel.co.uk |
| catchment.school | AdSense (pending) | TBD |
| punchfoods.com | AdSense (pending) | TBD |
| thetutor.link | Platform commission / subscription | Growing (+600%) |

---

## AUTOMATION / AGENT STACK (Apr 26 2026)

Architectural roles (no duplication â€” each tool owns a layer):

| Layer | Tool | Host | Job |
|-------|------|------|-----|
| Routing (no-LLM) | **Pabbly Connect** | Cloud (lifetime) | Webhook pipelines, lead routing, digest aggregation, IndexNow batches |
| MCP gateway | **Activepieces** (CE, MIT) | Oracle 132.145.23.216 (self-hosted Docker) | 280+ pieces auto-exposed as MCP tools to Claude Code |
| Autonomous reasoning | **Hermes Agent** (MIT) | Oracle 132.145.23.216 | Always-on scheduled agent, self-improving memory |
| Inference | **Ollama + Qwen 2.5 32B** | Oracle 132.145.23.216 | Local LLM for Hermes (zero API cost) |
| Email broadcast | **Listmonk** | Oracle (planned) | Self-hosted lists + sequences |

### Pabbly Connect

| Field | Value |
|-------|-------|
| Account | sunnypat81@gmail.com |
| Tier | Lifetime ($349 one-time) |
| API key | `[REDACTED-PABBLY-KEY]` |
| Primary integration mode | Webhooks (free, no key needed) |
| API key purpose | Programmatic flow management (list/create/update/trigger workflows from code) |
| Dashboard | https://connect.pabbly.com/dashboard |

### Activepieces (planned)

| Field | Value |
|-------|-------|
| Edition | Community (MIT, free, self-hosted) |
| Cloud plan limitation | API access not on current cloud plan â€” bypassed by self-hosting |
| Deploy | `git clone activepieces/activepieces && docker compose up -d` on Oracle |
| MCP exposure | Every connected piece auto-exposed as MCP server to Claude Code |
| Status | NOT YET DEPLOYED â€” requires Oracle setup first |

### Hermes Agent (planned)

| Field | Value |
|-------|-------|
| License | MIT |
| Provider | Custom OpenAI-compatible endpoint â†’ local Ollama at `http://localhost:11434/v1` |
| Recommended model | Qwen 2.5 32B Instruct (â‰¥64k ctx required) |
| Install | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` |
| Status | NOT YET DEPLOYED â€” requires Oracle setup first |

### Lifetime data-layer SaaS

| Tool | Job | Dashboard |
|------|-----|-----------|
| Jepto | GA4/GSC anomaly alerts | https://app.jepto.com |
| Hexowatch | Visual + content change detection | https://hexowatch.com/login |
| Hexometer | 24/7 site health + uptime | https://hexometer.com/login |
| Hexomate | Scheduled browser automation / scraping | https://hexomate.com/login |

