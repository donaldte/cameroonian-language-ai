# 🤝 CLA-Data v0.1 — Consent, Licensing & Retention Policy

> **Status:** Draft v0.1 — must be reviewed and, ideally, checked by someone with relevant legal/data-protection expertise before real collection starts. This is a starting point, not a finished legal document.
> **Policy version:** `v1.0` — every record collected under this policy stores this version in its `consent_version` field (see [`docs/cla-data-schema.md`](cla-data-schema.md)), so future changes never retroactively reinterpret what a contributor agreed to.

No text, translation, or audio should be collected from any contributor until this policy is in place and each contributor has explicitly agreed to it.

---

## 1. What contributors are told (informed consent)

Before submitting anything, a contributor must be shown a plain-language notice, in French and English at minimum (and ideally in the target language too), covering:

1. **What CLA is** and what the contribution will be used for: building open datasets, benchmarks, and AI models (speech recognition, translation, language models) for Cameroonian languages.
2. **What is being collected**: the specific text, translation, or audio recording, plus minimal metadata (see [§4](#4-metadata-and-privacy)).
3. **The license**: the contribution will be published under **CC-BY-4.0** (see [§2](#2-license)) — meaning anyone, including companies, may reuse it, as long as CLA is credited.
4. **Who can see it**: validated data will be public; unvalidated/raw data is handled per [§5](#5-storage-and-retention).
5. **Voluntariness**: participation is voluntary, unpaid unless explicitly stated otherwise for a given campaign, and can be withdrawn (see [§6](#6-withdrawal--right-to-be-forgotten)).
6. **No sensitive content**: contributors must not submit content that identifies third parties, contains private/personal information about someone else, or repeats copyrighted material they don't have rights to (unless explicitly public-domain, tagged as `public_domain_text`).
7. **Age requirement**: contributors must be **18 or older**. CLA v0.1 does not collect data from minors — this may be revisited later with appropriate safeguards (parental consent, ethics review) but is out of scope for now.

Consent must be an affirmative action (a checkbox or explicit button), never a default/pre-checked state, and must be re-obtained if the policy materially changes (tracked via `consent_version`).

## 2. License

All CLA-Data contributions are published under **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)**.

Rationale: it is the de facto standard for open NLP/speech datasets (Common Voice, Masakhane, FLORES), it maximizes reuse and adoption — including by researchers and companies who might otherwise ignore Cameroonian languages entirely — and it only requires attribution, which is straightforward to give ("CLA — Cameroonian Language AI contributors").

This choice trades away the tighter control a non-commercial or custom license would give the community over downstream commercial use. If experience shows this is a problem (e.g. a company using CLA-Data with no reciprocity), CLA can introduce a differently-licensed tier for future contributions — but it cannot retroactively relicense data already published as CC-BY-4.0.

Code in this repository remains **Apache-2.0** (see [LICENSE](../LICENSE)); this policy concerns datasets only.

## 3. Attribution

Contributors are attributed collectively as "CLA — Cameroonian Language AI contributors" in any published dataset, unless a contributor explicitly opts in to being named individually (e.g. in a project acknowledgments file). By default, contributors are identified only by a **pseudonymous `contributor_id`** (e.g. `contrib_0042`), never by real name, email, or other directly identifying information, in any published record.

## 4. Metadata and privacy

- `speaker_demographics` (age range, gender, region) is **entirely optional and opt-in**, coarse-grained, and must never be combined in a way that could re-identify a specific person (e.g. "only Fulfulde speaker from village X, age 70-80" is too specific — categories should be broad enough to protect anonymity).
- Audio recordings are voices, which are themselves potentially identifying. Contributors must be told this explicitly, separately from the general text-data notice.
- No collection of names, phone numbers, exact addresses, national ID numbers, or similar direct identifiers, under any circumstance.
- Free-text fields (`text`, `transcription`) are subject to basic PII screening before validation (a validator flags and removes/redacts any record that inadvertently names a third party or contains private information).

## 5. Storage and retention

- **Raw, unvalidated submissions** are kept in a restricted-access holding area until validated or rejected. Target: resolve within a documented review window (TBD — see open items).
- **Rejected submissions** (failed validation, policy violation, or a withdrawal request) are deleted, not archived indefinitely.
- **Validated data** is published (e.g. via GitHub and/or Hugging Face Hub) under CC-BY-4.0 and is, by design, then outside CLA's exclusive control — anyone can have already downloaded and redistributed a public dataset. This must be made unmistakably clear to contributors before they submit (see [§6](#6-withdrawal--right-to-be-forgotten)).

## 6. Withdrawal / right to be forgotten

A contributor may request removal of their contribution at any time by contacting the project (mechanism TBD — tracked as an open item) and referencing their `contributor_id`.

- If the record has **not yet been published** (still in the raw/validation holding area), it is deleted outright.
- If the record **has already been published** under CC-BY-4.0, CLA will remove it from CLA's own future dataset releases and from any CLA-controlled hosting, but **cannot retract copies already downloaded or redistributed by third parties**, nor unlearn it from any model already trained on a prior release. This limitation must be stated plainly in the consent notice (§1), not discovered later.

## 7. Governance of this policy

This policy is versioned (`v1.0` and up). Material changes (e.g. changing the license, changing what demographic data is collected) require a new version number and do not apply retroactively to already-collected `consent_version` values. Proposed changes should go through a GitHub issue for discussion, consistent with [CONTRIBUTING.md](../CONTRIBUTING.md).

## Open items

- [ ] Define the exact contact mechanism for withdrawal requests (dedicated email? issue template? form?)
- [ ] Define the raw-submission review window (how long unvalidated data sits before validation or deletion)
- [ ] Get this policy reviewed by someone with data-protection/legal background, ideally familiar with Cameroonian law, before real collection begins
- [ ] Decide whether/how to support a future, more restrictive license tier for contributors who want tighter control
- [ ] Translate the consent notice into Fulfulde, Ewondo, and Ghomala' (Bandjoun) themselves, not just French/English
