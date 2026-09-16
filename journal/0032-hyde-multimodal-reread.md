# 0032 — HyDE multimodal re-read (Pass 1–5): Rewrite / REWRITE HYDE

**Date:** 2026-09-17 ~01:05 IST (Europe/Dublin)  
**Type:** multimodal source read (query rewrite / hypothetical-doc dense retrieval)  
**Status:** Pass 1–5 complete for this source  
**Source:** Gao, Ma, Lin, Callan — *Precise Zero-Shot Dense Retrieval without Relevance Labels* — ACL 2023 (Long Papers), pp. 1762–1777  
**URLs:** ACL Anthology [2023.acl-long.99](https://aclanthology.org/2023.acl-long.99/) · DOI [10.18653/v1/2023.acl-long.99](https://doi.org/10.18653/v1/2023.acl-long.99) · arXiv:2212.10496 · code https://github.com/texttron/hyde  
**Local PDF:** `tooling/scripts/extract_out/hyde-2212.10496.pdf` (**11 pp**, arXiv v1 20 Dec 2022 — preprint of ACL’23; venue/pages from Anthology)  
**Extract dir:** `tooling/scripts/extract_out/hyde_2212/` (0 XObject figures / noisy table extracts; 34 nodes / 77 edges; `page_renders/page-01..11.png`)  
**OKF bundle:** [`../knowledge/reads/hyde-2212.10496/`](../knowledge/reads/hyde-2212.10496/)  
**Cite-chase of:** provisional HyDE / `REWRITE HYDE` in docs/05–08, examples/10, thesis §05 Rewrite row; sibling to BlinkDB budget pass (0031)

---

## Context

RQL’s evolved idea and examples already expose Hypothesis `REWRITE HYDE` / algebra `Rewrite` as plan nodes with token cost, citing HyDE only as provisional. After BlinkDB grounded budget contracts (0031), the solid next seed was a full multimodal Pass 1–5 so we can label the **hypothetical-document → Contriever/MIPS** mechanism Established while keeping RQL surface packaging Hypothesis — and explicitly **not** treating AUTHOR DL/BEIR/Mr.TyDi tables as our metrics.

## Question asked

What exact factorization (InstructLM generate → contrastive encode → doc–doc MIPS), equations, and delineations vs transfer-from-MS-MARCO / generative-IR does HyDE establish, and how should RQL name `Rewrite` / `REWRITE HYDE` without fake metrics?

## Where we looked

- WebSearch `Gao Ma Lin Callan HyDE Precise Zero-Shot Dense Retrieval` → ACL Anthology 2023.acl-long.99; DOI 10.18653/v1/2023.acl-long.99; pages 1762–1777
- `curl` arXiv PDF 2212.10496 + `extract_document.py` + `relate_components.py` + full page PNG skim
- Focus pages: Fig 1 pipeline; §3.1–3.2 Eqs. (1)–(8); Tables 1–4 AUTHOR empirics; §5 ablations; Appendix A.1 instructions; §6 conclusion lifecycle

## Pass 1 — Skim

1. Fully zero-shot dense retrieval **without relevance labels** (and without training HyDE’s components for the retrieval task).
2. Pivot: InstructLM generates a **hypothetical document** from query+instruction; Contriever (or mContriever) embeds it; retrieve real docs by vector similarity (doc–doc space).
3. Claim: generative step captures relevance patterns; dense bottleneck acts as **lossy compressor** filtering hallucinations / grounding to corpus.
4. Backbone: InstructGPT (`text-davinci-003`) + Contriever/mContriever; Pyserini; no models trained/fine-tuned for this preprint.
5. AUTHOR eval: TREC DL19/20, 6 BEIR low-resource sets, Mr.TyDi (sw/ko/ja/bn) — unreproduced here.
6. Related: BEIR transfer setups; generative retrieval (doc-id generation) ≠ HyDE intermediate hyp-doc; concurrent instruction-aware encoders (Asai et al.).

## Pass 2 — Multimodal inventory

| Kind | IDs / notes |
|------|-------------|
| Sections | §1 Intro → §2 Related (dense; instruction LMs; zero-shot; generative retrieval) → §3 Methodology (3.1 Preliminaries; 3.2 HyDE) → §4 Experiments (4.1 Setup; 4.2 Web; 4.3 Low-resource BEIR; 4.4 Multilingual) → §5 Analysis (5.1 generative models; 5.2 fine-tuned encoder) → §6 Conclusion → References → Appendix A.1 instructions |
| Figures | **Fig 1** (p.2): HyDE pipeline — instruction+query → GPT hyp-doc → Contriever → real documents; multilingual/task examples; shared backbone models |
| Tables | **Table 1** DL19/20 map / nDCG@10 / recall@1k; **Table 2** BEIR nDCG@10 + Recall@100 (6 sets); **Table 3** Mr.TyDi MRR@100; **Table 4** NDCG@10 ablations (Flan-T5 / Cohere / GPT × Contriever / ContrieverFT) — all AUTHOR-only |
| Algorithms / math | Eq. (1) classical dual-encoder sim; Eqs. (2)–(3) shared contrastive doc encoder \(f\); Eq. (4) InstructLM \(g(q,\mathrm{INST})\); Eqs. (5)–(7) expect/mean of \(f(\hat d_k)\); Eq. (8) optional include \(f(q)\) in average |
| Instructions (App A.1) | Task-specific prompts (passage / scientific / counter-arg / financial / news / multilingual detail) |

**Miss checklist:** all 11 page PNGs opened; Fig 1 caption/flow understood; Tables 1–4 recovered via text+PNG (pdfplumber/pymupdf table fragments noisy); ACL venue/pages verified separately from arXiv PDF; AUTHOR nDCG/MAP/MRR **not** treated as ours.

## Pass 3 — High-signal relationships

| From | Edge | To | Note |
|------|------|----|------|
| §3.1 Eq. (1) | qualifies | dual-encoder relevance learning | hard without labels |
| §3.2 / Fig 1 | introduces | hyp-doc pivot + doc–doc MIPS | ESTABLISHED mechanism |
| Eqs. (5)–(8) | implements | multi-sample mean query vector (± query) | ESTABLISHED aggregation |
| §2 generative retrieval | delineates | doc-id decoding ≠ hyp-doc intermediate | not generative index |
| §2 Asai et al. | cites-sideways | instruction-tuned *encoder* vs HyDE unsupervised enc + generative rewrite | concurrent |
| Tables 1–4 | grounds | AUTHOR effectiveness claims | unreproduced |
| §5.1 Table 4 | qualifies | larger InstructLM → larger gains (AUTHOR) | model-capacity story |
| §6 | qualifies | HyDE early-life / long-tail; supervised dense for common queries | lifecycle narrative |

## Pass 4 — Seed (1–5%)

**Observation:**

> HyDE (ACL’23; arXiv:2212.10496) factorizes zero-shot dense retrieval as **NLG relevance by example** then **unsupervised doc–doc similarity**: an instruction-following LM generates one or more hypothetical documents; a contrastive encoder embeds them (optionally averaging with the raw query embedding, Eqs. 6–8); MIPS retrieves real corpus neighbors. Query–document similarity is **not** explicitly trained. This is Established literature mechanism for LLM-mediated query rewriting into the document embedding space — not a claim about RQL syntax or our measured IR quality.

**Interpretation for RQL:**

> Package surface `REWRITE HYDE MODEL … TEXT … AS …` (and algebra \(\mathrm{Rewrite}\) / \(\mathrm{Rewrite}_{hyde}\)) as **Hypothesis packaging** of that Established pipeline: a costed plan node (token/latency) whose output feeds `EMBED` / `Search_dense` (possibly multi-sample union or mean). Compose with BlinkDB-inspired `OPTION RECALL|LATENCY` (journal 0031) as in `examples/10-hyde-rewrite-budget.rql`.  
> **Hard delineation:** AUTHOR DL/BEIR/Mr.TyDi tables stay AUTHOR-only; do **not** invent RQL HyDE gains; do **not** equate HyDE with generative doc-id retrieval or with fine-tuned instruction encoders; instruction text is a plan attribute, not magic.  
> Established: hyp-doc generation + contrastive encode + doc–doc MIPS (+ multi-sample mean). Hypothesis: RQL names, CTE/WITH shape, planner cost attributes, and adapter execution.

**Evidence pointers:** Fig 1; §3.1–3.2 Eqs. (1)–(8); §4.1 InstructGPT+Contriever; Tables 1–4 AUTHOR-only; App A.1; §6 lifecycle.

**Anti-overclaim:** unreproduced map/nDCG/recall/MRR; no claim we run InstructGPT/Contriever; arXiv PDF ≠ guaranteed byte-identical to ACL camera-ready; no claim HyDE removes need for ACL/filter correctness.

**Uncertainty:** Exact N samples used per table row; temperature 0.7 default only; ambiguous-query diversity left open by authors; ACL pagination vs arXiv line breaks.

## Pass 5 — Next queries

1. Optional: widen toy RQL grammar to parse `REWRITE HYDE` / `WITH` CTE into LogicalPlan (low-risk engineering; note already in grammar.md out-of-scope)
2. Optional: Multi-HyDE / DMQR-RAG multimodal if multi-query rewrite needs depth
3. Optional: Asai et al. instruction-aware retrieval for encoder-side instruction contrast
4. Optional: Hellerstein OLA (queued from 0031) if AQP refine-vs-contract still needed
5. Human P0 FANNS / live adapter smoke remains blocked on Vijay (unchanged)

## Promote?

- [x] Journal 0032 + OKF `knowledge/reads/hyde-2212.10496/`
- [x] Thesis: §03 related-work HyDE paragraph; §05 Rewrite Established+Hypothesis; §08 apps; abstract; bib ACL pages+DOI
- [x] Meta: NOTES / CHANGELOG / docs/06 / docs/08 / docs/references / journal index / knowledge README / grammar note
- [ ] Do not invent HyDE IR metrics or treat Tables 1–4 as ours
- [ ] Do not push
