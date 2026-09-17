# Datasets (HUMAN)

**Policy:** Do not commit multi-GB binaries without an explicit LFS decision. Record URLs, licenses, digests, and gitignored local paths. See [`../HOW_TO_PROVIDE_RESULTS.md`](../HOW_TO_PROVIDE_RESULTS.md) and [`../protocols/02-datasets.md`](../protocols/02-datasets.md).

## Canonical registry (companion repro)

**Authoritative digests + download script live in `rql-repro`:**

- Registry: https://github.com/vijaykumarjob0701/rql-repro/blob/main/datasets/REGISTRY.md  
  (local checkout: `/workspace/rql-repro/datasets/REGISTRY.md`)
- Download: `rql-repro/datasets/scripts/download_sift1m.sh` (HF → FTP)
- Cache path (gitignored): `rql-repro/datasets/cache/sift1m/`

Do **not** duplicate multi-GB files here. Optional empty `experiments/datasets/data/` stays gitignored.

## SIFT1M (filled 2026-09-17 Europe/Dublin)

| Dataset | Preferred URL | License | Digest (sha256) | Local path (repro, gitignored) | Ground-truth |
|---------|---------------|---------|-----------------|--------------------------------|--------------|
| **SIFT1M** | HF `qbo-odp/sift1m` | INRIA TexMex / academic ANN; HF is redistribution mirror | see companion REGISTRY (base `21f66e29…`, query `f7fc9be1…`, gt `2b71de0a…`, learn `331bc82b…`) | `rql-repro/datasets/cache/sift1m/` | `sift_groundtruth.ivecs` (unfiltered 100-NN) |

| Mirror | Status |
|--------|--------|
| Hugging Face HTTPS `qbo-odp/sift1m` | **Working** (preferred) |
| FTP `ftp://ftp.irisa.fr/local/texmex/corpus/sift.tar.gz` | Working |
| ANN-Benchmarks HDF5 | Working (different format) |
| TexMex HTTPS `corpus-texmex.irisa.fr` | **Dead** (SSL/404) |

## Notes

- Accept license terms before download.
- FANNS P0 expects a licensed set (e.g. SIFT1M) plus synthetic predicates at selectivities `{0.01, 0.05, 0.1, 0.5}`.
- Microbench harness: `rql-repro/code/bench/fanns_sift1m_microbench.py` (subset default; `--full` optional).
