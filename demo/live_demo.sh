#!/usr/bin/env bash

set -euo pipefail

cd /Users/zhangbin/GitHub/docs/demo
export TERM="${TERM:-xterm-256color}"

exec python3 scripts/live_demo_player.py
