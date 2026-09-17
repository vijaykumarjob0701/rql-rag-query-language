# 0034 — Thesis publishability / clarity / implementability polish

**Date:** 2026-09-17 ~01:15 IST (Europe/Dublin)  
**Type:** thesis structural + prose revision (no new empirics)  
**Status:** complete for this pass; PDF rebuild required  
**Integrity:** no fabricated metrics; no GitHub push; no NeurIPS/VLDB/SOTA claims

---

## Goal

Make `thesis/` good enough to publish as an **arXiv-style technical report / proposal + prototype**: clear for full-stack→ML→IR/DB readers, implementable against the toy harness, and honest about what is Established vs Hypothesis vs Provisional vs AUTHOR-only.

## What changed

### Framing
- Title block + banner: **technical report — proposal, prior-art grounding, and offline prototype**; explicit arXiv-style draft; not camera-ready venue submission.
- Honesty macros: added `\authoronly{}` alongside Established / Hypothesis / Provisional.
- Abstract rewritten: **problem → idea → contributions → status** (citation dump shortened; details stay in §03).

### Structure / readability
- §01: motivation triad; **5 numbered contributions**; **Reader's guide / how to implement RQL today**; paper roadmap.
- §02/§03: short reader pointers at section opens.
- §04: plain-language setting before formal requirements; sharpened non-goals.
- §05: plain-language dataflow + **hello RQL listing** (Figure); formalism retained.
- §06: plain-language physical choices before FilterExec set.
- §07: **E2E pipeline tikz** (`figures/e2e-pipeline.tikz`) + **Hello RQL walkthrough** with file paths and 12/12 pointer.
- §09: split **What we measured** vs **What remains for citation-grade ANN/RAG**.
- §10: limitations/threats sharpened (prototype≠compiler; docs-only matrix; synthetic≠P0; RAG external validity); fixed outdated “only ACORN multimodal” claim.
- §11: actionable next steps for implementers; arXiv-pending-P0 framing.
- `main.tex`: `listings`, `caption`, `enumitem`; status banner updated.
- `thesis/README.md`: build + **arXiv-ready draft pending P0** status table + engineer reader path.

### Figures / listings
- Existing: `figures/plan-layers.tikz`.
- New: `figures/e2e-pipeline.tikz`.
- New: toy hybrid RRF listing in §05 (`fig:hello-rql`).

### Non-changes (intentional)
- No new experimental numbers.
- Colab synth remains plumbing-only.
- Algebra/optimizer content preserved; packaging clarified.
- **No push.**

## Remaining gaps for a true venue paper

| Gap | Why it blocks venue submission | Suggested owner |
|-----|--------------------------------|-----------------|
| **P0 SIFT1M (or licensed large-set) FANNS** with GT kNN + recall/latency tables | Systems/IR venues expect measured ANN quality, not synthetic smoke | Human (GPU/Colab); protocols 01 |
| **Live adapter smoke (P1)** | Docs-only matrix + emit sketches ≠ validated portability | Human; protocol 03 |
| **Judgment-bearing retrieval/RAG eval** | Need BEIR/MS MARCO (license) and/or human judgments | Human; protocol 02 |
| **Cost model for AUTO** | Rule stub ≠ Cascades; ablations vs AUTO unmeasured | Research + eng |
| **Deeper Indri/Galago / polystore re-reads** | Still Provisional in places | Optional multimodal |
| **Camera-ready polish** | Copy-edit, tighter related-work compression, anonymity if needed | Pre-arXiv / pre-venue |
| **Optional Substrait dialect** | Nice systems story; not required for arXiv proposal | Future work |

## Suggested commits (do not push from agent)

1. `thesis: publishability polish — abstract/intro/reader guide, E2E figure, eval split`
2. `journal: 0034 thesis publishability polish + README/CHANGELOG`

Or a single commit if preferred.


## Concurrent note
Journal **0033** (MMR Carbonell Pass 1–5) was woven into thesis sections in the same window; this polish pass preserves those Established/Hypothesis labels and lists MMR among packaged priors. No conflict with publishability framing.

## Build note

After this entry: `cd thesis && latexmk -pdf -interaction=nonstopmode main.tex` and record page count below.

**Page count (post-build):** **25 pages** (`thesis/main.pdf`, latexmk 2026-09-17 ~01:15 IST; was 21 pages pre-polish)
