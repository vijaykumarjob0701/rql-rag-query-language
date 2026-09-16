# 0003 — Adjacent brainstorm & deep dive (v2)

**When:** 2026-09-16 (Europe/Dublin)  
**Artifacts:** [`../docs/05-brainstorm-adjacent.md`](../docs/05-brainstorm-adjacent.md), [`../docs/06-deep-literature.md`](../docs/06-deep-literature.md), [`../docs/07-evolved-idea.md`](../docs/07-evolved-idea.md), [`../NOTES-search-log.md`](../NOTES-search-log.md)

---

## Context

v1 answered “what exists on vector DBs?” v2 asks the transformer-style question: **what adjacent fields already solved analogous problems under different names?**

## Question asked

Which sideways literatures supply operators, planner vocabulary, shims, budgets, and physical strategies that RQL should *steal* rather than invent?

## Where we looked

Adjacent angles (22) spanning: Indri/Galago/CQL; PostGIS/GiST; array DBs; BlinkDB/AQP; Calcite/Cascades; BigDAWG/Substrait; Datalog; filtered ANN (ACORN, Filtered-DiskANN, …); ColBERT/MUVERA; GraphRAG; Lara/SystemDS; HyDE; provenance; VSS joins; learned FANNS planners.

Surfaces: arXiv, primary PDFs, SIGMOD-era pages, standards (CQL), GitHub for systems — logged in `NOTES-search-log.md`.

## What we read

**Breadth-first literature pass** (~28 papers/systems annotated in docs/06). Important honesty: this pass was largely **title/abstract/HTML + selective PDF text**, not the full multimodal Pass 1–5 protocol. Figures/tables were not systematically inventoried. Therefore **all aha insights below are provisional**.

## Aha insights (provisional — pending slow multimodal re-read)

1. **Retrieval as operator algebra** — classical IR `#combine` / `#weight` / fusion is closer to RQL’s heart than SQL SELECT nostalgia.  
2. **Filter strategy is physical, not logical** — PRE/POST/ITERATIVE/predicate-subgraph/partition; no universal winner (ACORN vs label-aware DiskANN vs surveys).  
3. **ANN as iterator** (VBASE-style) unlocks joins and pipelining better than TopK-RPC-only thinking.  
4. **Portable plans beat portable SQL skins** — Substrait / BigDAWG shim doctrine.  
5. **Budgets are first-class** — BlinkDB-like recall/latency targets for approximate search.  
6. **Late interaction needs rewrite rules** — ColBERT/MUVERA as leaves + physical rewrites.  
7. **Multi-hop as bounded recursion** — GraphRAG/Datalog, not ad-hoc agent loops only.  
8. **Tiny kernel** — Lara-like join ∪ union ∪ ext plus score/channel attributes.

docs/07 re-framed RQL as **retrieval algebra + cost-based physical planner**; textual DSL is a frontend.

## 1–5% seed (meta)

The unlock was **methodological**: sideways search changes the thesis more than more vendor API pages. But the *evidence quality* for each stolen piece is still too thin until figures/tables are re-read.

## Uncertainty

- Venue/camera-ready status for several arXiv entries  
- Whether docs/07 algebra is overfitted to abstracts  
- Which provisional operators survive Pass 3–4 on primary PDFs  

## Next questions

- Slow down: define search/read/synthesis protocol before more dumps (→ 0004)  
- Multimodal re-read of 2–3 seeds from docs/06 (e.g. ACORN, RRF/fusion theory, Substrait or VBASE)  
- Do not invent further RQL syntax until promotion rules fire
