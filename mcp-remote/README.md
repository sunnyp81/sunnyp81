# mcp-remote

Remote HTTP MCP servers for the SEO stack — GSC, GA4, Bing Webmaster — so
Claude Code can hit them from **anywhere**: desktop, web, mobile, GitHub
Actions. No more stdio-bound-to-Windows.

## Why

The local stdio setup (`C:\Users\sunny\.gsc-mcp\...`) works fine when
you're at the desk. It doesn't when you're on your phone, in a cloud
session, or in CI. This repo ports each server to HTTP + Fly.io so the
same URL works from every client.

## Layout

```
servers/
  bing/    Bing Webmaster Tools (API key)
  gsc/     Google Search Console (OAuth refresh token)
  ga4/     Google Analytics 4    (OAuth refresh token)
scripts/
  seed_oauth.py    one-shot browser OAuth flow, prints refresh token
DEPLOY.md          runbook — flyctl commands, secrets, verify steps
```

Each `servers/<name>/` is a self-contained Fly app: `server.py`, `auth.py`,
`Dockerfile`, `fly.toml`, `requirements.txt`. Deploy them independently.

## Deploy

See [DEPLOY.md](./DEPLOY.md). Short version:

1. Pick a shared bearer token (`MCP_API_KEY`).
2. `fly launch --no-deploy && fly secrets set … && fly deploy` in each
   `servers/*` folder.
3. Google servers need a one-time OAuth seed from your Windows box via
   `scripts/seed_oauth.py` — that gives you the refresh token.
4. Update `claude-mcp-config.json` (see
   [claude-mcp-config.example.json](./claude-mcp-config.example.json)) on
   every machine.

## Auth model

Two layers:

- **Client → this server:** bearer token in `Authorization` header,
  checked with constant-time compare against `MCP_API_KEY` env var.
- **This server → Google/Bing:** OAuth refresh token (Google) or API key
  (Bing), both stored as Fly secrets.

## Adding tools

FastMCP decorators. Add a `@mcp.tool()` in `server.py`, rebuild, deploy.
The tool becomes callable from any connected Claude Code client.

## Notes

- Fly auto-stops idle machines to save cost. First request after idle
  has a cold-start pause (~2–5s). Bump `min_machines_running = 1` in
  `fly.toml` if that's annoying.
- Ahrefs already ran as HTTP so it's not in this repo — it stays as-is.
- The old stdio configs still work locally. Once you've verified the
  remote ones, you can delete them from `claude-mcp-config.json`.
