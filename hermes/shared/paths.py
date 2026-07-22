"""Consistent day-partitioned output paths for pullers."""

from __future__ import annotations

import re
from datetime import date, datetime, timezone
from pathlib import Path

from config import DATA_DIR


def today_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def slugify(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")[:120]


def snapshot_path(service: str, account_key: str, site: str, report: str, day: str | None = None) -> Path:
    day = day or today_utc()
    d = DATA_DIR / service / day
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{slugify(account_key)}__{slugify(site)}__{slugify(report)}.json"


def summary_path(service: str, day: str | None = None) -> Path:
    day = day or today_utc()
    d = DATA_DIR / service / day
    d.mkdir(parents=True, exist_ok=True)
    return d / "_summary.json"
