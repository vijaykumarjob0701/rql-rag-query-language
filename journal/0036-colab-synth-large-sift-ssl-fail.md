# 0036 — Colab large synthetic FANNS; SIFT1M SSL failure

**Date:** 2026-09-17 ~01:15 IST (Europe/Dublin)  
**Type:** empirical attempt  
**Status:** large synth results in-repo; **SIFT1M not obtained**

## Colab
- URL: https://colab.research.google.com/drive/1FH33zBXZezHLS3cSAR5nJQdELxX29s_A (saved)
- Runtime: T4 GPU **detected**, but FAISS GPU unavailable → **CPU** FAISS for this run

## SIFT1M
- Documented INRIA/TexMex URL `https://corpus-texmex.irisa.fr/sift.tar.gz`
- **Download failed:** SSL certificate hostname mismatch
- **No SIFT claims**

## What ran instead
- Synthetic Gaussian **N=200000** d=128, 100 queries, PRE/POST × 4 selectivities
- Artifacts: `experiments/results/fanns/colab_synth_large_20260917_001447/`
- Label: plumbing / scale-up smoke — **still not P0**

## Next for P0
- Obtain SIFT1M via alternate mirror or manual download with license note + digests into `rql-repro` registry
- Or use another licensed ANN set with GT neighbors
