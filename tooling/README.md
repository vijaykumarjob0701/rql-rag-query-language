# Tooling — multimodal PDF helpers

**Date:** 2026-09-16 (Europe/Dublin)  
Supports the slow read protocol ([`../methodology/02-read-protocol.md`](../methodology/02-read-protocol.md)).  
Library survey: [`python-libraries.md`](python-libraries.md).

## Setup (local venv)

```bash
cd tooling
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r scripts/requirements.txt
```

Optional heavier parsers (may fail on lean machines — that is OK):

```bash
pip install docling   # optional; extract_document.py --try-docling
```

## Scripts

### `extract_document.py`

```bash
source .venv/bin/activate
python scripts/extract_document.py /path/to/paper.pdf --out /tmp/acorn_extract
# or URL:
python scripts/extract_document.py 'https://arxiv.org/pdf/2403.04871.pdf' --out /tmp/acorn_extract --max-pages 8
```

Outputs:

| Path | Contents |
|------|----------|
| `full_text.md` / `.txt` | Extracted text with page markers |
| `structure.json` | Pages + heuristic sections |
| `tables/*.csv` + `*.md` | Tables from pdfplumber and/or pymupdf |
| `figures/` | Embedded images when present |
| `inventory.json` | Component listing + honest limits |

### `relate_components.py`

```bash
python scripts/relate_components.py /tmp/acorn_extract
```

Writes `relations.json`, `relations.mmd` (Mermaid), `relations.dot` (GraphViz).

### `notes_template.md`

Copy after Pass 4 of the read protocol for the 1–5% seed.

## Honest defaults

- Baseline backends are **pymupdf** + **pdfplumber** (reliable pip installs).  
- **Docling** is optional and degraded gracefully if missing.  
- Embedded raster images often **do not** equal numbered paper figures (many are vector drawings). Always visually open the PDF in Pass 2.  
- Relation edges are **heuristics** for Pass 3 assistance — not ground truth.

## Smoke test

See journal entry [`../journal/0004-slow-path-methodology.md`](../journal/0004-slow-path-methodology.md) and any `scripts/extract_out/` artifacts created locally (gitignored if large).

## Smoke-test result (2026-09-16 Europe/Dublin)

**PDF:** ACORN — *Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data* (arXiv:2403.04871), 15 pages, downloaded from `https://arxiv.org/pdf/2403.04871.pdf`.

| Output | Result |
|--------|--------|
| `full_text.md` | **Worked** — ~92.7k chars, page markers |
| `structure.json` | **Worked** — page sizes + heuristic section regex (noisy but present) |
| `figures/` | **Partial** — 30 embedded raster images extracted; these are **not** 1:1 with numbered paper figures (many figures are vector drawings) |
| `tables/` | **Empty** — neither pdfplumber nor pymupdf `find_tables` returned tables on this PDF (likely tables drawn as figures / complex layout) |
| `inventory.json` | **Worked** — lists components + honest limits |
| `relations.json` | **Worked** — 64 in-text refs, 21 caption-like nodes, heuristic edges (verify manually in Pass 3) |

**Takeaway:** Baseline extractors are good enough to *start* Pass 2 inventory; they do **not** replace opening the PDF for figures/tables. For table-heavy re-reads, try Docling/camelot later or manually transcribe key tables into notes.
