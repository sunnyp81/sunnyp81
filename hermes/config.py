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

GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
GA4_SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]


def refresh_token_env_name(service: str, account: Account) -> str:
    """`GSC_REFRESH_TOKEN_2012INFINITE`, `GA4_REFRESH_TOKEN_SUNNYPAT81`, etc."""
    return f"{service.upper()}_REFRESH_TOKEN_{account.key.upper()}"


def google_client_env() -> tuple[str, str]:
    cid = os.environ.get("GOOGLE_CLIENT_ID", "")
    csec = os.environ.get("GOOGLE_CLIENT_SECRET", "")
    return cid, csec


BING_API_KEY = os.environ.get("BING_API_KEY", "")
