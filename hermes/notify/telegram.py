#!/usr/bin/env python3
"""Send a Telegram message to Sunny's phone. Stdlib only.

Reads TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID from the environment
(GitHub Actions secrets). Message text comes from argv[1] or stdin.

Never fails the caller: if secrets are unset or the send errors, it prints
the message to the log and exits 0, so a broken notifier can not break a
workflow. The absence of an expected Telegram message is itself the alarm
(see hermes/RUNBOOK.md).
"""
import json
import os
import sys
import urllib.request


def main() -> int:
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat = os.environ.get("TELEGRAM_CHAT_ID", "")
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    text = text.strip()[:4000]
    if not text:
        return 0
    if not token or not chat:
        print("telegram: TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID unset; message was:")
        print(text)
        return 0
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=json.dumps(
            {"chat_id": chat, "text": text, "disable_web_page_preview": True}
        ).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"telegram: sent (HTTP {resp.status})")
    except Exception as exc:  # noqa: BLE001 - notifier must never fail the caller
        print(f"telegram: send failed ({exc}); message was:")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
