# AI Bot Crawl Monitoring & Tools

Verify AI bots actually crawl your site (not just allowed in robots.txt).

## Server Log Check
If you have access to server logs (CF analytics, Vercel analytics, or raw logs):
- Search for user agents: `GPTBot`, `ChatGPT-User`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`
- Note crawl frequency per bot and which pages they visit
- Flag: if a bot is allowed but never visits = content not discoverable

## Cloudflare Analytics (for CF Pages sites)
- Dashboard → Security → Bots → Filter by "Verified Bot"
- Check which AI bots are hitting your site and how often

## Bing Webmaster Tools
- Copilot relies entirely on Bing index
- Check: Site Explorer → Crawl Stats → look for BingPreview/Copilot crawls
- Many portfolio sites are NOT indexed in Bing — this is the #1 gap for AI visibility

## Manual Citation Test Protocol
For top 5 topics per site, search in:
1. ChatGPT: "What are the best [topic]?" or "[entity] [attribute]"
2. Perplexity: Same queries — check if your site appears in citations
3. Google (with AI Overview): Search main keywords, check if cited in AIO

Log results in: `G:\My Drive\SEO\ai-citations\{domain}_citation_log.md`

| Query | ChatGPT | Perplexity | Google AIO | Date |
|-------|---------|------------|------------|------|
| [query] | Cited/Not/Competitor cited | Cited/Not | Cited/Not | [date] |

## When to Use This vs `/geo-optimizer`

| Use This (`/ai-seo`) | Use `/geo-optimizer` Instead |
|---|---|
| Overall strategy and presence audit | Optimizing a specific page for AI citation |
| Third-party presence building | Rewriting content with GEO methods |
| Setting up monitoring | Applying Princeton 9 methods to content |
| New site AI readiness check | Improving existing content's citation rate |

## Monitoring Tools

Track AI citation performance:
- **Otterly AI** — monitors ChatGPT, Perplexity, Google AI Overviews
- **Peec AI** — multi-platform AI citation tracking
- **ZipTie** — Google AI Overviews, ChatGPT, Perplexity tracking
- **LLMrefs** — keyword-to-AI visibility mapping

For our portfolio: start with manual spot-checks (search key topics in ChatGPT/Perplexity), then invest in tooling when revenue justifies it.
