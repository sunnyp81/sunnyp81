# SEO Portfolio Remediation — Action Pack

Analysis of a ~100-site GSC portfolio, built from the authoritative Search Console
exports (`organic_visibility_*` CSVs). Snapshot: **28-day window ~May 17–22 2026**
(cross-referenced against the Apr 3 – Jun 5 dashboard). Generated 2026-06-06.

> **Read the crash diagnosis first** — the May snapshot was captured *mid-rollout*
> of Google's May 2026 Core Update, so several "drops" are overstated and the
> earliest clean comparison window is ~June 9. Don't make irreversible content
> decisions on the drop magnitudes until then.

## The five workstreams

| # | Task | Deliverable(s) | Headline |
|---|------|----------------|----------|
| 1 | **May crash diagnosis** | [`01-crash-diagnosis.md`](01-crash-diagnosis.md) | Crash = **Google May 2026 Core Update** (May 21–Jun 2), confirmed algorithmic & bidirectional. `carehome.page` the only material loss (−531 clicks); June numbers are normal post-rollout settling. |
| 2 | **CTR / title sprint** | [`02-ctr-action-list.csv`](02-ctr-action-list.csv) · [`02-ctr-title-rewrites.md`](02-ctr-title-rewrites.md) | **≈1,964 clicks/period** of latent upside across 185 page-1 pages; top-25 rewrites = ~1,260 of it. Mostly a **SERP-feature** (AI Overview/snippet/PAA) problem, not pure titles. |
| 3 | **shecookssheeats fix** | [`03-shecooks-consolidation.md`](03-shecooks-consolidation.md) | Thin-content-at-scale + cannibalization (500 pages, 4 queries/page, pos 17). 5 dup clusters to 301; ~30+ thin pages → 1 Syns hub + 6 guides. Target ~800–1,000+ clicks/mo. |
| 4 | **Momentum growth plan** | [`04-momentum-growth-plan.md`](04-momentum-growth-plan.md) | 7 growing sites; invest next in **waterhard.uk** (page-1, brand-heavy, leaking non-brand clicks), **catchment.school** (the +110% star), **deadhangs.com** (de-risk 2-URL concentration). |
| 5 | **Prune dead-weight** | [`05-prune-decisions.csv`](05-prune-decisions.csv) · [`05-prune-summary.md`](05-prune-summary.md) | 27 weak sites: **22 CUT, 1 CONSOLIDATE, 4 KEEP-watch**. Dup property `towrating.org`/`.net`. `wagearea.com` flagged for manual-action check. |

## Recommended order of execution

1. **Stabilise & diagnose (now):** reconnect the lost `sunnyshares.com@gmail.com`
   Google account, run a manual-action check (esp. `wagearea.com`/`carehome.page`),
   URL-inspect the named dead pages. *(Task 1)*
2. **Fastest ROI (this week):** the CTR/SERP-feature sprint — titles/meta on the
   P1 list, plus FAQ/answer-block/structured-data for the SERP-feature pages.
   *(Task 2)* — overlaps with `nomadranker.com` and `waterhard.uk` in Task 4.
3. **Biggest structural fix:** shecookssheeats dedupe + consolidation. *(Task 3)*
4. **Compound the winners:** momentum content + internal-link plays. *(Task 4)*
5. **Clear the decks:** prune/redirect the T4 dead pool to free focus & renewals. *(Task 5)*

## Data provenance & caveats

- Sourced from Google Search Console exports in Google Drive; no numbers fabricated.
- Live on-page titles **could not be fetched** (every site returns HTTP 403 / bot
  protection), so target queries and title rewrites are **inferred from URL slugs**.
- Expected-impact ranges are labelled inferences derived from GSC `potential_clicks` gaps.
- Cloudflare zone verification of the full domain inventory is still pending owner auth.
