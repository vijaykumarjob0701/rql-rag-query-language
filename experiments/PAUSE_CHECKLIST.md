# PAUSE_CHECKLIST — hand-off for human P0

**Date:** 2026-09-17 ~00:25 IST (Europe/Dublin)  
**Purpose:** Summarize what is **Established / in-repo** vs what **blocks citation-ready** evaluation.  
**Policy:** Agents must not fake GPU ANN benches, invent smoke.json, or hit live DBs. See [`HUMAN_TODOS.md`](HUMAN_TODOS.md) and [`protocols/`](protocols/).

**Agent recommendation (2026-09-17):** **Pause for human P0** (protocols 01–02) before another literature seed. Offline E2E compile glue is done (journal 0026); further paper passes yield diminishing returns for citation-ready claims.

---

## A. ESTABLISHED / in-repo (do not redo unless regenerating)

### Literature mechanisms (multimodal Pass 1–5)

| Topic | Journal / OKF | Label |
|-------|---------------|--------|
| ACORN filtered ANN | 0006 · `knowledge/reads/acorn-2403.04871/` | Established mechanism |
| VBASE | 0009 · `vbase-osdi23/` | Established mechanism |
| Filtered-DiskANN | 0010 · `filtered-diskann-www23/` | Established mechanism |
| Cormack RRF | 0011 · `rrf-cormack-sigir09/` | Established (k=60 formula) |
| ColBERT MaxSim | 0012 · `colbert-sigir20/` | Established |
| MUVERA FDE ladder | 0013 · `muvera-2405.19504/` | Established rewrite mechanism |
| PLAID centroid interaction | 0014 · `plaid-cikm22/` | Established mechanism |
| Bruch CC/TM2C2 | 0016 · `bruch-arxiv-2210.11934/` | Established mechanism |
| Chen ECIR’22 RRF-vs-linear | 0017 · `chen-ecir2022-2201.10582/` | Established setup conflict |
| Montague–Aslam Condorcet | 0018 · `montague-aslam-cikm02-condorcet/` | Established mechanism |
| FANNS survey Lin 2025 | 0019 · `fanns-lin2025-2505.06501/` | Established taxonomy |
| Vendor API matrix (docs-only) | 0020 · `vendor-api-matrix-2026-09/` + `docs/09-…` | Established **surface survey** (not live) |
| Substrait / Calcite adjacency | 0025 · `substrait-spec-2026-09/` + `calcite-begoli-sigmod18/` | Established priors; RQL inspired-by only |

### Hypothesis packaging (offline prototype — not a standard)

| Component | Path / journal | Smoke |
|-----------|----------------|-------|
| LogicalPlan / PhysicalPlan JSON Schema 0.1.0-draft | `schemas/` · 0021 | examples validate |
| Toy RQL → LogicalPlan parser | `experiments/harness/rql_parser/` · 0022 | 4/4 |
| Logical→Physical planner stub | `experiments/harness/rql_planner/` · 0023 | 12/12 |
| Physical→vendor emit stub | `experiments/harness/rql_adapters/` · 0024 | 6/6 (subset) |
| **E2E CLI glue** | `experiments/harness/rql_pipeline.py` · 0026 | **4 toys × 3 profiles = 12/12** |
| Human+Colab result paths | `HOW_TO_PROVIDE_RESULTS.md` · `colab/` · 0028 | docs + optional CPU smoke (**not P0**) |
| Deterministic unit toys | RRF / linear / MaxSim / filter chooser | unit txt under `results/` |
| Thesis draft + PDF | `thesis/main.pdf` | rebuilt with E2E sentence |

### Honest non-claims (still)

- RQL ≠ Substrait implementation / Calcite embedding.  
- Planner stub ≠ Cascades/Volcano cost model.  
- Emit / E2E ≠ live adapter smoke.  
- No unreproduced ANN/RAG scores in thesis.

---

## B. BLOCKS citation-ready (human-owned)

### P0 — must have for citation-ready filtered-ANN / eval claims

| Item | Protocol | Expected artifacts | Why agent stopped |
|------|----------|--------------------|-------------------|
| **Filtered-ANN microbench** | protocol 01 | **Partial** — FAISS HNSW32 curves at `results/fanns/sift1m_faiss_HNSW32_20260917_022017/`; depth sweeps optional | Agent delivered index microbench; not ACORN; further sweeps optional |
| **Dataset acquisition + licenses** | [`protocols/02-datasets.md`](protocols/02-datasets.md) · stub [`datasets/README.md`](datasets/README.md) | `experiments/datasets/README.md` (URLs, digests, licenses) | Large downloads / license acceptance |

Without P0, thesis evaluation sections remain a **plan**, not results.

### P1 — needed for solid “adapters / quality” paper claims

| Item | Protocol | Expected artifacts | Notes |
|------|----------|--------------------|-------|
| **Backend adapter live smoke** | [`protocols/03-adapter-smoke.md`](protocols/03-adapter-smoke.md) | `experiments/results/adapters/<backend>/smoke.json` (sanitized) | Emit stub / E2E offline **do not** satisfy this; no credentials in git |
| **RAG judgments** (human / LLM-as-judge) | [`protocols/04-rag-judgments.md`](protocols/04-rag-judgments.md) | `experiments/results/judgments/<set_id>/labels.jsonl` | No fabricated nDCG |

### P2 — nice-to-have

- Production plan-stability soak (CI machine).  
- Optional deeper Substrait Extension*Rel prototype (defer unless needed for paper narrative).

Full field detail: [`HUMAN_TODOS.md`](HUMAN_TODOS.md).

---

## C. How to use the offline E2E (agent-safe)

```bash
# from repo root — never hits live DBs
tooling/.venv/bin/python experiments/harness/rql_pipeline.py \
  --inputs examples/toy \
  --profiles qdrant,elasticsearch,pgvector \
  --out-dir experiments/results/e2e \
  --run-id smoke \
  --validate
# → experiments/results/e2e/run_validate.txt  (expect ok=12/12)
```

---

## D. Suggested human next steps (ordered)

1. **P0 datasets** — accept licenses; record digests in `experiments/datasets/README.md`.  
2. **P0 FANNS microbench** — one library (FAISS or HNSWlib) × selectivity sweep; mark AUTHOR_CLAIM vs REPRODUCED.  
   - Local: Option A in [`HOW_TO_PROVIDE_RESULTS.md`](HOW_TO_PROVIDE_RESULTS.md).  
   - **Colab:** [`colab/fanns_microbench_colab.ipynb`](colab/fanns_microbench_colab.ipynb) → zip → `experiments/results/fanns/<run_id>/` (synthetic ≠ P0; use licensed SIFT1M cell for P0).  
3. **P1 adapter smoke** — local docker Qdrant + pgvector; feed sketches from E2E emit as starting points (still validate live); path `results/adapters/<backend>/smoke.json`.  
4. Optional P1 judgments once retrieval runs exist.

---

## E. Agent continue-vs-pause

| Option | When |
|--------|------|
| **Pause for human P0** (recommended) | Citation-ready eval is the bottleneck; offline stack is sufficient for a draft thesis narrative. |
| Continue agent seed | Only low-cost polish (extra emit vendors, grammar docs) — **not** a substitute for P0. |

Journal companions: [`../journal/0027-pause-human-p0-checklist.md`](../journal/0027-pause-human-p0-checklist.md), [`../journal/0028-human-colab-results-paths.md`](../journal/0028-human-colab-results-paths.md).

**Update 2026-09-17 (later):** **P0 partially addressed** — FAISS HNSW32 SIFT1M PRE/POST curves in `results/fanns/sift1m_faiss_HNSW32_20260917_022017/` (journal 0038). Dataset digests filled. Still missing: live adapters (P1), judgments (P1), optional depth/multi-index sweeps. Pause remains appropriate for those human-owned items.

**Earlier:** Colab synthetic microbench in `results/fanns/colab_synth_20260916_233628/`.
