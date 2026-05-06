# Paperclip Weekly Scan Protocol

Goal: every scan returns **one real, novel use case** mapped to Sunny's actual stack (44-site SEO portfolio, MerchByAmazon, lead-gen funnels, Claude Code + Codex agents, Cloudflare Pages / Vercel / WordPress sites). No empty reports.

## Sunny's stack signals (use these as the relevance filter)
- SEO at scale (programmatic SEO, GSC monitoring, content decay, CTR rewrites)
- Affiliate / Amazon / ad revenue (Ezoic, AdSense, Mediavine, AWIN)
- Inbound-lead funnels (sunnypatel.co.uk, AAA Inbound Leads Paperclip company)
- Multi-site portfolio ops (44 sites, daily triage)
- Self-hosted automation (Oracle box, Activepieces, Listmonk planned)
- Recipe / niche / directory sites (shecookssheeats, calculator.place, fixerror.dev, towrating.net, claimwatt.com)

## Scan steps (in order)

1. **WebSearch** these queries, last 7 days:
   - `"paperclipai" OR "paperclip.ing"` (catch-all)
   - `paperclip claude code site:reddit.com`
   - `paperclip claude code site:twitter.com OR site:x.com`
   - `paperclip ai agent site:news.ycombinator.com`
   - `paperclip claude code tutorial youtube`
   - `paperclip orchestration agent` (general)

2. **WebFetch**:
   - `https://paperclip.ing/llms.txt` (check for new doc sections vs last scan)
   - `https://github.com/paperclipai/paperclip/releases.atom` (new releases)
   - `https://github.com/paperclipai/paperclip/discussions` (new discussions)

3. **Dedupe** against `usecases-log.md` by URL.

4. **Score & pick ONE** — the single highest-relevance use case for Sunny's stack. Scoring:
   - +3 if it maps to SEO/portfolio/lead-gen
   - +2 if it shows a novel adapter/pattern not already in SKILL.md
   - +1 if it's by a credible operator (not vibes)
   - +1 if implementable in <1 day with existing AAA Inbound Leads infra
   - Pick highest. Ties → newest.

5. **If nothing scored ≥3**, broaden: search general "AI agent orchestration use case last week" and adapt one to Paperclip. Never report "nothing found." Always synthesize a real, applicable use case — even if it requires translating a generic agent pattern into a Paperclip company shape.

6. **Write entry** to `usecases-log.md` (prepend after the `---` line):
   ```
   ## YYYY-MM-DD
   **Use case:** <one sentence — what this Paperclip company does>
   **Source:** <url>
   **Applicability:** <2 sentences — which of Sunny's sites/streams this fits, est £ impact>
   **Implementation sketch:** <3-5 bullets — adapter type, agents, heartbeat, instructions file, est setup time>
   **Novel pattern?** <yes/no — if yes, also patch SKILL.md>
   ```

7. **If `Novel pattern? yes`**, edit `C:\Users\sunny\.claude\skills\paperclip\SKILL.md` to add the pattern under "Common use cases" or wherever it fits. Keep additions tight (1–3 lines).

8. **Email summary** to 2012.infinite@gmail.com via Brevo / configured sender — subject `Paperclip weekly: <use case headline>`, body = the new log entry. Always send (every scan = 1 use case = 1 email).

## Hard rules

- Never write speculative/hypothetical use cases without a real source URL. If no source exists, translate a generic agent pattern but cite the original (e.g. "adapted from <url>").
- Skip use cases already in `SKILL.md` "Common use cases" section.
- Stay under 500 tokens per log entry.
- If WebSearch returns 0 hits across all queries (rare), do step 5 and explicitly note `Source: synthesized from <generic agent pattern url>`.
