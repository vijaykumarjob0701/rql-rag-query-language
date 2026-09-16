# Research journal — read this first

**Purpose:** Make the RQL research path legible on GitHub. Each entry is one *thinking step*, in chronological order. A newcomer should be able to walk `0001 → 0002 → …` and see how questions, searches, multimodal reads, 1–5% seeds, and next questions evolved — without treating early dumps as final truth.

**Date convention:** Europe/Dublin timestamps in entry headers.

---

## Convention

One file per thinking step:

```
journal/NNNN-short-slug.md
```

Numbered monotonically (`0001`, `0002`, …). Do not rewrite history; add a later entry that corrects an earlier provisional claim.

### Each entry should answer

| Section | What to write |
|---------|----------------|
| **Context** | Where we were in the project |
| **Question asked** | What we were trying to find out |
| **Where we looked** | Surfaces + query families (or “methodology only”) |
| **What we read** | Sources touched; note if multimodal protocol was used |
| **1–5% seed** | The unlock insight (or “none yet — process change”) |
| **Uncertainty** | What remains fuzzy |
| **Next questions** | Concrete follow-ups |

### Relationship to other folders

| Folder | Role |
|--------|------|
| `journal/` | Chronological *thinking* (this index) |
| `methodology/` | Reusable slow-path protocols |
| `tooling/` | Scripts/libraries to support multimodal reads |
| `docs/` | Synthesized artifacts (landscape, literature, evolved idea) — may lag journal honesty |
| `NOTES-search-log.md` | Raw query log (optional detail behind journal) |

### Provisional vs settled

Early entries (especially v2 adjacent brainstorm) produce **provisional** seeds. They are not promoted to settled RQL algebra until multimodal re-read under [`../methodology/02-read-protocol.md`](../methodology/02-read-protocol.md) and the promotion rules in [`../methodology/03-preprocess-and-synthesis.md`](../methodology/03-preprocess-and-synthesis.md).

---

## Index (chronological)

| # | Entry | One-line summary |
|---|-------|------------------|
| 0001 | [`0001-initial-question.md`](0001-initial-question.md) | Original RAG / vector QL question; goals (accuracy, reliability, speed) |
| 0002 | [`0002-first-landscape-pass.md`](0002-first-landscape-pass.md) | v1 direct survey of vendor APIs & emerging languages |
| 0003 | [`0003-adjacent-brainstorm-deep-dive.md`](0003-adjacent-brainstorm-deep-dive.md) | v2 sideways angles + provisional aha insights |
| 0004 | [`0004-slow-path-methodology.md`](0004-slow-path-methodology.md) | Decision to slow down; strategy + multimodal tooling |
| 0005 | [`0005-okf-correction.md`](0005-okf-correction.md) | User correction: Google **OKF** (Open Knowledge Format), not LangExtract |
| 0006 | [`0006-acorn-multimodal-reread.md`](0006-acorn-multimodal-reread.md) | ACORN Pass 1–5 multimodal re-read + OKF bundle |
| 0007 | [`0007-vbase-seed-stub.md`](0007-vbase-seed-stub.md) | VBASE queued stub — **superseded by 0009** |
| 0008 | [`0008-human-todos-hand-off.md`](0008-human-todos-hand-off.md) | HUMAN_TODO list for benches Vijay must run |
| 0009 | [`0009-vbase-multimodal-reread.md`](0009-vbase-multimodal-reread.md) | VBASE OSDI’23 Pass 1–5 + OKF bundle |
| 0010 | [`0010-filtered-diskann-multimodal-reread.md`](0010-filtered-diskann-multimodal-reread.md) | Filtered-DiskANN WWW’23 Pass 1–5 + OKF |
| 0011 | [`0011-rrf-cormack-multimodal-reread.md`](0011-rrf-cormack-multimodal-reread.md) | Cormack RRF SIGIR’09 Pass 1–5 + OKF (Fuse_rrf established) |
| 0012 | [`0012-colbert-multimodal-reread.md`](0012-colbert-multimodal-reread.md) | ColBERT SIGIR’20 Pass 1–5 — MaxSim **Established** |
| 0013 | [`0013-muvera-multimodal-reread.md`](0013-muvera-multimodal-reread.md) | MUVERA arXiv:2405.19504 Pass 1–5 — FDE rewrite |
| 0014 | [`0014-plaid-multimodal-reread.md`](0014-plaid-multimodal-reread.md) | PLAID CIKM’22 Pass 1–5 — centroid interaction Established |
| 0015 | [`0015-next-bruch-or-human-note.md`](0015-next-bruch-or-human-note.md) | Hand-off seed note (not a Pass 1–5) |
| 0016 | [`0016-bruch-fusion-multimodal-reread.md`](0016-bruch-fusion-multimodal-reread.md) | Bruch CC/TM2C2 vs RRF Pass 1–5 — Fuse_linear Established |
| 0017 | [`0017-chen-ecir2022-multimodal-reread.md`](0017-chen-ecir2022-multimodal-reread.md) | Chen ECIR’22 Pass 1–5 — resolves Bruch RRF-vs-CC cite-chase |
| 0018 | [`0018-montague-aslam-condorcet-multimodal-reread.md`](0018-montague-aslam-condorcet-multimodal-reread.md) | Montague–Aslam Condorcet-fuse CIKM’02 Pass 1–5 — Fuse_condorcet sibling |
| 0019 | [`0019-fanns-lin2025-multimodal-reread.md`](0019-fanns-lin2025-multimodal-reread.md) | FANNS survey Lin 2025 Pass 1–5 — VSP/VJP/SJP/SSP → FilterExec |
| 0020 | [`0020-vendor-hybrid-api-matrix.md`](0020-vendor-hybrid-api-matrix.md) | Docs-only vendor hybrid/filter/fusion API matrix → RQL adapters |
| 0021 | [`0021-logical-physical-plan-schema-v0.1.md`](0021-logical-physical-plan-schema-v0.1.md) | Draft LogicalPlan/PhysicalPlan JSON Schema v0.1.0-draft (Hypothesis IR) |
| 0022 | [`0022-toy-rql-parser.md`](0022-toy-rql-parser.md) | Toy RQL → LogicalPlan parser (Hypothesis subset; 4/4 validate) |
| 0023 | [`0023-physical-planner-stub.md`](0023-physical-planner-stub.md) | Logical→Physical planner stub (Hypothesis; 12/12 validate) |
| 0024 | [`0024-adapter-emit-stub.md`](0024-adapter-emit-stub.md) | PhysicalPlan → vendor emit stub (Hypothesis sketches; 6/6; not executed) |
| 0025 | [`0025-substrait-calcite-ir-adjacency.md`](0025-substrait-calcite-ir-adjacency.md) | Substrait/Calcite IR adjacency Pass — Established priors; RQL inspired-by only |
| 0026 | [`0026-e2e-pipeline-cli.md`](0026-e2e-pipeline-cli.md) | Offline E2E CLI glue (parse→plan→emit; 12/12; no live DB) |
| 0027 | [`0027-pause-human-p0-checklist.md`](0027-pause-human-p0-checklist.md) | Pause / human P0 checklist hand-off |
| 0028 | [`0028-human-colab-results-paths.md`](0028-human-colab-results-paths.md) | Human+Colab result paths; synthetic CPU smoke (not P0) |
| 0029 | [`0029-colab-fanns-synth-run.md`](0029-colab-fanns-synth-run.md) | Colab T4 synthetic FANNS PRE/POST run + notebook URL |
| 0030 | [`0030-thesis-fold-colab-synth.md`](0030-thesis-fold-colab-synth.md) | Thesis fold: Colab synth as plumbing + qualitative PRE/POST (not P0) |
| 0031 | [`0031-blinkdb-aqp-budgets-multimodal-reread.md`](0031-blinkdb-aqp-budgets-multimodal-reread.md) | BlinkDB EuroSys’13 Pass 1–5 — AQP budgets → RECALL/LATENCY |
| 0032 | [`0032-hyde-multimodal-reread.md`](0032-hyde-multimodal-reread.md) | HyDE ACL’23 Pass 1–5 — Rewrite / REWRITE HYDE |

Also: OKF-shaped notes under [`../knowledge/reads/`](../knowledge/reads/) (`acorn-2403.04871`, `vbase-osdi23`, `filtered-diskann-www23`, `rrf-cormack-sigir09`, `colbert-sigir20`, `muvera-2405.19504`, `plaid-cikm22`, `bruch-arxiv-2210.11934`, `chen-ecir2022-2201.10582`, `montague-aslam-cikm02-condorcet`, `fanns-lin2025-2505.06501`, `substrait-spec-2026-09`, `calcite-begoli-sigmod18`, `blinkdb-eurosys13`).

*Add new rows here when you add entries.*
