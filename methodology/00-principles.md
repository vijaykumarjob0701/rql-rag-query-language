# 00 — Slow Research Principles

**Date:** 2026-09-16 (Europe/Dublin)  
**Purpose:** Ground rules for RQL literature work. Methodology and tooling first; do **not** invent new algebra claims until sources have been re-read multimodally under this protocol.

Companion: [`01-search-strategy.md`](01-search-strategy.md) · [`02-read-protocol.md`](02-read-protocol.md) · [`03-preprocess-and-synthesis.md`](03-preprocess-and-synthesis.md) · [`04-iteration-loop.md`](04-iteration-loop.md).

---

## Why slow

The v2 literature dump ([`../docs/06-deep-literature.md`](../docs/06-deep-literature.md)) was a useful *funnel opener*. It is **provisional**. Paper titles and abstract takeaways are not the same as understanding a figure, a cost table, or a planner diagram. Rushing more dumps compounds that gap. The transformer analogy for RQL was never “read 28 abstracts”; it was “find the 1–5% that unlocks the next search.”

---

## Core principles

### 1. Re-read is the work

First contact with a source is inventory, not conclusion. Plan at least two full passes (skim + multimodal) before writing anything that sounds like a claim. Prefer re-reading one paper carefully over skimming five.

### 2. The 1–5% seed insight

Most of a paper is context. The useful residue is often a single definition, a taxonomy row, an EXPLAIN fragment, a failure case in a figure, or a related-work citation that names a field you had not searched. Capture that seed explicitly. Then **mutate the search** from the seed — do not keep repeating the original query.

### 3. Multimodal reading is mandatory

Academic PDFs encode meaning in:

- body text and footnotes  
- section structure and algorithms  
- figures (architectures, latency–recall curves, ablation bars)  
- tables (benchmarks, selectivity, parameter grids)  
- captions and in-text cross-references (“Figure 3”, “Table 2”)

Text-only extraction systematically misses planner diagrams and statistical trade-off plots that are often the actual seed. Treat missing a figure or table as a **protocol failure**, not a minor omission.

### 4. Relationship-first understanding

Do not store “figure exists” and “paragraph exists” as unrelated facts. Establish:

- which paragraph *introduces* a figure  
- which table *grounds* a textual claim  
- which algorithm box *implements* a named strategy  
- which citation *points sideways* to an adjacent field  

The relationship graph is the understanding; isolated snippets are not.

### 5. Uncertainty stays visible

Venue, year, and camera-ready status are often fuzzy from arXiv. Mark inference. Do not promote a provisional takeaway into [`../docs/07-evolved-idea.md`](../docs/07-evolved-idea.md) until the read protocol is complete and cross-paper comparison supports it.

### 6. Steal vocabulary before inventing syntax

Aligned with the project thesis in docs/07: prefer adopting shared vocabulary from IR, spatial SQL, filtered ANN, polystores, and planners. New RQL surface syntax is deferred until multimodal re-reads justify it.

### 7. Tooling assists; judgment decides

Python extractors (layout, tables, figures, relation heuristics) reduce miss-rate. They do not replace Pass 3 (relate) or Pass 4 (extract the seed). When extraction is partial, document honesty beats fake completeness.

---

## Anti-patterns (explicit)

| Anti-pattern | Why it hurts |
|--------------|--------------|
| Another bulk paper dump | Dilutes attention; freezes provisional claims |
| Abstract-only “implications for RQL” | Invents algebra without evidence |
| Text-only notes | Misses curves, taxonomies, EXPLAIN sketches |
| Query repetition without mutation | Stays in the same local minimum |
| Promoting ideas to docs/07 mid-skim | Contaminates the evolved thesis |

---

## Success signal

A successful slow cycle ends with: (a) a structured note for one source, (b) an explicit 1–5% seed, (c) 2–5 mutated next queries, and (d) an updated uncertainty list — **not** a longer literature markdown file.
