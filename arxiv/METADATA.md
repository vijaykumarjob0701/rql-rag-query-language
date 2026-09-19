# arXiv metadata (paste fields)

**Prepared:** 19 September 2026 (Europe/Dublin)  
**Do not fabricate.** Submit only after Vijay reviews PDF + zip.

## Title

RQL: A Portable Intermediate Representation for Retrieval Plans in RAG Systems

## Authors

- Vijay Kumar (Independent researcher, Dublin, Ireland)
- Email: vijaykumarjob0701@gmail.com

## Abstract (plain text for arXiv paste)

Retrieval-augmented generation (RAG) systems compose embedding search, lexical retrieval, metadata and ACL filters, hybrid fusion, reranking, and sometimes graph or multi-hop expansion. In practice those stages are glued together in application code against vendor-specific vector-database APIs, so accuracy, latency, and reliability become properties of brittle scripts rather than of inspectable plans.

This technical report proposes RQL (Retrieval Query Language) as a portable intermediate representation for retrieval plans: a small algebra over scored evidence, cost-aware physical planning under recall, latency, and ACL constraints, and compilation through adapters to heterogeneous backends. The textual DSL is a convenient frontend; the centre of mass is the LogicalPlan / PhysicalPlan IR and the adapter doctrine.

Contributions. (1) A problem formulation for portable retrieval plans. (2) An algebra and physical operator set that packages established IR/DB mechanisms (RRF, Condorcet-fuse, linear/CC fusion, ColBERT MaxSim, PLAID/MUVERA late-interaction ladders, HyDE rewrite, MMR diversify, FANNS filter strategies, BlinkDB-style budgets) without claiming unreproduced author metrics. (3) Draft JSON Schemas (0.1.0-draft), a docs-only vendor API matrix, and an offline prototype stack (toy parser → physical planner → emit sketches → E2E CLI; 12/12 schema-validated toy runs). (4) Related-work positioning with multimodal re-reads of the key priors. (5) An honest evaluation split: what we measured vs what remains for citation-grade ANN/RAG.

Status. We report unit tests, schema validation, and offline emit sketches as feasibility evidence. A Colab synthetic FANNS PRE/POST smoke is plumbing only — not P0 and not citation-ready ANN quality. A FAISS HNSW32 SIFT1M PRE/POST microbench (run sift1m_faiss_HNSW32_20260917_022017; N=10^6, n_q=1000) provides measured index-ANN filter curves under synthetic Bernoulli predicates — stronger than NumPy brute plumbing, but not an ACORN-class claim and still missing live adapters and RAG judgments. We do not report unreproduced large-set paper-table FANNS, BEIR, or RAG end-to-end scores.

## Categories

| Role | Category |
|------|----------|
| Primary | **cs.IR** |
| Secondary | **cs.DB** |
| Optional | cs.LG |

## Comments field (suggested)

Technical report. Proposal + offline prototype + measured FAISS HNSW32 SIFT1M PRE/POST microbench (synthetic predicates; not ACORN reproduction). Code: https://github.com/vijaykumarjob0701/rql-rag-query-language — Data registry / repro: https://github.com/vijaykumarjob0701/rql-repro

## License recommendation

**CC-BY-4.0** (preferred for reuse) — or arXiv's perpetual non-exclusive license if you prefer minimal choice friction.

## MSC / ACM (optional)

- ACM CCS (suggest): Information systems → Information retrieval; Information systems → Database query processing
- MSC: not required for cs.IR/cs.DB

## Files to upload

1. `rql-arxiv-source.zip` (TeX source tree from `build_arxiv_zip.sh`)
2. Optionally also attach `rql-arxiv.pdf` if arXiv UI asks for a PDF preview (arXiv usually builds from source)

## Integrity reminders

- No NeurIPS / VLDB acceptance claims
- No fabricated metrics
- Label FAISS results as measured plumbing with synthetic predicates
