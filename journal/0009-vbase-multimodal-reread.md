# 0009 — VBASE multimodal re-read (Pass 1–5)

**Date:** 2026-09-16 ~22:48 IST (Europe/Dublin)  
**Type:** multimodal source read  
**Status:** Pass 1–5 complete for this source (seed provisional for RQL algebra)  
**Source:** Zhang, Xu, Chen, Sui, Xie, Cai, Chen, He, Yang, Yang, Yang, Zhou — *VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity* — OSDI 2023 (USENIX), pages 377–395  
**Verified identity:** WebSearch + USENIX presentation page + dblp + PDF title page (same title; **not** a different “Ending the Anomaly…” paper)  
**URLs:** https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi · https://www.usenix.org/system/files/osdi23-zhang-qianxi_1.pdf · MSR publication page · https://github.com/microsoft/MSVBASE  
**Local PDF:** `tooling/scripts/extract_out/vbase-osdi23-zhang.pdf` (20 pp)  
**Extract dir:** `tooling/scripts/extract_out/vbase_osdi23/` (`extract_document.py` + `relate_components.py`; 16 embedded rasters, 149 nodes / 306 edges)  
**OKF bundle:** [`../knowledge/reads/vbase-osdi23/`](../knowledge/reads/vbase-osdi23/)  
**Supersedes:** stub narrative in [`0007-vbase-seed-stub.md`](0007-vbase-seed-stub.md) (stub retained as history)

---

## Context

After ACORN (`0006`), `ITERATIVE` / Open–Next ANN was still only a queued hypothesis. VBASE is the primary published system tying high-dim ANN traversal to Volcano-style relational iterators via **relaxed monotonicity**.

## Question asked

Does VBASE actually expose vector similarity as a **monotonic-enough iterator** (`Open`/`Next`/`Close`) composable with relational operators (filter during traversal, multi-column TopK, distance range, similarity join), and which figures/defs ground relaxed monotonicity vs plain TopK RPC?

## Where we looked

- Downloaded USENIX camera PDF; ran extract + relate under `tooling/.venv`
- Full-text skim + section map; Table 1 / Tables 4–8 captions; Def. 1 + Eqs. 1–3
- Visual Pass 2: rendered p.5 (Fig. 1–2 traversal / neighbor sphere); reviewed caption inventory for Figs. 3–8 and eval tables
- Honest gaps: many “figures” are vector drawings; embedded XObjects on p.7/p.10 largely black/logo-ish; table cells OCR-noisy — cite author prose carefully, do not invent metrics

## Pass 1 — Skim (what this appears to be about)

1. High-dim vector indices lack classical **monotonicity**, so DBs wrap them via tentative TopK “soft indices” with hard-to-predict \(K'\).
2. Authors observe a common **two-phase** ANN traversal (approach then steadily depart) and formalize **Relaxed Monotonicity** (Def. 1 / Eq. 3).
3. Unified engine on **Volcano iterator model**: adapt ANN to `Open`/`Next`/`Close`; terminate when original condition **and** relaxed-monotonicity check hold.
4. Supports S1–S4: single TopK; TopK+scalar filter; multi-column TopK; distance range; plus vector **Join** via range-filter index join.
5. PostgreSQL implementation (~2k LOC); recipe hybrid dataset eval; **AUTHOR-CLAIM** large speedups (up to ~10³× online; ~7000× join vs scan) — **not reproduced here**.
6. Related-work tokens: AnalyticDB-V, PASE, Milvus, Elasticsearch, SPANN, FAISS IVFFlat, HNSW, NRA.

## Pass 2 — Multimodal inventory (summary)

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro → §2 Background (S1–S4; DB vs vector division) → §3 Design (3.1 RM, 3.2 unified engine, 3.3 equivalence) → §4 Implementation (RM check, engine, planning, multi-column) → §5 Evaluation → §6 Related → §7 Conclusion |
| Figures | Fig.1 IVFFlat/HNSW distance-vs-steps traversal; Fig.2 neighbor sphere \(R_q\), window median \(M^s_q\); Fig.3 result-equivalence schematic (caption noisy in extract); Fig.4–5 multi-column / multi-index traversal; Fig.6 p99 latency; Fig.7 Q-error vs selectivity; Fig.8 planning estimation |
| Tables | T1 online query support matrix (S1–S4 × systems); T2–T3 recipe/tag schemas; T4 8-query latency/recall overview; T5 scalar filter × selectivity; T6 range; T7 multi-column; T8 SPANN |
| Algorithms / APIs | No numbered “Algorithm 1” in extract; physical APIs **Open / Next / Close** for HNSW, IVFFlat, SPANN (§4.2) |
| Equations | (1) \(R_q\); (2) \(M^s_q\) median over window \(w\); (3) Def.1 \(\exists s,\forall t\ge s: M^t_q \ge R_q\) |

**Miss checklist:** figure/table pages viewed via pdftoppm + captions; captions in `relations.json`; table *headers* understood (numeric cells noisy); refs/ack through p.20; vector figures without usable XObjects noted.

## Pass 3 — High-signal relationships (manual)

| From | Edge | To | Note |
|------|------|----|------|
| Fig.1 + §3.1 | introduces | two-phase traversal | motivates RM |
| Fig.2 + Eqs.1–3 | implements | Def.1 relaxed monotonicity | early-stop predicate |
| §3.2 Volcano | implements | Open/Next/Close ANN | iterator physical mode |
| §3.2 + §4.2 range/Join | grounds | filter-during-traversal + VSIM JOIN | vs post-TopK filter |
| §3.3 | qualifies | equivalence to optimal-\(eK\) TopK | semantic claim |
| T1 | grounds | S1–S4 coverage gap in prior systems | landscape |
| T4–T5 / Fig.6 | grounds | AUTHOR latency/recall claims | unreproduced |
| §4.3 planning | cites-sideways | selectivity / Q-error (Fig.7–8) | planner hooks |

## Pass 4 — Seed (1–5%)

**Observation** (what the source shows):

> Vector ANN indices are not classically monotonic, but practical IVFFlat/HNSW traversals exhibit a two-phase pattern that VBASE captures as **relaxed monotonicity** (neighbor-sphere radius \(R_q\) vs window median distance \(M^s_q\)). Exposing internal traversal as Volcano **`Open`/`Next`/`Close`** lets relational operators (OrderBy+limit, scalar predicates, distance range, index-nested-loop Join) **consume ANN as an iterator** and stop when both the operator’s condition and the RM check succeed—avoiding a brittle predicted over-fetch \(K'\). Authors claim large latency wins on hybrid SQL workloads and a vector join that prior TopK-only systems lack; we did not re-run those benches.

**Interpretation for RQL** (`[hypothesis]` only):

> Map VBASE-class backends to `FilterExec=ITERATIVE` (and capability `ann_iterator=true`). Logical `Search_dense` / `Filter` / `VSimJoin` may rewrite to iterator plans when the adapter exposes Next+RM (or equivalent early-stop). This complements ACORN’s `SUBGRAPH` and Filtered-DiskANN’s `SPECIALIZED`; it does **not** mean every HNSW library is VBASE. `VSIM JOIN` in provisional docs/07 is no longer abstract-only: VBASE shows a concrete index-join + range-filter pattern (AUTHOR eval unreproduced).

**Evidence pointers:** Fig.1–2, Def.1 / Eqs.1–3, §3.2–3.3, §4.2 (Open/Next/Close; range+Join), Table 1, Table 4–5, §7.

**Anti-overclaim — this seed does *not* justify:**

- Citing 10³× or 7000× as our results.
- Claiming RQL “is VBASE” or requires PostgreSQL.
- That relaxed monotonicity holds for every ANN index without checking.
- Promoting docs/07 algebra from provisional → settled solely on this read.

**Uncertainty:**

- Exact Fig.3 panel semantics (extract caption fragmentation).
- Table numeric OCR noise — paraphrase only.
- How closely MSVBASE / pgvecto.rs “vbase” flags match the OSDI paper (separate code read).
- Interaction of RM early-stop with ACL hard filters under adversarial selectivity (not stressed as RAG threat model here).

## Pass 5 — Next queries (mutations)

1. **Sibling specialized graphs:** Filtered-DiskANN FilteredVamana StitchedVamana (execute next — PDF already local)
2. **Fusion classic:** Cormack Clarke Buettcher reciprocal rank fusion SIGIR 2009 PDF
3. **Survey:** FANNS survey Lin 2025 arXiv:2505.06501 figure/table pass
4. **Systems follow-on:** MSVBASE GitHub Open/Next API surface vs paper §4.2
5. **Planner:** multi-column NRA / threshold algorithms with vector channels for RQL Fuse

## Promote?

- [x] Candidate to strengthen thesis §5–§6 / related-work **as hypothesis-labeled** citations  
- [ ] Not yet promote docs/07 to settled algebra
