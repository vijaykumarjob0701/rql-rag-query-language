# 0025 — Substrait / Calcite IR adjacency (docs + paper pass)

**Date:** 2026-09-17 ~00:10 IST (Europe/Dublin)  
**Type:** multimodal / docs+spec adjacency read  
**Status:** Pass 1–5 complete for Substrait (spec/docs) + Calcite (Begoli et al. SIGMOD’18 / arXiv:1802.10233); Cascades (Graefe 1995) skimmed for citation grounding  
**Sources:**
- Substrait: https://substrait.io/ · about · relations/basics · logical_relations · physical_relations · extensions · serialization/basics  
- Calcite: Begoli et al., arXiv:1802.10233 / SIGMOD’18 (10 pp PDF)  
- Cascades (optional classic): Graefe, IEEE Data Eng. Bull. 18(3):19–29, 1995 (10 pp PDF)  
**Local extracts:** `tooling/scripts/extract_out/substrait_calcite_2026-09/` (`calcite-1802.10233.pdf`, `graefe-cascades-1995.pdf`, text dumps, page PNGs)  
**OKF bundles:** [`../knowledge/reads/substrait-spec-2026-09/`](../knowledge/reads/substrait-spec-2026-09/) · [`../knowledge/reads/calcite-begoli-sigmod18/`](../knowledge/reads/calcite-begoli-sigmod18/)  
**Prior seed:** journal 0024 → deeper Substrait / Apache Calcite read for IR adjacency

---

## Context

Journals 0021–0024 froze Hypothesis Logical/Physical JSON schemas, a toy parser, a capability-profile planner stub, and docs-shaped adapter emit — repeatedly citing Substrait/Calcite as *inspiration* without a careful source pass. This entry grounds what those systems **actually** establish, and what RQL may honestly claim as adjacency (inspired-by), **not** identity or implementation.

## Question asked

What portable-plan / optimizer-framework facts are **Established** in Substrait and Calcite (and Cascades for vocabulary), and how should RQL LogicalPlan/PhysicalPlan + capability negotiation be positioned relative to them without overclaiming that RQL implements Substrait or embeds Calcite?

## Where we looked

- Substrait site (home, about, relation basics, logical + physical relations, extensions, serialization basics) via WebFetch 2026-09-17  
- Full Calcite PDF multimodal: text extract + page PNG renders (Figs 1–4, Tables 1–2)  
- Cascades PDF skim (Fig. 1 task graph; enforcers; logical/physical properties) for citation depth  
- In-repo: thesis §03/§06/§07, schemas README, journals 0021–0024

---

## Pass 1 — Skim (what these appear to be about)

### Substrait
1. Cross-language **serialized compute / relational plan IR** — not a SQL replacement; plans, not SQL text.  
2. Plans = trees/DAGs of relations; binary (protobuf) + text serializations.  
3. Core logical ops (Read/Filter/Project/Join/Aggregate/…) + conventionally “physical” variants (HashJoin, Exchange, TopN, …).  
4. **No hard logical/physical split in the spec** — physicality is largely consumer convention.  
5. Strong **extension** story: YAML simple extensions (types/functions); AdvancedExtension optimization vs enhancement; ExtensionLeaf/Single/MultiRel custom relations.

### Calcite (Begoli et al.)
1. Embeddable framework: SQL parser/validator **or** RelBuilder → tree of relational operators → pluggable optimizer → adapters to heterogeneous backends.  
2. Deliberately omits storage/execution engines; mediates across engines.  
3. Physical properties via **traits** (ordering, partitioning, **calling convention**) rather than separate logical vs physical operator classes.  
4. Cost-based planner “similar to Volcano”; also exhaustive planner; rules + metadata providers.  
5. Adapters push operators into backend conventions; enumerable convention as client-side fallback.

### Cascades (Graefe 1995) — citation classic
1. Extensible optimizer after EXODUS/Volcano: tasks-as-objects, memoization, **enforcers**/glue for required physical properties, rules as objects, guided search.  
2. Vocabulary source for “Cascades-style” planners (not a claim that RQL implements Cascades).

---

## Pass 2 — Multimodal / docs inventory

### Substrait (docs; no single PDF primary)
| Kind | Notes |
|------|-------|
| Spec sections | About/vision; Relation basics (Emit, Hints, Constraints, distribution, orderedness); Logical relations (Read w/ filter + best_effort_filter, Filter, Project, Join, Set, Aggregate, Fetch, Reference, Write, …); Physical relations (Hash/NLJ/Merge Join, Exchange, Top-N, Hash/Streaming Aggregate, …); Extensions; Serialization |
| Key design facts | Plan = relation tree/DAG via ReferenceRel; functions extend via YAML URNs; relations extend via Extension*Rel + protobuf `Any` detail |
| Physicality | Spec text: *“There is no true distinction between logical and physical operations in Substrait”* — convention of consumer |
| Serializations | Binary (Plan / PlanRel) + human text |

### Calcite PDF (10 pages)
| Kind | IDs |
|------|-----|
| Sections | §1 Intro → §2 Related → §3 Architecture → §4 Query algebra → §5 Adapters → §6 Query processing/optimization → §7 Extending → §8 Adoption → §9 Future → §10 Conclusion |
| Figures | Fig.1 architecture (parser/builder → operator expressions → optimizer rules/metadata → backends); Fig.2 cross-engine optimization (Splunk×MySQL conventions); Fig.3 adapter SchemaFactory/Schema/Table; Fig.4 FilterIntoJoinRule before/after |
| Tables | T1 systems embedding Calcite; T2 adapters / target languages |
| Algorithms | Implicit: Volcano-like DP equivalence sets + digests; no numbered Alg. block |

**Miss checklist:** opened all figure pages via PNG renders; captions captured; tables understood from captions/body; Cascades Fig.1 (Optimize/Explore/Apply Rule tasks) viewed for vocabulary.

### Cascades PDF (10 pages)
| Kind | Notes |
|------|-------|
| Fig.1 | Optimization tasks: Optimize Group/Expression, Explore Group/Expression, Apply Rule, Optimize Inputs |
| Concepts | Enforcers for physical properties; memo; pattern-guided exploration vs Volcano’s full expand-then-optimize |

---

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| Substrait about | motivates | “plans not SQL” doctrine | Established project vision |
| Substrait physical_relations | qualifies | logical/physical split | **No true distinction** in spec |
| Substrait extensions | implements | custom retrieval ops path | Extension*Rel / AdvancedExtension |
| Calcite Fig.1 | introduces | operator-tree IR + pluggable rules | Architecture |
| Calcite §4 traits | implements | physical props without dual operator taxonomies | calling convention |
| Calcite Fig.2–3 + §5 | implements | adapter pushdown / multi-backend | enumerable fallback |
| Calcite §6 | cites-sideways | Volcano DP | cost-based engine |
| Cascades Fig.1 / enforcers | grounds | Cascades vocabulary | optional cite for “Cascades-style” |
| RQL schemas 0021 | **inspired-by** (Hypothesis) | Substrait portable IR + Calcite logical→physical/adapters | **not** identity |

---

## Pass 4 — Seed (1–5%)

### ESTABLISHED (source facts)

1. **Substrait** is an open, cross-language specification for **serialized relational/compute plans** (binary + text), designed so producers/consumers exchange **plans rather than SQL text**; SQL remains a human frontend that systems lower to plans.  
2. Substrait plans are **trees (or DAGs via ReferenceRel)** of relational operators with declared signatures, emit/ordering, optional hints/constraints, distribution & orderedness properties.  
3. Substrait **does not enforce** a hard logical vs physical IR split; “physical” operators (HashJoin, Exchange, TopN, …) are conventional; the consuming system decides what counts as a physical plan.  
4. Substrait provides **extension points**: YAML simple extensions (types, scalar/agg/window/table functions via extension URNs); `AdvancedExtension` (**optimization** = ignorable hints vs **enhancement** = semantic-changing); custom **ExtensionLeafRel / ExtensionSingleRel / ExtensionMultiRel** with producer/consumer-agreed `detail` schemas.  
5. **Apache Calcite** (Begoli et al.) is an embeddable relational algebra + optimizer framework over **heterogeneous** sources: parser/RelBuilder → operator tree → rules + metadata + planner engines → **adapters** with **calling-convention** traits; storage/execution omitted by design.  
6. Calcite represents physical properties primarily via **traits** (ordering, grouping, partitioning, calling convention), not a mandatory separate logical/physical operator class hierarchy; converters enforce traits; enumerable convention implements missing backend ops client-side.  
7. Calcite’s cost-based planner uses **Volcano-like dynamic programming** over equivalence sets/digests; a second exhaustive rule engine exists; both are pluggable.  
8. **Cascades** (Graefe 1995) supplies classic vocabulary: task-based search, memoization, **enforcers** for required physical properties, rule objects, guided exploration — lineage behind many “Cascades/Volcano-style” citations (including Calcite’s related-work framing).

### HYPOTHESIS (RQL packaging — adjacency only)

> RQL’s draft LogicalPlan / PhysicalPlan JSON (0.1.0-draft) and capability-negotiated compile stack (parser → planner stub → emit stub) are **Substrait-inspired** (portable plan IR; extensions for retrieval-specific ops; adapters as consumers) and **Calcite-inspired** (logical algebra + physical strategies via capability/traits; pushdown vs shim; fail-closed when capability missing).  
> This does **not** claim: RQL implements Substrait protobuf; RQL is a Calcite extension; RQL ships a Cascades cost model; or that vector/ANN/fusion ops are already in the Substrait core.

### Mapping table (honest adjacency)

| Established prior | RQL Hypothesis analogue | Must not claim |
|-------------------|-------------------------|----------------|
| Substrait Plan / Rel tree | `LogicalPlan` / `PhysicalPlan` JSON trees | Wire-compatible Substrait |
| Extension*Rel / YAML functions | `Ext`, `Search_*`, `Fuse_*`, `LateInteractExec` as domain ops | Official Substrait dialect today |
| AdvancedExtension optimization vs enhancement | budgets / EXPLAIN hints vs semantic ShimCast | Same protobuf Any layout |
| Calcite traits / calling convention | `capabilities.*` profiles + FilterExec modes | Calcite RelTraitDef implementation |
| Calcite adapters + enumerable fallback | vendor emit + ShimCast | Live Calcite adapter |
| Cascades enforcers | ShimCast / explicit client fuse when trait missing | Cascades memo search |

### Anti-overclaim

- RQL ≠ Substrait implementation or fork.  
- RQL ≠ Calcite embedding.  
- Journal 0023 planner stub ≠ Cascades/Volcano cost-based search.  
- No fabricated interoperability demos with Arrow/DataFusion/Spark Substrait consumers.

### Uncertainty

- Exact Substrait release/version pins for each fetched page (docs are living; accessed 2026-09-17).  
- Whether a future “retrieval island” belongs as Substrait custom relations vs a separate IR that *emits* Substrait for relational tails only.  
- Calcite paper is 2018 SIGMOD; project APIs (RelBuilder docs) evolve — architecture claims anchored to paper + official algebra docs skim.

---

## Pass 5 — Next queries / seeds

1. **E2E CLI glue:** `rql → parse → plan → emit` single command over toy examples (still no live DB).  
2. **Human P0 pause checklist:** protocol 03 live smoke; decide whether Substrait Extension*Rel prototype is in-scope or defer.  
3. Optional: skim Arrow/DataFusion Substrait producer/consumer docs for interchange reality-check (not required to keep honesty).  
4. Optional: Calcite `VolcanoPlanner` javadoc + one adapter rule example as deeper implementation cite (paper already sufficient for adjacency).

## Promote?

- **Promote to thesis §03/§07:** Established Substrait/Calcite adjacency paragraphs + strengthened Hypothesis “inspired-by” wording.  
- **Do not promote:** any claim that RQL *is* Substrait or that schemas are standards-stable.

## Artifacts touched this entry

- Journal 0025; OKF `substrait-spec-2026-09/` + `calcite-begoli-sigmod18/`  
- Thesis §03 related-work, §07 compilation (+ abstract/conclusion); bib notes  
- `schemas/README.md` extension-points note; CHANGELOG; NOTES; knowledge/journal indexes  
- PDF rebuild — **no push**
