# 0004 — Slow-path methodology & tooling

**When:** 2026-09-16 (Europe/Dublin)  
**Artifacts:** [`../methodology/`](../methodology/), [`../tooling/`](../tooling/)

---

## Context

After v2’s adjacent dump, the user redirected: **do not rush more paper dumps.** Prefer incremental, careful process — strategy first, multimodal reading, relationship extraction, Python tooling — so GitHub readers can follow thinking → findings.

## Question asked

How should we search, read, preprocess, and iterate so that only validated 1–5% seeds move the RQL thesis — and what libraries/scripts support multimodal PDF understanding (text ↔ tables ↔ figures ↔ entities)?

## Where we looked

- Existing project docs (`README`, docs/05–07) for alignment — **no expansion of literature claims**  
- Web survey (2024–2026) of Python document libraries: PyMuPDF, pdfplumber, Docling, unstructured, marker, MinerU, camelot, LayoutParser, LayoutLM/Donut ecosystem, GraphDoc, Google Document AI, LangExtract (later deprioritized), **OKF**, etc.

## What we did (this step)

1. Wrote slow-path methodology: principles, search strategy (funnel + mutation), read protocol (5 passes), preprocess/synthesis (promotion gates), iteration loop + stop criteria.  
2. Surveyed libraries into `tooling/python-libraries.md` (initial Google guess later corrected to OKF in `0005`).  
3. Built minimal local scripts: `extract_document.py`, `relate_components.py`, notes template, venv + smoke-test on one public PDF.  
4. Introduced this `journal/` so humans can follow chronological thinking.

## What we read multimodally

Smoke-test PDF only (tooling validation) — **not** yet a full protocol pass on docs/06 sources. Methodology work intentionally precedes that re-read.

## 1–5% seed

**Process seed:** often only 1–5% of a source unlocks the next search; that fraction frequently lives in a figure, table, or caption relationship — so inventory + relate passes are mandatory before synthesis.  
**Tooling seed (later corrected):** We initially guessed LangExtract; the user confirmed **OKF (Open Knowledge Format)** — see `0005`. Local baseline extractors still do offline PDF inventory; OKF is the preferred *shape* for linked notes.

## Uncertainty

- Docling/MinerU may be heavy for the default venv; baseline is pymupdf/pdfplumber with graceful degrade  
- Heuristic figure/table linking is imperfect without layout models  
- Journal discipline only helps if later agents obey promotion rules  

## Next questions

1. Pick **2–3** sources from docs/06 (recommended: ACORN; a fusion/RRF or FANNS survey figure-heavy paper; VBASE or Substrait/plan-IR note) and run full Pass 1–5.  
2. File journal `0005+` per completed multimodal read.  
3. Only then consider demoting/enriching docs/06 rows or promoting into docs/07.

---

## Smoke-test appendix (same day)

Ran baseline pipeline on **ACORN** arXiv:2403.04871 (15 pp PDF):

- Text + structure + 30 embedded images: OK  
- Table CSV export: **none** (Table 1 appears in text/captions; geometry not recovered by pdfplumber/pymupdf)  
- `relate_components.py`: 64 refs / 21 captions → heuristic `relations.json`  

Reinforces protocol rule: tooling assists inventory; Pass 2 still requires opening the PDF for figures/tables.

---

## Correction (same day)

User clarified the Google piece was **OKF (Open Knowledge Format)**, not LangExtract. See `journal/0005-okf-correction.md`. Seed insight above about “entity/relation tooling” still holds; the **format** we should align notes to is OKF-shaped linked markdown.
