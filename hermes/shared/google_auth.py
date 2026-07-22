"""OAuth-refresh-token based Google service builder.

Reads a credentials JSON file with `client_id`, `client_secret`, and
`refresh_token`, refreshes the access token, and returns a googleapiclient
service handle. Cached per (creds_path, api_name) tuple.
"""

from __future__ import annotations

import json
import threading
import time
from pathlib import Path

from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

_cache: dict[tuple[str, str, str], tuple[object, float]] = {}
_lock = threading.Lock()


def build_service(creds_path: Path, api_name: str, api_version: str, scopes: list[str]):
    """Return a discovery-built service, cached ~50 min per creds+api."""
    key = (str(creds_path), api_name, api_version)
    now = time.time()
    with _lock:
        cached = _cache.get(key)
        if cached and cached[1] > now:
            return cached[0]
        payload = json.loads(Path(creds_path).read_text())
        creds = Credentials(
            token=None,
            refresh_token=payload["refresh_token"],
            client_id=payload["client_id"],
            client_secret=payload["client_secret"],
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes,
        )
        creds.refresh(GoogleRequest())
        svc = build(api_name, api_version, credentials=creds, cache_discovery=False)
        _cache[key] = (svc, now + 50 * 60)
        return svc
