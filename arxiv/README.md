# arXiv upload package — RQL technical report

**Date:** 19 September 2026 (Europe/Dublin)  
**Author:** Vijay Kumar (`vijaykumarjob0701@gmail.com`)  
**Status:** Package prepared locally. **Vijay must click Submit** on https://arxiv.org with his account. Agents do **not** push or submit.

## What is in this folder

| File | Purpose |
|------|---------|
| `METADATA.md` | Title, authors, abstract paste, categories, comments, license |
| `00README.XXX` | AutoTeX / compiler notes shipped inside the source zip |
| `build_arxiv_zip.sh` | Builds a clean TeX source tree → `rql-arxiv-source.zip` |
| `rql-arxiv-source.zip` | Upload this as the TeX source package |
| `rql-arxiv.pdf` | Final PDF copy for human review (optional attach) |

## Suggested categories

1. **Primary: cs.IR** (Information Retrieval)
2. **Secondary: cs.DB** (Databases)
3. Optional: **cs.LG**

## License

Recommend **CC-BY-4.0**. Alternative: arXiv perpetual non-exclusive license.

## Comments field (copy-paste)

```
Technical report. Proposal + offline prototype + measured FAISS HNSW32 SIFT1M PRE/POST microbench (synthetic predicates; not ACORN reproduction). Code: https://github.com/vijaykumarjob0701/rql-rag-query-language — Data registry / repro: https://github.com/vijaykumarjob0701/rql-repro
```

## Rebuild zip + PDF copy

From the research repo root:

```bash
cd thesis && latexmk -pdf -interaction=nonstopmode main.tex && cd ..
bash arxiv/build_arxiv_zip.sh
```

## Upload checklist (Vijay — human only)

1. [ ] Log in at https://arxiv.org with your account.
2. [ ] Start **Submit** → new submission.
3. [ ] Choose license (**CC-BY-4.0** recommended).
4. [ ] Upload **`arxiv/rql-arxiv-source.zip`** (TeX source).
5. [ ] Confirm autoTeX builds cleanly; download/preview PDF.
6. [ ] Paste title + abstract from `METADATA.md`.
7. [ ] Set primary **cs.IR**, secondary **cs.DB** (optional cs.LG).
8. [ ] Paste comments field (repos + honesty one-liner).
9. [ ] Author: Vijay Kumar; affiliation Independent researcher / Dublin, Ireland; email on file.
10. [ ] Final read of compiled PDF — no NeurIPS claims; FAISS labelled accurately.
11. [ ] Click **Submit**. Record arXiv id here when assigned.

## Integrity

- Do **not** claim NeurIPS/VLDB acceptance.
- Do **not** invent metrics.
- FAISS run `sift1m_faiss_HNSW32_20260917_022017` = measured PRE/POST under **synthetic** predicates; **not** ACORN reproduction.
