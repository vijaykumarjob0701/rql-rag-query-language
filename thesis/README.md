# RQL thesis / technical report (arXiv prep)

**Date started:** 2026-09-16 (Europe/Dublin)  
**Last major polish:** 2026-09-19 (arXiv upload package)  
**Author:** Vijay Kumar (Independent researcher, Dublin, Ireland)  
**Email:** vijaykumarjob0701@gmail.com  
**Research repo:** https://github.com/vijaykumarjob0701/rql-rag-query-language  
**Companion repro:** https://github.com/vijaykumarjob0701/rql-repro  

## Status

**arXiv-ready technical report (proposal + prototype + measured plumbing).**  
Not a camera-ready NeurIPS/VLDB venue submission. Draft status is on the first page (not in the title line).

| Ready now | Not claimed yet |
|-----------|-----------------|
| Clear problem → idea → contributions → status | NeurIPS / VLDB acceptance |
| Offline parser / planner / emit / E2E (12/12 toy) | Full P0 depth / multi-index sweeps |
| Docs-only vendor matrix + schema freeze `0.1.0-draft` | Live adapter smoke (P1) |
| Multimodal prior-art grounding + honesty labels | BEIR / RAG judgment metrics |
| Colab synth FANNS as **plumbing only** | Unreproduced ANN SOTA |
| **FAISS HNSW32 SIFT1M PRE/POST** (`sift1m_faiss_HNSW32_20260917_022017`) | ACORN / paper-table reproduction |

**P0 partially addressed** by FAISS HNSW32 curves (journal 0038): synthetic Bernoulli predicates; single efSearch/candidate-mult; not ACORN numbers. Live adapters + judgments still open.

See journal `0034` (publishability), `0038` (FAISS), `0039` (arXiv prep). Submission package: `../arxiv/`.

## Suggested arXiv categories

| Role | Category | Why |
|------|----------|-----|
| **Primary** | **cs.IR** | Retrieval plans, FANNS/hybrid IR, RAG retrieval staging |
| **Secondary** | **cs.DB** | Portable IR / LogicalPlan–PhysicalPlan, compile-to-adapters, Substrait/Calcite adjacency |
| Optional | cs.LG | Only if you want ML-adjacent discoverability; not required for this draft |

License recommendation for upload: **CC-BY-4.0** (or arXiv perpetual non-exclusive license). See `../arxiv/README.md`.

## Honesty policy

- Every factual claim about prior work must cite a real BibTeX entry with a URL or arXiv id already verified in `docs/references.md` or freshly checked.
- Label claims as **ESTABLISHED** (sourced), **HYPOTHESIS** (proposed RQL design), **PROVISIONAL** (surveyed but not multimodally re-read), or **AUTHOR-only** (paper tables not reproduced here).
- **Do not** invent experimental metrics, user studies, or “accepted at …” claims.
- Evaluation separates **what we measured** (unit tests, E2E 12/12, Colab synth plumbing, FAISS HNSW32 SIFT1M microbench) from **what remains** (P0 remainder / P1 / judgments).
- Work beyond the agent sandbox (GPU ANN, paid APIs, clusters, human judgments) is listed in `../experiments/HUMAN_TODOS.md`.

## Build

```bash
cd thesis
latexmk -pdf -interaction=nonstopmode main.tex
# or: pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Output: `main.pdf`.

Requires TeX Live with `article`, `booktabs`, `hyperref`, `natbib`, `graphicx`, `amsmath`, `tikz`, `listings`, `caption`, `enumitem`, `microtype`.

For the arXiv source zip (from repo root):

```bash
bash arxiv/build_arxiv_zip.sh
```

## Reader path (engineers)

1. Abstract + §1 (esp. Reader's guide / hello RQL).
2. Figure: end-to-end pipeline (`figures/e2e-pipeline.tikz`) + plan layers (`figures/plan-layers.tikz`).
3. Run offline:
   ```bash
   cd experiments/harness
   python rql_pipeline.py --help
   # toy matrix → experiments/results/e2e/
   ```
4. Then §5–§7 for algebra / planner / adapters; §9 for measured vs remaining.

## Section status

| File | Status | Notes |
|------|--------|-------|
| `00-abstract.tex` | polished | problem → idea → contributions → status (+ FAISS HNSW32) |
| `01-introduction.tex` | polished | motivation, 5 contributions, reader's guide, roadmap |
| `02-background.tex` | draft | ANN, hybrid, late interaction, RAG stages |
| `03-related-work.tex` | draft + multimodal | FANNS/ACORN/VBASE/Filtered-DiskANN; fusion; ColBERT/PLAID/MUVERA; HyDE; BlinkDB; Substrait/Calcite |
| `04-problem-formulation.tex` | polished | plain language + requirements / non-goals |
| `05-rql-algebra.tex` | **HYPOTHESIS** | plain language + hello listing; mechanisms Established where cited |
| `06-optimizer.tex` | **HYPOTHESIS** | plain language + FilterExec / budgets / fuse preference |
| `07-compilation.tex` | **HYPOTHESIS** (+ ESTABLISHED adjacency) | E2E figure + hello walkthrough; journals 0020–0026 |
| `08-applications.tex` | draft | hybrid / HyDE / late patterns → `examples/*.rql` |
| `09-evaluation-plan.tex` | polished | measured vs remains; FAISS run id explicit; no fake results |
| `10-threats.tex` | polished | limitations / threats sharpened |
| `11-conclusion.tex` | polished | actionable implementer next steps; arXiv framing |
| `A-reproducibility.tex` | draft | artifact checklist + Colab + FAISS + companion |

## Relationship to research notes

- Journal: `../journal/` (through `0039`)
- OKF packaging: `../knowledge/reads/`
- Markdown algebra mirror: `../docs/08-algebra-sketch.md`
- arXiv package: `../arxiv/` (`rql-arxiv-source.zip`, `rql-arxiv.pdf`, `METADATA.md`)
- Latest build: see `main.pdf` after `latexmk`; page count recorded in journal 0039
