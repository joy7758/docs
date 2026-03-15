#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

if [ -t 1 ] && command -v clear >/dev/null 2>&1; then
  clear
fi
echo "===== DIGITAL BIOSPHERE DEMO ====="
sleep 1
python3 scripts/run_demo.py
sleep 2
echo ""
echo "Generated artifacts:"
LC_ALL=C ls -1 output
sleep 2
python3 scripts/verify_demo.py
sleep 1
echo ""
echo "Demo finished."
