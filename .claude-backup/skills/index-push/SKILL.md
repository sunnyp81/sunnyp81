---
name: index-push
description: Push URLs to Google Indexing API, Bing URL Submission, and ping services for fast crawling and indexing. Supports batch submission with rate limiting.
user-invocable: true
allowed-tools: Read, Write, Bash, Agent
argument-hint: "[site URL] or [--sitemap URL] or [--urls file.txt]"
version: 1.0.0
---

# Index Push — Fast URL Submission

Submit URLs to search engines for rapid crawling and indexing. Combines Google Indexing API, Bing Webmaster Tools API, and sitemap ping services.

## Arguments

- `site` (required): Base site URL (e.g. https://selflandlord.com)
- `--sitemap` (optional): Sitemap URL to extract all URLs from
- `--urls` (optional): Path to text file with one URL per line
- `--priority` (optional): Comma-separated priority URLs to submit first
- `--bing-only` (optional): Skip Google Indexing API (useful if no service account)
- `--google-only` (optional): Skip Bing

If no `--urls` or `--sitemap` provided, auto-discovers sitemap from robots.txt or {site}/sitemap.xml.

## Google Indexing API

### Setup
- Service account key locations (check in order):
  1. Project `.env` file: `GOOGLE_INDEXING_KEY_PATH=...`
  2. Default: `C:\Users\sunny\Downloads\claudeindex-6b5681c013d4.json`
- OAuth2 scope: `https://www.googleapis.com/auth/indexing`
- Endpoint: `POST https://indexing.googleapis.com/v3/urlNotifications:publish`
- Body: `{"url": "...", "type": "URL_UPDATED"}`

### Process
1. Locate service account key (check .env first, then default path)
2. Authenticate with service account key using OAuth2
3. Submit each URL with type `URL_UPDATED`
4. Rate limit: max 200 URLs/day per property
5. **Retry logic:** On 429/5xx errors, wait 30s and retry (max 3 attempts per URL)
6. Log response status for each URL
7. Report: successful, failed (with error codes), retried, quota remaining

### Requirements
- Python with `google-auth` and `requests` packages, OR
- Node.js with `google-auth-library` and `node-fetch`
- Site must be verified in GSC with the service account added as owner/delegate

### If no service account available:
- Use GSC MCP tools instead: `mcp__gsc__submit_sitemap`
- Flag to user that manual GSC verification is needed

## Bing URL Submission

### Via MCP (preferred)
- Use `mcp__bing__submit_url_batch` for batches of up to 500 URLs
- Use `mcp__bing__submit_url` for single URLs
- Requires site to be verified in Bing Webmaster Tools

### If MCP fails (not verified)
- Flag to user for manual verification
- Offer CNAME or meta tag method

## Ping Services

Always run these regardless of API access:

```bash
curl -s "https://www.google.com/ping?sitemap={sitemap_url}"
curl -s "https://www.bing.com/ping?sitemap={sitemap_url}"
```

## Output

```markdown
# Index Push Report: {site}

## Google Indexing API
- URLs submitted: [count]
- Successful: [count]
- Failed: [count] (reasons)
- Quota remaining: [count]/200

## Bing URL Submission
- URLs submitted: [count]
- Successful: [count]
- Failed: [count] (reasons)

## Ping Services
- Google ping: [sent/failed]
- Bing ping: [sent/failed]

## URLs Not Submitted
[list any that failed with reasons]

## Next Steps
- [any manual actions needed]
```

## Rate Limits

| Service | Daily Limit | Batch Size |
|---------|-------------|------------|
| Google Indexing API | 200 URLs/day | 1 per request |
| Bing URL Submission | 10,000 URLs/day | 500 per batch |
| Ping services | No limit | 1 sitemap per request |

## When to Use

- After first deploy of a new site (`/launch-seo` calls this automatically)
- After publishing a batch of new pages
- After major content updates to existing pages
- After fixing crawl errors or removing noindex tags
- Weekly for sites actively publishing content

## Tips

- Submit your 10 most important pages first (homepage, pillar content, money pages)
- Re-submit updated pages after major content changes
- Don't submit noindex pages or redirects
- Check `mcp__bing__get_url_submission_quota` before large batches
