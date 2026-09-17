# 0038 — SIFT1M FAISS-index filtered-ANN microbench (HNSW32)

**Date:** 2026-09-17 ~02:21 IST (Europe/Dublin)  
**Type:** empirical microbench (protocol 01)  
**Status:** FAISS **index** PRE/POST curves on full SIFT1M recorded — stronger than NumPy brute; **not** ACORN numbers

## Context
Journal `0037` obtained SIFT1M (HF mirror) and ran NumPy brute PRE/POST plumbing. Venue-style P0 still needed a real ANN index (FAISS/HNSWlib) with filtered GT, ENV, and selectivity curves.

## Question asked
Can we run a protocol-01-aligned FAISS-index filtered-ANN microbench on full SIFT1M (PRE/POST × selectivities) with real metrics only?

## Method
| Choice | Value | Why |
|--------|-------|-----|
| Primary index | **HNSW32** (`IndexHNSWFlat`, M=32, efConstruction=200, efSearch=64) | Prefer over IVF4096,Flat: no train/nprobe tuning; graph family; `IDSelectorBitmap` PRE; `efSearch` depth knob |
| Filtered GT | `IndexFlatL2` + `IDSelectorBitmap` | Exact filtered top-k (not official unfiltered `sift_groundtruth.ivecs`) |
| PRE | `SearchParametersHNSW` + `IDSelectorBitmap` on full HNSW | First-class FAISS filter-at-search |
| POST | HNSW top-(k×50) then predicate filter | No exact Flat pad; shortfall → −1 (honest POST) |
| Predicates | Bernoulli seed=42 (same as NumPy microbench) | Synthetic; not real metadata |
| n_queries | **1000**; k=10; N=1 000 000 | Feasible on this box |

Harness: `rql-repro/code/bench/fanns_sift1m_faiss_microbench.py` (faiss-cpu 1.15.1).

**Integrity note:** `IDSelectorBitmap` holds a raw pointer into the packed bit buffer — caller must keep the NumPy buffer alive for the duration of search (fixed in harness).

## Results
Run dir (both repos): `experiments/results/fanns/sift1m_faiss_HNSW32_20260917_022017/` (+ repro twin under `rql-repro/results/fanns/`).

| s | mode | recall@10 | p50 ms | p95 ms | QPS |
|--:|------|----------:|-------:|-------:|----:|
| 0.01 | PRE | 0.536 | 0.233 | 0.308 | 4284 |
| 0.01 | POST | 0.514 | 1.599 | 1.936 | 606 |
| 0.05 | PRE | 0.825 | 0.236 | 0.362 | 4159 |
| 0.05 | POST | 0.996 | 1.549 | 2.032 | 652 |
| 0.10 | PRE | 0.897 | 0.235 | 0.311 | 4256 |
| 0.10 | POST | 0.998 | 1.490 | 1.769 | 692 |
| 0.50 | PRE | 0.969 | 0.234 | 0.286 | 4368 |
| 0.50 | POST | 1.000 | 1.474 | 1.768 | 698 |

Wall time (total): **~87 s** (HNSW build ~71 s; search+GT ~15 s). CPU: Intel Xeon, 8 OMP search threads.

## Reading (honest)
- At s≥0.05, **POST** with candidate mult=50 is near-exact vs filtered Flat GT; **PRE** is faster (~0.23 ms p50) but trails POST recall until high selectivity.
- At s=0.01 both modes ~0.51–0.54 recall — expected for vanilla HNSW+filter / shallow POST pool (motivates predicate-aware methods; **do not** cite as ACORN reproduction).
- Stronger than NumPy brute plumbing; still synthetic predicates; single efSearch / mult setting (not a full depth sweep).

## 1–5% seed
FAISS-index curves close the “no index yet” gap from `0037`; live adapters + judgments remain open.

## Uncertainty / non-claims
- Not ACORN / Filtered-DiskANN / paper table reproduction.
- Not live Qdrant/ES/pgvector smoke; not RAG judgments.
- HNSW build has no public FAISS seed (OpenMP multi-thread add).

## Next questions
- Optional: efSearch / candidate-mult sweep; IVF4096,Flat secondary curve.
- P1 live adapters; P1 judgments.
- Do **not** push unless human requests.
