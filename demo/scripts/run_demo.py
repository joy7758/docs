#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = BASE_DIR / "input" / "dpp_object.json"
OUTPUT_DIR = BASE_DIR / "output"
DELAY_SCALE = max(0.0, float(os.environ.get("DEMO_DELAY_SCALE", "1.0")))


def canonical_json(data: object) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def sha256_json(data: object) -> str:
    payload = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_json(path: Path, data: object) -> None:
    path.write_text(canonical_json(data) + "\n", encoding="utf-8")


def pause(seconds: float) -> None:
    time.sleep(seconds * DELAY_SCALE)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    digital_object = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    object_hash = sha256_json(digital_object)

    run_id = "RUN-DEMO-20260101-0001"
    audit_record_id = "ARO-DEMO-0001"
    summary_id = "SUMMARY-DEMO-0001"

    agent_result = {
        "run_id": run_id,
        "object_id": digital_object["object_id"],
        "status": "EXECUTION_OK",
        "agent": {
            "name": "fdo-demo-agent",
            "version": "1.0.0",
        },
        "input_hash": object_hash,
        "steps": [
            {"name": "ingest_digital_object", "status": "OK"},
            {"name": "extract_core_fields", "status": "OK"},
            {"name": "prepare_evidence_bundle", "status": "OK"},
        ],
    }

    aro_audit_record = {
        "record_id": audit_record_id,
        "run_id": run_id,
        "object_id": digital_object["object_id"],
        "event_type": "AGENT_EXECUTION",
        "decision": "EVIDENCE_BUNDLE_CREATED",
        "agent_name": "fdo-demo-agent",
        "object_hash": object_hash,
        "timestamp": "2026-01-01T10:00:05Z",
    }

    public_evidence_summary = {
        "summary_id": summary_id,
        "object_id": digital_object["object_id"],
        "product": digital_object["product"],
        "manufacturer": digital_object["manufacturer"],
        "run_id": run_id,
        "result": "Execution completed and evidence bundle generated.",
        "evidence_files": [
            "agent_result.json",
            "aro_audit_record.json",
            "mvk_input.json",
            "public_evidence_summary.json",
        ],
    }

    verification_payload = {
        "object_id": digital_object["object_id"],
        "run_id": run_id,
        "object_hash": object_hash,
        "audit_record_id": audit_record_id,
        "summary_id": summary_id,
    }

    mvk_input = {
        "verification_id": "MVK-DEMO-0001",
        "hash_algorithm": "sha256",
        "bundle_payload": verification_payload,
        "bundle_hash": sha256_json(verification_payload),
        "expected_result": "REPLAY_PASS",
    }

    print("=== RUNNING DEMO ===", flush=True)
    pause(1.5)
    print("Agent processing object...", flush=True)
    pause(3.0)
    write_json(OUTPUT_DIR / "agent_result.json", agent_result)
    print("EXECUTION_OK", flush=True)
    pause(1.5)
    print("", flush=True)
    print("Generating evidence bundle...", flush=True)
    pause(3.0)
    write_json(OUTPUT_DIR / "aro_audit_record.json", aro_audit_record)
    write_json(OUTPUT_DIR / "mvk_input.json", mvk_input)
    write_json(OUTPUT_DIR / "public_evidence_summary.json", public_evidence_summary)
    print("EVIDENCE_CREATED", flush=True)
    pause(1.0)


if __name__ == "__main__":
    main()
