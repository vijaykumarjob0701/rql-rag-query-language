# Evidence audit — RQL research repo

**Date:** 2026-09-17 (Europe/Dublin)  
**Research repo:** [vijaykumarjob0701/rql-rag-query-language](https://github.com/vijaykumarjob0701/rql-rag-query-language)  
**Companion repro repo (recommended):** [vijaykumarjob0701/rql-repro](https://github.com/vijaykumarjob0701/rql-repro)  
**Integrity:** no fabricated P0 metrics; offline prototype claims only where paths below exist.

This audit separates **what is already in-repo and checkable** from **what is still missing for venue-grade empirics**. Narrative / thesis / OKF stay here; runnable datasets + pinned package + small result fixtures belong in the companion repo.

---

## Provided properly (in-repo)

| Artifact | Path(s) | Notes |
|----------|---------|-------|
| Literature OKF / multimodal journal reads | `knowledge/reads/*/` (17 bundles), `journal/0016`–`0033` | Claims / concepts / extracts; honesty labels in thesis macros |
| Thesis PDF + honesty labels | `thesis/main.pdf`, `thesis/main.tex` (`\established{}` / `\hypothesis{}` / `\provisional{}` / `\authoronly{}`) | arXiv-style proposal + prototype framing |
| Schemas + examples | `schemas/logical-plan.schema.json`, `schemas/physical-plan.schema.json`, `schemas/examples/`, `examples/toy/*.rql` | Draft IR 0.1.0 |
| Offline prototype (parser / planner / emit / E2E 12/12) | `experiments/harness/rql_{parser,planner,adapters}/`, `experiments/harness/rql_pipeline.py` | Live DB: **false**; `notExecuted: true` |
| Unit / validate scripts | `experiments/harness/test_*.py`, `validate_plans.py` | RRF, MaxSim, linear fusion, filter chooser, parser/planner/adapters |
| E2E smoke evidence | `experiments/results/e2e/smoke/` (`summary.txt`, `manifest.json`, `run_validate.txt`) | **RESULT: ok=12/12** (2026-09-17T00:10:55+01:00) |
| Colab synth FANNS results + LINKS | `experiments/results/fanns/colab_synth_20260916_233628/`, `experiments/colab/LINKS.md` | **Not P0**; synthetic Gaussian / T4 plumbing |
| Vendor matrix (docs-only) | `knowledge/reads/vendor-api-matrix-2026-09/`, `docs/09-vendor-api-matrix.md` | No live API smokes |
| Colab notebook + how-to | `experiments/colab/fanns_microbench_colab.ipynb`, `experiments/HOW_TO_PROVIDE_RESULTS.md` | Human/Colab return paths |

---

## Incomplete / missing for venue-grade

| Gap | Status | Where it should land |
|-----|--------|----------------------|
| **P0 large-set FANNS with ground truth** (e.g. SIFT1M + selectivities) | **SIFT1M obtained**; NumPy plumbing + **FAISS HNSW32 PRE/POST curves** (nq=1000) present — still not ACORN-class / depth-sweep complete; live adapters + judgments still missing | Companion `code/bench/fanns_sift1m_faiss_microbench.py`; results `experiments/results/fanns/sift1m_faiss_HNSW32_20260917_022017/` |
| **Dataset binaries** | Correctly **absent** from git | Companion `datasets/REGISTRY.md` + `download_sift1m.sh`; **digests filled 2026-09-17** from HF `qbo-odp/sift1m` |
| **Live adapter smokes** (Qdrant / ES / pgvector) | Missing | `experiments/results/adapters/` (sanitized); never commit secrets |
| **RAG judgments** (nDCG / human prefs) | Missing | Protocol `experiments/protocols/04-rag-judgments.md`; results TBD |
| **Pinned `requirements.txt` at experiments root** | Missing here | Companion ships pinned `requirements.txt`; research may add a thin pointer later |

---

## Recommendation

**Yes — provide a separate companion repo `rql-repro`** for:

1. **Dataset registry** + synthetic fixtures + download **instructions** (no multi-GB binaries in git).
2. **Runnable implementation package** (parser / planner / adapters / pipeline) with pinned deps.
3. **Small committed result fixtures** (text/JSON smoke summaries only).

Keep this research repo focused on **thesis / journal / OKF narrative**, schemas-as-spec, and pointers to measured plumbing.

Companion URL (after parent `gh repo create`):  
https://github.com/vijaykumarjob0701/rql-repro

---

## Quick verdict

| Tier | Verdict |
|------|---------|
| Offline compile-stack prototype | **Supported** (12/12 E2E + unit scripts) |
| Literature / honesty discipline | **Supported** (OKF + thesis labels) |
| Citation-ready FANNS / RAG empirics | **Partial** — FAISS HNSW32 SIFT1M curves on disk (journal 0038); still missing depth sweeps / live adapters / judgments |
| Venue-grade artifact package | **Split recommended** → `rql-repro` |

**Update 2026-09-17 (later):** SIFT1M via HF `qbo-odp/sift1m`; digests in companion REGISTRY. NumPy PRE/POST: `sift1m_{subset,full}_20260917_01224*`. **FAISS HNSW32 index microbench:** `sift1m_faiss_HNSW32_20260917_022017/` (nq=1000, PRE/POST × s∈{0.01,0.05,0.1,0.5}; journal 0038). Not ACORN numbers. Live adapters + judgments still open. Colab synth: `colab_synth_large_20260917_001447/`.
