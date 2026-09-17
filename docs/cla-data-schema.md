# 📐 CLA-Data v0.1 — Schema Specification

> **Status:** Draft v0.1 — Phase 1 (CLA-Data)
> **Applies to:** Fulfulde (`fub`), Ewondo (`ewo`), Ghomala' Bandjoun (`bbj`) — see [`docs/language-landscape.md`](language-landscape.md)

This document defines the record formats every CLA dataset must follow. The goals are the same for every language and every modality: **reproducible, versioned, attributable, and machine-validatable** data.

Machine-readable versions of these schemas live in [`data/schemas/`](../data/schemas/) as JSON Schema files, so any ingestion or validation script can check a record against them automatically.

No data has been collected under this schema yet. See [`docs/data-consent-and-licensing.md`](data-consent-and-licensing.md) for the policy that must be in place, and agreed to by each contributor, before collection starts.

---

## Language codes

CLA uses **ISO 639-3** codes as the canonical language identifier in every record and directory name:

| Code | Language |
|---|---|
| `fub` | Fulfulde (Adamawa) |
| `ewo` | Ewondo |
| `bbj` | Ghomala' (Bandjoun) |

## Common fields

These fields appear, with the same meaning, in both the text and audio schemas:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | ✅ | Unique record ID, format `cla_{lang}_{uuid4}` (e.g. `cla_bbj_3f2a1c9e-...`) |
| `language` | string (enum) | ✅ | One of the ISO 639-3 codes above |
| `source` | string (enum) | ✅ | How the content originated — see [Source values](#source-values) |
| `license` | string (enum) | ✅ | `"CC-BY-4.0"` for individual contributions, `"CC-BY-NC-4.0"` for institutional partner content (see [licensing policy §2, §8](data-consent-and-licensing.md#2-license)) |
| `consent_version` | string | ✅ | Version of the consent policy the contributor agreed to (e.g. `"v1.0"`), or a partner-agreement reference (e.g. `"partner:abc-2026-09"`) for `institutional_partner` records |
| `contributor_id` | string \| null | ✅ | Pseudonymous ID of the contributor who submitted the record. Never a real name — see consent policy. `null` for `institutional_partner` records |
| `source_organization` | string \| null | ⛔ required when `source` is `institutional_partner`, `null` otherwise | Name of the institutional partner the record came from (e.g. `"Alliance Biblique du Cameroun"`) |
| `speaker_id` | string \| null | ⛔ optional | Pseudonymous ID of the *speaker*, if different from the contributor (e.g. someone transcribing another person's speech) |
| `validated` | boolean | ✅ | `true` only once the record has passed [validation](#validation) |
| `validated_by` | array of strings | ✅ | Pseudonymous IDs of validators who reviewed this record (empty until validated) |
| `created_at` | string (ISO 8601) | ✅ | Submission timestamp, UTC |

### Source values

`original` (contributor wrote/said it themselves) · `elicited` (produced in response to a CLA prompt) · `translated_from_existing` (translation of an existing public-domain or appropriately licensed text) · `public_domain_text` (verbatim public-domain text, e.g. out-of-copyright literature) · `institutional_partner` (content obtained directly from a partner organization under a documented agreement — see [data-consent-and-licensing.md §8](data-consent-and-licensing.md#8-partner-sourced-content), never scraped from a partner's website) — any other source must be documented in an issue before use.

---

## Text record schema

```json
{
  "id": "cla_bbj_3f2a1c9e-4b7a-4e9a-9d3a-1a2b3c4d5e6f",
  "language": "bbj",
  "text": "Original sentence in the source language.",
  "translation_fr": "Traduction française.",
  "translation_en": "English translation.",
  "source": "elicited",
  "license": "CC-BY-4.0",
  "consent_version": "v1.0",
  "contributor_id": "contrib_0042",
  "source_organization": null,
  "speaker_id": null,
  "validated": false,
  "validated_by": [],
  "created_at": "2026-09-17T12:00:00Z"
}
```

Additional required fields beyond the [common fields](#common-fields):

| Field | Type | Required | Description |
|---|---|---|---|
| `text` | string | ✅ | The sentence/utterance in the target Cameroonian language |
| `translation_fr` | string \| null | ⚠️ at least one of `translation_fr`/`translation_en` required | French translation |
| `translation_en` | string \| null | ⚠️ at least one of `translation_fr`/`translation_en` required | English translation |

Full JSON Schema: [`data/schemas/text-record.schema.json`](../data/schemas/text-record.schema.json)

---

## Audio record schema

```json
{
  "id": "cla_ewo_9c1d2e3f-...",
  "language": "ewo",
  "audio_path": "audio/ewo/000001.wav",
  "transcription": "Transcription of what was said, in the target language.",
  "translation_fr": "Traduction française.",
  "translation_en": "English translation.",
  "duration_sec": 4.8,
  "sample_rate": 16000,
  "source": "read_speech",
  "license": "CC-BY-4.0",
  "consent_version": "v1.0",
  "contributor_id": "contrib_0017",
  "source_organization": null,
  "speaker_id": "contrib_0017",
  "speaker_demographics": {
    "age_range": "25-34",
    "gender": null,
    "region": "Centre"
  },
  "validated": false,
  "validated_by": [],
  "created_at": "2026-09-17T12:00:00Z"
}
```

Additional required fields beyond the [common fields](#common-fields):

| Field | Type | Required | Description |
|---|---|---|---|
| `audio_path` | string | ✅ | Relative path to the `.wav` file under the language's `speech/` directory |
| `transcription` | string | ✅ | Exact transcription of the audio in the target language |
| `translation_fr` / `translation_en` | string \| null | ⚠️ at least one required | Translations of the transcription |
| `duration_sec` | number | ✅ | Audio duration in seconds |
| `sample_rate` | integer | ✅ | Must be `16000` Hz (CLA v0.1 standard — mono, 16-bit PCM WAV) |
| `speaker_demographics` | object \| null | ⛔ optional, **opt-in only** | Self-reported, coarse-grained demographics. Every sub-field is individually optional and must never be inferable back to a real identity — see consent policy |
| `source` (audio-specific values) | string (enum) | ✅ | `read_speech` (contributor read a provided sentence) · `spontaneous` (free/natural speech) · `elicited` (responded to a prompt) |

Full JSON Schema: [`data/schemas/audio-record.schema.json`](../data/schemas/audio-record.schema.json)

**Audio format standard:** mono WAV, 16-bit PCM, 16kHz sample rate. This matches common ASR training pipelines (e.g. Whisper, wav2vec2) and keeps file sizes manageable for a community-driven, low-bandwidth collection effort.

---

## Validation

A record becomes `"validated": true` only once **at least two independent native-speaker validators**, other than the original contributor, confirm that:

- the transcription/text is accurate;
- the translation(s) are faithful;
- (audio only) the recording is intelligible and correctly segmented.

Validator IDs are appended to `validated_by`. Disagreements between validators are resolved by a third reviewer; the process and its outcome should be logged (mechanism TBD — tracked as an open item below).

## Dataset splits

To keep [CLA-Bench](../README.md#-cla-bench) meaningful, a fixed portion of validated data per language (target: **15%**, exact split TBD) must be held out as `test`/`benchmark` and never used for model training. This split should be decided and frozen before any model training begins, not after.

## Open items

- [ ] Decide and document the exact train/dev/test split strategy and target sizes
- [ ] Decide the validator-disagreement resolution process
- [ ] Decide where `speaker_demographics` categories come from (self-report free text vs. fixed enums) and who reviews them for re-identification risk
- [ ] Add a `dialect` field once dialectal variation within Fulfulde/Ghomala' is better documented (see [language-landscape.md](language-landscape.md) open items)
