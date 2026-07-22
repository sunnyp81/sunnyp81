"""Shared config for the Hermes data pullers.

Two Google accounts, one Bing account. Credentials are loaded from
per-account JSON files under `credentials/`, kept out of git. See
`credentials/README.md` for the exact shape.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
CREDS_DIR = REPO_ROOT / "credentials"
DATA_DIR = Path(os.environ.get("HERMES_DATA_DIR", REPO_ROOT / "data"))


@dataclass(frozen=True)
class Account:
    key: str
    email: str
    gsc_creds: Path
    ga4_creds: Path


ACCOUNTS: list[Account] = [
    Account(
        key="2012infinite",
        email="2012.infinite@gmail.com",
        gsc_creds=CREDS_DIR / "gsc_2012infinite.json",
        ga4_creds=CREDS_DIR / "ga4_2012infinite.json",
    ),
    Account(
        key="sunnypat81",
        email="sunnypat81@gmail.com",
        gsc_creds=CREDS_DIR / "gsc_sunnypat81.json",
        ga4_creds=CREDS_DIR / "ga4_sunnypat81.json",
    ),
]

GSC_SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
GA4_SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

BING_API_KEY = os.environ.get("BING_API_KEY", "")
