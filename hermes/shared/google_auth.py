"""Env-var backed Google service builder.

Given an Account + (service, api_version, scopes), refreshes the
access token and returns a googleapiclient service handle. Cached
per (account.key, service) for ~50 min so long sweeps don't re-auth.
"""

from __future__ import annotations

import os
import threading
import time

from google.auth.transport.requests import Request as GoogleRequest
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import Account, google_client_env, refresh_token_env_name

_cache: dict[tuple[str, str, str], tuple[object, float]] = {}
_lock = threading.Lock()


def build_service(account: Account, service: str, api_name: str, api_version: str, scopes: list[str]):
    key = (account.key, api_name, api_version)
    now = time.time()
    with _lock:
        cached = _cache.get(key)
        if cached and cached[1] > now:
            return cached[0]

        client_id, client_secret = google_client_env(service, account.key)
        if not (client_id and client_secret):
            raise RuntimeError(
                f"{service.upper()}_CLIENT_ID/SECRET (optionally _{account.key.upper()}) "
                "or GOOGLE_CLIENT_ID/SECRET must be set"
            )

        env_name = refresh_token_env_name(service, account)
        refresh_token = os.environ.get(env_name)
        if not refresh_token:
            raise RuntimeError(f"{env_name} env var not set")

        creds = Credentials(
            token=None,
            refresh_token=refresh_token,
            client_id=client_id,
            client_secret=client_secret,
            token_uri="https://oauth2.googleapis.com/token",
            scopes=scopes,
        )
        creds.refresh(GoogleRequest())
        svc = build(api_name, api_version, credentials=creds, cache_discovery=False)
        _cache[key] = (svc, now + 50 * 60)
        return svc
