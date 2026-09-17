# RQL thesis / technical report (incremental)

**Date started:** 2026-09-16 (Europe/Dublin)  
**Last major polish:** 2026-09-17 (publishability / clarity / implementability)  
**Author:** Vijay Kumar  
**Repo:** https://github.com/vijaykumarjob0701/rql-rag-query-language  

## Status

**arXiv-ready draft pending P0** — structured as a technical report / arXiv-style *proposal + prototype*.

| Ready now | Not claimed yet |
|-----------|-----------------|
| Clear problem → idea → contributions → status | NeurIPS / VLDB acceptance |
| Offline parser / planner / emit / E2E (12/12 toy) | SIFT1M / large-set FANNS P0 |
| Docs-only vendor matrix + schema freeze `0.1.0-draft` | Live adapter smoke (P1) |
| Multimodal prior-art grounding + honesty labels | BEIR / RAG judgment metrics |
| Colab synth FANNS as **plumbing only** | Unreproduced ANN SOTA |

See journal `0034-thesis-publishability-polish.md` for what changed and remaining venue gaps.

## Honesty policy

- Every factual claim about prior work must cite a real BibTeX entry with a URL or arXiv id already verified in `docs/references.md` or freshly checked.
- Label claims as **ESTABLISHED** (sourced), **HYPOTHESIS** (proposed RQL design), **PROVISIONAL** (surveyed but not multimodally re-read), or **AUTHOR-only** (paper tables not reproduced here).
- **Do not** invent experimental metrics, user studies, or “accepted at …” claims.
- Evaluation separates **what we measured** (unit tests, E2E 12/12, Colab synth plumbing) from **what remains** (P0/P1/judgments).
- Work beyond the agent sandbox (GPU ANN, paid APIs, clusters, human judgments) is listed in `../experiments/HUMAN_TODOS.md`.

## Build

```bash
cd thesis
latexmk -pdf -interaction=nonstopmode main.tex
# or: pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Output: `main.pdf`.

Requires TeX Live with `article`, `booktabs`, `hyperref`, `natbib`, `graphicx`, `amsmath`, `tikz`, `listings`, `caption`, `enumitem`, `microtype`.

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
| `00-abstract.tex` | polished | problem → idea → contributions → status |
| `01-introduction.tex` | polished | motivation, 5 contributions, reader's guide, roadmap |
| `02-background.tex` | draft | ANN, hybrid, late interaction, RAG stages |
| `03-related-work.tex` | draft + multimodal | FANNS/ACORN/VBASE/Filtered-DiskANN; fusion; ColBERT/PLAID/MUVERA; HyDE; BlinkDB; Substrait/Calcite |
| `04-problem-formulation.tex` | polished | plain language + requirements / non-goals |
| `05-rql-algebra.tex` | **HYPOTHESIS** | plain language + hello listing; mechanisms Established where cited |
| `06-optimizer.tex` | **HYPOTHESIS** | plain language + FilterExec / budgets / fuse preference |
| `07-compilation.tex` | **HYPOTHESIS** (+ ESTABLISHED adjacency) | E2E figure + hello walkthrough; journals 0020–0026 |
| `08-applications.tex` | draft | hybrid / HyDE / late patterns → `examples/*.rql` |
| `09-evaluation-plan.tex` | polished | measured vs remains; no fake results |
| `10-threats.tex` | polished | limitations / threats sharpened |
| `11-conclusion.tex` | polished | actionable implementer next steps |
| `A-reproducibility.tex` | draft | artifact checklist + Colab synth note |

## Relationship to research notes

- Journal: `../journal/` (through `0034`)
- OKF packaging: `../knowledge/reads/`
- Markdown algebra mirror: `../docs/08-algebra-sketch.md`
- Latest build: `main.pdf` **25 pages**, 2026-09-17 ~01:15 IST (Europe/Dublin); see journal 0034
