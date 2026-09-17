# 0035 — Evidence audit + companion reproducibility repo

**Date:** 2026-09-17 ~01:10 IST (Europe/Dublin)  
**Type:** evidence inventory + artifact packaging recommendation  
**Status:** complete locally; parent will `gh repo create` + push both remotes  
**Integrity:** no fabricated P0 metrics; no GitHub push from this turn; no invented dataset digests

---

## Goal

Produce a clear in-repo evidence audit and a **separate** companion workspace `rql-repro` so venue-grade empirics (datasets, pinned runnable package, small fixtures) are not mixed into the thesis/OKF narrative tree.

## What changed (research repo)

- New root [`EVIDENCE.md`](../EVIDENCE.md): tables for **provided properly** vs **incomplete/missing for venue-grade**, plus recommendation to split.
- Thesis appendix: [`thesis/sections/A-reproducibility.tex`](../thesis/sections/A-reproducibility.tex) — subsection pointing to `https://github.com/vijaykumarjob0701/rql-repro`.
- Rebuild `thesis/main.pdf`.

## Companion workspace (local)

Path: `/workspace/rql-repro/` (fresh). Intended remote after parent create: `vijaykumarjob0701/rql-repro`.

Contents (high level):

- `datasets/REGISTRY.md` + `synthetic/` generator + tiny committed fixtures; SIFT1M download **instructions only**; digests **TBD after download**.
- `code/` — copied offline harness (parser/planner/adapters/pipeline) + schemas + toy examples + tests; pinned `requirements.txt`.
- `colab/` — notebook + `LINKS.md` Drive URL.
- `results/fixtures/` — small text/JSON smoke evidence copies (not P0).
- `EVIDENCE.md` mirrored checklist; `CITATION.cff` / `cite.md`; MIT `LICENSE`.

## Verdict (one line)

Offline prototype + literature **OK**; citation-ready FANNS/RAG **not yet**; **yes** to companion `rql-repro`.

## Non-changes

- No multi-GB data committed.
- No live DB adapter execution.
- No push.
