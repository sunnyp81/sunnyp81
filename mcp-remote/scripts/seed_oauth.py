"""One-shot browser OAuth flow -> refresh token.

Run this ONCE from your Windows laptop for each Google-based MCP.
The script opens a browser, asks for consent, then prints a refresh
token you paste into `fly secrets set GOOGLE_REFRESH_TOKEN=...`.

Usage:
    python seed_oauth.py --service gsc --client-secrets client_secrets.json
    python seed_oauth.py --service ga4 --client-secrets client_secrets.json

`client_secrets.json` is the "Desktop app" OAuth client JSON you
download from Google Cloud Console. Any OAuth client tied to a project
with the Search Console API + Analytics APIs enabled will work.
"""

from __future__ import annotations

import argparse
import json
import sys

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    sys.stderr.write(
        "google-auth-oauthlib not installed. Run: pip install google-auth-oauthlib\n"
    )
    sys.exit(1)


SCOPES = {
    "gsc": ["https://www.googleapis.com/auth/webmasters"],
    "ga4": ["https://www.googleapis.com/auth/analytics.readonly"],
    "both": [
        "https://www.googleapis.com/auth/webmasters",
        "https://www.googleapis.com/auth/analytics.readonly",
    ],
}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--service", choices=list(SCOPES), required=True)
    ap.add_argument(
        "--client-secrets",
        required=True,
        help="Path to Google OAuth client_secrets JSON (Desktop app type).",
    )
    ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args()

    flow = InstalledAppFlow.from_client_secrets_file(
        args.client_secrets, scopes=SCOPES[args.service]
    )
    creds = flow.run_local_server(
        port=args.port,
        access_type="offline",
        prompt="consent",
        open_browser=True,
    )

    with open(args.client_secrets, "r", encoding="utf-8") as f:
        secrets = json.load(f)
    installed = secrets.get("installed") or secrets.get("web") or {}

    print("\n" + "=" * 60)
    print(" OAuth seed complete. Set these three secrets on Fly:")
    print("=" * 60)
    print(f"GOOGLE_CLIENT_ID={installed.get('client_id')}")
    print(f"GOOGLE_CLIENT_SECRET={installed.get('client_secret')}")
    print(f"GOOGLE_REFRESH_TOKEN={creds.refresh_token}")
    print("=" * 60)
    print("\nExample flyctl:")
    app = "sunny-gsc-mcp" if args.service == "gsc" else "sunny-ga4-mcp"
    print(
        f"  fly secrets set -a {app} \\\n"
        f"    GOOGLE_CLIENT_ID={installed.get('client_id')} \\\n"
        f"    GOOGLE_CLIENT_SECRET={installed.get('client_secret')} \\\n"
        f"    GOOGLE_REFRESH_TOKEN={creds.refresh_token}"
    )


if __name__ == "__main__":
    main()
