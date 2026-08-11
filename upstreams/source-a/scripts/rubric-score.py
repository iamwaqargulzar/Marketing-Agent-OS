#!/usr/bin/env python3
"""Deterministic scorer for the eight advisory marketing frameworks.

Input follows ``references/audit-run.schema.json``. No score is emitted until
every applicable item is observed. Unknown and missing items remain visible as
coverage gaps; N/A is accepted only for catalog-declared conditional items.
"""
from __future__ import annotations

import argparse
import datetime as dt
from decimal import Decimal
from fractions import Fraction
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CATALOG = os.path.join(ROOT, "references", "framework-catalog.json")
OBSERVED_STATES = {"pass", "partial", "fail"}
ALL_STATES = OBSERVED_STATES | {"unknown", "na"}
EVIDENCE_TYPES = {"measured", "user-provided", "calculated", "estimated", "proxy"}
CONFIDENCE = {"high", "medium", "low"}
RUN_FIELDS = {"framework", "profile", "target", "observed_at", "context", "items"}
ITEM_FIELDS = {"id", "state", "reason", "evidence"}
EVIDENCE_FIELDS = {"type", "source", "observed_at", "confidence"}
SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
NUMBER_TYPES = (int, float, Decimal, Fraction)
MAX_JSON_DEPTH = 64
MAX_JSON_NODES = 10_000
MAX_NUMBER_BITS = 4096
MAX_DECIMAL_DIGITS = 1000
MAX_DECIMAL_ADJUSTED_EXPONENT = 1000
MAX_INPUT_BYTES = 1_000_000
CATALOG_FIELDS = {"catalog_version", "semantics", "frameworks"}
SEMANTICS_FIELDS = {
    "external_validity", "score_states", "item_points", "evidence_types",
    "confidence_factors", "required_coverage", "missingness", "rounding",
    "veto_ceiling", "multi_veto", "bands",
}
FRAMEWORK_FIELDS = {
    "source", "construct", "unit_of_analysis", "required_context", "context_allowed",
    "profiles", "dimensions", "item_definitions", "item_policies", "veto_items",
    "benchmark_mode", "composite_score", "outcomes",
}
PROFILE_FIELDS = {"context_equals", "dimensions", "include_items", "exclude_items"}
DIMENSION_FIELDS = {"name", "item_prefix", "item_count", "id_width"}
ITEM_POLICY_FIELDS = {
    "applicability", "applicable_when", "condition", "definition", "benchmark",
    "unknown_policy", "veto", "fail_flag", "asset_gate_note",
}


class RubricError(ValueError):
    pass


def load_json(path):
    try:
        with open(path, "rb") as handle:
            raw = handle.read(MAX_INPUT_BYTES + 1)
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError("input exceeds %d-byte limit" % MAX_INPUT_BYTES)
        text = raw.decode("utf-8")
        return json.loads(
            text,
            parse_float=Decimal,
            parse_constant=lambda value: (_ for _ in ()).throw(
                ValueError("non-finite JSON constant: %s" % value)
            ),
        )
    except (OSError, UnicodeDecodeError, ValueError, RecursionError) as exc:
        raise RubricError("cannot load %s: %s" % (path, exc)) from exc


def finite_number(value):
    """Return whether *value* is a finite JSON number (never a boolean)."""
    if isinstance(value, bool) or not isinstance(value, NUMBER_TYPES):
        return False
    if isinstance(value, int):
        return value.bit_length() <= MAX_NUMBER_BITS
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, Decimal):
        return (
            value.is_finite()
            and len(value.as_tuple().digits) <= MAX_DECIMAL_DIGITS
            and abs(value.adjusted()) <= MAX_DECIMAL_ADJUSTED_EXPONENT
        )
    if isinstance(value, Fraction):
        return (
            value.numerator.bit_length() <= MAX_NUMBER_BITS
            and value.denominator.bit_length() <= MAX_NUMBER_BITS
        )
    return False


def canonical_json_value(value):
    """Return one hashable, exact, type-aware JSON value tree.

    Child nodes stay as tuples. Serializing each child before embedding it in
    its parent repeatedly escapes the same subtree and grows exponentially for
    nested catalog selectors.
    """
    if value is None:
        return ("null",)
    elif isinstance(value, bool):
        return ("boolean", value)
    elif isinstance(value, str):
        return ("string", value)
    elif finite_number(value):
        number = exact_fraction(value)
        return ("number", number.numerator, number.denominator)
    elif isinstance(value, list):
        encoded = [canonical_json_value(item) for item in value]
        if None in encoded:
            return None
        return ("array", tuple(encoded))
    elif isinstance(value, dict) and all(isinstance(key, str) for key in value):
        encoded = [(key, canonical_json_value(item)) for key, item in value.items()]
        if any(item is None for _, item in encoded):
            return None
        return ("object", tuple(sorted(encoded)))
    else:
        return None


def finite_json_value(value):
    """Iteratively validate finite, bounded JSON values without recursion overflow."""
    stack = [(value, 0)]
    nodes = 0
    while stack:
        current, depth = stack.pop()
        nodes += 1
        if nodes > MAX_JSON_NODES or depth > MAX_JSON_DEPTH:
            return False
        if current is None or isinstance(current, (bool, str)):
            continue
        if isinstance(current, NUMBER_TYPES) and not isinstance(current, bool):
            if not finite_number(current):
                return False
            continue
        if isinstance(current, list):
            stack.extend((item, depth + 1) for item in current)
            continue
        if isinstance(current, dict) and all(isinstance(key, str) for key in current):
            stack.extend((item, depth + 1) for item in current.values())
            continue
        return False
    return True


def exact_json_dumps(value, indent=2, level=0):
    """Serialize Decimal values as their exact JSON number lexemes."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return json.dumps(value, ensure_ascii=False, allow_nan=False)
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("non-finite Decimal is not JSON")
        return str(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        prefix = " " * (indent * (level + 1))
        suffix = " " * (indent * level)
        return "[\n%s%s\n%s]" % (
            prefix,
            (",\n" + prefix).join(
                exact_json_dumps(item, indent, level + 1) for item in value
            ),
            suffix,
        )
    if isinstance(value, dict) and all(isinstance(key, str) for key in value):
        if not value:
            return "{}"
        prefix = " " * (indent * (level + 1))
        suffix = " " * (indent * level)
        entries = []
        for key in sorted(value):
            entries.append(
                "%s: %s" % (
                    json.dumps(key, ensure_ascii=False),
                    exact_json_dumps(value[key], indent, level + 1),
                )
            )
        return "{\n%s%s\n%s}" % (prefix, (",\n" + prefix).join(entries), suffix)
    raise TypeError("value is not strict JSON: %r" % (value,))


def item_ids(dimension):
    prefix = dimension["item_prefix"]
    width = int(dimension.get("id_width", 1))
    return [prefix + str(index).zfill(width) for index in range(1, int(dimension["item_count"]) + 1)]


def framework_item_ids(framework):
    result = set()
    for dimension in framework["dimensions"].values():
        result.update(item_ids(dimension))
    return result


def validate_catalog(catalog):
    errors = []
    if not isinstance(catalog, dict):
        return ["catalog must be an object"]
    if not finite_json_value(catalog):
        return ["catalog must contain bounded finite JSON values"]
    extra_catalog_fields = set(catalog) - CATALOG_FIELDS
    if extra_catalog_fields:
        errors.append("catalog has unknown fields: %s" % ", ".join(
            sorted(repr(key) for key in extra_catalog_fields)
        ))
    catalog_version = catalog.get("catalog_version")
    if not isinstance(catalog_version, str) or not SEMVER_RE.fullmatch(catalog_version):
        errors.append("catalog_version must be a semantic version")

    frameworks = catalog.get("frameworks")
    expected_names = {"CORE-EEAT", "CITE", "STAR", "ROAS", "SEND", "RAMP", "ECHO", "TALE"}
    if not isinstance(frameworks, dict) or set(frameworks) != expected_names:
        errors.append("catalog must contain exactly the eight frameworks")
        if not isinstance(frameworks, dict):
            return errors
    semantics = catalog.get("semantics")
    if not isinstance(semantics, dict):
        return errors + ["catalog semantics must be an object"]
    extra_semantics = set(semantics) - SEMANTICS_FIELDS
    missing_semantics = SEMANTICS_FIELDS - set(semantics)
    if extra_semantics:
        errors.append("catalog semantics has unknown fields: %s" % ", ".join(
            sorted(repr(key) for key in extra_semantics)
        ))
    if missing_semantics:
        errors.append("catalog semantics is missing fields: %s" % ", ".join(sorted(missing_semantics)))
    if not isinstance(semantics.get("external_validity"), str) or not semantics.get("external_validity", "").strip():
        errors.append("catalog external_validity must be a non-empty string")
    if semantics.get("score_states") != ["pass", "partial", "fail", "unknown", "na"]:
        errors.append("catalog score_states differ from the v17 contract")
    if semantics.get("item_points") != {"pass": 10, "partial": 5, "fail": 0}:
        errors.append("catalog item_points differ from the v17 contract")
    for label, values, expected_keys in (
            ("evidence types", semantics.get("evidence_types"), EVIDENCE_TYPES),
            ("confidence factors", semantics.get("confidence_factors"), CONFIDENCE)):
        if not isinstance(values, dict) or set(values) != expected_keys:
            errors.append("catalog %s differ from the v17 contract" % label)
        elif any(not finite_number(value) or value < 0 or value > 1 for value in values.values()):
            errors.append("catalog %s must be finite numbers from 0 to 1" % label)
    if semantics.get("required_coverage") != 100:
        errors.append("v17 comparable scoring requires required_coverage=100")
    missingness = semantics.get("missingness")
    if (not isinstance(missingness, dict) or set(missingness) != {"unknown", "na", "missing"}
            or any(not isinstance(value, str) or not value.strip() for value in missingness.values())):
        errors.append("catalog missingness must define non-empty unknown, na, and missing policies")
    if semantics.get("rounding") != "floor":
        errors.append("v17 rounding must be floor")
    if semantics.get("veto_ceiling") != 59:
        errors.append("v17 universal veto ceiling must be 59")
    if semantics.get("multi_veto") != {"minimum": 2, "verdict": "BLOCK", "emit_final_score": False}:
        errors.append("catalog multi_veto differs from the v17 contract")
    bands = semantics.get("bands")
    if not isinstance(bands, list) or len(bands) != 5:
        errors.append("catalog bands must contain exactly five entries")
    else:
        for index, band in enumerate(bands, 1):
            if (not isinstance(band, dict) or set(band) != {"name", "minimum", "maximum"}
                    or not isinstance(band.get("name"), str) or not band.get("name", "").strip()
                    or not isinstance(band.get("minimum"), int) or isinstance(band.get("minimum"), bool)
                    or not isinstance(band.get("maximum"), int) or isinstance(band.get("maximum"), bool)
                    or not 0 <= band.get("minimum", -1) <= 100
                    or not 0 <= band.get("maximum", -1) <= 100):
                errors.append("catalog band %d is invalid" % index)

    for name, framework in frameworks.items():
        if not isinstance(framework, dict):
            errors.append("%s framework must be an object" % name)
            continue
        extra_framework_fields = set(framework) - FRAMEWORK_FIELDS
        required_framework_fields = {
            "source", "construct", "unit_of_analysis", "required_context",
            "profiles", "dimensions", "veto_items",
        }
        missing_framework_fields = required_framework_fields - set(framework)
        if extra_framework_fields:
            errors.append("%s has unknown fields: %s" % (
                name, ", ".join(sorted(repr(key) for key in extra_framework_fields)),
            ))
        if missing_framework_fields:
            errors.append("%s is missing fields: %s" % (name, ", ".join(sorted(missing_framework_fields))))
        source = framework.get("source")
        if not isinstance(source, str) or not re.fullmatch(r"references/.+\.md", source):
            errors.append("%s source must name a Markdown reference" % name)
        for field_name in ("construct", "unit_of_analysis"):
            if not isinstance(framework.get(field_name), str) or not framework.get(field_name, "").strip():
                errors.append("%s %s must be a non-empty string" % (name, field_name))
        for field_name in ("benchmark_mode", "outcomes"):
            if field_name in framework and (
                    not isinstance(framework[field_name], str) or not framework[field_name].strip()):
                errors.append("%s %s must be a non-empty string" % (name, field_name))
        if "composite_score" in framework and not isinstance(framework["composite_score"], bool):
            errors.append("%s composite_score must be boolean" % name)
        required_context = framework.get("required_context", [])
        valid_context_keys = (
            isinstance(required_context, list) and bool(required_context)
            and all(isinstance(key, str) and key for key in required_context)
        )
        if not valid_context_keys or len(required_context) != len(set(required_context)):
            errors.append("%s required_context is invalid" % name)
            required_context = []
        dimensions = framework.get("dimensions", {})
        if not isinstance(dimensions, dict) or not dimensions:
            errors.append("%s has no valid dimensions" % name)
            continue
        known_ids = set()
        for dimension_name, dimension in dimensions.items():
            if not isinstance(dimension, dict):
                errors.append("%s/%s dimension must be an object" % (name, dimension_name))
                continue
            if set(dimension) != DIMENSION_FIELDS:
                errors.append("%s/%s dimension fields are invalid" % (name, dimension_name))
            count = dimension.get("item_count")
            width = dimension.get("id_width", 1)
            prefix = dimension.get("item_prefix")
            dimension_label = dimension.get("name")
            if (not isinstance(count, int) or isinstance(count, bool) or count < 1
                    or not isinstance(width, int) or isinstance(width, bool) or width < 1
                    or not isinstance(prefix, str) or not prefix
                    or not isinstance(dimension_label, str) or not dimension_label.strip()):
                errors.append("%s/%s has invalid item identity fields" % (name, dimension_name))
                continue
            ids = set(item_ids(dimension))
            if known_ids & ids:
                errors.append("%s dimensions produce duplicate item IDs" % name)
            known_ids.update(ids)
        profiles = framework.get("profiles", {})
        if not isinstance(profiles, dict) or not profiles:
            errors.append("%s has no profiles" % name)
            continue
        for profile, spec in profiles.items():
            if not isinstance(spec, dict):
                errors.append("%s/%s profile must be an object" % (name, profile))
                continue
            extra_profile_fields = set(spec) - PROFILE_FIELDS
            if extra_profile_fields:
                errors.append("%s/%s has unknown profile fields: %s" % (
                    name, profile, ", ".join(sorted(repr(key) for key in extra_profile_fields)),
                ))
            weights = spec.get("dimensions", {})
            if not isinstance(weights, dict) or not weights:
                errors.append("%s/%s has no dimensions" % (name, profile))
                continue
            if any(dimension not in dimensions for dimension in weights):
                errors.append("%s/%s references an unknown dimension" % (name, profile))
            numeric_weights = all(
                finite_number(weight) and 0 < weight <= 1
                for weight in weights.values()
            )
            exact_weight_total = (
                sum(exact_fraction(weight) for weight in weights.values())
                if numeric_weights else Fraction(0)
            )
            if not numeric_weights or exact_weight_total != 1:
                errors.append("%s/%s weights do not sum to 1" % (name, profile))
            context_equals = spec.get("context_equals", {})
            if not isinstance(context_equals, dict) or any(
                    key not in required_context for key in context_equals):
                errors.append("%s/%s has invalid context_equals" % (name, profile))
            elif any(canonical_json_value(value) is None for value in context_equals.values()):
                errors.append("%s/%s context_equals must contain finite JSON values" % (name, profile))
            for selector in ("include_items", "exclude_items"):
                selected = spec.get(selector, {})
                if not isinstance(selected, dict) or any(key not in weights for key in selected):
                    errors.append("%s/%s has invalid %s dimensions" % (name, profile, selector))
                    continue
                for ids in selected.values():
                    if (not isinstance(ids, list)
                            or not all(isinstance(item_id, str) for item_id in ids)
                            or len(ids) != len(set(ids))):
                        errors.append("%s/%s %s must contain unique item arrays" % (name, profile, selector))
                        continue
                    for item_id in ids:
                        if item_id not in known_ids:
                            errors.append("%s/%s %s has unknown item %s" % (name, profile, selector, item_id))
        context_allowed = framework.get("context_allowed", {})
        valid_allowed = isinstance(context_allowed, dict)
        if valid_allowed:
            for key, values in context_allowed.items():
                encoded = [canonical_json_value(value) for value in values] if isinstance(values, list) else []
                if (key not in required_context or not isinstance(values, list) or not values or None in encoded
                        or len(encoded) != len(set(encoded))):
                    valid_allowed = False
                    break
        if not valid_allowed:
            errors.append("%s has invalid context_allowed" % name)
        veto_items = framework.get("veto_items", [])
        if (not isinstance(veto_items, list)
                or not all(isinstance(item_id, str) for item_id in veto_items)
                or len(veto_items) != len(set(veto_items))):
            errors.append("%s veto_items must be a unique array" % name)
            veto_items = []
        for item_id in veto_items:
            if item_id not in known_ids:
                errors.append("%s veto item %s is unknown" % (name, item_id))
        policies = framework.get("item_policies", {})
        if not isinstance(policies, dict):
            errors.append("%s item_policies must be an object" % name)
            policies = {}
        for item_id, policy in policies.items():
            if item_id not in known_ids:
                errors.append("%s item policy %s is unknown" % (name, item_id))
            if not isinstance(policy, dict):
                errors.append("%s item policy %s must be an object" % (name, item_id))
                continue
            if set(policy) - ITEM_POLICY_FIELDS:
                errors.append("%s item policy %s has unknown fields" % (name, item_id))
            if "applicability" in policy and policy["applicability"] != "conditional":
                errors.append("%s item policy %s has invalid applicability" % (name, item_id))
            applicable_when = policy.get("applicable_when", {})
            if not isinstance(applicable_when, dict) or any(
                    key not in required_context for key in applicable_when):
                errors.append("%s item policy %s has invalid applicable_when" % (name, item_id))
            elif any(canonical_json_value(value) is None for value in applicable_when.values()):
                errors.append("%s item policy %s applicable_when is not finite JSON" % (name, item_id))
            for field_name in ("condition", "definition", "benchmark", "fail_flag", "asset_gate_note"):
                if field_name in policy and (
                        not isinstance(policy[field_name], str) or not policy[field_name].strip()):
                    errors.append("%s item policy %s has invalid %s" % (name, item_id, field_name))
            if "unknown_policy" in policy and policy["unknown_policy"] != "needs-input":
                errors.append("%s item policy %s has invalid unknown_policy" % (name, item_id))
            if "veto" in policy and not isinstance(policy["veto"], bool):
                errors.append("%s item policy %s veto must be boolean" % (name, item_id))
        definitions = framework.get("item_definitions", {})
        if not isinstance(definitions, dict):
            errors.append("%s item_definitions must be an object" % name)
            definitions = {}
        for item_id, definition in definitions.items():
            if item_id not in known_ids:
                errors.append("%s item definition %s is unknown" % (name, item_id))
            if not isinstance(definition, str) or not definition.strip():
                errors.append("%s item definition %s must be a non-empty string" % (name, item_id))
    return errors


def expected_items(framework, profile):
    spec = framework["profiles"][profile]
    result = {}
    for dimension_name in spec["dimensions"]:
        ids = item_ids(framework["dimensions"][dimension_name])
        include = spec.get("include_items", {}).get(dimension_name)
        exclude = set(spec.get("exclude_items", {}).get(dimension_name, []))
        if include is not None:
            ids = list(include)
        result[dimension_name] = [item_id for item_id in ids if item_id not in exclude]
    return result


def parse_date(value, label, errors):
    if not isinstance(value, str):
        errors.append("%s must be an ISO date" % label)
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        errors.append("%s must be an ISO date" % label)
        return None


def evidence_strength(evidence, semantics):
    return (exact_fraction(semantics["evidence_types"][evidence["type"]])
            * exact_fraction(semantics["confidence_factors"][evidence["confidence"]]))


def confidence_label(strengths):
    if not strengths:
        return "not_scored"
    average = sum(strengths, Fraction()) / len(strengths)
    if average >= Fraction(85, 100):
        return "high"
    if average >= Fraction(65, 100):
        return "medium"
    return "low"


def exact_fraction(value):
    """Return the exact decimal value encoded by a catalog/fixture number."""
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def floor_fraction(value):
    value = exact_fraction(value)
    return value.numerator // value.denominator


def json_number(value):
    """Render an exact internal fraction as a JSON-compatible number."""
    value = exact_fraction(value)
    if value.denominator == 1:
        return value.numerator
    return float(value)


def score_run(run, catalog):
    errors = validate_catalog(catalog)
    if errors:
        raise RubricError("invalid catalog: " + "; ".join(errors))
    if not isinstance(run, dict):
        raise RubricError("audit run must be an object")
    extra_run_fields = sorted(set(run) - RUN_FIELDS)
    if extra_run_fields:
        raise RubricError("unknown audit run fields: %s" % ", ".join(extra_run_fields))
    framework_name = run.get("framework")
    if not isinstance(framework_name, str):
        raise RubricError("framework must be a string")
    framework = catalog["frameworks"].get(framework_name)
    if framework is None:
        raise RubricError("unknown framework: %r" % framework_name)
    profile = run.get("profile")
    if not isinstance(profile, str):
        raise RubricError("profile must be a string")
    if profile not in framework["profiles"]:
        raise RubricError("unknown profile %r for %s" % (profile, framework_name))

    errors = []
    target_value = run.get("target")
    target = target_value.strip() if isinstance(target_value, str) else ""
    if not target:
        errors.append("target is required")
    observed_at = parse_date(run.get("observed_at", ""), "observed_at", errors)
    context = run.get("context")
    if not isinstance(context, dict):
        errors.append("context must be an object")
        context = {}
    for key in framework.get("required_context", []):
        if key not in context or context[key] in (None, "", []):
            errors.append("missing required context: %s" % key)
    for key, expected_value in framework["profiles"][profile].get("context_equals", {}).items():
        if context.get(key) != expected_value:
            errors.append(
                "context.%s must be %r for profile %s" % (key, expected_value, profile)
            )
    for key, allowed_values in framework.get("context_allowed", {}).items():
        if context.get(key) not in allowed_values:
            errors.append("context.%s must be one of %s" % (key, allowed_values))
    if not finite_json_value(context):
        errors.append("context must contain finite JSON values")

    expected_by_dimension = expected_items(framework, profile)
    expected = {item_id for ids in expected_by_dimension.values() for item_id in ids}
    supplied = {}
    raw_items = run.get("items")
    if not isinstance(raw_items, list):
        errors.append("items must be an array")
        raw_items = []
    elif len(raw_items) > len(expected):
        raise RubricError(
            "items exceeds the %d-item maximum for %s/%s"
            % (len(expected), framework_name, profile)
        )
    for position, item in enumerate(raw_items, 1):
        if not isinstance(item, dict):
            errors.append("items[%d] must be an object" % position)
            continue
        extra_item_fields = sorted(set(item) - ITEM_FIELDS)
        if extra_item_fields:
            errors.append(
                "items[%d] has unknown fields: %s" % (position, ", ".join(extra_item_fields))
            )
        item_id = item.get("id")
        if not isinstance(item_id, str):
            errors.append("items[%d].id must be a string" % position)
            continue
        if item_id not in expected:
            errors.append("item %r is not part of %s/%s" % (item_id, framework_name, profile))
            continue
        if item_id in supplied:
            errors.append("duplicate item: %s" % item_id)
            continue
        supplied[item_id] = item

    semantics = catalog["semantics"]
    points = semantics["item_points"]
    policies = framework.get("item_policies", {})
    veto_ids = set(framework.get("veto_items", []))
    normalized = {}
    strengths = []
    gaps = []
    veto_failures = []
    flags = []
    run_date = observed_at

    for item_id in sorted(expected):
        item = supplied.get(item_id, {"id": item_id, "state": "unknown", "reason": "not supplied"})
        state = item.get("state")
        if not isinstance(state, str) or state not in ALL_STATES:
            errors.append("%s has invalid state %r" % (item_id, state))
            continue
        policy = policies.get(item_id, {})
        conditional = (
            policy.get("applicability") == "conditional"
            or bool(policy.get("applicable_when"))
        )
        raw_reason = item.get("reason", "")
        if not isinstance(raw_reason, str):
            errors.append("%s reason must be a string" % item_id)
            reason = ""
        else:
            reason = raw_reason.strip()
        evidence = item.get("evidence")
        applicable_when = policy.get("applicable_when")
        context_applies = True
        if applicable_when:
            context_applies = all(context.get(key) == value for key, value in applicable_when.items())

        if state == "na":
            if not conditional:
                errors.append("%s cannot be N/A under the catalog" % item_id)
            if applicable_when and context_applies:
                errors.append("%s is applicable under the declared context and cannot be N/A" % item_id)
            if not reason:
                errors.append("%s N/A requires a reason" % item_id)
            if evidence is not None:
                errors.append("%s N/A must not carry evidence" % item_id)
            normalized[item_id] = {"state": state, "reason": reason}
            continue
        if applicable_when and not context_applies:
            errors.append("%s must be N/A outside its applicable context" % item_id)
        if state == "unknown":
            if item_id in supplied and not reason:
                errors.append("%s Unknown requires a gap reason" % item_id)
            if evidence is not None:
                errors.append("%s Unknown must not carry evidence" % item_id)
            gaps.append({"id": item_id, "reason": reason or "applicable evidence not observed"})
            normalized[item_id] = {"state": state, "reason": reason or "applicable evidence not observed"}
            continue

        if not isinstance(evidence, dict):
            errors.append("%s %s requires evidence" % (item_id, state))
            continue
        extra_evidence_fields = sorted(set(evidence) - EVIDENCE_FIELDS)
        if extra_evidence_fields:
            errors.append("%s evidence has unknown fields: %s" % (
                item_id, ", ".join(extra_evidence_fields)
            ))
        evidence_type = evidence.get("type")
        evidence_confidence = evidence.get("confidence")
        source_value = evidence.get("source")
        source = source_value.strip() if isinstance(source_value, str) else ""
        evidence_date = parse_date(evidence.get("observed_at", ""), "%s evidence.observed_at" % item_id, errors)
        valid_evidence_type = isinstance(evidence_type, str) and evidence_type in EVIDENCE_TYPES
        valid_evidence_confidence = (
            isinstance(evidence_confidence, str) and evidence_confidence in CONFIDENCE
        )
        if not valid_evidence_type:
            errors.append("%s has invalid evidence type" % item_id)
        if not valid_evidence_confidence:
            errors.append("%s has invalid evidence confidence" % item_id)
        if not source:
            errors.append("%s evidence source is required" % item_id)
        if run_date and evidence_date and evidence_date > run_date:
            errors.append("%s evidence date is after the audit observation date" % item_id)
        if valid_evidence_type and valid_evidence_confidence:
            strengths.append(evidence_strength(evidence, semantics))
        normalized[item_id] = {
            "state": state,
            "points": points[state],
            "evidence": evidence,
        }
        if state == "fail" and item_id in veto_ids:
            veto_failures.append(item_id)
        if state == "fail" and policy.get("fail_flag"):
            flags.append({"id": item_id, "flag": policy["fail_flag"]})

    if errors:
        raise RubricError("; ".join(sorted(set(errors))))

    dimension_scores_exact = {}
    dimension_coverage = {}
    dimension_intervals_exact = {}
    dimension_intervals = {}
    empty_dimensions = []
    total_expected = 0
    total_observed = 0
    for dimension_name, ids in expected_by_dimension.items():
        applicable = [item_id for item_id in ids if normalized[item_id]["state"] != "na"]
        observed = [item_id for item_id in applicable if normalized[item_id]["state"] in OBSERVED_STATES]
        total_expected += len(applicable)
        total_observed += len(observed)
        coverage = 0 if not applicable else 100 * len(observed) // len(applicable)
        dimension_coverage[dimension_name] = coverage
        observed_points = sum(normalized[item_id].get("points", 0) for item_id in observed)
        unknown_count = len(applicable) - len(observed)
        if applicable:
            lower = Fraction(observed_points * 10, len(applicable))
            upper = Fraction((observed_points + unknown_count * 10) * 10, len(applicable))
        else:
            lower, upper = Fraction(0), Fraction(100)
            empty_dimensions.append(dimension_name)
            gaps.append({"id": dimension_name, "reason": "profile dimension has no applicable items"})
        dimension_intervals_exact[dimension_name] = (lower, upper)
        dimension_intervals[dimension_name] = [json_number(lower), json_number(upper)]
        if coverage == 100 and applicable:
            dimension_scores_exact[dimension_name] = lower

    overall_coverage = 100 if total_expected == 0 else 100 * total_observed // total_expected
    weights = framework["profiles"][profile]["dimensions"]
    exact_weights = {name: exact_fraction(weight) for name, weight in weights.items()}
    lower_bound = floor_fraction(sum(
        dimension_intervals_exact[name][0] * exact_weights[name] for name in weights
    ))
    upper_bound = floor_fraction(sum(
        dimension_intervals_exact[name][1] * exact_weights[name] for name in weights
    ))
    complete = not empty_dimensions and overall_coverage == semantics["required_coverage"] and all(
        dimension_coverage[name] == semantics["required_coverage"] for name in weights
    )
    veto_count = len(veto_failures)
    result = {
        "schema_version": "3.0",
        "catalog_version": catalog["catalog_version"],
        "advisory": True,
        "external_validity": semantics["external_validity"],
        "framework": framework_name,
        "profile": profile,
        "target": target,
        "observed_at": run.get("observed_at"),
        "context": context,
        "score_state": "SCORED" if complete else "NOT_SCORED",
        "evidence_coverage": overall_coverage,
        "dimension_coverage": dimension_coverage,
        "score_interval": [lower_bound, upper_bound],
        "score_confidence": confidence_label(strengths) if complete else "not_scored",
        "veto_items_failed": sorted(veto_failures),
        "veto_count": veto_count,
        "flags": flags,
        "cap_applied": False,
        "gaps": gaps,
    }
    if not complete:
        result["status"] = "DONE" if veto_count >= 2 else "NEEDS_INPUT"
        result["verdict"] = "BLOCK" if veto_count >= 2 else "UNDECIDED"
        return result

    raw = floor_fraction(sum(
        dimension_scores_exact[name] * exact_weights[name] for name in weights
    ))
    result["dimension_scores"] = {
        name: json_number(value) for name, value in dimension_scores_exact.items()
    }
    result["raw_overall_score"] = raw
    if veto_count >= 2:
        result.update({"status": "DONE", "verdict": "BLOCK"})
    elif veto_count == 1:
        result.update({
            "status": "DONE_WITH_CONCERNS",
            "verdict": "FIX",
            "cap_applied": True,
            "final_overall_score": min(raw, semantics["veto_ceiling"]),
        })
    else:
        any_fail = any(item["state"] == "fail" for item in normalized.values())
        final = raw
        result.update({
            "status": "DONE" if raw >= 75 and not any_fail else "DONE_WITH_CONCERNS",
            "verdict": "SHIP" if raw >= 75 and not any_fail else "FIX",
            "final_overall_score": final,
        })
    if result.get("verdict") == "SHIP" and result["score_confidence"] == "low":
        result["confidence_caveat"] = (
            "SHIP (low confidence): the evidence mix behind this score is weak; lead "
            "the handoff summary with this caveat and treat the verdict as provisional "
            "until stronger evidence lands."
        )
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default=DEFAULT_CATALOG)
    subparsers = parser.add_subparsers(dest="command", required=True)
    score_parser = subparsers.add_parser("score", help="Score one typed audit run.")
    score_parser.add_argument("run")
    subparsers.add_parser("check-catalog", help="Validate the framework catalog.")
    args = parser.parse_args(argv)
    try:
        catalog = load_json(args.catalog)
        catalog_errors = validate_catalog(catalog)
        if catalog_errors:
            raise RubricError("invalid catalog: " + "; ".join(catalog_errors))
        if args.command == "check-catalog":
            print("framework catalog valid: 8 frameworks")
            return 0
        output = score_run(load_json(args.run), catalog)
    except (RubricError, OverflowError, RecursionError) as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1
    print(exact_json_dumps(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
