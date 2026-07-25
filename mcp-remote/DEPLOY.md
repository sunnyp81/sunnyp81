# Deploy runbook — remote MCPs on Fly.io

Three servers, one repo. Each deploys as its own Fly app.

| Server | Fly app          | URL after deploy                       |
| ------ | ---------------- | -------------------------------------- |
| GSC    | `sunny-gsc-mcp`  | `https://sunny-gsc-mcp.fly.dev/mcp`    |
| GA4    | `sunny-ga4-mcp`  | `https://sunny-ga4-mcp.fly.dev/mcp`    |
| Bing   | `sunny-bing-mcp` | `https://sunny-bing-mcp.fly.dev/mcp`   |

Prereqs on your Windows laptop:

```powershell
# Fly CLI
iwr https://fly.io/install.ps1 -useb | iex
fly auth signup    # or: fly auth login

# Python (for the OAuth seed step only)
python -m pip install google-auth-oauthlib
```

## 1. Pick a shared bearer token

This is the token Claude Code sends to your MCPs. Generate once, reuse
for all three servers so your `claude-mcp-config.json` stays tidy.

```powershell
# any long random string; keep it out of git
$env:MCP_API_KEY = -join ((1..48) | % { [char](Get-Random -min 33 -max 126) })
$env:MCP_API_KEY   # copy this
```

## 2. Deploy Bing (easiest, no OAuth)

```powershell
cd G:\...\mcp-remote\servers\bing
fly launch --no-deploy --copy-config --name sunny-bing-mcp --region lhr
fly secrets set `
  MCP_API_KEY=$env:MCP_API_KEY `
  BING_API_KEY=$env:BING_API_KEY   # from Bing Webmaster Tools -> Settings -> API Access
fly deploy
```

Smoke test:

```powershell
curl.exe https://sunny-bing-mcp.fly.dev/health
```

## 3. Seed Google OAuth (once)

```powershell
cd G:\...\mcp-remote\scripts
# Get client_secrets.json from your existing GCP OAuth client (Desktop app type)
# https://console.cloud.google.com/apis/credentials?project=ga4-mcp-488300
python seed_oauth.py --service both --client-secrets client_secrets.json
```

Copy the three `GOOGLE_*` values it prints.

## 4. Deploy GSC

```powershell
cd G:\...\mcp-remote\servers\gsc
fly launch --no-deploy --copy-config --name sunny-gsc-mcp --region lhr
fly secrets set `
  MCP_API_KEY=$env:MCP_API_KEY `
  GOOGLE_CLIENT_ID=<from seed step> `
  GOOGLE_CLIENT_SECRET=<from seed step> `
  GOOGLE_REFRESH_TOKEN=<from seed step>
fly deploy
```

## 5. Deploy GA4

```powershell
cd G:\...\mcp-remote\servers\ga4
fly launch --no-deploy --copy-config --name sunny-ga4-mcp --region lhr
fly secrets set `
  MCP_API_KEY=$env:MCP_API_KEY `
  GOOGLE_CLIENT_ID=<same> `
  GOOGLE_CLIENT_SECRET=<same> `
  GOOGLE_REFRESH_TOKEN=<same>
fly deploy
```

## 6. Wire up Claude Code

Merge `claude-mcp-config.example.json` into `.claude/mcp/claude-mcp-config.json`
on every machine you use Claude Code from — desktop, web, mobile app,
GitHub Actions, whatever. Replace the placeholder bearer token with the
`MCP_API_KEY` you generated in step 1.

## 7. Verify

Anywhere Claude Code runs:

```
/mcp
```

You should see `gsc`, `ga4`, `bing` all connected. Then:

```
Ask GSC to list all sites and their sitemap errors.
```

## Rotating the bearer token

```powershell
$env:MCP_API_KEY = -join ((1..48) | % { [char](Get-Random -min 33 -max 126) })
fly secrets set -a sunny-gsc-mcp  MCP_API_KEY=$env:MCP_API_KEY
fly secrets set -a sunny-ga4-mcp  MCP_API_KEY=$env:MCP_API_KEY
fly secrets set -a sunny-bing-mcp MCP_API_KEY=$env:MCP_API_KEY
# Update claude-mcp-config.json on every device.
```

## Debugging

```powershell
fly logs -a sunny-gsc-mcp
fly ssh console -a sunny-gsc-mcp
fly status -a sunny-gsc-mcp
```

A cold-start pause on the first request is expected — Fly auto-stops
idle machines and boots them on demand. If that lag bothers you, set
`min_machines_running = 1` in the fly.toml.
