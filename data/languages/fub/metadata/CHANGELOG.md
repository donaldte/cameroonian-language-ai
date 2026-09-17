# Fulfulde (Adamawa) — dataset changelog

## 2026-09-17 — Initial ingestion: `sil-ai/bloom-lm`

- **Source:** [sil-ai/bloom-lm](https://huggingface.co/datasets/sil-ai/bloom-lm) (Hugging Face, gated — requires accepting SIL's access terms).
- **Records ingested:** **7** monolingual documents → [`text/sil-ai-bloom-lm.jsonl`](../text/sil-ai-bloom-lm.jsonl), using [`monolingual-document.schema.json`](../../../schemas/monolingual-document.schema.json), not the sentence-pair `text-record` schema — these are whole documents (children's stories, a health pamphlet) with no per-sentence French/English translation.
- **Licenses:** mixed per document — `CC-BY-4.0`, `CC-BY-NC-4.0`, and `CC-BY-NC-SA-4.0` (normalized from the source's lowercase forms; CC version 4.0 is assumed per Bloom Library's default, **not independently confirmed**). Copyright held by **CABTAL** (1 document) and the **American University of Nigeria** (6 documents) — not SIL itself.
- **Validation status:** `validated: false` for all 7.
- **Note on language variety:** bloom-lm's `fub` config is intended to correspond to Adamawa Fulfulde, CLA's selected variety — this has not been independently re-verified against the actual text (Fulfulde has many mutually-intelligible-to-varying-degrees varieties; bloom-lm also has a separate `fuh` config for Western Niger Fulfulde which was correctly excluded).
- **Tooling used:** [`data/scripts/ingest_bloom_lm.py`](../../../scripts/ingest_bloom_lm.py) — validated with [`data/scripts/validate_records.py`](../../../scripts/validate_records.py).

### Open items

- [ ] Confirm the CC license version (assumed 4.0) and verify per-document terms directly where possible
- [ ] Verify the `fub` texts are indeed the Adamawa Fulfulde variety spoken in Cameroon and not a related but distinct variety
- [ ] `CC-BY-NC-SA-4.0` (1 of the 7 documents) carries a ShareAlike condition — clarify implications before using it beyond internal experimentation
- [ ] 7 short documents is far too small to be useful alone; treat as a placeholder pending Alliance Biblique du Cameroun / GRN / government content (see [language-landscape.md § Potential partners](../../../../docs/language-landscape.md#-potential-partners-found-during-resource-hunt-2026-09-17))
