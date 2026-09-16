# Changelog

## 2026-09-17 — Colab FANNS synthetic run + LINKS

- Ran `fanns_microbench_colab.ipynb` on Colab T4 GPU; results under `experiments/results/fanns/colab_synth_20260916_233628/` (**not P0**).
- Recorded live Colab URL in `experiments/colab/LINKS.md`.
- Journal `0029-colab-fanns-synth-run.md`.

## 2026-09-17 ~00:25 IST — Human + Colab paths for experiment results

- `experiments/HOW_TO_PROVIDE_RESULTS.md`: preferred commit layout; FANNS/datasets/adapters paths; metrics.json schema; Options A (local), B (Colab zip), C (agent CPU smoke).
- Colab: `experiments/colab/fanns_microbench_colab.ipynb` + `colab/README.md` (synthetic PRE/POST; optional SIFT1M license stub; zip → `results/fanns/<run_id>/`).
- Datasets stub: `experiments/datasets/README.md` + `.gitignore` for `data/`.
- Optional smoke: `experiments/harness/fanns_synthetic_cpu.py` → `results/fanns/synthetic_cpu_smoke_2026-09-17/` (**smoke / not P0**).
- Journal `0028`; HUMAN_TODOS / PAUSE_CHECKLIST mention Colab path.
- Integrity: **no** ACORN paste; **no** fabricated P0; **no push.**

## 2026-09-17 ~00:12 IST — E2E pipeline CLI + human P0 pause checklist

- Offline E2E glue: `experiments/harness/rql_pipeline.py` (+ `run_rql.py`) runs toy `.rql` → parse → LogicalPlan → plan(profile) → PhysicalPlan → emit(adapter) → `experiments/results/e2e/<run_id>/`.
- Profiles: qdrant / elasticsearch / pgvector; schema validate on; **4×3 = 12/12** → `experiments/results/e2e/run_validate.txt`.
- Journals `0026-e2e-pipeline-cli.md`, `0027-pause-human-p0-checklist.md`; hand-off `experiments/PAUSE_CHECKLIST.md`.
- Thesis: §07 offline E2E subsection + abstract/conclusion one-liners; rebuild `main.pdf`.
- Integrity: **no** live vector-DB network; **no** fabricated metrics; **no push.** Recommend **pause for human P0** (protocols 01–02).

## 2026-09-17 ~00:10 IST — Substrait / Calcite IR adjacency

- Careful docs+paper pass: **Substrait** (substrait.io spec pages) + **Apache Calcite** Begoli et al. (arXiv:1802.10233 / SIGMOD’18, 10 pp) + Cascades Graefe 1995 skim for vocabulary.
- Journal `0025-substrait-calcite-ir-adjacency.md`; OKF `knowledge/reads/substrait-spec-2026-09/` + `calcite-begoli-sigmod18/`.
- **Established:** portable plan IR (not SQL text); Substrait extension points; no hard logical/physical split in Substrait; Calcite traits/calling convention + adapters; Volcano-like planner; Cascades enforcers vocabulary.
- **Hypothesis only:** RQL Logical/Physical JSON + compile stack are Substrait-/Calcite-*inspired* — **not** a Substrait implementation or Calcite embedding.
- Thesis: strengthen §07 adjacency + §03 related-work; abstract/conclusion; bib `graefe1995cascades` + notes; `schemas/README.md` extension-points note; rebuild `main.pdf`.
- Integrity: **no** overclaim that RQL implements Substrait. **No push.**

## 2026-09-17 ~00:00 IST — Adapter emit stub (PhysicalPlan → vendor sketches)

- Hypothesis emitters under `experiments/harness/rql_adapters/` (qdrant Query API JSON; elasticsearch retriever/knn JSON; pgvector SQL).
- CLI `emit_rql.py`; test `test_rql_adapters.py`: **hybrid-rrf + filtered-dense × 3 profiles = 6/6** (not executed; approximate sketches).
- Results `experiments/results/rql_adapters/`; journal `0024`; thesis §07 (+ abstract/conclusion) cite emit stub.
- Integrity: **no** live vector-DB network; live smoke remains HUMAN_TODO (protocol 03). **No push.**

## 2026-09-16 ~23:59 IST — LogicalPlan → PhysicalPlan planner stub

- Hypothesis rule engine under `experiments/harness/rql_planner/` (profiles: qdrant / elasticsearch / pgvector from docs/09 — **not** live probes).
- Rules: Filter→FilterExec (chooser + FANNS labels); Fuse_rrf/linear→FusionExec native or ShimCast; Search_late→LateInteractExec (colbert default; optional plaid/muvera).
- CLI: `experiments/harness/plan_rql.py`; test **4 logical × 3 profiles = 12/12 validate** → `experiments/results/rql_planner/`.
- Journal `0023`; thesis §06/§07 (+ abstract/conclusion) cite stub.
- **No** GitHub push; **no** fabricated latency/recall; not a Cascades cost model.


## 2026-09-16 ~23:59 IST — Toy RQL → LogicalPlan parser

- Minimal **Hypothesis** frontend under `experiments/harness/rql_parser/` (grammar.md documents tiny EBNF).
- Supports SEARCH DENSE/BM25/LATE|COLBERT, WHERE (+ ACL_HARD), FUSE RRF/LINEAR, K/CANDIDATES/LIMIT; rejects EMBED/WITH/RERANK/….
- CLI: `experiments/harness/parse_rql.py parse path.rql [--validate]`; also `python -m rql_parser` from `experiments/harness/`.
- Schema-aligned `.rql` under `schemas/examples/` (+ `examples/toy/`); test **4/4 parse+validate** → `experiments/results/rql_parser/`.
- Journal `0022`; thesis §05/§07 (+ abstract/conclusion) cite prototype textual frontend.
- **No** GitHub push; **no** fabricated metrics; not a full SQL engine.


## 2026-09-16 ~23:55 IST — LogicalPlan / PhysicalPlan schema freeze v0.1.0-draft

- Freeze **Hypothesis IR** JSON Schema draft 2020-12 under `schemas/`: `logical-plan.schema.json`, `physical-plan.schema.json`, `examples/` (hybrid RRF, filtered dense, late+PLAID, client RRF shim, MUVERA ladder), `README.md`.
- Validator harness `experiments/harness/validate_plans.py` (`jsonschema`); all 8 examples **passed** → `experiments/results/plan_schema/validate.txt`.
- Journal `0021`; thesis §05/§07 (+ abstract/conclusion) cite schema freeze as Hypothesis IR — **not** a standard.
- Maps optional capability flags to vendor matrix (journal 0020 / docs/09).
- **No** GitHub push; **no** fabricated metrics; schemas remain draft Hypothesis.


## 2026-09-16 ~23:50 IST — Vendor hybrid/filter/fusion API matrix (docs-only)

- Docs-only survey of **Qdrant, Elasticsearch/OpenSearch, Weaviate, Milvus, pgvector** (+ optional Pinecone/Redis); **no** live DB/credentials.
- Artifacts: `docs/09-vendor-api-matrix.md` (citable tables + URLs); journal `0020`; OKF `knowledge/reads/vendor-api-matrix-2026-09/` (one concept/vendor).
- **Established:** incompatible filter DSLs; heterogeneous filter+ANN composition (PRE / POST+iterative / leaf-propagated / hybrid-batch / UNKNOWN); native RRF on Qdrant/ES/OS/Milvus; weighted/score fusion variants not interchangeable; late-interaction native on Qdrant/Weaviate; EXPLAIN strong on pgvector (+ ES Profile / OS hybrid explain).
- Thesis: §07 compilation cites matrix as Established adapter-surface survey; Hypothesis that RQL compiles via shims; related-work + abstract + conclusion; rebuild `main.pdf`.
- HUMAN_TODOS: live adapter smoke remains **P1 for Vijay**.
- **No** GitHub push; **no** invented API features (UNKNOWN left UNKNOWN).



## 2026-09-16 ~23:35 IST — FANNS survey Lin 2025 multimodal + FilterExec taxonomy weave

- Completed Pass 1–5 on **Lin et al.** FANNS survey (arXiv:2505.06501, **25 pp**); journal `0019`; OKF `knowledge/reads/fanns-lin2025-2505.06501/`.
- Extract: `fanns-lin2025-2505.06501.pdf` + `fanns_lin2025_2505_06501/` (47 nodes / 65 edges); full page PNG renders (Figs 1–6 / Tables 1–2 / A1–A17 via pages).
- **Established (survey structure):** VSP/VJP/SJP/SSP pruning taxonomy; A1–A17 classification; selectivity×ID/POD/OOD difficulty; §6.3 multi-algo combination as literature direction.
- **AUTHOR-only:** Fig 3 recall curves — unreproduced. **No** fabricated RQL metrics.
- Thesis: strengthen §06 FilterExec with survey map; add `PARTITION`/`ROUTER`; bib `lin2025fanns`; related-work + abstract; rebuild `main.pdf`.
- Meta: NOTES / docs/06 / docs/08 / journal index / filter-chooser toy modes.
- **No** GitHub push.


## 2026-09-16 ~23:30 IST — Montague–Aslam Condorcet-fuse multimodal + Fuse_condorcet sibling

- Completed Pass 1–5 on **Montague & Aslam** (CIKM 2002 / DOI 10.1145/584792.584881, **11 pp** author PDF); journal `0018`; OKF `knowledge/reads/montague-aslam-cikm02-condorcet/`.
- Extract: `montague-aslam-cikm02-condorcet.pdf` + `montague_condorcet_cikm02/` (53 nodes / 44 edges); full page PNG renders (Figs 1–5 / Tables 1–4 via pages).
- **Established (mechanism):** pairwise-majority sort Condorcet-fuse (Alg 1+3); Fig 1 ranks×training fusion-input taxonomy; dependence-filter / weighted variants as AUTHOR literature.
- **AUTHOR-only:** Fig 4/5 MAP curves; Table 2 sign tests — unreproduced.
- Thesis: \(\mathrm{Fuse}_{condorcet}\) as Fuse-family sibling of \(\mathrm{Fuse}_{rrf}\) (RRF remains portable default); related-work / algebra / optimizer preference / abstract / apps / conclusion; bib DOI + pages 538–548.
- Meta: NOTES / docs/06 §11b / docs/references 72c / journal index.
- **No** GitHub push; **no** fabricated IR metrics. FANNS survey figure pass still open.


## 2026-09-16 ~23:35 IST — Chen ECIR’22 cite-chase + Fuse preference weave

- Completed Pass 1–5 on **Chen et al.** (ECIR 2022 / arXiv:2201.10582, **16 pp**); journal `0017`; OKF `knowledge/reads/chen-ecir2022-2201.10582/`.
- Extract: `chen-ecir2022-2201.10582.pdf` + `chen_ecir2022/` (47 nodes / 86 edges); full page PNG renders (Figs 1–2 / Tables 1–5 via pages).
- **Resolved Bruch disagreement as setup conflict:** Chen AUTHOR Recall@1K RRF>linear-interp (zero-shot); Bruch AUTHOR NDCG TM2C2>RRF(60); different \(\phi\)/metrics/labels.
- Thesis: short \(\mathrm{Fuse}_{rrf}\) vs \(\mathrm{Fuse}_{linear}\) preference subsection (**Established** disagreement → **Hypothesis** planner rule); related-work Chen paragraph; abstract/background/algebra/apps/conclusion; bib DOI 10.1007/978-3-030-99736-6_7.
- **No** GitHub push; **no** fabricated IR metrics.

## 2026-09-16 ~23:25 IST — Bruch fusion multimodal + Fuse_linear weave

- Completed Pass 1–5 on **Bruch et al.** (ACM TOIS / arXiv:2210.11934, **36 pp**); journal `0016` (kept `0015` as hand-off only); OKF `knowledge/reads/bruch-arxiv-2210.11934/`.
- Extract: `bruch-arxiv-2210.11934.pdf` + `bruch_2210/` (181 nodes / 283 edges); full page PNG renders (Figs 1–20 / Tables 1–8 via pages + appendices).
- **Established (mechanism):** convex combination / TM2C2 (Eqs. 2–5); RRF-vs-CC delineation; normalisation role; sample-efficiency claim as AUTHOR literature.
- **AUTHOR-only:** Table 2/4 NDCG/Recall; Fig 5/12 curves — unreproduced.
- Thesis: `Fuse_linear` / `Fuse_ltr` vs `Fuse_rrf` labels; related-work Bruch paragraph; abstract/background/algebra/optimizer/apps/eval/conclusion; bib DOI 10.1145/3596512.
- Docs: `docs/08-algebra-sketch.md`, HUMAN_TODOS, NOTES, READMEs.
- Optional harness: weighted linear/CC on fixed toy scores → `experiments/results/linear_fusion/unit_test.txt`.
- **No** GitHub push; **no** fabricated IR metrics.

## 2026-09-16 ~23:05 IST — PLAID multimodal + rewrite-ladder middle

- Completed Pass 1–5 on **PLAID** (CIKM’22 / arXiv:2205.09707, **10 pp**); journal `0014`; OKF `knowledge/reads/plaid-cikm22/`.
- Extract: `plaid-2205.09707.pdf` + `plaid_2205/` (87 nodes / 87 edges); full page PNG renders (Figs 1–8 / Tables 1–6 via pages).
- **Established (mechanism):** centroid interaction (Eqs. 2–4), centroid pruning (Eq. 5), four-stage funnel (Fig 5).
- **AUTHOR-only:** latency/speedup/MRR tables (abstract 7× GPU / 45× CPU; Tables 3–6; Fig 6 ablation) — unreproduced.
- Thesis: ColBERT→**PLAID**→MUVERA ladder middle filled; abstract / background / related-work / algebra / optimizer / applications updated; bib CIKM pages+DOI.
- Docs: `docs/08-algebra-sketch.md`, HUMAN_TODOS, NOTES, READMEs.
- **No** GitHub push; **no** fabricated IR metrics; Bruch fusion **not** started (quality bar first; leave next note).

## 2026-09-16 late evening — ColBERT + MUVERA multimodal + Search_late weave

- Completed Pass 1–5 on **ColBERT** (SIGIR’20, **10 pp**); journal `0012`; OKF `knowledge/reads/colbert-sigir20/`.
- Completed Pass 1–5 on **MUVERA** (arXiv:2405.19504, **26 pp**); journal `0013`; OKF `knowledge/reads/muvera-2405.19504/` (PDF found — Bruch deferred).
- Extract: `colbert-sigir20.pdf` + `colbert_sigir20/` (78 nodes / 196 edges); `muvera-2405.19504.pdf` + `muvera_2405/` (155 nodes / 109 edges); full page PNG renders.
- Thesis: MaxSim/late interaction **Established** (Eq. 3); `Search_late` + ColBERT→PLAID→MUVERA rewrite ladder **Hypothesis**; related-work late-interact subsection; abstract/apps/optimizer updated; PLAID bib cite-only.
- Docs mirror `docs/08-algebra-sketch.md`; HUMAN_TODOS / NOTES / READMEs updated.
- Optional harness: deterministic MaxSim toy test → `experiments/results/maxsim/unit_test.txt`.
- **No** GitHub push; **no** fabricated IR/RAG metrics (ColBERT/MUVERA tables AUTHOR-only).

## 2026-09-16 late evening — Cormack RRF multimodal + Fuse_rrf weave

- Completed Pass 1–5 on **Cormack et al. RRF** (SIGIR’09, **2 pp**); journal `0011`; OKF `knowledge/reads/rrf-cormack-sigir09/`.
- Extract: `tooling/scripts/extract_out/cormack-sigir09-rrf.pdf` + `rrf_cormack_sigir09/` (9 nodes / 6 edges; page PNG renders for Tables 1–3).
- Thesis: related-work fusion subsection; algebra Fuse_rrf + rewrite; applications hybrid pattern; abstract cites RRF; bib pages 758–759 + DOI.
- Docs mirror `docs/08-algebra-sketch.md`; HUMAN_TODOS marks RRF P2 **done**.
- RRF harness: re-ran unit test; added channel-order invariance property assertion.
- **No** GitHub push; **no** fabricated IR/RAG metrics (Cormack MAPs labelled AUTHOR-only).

## 2026-09-16 evening — VBASE + Filtered-DiskANN multimodal + algebra expand

- Completed Pass 1–5 on **VBASE** (OSDI’23); journal `0009` supersedes stub `0007`; OKF `knowledge/reads/vbase-osdi23/`.
- Completed Pass 1–5 on **Filtered-DiskANN** (WWW’23); journal `0010`; OKF `knowledge/reads/filtered-diskann-www23/`.
- Expanded thesis §05 algebra (typed evidence, signatures, rewrite examples) and §06 FilterExec modes; related-work updated; abstract mentions three multimodal reads.
- Added markdown mirror `docs/08-algebra-sketch.md`.
- Deterministic toy `FilterExec` chooser unit test → `experiments/results/filter_chooser/unit_test.txt`.
- **No** GitHub push; **no** fabricated ANN metrics.

All dates are **Europe/Dublin** local time. Entries describe human-readable research increments (aligned with git commits when the parent agent commits).

## 2026-09-16 — HUMAN_TODO hand-off + thesis rebuild

- Added `experiments/HUMAN_TODOS.md` + protocols 01–04 (FANNS, datasets, adapters, judgments).
- Thesis §09 / Appendix A now point at HUMAN_TODO paths; no fake metrics.
- Fixed planned-run YAML parser; saved RRF unit-test output under `experiments/results/`.
- Journal `0008-human-todos-hand-off.md`.

## 2026-09-16 — ACORN multimodal re-read + thesis + experiments stubs

- Completed Pass 1–5 on ACORN (arXiv:2403.04871); journal `0006-acorn-multimodal-reread.md`.
- OKF-shaped knowledge bundle: `knowledge/reads/acorn-2403.04871/` (concepts + links; research methodology packaging, not RQL runtime).
- Queued VBASE as second seed stub: `journal/0007-vbase-seed-stub.md` (no fake Pass notes).
- Started incremental LaTeX thesis under `thesis/` (arXiv-style article; provisional/hypothesis labels).
- Added `experiments/` reproducibility stubs + tiny deterministic harness smoke test.
- Re-verified `relate_components.py` on existing ACORN extract outputs.

## 2026-09-16 — Correction: Google OKF

- User clarified the Google format/library was **OKF (Open Knowledge Format)**, not LangExtract.
- Updated `tooling/python-libraries.md` and added `journal/0005-okf-correction.md`.
- Implication: prefer OKF-shaped linked markdown for multimodal paper notes / entity graphs.

## 2026-09-16 — Slow-path methodology, journal, tooling

- Added `journal/` so GitHub readers can follow thinking chronologically (`0001`–`0004`).
- Added `methodology/` (principles, search strategy, read protocol, preprocess/synthesis, iteration loop).
- Added `tooling/` library survey + baseline PDF extract/relate scripts (pymupdf/pdfplumber).
- Clarified in root README that v2 literature (`docs/06`, `docs/07`) is **provisional** until multimodal re-read.
- **No** new literature dump; **no** new RQL algebra claims.

## 2026-09-16 — v2 adjacent brainstorm (earlier same day)

- `docs/05`–`07`, expanded examples, search log — breadth-first adjacent literature (provisional).

## 2026-09-16 — v1 landscape (earlier same day)

- Initial landscape, gaps, RQL v1 proposal, related work, examples 01–09.
