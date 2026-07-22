#!/usr/bin/env bash
# One-shot VPS setup for the Hermes pullers.
#
# Assumes:
#   - You have SSH access to the VPS as root.
#   - Python 3.11+ is installed.
#   - Credentials JSON files have been seeded locally via deploy/seed_oauth.py
#     and are present under credentials/ on your desk.
#
# Usage on desktop:
#   scp -r hermes/credentials root@VPS:/root/.hermes/credentials
#   ssh root@VPS 'bash -s' < hermes/deploy/setup.sh

set -euo pipefail

HERMES_HOME="${HERMES_HOME:-/root/.hermes}"

mkdir -p "$HERMES_HOME"/{pullers,shared,data,logs}
cd "$HERMES_HOME"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --quiet -r requirements.txt

echo "Installing crontab entries…"
( crontab -l 2>/dev/null | grep -v 'hermes_' ; cat deploy/hermes-crontab.txt ) | crontab -

echo "Done. Verify with: crontab -l | grep hermes_"
