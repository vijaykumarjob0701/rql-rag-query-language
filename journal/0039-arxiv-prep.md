# 0039 — arXiv submission prep (thesis polish + package)

**Date:** 2026-09-19 ~08:28 IST (Europe/Dublin)  
**Type:** packaging / publishability  
**Status:** Local arXiv package ready; **human must Submit** on arxiv.org. **No push.**

## Context
Thesis was already an arXiv-style proposal+prototype (journal 0034) with FAISS HNSW32 SIFT1M PRE/POST measured plumbing (journal 0038). Goal: polish for upload and ship a clean source zip under `arxiv/`.

## What changed

### Thesis polish
- **Title line:** kept strong title + “Technical Report …” subtitle; removed “not a camera-ready venue submission” from the title (moved into first-page draft-status note).
- **Author block:** Vijay Kumar; Independent researcher, Dublin, Ireland; email; links to both GitHub repos.
- **Date:** 19 September 2026.
- **Abstract:** mentions FAISS HNSW32 SIFT1M PRE/POST microbench (run `sift1m_faiss_HNSW32_20260917_022017`) with honest synthetic-predicate / non-ACORN framing.
- **§09:** already listed the FAISS run under “what we measured”; left intact (no fabricated metrics).
- **§11 + Appendix A:** FAISS plumbing + P0 *partially* addressed; remaining depth sweeps / adapters / judgments.
- **`thesis/README.md`:** status table P0 partially addressed; suggested categories cs.IR (primary), cs.DB (secondary), optional cs.LG.

### arXiv package (`arxiv/`)
- `README.md` — upload how-to + checklist for Vijay
- `METADATA.md` — title, abstract paste, comments, license
- `00README.XXX` — autoTeX notes
- `build_arxiv_zip.sh` → `rql-arxiv-source.zip` + copy `rql-arxiv.pdf`
- Integrity: no NeurIPS claims; FAISS labelled accurately

## Build artifacts
- `thesis/main.pdf` / `arxiv/rql-arxiv.pdf`: **25 pages** (2026-09-19 Europe/Dublin rebuild)
- Zip: `arxiv/rql-arxiv-source.zip` (21 files; main.tex + sections + figures + bib + bbl + 00README.XXX)

## Non-claims
- Not NeurIPS/VLDB accepted
- Not ACORN / paper-table reproduction
- No live adapters / RAG judgments invented

## Next
- Vijay reviews PDF + zip, then clicks **Submit** on arxiv.org with his account.
- Do **not** push unless human requests.
