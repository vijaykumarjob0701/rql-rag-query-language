# HUMAN_TODOS — what Vijay should run / push back

**Date:** 2026-09-16 (Europe/Dublin)  
**Policy:** Agents must not fake GPU ANN benches, paid APIs, large datasets, production clusters, or human judgments. Items below are explicit hand-offs. Push results into the listed artifact paths in this same GitHub repo.

Legend: **P0** blocks citation-ready eval; **P1** needed for solid paper; **P2** nice-to-have.

---

## P0 — Filtered-ANN microbench (local/GPU optional)

| Field | Value |
|-------|--------|
| Why agent stopped | Needs large vectors, ground-truth kNN, possibly GPU; hours of compute; must not copy ACORN tables |
| Protocol | `experiments/protocols/01-fanns-microbench.md` |
| Suggested command sketch | Build/index with chosen library (FAISS/HNSWlib/DiskANN); sweep selectivity × filter_mode; record recall@10 + p50/p95 |
| Expected artifacts | `experiments/results/fanns/<run_id>/metrics.json`, `plans/*.json`, `ENV.txt` (CPU/GPU, lib versions) |
| Push back | PR with results + ENV; mark AUTHOR_CLAIM vs REPRODUCED in CSV |

## P0 — Dataset acquisition + license notes

| Field | Value |
|-------|--------|
| Why agent stopped | Large downloads / license acceptance (BEIR, MS MARCO, LAION-scale, SIFT1M mirrors) |
| Protocol | `experiments/protocols/02-datasets.md` |
| Expected artifacts | `experiments/datasets/README.md` (URLs, digests, licenses); data itself may be gitignored |
| Push back | Digests + license checklist committed; binaries via LFS or external mirror noted |

## P1 — Backend adapter smoke (real DBs)


### Offline E2E pipeline CLI — **DONE by agent (2026-09-17 ~00:11 IST)** — offline only

| Field | Value |
|-------|--------|
| Status | `experiments/harness/rql_pipeline.py`; results `experiments/results/e2e/` (journal 0026); pause checklist journal 0027 / `PAUSE_CHECKLIST.md` |
| **Still P1 for Vijay** | Live smoke per protocol 03 — E2E offline **does not** satisfy smoke |

### Adapter emit stub — **DONE by agent (2026-09-17 ~00:00 IST)** — emit only

| Field | Value |
|-------|--------|
| Status | Hypothesis sketches under `experiments/harness/rql_adapters/` + results `experiments/results/rql_adapters/` (journal 0024) |
| **Still P1 for Vijay** | Live smoke vs real/local clusters per `experiments/protocols/03-adapter-smoke.md` — emit stub **does not** satisfy smoke; agents must **not** hit live DBs or invent `smoke.json` |


### Docs-only vendor API matrix — **DONE by agent (2026-09-16 ~23:50 IST)**

| Field | Value |
|-------|--------|
| Status | Docs-only complete — `journal/0020-vendor-hybrid-api-matrix.md`, `docs/09-vendor-api-matrix.md`, OKF `knowledge/reads/vendor-api-matrix-2026-09/` |
| **Still P1 for Vijay** | Live smoke vs real/local clusters per `experiments/protocols/03-adapter-smoke.md` — agents must **not** hit live DBs or commit credentials; do not invent `smoke.json` |
| Why agent stopped at docs | Matrix cells are documentation claims; PRE/POST/RRF behaviour under load unverified |



| Field | Value |
|-------|--------|
| Why agent stopped | Needs running Qdrant/pgvector/Pinecone (paid) / Weaviate clusters and credentials |
| Protocol | `experiments/protocols/03-adapter-smoke.md` |
| Expected artifacts | `experiments/results/adapters/<backend>/smoke.json` (latency only OK); **never commit API keys** |
| Push back | Sanitized smoke JSON + docker-compose if local |

## P1 — Human / LLM-as-judge relevance (RAG quality)

| Field | Value |
|-------|--------|
| Why agent stopped | Human judgments or paid LLM judge APIs; subjective labels |
| Protocol | `experiments/protocols/04-rag-judgments.md` |
| Expected artifacts | `experiments/results/judgments/<set_id>/labels.jsonl`, judge prompt hash |
| Push back | Label file + agreement stats; no fabricated nDCG |

## P1 — Complete VBASE multimodal Pass 1–5 — **DONE by agent (2026-09-16 evening IST)**

| Field | Value |
|-------|--------|
| Status | Completed independently — journal `0009`, OKF `knowledge/reads/vbase-osdi23/` (stub `0007` retained as history) |
| Human follow-up (optional) | Spot-check PDF figures; compare MSVBASE GitHub APIs to §4.2 if desired |

## P2 — Filtered-DiskANN + Cormack RRF + ColBERT + MUVERA + PLAID + Bruch multimodal — **DONE by agent**

| Field | Value |
|-------|--------|
| Filtered-DiskANN | journal `0010`, OKF `knowledge/reads/filtered-diskann-www23/` |
| Cormack RRF SIGIR’09 | journal `0011`, OKF `knowledge/reads/rrf-cormack-sigir09/` (2 pp; formula+k=60 **Established**) |
| ColBERT SIGIR’20 | journal `0012`, OKF `knowledge/reads/colbert-sigir20/` (10 pp; MaxSim Eq.3 **Established**) |
| MUVERA arXiv:2405.19504 | journal `0013`, OKF `knowledge/reads/muvera-2405.19504/` (26 pp; FDE rewrite mechanism) |
| PLAID CIKM’22 | journal `0014`, OKF `knowledge/reads/plaid-cikm22/` (10 pp; centroid interaction/pruning **Established**; speedups AUTHOR-only) |
| Bruch fusion TOIS/arXiv:2210.11934 | journal `0016`, OKF `knowledge/reads/bruch-arxiv-2210.11934/` (36 pp; CC/TM2C2 **Established** mechanism; AUTHOR NDCG unreproduced) |
| Still open (P2) | FANNS survey Lin 2025 figure/table pass (**done** journal 0019); vendor API matrix (**done** docs-only journal 0020 — live smoke still P1 below) |
| Done (2026-09-16) | Chen et al. ECIR’22 RRF-vs-CC cite-chase (journal 0017; setup conflict → Fuse preference Hypothesis) |

## P2 — Production plan-stability soak

Long-running identical RQL → plan hash stability across versions; needs CI machine.

---

## Already done by agent (do not redo unless regenerating)

- Vendor hybrid/filter/fusion API matrix docs-only (journal `0020`, `docs/09-vendor-api-matrix.md`, OKF `knowledge/reads/vendor-api-matrix-2026-09/`); **live smoke still P1**
- Offline E2E pipeline CLI (journal `0026`, `experiments/harness/rql_pipeline.py`, `experiments/results/e2e/`); **live smoke still P1**
- Pause / human P0 checklist (journal `0027`, `experiments/PAUSE_CHECKLIST.md`)

- ACORN Pass 1–5 + OKF bundle (`journal/0006`, `knowledge/reads/acorn-2403.04871/`)
- VBASE Pass 1–5 + OKF (`journal/0009`, `knowledge/reads/vbase-osdi23/`)
- Filtered-DiskANN Pass 1–5 + OKF (`journal/0010`, `knowledge/reads/filtered-diskann-www23/`)
- Cormack RRF Pass 1–5 + OKF (`journal/0011`, `knowledge/reads/rrf-cormack-sigir09/`)
- ColBERT Pass 1–5 + OKF (`journal/0012`, `knowledge/reads/colbert-sigir20/`)
- MUVERA Pass 1–5 + OKF (`journal/0013`, `knowledge/reads/muvera-2405.19504/`)
- PLAID Pass 1–5 + OKF (`journal/0014`, `knowledge/reads/plaid-cikm22/`)
- Bruch CC/TM2C2 Pass 1–5 + OKF (`journal/0016`, `knowledge/reads/bruch-arxiv-2210.11934/`)
- Thesis LaTeX draft + PDF build (`thesis/main.pdf`) — Fuse_rrf / Fuse_linear delineation + ColBERT→PLAID→MUVERA ladder (mechanisms)
- Deterministic RRF unit tests (`experiments/harness/test_rrf_fusion.py` → `experiments/results/rrf_unit_test.txt`; property: channel-order invariance)
- Deterministic linear/CC unit tests (`experiments/harness/test_linear_fusion.py` → `experiments/results/linear_fusion/unit_test.txt`)
- Deterministic FilterExec chooser toy test (`experiments/harness/test_filter_strategy_chooser.py` → `experiments/results/filter_chooser/unit_test.txt`)
- Deterministic MaxSim toy test (`experiments/harness/test_maxsim_late.py` → `experiments/results/maxsim/unit_test.txt`)
- Planned-run printer (no scores)
