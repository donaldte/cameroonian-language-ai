# CLA-Data scripts

```bash
pip install -r data/scripts/requirements.txt
```

- **`ingest_hf_text_dataset.py`** — converts an existing, appropriately-licensed Hugging Face text dataset into CLA-Data text records (`source: "existing_dataset"`). See the script's docstring for the field-mapping CLI options and a worked example (Ghomala' Bandjoun).
- **`validate_records.py`** — validates a JSONL file of text or audio records against the JSON Schemas in [`../schemas/`](../schemas/). Run this on every ingested or collected file before it's merged:
  ```bash
  python3 data/scripts/validate_records.py --kind text --input data/languages/bbj/text/some-file.jsonl
  ```

Both scripts assume the record schemas defined in [`docs/cla-data-schema.md`](../../docs/cla-data-schema.md).
