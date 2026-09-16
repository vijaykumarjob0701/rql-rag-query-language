# Google Colab notebook links

Stable Drive/Colab URLs for notebooks used in this research. Keep this file updated whenever a new Colab notebook is created or re-uploaded.

| Notebook (repo path) | Colab URL | Runtime used | Results path | Notes |
|----------------------|-----------|--------------|--------------|-------|
| [`fanns_microbench_colab.ipynb`](fanns_microbench_colab.ipynb) | https://colab.research.google.com/drive/1FH33zBXZezHLS3cSAR5nJQdELxX29s_A | T4 GPU (`faiss-gpu` 1.15.1) | [`../results/fanns/colab_synth_20260916_233628/`](../results/fanns/colab_synth_20260916_233628/) | Synthetic N=50k d=128 PRE/POST — **not P0** (SIFT1M skipped) |

## How to open

Click the Colab URL while signed into the same Google account that owns the Drive file, or open from [Colab](https://colab.research.google.com/) → recent uploads.

## Policy

- Prefer committing the `.ipynb` in-repo **and** listing the live Colab URL here.
- Do not commit multi-GB datasets; only `metrics.json` / `ENV.txt` / `plans/`.
