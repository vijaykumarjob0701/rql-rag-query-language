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

*Add new rows here when you add entries.*
