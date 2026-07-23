#!/usr/bin/env python3
"""Validate the public ShieldVault Detection Anthology.

This validator deliberately uses only Python's standard library so it can run
locally and in GitHub Actions without installing dependencies.

It validates corpus structure and safety invariants. It does not execute the
production ShieldVault detector; that integration belongs in the private
product repository.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "anthology" / "cases"
VALID_OUTCOMES = {"STOP", "PAUSE", "ALLOW", "AMBIGUOUS"}
VALID_DOMAINS = {"secret", "behavior"}
ID_PATTERN = re.compile(r"^[A-Z]+-[A-Z0-9-]+-[0-9]{4}$")

# These patterns are intentionally conservative. A match is only an error when
# the surrounding fixture lacks an obvious synthetic marker.
POTENTIAL_LIVE_SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access-key style": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token style": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "Slack token style": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
}
SAFE_MARKERS = {
    "SHIELDVAULT",
    "SYNTHETIC",
    "FAKE",
    "TEST",
    "REDACTED",
    "EXAMPLE",
    "INVALID",
    "000000",
    "4242 4242 4242 4242",
}


def fail(errors: list[str], location: str, message: str) -> None:
    errors.append(f"{location}: {message}")


def require_nonempty_string(
    case: dict[str, Any], field: str, errors: list[str], location: str
) -> None:
    value = case.get(field)
    if not isinstance(value, str) or not value.strip():
        fail(errors, location, f"'{field}' must be a non-empty string")


def validate_case(
    case: Any,
    location: str,
    seen_ids: set[str],
    errors: list[str],
) -> tuple[str | None, str | None]:
    if not isinstance(case, dict):
        fail(errors, location, "case must be a JSON object")
        return None, None

    for field in ("id", "domain", "category", "text", "expected", "reason"):
        require_nonempty_string(case, field, errors, location)

    case_id = case.get("id")
    if isinstance(case_id, str):
        if not ID_PATTERN.fullmatch(case_id):
            fail(errors, location, f"invalid case ID format: {case_id!r}")
        if case_id in seen_ids:
            fail(errors, location, f"duplicate case ID: {case_id}")
        seen_ids.add(case_id)

    domain = case.get("domain")
    if domain not in VALID_DOMAINS:
        fail(errors, location, f"domain must be one of {sorted(VALID_DOMAINS)}")

    expected = case.get("expected")
    if expected not in VALID_OUTCOMES:
        fail(errors, location, f"expected must be one of {sorted(VALID_OUTCOMES)}")

    if case.get("synthetic") is not True:
        fail(errors, location, "synthetic must be exactly true")

    acceptable = case.get("acceptable", [])
    if not isinstance(acceptable, list):
        fail(errors, location, "acceptable must be an array when present")
        acceptable = []
    else:
        invalid = set(acceptable) - VALID_OUTCOMES
        if invalid:
            fail(errors, location, f"acceptable contains invalid outcomes: {sorted(invalid)}")
        if len(acceptable) != len(set(acceptable)):
            fail(errors, location, "acceptable contains duplicate outcomes")
        if acceptable and expected not in acceptable:
            fail(errors, location, "acceptable must include the expected outcome")

    must_not = case.get("must_not", [])
    if not isinstance(must_not, list):
        fail(errors, location, "must_not must be an array when present")
        must_not = []
    else:
        invalid = set(must_not) - VALID_OUTCOMES
        if invalid:
            fail(errors, location, f"must_not contains invalid outcomes: {sorted(invalid)}")
        if len(must_not) != len(set(must_not)):
            fail(errors, location, "must_not contains duplicate outcomes")

    permitted = set(acceptable) if acceptable else ({expected} if expected else set())
    overlap = permitted.intersection(must_not)
    if overlap:
        fail(errors, location, f"outcomes cannot be both permitted and prohibited: {sorted(overlap)}")

    if domain == "secret" and expected in {"PAUSE", "AMBIGUOUS"}:
        fail(errors, location, "secret cases must use objective STOP or ALLOW expectations")

    if domain == "behavior" and expected == "STOP":
        fail(errors, location, "behavioral cases may not require a hard STOP")

    text = case.get("text")
    if isinstance(text, str):
        upper_text = text.upper()
        has_safe_marker = any(marker in upper_text for marker in SAFE_MARKERS)
        for label, pattern in POTENTIAL_LIVE_SECRET_PATTERNS.items():
            if pattern.search(text) and not has_safe_marker:
                fail(
                    errors,
                    location,
                    f"possible live {label}; replace it with an unmistakably synthetic fixture",
                )

    tags = case.get("tags", [])
    if not isinstance(tags, list) or any(
        not isinstance(tag, str) or not tag.strip() for tag in tags
    ):
        fail(errors, location, "tags must be an array of non-empty strings")

    return domain if isinstance(domain, str) else None, expected if isinstance(expected, str) else None


def validate_file(
    path: Path,
    seen_ids: set[str],
    errors: list[str],
) -> tuple[int, dict[str, int], dict[str, int]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, str(path.relative_to(ROOT)), f"cannot read valid JSON: {exc}")
        return 0, {}, {}

    location = str(path.relative_to(ROOT))
    if not isinstance(payload, dict):
        fail(errors, location, "top-level value must be a JSON object")
        return 0, {}, {}

    if payload.get("schema_version") != "1.0":
        fail(errors, location, "schema_version must be '1.0'")

    if not isinstance(payload.get("collection"), str) or not payload["collection"].strip():
        fail(errors, location, "collection must be a non-empty string")

    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(errors, location, "cases must be a non-empty array")
        return 0, {}, {}

    domains: dict[str, int] = {}
    outcomes: dict[str, int] = {}
    for index, case in enumerate(cases):
        domain, expected = validate_case(
            case,
            f"{location}#cases[{index}]",
            seen_ids,
            errors,
        )
        if domain:
            domains[domain] = domains.get(domain, 0) + 1
        if expected:
            outcomes[expected] = outcomes.get(expected, 0) + 1

    return len(cases), domains, outcomes


def main() -> int:
    errors: list[str] = []
    seen_ids: set[str] = set()
    total = 0
    domain_counts: dict[str, int] = {}
    outcome_counts: dict[str, int] = {}

    files = sorted(CASES_DIR.glob("*.json"))
    if not files:
        print(f"ERROR: no anthology case files found in {CASES_DIR}", file=sys.stderr)
        return 1

    for path in files:
        count, domains, outcomes = validate_file(path, seen_ids, errors)
        total += count
        for key, value in domains.items():
            domain_counts[key] = domain_counts.get(key, 0) + value
        for key, value in outcomes.items():
            outcome_counts[key] = outcome_counts.get(key, 0) + value

    if errors:
        print("ShieldVault Detection Anthology validation FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("ShieldVault Detection Anthology validation PASSED")
    print(f"Files: {len(files)}")
    print(f"Cases: {total}")
    print("Domains: " + ", ".join(f"{k}={v}" for k, v in sorted(domain_counts.items())))
    print("Expected outcomes: " + ", ".join(f"{k}={v}" for k, v in sorted(outcome_counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
