# Datasets (HUMAN)

**Policy:** Do not commit multi-GB binaries without an explicit LFS decision. Record URLs, licenses, digests, and gitignored local paths here. See [`../HOW_TO_PROVIDE_RESULTS.md`](../HOW_TO_PROVIDE_RESULTS.md) and [`../protocols/02-datasets.md`](../protocols/02-datasets.md).

## Template

| Dataset | URL | License | Digest (sha256) | Local path (gitignored) | Ground-truth neighbors |
|---------|-----|---------|-----------------|-------------------------|------------------------|
| _e.g. SIFT1M_ | _fill_ | _fill_ | _fill_ | `experiments/datasets/data/sift1m/` | included / compute |

## Notes

- Accept license terms before download.
- Optional raw files under `experiments/datasets/data/` (see `.gitignore`).
- FANNS P0 expects a licensed set (e.g. SIFT1M) plus synthetic predicates at selectivities `{0.01, 0.05, 0.1, 0.5}`.
