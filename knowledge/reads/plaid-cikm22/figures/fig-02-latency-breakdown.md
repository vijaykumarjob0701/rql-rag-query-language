---
type: Figure
title: "Figure 2 — Latency breakdown vanilla vs PLAID ColBERTv2"
tags: [plaid, figure]
status: provisional
---

# Figure 2

Stacked bars on TITAN V / MS MARCO v1: (a) vanilla ColBERTv2 ≈ **287 ms** dominated by index lookup + residual decompression; (b) PLAID ColBERTv2 (\(k=1000\)) ≈ **58 ms** with lookup/decompress/scoring collapsed.

**Use for RQL:** Motivates why a centroid-first physical plan exists — I/O and decompress dominate naive multi-vector search.
