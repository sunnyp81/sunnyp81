"""Minimal JSON logger for cron output."""

from __future__ import annotations

import json
import sys
import time


def log(event: str, **fields):
    payload = {"ts": time.time(), "event": event, **fields}
    print(json.dumps(payload, default=str), flush=True)


def die(event: str, **fields):
    log(event, level="fatal", **fields)
    sys.exit(1)
