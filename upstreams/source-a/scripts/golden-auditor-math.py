#!/usr/bin/env python3
"""Behavior-level golden checks for every typed framework profile.

The framework catalog and deterministic scorer are the executable methodology.
This guard deliberately does not scrape formulas or example strings from
Markdown: explanatory prose may change without changing arithmetic, while a
catalog/scorer defect must always fail CI.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "references" / "framework-catalog.json"
SCORER_PATH = ROOT / "scripts" / "rubric-score.py"
SPEC = importlib.util.spec_from_file_location("rubric_score", SCORER_PATH)
SCORER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SCORER)


def evidence():
    return {
        "type": "measured",
        "source": "golden behavior fixture",
        "observed_at": "2026-07-10",
        "confidence": "high",
    }


def complete_run(catalog, framework_name, profile, state="pass"):
    framework = catalog["frameworks"][framework_name]
    items = []
    for item_ids in SCORER.expected_items(framework, profile).values():
        items.extend(
            {"id": item_id, "state": state, "evidence": evidence()}
            for item_id in item_ids
        )
    context = {key: "golden-fixture" for key in framework.get("required_context", [])}
    if framework_name == "STAR":
        context["assessment_time"] = "actual"
    if framework_name == "RAMP":
        context["lifecycle_read"] = profile
    if framework_name == "ECHO":
        context["assessment_mode"] = "asset" if profile == "asset-gate" else "program"
    if framework_name == "TALE":
        context["assessment_mode"] = profile
    context.update(framework["profiles"][profile].get("context_equals", {}))
    return {
        "framework": framework_name,
        "profile": profile,
        "target": "golden-target",
        "observed_at": "2026-07-10",
        "context": context,
        "items": items,
    }


def assert_equal(actual, expected, message, failures):
    if actual == expected:
        print("  ok   " + message)
    else:
        failures.append("%s (expected %r, got %r)" % (message, expected, actual))
        print("FAIL   " + failures[-1])


def main():
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    failures = list(SCORER.validate_catalog(catalog))
    if failures:
        for failure in failures:
            print("FAIL   catalog: " + failure)
        return 1

    print("== Typed profile behavior ==")
    scored = {}
    for framework_name, framework in catalog["frameworks"].items():
        for profile in framework["profiles"]:
            label = "%s/%s" % (framework_name, profile)
            run = complete_run(catalog, framework_name, profile)
            result = SCORER.score_run(run, catalog)
            assert_equal(result["score_state"], "SCORED", label + " complete run is scored", failures)
            assert_equal(result.get("raw_overall_score"), 100, label + " all-pass raw score is 100", failures)
            assert_equal(result.get("final_overall_score"), 100, label + " all-pass final score is 100", failures)
            assert_equal(result["evidence_coverage"], 100, label + " coverage is 100", failures)
            assert_equal(result["verdict"], "SHIP", label + " all-pass verdict is SHIP", failures)
            scored[(framework_name, profile)] = result

            unknown_run = complete_run(catalog, framework_name, profile)
            unknown_run["items"][0] = {
                "id": unknown_run["items"][0]["id"],
                "state": "unknown",
                "reason": "golden missing evidence",
            }
            unknown = SCORER.score_run(unknown_run, catalog)
            assert_equal(unknown["score_state"], "NOT_SCORED", label + " Unknown prevents a total", failures)
            assert_equal(unknown["verdict"], "UNDECIDED", label + " Unknown verdict is UNDECIDED", failures)
            assert_equal("raw_overall_score" in unknown, False, label + " Unknown emits no raw score", failures)

            included = {item["id"] for item in run["items"]}
            vetoes = [item_id for item_id in framework["veto_items"] if item_id in included]
            if vetoes:
                one_veto = complete_run(catalog, framework_name, profile)
                target = next(item for item in one_veto["items"] if item["id"] == vetoes[0])
                target["state"] = "fail"
                capped = SCORER.score_run(one_veto, catalog)
                assert_equal(capped["verdict"], "FIX", label + " one veto yields FIX", failures)
                assert_equal(capped["cap_applied"], True, label + " one veto applies cap", failures)
                if capped.get("final_overall_score", 100) > catalog["semantics"]["veto_ceiling"]:
                    failures.append(label + " one-veto score exceeds universal ceiling")
                    print("FAIL   " + failures[-1])
            if len(vetoes) >= 2:
                two_veto = complete_run(catalog, framework_name, profile)
                for item in two_veto["items"]:
                    if item["id"] in vetoes[:2]:
                        item["state"] = "fail"
                blocked = SCORER.score_run(two_veto, catalog)
                assert_equal(blocked["status"], "DONE", label + " two vetoes complete execution", failures)
                assert_equal(blocked["verdict"], "BLOCK", label + " two vetoes yield BLOCK", failures)
                assert_equal("final_overall_score" in blocked, False, label + " BLOCK emits no final score", failures)

    print("== STAR exact weighting ==")
    exact = complete_run(catalog, "STAR", "awareness")
    for item in exact["items"]:
        if item["id"] == "A10":
            item["state"] = "partial"  # A dimension: 9 pass + 1 partial -> 95
    exact_result = SCORER.score_run(exact, catalog)
    # awareness weights S0.30 T0.20 A0.35 R0.15 -> 100*.65 + 95*.35 = 98.25 -> floor 98
    assert_equal(
        exact_result["raw_overall_score"], 98,
        "STAR exact profile-weighted mean is floored only after dimension rollup", failures,
    )

    print()
    if failures:
        print("GOLDEN BEHAVIOR FAILED: %d issue(s)" % len(failures))
        return 1
    print("All typed framework golden-behavior checks passed (%d profiles)." % len(scored))
    return 0


if __name__ == "__main__":
    sys.exit(main())
