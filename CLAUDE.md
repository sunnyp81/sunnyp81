# Project Memory

This is the `sunnyp81/sunnyp81` GitHub profile repository. It stores Claude Code MCP server configuration and setup documentation.

## MCP Servers

| Server | Type | Auth | Status |
|--------|------|------|--------|
| **Ahrefs** | HTTP (remote) | OAuth (browser popup) | Active |
| **Google Search Console** | stdio (custom Python) | OAuth2 via `client_secrets_oauth.json` | Active |
| **Google Analytics 4** | stdio (pipx: `analytics-mcp`) | Google Cloud ADC | Active |
| **Bing Webmaster Tools** | stdio (custom Python) | API key (env var) | Active |

## Setup Instructions

### Google Search Console (GSC)
- **Server**: Custom Python at `G:\My Drive\_SHARED\mcp-servers\gsc\gsc_server.py`
- **Venv**: `C:\Users\sunny\.gsc-mcp\venv\Scripts\python.exe`
- **Credentials**: `C:\Users\sunny\.gsc-mcp\token.json` (OAuth2)

### Google Analytics 4 (GA4)
- **Package**: `analytics-mcp` (install via `pipx install analytics-mcp`)
- **GCP Project**: `ga4-mcp-488300`
- **Required APIs**: Google Analytics Admin API, Google Analytics Data API
- **Setup**:
  ```
  gcloud auth application-default login --scopes https://www.googleapis.com/auth/analytics.readonly,https://www.googleapis.com/auth/cloud-platform
  pipx install analytics-mcp
  ```

### Bing Webmaster Tools
- **Server**: Custom Python at `G:\My Drive\_SHARED\mcp-servers\bing\`
- **Entry point**: `mcp_server_bwt`
- **Auth**: Set `BING_WEBMASTER_API_KEY` environment variable (get key from Bing Webmaster Tools > Settings > API Access)

### Ahrefs
- **URL**: `https://api.ahrefs.com/mcp/mcp`
- **Auth**: Built-in OAuth flow (no config needed)

## Restore Instructions

1. Update `~/.claude.json` with the `mcpServers` section from `.claude/mcp/claude-mcp-config.json`
2. For GA4: Ensure `gcloud auth` is set up and `pipx` has `analytics-mcp` installed
3. For Bing: Set the `BING_WEBMASTER_API_KEY` environment variable
4. Restart Claude Code

## Important Notes

- MCP config paths are **Windows-specific** — adjust for other environments
- Never commit API keys or secrets to this repo — use environment variables
