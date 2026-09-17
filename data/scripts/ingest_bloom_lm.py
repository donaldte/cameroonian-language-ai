#!/usr/bin/env python3
"""Ingest sil-ai/bloom-lm documents for CLA's languages into CLA-Data
monolingual-document records (see data/schemas/monolingual-document.schema.json).

bloom-lm is a *gated* Hugging Face dataset (requires accepting SIL's terms
on huggingface.co) and, as of this writing, uses a legacy dataset-loading
script that modern versions of the `datasets` library refuse to execute
(security deprecation). This script therefore bypasses `load_dataset()`
entirely and reads the dataset's raw JSON files directly via
`huggingface_hub.hf_hub_download` — no remote code execution involved.

Each bloom-lm entry is a whole document (a book/story/pamphlet), not a
sentence-level translation pair, and carries its OWN license and copyright
holder (set by the original author on Bloom Library) — these are preserved
per-record, never overwritten with a blanket CLA license.

Usage:
    python3 data/scripts/ingest_bloom_lm.py
"""
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from huggingface_hub import hf_hub_download

CLA_UUID_NAMESPACE = uuid.UUID("a3f1b1c0-6e2a-4b0a-9e2a-3c4d5e6f7a8b")
DATASET_ID = "sil-ai/bloom-lm"
LANGUAGES = ["ewo", "fub"]  # bbj is confirmed absent from this dataset
SPLITS = ["train", "val", "test"]

# Bloom Library's license picker offers Creative Commons licenses; it does
# not appear to record a CC version number in this export. 4.0 is assumed
# (Bloom's current default) but NOT independently verified per document —
# see the changelog this script writes for the open item.
LICENSE_MAP = {
    "cc-by": "CC-BY-4.0",
    "cc-by-nc": "CC-BY-NC-4.0",
    "cc-by-nc-sa": "CC-BY-NC-SA-4.0",
    "cc-by-sa": "CC-BY-SA-4.0",
}

OUT_ROOT = Path(__file__).resolve().parent.parent / "languages"


def make_id(language: str, external_id: str) -> str:
    u = uuid.uuid5(CLA_UUID_NAMESPACE, f"{DATASET_ID}:{external_id}")
    return f"cla_{language}_{u}"


def main():
    created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    source_organization = f"{DATASET_ID} (Hugging Face)"
    consent_version = f"dataset:{DATASET_ID}"

    records_by_lang = {lang: [] for lang in LANGUAGES}
    skipped_licenses = set()

    for split in SPLITS:
        local_path = hf_hub_download(DATASET_ID, f"bloom_lm_{split}.json", repo_type="dataset")
        with open(local_path, encoding="utf-8") as f:
            data = json.load(f)

        for lang in LANGUAGES:
            for entry in data.get(lang, []):
                raw_license = entry.get("license")
                license_norm = LICENSE_MAP.get(raw_license)
                if not license_norm:
                    skipped_licenses.add(raw_license)
                    continue

                external_id = entry.get("bookInstanceId") or entry.get("title")
                record = {
                    "id": make_id(lang, external_id),
                    "language": lang,
                    "title": entry.get("title", ""),
                    "text": entry.get("text", ""),
                    "license": license_norm,
                    "license_raw": raw_license,
                    "copyright_holder": entry.get("copyright", ""),
                    "external_id": external_id,
                    "page_count": entry.get("pageCount"),
                    "source": "existing_dataset",
                    "source_organization": source_organization,
                    "consent_version": consent_version,
                    "validated": False,
                    "validated_by": [],
                    "created_at": created_at,
                }
                records_by_lang[lang].append(record)

    for lang, records in records_by_lang.items():
        out_path = OUT_ROOT / lang / "text" / "sil-ai-bloom-lm.jsonl"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as out:
            for r in records:
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{lang}: wrote {len(records)} records to {out_path}")

    if skipped_licenses:
        print(f"Skipped entries with unrecognized license values: {skipped_licenses}")


if __name__ == "__main__":
    main()
