#!/usr/bin/env python3
"""Convert an existing, appropriately-licensed Hugging Face text dataset
into CLA-Data text records (see docs/cla-data-schema.md).

This is for source="existing_dataset" ingestion only — i.e. a dataset that
is *already* published under a license CLA can reuse (Apache-2.0, CC-BY,
CC-BY-NC, etc.), as opposed to data collected directly from individual
contributors (source="original"/"elicited", license CC-BY-4.0) or obtained
from an institutional partner under a private agreement
(source="institutional_partner", license CC-BY-NC-4.0 — see
docs/data-consent-and-licensing.md §8).

Every record gets validated == false: reuse of an existing dataset does
not substitute for CLA's own native-speaker validation pass.

Example (Ghomala' Bandjoun, 2026-09):
    python3 data/scripts/ingest_hf_text_dataset.py \\
      --dataset stfotso/french-ghomala-bandjoun \\
      --language bbj \\
      --text-field ghomala \\
      --translation-fr-field francais \\
      --license Apache-2.0 \\
      --output data/languages/bbj/text/stfotso-french-ghomala-bandjoun.jsonl
"""
import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from datasets import load_dataset

# Fixed namespace so re-running this script for the same dataset regenerates
# the same ids (idempotent), instead of minting new UUIDs every run.
CLA_UUID_NAMESPACE = uuid.UUID("a3f1b1c0-6e2a-4b0a-9e2a-3c4d5e6f7a8b")


def make_id(language: str, dataset: str, index: int) -> str:
    name = f"{dataset}:{index}"
    u = uuid.uuid5(CLA_UUID_NAMESPACE, name)
    return f"cla_{language}_{u}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dataset", required=True, help="Hugging Face dataset id, e.g. stfotso/french-ghomala-bandjoun")
    parser.add_argument("--config", default=None, help="Dataset config name, if the dataset has one (e.g. a language code)")
    parser.add_argument("--split", default="train")
    parser.add_argument("--language", required=True, help="CLA ISO 639-3 code: fub, ewo, or bbj")
    parser.add_argument("--text-field", required=True, help="Field in the HF dataset holding the target-language text")
    parser.add_argument("--translation-fr-field", default=None)
    parser.add_argument("--translation-en-field", default=None)
    parser.add_argument("--license", required=True, choices=["CC-BY-4.0", "CC-BY-NC-4.0", "Apache-2.0"])
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    if not args.translation_fr_field and not args.translation_en_field:
        parser.error("at least one of --translation-fr-field / --translation-en-field is required")

    ds = load_dataset(args.dataset, args.config) if args.config else load_dataset(args.dataset)
    split = ds[args.split]

    created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source_organization = f"{args.dataset} (Hugging Face)"
    consent_version = f"dataset:{args.dataset}"

    args.output.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped = 0
    with args.output.open("w", encoding="utf-8") as out:
        for i, row in enumerate(split):
            text = (row.get(args.text_field) or "").strip()
            translation_fr = (row.get(args.translation_fr_field) or "").strip() if args.translation_fr_field else None
            translation_en = (row.get(args.translation_en_field) or "").strip() if args.translation_en_field else None

            if not text or not (translation_fr or translation_en):
                skipped += 1
                continue

            record = {
                "id": make_id(args.language, args.dataset, i),
                "language": args.language,
                "text": text,
                "translation_fr": translation_fr or None,
                "translation_en": translation_en or None,
                "source": "existing_dataset",
                "license": args.license,
                "consent_version": consent_version,
                "contributor_id": None,
                "source_organization": source_organization,
                "speaker_id": None,
                "validated": False,
                "validated_by": [],
                "created_at": created_at,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

    print(f"Wrote {written} records to {args.output} ({skipped} skipped for missing text/translation).")


if __name__ == "__main__":
    main()
