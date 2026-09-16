# 0031 — BlinkDB multimodal re-read (Pass 1–5): AQP budgets → RECALL/LATENCY

**Date:** 2026-09-17 ~00:55 IST (Europe/Dublin)  
**Type:** multimodal source read (AQP budget / contract seed)  
**Status:** Pass 1–5 complete for this source  
**Source:** Agarwal, Mozafari, Panda, Milner, Madden, Stoica — *BlinkDB: Queries with Bounded Errors and Bounded Response Times on Very Large Data* — EuroSys ’13, pp. 29–42  
**URLs:** DOI [10.1145/2465351.2465355](https://doi.org/10.1145/2465351.2465355) · arXiv:1203.5485 · author PDF https://sameeragarwal.github.io/blinkdb_eurosys13.pdf  
**Local PDF:** `tooling/scripts/extract_out/blinkdb-1203.5485.pdf` (**16 pp**, arXiv v2 19 Jun 2012 — preprint of EuroSys’13; author list on arXiv omits Henry Milner present in ACM record)  
**Extract dir:** `tooling/scripts/extract_out/blinkdb_1203/` (39 XObjects / noisy table extracts; 139 nodes / 244 edges; `page_renders/page-01..16.png`)  
**OKF bundle:** [`../knowledge/reads/blinkdb-eurosys13/`](../knowledge/reads/blinkdb-eurosys13/)  
**Cite-chase of:** provisional BlinkDB cite in thesis §03/§06 / docs/07 evolved idea item 8; chosen over HyDE this turn to ground **budget contracts** before rewrite ops

---

## Context

RQL’s evolved idea and PhysicalPlan schema already expose Hypothesis `OPTION RECALL TARGET` / `LATENCY` and `budgets.recallTarget` / `budgets.latencyMs`, citing BlinkDB only as \provisional{}. After Colab synth fold (0030), the solid next seed was a full multimodal Pass 1–5 so we can label the **AQP dual-constraint + ELP mechanism** Established while keeping RQL packaging Hypothesis — and explicitly **not** equating ANN recall@k with BlinkDB aggregate error bars.

## Question asked

What exact query-surface contracts, sample-selection mechanism (ELP), and delineations vs OLA/AQP priors does BlinkDB establish, and how should RQL name `RECALL`/`LATENCY` options without fake metrics or category errors?

## Where we looked

- WebSearch `BlinkDB Agarwal EuroSys 2013 DOI` → ACM 10.1145/2465351.2465355; dblp AgarwalMPMMS13; pages 29–42; six authors
- `curl` arXiv PDF 1203.5485 + `extract_document.py` + `relate_components.py` + full page PNG skim
- Focus pages: p.3 query syntax; Fig 1–2 architecture/samples; Table 2 variance formulas; Fig 4 HDFS rings; Fig 5 stack; Fig 6–8 eval; §7 related (OLA/STRAT/SciBORQ)

## Pass 1 — Skim

1. Sampling-based AQP SQL engine on Hive/Hadoop (+ Shark): trade accuracy for response time; results with error bars.
2. Two ideas: (i) multi-dimensional multi-resolution stratified (+ uniform) samples offline; (ii) dynamic sample selection at runtime from error and/or time constraints.
3. Query surface: `ERROR WITHIN ε AT CONFIDENCE C` **or** `WITHIN T` returning relative error at confidence.
4. Error-Latency Profile (ELP) from pilot runs on small samples → pick resolution.
5. AUTHOR eval: 100-node EC2; Conviva ~17 TB + TPC-H 1 TB; claims ~<2s / 2–10% error — unreproduced here.
6. Related: OLA online refine vs BlinkDB offline samples; STRAT / SciBORQ / 1-D stratified priors.

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro → §2 Overview (settings; architecture; example) → §3 Sample creation (stratified families; MILP storage) → §4 Runtime selection (family + size; ELP; Table 2) → §5 Implementation → §6 Evaluation → §7 Related → §8 Conclusion |
| Figures | **Fig 1** architecture (sample create + selection; result ± error); **Fig 2** sample families by query templates; **Fig 3** stratified family example; **Fig 4** non-overlapping sample rings → HDFS; **Fig 5** implementation stack; **Fig 6** storage budgets Conviva/TPC-H + vs no-sampling latency; **Fig 7** error vs multi/1-D/random + convergence; **Fig 8** actual vs requested time/error + scaleup |
| Tables | **Table 1** notation §3.1; **Table 2** error/variance formulas Avg/Count/Sum/Quantile; **Tables 3–4** Sessions toy + stratified sample rates |
| Algorithms / math | Stratified sample family S(φ,K); MILP goal/coverage/storage (§3.2); ELP error ~1/√n projection; latency ~ linear in rows read |
| Query surface | `ERROR WITHIN 10% AT CONFIDENCE 95%`; `WITHIN 5 SECONDS` + `RELATIVE ERROR AT 95% CONFIDENCE` |

**Miss checklist:** all 16 page PNGs opened; Figs 1–8 captions/axes understood; Tables 1–4 recovered via text+PNG (pdfplumber table count inflated by layout); arXiv vs EuroSys author-list delta noted; AUTHOR speed/error numbers not treated as ours.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §2 query examples | introduces | dual constraints ERROR vs TIME | ESTABLISHED surface contract |
| Fig 1 | implements | offline samples + runtime selection | architecture |
| Fig 2 / §3 | grounds | multi-dim multi-res stratified families | ESTABLISHED mechanism |
| Table 2 | grounds | closed-form aggregate variance | ESTABLISHED for COUNT/SUM/AVG/quantile AQP |
| §4.2 ELP | implements | map constraint → sample size K | ESTABLISHED selection idea |
| Fig 6(c)/7/8 | grounds | AUTHOR latency/error empirics | unreproduced |
| §7 OLA | qualifies | online refine ≠ offline sample pick | delineation |
| §7 STRAT/SciBORQ | cites-sideways | single-sample / impressions priors | AQP lineage |

## Pass 4 — Seed (1–5%)

**Observation:**

> BlinkDB (EuroSys’13; arXiv:1203.5485) makes approximate answers a **first-class query contract**: users declare either an **error+confidence** bound or a **response-time** bound; the engine selects among precomputed multi-resolution sample families using an **Error-Latency Profile** (pilot on small samples → project ~1/√n error and ~linear latency) and returns answers **with** error bars. Table 2 supplies closed-form variance for common aggregates. This is Established AQP doctrine for SQL aggregation over samples — not an ANN recall theorem.

**Interpretation for RQL:**

> Package surface options `OPTION RECALL TARGET r` / `LATENCY …` (and PhysicalPlan `budgets.recallTarget` / `budgets.latencyMs`) as **Hypothesis packaging inspired by BlinkDB’s dual ERROR/TIME contracts + ELP-style selection**, mapping onto retrieval physical knobs (ef/nprobe/candidates, FilterExec mode, rewrite/rerank depth) under EXPLAIN.  
> **Hard delineation:** BlinkDB’s ε is statistical error on aggregates with sampling theory; RQL’s “recall target” is an **ANN/IR recall proxy** (or planner soft constraint) — **do not** claim BlinkDB confidence intervals transfer to recall@k, and **do not** invent measured recall/latency from this paper read.  
> Established: dual bounded-error / bounded-time query surface + ELP sample-size selection + stratified multi-resolution idea. Hypothesis: RQL names, schema fields, and planner policies that bind budgets → physical retrieval plans.

**Evidence pointers:** §2 examples p.3; Fig 1–2; Table 2; §4.1–4.2 ELP; Fig 4–5; Fig 6–8 AUTHOR-only; §7 OLA/STRAT.

**Anti-overclaim:** unreproduced 17 TB / <2s / 2–10% figures; no claim RQL implements stratified sampling or Hive shims; no claim ERROR≡RECALL; arXiv PDF ≠ guaranteed byte-identical to ACM camera-ready (Milner on ACM author list).

**Uncertainty:** Exact EuroSys pagination vs arXiv line breaks; closed-form aggregates only (not neural rerankers); confidence-interval coverage under sample reuse caveats in §2.1.

## Pass 5 — Next queries

1. **HyDE / Gao et al. arXiv:2212.10496** Pass 1–5 → ground `Rewrite` / `REWRITE HYDE` (queued; preferred sibling to this budget pass)
2. Optional: Hellerstein Online Aggregation (OLA) primary PDF for refine-vs-contract contrast
3. Optional: modern vector AQP / recall–latency Pareto papers that actually measure ANN recall under time budgets (for future empirics — still HUMAN/P0)
4. Optional: widen toy RQL grammar to parse `OPTION RECALL|LATENCY` into LogicalPlan budgets (low-risk engineering after HyDE or Condorcet/LATE parser expansion)
5. Optional: SciBORQ / STRAT multimodal if AQP lineage needs depth

## Promote?

- [x] Journal 0031 + OKF `knowledge/reads/blinkdb-eurosys13/`
- [x] Thesis: strengthen §06 cost-vector / budgets; §03 related-work BlinkDB paragraph; algebra note; bib authors+DOI+pages
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/08 / docs/references / journal index / schemas README note
- [ ] Do not invent recall/latency metrics or equate ε with recall@k
- [ ] Do not push
