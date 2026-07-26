# Hermes setup — fastest path first

Google's OAuth consent screens fought back, so the plan changed:
**hermes no longer needs Google OAuth to be useful.** SEO Gets (Pro)
already aggregates GSC + GA4 for every site you've added there, and
its MCP endpoint auths with a plain API key. Bing auths with a plain
API key too.

## Path 1 — phone-only, no Google, works right now

Add **two** secrets at
`https://github.com/sunnyp81/sunnyp81/settings/secrets/actions/new`:

| Name              | Value                                                     |
| ----------------- | --------------------------------------------------------- |
| `SEOGETS_API_KEY` | `sg_mcp_uApsq1N81vGt72ecRTU7shMPZF390qdMzxC10eFU8k4FWZbNQeRXk` |
| `BING_API_KEY`    | `fd0147cf4f4446f4984568ee673533e6`                        |

(Both values are already in this repo's history — rotate them when
convenient and update the secrets.)

Then trigger the workflow:

1. Open `https://github.com/sunnyp81/sunnyp81/actions`.
2. Pick **hermes** in the sidebar → **Run workflow** → keep defaults →
   **Run workflow**.
3. On success, snapshots land on the `hermes-snapshots` branch:
   `https://github.com/sunnyp81/sunnyp81/tree/hermes-snapshots/hermes/data/`

The `all` puller runs whatever has credentials and **skips** the rest,
so the run is green with just these two secrets. The SEO Gets puller is
self-discovering: its first run also snapshots the server's tool
catalog to `data/seogets/<day>/meta__server__catalog.json`, so the
per-site pulls can be tuned after seeing what the server offers.

After the first success the schedule takes over: **04:30 UTC daily.**

## Path 2 — raw Google data, next time you're at the desk (~3 min)

Your desktop MCPs **already hold working refresh tokens** — no
Playground, no consent screens, no browser flows. Just read them off
disk and paste into GitHub Secrets.

### GSC (custom MCP)

In PowerShell:

```powershell
Get-Content C:\Users\sunny\.gsc-mcp\token.json
```

That JSON contains `client_id`, `client_secret`, and `refresh_token`.
Add them as secrets:

| Secret name                      | From token.json field |
| -------------------------------- | --------------------- |
| `GSC_CLIENT_ID`                  | `client_id`           |
| `GSC_CLIENT_SECRET`              | `client_secret`       |
| `GSC_REFRESH_TOKEN_2012INFINITE` | `refresh_token`       |

(That token belongs to whichever account the desktop GSC MCP is signed
into — almost certainly `2012.infinite@gmail.com`. If the GSC pull
lists the wrong sites, it was the other account: rename the secret to
`GSC_REFRESH_TOKEN_SUNNYPAT81`.)

### GA4 (official analytics-mcp)

The pipx-installed analytics-mcp uses Application Default Credentials:

```powershell
Get-Content $env:APPDATA\gcloud\application_default_credentials.json
```

Same shape. Add:

| Secret name                      | From the file's field |
| -------------------------------- | --------------------- |
| `GA4_CLIENT_ID`                  | `client_id`           |
| `GA4_CLIENT_SECRET`              | `client_secret`       |
| `GA4_REFRESH_TOKEN_2012INFINITE` | `refresh_token`       |

If the GA4 pull later fails with an `insufficient_scope`-style error,
that ADC grant lacks the analytics scope — use the appendix below for
GA4 only.

The workflow auto-detects these: next `all` run picks them up, no
config change needed. Per-service `GSC_CLIENT_ID`/`GA4_CLIENT_ID`
override the shared `GOOGLE_CLIENT_ID`, so it's fine that the two
tokens came from different OAuth clients.

### Second account (`sunnypat81@gmail.com`)

SEO Gets covers its sites in the meantime. To add raw pulls for it,
seed `GSC_REFRESH_TOKEN_SUNNYPAT81` / `GA4_REFRESH_TOKEN_SUNNYPAT81`
via the appendix once, from the desk, in a normal browser.

## Appendix — OAuth Playground (last resort)

Only needed for tokens you can't harvest from Path 2. Known blockers,
both fixed in the GCP console (`console.cloud.google.com`, desktop
browser strongly recommended):

- **`Error 403: access_denied` ("app is being tested")** — the OAuth
  client's consent screen is in *Testing* mode. Either add the signing
  account under **APIs & Services → OAuth consent screen → Test
  users**, or hit **PUBLISH APP** (also stops testing-mode refresh
  tokens expiring every 7 days).
- **`redirect_uri_mismatch`** — the client must be a **Web
  application** type with `https://developers.google.com/oauthplayground`
  in its Authorized redirect URIs.

Then per token: `https://developers.google.com/oauthplayground/` → ⚙️ →
*Use your own OAuth credentials* → paste client id + secret → scope
`https://www.googleapis.com/auth/webmasters.readonly` (GSC) or
`https://www.googleapis.com/auth/analytics.readonly` (GA4) →
**Authorize APIs** → sign in as the target account → **Exchange
authorization code for tokens** → copy `refresh_token` (starts `1//`)
→ save as the matching `*_REFRESH_TOKEN_*` secret. When using
Playground-minted tokens for both services, also set the shared
`GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` secrets to that client.

## Troubleshooting

- **`missing_seogets_api_key` / `missing_bing_api_key`** — secret name
  typo'd; match the tables exactly.
- **`invalid_grant`** — that refresh token was revoked or is from a
  Testing-mode consent screen past its 7-day expiry. Re-harvest or
  re-seed it.
- **Workflow can't push** — repo → Settings → Actions → General →
  Workflow permissions → **Read and write permissions** → Save.
