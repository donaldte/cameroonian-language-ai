# Ewondo — dataset changelog

## 2026-09-17 — Initial ingestion: `sil-ai/bloom-lm`

- **Source:** [sil-ai/bloom-lm](https://huggingface.co/datasets/sil-ai/bloom-lm) (Hugging Face, gated — requires accepting SIL's access terms).
- **Records ingested:** **1** monolingual document → [`text/sil-ai-bloom-lm.jsonl`](../text/sil-ai-bloom-lm.jsonl), using the new [`monolingual-document.schema.json`](../../../schemas/monolingual-document.schema.json), not the sentence-pair `text-record` schema — this is a whole document (a COVID-19 health pamphlet) with no per-sentence French/English translation, so it doesn't fit the parallel-corpus schema.
- **License:** `CC-BY-NC-SA-4.0` (normalized from the source's `cc-by-nc-sa`; CC version 4.0 is assumed per Bloom Library's default, **not independently confirmed** — see open items). Copyright held by **CABTAL** (Cameroon Association for Bible Translation and Literacy), not SIL itself.
- **Validation status:** `validated: false`.
- **Tooling used:** [`data/scripts/ingest_bloom_lm.py`](../../../scripts/ingest_bloom_lm.py) (reads the dataset's raw JSON files directly via `huggingface_hub`, bypassing bloom-lm's legacy loading script, which modern `datasets` versions refuse to execute) — validated with [`data/scripts/validate_records.py`](../../../scripts/validate_records.py).

### Why only 1 record

bloom-lm's Ewondo coverage across its train/val/test splits totals exactly one document. This was verified directly against the source data, not assumed. Ewondo text/translation coverage otherwise remains an open gap — see [docs/language-landscape.md](../../../../docs/language-landscape.md).

### Open items

- [ ] Confirm the CC license version (assumed 4.0) directly with Bloom Library/CABTAL
- [ ] CC-BY-NC-SA carries a ShareAlike condition — clarify what that implies for any model trained on this text before using it beyond internal experimentation
- [ ] This single document is far too small to be useful alone; treat it as a placeholder pending Alliance Biblique du Cameroun / GRN / government content (see [language-landscape.md § Potential partners](../../../../docs/language-landscape.md#-potential-partners-found-during-resource-hunt-2026-09-17))
