# credentials/

**Gitignored.** Never commit anything here.

## Google (GSC + GA4) — one file per (account × service)

Four files, each containing a Google OAuth refresh token bundle:

- `gsc_2012infinite.json` — GSC scope, refresh token for `2012.infinite@gmail.com`
- `gsc_sunnypat81.json` — GSC scope, refresh token for `sunnypat81@gmail.com`
- `ga4_2012infinite.json` — GA4 scope, refresh token for `2012.infinite@gmail.com`
- `ga4_sunnypat81.json` — GA4 scope, refresh token for `sunnypat81@gmail.com`

Shape:

```json
{
  "client_id": "xxxx.apps.googleusercontent.com",
  "client_secret": "GOCSPX-...",
  "refresh_token": "1//..."
}
```

### How to generate

From your desktop (needs browser):

```bash
cd hermes
python deploy/seed_oauth.py \
  --service gsc \
  --account 2012infinite \
  --client-secrets /path/to/client_secrets.json

python deploy/seed_oauth.py \
  --service gsc \
  --account sunnypat81 \
  --client-secrets /path/to/client_secrets.json

# repeat for --service ga4
```

The script opens a browser, you sign into the target Google account,
approve, and it writes the JSON file into `credentials/`.

Both accounts can share the same `client_secrets.json` (same GCP OAuth
client). Just sign into a different Google account for each run.

## Bing — env var only

Bing uses a single API key across all sites. Set it in the environment
that runs the puller:

```bash
export BING_API_KEY=fd0147cf4f4446f4984568ee673533e6
```

On the VPS this belongs in `credentials/bing.env` and gets sourced by
the systemd timer / cron wrapper.
