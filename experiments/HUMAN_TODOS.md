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

## P2 — Filtered-DiskANN multimodal — **DONE by agent**; RRF classic still open

| Field | Value |
|-------|--------|
| Filtered-DiskANN | journal `0010`, OKF `knowledge/reads/filtered-diskann-www23/` |
| Still open (P2) | Cormack et al. RRF SIGIR 2009 multimodal Pass 1–5; optional FANNS survey figure/table pass (`docs/references.md` #71, #61) |

## P2 — Production plan-stability soak

Long-running identical RQL → plan hash stability across versions; needs CI machine.

---

## Already done by agent (do not redo unless regenerating)

- ACORN Pass 1–5 + OKF bundle (`journal/0006`, `knowledge/reads/acorn-2403.04871/`)
- VBASE Pass 1–5 + OKF (`journal/0009`, `knowledge/reads/vbase-osdi23/`)
- Filtered-DiskANN Pass 1–5 + OKF (`journal/0010`, `knowledge/reads/filtered-diskann-www23/`)
- Thesis LaTeX draft + PDF build (`thesis/main.pdf`) — algebra/optimizer expanded evening IST
- Deterministic RRF unit test (`experiments/harness/test_rrf_fusion.py` → `experiments/results/rrf_unit_test.txt`)
- Deterministic FilterExec chooser toy test (`experiments/harness/test_filter_strategy_chooser.py` → `experiments/results/filter_chooser/unit_test.txt`)
- Planned-run printer (no scores)
