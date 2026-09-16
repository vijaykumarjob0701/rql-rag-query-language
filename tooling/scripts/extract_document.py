#!/usr/bin/env python3
"""
Extract text, structure, tables, and figures from a PDF (local path or URL).

Baseline: pymupdf + pdfplumber. Optionally tries docling if installed.
Outputs a folder with full_text, structure.json, tables/, figures/, inventory.json.

Usage:
  python extract_document.py INPUT [--out DIR] [--max-pages N]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

SECTION_RE = re.compile(
    r"^(?P<num>(?:\d+\.)+\d*|\d+)\s+(?P<title>[A-Z][^\n]{2,120})$",
    re.MULTILINE,
)


def download_pdf(url: str, dest: Path) -> Path:
    import requests

    r = requests.get(url, timeout=120, headers={"User-Agent": "rql-research-extract/0.1"})
    r.raise_for_status()
    dest.write_bytes(r.content)
    return dest


def resolve_input(src: str, work: Path) -> Path:
    if src.startswith("http://") or src.startswith("https://"):
        name = Path(urlparse(src).path).name or "download.pdf"
        if not name.lower().endswith(".pdf"):
            name += ".pdf"
        return download_pdf(src, work / name)
    path = Path(src).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Input not found: {path}")
    return path


def try_docling(pdf_path: Path, out_dir: Path) -> dict[str, Any] | None:
    try:
        from docling.document_converter import DocumentConverter  # type: ignore
    except Exception as e:
        return {"attempted": True, "available": False, "error": str(e)}

    try:
        converter = DocumentConverter()
        result = converter.convert(str(pdf_path))
        doc = result.document
        md = doc.export_to_markdown()
        (out_dir / "docling_full.md").write_text(md, encoding="utf-8")
        # Best-effort JSON dump if available
        if hasattr(doc, "export_to_dict"):
            (out_dir / "docling_document.json").write_text(
                json.dumps(doc.export_to_dict(), indent=2, default=str),
                encoding="utf-8",
            )
        return {"attempted": True, "available": True, "ok": True}
    except Exception as e:
        return {"attempted": True, "available": True, "ok": False, "error": str(e)}


def extract_with_pymupdf(pdf_path: Path, out_dir: Path, max_pages: int | None) -> dict[str, Any]:
    import pymupdf as fitz

    figures_dir = out_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    n_pages = doc.page_count
    limit = n_pages if max_pages is None else min(n_pages, max_pages)

    text_parts: list[str] = []
    pages_meta: list[dict[str, Any]] = []
    figures: list[dict[str, Any]] = []
    tables_mu: list[dict[str, Any]] = []

    img_global = 0
    for i in range(limit):
        page = doc[i]
        page_text = page.get_text("text")
        text_parts.append(f"\n\n--- Page {i + 1} ---\n\n{page_text}")
        blocks = page.get_text("dict").get("blocks", [])
        pages_meta.append(
            {
                "page": i + 1,
                "width": page.rect.width,
                "height": page.rect.height,
                "n_blocks": len(blocks),
            }
        )

        # Embedded images
        for img_i, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n > 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                img_global += 1
                fname = f"page{i + 1:03d}_img{img_i + 1:02d}_xref{xref}.png"
                fpath = figures_dir / fname
                pix.save(str(fpath))
                figures.append(
                    {
                        "id": f"embedded-{img_global}",
                        "page": i + 1,
                        "path": str(fpath.relative_to(out_dir)),
                        "xref": xref,
                        "width": pix.width,
                        "height": pix.height,
                        "kind": "embedded_image",
                    }
                )
            except Exception as e:
                figures.append(
                    {
                        "id": f"embedded-fail-{i + 1}-{img_i + 1}",
                        "page": i + 1,
                        "error": str(e),
                        "kind": "embedded_image",
                    }
                )

        # Optional page render thumbnail for pages with few embeds (helps caption review)
        # Skip full-page renders by default to keep smoke-test light.

        # Tables via pymupdf
        try:
            tf = page.find_tables()
            for t_i, table in enumerate(tf.tables):
                data = table.extract()
                tables_mu.append(
                    {
                        "id": f"pymupdf-p{i + 1}-t{t_i + 1}",
                        "page": i + 1,
                        "backend": "pymupdf",
                        "nrows": len(data) if data else 0,
                        "ncols": len(data[0]) if data and data[0] else 0,
                        "data": data,
                    }
                )
        except Exception:
            pass

    doc.close()
    full_text = "".join(text_parts).strip() + "\n"
    (out_dir / "full_text.md").write_text(full_text, encoding="utf-8")
    (out_dir / "full_text.txt").write_text(full_text, encoding="utf-8")

    sections = []
    for m in SECTION_RE.finditer(full_text):
        sections.append(
            {
                "number": m.group("num"),
                "title": m.group("title").strip(),
                "char_start": m.start(),
            }
        )

    structure = {
        "source": str(pdf_path),
        "page_count_processed": limit,
        "page_count_total": n_pages,
        "pages": pages_meta,
        "sections_heuristic": sections,
    }
    (out_dir / "structure.json").write_text(json.dumps(structure, indent=2), encoding="utf-8")

    return {
        "full_text_chars": len(full_text),
        "sections_heuristic": len(sections),
        "figures": figures,
        "tables_pymupdf": tables_mu,
        "pages_processed": limit,
        "pages_total": n_pages,
    }


def extract_tables_pdfplumber(pdf_path: Path, out_dir: Path, max_pages: int | None) -> list[dict[str, Any]]:
    import pdfplumber

    tables_dir = out_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    found: list[dict[str, Any]] = []

    with pdfplumber.open(pdf_path) as pdf:
        limit = len(pdf.pages) if max_pages is None else min(len(pdf.pages), max_pages)
        for i in range(limit):
            page = pdf.pages[i]
            try:
                tables = page.extract_tables() or []
            except Exception as e:
                found.append({"page": i + 1, "error": str(e), "backend": "pdfplumber"})
                continue
            for t_i, table in enumerate(tables):
                tid = f"pdfplumber-p{i + 1}-t{t_i + 1}"
                md_path = tables_dir / f"{tid}.md"
                csv_path = tables_dir / f"{tid}.csv"
                # markdown
                lines = []
                if table:
                    header = [str(c) if c is not None else "" for c in table[0]]
                    lines.append("| " + " | ".join(header) + " |")
                    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
                    for row in table[1:]:
                        cells = [str(c) if c is not None else "" for c in row]
                        # pad
                        while len(cells) < len(header):
                            cells.append("")
                        lines.append("| " + " | ".join(cells[: len(header)]) + " |")
                md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
                # csv
                import csv

                with csv_path.open("w", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    for row in table or []:
                        w.writerow(["" if c is None else c for c in row])
                found.append(
                    {
                        "id": tid,
                        "page": i + 1,
                        "backend": "pdfplumber",
                        "path_md": str(md_path.relative_to(out_dir)),
                        "path_csv": str(csv_path.relative_to(out_dir)),
                        "nrows": len(table) if table else 0,
                    }
                )
    return found


def write_pymupdf_tables(tables: list[dict[str, Any]], out_dir: Path) -> list[dict[str, Any]]:
    tables_dir = out_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    import csv

    meta = []
    for t in tables:
        if "data" not in t:
            meta.append(t)
            continue
        tid = t["id"]
        data = t["data"] or []
        csv_path = tables_dir / f"{tid}.csv"
        md_path = tables_dir / f"{tid}.md"
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for row in data:
                w.writerow(["" if c is None else c for c in row])
        lines = []
        if data:
            header = [str(c) if c is not None else "" for c in data[0]]
            lines.append("| " + " | ".join(header) + " |")
            lines.append("| " + " | ".join(["---"] * len(header)) + " |")
            for row in data[1:]:
                cells = [str(c) if c is not None else "" for c in row]
                while len(cells) < len(header):
                    cells.append("")
                lines.append("| " + " | ".join(cells[: len(header)]) + " |")
        md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        entry = {k: v for k, v in t.items() if k != "data"}
        entry["path_md"] = str(md_path.relative_to(out_dir))
        entry["path_csv"] = str(csv_path.relative_to(out_dir))
        meta.append(entry)
    return meta


def main() -> int:
    ap = argparse.ArgumentParser(description="Extract multimodal inventory from a PDF")
    ap.add_argument("input", help="Local PDF path or URL")
    ap.add_argument(
        "--out",
        default=None,
        help="Output directory (default: ./extract_out/<pdf-stem>)",
    )
    ap.add_argument("--max-pages", type=int, default=None, help="Limit pages processed")
    ap.add_argument(
        "--try-docling",
        action="store_true",
        help="Attempt docling if installed (graceful degrade)",
    )
    args = ap.parse_args()

    scripts_dir = Path(__file__).resolve().parent
    default_root = scripts_dir / "extract_out"
    with tempfile.TemporaryDirectory(prefix="rql-pdf-") as tmp:
        work = Path(tmp)
        try:
            pdf_path = resolve_input(args.input, work)
        except Exception as e:
            print(f"ERROR resolving input: {e}", file=sys.stderr)
            return 1

        out_dir = Path(args.out) if args.out else default_root / pdf_path.stem
        out_dir.mkdir(parents=True, exist_ok=True)

        # Copy or note source
        meta_src = {"input": args.input, "resolved_pdf": str(pdf_path.name)}

        mu = extract_with_pymupdf(pdf_path, out_dir, args.max_pages)
        tables_mu = write_pymupdf_tables(mu["tables_pymupdf"], out_dir)
        tables_pl = extract_tables_pdfplumber(pdf_path, out_dir, args.max_pages)

        docling_info = None
        if args.try_docling:
            docling_info = try_docling(pdf_path, out_dir)

        inventory = {
            "source": meta_src,
            "backends": {
                "pymupdf": True,
                "pdfplumber": True,
                "docling": docling_info,
            },
            "pages_processed": mu["pages_processed"],
            "pages_total": mu["pages_total"],
            "full_text_chars": mu["full_text_chars"],
            "sections_heuristic_count": mu["sections_heuristic"],
            "figures": mu["figures"],
            "tables": tables_mu + tables_pl,
            "components": {
                "text": ["full_text.md", "full_text.txt"],
                "structure": ["structure.json"],
                "figures_dir": "figures/",
                "tables_dir": "tables/",
            },
            "honest_limits": [
                "Section detection is heuristic regex on extracted text, not true TOC parsing.",
                "Figure–caption semantic linking is deferred to relate_components.py (refs + proximity).",
                "Embedded images ≠ paper figures; many figures are vector drawings without image XObjects.",
                "Table extraction may duplicate across pymupdf and pdfplumber backends.",
            ],
        }
        (out_dir / "inventory.json").write_text(json.dumps(inventory, indent=2), encoding="utf-8")

        print(f"Wrote extraction to: {out_dir}")
        print(
            f"  pages={mu['pages_processed']}/{mu['pages_total']} "
            f"chars={mu['full_text_chars']} "
            f"figures={len(mu['figures'])} "
            f"tables={len(inventory['tables'])}"
        )
        if docling_info is not None:
            print(f"  docling: {docling_info}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
