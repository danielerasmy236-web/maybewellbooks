#!/bin/bash
# Wrapper invoked weekly by launchd. Runs the PDF-factory orchestrator using
# an ephemeral uv-managed Python environment with reportlab installed.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export PATH="$HOME/.local/bin:$PATH"

cd "$SCRIPT_DIR"
uv run --python 3.11 --with reportlab python3 run_next.py
