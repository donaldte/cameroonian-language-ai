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

CLA-Data has **two license tiers**, distinguished by the `license` field on every record:

- **CC-BY-4.0** — the default for original contributions collected directly from individual contributors (see [§1](#1-what-contributors-are-told-informed-consent)).
- **[CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/)** — for content sourced from institutional partners under a non-commercial-only agreement (e.g. a church/mission organization's existing Bible translation, or a linguistic organization's audio archive). See [§8](#8-partner-sourced-content) below.

Rationale for CC-BY-4.0 as the default: it is the de facto standard for open NLP/speech datasets (Common Voice, Masakhane, FLORES), it maximizes reuse and adoption — including by researchers and companies who might otherwise ignore Cameroonian languages entirely — and it only requires attribution, which is straightforward to give ("CLA — Cameroonian Language AI contributors").

This choice trades away the tighter control a non-commercial or custom license would give the community over downstream commercial use for that tier. Records cannot be retroactively relicensed once published under a given tier — the `license` field on each record is permanent for that record.

## 8. Partner-sourced content

Some CLA-Data content does not come from individual contributors submitting through CLA's own collection process, but from **institutional partners** who hold rights to pre-existing material (a Bible translation, an audio archive, a set of children's books) and have granted CLA permission to publish it, typically on condition that it is **not used commercially**.

Rules specific to this content:

- It is tagged `license: "CC-BY-NC-4.0"` (or whatever more restrictive term the specific partner requires — the exact license string must never be assumed and must be confirmed per partner before ingestion).
- `contributor_id` is `null`; a `source_organization` field (see [`docs/cla-data-schema.md`](cla-data-schema.md)) records which partner it came from.
- `consent_version` records a reference to the partner agreement rather than the individual-contributor consent policy (e.g. `"partner:abc-2026-09"`), so it's always traceable to a specific, documented agreement — not a verbal understanding.
- CLA does not scrape partner content from a website to obtain it, even when a partner has verbally agreed to sharing — a rights-holder's permission does not override a separate technical access control (e.g. bot-detection) that a hosting platform (not the rights holder) has put in place. Content should be obtained as a direct file export from the partner, or via a dataset the partner has already published through a proper channel (e.g. Hugging Face Hub).
- Every partner agreement should be recorded in writing somewhere durable (an email thread, a signed letter, a dataset's own published terms) — not relied upon as a verbal claim alone — before content is ingested and published under this tier.

Partners identified so far (see [`docs/language-landscape.md` § Potential partners](language-landscape.md#-potential-partners-found-during-resource-hunt-2026-09-17)): Alliance Biblique du Cameroun, Global Recordings Network, SIL Cameroun / Bloom Library. Confirming and documenting the exact terms of each agreement is an open item.

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
