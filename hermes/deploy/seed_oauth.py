"""One-shot OAuth seed for the Hermes pullers.

Runs on your desktop (needs a browser). For each --service / --account
combination, opens a browser, prompts consent, and writes a JSON file
into hermes/credentials/{service}_{account}.json containing client_id,
client_secret, and refresh_token.

Usage:
    python deploy/seed_oauth.py --service gsc --account 2012infinite \
        --client-secrets /path/to/client_secrets.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    sys.stderr.write("pip install google-auth-oauthlib\n")
    sys.exit(1)

SCOPES = {
    "gsc": ["https://www.googleapis.com/auth/webmasters.readonly"],
    "ga4": ["https://www.googleapis.com/auth/analytics.readonly"],
}

REPO_ROOT = Path(__file__).resolve().parents[1]
CREDS_DIR = REPO_ROOT / "credentials"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--service", choices=["gsc", "ga4"], required=True)
    ap.add_argument("--account", required=True, help="e.g. 2012infinite / sunnypat81")
    ap.add_argument("--client-secrets", required=True)
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
    if "client_id" not in installed:
        sys.stderr.write("client_secrets JSON has no 'installed' or 'web' block\n")
        sys.exit(1)

    payload = {
        "client_id": installed["client_id"],
        "client_secret": installed["client_secret"],
        "refresh_token": creds.refresh_token,
    }

    CREDS_DIR.mkdir(parents=True, exist_ok=True)
    out = CREDS_DIR / f"{args.service}_{args.account}.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
