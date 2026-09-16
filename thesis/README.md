# RQL thesis / paper (incremental)

**Date started:** 2026-09-16 (Europe/Dublin)  
**Author:** Vijay Kumar  
**Repo:** https://github.com/vijaykumarjob0701/rql-rag-query-language  

## Honesty policy

- Every factual claim about prior work must cite a real BibTeX entry with a URL or arXiv id already verified in `docs/references.md` or freshly checked.
- Label claims in prose and comments as **ESTABLISHED** (sourced), **HYPOTHESIS** (proposed RQL design), or **PROVISIONAL** (surveyed but not multimodally re-read).
- **Do not** invent experimental metrics, user studies, or “accepted at …” claims. This draft is structured so it *can* grow into a citable work; it is **not** ready for NeurIPS/VLDB/arXiv acceptance.
- Evaluation section describes a **plan** and harness stubs. Only report numbers you actually ran (see `../experiments/`).
- Work beyond the agent sandbox (GPU ANN, paid APIs, clusters, human judgments) is listed in `../experiments/HUMAN_TODOS.md` for Vijay to run and push.

## Build

```bash
cd thesis
latexmk -pdf -interaction=nonstopmode main.tex
# or: pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Output: `main.pdf` (also copied/noted after successful builds).

Requires TeX Live with `article`, `booktabs`, `hyperref`, `natbib`/`biblatex` (this draft uses `natbib` + BibTeX), `graphicx`, `amsmath`, `tikz` (optional figure).

## Section status

| File | Status | Notes |
|------|--------|-------|
| `00-abstract.tex` | draft | Honest about provisional stage |
| `01-introduction.tex` | draft | Motivation: accuracy/latency/reliability |
| `02-background.tex` | draft | ANN, hybrid, RAG pipeline stages |
| `03-related-work.tex` | draft | ACORN + VBASE + Filtered-DiskANN multimodally read |
| `04-problem-formulation.tex` | draft | Formal problem for portable retrieval IR |
| `05-rql-algebra.tex` | **HYPOTHESIS** | Typed evidence + rewrite examples (ACORN/VBASE/FDANN seeds) |
| `06-optimizer.tex` | **HYPOTHESIS** | FilterExec modes tied to ACORN/VBASE/FDANN |
| `07-compilation.tex` | **HYPOTHESIS** | Adapters / polystore shims |
| `08-applications.tex` | draft | RAG patterns → RQL |
| `09-evaluation-plan.tex` | plan only | No fake results |
| `10-threats.tex` | draft | |
| `11-conclusion.tex` | draft | |
| `A-reproducibility.tex` | draft | Artifact checklist |

## Relationship to research notes

- Journal: `../journal/` (`0006` ACORN, `0009` VBASE, `0010` Filtered-DiskANN)
- OKF packaging (methodology, not runtime): `../knowledge/reads/{acorn-2403.04871,vbase-osdi23,filtered-diskann-www23}/`
- Markdown algebra mirror: `../docs/08-algebra-sketch.md`
- Evolved idea (provisional): `../docs/07-evolved-idea.md`
- Latest build: `main.pdf` (**10 pages**, 2026-09-16 evening IST)
