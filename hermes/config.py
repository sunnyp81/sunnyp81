"""Shared config for the Hermes data pullers.

Credentials come from environment variables (populated from GitHub
Actions secrets in prod, from a `.env` you source locally in dev).
Naming convention:

  GOOGLE_CLIENT_ID              — shared OAuth app (both accounts)
  GOOGLE_CLIENT_SECRET          — shared OAuth app (both accounts)
  GSC_REFRESH_TOKEN_{KEY}       — per-account GSC refresh token
  GA4_REFRESH_TOKEN_{KEY}       — per-account GA4 refresh token
  BING_API_KEY                  — single Bing Webmaster key
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("HERMES_DATA_DIR", REPO_ROOT / "data"))


@dataclass(frozen=True)
class Account:
    key: str
    email: str


ACCOUNTS: list[Account] = [
    Account(key="2012infinite", email="2012.infinite@gmail.com"),
    Account(key="sunnypat81", email="sunnypat81@gmail.com"),
]

# Must match what the refresh tokens were actually granted, exactly —
# Google's token endpoint rejects a refresh request whose "scope" isn't
# what that token was issued for, even a narrower one (e.g. requesting
# .readonly against a token minted with the broader, unsuffixed scope
# fails with invalid_scope). Both harvested GSC tokens were minted via
# seed_oauth.py / the desktop MCP with the full (non-readonly) scope.
GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters"]
GA4_SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def refresh_token_env_name(service: str, account: Account) -> str:
    """`GSC_REFRESH_TOKEN_2012INFINITE`, `GA4_REFRESH_TOKEN_SUNNYPAT81`, etc."""
    return f"{service.upper()}_REFRESH_TOKEN_{account.key.upper()}"


def google_client_env(service: str = "", account_key: str = "") -> tuple[str, str]:
    """OAuth client for a (service, account) pair, most specific wins:

      1. `{SERVICE}_CLIENT_ID_{ACCOUNT}` / `..._SECRET_{ACCOUNT}` — a refresh
         token minted by a client unique to that one account+service.
      2. `{SERVICE}_CLIENT_ID` / `..._SECRET` — shared across accounts for
         one service.
      3. `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` — shared across everything.

    A refresh token can only be redeemed by the exact client that minted
    it, and desktop MCP installs + ad-hoc seed runs hand out tokens from
    different clients per account — hence three fallback tiers instead of one.
    """
    if service and account_key:
        cid = os.environ.get(f"{service.upper()}_CLIENT_ID_{account_key.upper()}", "")
        csec = os.environ.get(f"{service.upper()}_CLIENT_SECRET_{account_key.upper()}", "")
        if cid and csec:
            return cid, csec
    if service:
        cid = os.environ.get(f"{service.upper()}_CLIENT_ID", "")
        csec = os.environ.get(f"{service.upper()}_CLIENT_SECRET", "")
        if cid and csec:
            return cid, csec
    cid = os.environ.get("GOOGLE_CLIENT_ID", "")
    csec = os.environ.get("GOOGLE_CLIENT_SECRET", "")
    return cid, csec


BING_API_KEY = os.environ.get("BING_API_KEY", "")

# Sites every puller must skip — client properties that appear in shared
# accounts but aren't part of the portfolio (e.g. Figment clients).
BLACKLIST = {
    "londonorthotics.co.uk",
}


def is_blacklisted(site: str) -> bool:
    """Match a site against BLACKLIST regardless of scheme/www/sc-domain form."""
    s = re.sub(r"^(sc-domain:|https?://)", "", site.strip().lower())
    s = s.split("/")[0]
    if s.startswith("www."):
        s = s[4:]
    return s in BLACKLIST
