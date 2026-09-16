# Changelog

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
