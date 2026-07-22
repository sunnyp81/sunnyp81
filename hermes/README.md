# hermes — GSC / GA4 / Bing data pullers

Daily GitHub-Actions-driven snapshots of every property across both
Google accounts (`2012.infinite@gmail.com`, `sunnypat81@gmail.com`)
plus the single Bing Webmaster account. Snapshots commit to the
`hermes-snapshots` branch as day-partitioned JSON — a growing corpus
you can point downstream agents at.

**Runs on GitHub Actions, credentials in GitHub Secrets. Setup and
manual triggers all work from a phone browser.**

## Getting started (mobile)

See [`deploy/PHONE_SETUP.md`](deploy/PHONE_SETUP.md). Five minutes end
to end, no desktop needed. Summary:

1. Seed four Google refresh tokens via OAuth Playground on your phone.
2. Paste seven secrets into
   `github.com/sunnyp81/sunnyp81/settings/secrets/actions`.
3. Trigger `.github/workflows/hermes.yml` from the Actions tab.

## Layout

```
hermes/
├── config.py                    # accounts + env-var naming
├── shared/
│   ├── google_auth.py           # env-var refresh -> service handle (cached)
│   ├── paths.py                 # day-partitioned output paths
│   └── logging.py               # JSON stdout logger
├── pullers/
│   ├── gsc_pull.py              # sitemaps + search analytics
│   ├── ga4_pull.py              # traffic/country/source/date/conversions
│   └── bing_pull.py             # page/query/crawl stats
├── data/                        # snapshot output — committed to hermes-snapshots branch
├── deploy/
│   └── PHONE_SETUP.md           # mobile-only setup guide
└── requirements.txt
```

The workflow itself lives at
[`.github/workflows/hermes.yml`](../.github/workflows/hermes.yml).

## Accounts

| key            | email                        | services  |
| -------------- | ---------------------------- | --------- |
| `2012infinite` | `2012.infinite@gmail.com`    | GSC + GA4 |
| `sunnypat81`   | `sunnypat81@gmail.com`       | GSC + GA4 |
| `bing`         | (single Bing account)        | Bing WMT  |

Bing has one API key, no per-account OAuth.

## Env-var conventions

| Var                                 | What                                          |
| ----------------------------------- | --------------------------------------------- |
| `GOOGLE_CLIENT_ID`                  | OAuth Web-app client id (shared)              |
| `GOOGLE_CLIENT_SECRET`              | OAuth Web-app client secret (shared)          |
| `GSC_REFRESH_TOKEN_2012INFINITE`    | GSC refresh token, 2012.infinite@gmail.com    |
| `GSC_REFRESH_TOKEN_SUNNYPAT81`      | GSC refresh token, sunnypat81@gmail.com       |
| `GA4_REFRESH_TOKEN_2012INFINITE`    | GA4 refresh token, 2012.infinite@gmail.com    |
| `GA4_REFRESH_TOKEN_SUNNYPAT81`      | GA4 refresh token, sunnypat81@gmail.com       |
| `BING_API_KEY`                      | Bing Webmaster Tools API key                  |

## Manual trigger from the Actions tab

- **puller**: `all`, `gsc`, `ga4`, or `bing`
- **days**: history window for GSC + GA4 (default 28)

## Output shape

```
hermes-snapshots branch:
data/
├── gsc/
│   └── 2026-07-22/
│       ├── _summary.json
│       ├── 2012infinite__sc-domain_bestvibrationplates.co.uk__sitemaps.json
│       ├── 2012infinite__sc-domain_bestvibrationplates.co.uk__searchanalytics_query.json
│       └── ...
├── ga4/2026-07-22/…
└── bing/2026-07-22/…
```

Each `_summary.json` is a top-down view — site counts, sitemap error
totals, per-site row counts — for a quick "did today's pull find
anything weird?" check.

## Design notes

- **Idempotent by day** — re-running overwrites the day's files.
- **One HttpError doesn't kill the run** — captured in the summary,
  the puller moves on to the next site/property.
- **Access-token cache** — refreshes every ~50 min so long sweeps
  don't re-auth per call.
- **Storage** — currently plain JSON committed to a git branch. Fine
  for a corpus of daily snapshots you'll query with tools/agents.
  If it gets huge, switch to Actions artifacts + a data bucket.

## Where this code lives

Staged in `sunnyp81/sunnyp81` because `sunnyp81/hermes-swarm` wasn't in
the session's scope when this was written. The GitHub Actions workflow
runs from wherever this code lives — you can either keep it here or
move it into `hermes-swarm` later (and copy `.github/workflows/hermes.yml`
too).
