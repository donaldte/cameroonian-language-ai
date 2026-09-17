# Ghomala' (Bandjoun) — dataset changelog

## 2026-09-17 — Initial ingestion: `stfotso/french-ghomala-bandjoun`

- **Source:** [stfotso/french-ghomala-bandjoun](https://huggingface.co/datasets/stfotso/french-ghomala-bandjoun) (Hugging Face), an existing, independently published French↔Ghomala' Bandjoun parallel dataset.
- **License:** Apache-2.0, as published by the dataset's author — used as-is (`source: "existing_dataset"`), no CLA consent process applies to this record set (see [docs/data-consent-and-licensing.md](../../../../docs/data-consent-and-licensing.md)).
- **Records ingested:** 15,190 text records → [`text/stfotso-french-ghomala-bandjoun.jsonl`](../text/stfotso-french-ghomala-bandjoun.jsonl)
- **Fields mapped:** `ghomala` → `text`, `francais` → `translation_fr` (no English translation available in the source dataset — `translation_en` is `null` throughout)
- **Validation status:** `validated: false` for every record. Reusing an existing dataset does not substitute for CLA's own native-speaker validation pass (see [docs/cla-data-schema.md § Validation](../../../../docs/cla-data-schema.md#validation)) — this is tracked as an open item.
- **Content mix (observed in samples):** everyday phrases, legal/administrative text (e.g. court proceedings), and what appears to be biblical text (e.g. 1 Corinthians 15:39-style phrasing) — domain diversity not yet formally characterized.
- **Tooling used:** [`data/scripts/ingest_hf_text_dataset.py`](../../../scripts/ingest_hf_text_dataset.py), validated with [`data/scripts/validate_records.py`](../../../scripts/validate_records.py) (0 schema errors, 0 duplicate ids).

### Open items

- [ ] Native-speaker validation pass (2+ validators per record, per the schema's validation policy) before this data is used in any model training or CLA-Bench split
- [ ] Characterize the dataset's domain mix and register/formality more precisely
- [ ] Check for near-duplicate or templated sentences that could inflate apparent dataset size without adding real diversity
- [ ] Decide the train/dev/test split once validation is underway
