# Phone runbook: running and monitoring the portfolio without a laptop

Everything below works from a phone browser plus Telegram. No laptop, no VPS.
This replaces the old Hermes-on-VPS operating model, whose failure mode was
silence: crons died or misbehaved and nothing told you. The design rule here
is the opposite: every job either reports, or its absence is itself the alarm.

## The three ways work runs

| Layer | What | How it runs | Where results land |
|-------|------|-------------|--------------------|
| Data | `hermes.yml` GSC/GA4/Bing pull | daily 04:30 UTC + manual | `hermes-snapshots` branch |
| Watchdog | `portfolio-status.yml` | daily 07:05 UTC + manual | `portfolio-status` branch `STATUS.md` + Telegram digest |
| Model work | `ux-audit.yml` (guardrail report, optional fix PRs) and the Claude cloud Routine `portfolio-ux-sweep` | manual dispatch / fire the Routine | PRs on site repos, run summaries, Claude push+email notification |

## How you know something is running (and when it finishes)

1. **Trigger from the phone:** github.com > sunnyp81/sunnyp81 > Actions >
   pick the workflow > Run workflow. The run appears immediately with a live
   log; the page works fine on mobile.
2. **While it runs:** the Actions tab shows a yellow dot. Open the run to
   watch step logs stream.
3. **When it finishes:** green tick or red cross in the Actions tab. On
   failure of any hermes/data job you get a Telegram message within a minute.
   GitHub also emails you when a scheduled workflow fails.
4. **Claude Routine runs:** firing `portfolio-ux-sweep` (from the Routines
   area on claude.ai, phone app included) starts a fresh Claude session; it
   sends a push notification and an email when the run completes. The session
   transcript is openable from the notification.

## The heartbeat rule (read this once, remember it forever)

The Telegram **daily digest arrives every morning (~07:06 UTC), even when
everything is healthy**. That is deliberate:

- Digest says all OK: all good.
- Digest says STALE or lists failures: something needs a look; the message
  links to `STATUS.md`.
- **No digest at all: the monitor itself is down.** That is the one state a
  monitor cannot report, so the absence of the morning message is the alarm.
  Open the Actions tab and look at `portfolio-status`.

## Dead-man guarantees

| Failure | How you find out | Within |
|---------|------------------|--------|
| Data pull crashes | Telegram failure alert + red run | ~1 min |
| Data pull silently stops being scheduled | Digest flags `STALE` (>26h since last success) | next morning |
| Guardrail regressions creep into a site repo | Digest blocker counts rise; per-PR CI check blocks the merge | next morning / at PR time |
| Watchdog itself dies | Morning digest does not arrive | next morning |
| Claude Routine run fails or finishes | Push + email from claude.ai | at completion |

## One-time setup (phone, ~5 minutes)

Add these repo secrets at
github.com/sunnyp81/sunnyp81/settings/secrets/actions (same flow as
`hermes/deploy/PHONE_SETUP.md`):

- `TELEGRAM_BOT_TOKEN`: the @SunnyClaw123_Bot token (already stored in the
  redlighttherapy-expert repo secrets; copy it across, never into git).
- `TELEGRAM_CHAT_ID`: `5934727651`.
- `PORTFOLIO_PAT`: fine-grained PAT, contents read on all site repos (lets the
  watchdog sweep private repos; add contents:write + pull_requests:write only
  when you enable fix PRs in `ux-audit.yml`).
- `ANTHROPIC_API_KEY`: only needed for the `ux-audit.yml` fix-PR job.
- `CODEX_AUTH_JSON`: only needed for the Codex lane in `ux-audit.yml`. Uses
  your ChatGPT subscription, not metered API billing: run `codex login` once
  on any machine, then paste the contents of `~/.codex/auth.json` into this
  secret. Re-mint it if the lane ever starts failing auth. (`OPENAI_API_KEY`
  works as a fallback if you ever prefer API billing.)

Missing secrets degrade politely: without Telegram secrets the digest prints
to the run log; without the PAT the sweep marks private repos "no access".

## Standing rules (unchanged)

- Branches only; Sunny merges. Nothing auto-merges, ever.
- The guardrail (`hermes/guardrail/`) is the hard floor in CI.
- Model-written changes follow `hermes/ARCHITECTURE.md`: propose, verify
  against real sources with a different model, guardrail, human merge.
- No em/en dashes in content. British English on .co.uk sites.
