#!/usr/bin/env python3
"""Strict front matter quality checks for content pages.

Checks required fields and formatting rules for key content types:
- docs/reading/*.md       -> requires date_read
- docs/syntheses/*.md     -> requires last_updated
- docs/knowledge-base/*.md
- docs/survey/*.md
- docs/strange/*.md

This script is intended for CI and exits non-zero on validation errors.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: str
    required_fields: tuple[str, ...]


RULES: tuple[Rule, ...] = (
    Rule(
        name="Reading Notes",
        pattern="reading/*.md",
        required_fields=("title", "parent", "summary", "tags", "date_read"),
    ),
    Rule(
        name="Syntheses",
        pattern="syntheses/*.md",
        required_fields=("title", "parent", "summary", "tags", "last_updated"),
    ),
    Rule(
        name="Knowledge Base",
        pattern="knowledge-base/*.md",
        required_fields=("title", "parent", "summary", "tags"),
    ),
    Rule(
        name="Surveys",
        pattern="survey/*.md",
        required_fields=("title", "parent", "summary", "tags"),
    ),
    Rule(
        name="Strange",
        pattern="strange/*.md",
        required_fields=("title", "parent", "summary", "tags"),
    ),
)

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def extract_front_matter(file_path: Path):
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "File must start with YAML front matter delimiter ('---')."

    match = re.match(r"^---\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return None, "Front matter block is not closed with a terminating '---'."

    try:
        data = yaml.safe_load(match.group(1))
    except Exception as exc:  # noqa: BLE001
        return None, f"YAML parse error: {exc}"

    if not isinstance(data, dict):
        return None, "Front matter must parse to a YAML mapping (key/value pairs)."

    return data, None


def validate_date(value, field_name: str, issues: list[str]):
    if value is None:
        return
    value_str = str(value).strip()
    if not ISO_DATE_RE.match(value_str):
        issues.append(
            f"'{field_name}' must use YYYY-MM-DD format. Example: {field_name}: 2026-02-22"
        )
        return
    try:
        dt.datetime.strptime(value_str, "%Y-%m-%d")
    except ValueError:
        issues.append(f"'{field_name}' is not a valid calendar date: {value_str}")


def validate_tags(value, issues: list[str]):
    if not isinstance(value, list):
        issues.append("'tags' must be a YAML list. Example: tags: [planning, state-estimation]")
        return
    if not value:
        issues.append("'tags' must contain at least one tag.")
        return
    for tag in value:
        tag_str = str(tag).strip()
        if not TAG_RE.match(tag_str):
            issues.append(
                f"Tag '{tag_str}' is invalid. Use lowercase and hyphenated format, e.g. 'state-estimation'."
            )


def validate_summary(value, issues: list[str]):
    if not isinstance(value, str) or not value.strip():
        issues.append("'summary' must be a non-empty string.")


def iter_rule_files(rule: Rule) -> Iterable[Path]:
    yield from sorted((DOCS / Path(rule.pattern).parent).glob(Path(rule.pattern).name))


def main() -> int:
    all_errors: list[tuple[Path, str, list[str]]] = []
    checked = 0

    for rule in RULES:
        for file_path in iter_rule_files(rule):
            if file_path.name == "view-all.md":
                continue

            checked += 1
            fm, parse_error = extract_front_matter(file_path)
            issues: list[str] = []

            if parse_error:
                issues.append(parse_error)
            else:
                for field in rule.required_fields:
                    if field not in fm:
                        issues.append(f"Missing required field '{field}'.")

                if "summary" in fm:
                    validate_summary(fm.get("summary"), issues)

                if "tags" in fm:
                    validate_tags(fm.get("tags"), issues)

                # Content-specific date checks requested by repo maintainers
                if "date_read" in rule.required_fields:
                    validate_date(fm.get("date_read"), "date_read", issues)
                if "last_updated" in rule.required_fields:
                    validate_date(fm.get("last_updated"), "last_updated", issues)

            if issues:
                all_errors.append((file_path, rule.name, issues))

    if all_errors:
        print("\n❌ Front matter quality checks failed.\n")
        for file_path, rule_name, issues in all_errors:
            rel = file_path.relative_to(ROOT)
            print(f"- {rel} ({rule_name})")
            for issue in issues:
                print(f"  • {issue}")
            print("  Suggested fix: start from the corresponding template in docs/_templates/.\n")

        print(f"Checked {checked} content files. Files with errors: {len(all_errors)}")
        return 1

    print(f"✅ Front matter quality checks passed for {checked} content files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
