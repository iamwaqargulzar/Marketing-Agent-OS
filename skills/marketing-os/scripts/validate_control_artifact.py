#!/usr/bin/env python3
"""Validate a portable Marketing Agent OS control artifact."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
from pathlib import Path


TOP_FIELDS = {
    "$schema", "schema_version", "artifact_id", "revision", "state",
    "objective", "owner", "created_at", "updated_at", "inputs", "action",
    "authority", "constraints", "idempotency_key", "measurement", "result",
}
REQUIRED = {
    "schema_version", "artifact_id", "revision", "state", "objective", "owner",
    "created_at", "updated_at", "inputs", "action", "authority",
}
STATES = {"proposed", "approved", "executing", "complete", "blocked"}
ACTION_TYPES = {
    "planning", "read-only", "file-write", "account-write", "send", "publish",
    "spend", "delete", "other",
}
SIDE_EFFECTS = ACTION_TYPES - {"planning", "read-only"}
AUTHORITY_STATES = {"not-required", "pending", "granted", "denied"}
EVIDENCE_LABELS = {"measured", "user-provided", "calculated", "estimated", "proxy"}
OUTCOMES = {"succeeded", "failed", "partial", "unknown"}
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def strict_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def finite_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise ValueError("numbers must be finite")
    return number


def canonical_bytes(value: object) -> bytes:
    rendered = json.dumps(
        value, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True
    )
    return (rendered + "\n").encode("utf-8")


def utc_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = dt.datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() == dt.timedelta(0)


def object_fields(value, name, allowed, required, errors):
    if not isinstance(value, dict):
        errors.append(f"{name} must be an object")
        return {}
    missing = sorted(required - set(value))
    extra = sorted(set(value) - allowed)
    if missing:
        errors.append(f"{name} is missing: {', '.join(missing)}")
    if extra:
        errors.append(f"{name} has unsupported fields: {', '.join(extra)}")
    return value


def nonempty(value, name, errors, maximum=1000):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        errors.append(
            f"{name} must be a non-empty string of at most {maximum} characters"
        )


def validate(document: object) -> list[str]:
    errors: list[str] = []
    root = object_fields(document, "artifact", TOP_FIELDS, REQUIRED, errors)
    if not root:
        return errors

    if root.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    artifact_id = root.get("artifact_id")
    if not isinstance(artifact_id, str) or not SAFE_ID.fullmatch(artifact_id):
        errors.append("artifact_id must be a portable 1..128 character identifier")
    revision = root.get("revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 1:
        errors.append("revision must be an integer greater than zero")
    if root.get("state") not in STATES:
        errors.append("state is invalid")
    nonempty(root.get("objective"), "objective", errors)
    nonempty(root.get("owner"), "owner", errors, 200)
    for field in ("created_at", "updated_at"):
        if not utc_timestamp(root.get(field)):
            errors.append(f"{field} must be an RFC 3339 UTC timestamp ending in Z")

    inputs = root.get("inputs")
    if not isinstance(inputs, list) or len(inputs) > 100:
        errors.append("inputs must be an array with at most 100 items")
        inputs = []
    for index, item in enumerate(inputs):
        record = object_fields(
            item,
            f"inputs[{index}]",
            {"ref", "evidence_label", "sha256"},
            {"ref", "evidence_label"},
            errors,
        )
        nonempty(record.get("ref"), f"inputs[{index}].ref", errors, 500)
        if record.get("evidence_label") not in EVIDENCE_LABELS:
            errors.append(f"inputs[{index}].evidence_label is invalid")
        digest = record.get("sha256")
        if digest is not None and (
            not isinstance(digest, str) or not SHA256.fullmatch(digest)
        ):
            errors.append(
                f"inputs[{index}].sha256 must be 64 lowercase hexadecimal characters"
            )

    action = object_fields(
        root.get("action"),
        "action",
        {"type", "scope", "payload_sha256"},
        {"type", "scope"},
        errors,
    )
    action_type = action.get("type")
    if action_type not in ACTION_TYPES:
        errors.append("action.type is invalid")
    nonempty(action.get("scope"), "action.scope", errors, 500)
    payload_hash = action.get("payload_sha256")
    if payload_hash is not None and (
        not isinstance(payload_hash, str) or not SHA256.fullmatch(payload_hash)
    ):
        errors.append("action.payload_sha256 must be 64 lowercase hexadecimal characters")

    authority = object_fields(
        root.get("authority"),
        "authority",
        {"required", "status", "scope", "granted_by", "granted_at"},
        {"required", "status", "scope"},
        errors,
    )
    authority_required = authority.get("required")
    authority_status = authority.get("status")
    if not isinstance(authority_required, bool):
        errors.append("authority.required must be a boolean")
    if authority_status not in AUTHORITY_STATES:
        errors.append("authority.status is invalid")
    nonempty(authority.get("scope"), "authority.scope", errors, 500)
    if authority.get("scope") != action.get("scope"):
        errors.append("authority.scope must exactly match action.scope")
    if authority_status == "granted":
        nonempty(authority.get("granted_by"), "authority.granted_by", errors, 200)
        if not utc_timestamp(authority.get("granted_at")):
            errors.append(
                "authority.granted_at is required and must be UTC when status is granted"
            )

    state = root.get("state")
    side_effect = action_type in SIDE_EFFECTS
    if side_effect and authority_required is not True:
        errors.append("persistent and external actions require authority")
    if authority_required is False and authority_status != "not-required":
        errors.append("authority.status must be not-required when authority is not required")
    if authority_required is True and authority_status == "not-required":
        errors.append("required authority cannot have status not-required")
    if authority_required is True and state in {"approved", "executing", "complete"}:
        if authority_status != "granted":
            errors.append(f"state {state} requires granted authority for this action")
        if payload_hash is None:
            errors.append(f"state {state} requires action.payload_sha256 for this action")
        nonempty(root.get("idempotency_key"), "idempotency_key", errors, 200)
    if authority_status == "denied" and state in {"approved", "executing", "complete"}:
        errors.append(
            "denied authority cannot accompany an approved, executing, or complete state"
        )

    constraints = root.get("constraints")
    if constraints is not None:
        record = object_fields(
            constraints,
            "constraints",
            {
                "budget_cap", "currency", "start_after", "deadline",
                "stop_condition", "recovery",
            },
            set(),
            errors,
        )
        budget = record.get("budget_cap")
        if budget is not None and (
            isinstance(budget, bool)
            or not isinstance(budget, (int, float))
            or not math.isfinite(budget)
            or budget < 0
        ):
            errors.append("constraints.budget_cap must be a finite non-negative number")
        currency = record.get("currency")
        if currency is not None and (
            not isinstance(currency, str) or not re.fullmatch(r"[A-Z]{3}", currency)
        ):
            errors.append("constraints.currency must be a three-letter uppercase code")
        for field in ("start_after", "deadline"):
            if field in record and not utc_timestamp(record[field]):
                errors.append(
                    f"constraints.{field} must be an RFC 3339 UTC timestamp ending in Z"
                )
        for field in ("stop_condition", "recovery"):
            if field in record:
                nonempty(record[field], f"constraints.{field}", errors)

    measurement = root.get("measurement")
    if measurement is not None:
        record = object_fields(
            measurement,
            "measurement",
            {"metric", "window", "decision_rule", "source_ref"},
            {"metric", "window", "decision_rule"},
            errors,
        )
        for field, maximum in (
            ("metric", 200), ("window", 200), ("decision_rule", 1000)
        ):
            nonempty(record.get(field), f"measurement.{field}", errors, maximum)
        if "source_ref" in record:
            nonempty(record["source_ref"], "measurement.source_ref", errors, 500)

    result = root.get("result")
    if state == "complete" and result is None:
        errors.append("state complete requires result")
    if result is not None:
        record = object_fields(
            result,
            "result",
            {"outcome", "observed_at", "receipt_ref"},
            {"outcome", "observed_at"},
            errors,
        )
        if record.get("outcome") not in OUTCOMES:
            errors.append("result.outcome is invalid")
        if not utc_timestamp(record.get("observed_at")):
            errors.append("result.observed_at must be an RFC 3339 UTC timestamp ending in Z")
        if "receipt_ref" in record:
            nonempty(record["receipt_ref"], "result.receipt_ref", errors, 500)
        if state == "complete" and side_effect and not record.get("receipt_ref"):
            errors.append(
                "a completed persistent or external action requires result.receipt_ref"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    parser.add_argument(
        "--allow-noncanonical",
        action="store_true",
        help="accept valid JSON that is not canonicalized",
    )
    args = parser.parse_args()
    try:
        raw = args.artifact.read_bytes()
        document = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=strict_object,
            parse_float=finite_float,
            parse_constant=lambda value: (_ for _ in ()).throw(
                ValueError(f"invalid number: {value}")
            ),
        )
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
        return 2
    errors = validate(document)
    if not args.allow_noncanonical and raw != canonical_bytes(document):
        errors.append(
            "artifact must use canonical JSON: UTF-8, sorted keys, two-space "
            "indentation, and a trailing newline"
        )
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
