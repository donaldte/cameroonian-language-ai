# CLA-Data

This directory holds CLA's actual datasets, organized per language, plus the machine-readable schemas and scripts used to validate and process them.

**No data has been collected yet.** This structure exists so that collection, when it starts, has a documented home from day one. See:

- [`docs/language-landscape.md`](../docs/language-landscape.md) — why these three languages
- [`docs/cla-data-schema.md`](../docs/cla-data-schema.md) — the record formats (full spec)
- [`docs/data-consent-and-licensing.md`](../docs/data-consent-and-licensing.md) — the policy that must be agreed to by every contributor before their data is collected

## Layout

```text
data/
├── languages/
│   ├── fub/   Fulfulde (Adamawa)
│   ├── ewo/   Ewondo
│   └── bbj/   Ghomala' (Bandjoun)
│       ├── text/       JSONL files of text records (docs/cla-data-schema.md#text-record-schema)
│       ├── speech/     .wav files + JSONL audio records (docs/cla-data-schema.md#audio-record-schema)
│       └── metadata/   Language-level stats: contributor counts, validation logs, dataset changelog
│
├── schemas/    JSON Schema files used to validate every record before it is merged
└── scripts/    Validation / ingestion / export tooling (not yet written)
```

Each language folder uses its **ISO 639-3 code** (`fub`, `ewo`, `bbj`) as the directory name, matching the `language` field in every record — see each language's own `README.md` for the human-readable name and a link to its landscape profile.

## License

All data published here is under **CC-BY-4.0** (see [data-consent-and-licensing.md](../docs/data-consent-and-licensing.md#2-license)). This is different from this repository's code license (Apache-2.0, see [LICENSE](../LICENSE)).
