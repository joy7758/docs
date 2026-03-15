#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
MVK_INPUT_PATH = BASE_DIR / "output" / "mvk_input.json"
DELAY_SCALE = max(0.0, float(os.environ.get("DEMO_DELAY_SCALE", "1.0")))


def sha256_json(data: object) -> str:
    payload = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def pause(seconds: float) -> None:
    time.sleep(seconds * DELAY_SCALE)


def main() -> int:
    mvk_input = json.loads(MVK_INPUT_PATH.read_text(encoding="utf-8"))
    computed_hash = sha256_json(mvk_input["bundle_payload"])

    print("=== VERIFYING ===", flush=True)
    pause(4.0)
    if computed_hash == mvk_input["bundle_hash"] and mvk_input["expected_result"] == "REPLAY_PASS":
        print("REPLAY_PASS", flush=True)
        return 0

    print("REPLAY_FAIL", flush=True)
    return 1


if __name__ == "__main__":
    sys.exit(main())
