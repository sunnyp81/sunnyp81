# Hermes — phone-only setup

Everything below is doable from a mobile browser. Chrome-desktop-site
mode helps for the GCP Console; the rest is mobile-native.

## What you'll do

1. Register **one** extra redirect URI on your GCP OAuth client (30 sec).
2. Use Google's **OAuth Playground** four times to get four refresh
   tokens — one per (service × account) pair (5 min total).
3. Paste seven secrets into GitHub (2 min).
4. Trigger the workflow. Done.

You do NOT need Python, SSH, a VPS, or a desk.

---

## 1. Add the OAuth Playground redirect URI

The Playground signs in on your behalf. Your OAuth client needs to
list its redirect URL.

- Open `https://console.cloud.google.com/apis/credentials` (Chrome →
  ⋮ → Desktop site helps).
- Pick the project whose OAuth client you use (`ga4-mcp-488300` or
  the fresh one from earlier).
- Tap your OAuth 2.0 Client ID.
- If it's **Web application** type: under **Authorized redirect URIs**
  tap **+ Add URI**, paste
  ```
  https://developers.google.com/oauthplayground
  ```
  → **Save**.
- If it's **Desktop app** type: create a new **Web application** client
  in the same project with that redirect URI. Note the new client_id +
  client_secret — the Playground needs a Web client.

## 2. Seed four refresh tokens via OAuth Playground

Do this whole flow **four times**. Once per row:

| # | Google account         | Scope                                                       | Save token as GH Secret       |
| - | ---------------------- | ----------------------------------------------------------- | ----------------------------- |
| 1 | 2012.infinite@gmail.com| `https://www.googleapis.com/auth/webmasters.readonly`       | `GSC_REFRESH_TOKEN_2012INFINITE` |
| 2 | 2012.infinite@gmail.com| `https://www.googleapis.com/auth/analytics.readonly`        | `GA4_REFRESH_TOKEN_2012INFINITE` |
| 3 | sunnypat81@gmail.com   | `https://www.googleapis.com/auth/webmasters.readonly`       | `GSC_REFRESH_TOKEN_SUNNYPAT81`   |
| 4 | sunnypat81@gmail.com   | `https://www.googleapis.com/auth/analytics.readonly`        | `GA4_REFRESH_TOKEN_SUNNYPAT81`   |

For each row:

1. Open `https://developers.google.com/oauthplayground/` on your phone.
2. Tap the ⚙️ (top right) → tick **"Use your own OAuth credentials"** →
   paste **your** OAuth Web-app **Client ID** and **Client secret** →
   **Close**.
3. In the left panel, in the "Input your own scopes" box paste the
   scope from the table (e.g. `https://www.googleapis.com/auth/webmasters.readonly`).
4. Tap **Authorize APIs**.
5. Google sign-in prompt appears — **switch to the row's target account**
   (add it if needed via Google's account switcher) → **Approve**.
6. You land back on the Playground with a green "Authorization code" box.
   Tap **Exchange authorization code for tokens**.
7. Copy the **`refresh_token`** value (starts with `1//`).
8. On another tab: `https://github.com/sunnyp81/sunnyp81/settings/secrets/actions/new`
   → Name = the value from the table's last column → paste the refresh
   token as the value → **Add secret**.

Repeat for rows 2–4. Rows 1 and 2 share account, rows 3 and 4 share
account — sign into the right one each time.

## 3. Add the shared secrets

Same GitHub Secrets page, add three more:

| Name                    | Value                                          |
| ----------------------- | ---------------------------------------------- |
| `GOOGLE_CLIENT_ID`      | the OAuth client_id you used in Playground     |
| `GOOGLE_CLIENT_SECRET`  | the OAuth client_secret you used in Playground |
| `BING_API_KEY`          | `fd0147cf4f4446f4984568ee673533e6`             |

You end up with **7 secrets** total.

## 4. Fire it manually

1. Open `https://github.com/sunnyp81/sunnyp81/actions` on your phone.
2. Pick the **hermes** workflow in the left sidebar.
3. Tap **Run workflow** → keep defaults (`puller: all`, `days: 28`) →
   **Run workflow**.
4. Watch the job. On success it commits snapshots to a new branch
   `hermes-snapshots`. Browse them at
   `https://github.com/sunnyp81/sunnyp81/tree/hermes-snapshots/hermes/data/`.

After the first success, the schedule takes over: **04:30 UTC daily**,
no clicks needed.

## Troubleshooting

- **`missing_creds` in logs** → a `*_REFRESH_TOKEN_*` secret name is
  wrong. Match the table exactly.
- **`invalid_grant`** → the refresh token was revoked or Playground gave
  you a token for the wrong account. Re-seed for that account.
- **`insufficient_scope`** → wrong scope pasted when authorizing.
  Playground caches consent; retry with the right scope in the box.
- **Workflow can't push** → repo → Settings → Actions → General →
  Workflow permissions → **Read and write permissions** → Save.
