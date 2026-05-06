---
name: ugc-publish
description: Deploy UGC affiliate content to WordPress via REST API. Reads credentials from wordpress-config.md, backs up existing content, publishes new content, and generates a deployment report. Run /ugc-review first.
user-invocable: true
allowed-tools: Read, Write, Bash, Glob
argument-hint: "[domain] [page-id] [content-file]"
version: 1.0.0
---

# UGC Publisher — WordPress Deployment

Deploy reviewed UGC content to a WordPress site via the REST API. Always creates a backup before overwriting.

## Arguments

- `domain` (required): WordPress site domain (e.g., bestreviews.co.uk)
- `page-id` (required): WordPress page ID to update
- `file` (required): Path to the HTML content file (must have passed `/ugc-review`)
- `status` (optional): Post status — `publish` (default) or `draft`
- `dry-run` (optional): If true, shows what would be deployed without making changes

## Prerequisites

1. Content must have passed `/ugc-review` with score ≥ 80
2. Credentials must exist in `G:\My Drive\SEO\sites\{domain}\wordpress-config.md`

---

## Deployment Process

### Step 1: Load Credentials

Read `G:\My Drive\SEO\sites\{domain}\wordpress-config.md` and extract:
- `username` — WordPress username
- `app_password` — Application password
- `affiliate_tag` — Amazon affiliate tag for this site

If `wordpress-config.md` does not exist, stop and ask the user to provide credentials.

### Step 2: Backup Existing Content

Fetch the current page before overwriting. Save to:
`G:\My Drive\SEO\sites\{domain}\backups\page-{page-id}-{YYYY-MM-DD}.json`

Use Node.js (Python not reliably available):

```javascript
const https = require('https');
const fs = require('fs');
const auth = Buffer.from(`{username}:{app_password}`).toString('base64');

const options = {
  hostname: '{domain}',
  path: `/wp-json/wp/v2/pages/{page-id}`,
  headers: { 'Authorization': `Basic ${auth}` }
};

https.get(options, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const page = JSON.parse(data);
    fs.writeFileSync('backup.json', JSON.stringify({
      id: page.id,
      title: page.title?.rendered,
      content: page.content?.rendered,
      slug: page.slug,
      backed_up_at: new Date().toISOString()
    }, null, 2));
    console.log('Backup saved:', page.slug);
  });
});
```

**Never deploy without a successful backup.** If backup fetch fails, stop and report the error.

### Step 3: Validate Content File

Read the content file and confirm:
- Contains `<table>` HTML (no markdown pipe tables)
- File is not empty
- Affiliate links match the domain's affiliate tag

### Step 4: Deploy

```javascript
const https = require('https');
const fs = require('fs');
const auth = Buffer.from(`{username}:{app_password}`).toString('base64');
const content = fs.readFileSync('{file}', 'utf8');
const payload = JSON.stringify({ content, status: '{status}' });

const req = https.request({
  hostname: '{domain}',
  path: `/wp-json/wp/v2/pages/{page-id}`,
  method: 'POST',
  headers: {
    'Authorization': `Basic ${auth}`,
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(payload)
  }
}, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const result = JSON.parse(data);
    console.log('Status:', res.statusCode);
    console.log('URL:', result.link);
  });
});
req.write(payload);
req.end();
```

### Step 5: Update Records

Append to `G:\My Drive\SEO\sites\{domain}\wordpress-config.md`:

```markdown
| {date} | {page-id} | {slug} | {review-score}/100 | ✅ Published |
```

---

## Output Report

```markdown
# UGC Deployment Report

**Date**: [date]
**Domain**: [domain]
**Page ID**: [id]
**Page URL**: [url]
**Review Score**: [X]/100

## Status: SUCCESS ✅ / FAILED ❌

### Actions Taken
- [x] Credentials loaded
- [x] Backup saved to [path]
- [x] Content validated
- [x] Deployed via REST API (HTTP 200)
- [x] wordpress-config.md updated

### Monitoring Plan
- Week 1 ([date +7]): GSC indexing, Amazon CTR baseline
- Week 2 ([date +14]): CTR vs previous content, conversion rate
- Success target: Amazon CTR > 3%, time-on-page > 2 min, bounce < 70%

### Rollback
Restore from backup: [backup path]
```

---

## Error Handling

| Error | Response |
|-------|----------|
| 401 Unauthorized | Stop. Credentials in wordpress-config.md are wrong or app password revoked. |
| 404 Not Found | Stop. Page ID does not exist on this domain. |
| Backup fetch fails | Stop. Never overwrite without backup. |
| Markdown table found in content | Stop. Run `/ugc-review` — content failed table check. |
| Network/DNS error | Stop. Check domain is accessible. |

## Dry Run Mode

If `dry-run=true`: load credentials, read file, show what WOULD be deployed (endpoint, content length, table count, affiliate link count) — make no HTTP requests.
