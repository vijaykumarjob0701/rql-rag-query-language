# Changelog

## 2026-09-16 late evening — ColBERT + MUVERA multimodal + Search_late weave

- Completed Pass 1–5 on **ColBERT** (SIGIR’20, **10 pp**); journal `0012`; OKF `knowledge/reads/colbert-sigir20/`.
- Completed Pass 1–5 on **MUVERA** (arXiv:2405.19504, **26 pp**); journal `0013`; OKF `knowledge/reads/muvera-2405.19504/` (PDF found — Bruch deferred).
- Extract: `colbert-sigir20.pdf` + `colbert_sigir20/` (78 nodes / 196 edges); `muvera-2405.19504.pdf` + `muvera_2405/` (155 nodes / 109 edges); full page PNG renders.
- Thesis: MaxSim/late interaction **Established** (Eq. 3); `Search_late` + ColBERT→PLAID→MUVERA rewrite ladder **Hypothesis**; related-work late-interact subsection; abstract/apps/optimizer updated; PLAID bib cite-only.
- Docs mirror `docs/08-algebra-sketch.md`; HUMAN_TODOS / NOTES / READMEs updated.
- Optional harness: deterministic MaxSim toy test → `experiments/results/maxsim/unit_test.txt`.
- **No** GitHub push; **no** fabricated IR/RAG metrics (ColBERT/MUVERA tables AUTHOR-only).

## 2026-09-16 late evening — Cormack RRF multimodal + Fuse_rrf weave

- Completed Pass 1–5 on **Cormack et al. RRF** (SIGIR’09, **2 pp**); journal `0011`; OKF `knowledge/reads/rrf-cormack-sigir09/`.
- Extract: `tooling/scripts/extract_out/cormack-sigir09-rrf.pdf` + `rrf_cormack_sigir09/` (9 nodes / 6 edges; page PNG renders for Tables 1–3).
- Thesis: related-work fusion subsection; algebra Fuse_rrf + rewrite; applications hybrid pattern; abstract cites RRF; bib pages 758–759 + DOI.
- Docs mirror `docs/08-algebra-sketch.md`; HUMAN_TODOS marks RRF P2 **done**.
- RRF harness: re-ran unit test; added channel-order invariance property assertion.
- **No** GitHub push; **no** fabricated IR/RAG metrics (Cormack MAPs labelled AUTHOR-only).

## 2026-09-16 evening — VBASE + Filtered-DiskANN multimodal + algebra expand

- Completed Pass 1–5 on **VBASE** (OSDI’23); journal `0009` supersedes stub `0007`; OKF `knowledge/reads/vbase-osdi23/`.
- Completed Pass 1–5 on **Filtered-DiskANN** (WWW’23); journal `0010`; OKF `knowledge/reads/filtered-diskann-www23/`.
- Expanded thesis §05 algebra (typed evidence, signatures, rewrite examples) and §06 FilterExec modes; related-work updated; abstract mentions three multimodal reads.
- Added markdown mirror `docs/08-algebra-sketch.md`.
- Deterministic toy `FilterExec` chooser unit test → `experiments/results/filter_chooser/unit_test.txt`.
- **No** GitHub push; **no** fabricated ANN metrics.

All dates are **Europe/Dublin** local time. Entries describe human-readable research increments (aligned with git commits when the parent agent commits).

## 2026-09-16 — HUMAN_TODO hand-off + thesis rebuild

- Added `experiments/HUMAN_TODOS.md` + protocols 01–04 (FANNS, datasets, adapters, judgments).
- Thesis §09 / Appendix A now point at HUMAN_TODO paths; no fake metrics.
- Fixed planned-run YAML parser; saved RRF unit-test output under `experiments/results/`.
- Journal `0008-human-todos-hand-off.md`.

## 2026-09-16 — ACORN multimodal re-read + thesis + experiments stubs

- Completed Pass 1–5 on ACORN (arXiv:2403.04871); journal `0006-acorn-multimodal-reread.md`.
- OKF-shaped knowledge bundle: `knowledge/reads/acorn-2403.04871/` (concepts + links; research methodology packaging, not RQL runtime).
- Queued VBASE as second seed stub: `journal/0007-vbase-seed-stub.md` (no fake Pass notes).
- Started incremental LaTeX thesis under `thesis/` (arXiv-style article; provisional/hypothesis labels).
- Added `experiments/` reproducibility stubs + tiny deterministic harness smoke test.
- Re-verified `relate_components.py` on existing ACORN extract outputs.

## 2026-09-16 — Correction: Google OKF

- User clarified the Google format/library was **OKF (Open Knowledge Format)**, not LangExtract.
- Updated `tooling/python-libraries.md` and added `journal/0005-okf-correction.md`.
- Implication: prefer OKF-shaped linked markdown for multimodal paper notes / entity graphs.

## 2026-09-16 — Slow-path methodology, journal, tooling

- Added `journal/` so GitHub readers can follow thinking chronologically (`0001`–`0004`).
- Added `methodology/` (principles, search strategy, read protocol, preprocess/synthesis, iteration loop).
- Added `tooling/` library survey + baseline PDF extract/relate scripts (pymupdf/pdfplumber).
- Clarified in root README that v2 literature (`docs/06`, `docs/07`) is **provisional** until multimodal re-read.
- **No** new literature dump; **no** new RQL algebra claims.

## 2026-09-16 — v2 adjacent brainstorm (earlier same day)

- `docs/05`–`07`, expanded examples, search log — breadth-first adjacent literature (provisional).

## 2026-09-16 — v1 landscape (earlier same day)

- Initial landscape, gaps, RQL v1 proposal, related work, examples 01–09.
