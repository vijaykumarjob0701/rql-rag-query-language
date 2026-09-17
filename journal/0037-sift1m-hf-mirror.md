# 0037 — SIFT1M obtained via Hugging Face mirror; digests + microbench

**Date:** 2026-09-17 ~01:22 IST (Europe/Dublin)  
**Type:** dataset acquisition + empirical smoke  
**Status:** SIFT1M **obtained**; digests filled; subset **and** full microbench ran

## Context
Journal `0036` recorded TexMex HTTPS SSL failure and large synthetic fallback. P0 still needed a licensed ANN set with digests in the companion registry.

## Question asked
Can we obtain SIFT1M from a working mirror, record real SHA-256 digests, and run a PRE/POST filtered microbench (subset first)?

## Where we looked / what worked
| Mirror | Result |
|--------|--------|
| Hugging Face `qbo-odp/sift1m` HTTPS | **Working** (preferred) — downloaded 2026-09-17 |
| FTP `ftp.irisa.fr/.../sift.tar.gz` | Documented as fallback (not needed this run) |
| ANN-Benchmarks HDF5 | Documented alternate format |
| TexMex HTTPS | Still **dead** (SSL/404) |

## Digests (HF download → `rql-repro/datasets/cache/sift1m/SHA256SUMS`)
| File | sha256 |
|------|--------|
| `sift_base.fvecs` | `21f66e2975057b5728ba56de1c825bac4f4d89d596609ae985741c6242631816` |
| `sift_query.fvecs` | `f7fc9be140accdfd64116c2fa2365ecdb69b8f084970c6b0532db5ff79ac8fdc` |
| `sift_groundtruth.ivecs` | `2b71de0a8d5a83e6a84eec3e23fb8b611d8801dd9b3a6cd62f070ab65ea65f4f` |
| `sift_learn.fvecs` | `331bc82b6a0e89465776a3ba0c2113e0bd0cceaa014ec3ed639bc8b981af72ea` |

License note: INRIA TexMex / academic ANN evaluation; HF is a **redistribution mirror**.

## Microbench
Harness: `rql-repro/code/bench/fanns_sift1m_microbench.py` (NumPy brute PRE/POST, synthetic Bernoulli selectivities).

| Run | Path | Label |
|-----|------|-------|
| Subset (n=100k, nq=100) | `experiments/results/fanns/sift1m_subset_20260917_012242/` (+ repro twin) | **subset smoke — not full P0 alone** |
| Full (n=1M, nq=100) | `experiments/results/fanns/sift1m_full_20260917_012246/` (+ repro twin) | full microbench (still NumPy brute / not FAISS index P0) |

No memory failure on this 15 GiB box for full load + 100 queries.

## 1–5% seed
TexMex HTTPS is not required — HF mirror + FTP restore the P0 data path; digests belong in companion `REGISTRY.md`.

## Uncertainty
- Full run is exact/brute PRE/POST plumbing, not an HNSW/IVF index sweep — venue-grade P0 still needs chosen ANN library + candidate-depth sweeps.
- Official `sift_groundtruth.ivecs` is **unfiltered**; filtered GT is recomputed in-harness.

## Next questions
- Wire FAISS (CPU/GPU) index modes and candidate-depth sweeps on the same cache.
- Update Colab cells to try HF URLs before TexMex (done in-repo notebooks).
- Do **not** push from agents unless human requests.
