# Python libraries for multimodal document research (survey 2024–2026)

**Survey date:** 2026-09-16 (Europe/Dublin)  
**Purpose:** Support the slow read protocol ([`../methodology/02-read-protocol.md`](../methodology/02-read-protocol.md)) — text, layout, tables, figures, and relationships — without inventing RQL claims.

**Baseline for this repo’s scripts:** `pymupdf` + `pdfplumber` (always installable via pip). Heavier stacks (Docling, MinerU, …) are optional.

---

## Likely Google libraries (user memory check)

The user recalled a recent Google library that relates entities / images / document structure. Strong matches:

| Library | What it is | Why it matches the memory | Install / access |
|---------|------------|---------------------------|------------------|
| **LangExtract** (`google/langextract`) | Open-source Python lib (announced ~2025 on Google Developers Blog) for LLM-based structured extraction with **precise source grounding**, relationship-style attributes, JSONL export, interactive HTML visualization | “Entities + relationships + grounding to source spans”; very recent; widely discussed | `pip install langextract` — https://github.com/google/langextract · https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/ |
| **Google Cloud Document AI — Layout Parser** | Managed processor: layout elements, context-aware chunks, **table & image annotation** options for RAG | Multimodal document structure; image↔table↔text in one API | `google-cloud-documentai` + GCP processor — https://cloud.google.com/document-ai/docs/layout-parse-quickstart |
| **Document AI Form / Custom Extractors** | Schematized **entities** (nested properties), normalized values, confidence | Classic “entity extraction from docs” Google product | Same client library; specialized processors |

**Also Google-adjacent (not the likely “recent lib”):** Vision API OCR; Gemini multimodal document understanding via API (not a dedicated extraction package).

**Recommendation:** Treat **LangExtract** as the open-source name most people mean in 2025–2026; treat **Document AI Layout Parser** as the managed multimodal layout/entity/image path. Local RQL research can stay offline with pymupdf/pdfplumber/Docling and optionally call LangExtract later for entity graphs over extracted text.

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
| **LangExtract** | OSS + LLM | Entities/relations with span grounding (text-first; feed it extracted text) | github.com/google/langextract |
| **LayoutLMv3** | Model (HF) | Multimodal transformer for VrD tasks (IE/RE) | https://huggingface.co/docs/transformers/model_doc/layoutlmv3 |
| **Donut** | Model (HF) | OCR-free document → structured generation | https://huggingface.co/docs/transformers/model_doc/donut |
| **GraphDoc** | Research code | Graph attention over text/layout/image nodes (2022) | https://github.com/ZZR8066/GraphDoc · arXiv:2203.13530 |

---

## Knowledge / entity graphs from documents

| Tool | Role |
|------|------|
| **LangExtract** | Extract typed entities + attributes with source offsets; visualize; good stepping stone to a graph |
| **Document AI entities** | Nested entity properties for forms/invoices |
| **spaCy + custom** | Classical NER on `full_text.md`; link to figure refs via heuristics |
| **networkx** | Build/save relation graphs from `relations.json` (used conceptually by our scripts) |
| **DocGraphLM / LayoutLMv3-RE papers** | Research directions for spatial entity linking — not turnkey pip tools |

---

## What this repo installs by default

See [`scripts/requirements.txt`](scripts/requirements.txt): **pymupdf**, **pdfplumber**, lightweight helpers. Docling is attempted optionally in `extract_document.py` and skipped if import/install fails.
