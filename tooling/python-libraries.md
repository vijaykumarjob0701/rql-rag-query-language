# Python libraries for multimodal document research (survey 2024–2026)

**Survey date:** 2026-09-16 (Europe/Dublin)  
**Purpose:** Support the slow read protocol ([`../methodology/02-read-protocol.md`](../methodology/02-read-protocol.md)) — text, layout, tables, figures, and relationships — without inventing RQL claims.

**Baseline for this repo’s scripts:** `pymupdf` + `pdfplumber` (always installable via pip). Heavier stacks (Docling, MinerU, …) are optional.

---

## Google Open Knowledge Format (OKF) — confirmed by user

**User correction (2026-09-16):** the Google piece they meant was **OKF** (Open Knowledge Format), not LangExtract.

| Piece | What it is | Why it matters for this research | Links |
|-------|------------|----------------------------------|-------|
| **OKF (Open Knowledge Format)** | Google Cloud open, vendor-neutral format: knowledge as a directory of **markdown concepts + YAML frontmatter**, cross-linked into a **graph** (relationships via markdown links). Interactive HTML visualizer shows concepts as nodes and links as edges (including ER/schema-style views for tables). | Matches “relate different entities” + portable knowledge graph humans and agents can both read; good target shape for multimodal paper notes (figure / table / claim as linked concepts) | Spec/repo: https://github.com/GoogleCloudPlatform/open-knowledge-format · Blog: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing · Also under Knowledge Catalog: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf |
| **Knowledge Catalog + unstructured insights** | Google Cloud catalog that can ingest OKF and extract entities/context from unstructured files (e.g. PDFs) into a context graph | Managed path from documents → related entities | https://docs.cloud.google.com/dataplex/docs/introduction |

**Related but not what the user meant:**

| Library | Role |
|---------|------|
| **LangExtract** (`google/langextract`) | Gemini-powered span-grounded entity extraction — useful optionally, but **not** the user’s OKF |
| **Document AI Layout Parser / Extractors** | Managed layout + tables/images + schematized entities |
| Vision API / Gemini multimodal | OCR / general document understanding |

**Recommendation for this repo:** Keep local PDF extract (`pymupdf`/`pdfplumber`) as Pass-2 inventory. For synthesis, prefer emitting an **OKF-shaped bundle** (one concept file per figure/table/claim/paper, markdown links for “Figure 3 supports Table 1”, etc.) so relationships stay human-readable and graph-visualizable — aligned with Google’s OKF, without requiring GCP.

---

## PDF text + layout (baseline)

| Library | Install | License (note) | Strengths | Limits | URL |
|---------|---------|----------------|-----------|--------|-----|
| **PyMuPDF** (`fitz`) | `pymupdf` | AGPL-3.0 / commercial | Fast text; blocks/dict layout; **image extraction**; render pages; basic `find_tables`; good CLI substrate | AGPL copyleft for derivatives; complex reading order still heuristic | https://pymupdf.readthedocs.io/ · https://pypi.org/project/pymupdf/ |
| **pdfplumber** | `pdfplumber` | MIT | Excellent for debugging layout; char/word/line boxes; **tables** API; visual debug | Slower on huge PDFs; figures are not semantically “understood” | https://github.com/jsvine/pdfplumber |
| **pypdf** | `pypdf` | BSD-3-Clause | Merge/split, metadata, basic text | Weak layout/tables/figures vs above | https://pypdf.readthedocs.io/ |

---

## Layout / structure (heavy parsers)

| Library | Install | License (note) | Strengths | Limits | URL |
|---------|---------|----------------|-----------|--------|-----|
| **Docling** (IBM → LF AI) | `docling` | MIT (project) | Unified `DoclingDocument`; layout, reading order, tables, OCR, formulas, image classification, provenance bboxes; Markdown/JSON export | Heavier deps/models; first install can be large | https://github.com/docling-project/docling |
| **unstructured** | `unstructured` | Apache-2.0 (core; check extras) | Broad file types; element taxonomy; `hi_res` PDF strategy | Quality varies by strategy; system deps (libmagic, etc.) | https://github.com/Unstructured-IO/unstructured |
| **marker** | `marker-pdf` (see upstream) | GPL-3.0 code; model license caveats | Strong Markdown; Surya OCR/layout; good throughput | License constraints for some orgs; compute | https://github.com/VikParuchuri/marker |
| **MinerU** | `mineru` / see docs | Apache-2.0 (+ model conditions) | Scientific PDFs; formulas→LaTeX; tables→HTML; multi-column; OCR | Heavy; model download agreements | https://github.com/opendatalab/MinerU |
| **LayoutParser** | `layoutparser` | Apache-2.0 | Detect layout blocks with DL models; toolkit, not full RAG pipeline | You assemble OCR+export yourself | https://github.com/Layout-Parser/layout-parser |

---

## Tables

| Library | Install | Notes |
|---------|---------|-------|
| **pdfplumber** | `pdfplumber` | `.extract_tables()`; good default for digital PDFs |
| **camelot-py** | `camelot-py[base]` | Lattice/stream (and newer modes); needs Ghostscript/opencv depending on flavor — https://camelot-py.readthedocs.io/ |
| **tabula-py** | `tabula-py` | Wraps Java tabula; good for ruled tables; JVM dependency |
| **PyMuPDF** | `pymupdf` | `page.find_tables()` — convenient, improving |
| **Docling TableFormer** | via `docling` | Strong on complex tables when models available |

---

## Figures / OCR / captions

| Approach | Install / stack | Role |
|----------|-----------------|------|
| **PyMuPDF image extract** | `pymupdf` | Dump embedded images + page renders for manual caption link |
| **Tesseract / pytesseract** | system `tesseract` + `pytesseract` | OCR scanned pages |
| **EasyOCR / Surya** | via Docling/marker stacks | Multilingual OCR inside heavier pipelines |
| **Caption linking** | heuristics in `relate_components.py` | Match `Figure N` refs + proximity; layout models improve this |

There is no single tiny library that perfectly pairs every figure with its caption across publishers; combine extraction + heuristics + (optional) Docling picture items.

---

## Multimodal document understanding (text ↔ table ↔ figure)

| System | Type | Notes | URL |
|--------|------|-------|-----|
| **Docling** | Local OSS | Structured doc with pictures/tables/text + provenance | https://docling-project.github.io/docling/ |
| **unstructured** | Local/API | Elements with metadata coordinates | GitHub above |
| **LlamaParse** / LlamaIndex parse | API-oriented | Strong practical PDF→md; not fully offline | https://docs.llamaindex.ai/ |
| **Google Document AI** | Cloud | Layout Parser + extractors | cloud.google.com/document-ai |
| **OKF** | Format + viz | Linked markdown concepts / knowledge graph (Google Cloud open format) | github.com/GoogleCloudPlatform/open-knowledge-format |
| **LangExtract** | OSS + LLM | Entities/relations with span grounding (optional; not what user meant) | github.com/google/langextract |
| **LayoutLMv3** | Model (HF) | Multimodal transformer for VrD tasks (IE/RE) | https://huggingface.co/docs/transformers/model_doc/layoutlmv3 |
| **Donut** | Model (HF) | OCR-free document → structured generation | https://huggingface.co/docs/transformers/model_doc/donut |
| **GraphDoc** | Research code | Graph attention over text/layout/image nodes (2022) | https://github.com/ZZR8066/GraphDoc · arXiv:2203.13530 |

---

## Knowledge / entity graphs from documents

| Tool | Role |
|------|------|
| **OKF bundle + visualizer** | Represent extracted concepts as linked markdown; visualize relationship graph (user-confirmed Google format) |
| **LangExtract** (optional) | Typed entities + span grounding over extracted text — complementary to OKF, not a substitute |
| **Document AI entities** | Nested entity properties for forms/invoices |
| **spaCy + custom** | Classical NER on `full_text.md`; link to figure refs via heuristics |
| **networkx** | Build/save relation graphs from `relations.json` (used conceptually by our scripts) |
| **DocGraphLM / LayoutLMv3-RE papers** | Research directions for spatial entity linking — not turnkey pip tools |

---

## What this repo installs by default

See [`scripts/requirements.txt`](scripts/requirements.txt): **pymupdf**, **pdfplumber**, lightweight helpers. Docling is attempted optionally in `extract_document.py` and skipped if import/install fails.
