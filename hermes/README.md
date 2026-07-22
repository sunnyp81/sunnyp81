# hermes — GSC / GA4 / Bing data pullers

Daily cron-driven snapshots of every property across both Google
accounts (`2012.infinite@gmail.com`, `sunnypat81@gmail.com`) plus the
single Bing Webmaster account. Output lands as day-partitioned JSON
under `data/`, ready for downstream analysis, dashboards, or feeding
into the SEO agents.

> **Staging note:** these files currently live in `sunnyp81/sunnyp81`
> under `hermes/`. Move to `sunnyp81/hermes-swarm` with:
>
> ```bash
> cd hermes-swarm
> git checkout -b add-data-pullers
> cp -R ../sunnyp81/hermes/* .
> git add . && git commit -m "add gsc/ga4/bing pullers"
> git push -u origin add-data-pullers
> ```

## Layout

```
hermes/
├── config.py                    # accounts list + paths
├── shared/
│   ├── google_auth.py           # OAuth refresh -> service handle
│   ├── paths.py                 # day-partitioned output paths
│   └── logging.py               # JSON stdout logger
├── pullers/
│   ├── gsc_pull.py              # sitemaps + search analytics
│   ├── ga4_pull.py              # traffic/country/source/date/conversions
│   └── bing_pull.py             # page/query/crawl stats
├── credentials/                 # GITIGNORED — see credentials/README.md
├── data/                        # GITIGNORED — snapshot output
├── deploy/
│   ├── seed_oauth.py            # one-shot OAuth flow, per account
│   ├── hermes-crontab.txt       # cron entries
│   └── setup.sh                 # VPS bootstrap
└── requirements.txt
```

## Accounts

| key            | email                        | services  |
| -------------- | ---------------------------- | --------- |
| `2012infinite` | `2012.infinite@gmail.com`    | GSC + GA4 |
| `sunnypat81`   | `sunnypat81@gmail.com`       | GSC + GA4 |
| `bing`         | (single Bing account)        | Bing WMT  |

Bing has one API key, no per-account OAuth. Set `BING_API_KEY` in the
cron env (see `deploy/hermes-crontab.txt`).

## One-shot bootstrap

From your desktop:

```bash
cd hermes
python -m pip install -r requirements.txt

# Seed all four Google refresh tokens (one browser session each,
# picking a different Google account per run)
python deploy/seed_oauth.py --service gsc --account 2012infinite --client-secrets ~/client_secrets.json
python deploy/seed_oauth.py --service gsc --account sunnypat81   --client-secrets ~/client_secrets.json
python deploy/seed_oauth.py --service ga4 --account 2012infinite --client-secrets ~/client_secrets.json
python deploy/seed_oauth.py --service ga4 --account sunnypat81   --client-secrets ~/client_secrets.json

# Test locally
python pullers/gsc_pull.py --days 28
python pullers/ga4_pull.py --days 28
python pullers/bing_pull.py
```

Then push to the VPS:

```bash
scp -r hermes root@VPS:/root/.hermes
ssh root@VPS 'bash -s' < hermes/deploy/setup.sh
```

## Output shape

```
data/
├── gsc/
│   └── 2026-07-22/
│       ├── _summary.json
│       ├── 2012infinite__sc-domain_bestvibrationplates.co.uk__sitemaps.json
│       ├── 2012infinite__sc-domain_bestvibrationplates.co.uk__searchanalytics_query.json
│       ├── 2012infinite__sc-domain_bestvibrationplates.co.uk__searchanalytics_page.json
│       └── ...
├── ga4/
│   └── 2026-07-22/
│       └── ...
└── bing/
    └── 2026-07-22/
        └── ...
```

Each `_summary.json` is a top-down view — site counts, sitemap error
totals, per-site row counts — for quick "did today's pull find anything
weird?" checks.

## Running just one account

```bash
python pullers/gsc_pull.py --account sunnypat81
python pullers/ga4_pull.py --account 2012infinite --days 7
```

## Design notes

- **Idempotent by day.** Re-running overwrites the day's files. Cron
  hitting the same day twice is a no-op-ish.
- **One HttpError doesn't kill the run.** Per-site errors are captured
  in the summary and logged, then the puller moves on.
- **Access-token cache** in `shared/google_auth.py` refreshes every
  ~50 min so a long GA4 sweep across dozens of properties doesn't
  re-auth per call.
- **Bing has no per-account concept** — its API is keyed and returns
  every verified site on the single account.
- **Storage** is currently plain files. SQLite/DuckDB come next if
  you want cross-day joins.
