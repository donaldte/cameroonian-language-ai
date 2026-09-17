#!/usr/bin/env python3
"""Validate a CLA-Data JSONL file against its JSON Schema.

Usage:
    python3 validate_records.py --kind text --input data/languages/bbj/text/foo.jsonl
    python3 validate_records.py --kind audio --input data/languages/ewo/speech/foo.jsonl

Exits non-zero if any record fails validation. Prints the first N errors
(default 20) so problems can be fixed without scrolling through thousands
of lines of output.
"""
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "schemas"
SCHEMA_FILES = {
    "text": SCHEMAS_DIR / "text-record.schema.json",
    "audio": SCHEMAS_DIR / "audio-record.schema.json",
    "monolingual": SCHEMAS_DIR / "monolingual-document.schema.json",
    "lexicon": SCHEMAS_DIR / "lexicon-entry.schema.json",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=["text", "audio", "monolingual", "lexicon"], required=True)
    parser.add_argument("--input", required=True, type=Path, help="JSONL file to validate")
    parser.add_argument("--max-errors", type=int, default=20)
    args = parser.parse_args()

    schema = json.loads(SCHEMA_FILES[args.kind].read_text())
    validator = Draft7Validator(schema)

    seen_ids = set()
    total = 0
    error_count = 0
    dup_count = 0

    with args.input.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                error_count += 1
                if error_count <= args.max_errors:
                    print(f"line {line_no}: invalid JSON: {e}")
                continue

            errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
            if errors:
                error_count += 1
                if error_count <= args.max_errors:
                    for err in errors:
                        loc = "/".join(str(p) for p in err.path) or "<root>"
                        print(f"line {line_no} [{record.get('id', '?')}] {loc}: {err.message}")

            rec_id = record.get("id")
            if rec_id in seen_ids:
                dup_count += 1
                print(f"line {line_no}: duplicate id {rec_id}")
            elif rec_id is not None:
                seen_ids.add(rec_id)

    print(f"\n{total} records checked, {error_count} with schema errors, {dup_count} duplicate ids.")
    if error_count > args.max_errors:
        print(f"(only the first {args.max_errors} error groups were printed)")

    if error_count or dup_count:
        sys.exit(1)
    print("OK — all records valid.")


if __name__ == "__main__":
    main()
