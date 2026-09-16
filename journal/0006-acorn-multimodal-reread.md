# 0006 — ACORN multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source (seed provisional for RQL algebra)  
**Source:** Patel, Kraft, Guestrin, Zaharia — *ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data* — arXiv:2403.04871v1 (cs.IR), 7 Mar 2024  
**URLs:** https://arxiv.org/abs/2403.04871 · https://arxiv.org/pdf/2403.04871.pdf  
**Local PDF:** `tooling/scripts/extract_out/acorn2403.04871.pdf`  
**Extract dir:** `tooling/scripts/extract_out/acorn_smoke/` (inventory + relations re-verified 2026-09-16)  
**OKF bundle:** [`../knowledge/reads/acorn-2403.04871/`](../knowledge/reads/acorn-2403.04871/)

---

## Context

After `0004` (slow-path methodology) and `0005` (OKF correction), the first primary paper for Pass 1–5 is ACORN — repeatedly cited in provisional `docs/06`–`07` as the exemplar of **predicate-agnostic / predicate-subgraph** filtered ANN. Goal: ground those citations in multimodal evidence without promoting algebra claims yet.

## Question asked

What does ACORN *actually* contribute for hybrid vector+predicate search, which figures/tables ground the pre/post-filter critique and the subgraph idea, and what (if anything) is safely stealable for an RQL physical planner?

## Where we looked

- Local extract + `relate_components.py` (re-ran relate; extract already present from smoke test)
- Full text skim + section map
- Visual review of embedded figure assets (Pass 2 miss checklist): Fig.-related pages 2–6 (schematics), 10–13 (eval / graph quality)
- Caption inventory from `relations.json` (21 captions: Figures 1–13, Tables 1–6, Algorithms 1–2)
- Honest gaps: tooling `tables/` empty (tables are layout/vector, not extractable CSV); many numbered figures are vector drawings — we relied on captions + body + available rasters

## Pass 1 — Skim (what this appears to be about)

1. Hybrid search = ANN over vectors **plus** structured predicates (attributes/keywords/ranges).
2. Critiques **pre-filtering** (brute force on survivors) and **post-filtering** (ANN then drop; expensive under low selectivity / low query–predicate correlation).
3. Critiques specialized indices (Filtered-DiskANN / NHQ / HQANN) for **low-cardinality equality** predicates only.
4. Proposes **ACORN-γ** and **ACORN-1**: HNSW modifications enabling **predicate subgraph traversal** to emulate an *oracle partition* HNSW over \(X_p\) without building one index per predicate.
5. Claims large QPS gains at fixed high recall on SIFT1M, Paper, TripClick, LAION (incl. 25M scale).
6. Related-work field tokens for cite-chase: Filtered-DiskANN, NHQ, HQI, Weaviate/Milvus pre-post, Qdrant densify-HNSW.

## Pass 2 — Multimodal inventory (summary)

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro → §2 HNSW background → §3 problem (selectivity, query correlation) → §4 theoretical ideal / oracle partition → §5 ACORN overview (γ search/construct, ACORN-1) → §6 discussion → §7 evaluation → §8 related → §9 conclusion |
| Figures | Fig.1 HNSW search schematic; Fig.2 predicate clustering × query correlation; Fig.3 predicate subgraph; Fig.4 neighbor selection strategies (filter / compression heuristic / neighbor expansion); Fig.5 construction pruning/compression; Fig.6 LAION qualitative hybrid vs vector-only; Fig.7–11 recall@10 vs QPS (LCPS/HCPS, selectivity sweeps, scale); Fig.12 pruning methods; Fig.13 predicate-subgraph graph quality vs oracle |
| Tables | T1 notation; T2 datasets; T3 distance computations @0.8 recall; T4 TTI; T5 index size GB; T6 avg out-degree |
| Algorithms | Alg.1 (HNSW-related search / efs tradeoff — caption near §2); Alg.2 `ACORN-SEARCH-LAYER` |
| Equations | Selectivity \(s\); recall@K; oracle search complexity \(O_s(\log s n + K)\) cited in §4; γ / \(M_β\) construction params |

**Miss checklist:** opened figure/table-bearing pages via extract assets + captions; captions captured in relations; table *headers* understood from captions/body (numeric cells not CSV-extracted); appendix — paper is 15pp, figures through p13, refs p14–15; vector figures without XObjects acknowledged.

## Pass 3 — High-signal relationships (manual)

| From | Edge | To | Note |
|------|------|----|------|
| §3.2 + Fig.2 | introduces | query-correlation regimes | motivates why POST fails |
| §4 oracle partition | grounds | Fig.3 predicate subgraph | ideal vs practical approximation |
| Alg.2 + Fig.4 | implements | ACORN search neighbor selection | physical strategies |
| Fig.5 + §5.2 | implements | denser γ-neighbor construction + compression | index build |
| Fig.7–8 / T3 | grounds | SOTA QPS@recall claims | LCPS vs HCPS |
| Fig.9 | qualifies | selectivity sensitivity | planner must condition on \(s\) |
| Fig.13 | grounds | “subgraph ≈ HNSW” quality claim | SCC / height / degree |
| §8 | cites-sideways | Filtered-DiskANN, NHQ, HQI, vendor pre/post | next seeds |

## Pass 4 — Seed (1–5%)

**Observation** (what the source shows):

> Hybrid ANN+predicate has no single fixed strategy: pre-filter, post-filter, and specialized equality indices each fail outside their regime. ACORN’s useful abstraction is **search on the predicate-induced subgraph** of a denser, predicate-agnostic HNSW, approximating an oracle HNSW built only on \(X_p\). Workload axes that matter are **selectivity**, **scale**, and **query–predicate correlation** (Fig. 2). Empirically, ACORN-γ reports large throughput gains at high recall versus prior methods on both low- and high-cardinality predicate workloads (authors’ claims; we did not re-run their benchmarks).

**Interpretation for RQL** (`[hypothesis]` only):

> RQL should treat filtered search as a **physical planning problem**: `FilterExec ∈ {PRE, POST, ITERATIVE, SUBGRAPH, SPECIALIZED, AUTO}`, chosen using estimated selectivity and (when available) correlation / empty-result risk — not as a boolean bolted onto TopK. `SUBGRAPH` is one named capability (ACORN-like backends); capability negotiation must not pretend every vendor implements it. This seed does **not** yet define RQL algebra operators beyond what provisional `docs/07` already sketched.

**Evidence pointers:** Fig. 2, Fig. 3, Fig. 4, Alg. 2, §4, Fig. 7–9, Fig. 13, abstract QPS claim, §9.

**Anti-overclaim — this seed does *not* justify:**

- That RQL “includes ACORN” or that we have reproduced 2–1000× QPS.
- That predicate-subgraph is always optimal (ACORN itself is one design point; FANNS survey literature may show routers/partitions win elsewhere — unread here).
- Promoting `docs/07` algebra from provisional → settled.
- Claiming OKF is part of the RQL runtime (OKF is research-note packaging only).

**Uncertainty:**

- Exact Alg.1 identity vs standard HNSW SEARCH-LAYER (caption/text fragmentation in extract).
- Table cell values not machine-extracted; cite author prose carefully.
- Venue beyond arXiv v1 not verified in this pass (mark `[arxiv-only]` until camera-ready checked).
- Whether production HNSW libraries already absorbed ACORN-like densification (Qdrant densify mentioned in §8 — needs separate read).

## Pass 5 — Next queries (mutations)

1. **Sibling method:** `Filtered-DiskANN FilteredVamana StitchedVamana equality predicate cardinality` (PDF already linked in `docs/references.md` #57)
2. **Iterator ANN:** `VBASE relaxed monotonicity OSDI 2023 vector similarity iterator join`
3. **Fusion classic:** `Cormack Clarke Buettcher reciprocal rank fusion SIGIR 2009`
4. **Survey / router:** `FANNS filtered approximate nearest neighbor survey Lin 2025 arXiv:2505.06501`
5. **Selectivity planning:** `filtered ANN query planning selectivity correlation cost model 2026`

Log also in `NOTES-search-log.md` when those searches are executed.

## Promote?

- [x] Not yet for `docs/07` algebra (default)
- [ ] Candidate: only after Filtered-DiskANN or VBASE Pass 1–5 and methodology/03 gates

## Files produced this step

- This journal entry
- OKF-shaped bundle under `knowledge/reads/acorn-2403.04871/`
- CHANGELOG + journal README updates
