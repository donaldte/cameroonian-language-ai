#!/usr/bin/env python3
"""Convert a parsed {headword_fr, pos, text} lexicon (JSONL, one sense per
line, in source order) into CLA-Data lexicon-entry records.

Does NOT do any PDF/text extraction itself — that's source-specific
(columns, page layout, etc.) and should be a separate one-off script kept
alongside the source material, outside this repo until its license is
confirmed. This script only does the generic last step: assign ids and
sense_index, attach provenance/license metadata, and validate the shape.

Usage:
    python3 data/scripts/ingest_lexicon.py \\
      --input /path/to/entries.jsonl \\
      --language fub \\
      --source institutional_partner \\
      --source-organization "Urs [surname], via SIL Cameroun (pending written confirmation)" \\
      --license CC-BY-NC-4.0 \\
      --consent-version "partner:urs-sil-2026-09-pending" \\
      --output data/languages/fub/text/urs-lexicon.jsonl

Each input line must be a JSON object with keys: headword_fr, pos, text (or
"fulfulde" as an alias for text).
"""
import argparse
import json
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

CLA_UUID_NAMESPACE = uuid.UUID("a3f1b1c0-6e2a-4b0a-9e2a-3c4d5e6f7a8b")


def make_id(language: str, headword: str, sense_index: int) -> str:
    name = f"lexicon:{headword}:{sense_index}"
    u = uuid.uuid5(CLA_UUID_NAMESPACE, name)
    return f"cla_{language}_{u}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--language", required=True, choices=["fub", "ewo", "bbj"])
    parser.add_argument("--source", required=True, choices=["original", "institutional_partner", "existing_dataset"])
    parser.add_argument("--source-organization", default=None)
    parser.add_argument("--license", required=True, choices=["CC-BY-4.0", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "CC-BY-SA-4.0", "Apache-2.0"])
    parser.add_argument("--consent-version", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    sense_counts = defaultdict(int)
    records = []
    with args.input.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            headword = row["headword_fr"].strip()
            pos = row["pos"].strip()
            text = (row.get("text") or row.get("fulfulde") or "").strip()
            if not text:
                continue
            idx = sense_counts[headword]
            sense_counts[headword] += 1
            records.append({
                "id": make_id(args.language, headword, idx),
                "language": args.language,
                "headword_fr": headword,
                "pos": pos,
                "text": text,
                "sense_index": idx,
                "source": args.source,
                "source_organization": args.source_organization,
                "license": args.license,
                "consent_version": args.consent_version,
                "validated": False,
                "validated_by": [],
                "created_at": created_at,
            })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as out:
        for r in records:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"Wrote {len(records)} lexicon entries ({len(sense_counts)} headwords) to {args.output}")


if __name__ == "__main__":
    main()
