# 🌍 CLA Language Landscape 2026

> **Status:** Draft v0.1 — Phase 0 (Research & Community)
> **Purpose:** Document what already exists for Cameroon's languages before CLA collects a single sentence, and justify the selection of CLA's first three working languages.

This document is the first deliverable of CLA v0.1. It does two things:

1. Surveys **10 candidate languages** across the dimensions that matter for building datasets, benchmarks, and models (speakers, writing system, existing corpora, audio, translations, Hugging Face resources, ASR/MT models, academic research).
2. Justifies the **selection of CLA's first three languages**.

Nothing here is final. Numbers for Cameroonian languages are notoriously inconsistent across sources (last census-quality sociolinguistic survey for most of them dates back to the 1980s–2000s), so every figure below is cited and should be treated as an estimate, not ground truth. Corrections from native speakers and linguists are explicitly welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).

---

## ⚠️ An important caveat: Cameroonian Pidgin English (Kamtok)

Before ranking indigenous languages, one fact needs to be on the table: **Cameroonian Pidgin English (Kamtok)** is very likely the single most widely spoken language in Cameroon in practice — an English-lexified creole used by an estimated **~12 million people** to some degree, with roughly **50% of the population** using it as a lingua franca (native speakers are a small minority, ~5%) ([Wikipedia](https://en.wikipedia.org/wiki/Cameroonian_Pidgin_English)).

CLA is **not** selecting Kamtok as one of its first three languages, for two reasons:

- CLA's mission (see [README](../README.md)) is specifically about **underrepresented indigenous Cameroonian languages** — the ones at real risk of being left out of digital life entirely. Kamtok, as an English-lexified creole, already benefits indirectly from English NLP tooling and has existing translation/research attention (APiCS, dedicated Pidgin-English translation tools).
- The founder's brief for CLA v0.1 fixed **Ghomala' (Bandjoun)** as a required language and asked for the **two most spoken indigenous languages of Cameroon** as the other two.

This is a judgment call, not a hidden fact — it's documented here so it can be revisited. Kamtok remains a strong **CLA v0.2+ candidate** given its reach.

---

## 📋 Candidate languages overview

Ten candidate languages were surveyed, chosen for combining high speaker counts, regional diversity (north/center/west/littoral), and at least some existing documentation.

| Language | ISO 639-3 | Region | L1 speakers (approx.) | L2 / total users | Writing system | Status |
|---|---|---|---|---|---|---|
| **Fulfulde (Adamawa)** | `fub` | Adamawa, North, Far North | ~2.5M (CM, 2019) | ~5.18M total users in Cameroon (2019) | Latin (Ajami historically) | **Selected** |
| **Ewondo** | `ewo` | Centre (Yaoundé) | ~578k (1982 figure, likely outdated) | Dominant lingua franca of Yaoundé metro area | Latin | **Selected** |
| **Ghomala' (Bandjoun)** | `bbj` | West (Bandjoun) | ~1.1M–2M (estimates vary) | Major Bamileke vehicular variety | Latin (general Cameroon alphabet) | **Selected** |
| Bulu | `bum` | South | ~858k (2007) | ~800k L2 | Latin | Candidate |
| Duala | `dua` | Littoral (Douala) | ~87.7k (1982, likely outdated) | Historic vehicular language of Douala | Latin | Candidate |
| Basaa (Bassa) | `bas` | Centre, Littoral | ~230k–300k | — | Latin | Candidate |
| Bamum (Shupamom) | `bax` | West (Foumban) | ~600k–700k (2025 est.) | — | Latin *and* the historic Bamum syllabary | Candidate |
| Medumba | `byv` | West (Bangangté) | ~210k–215k | — | Latin (5+ orthographies proposed historically) | Candidate |
| Yemba (Bamiléké-Dschang) | `ybb` | West (Dschang) | ~500k (2023 est.) | — | Latin + IPA-based tone marking | Candidate |
| Ngiemboon | `nnh` | West (Bamboutos) | ~250k (2007) | — | Latin, General Alphabet of Cameroon Languages | Candidate |

Sources for this table are listed in [References](#-references) below.

---

## 🔍 Detailed profiles — selected languages

### 🥇 Fulfulde (Adamawa Fulfulde) — `fub`

```text
Fulfulde (Adamawa)
├── Speakers: ~2.5M L1 in Cameroon, ~5.18M total users (Ethnologue, 2019)
├── Writing system: Latin script (official orthography); historical Ajami (Arabic-based)
├── Existing dictionaries: Fulfulde-French lexicons (SIL, missionary sources)
├── Existing text corpora: Religious texts (Bible translations), SIL Cameroon materials
├── Existing audio datasets: Known crowdsourced oral-data collection efforts targeting
│                            Fulfulde speakers in Adamawa/Far North (early-stage, not yet public)
├── Existing translation datasets: None found as a public, structured parallel corpus
├── Hugging Face datasets: None specific to Cameroonian Adamawa Fulfulde (`fub`) found;
│                          NLLB-200 / FLORES-200 support "Fulah" but under codes tied to
│                          Nigerian/West African Fulfulde varieties (`fuv`), not confirmed
│                          equivalent to `fub` — needs verification before reuse
├── Existing ASR models: None found publicly for `fub`
├── Existing translation models: Possibly usable as a starting point via NLLB `fuv_Latn`,
│                                 but linguistic distance to Adamawa Fulfulde is unverified
└── Existing academic research: Referenced in UNESCO World Atlas of Languages (WAL) profile
```

**Why it matters:** Fulfulde is the largest indigenous language of Cameroon by a wide margin and the primary lingua franca of the three northern regions, spoken across borders in Nigeria, Chad, and CAR. It is linguistically very different from the two others selected (Niger-Congo, Atlantic branch, vs. Bantu/Grassfields for the other two), which is valuable for testing that CLA's tools generalize.

### 🥈 Ewondo — `ewo`

```text
Ewondo
├── Speakers: ~578k L1 (1982 census figure — outdated; Yaoundé metro area alone has grown
│             to several million since, and Ewondo is its dominant vehicular language)
├── Writing system: Latin script, standardized orthography used in Beti-Pahuin literature
├── Existing dictionaries: Ewondo-French dictionaries (Catholic mission tradition, 20th c.)
├── Existing text corpora: Religious texts, some literary works, Beti-Pahuin linguistic studies
├── Existing audio datasets: Reported oral-data collection initiative including Ewondo
│                            speakers from the Centre region (early-stage, not yet public)
├── Existing translation datasets: None found as a public, structured parallel corpus
├── Hugging Face datasets: None found
├── Existing ASR models: None found publicly
├── Existing translation models: None found publicly
└── Existing academic research: Covered in Beti-Pahuin linguistics literature; cited in
                                 G. Echu's "The Language Question in Cameroon"
```

**Why it matters:** Ewondo's raw native-speaker count looks smaller than Bulu's on paper, but its role as the everyday vehicular language of Yaoundé — Cameroon's capital and one of its two largest metro areas — gives it outsized real-world reach and makes it a strong choice for a demo-ready assistant. This was the deciding factor over Bulu for CLA's second language (see [Selection Rationale](#-selection-rationale)).

### 🥉 Ghomala' (Bandjoun) — `bbj`

```text
Ghomala'
├── Speakers: estimates range from ~1.1M to ~2M across all Ghomala'-speaking areas
│             (Bandjoun, Bansoa, Bameka and related Bamileke chiefdoms); estimates vary
│             sharply by source — needs a dedicated verification pass
├── Writing system: Latin script, General Alphabet of Cameroon Languages (tone-marked)
├── Existing dictionaries: SIL/linguistic documentation referenced via Glottolog and OLAC;
│                          full dictionary status needs direct verification (no confirmed
│                          public Webonary page found during this pass)
├── Existing text corpora: Limited; promoted under Cameroon's Ministry of Education
│                          "Read at Home" initiative as one of five national languages
├── Existing audio datasets: None found publicly
├── Existing translation datasets: None found publicly
├── Hugging Face datasets: None found
├── Existing ASR models: None found publicly
├── Existing translation models: None found publicly
└── Existing academic research: Documented in Glottolog (ghom1247) and OLAC language
                                 archive records
```

**Why it matters:** Ghomala' (specifically the Bandjoun variety) is the founder's required language for CLA — it anchors the project in the Bamileke/Grassfields language family (West Region), the most linguistically dense and commercially dynamic part of Cameroon, and is essentially undocumented in existing NLP resources, which is exactly the gap CLA exists to close.

---

## 🔎 Detailed profiles — other candidates (compact)

| | Bulu | Duala | Basaa | Bamum | Medumba | Yemba | Ngiemboon |
|---|---|---|---|---|---|---|---|
| Dictionaries | Bulu-English-French-German dict. on [Webonary](https://www.webonary.org/bulu/) ✅ | Long written tradition (Bible since 19th c.) | Basaa-French dictionaries exist | Documented via Bamum script scholarship (Library of Congress) | Multiple historical orthographies (missionary, 1926+) | Yemba-French dictionary (Tadadjeu & Bird, 3,000+ words) ✅ | SIL documentation exists |
| Audio/ASR/MT datasets | None found public | None found public | None found public | None found public | None found public | None found public | None found public |
| HF datasets | None found | None found | None found | None found | None found | None found | None found |
| Distinguishing feature | Beti-Pahuin, close to Ewondo, higher raw L1 count | Historic coastal lingua franca, small L1 base today | Moderate L1 base, Centre/Littoral | **Unique historic Bamum syllabary** — interesting for OCR/script-preservation work | Long orthography history (6 systems) — interesting case study | Deepest tone-orthography documentation (90 years) | Governed by the General Alphabet of Cameroon Languages |

None of these seven show evidence of an existing public dataset, ASR model, or MT model as of this research pass (September 2026). This should be re-verified directly (Hugging Face Hub search, Google Scholar, ACL Anthology) before being treated as fact — search-engine coverage of Cameroonian-language NLP work is thin and academic papers may not surface easily.

---

## 🧭 Selection criteria

Languages were (and should continue to be) evaluated against:

| Criterion | Fulfulde | Ewondo | Ghomala' (Bandjoun) |
|---|---|---|---|
| Speaker availability for contribution | ✅ Very high, spread across 3 regions | ✅ High, concentrated in Yaoundé (easy to recruit) | ✅ High, concentrated in West Region |
| Orthography standardization | ✅ Standardized Latin | ✅ Standardized Latin | ⚠️ Latin + tone marking, less consistently used day-to-day |
| Existing resources to build on | ⚠️ Thin, but some mission/UNESCO documentation | ⚠️ Thin | ⚠️ Very thin |
| Linguistic diversity from the other two | ✅ Atlantic (Niger-Congo), very distinct | Bantu (Beti-Pahuin) | Grassfields Bantu — distinct from Ewondo, tests generalization |
| Founder requirement | — | — | ✅ Fixed requirement |
| Feasibility of responsible collection | Requires Fulfulde-speaking community partners in the North | Easiest — Yaoundé is CLA's likely home base | Requires West-Region community partners (Bandjoun) |

---

## ✅ Selection rationale — CLA v0.1's three languages

**CLA v0.1 will target: Fulfulde (Adamawa) · Ewondo · Ghomala' (Bandjoun).**

- **Fulfulde** — the most spoken indigenous language of Cameroon by a wide margin, and linguistically the most distinct from the other two (Atlantic vs. Bantu/Grassfields), which stress-tests CLA's tooling against real diversity rather than three similar Bantu languages.
- **Ewondo** — chosen over Bulu (which has a higher raw native-speaker count on paper) because Ewondo is the dominant everyday vehicular language of Yaoundé, Cameroon's capital and one of its largest urban areas; its practical reach today is almost certainly larger than the 1982 census figure suggests, and it offers the easiest path to recruiting contributors and running a public demo.
- **Ghomala' (Bandjoun)** — fixed as a project requirement; also independently justified as a Grassfields/Bamileke representative from the West Region, a linguistically rich and economically dynamic part of the country that is essentially absent from existing NLP resources.

Together these three span three different regions (North, Centre, West), three different language families/branches, and — combined — a native-speaker base of several million people, while keeping the initial scope to a manageable three languages per the "don't try to support 250 languages on day one" principle.

**Open item:** the exact Ghomala' speaker count (1.1M vs 2M depending on source) and the state of any existing Ghomala' dictionary/corpus should be verified directly with West Region linguists or SIL Cameroon contacts before CLA-Data v0.1 collection design is finalized.

---

## 📚 References

- [Ethnologue — Fulfulde, Adamawa (fub)](https://www.ethnologue.com/language/fub/)
- [Wikipedia — Adamawa Fulfulde](https://en.wikipedia.org/wiki/Adamawa_Fulfulde)
- [UNESCO WAL — Adamawa Fulfulde in Cameroon](https://en.wal.unesco.org/countries/cameroon/languages/adamawa-fulfulde)
- [Wikipedia — Ewondo language](https://en.wikipedia.org/wiki/Ewondo_language)
- [G. Echu — The Language Question in Cameroon](https://bop.unibe.ch/linguistik-online/article/download/765/1309)
- [Wikipedia — Ghomala' language](https://en.wikipedia.org/wiki/Ghomala%CA%BC_language)
- [Glottolog — Ghomálá'](https://glottolog.org/resource/languoid/id/ghom1247)
- [OLAC — resources in and about Ghomálá'](http://www.language-archives.org/language/bbj)
- [UNESCO WAL — Ghomálá' in Cameroon](https://en.wal.unesco.org/countries/cameroon/languages/ghomala)
- [Wikipedia — Bulu language](https://en.wikipedia.org/wiki/Bulu_language)
- [Webonary — Bulu-English-French-German dictionary](https://www.webonary.org/bulu/overview/introduction/?lang=en)
- [Wikipedia — Duala language](https://en.wikipedia.org/wiki/Duala_language)
- [Wikipedia — Bassa (Basaa) language](https://en.wikipedia.org/wiki/Bassa_language)
- [Wikipedia — Bamum language](https://en.wikipedia.org/wiki/Bamum_language)
- [Library of Congress — About Bamum Script](https://guides.loc.gov/bamum-script/bamum-script)
- [Wikipedia — Medumba language](https://en.wikipedia.org/wiki/Medumba_language)
- [Wikipedia — Yemba language](https://en.wikipedia.org/wiki/Yemba_language)
- [Academia.edu — The Yemba Language (Cameroon): 90 Years of Tone Orthography](https://www.academia.edu/27942444/The_Yemba_Language_Cameroon_90_Years_of_Tone_Orthography)
- [Wikipedia — Ngiemboon language](https://en.wikipedia.org/wiki/Ngiemboon_language)
- [Wikipedia — Languages of Cameroon](https://en.wikipedia.org/wiki/Languages_of_Cameroon)
- [Wikipedia — Cameroonian Pidgin English](https://en.wikipedia.org/wiki/Cameroonian_Pidgin_English)
- [APiCS Online — Cameroon Pidgin English survey](https://apics-online.info/surveys/18)
- [SIL Cameroon — Browse by Language](https://www.silcam.org/resources/browse/language/all?languageid=5)
- [Hugging Face — masakhane collection](https://huggingface.co/masakhane)

---

## 🚧 Next steps

- [ ] Open a GitHub issue to discuss and ratify this selection publicly (`CLA v0.1 — Language Landscape & Initial Language Selection`)
- [ ] Verify Ghomala' dictionary/corpus status directly with SIL Cameroon or West Region linguists
- [ ] Confirm whether NLLB-200's `fuv_Latn` (Fula) is linguistically close enough to Adamawa Fulfulde (`fub`) to be a usable baseline
- [ ] Identify 2–3 potential community/research partners per selected language (universities, churches/missions with translation history, diaspora associations)
- [ ] Begin drafting `CLA-Data v0.1` schema and consent/licensing policy (see [README §CLA-Data](../README.md#-cla-data))
