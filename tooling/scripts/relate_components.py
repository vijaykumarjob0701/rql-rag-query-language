#!/usr/bin/env python3
"""
Build a simple relationship graph between figures/tables and referring text.

Heuristics:
  - Find 'Figure N' / 'Fig. N' / 'Table N' / 'Algorithm N' references in full_text
  - Link to inventory components when ids/pages match
  - Attach nearby paragraph snippets as caption/context candidates

Usage:
  python relate_components.py EXTRACT_DIR [--out relations.json]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

REF_RE = re.compile(
    r"(?P<label>Figures?|Figs?\.?|Tables?|Algorithms?|Alg\.?|Equations?|Eqs?\.?)\s*"
    r"(?P<num>\d+[a-z]?)",
    re.IGNORECASE,
)

CAPTION_RE = re.compile(
    r"^(?P<label>Figure|Fig\.|Table|Algorithm)\s+(?P<num>\d+[a-z]?)\s*[:.\-—]?\s*(?P<cap>.*)$",
    re.IGNORECASE | re.MULTILINE,
)


def load_text(extract_dir: Path) -> str:
    for name in ("full_text.md", "full_text.txt"):
        p = extract_dir / name
        if p.is_file():
            return p.read_text(encoding="utf-8", errors="replace")
    raise FileNotFoundError(f"No full_text.md/.txt in {extract_dir}")


def paragraph_at(text: str, index: int, radius: int = 400) -> str:
    start = max(0, index - radius)
    end = min(len(text), index + radius)
    # snap to newlines lightly
    snip = text[start:end].replace("\n", " ")
    return re.sub(r"\s+", " ", snip).strip()


def page_near(text: str, index: int) -> int | None:
    # Look backward for '--- Page N ---' markers from extract_document.py
    ahead = text[: index + 1]
    matches = list(re.finditer(r"--- Page (\d+) ---", ahead))
    if matches:
        return int(matches[-1].group(1))
    return None


def normalize_label(label: str) -> str:
    l = label.lower().rstrip(".")
    if l.startswith("fig"):
        return "figure"
    if l.startswith("tab"):
        return "table"
    if l.startswith("alg"):
        return "algorithm"
    if l.startswith("eq"):
        return "equation"
    return l


def build_graph(extract_dir: Path) -> dict[str, Any]:
    text = load_text(extract_dir)
    inv_path = extract_dir / "inventory.json"
    inventory = json.loads(inv_path.read_text(encoding="utf-8")) if inv_path.is_file() else {}

    nodes: dict[str, dict[str, Any]] = {}
    edges: list[dict[str, Any]] = []

    # Nodes from inventory figures/tables
    for fig in inventory.get("figures", []):
        nid = f"asset:{fig.get('id', fig.get('path'))}"
        nodes[nid] = {
            "id": nid,
            "type": "figure_asset",
            "page": fig.get("page"),
            "path": fig.get("path"),
            "kind": fig.get("kind"),
        }
    for tab in inventory.get("tables", []):
        nid = f"table:{tab.get('id')}"
        nodes[nid] = {
            "id": nid,
            "type": "table_extract",
            "page": tab.get("page"),
            "backend": tab.get("backend"),
            "path_md": tab.get("path_md"),
        }

    # Caption-like lines
    for m in CAPTION_RE.finditer(text):
        kind = normalize_label(m.group("label"))
        num = m.group("num")
        nid = f"caption:{kind}:{num}"
        nodes[nid] = {
            "id": nid,
            "type": "caption",
            "kind": kind,
            "number": num,
            "text": (m.group("cap") or "").strip()[:500],
            "page": page_near(text, m.start()),
            "char_start": m.start(),
        }

    # In-text references
    for m in REF_RE.finditer(text):
        kind = normalize_label(m.group("label"))
        num = m.group("num")
        ref_id = f"ref:{kind}:{num}:{m.start()}"
        page = page_near(text, m.start())
        nodes[ref_id] = {
            "id": ref_id,
            "type": "reference",
            "kind": kind,
            "number": num,
            "page": page,
            "snippet": paragraph_at(text, m.start()),
            "char_start": m.start(),
        }
        cap_id = f"caption:{kind}:{num}"
        if cap_id in nodes:
            edges.append(
                {
                    "source": ref_id,
                    "target": cap_id,
                    "relation": "refers_to_caption",
                }
            )
        else:
            # placeholder logical node
            logical = f"logical:{kind}:{num}"
            if logical not in nodes:
                nodes[logical] = {
                    "id": logical,
                    "type": "logical_component",
                    "kind": kind,
                    "number": num,
                }
            edges.append(
                {
                    "source": ref_id,
                    "target": logical,
                    "relation": "refers_to",
                }
            )

        # Link to extracted assets on same page (weak heuristic)
        if page is not None:
            for nid, node in list(nodes.items()):
                if node.get("type") == "figure_asset" and node.get("page") == page and kind == "figure":
                    edges.append(
                        {
                            "source": ref_id,
                            "target": nid,
                            "relation": "same_page_figure_asset",
                            "confidence": "low",
                        }
                    )
                if node.get("type") == "table_extract" and node.get("page") == page and kind == "table":
                    edges.append(
                        {
                            "source": ref_id,
                            "target": nid,
                            "relation": "same_page_table_extract",
                            "confidence": "low",
                        }
                    )

    # Caption → same-page assets
    for nid, node in list(nodes.items()):
        if node.get("type") != "caption":
            continue
        page = node.get("page")
        kind = node.get("kind")
        if page is None:
            continue
        for aid, anode in list(nodes.items()):
            if kind == "figure" and anode.get("type") == "figure_asset" and anode.get("page") == page:
                edges.append(
                    {
                        "source": nid,
                        "target": aid,
                        "relation": "caption_near_asset",
                        "confidence": "medium",
                    }
                )
            if kind == "table" and anode.get("type") == "table_extract" and anode.get("page") == page:
                edges.append(
                    {
                        "source": nid,
                        "target": aid,
                        "relation": "caption_near_table",
                        "confidence": "medium",
                    }
                )

    # Dedup edges
    seen = set()
    uniq_edges = []
    for e in edges:
        key = (e["source"], e["target"], e["relation"])
        if key in seen:
            continue
        seen.add(key)
        uniq_edges.append(e)

    return {
        "extract_dir": str(extract_dir),
        "nodes": list(nodes.values()),
        "edges": uniq_edges,
        "stats": {
            "n_nodes": len(nodes),
            "n_edges": len(uniq_edges),
            "n_refs": sum(1 for n in nodes.values() if n["type"] == "reference"),
            "n_captions": sum(1 for n in nodes.values() if n["type"] == "caption"),
        },
        "honest_limits": [
            "Reference parsing is regex-based; misses 'Figs. 3–5' ranges and 'Figure~\ref{}'.",
            "Embedded images often do not correspond 1:1 to numbered paper figures.",
            "same_page_* edges are weak heuristics — verify in Pass 3 manually.",
        ],
    }


def to_mermaid(graph: dict[str, Any]) -> str:
    lines = ["flowchart LR"]
    # Limit size for readability
    caps = [n for n in graph["nodes"] if n["type"] == "caption"][:20]
    logicals = [n for n in graph["nodes"] if n["type"] == "logical_component"][:20]
    for n in caps + logicals:
        safe = n["id"].replace(":", "_").replace(".", "_")
        label = f"{n.get('kind', '')} {n.get('number', '')}".strip()
        lines.append(f'  {safe}["{label}"]')
    count = 0
    for e in graph["edges"]:
        if e["relation"] not in ("refers_to_caption", "refers_to"):
            continue
        # collapse many refs: only caption/logical targets already listed
        s = e["source"].replace(":", "_").replace(".", "_")
        t = e["target"].replace(":", "_").replace(".", "_")
        if not any(n["id"] == e["target"] for n in caps + logicals):
            continue
        # create tiny ref node
        lines.append(f'  {s}("{e["relation"]}") --> {t}')
        count += 1
        if count >= 40:
            break
    if count == 0:
        lines.append('  empty["No caption/ref edges found"]')
    return "\n".join(lines) + "\n"


def to_dot(graph: dict[str, Any]) -> str:
    lines = ["digraph relations {", "  rankdir=LR;", '  node [shape=box, fontsize=10];']
    for n in graph["nodes"]:
        if n["type"] not in ("caption", "logical_component", "table_extract", "figure_asset"):
            continue
        safe = n["id"].replace('"', "")
        label = n["id"]
        lines.append(f'  "{safe}" [label="{label}"];')
    for e in graph["edges"][:200]:
        lines.append(
            f'  "{e["source"]}" -> "{e["target"]}" [label="{e["relation"]}"];'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Relate figures/tables to text references")
    ap.add_argument("extract_dir", type=Path, help="Output dir from extract_document.py")
    ap.add_argument("--out", type=Path, default=None, help="relations.json path")
    args = ap.parse_args()

    extract_dir = args.extract_dir.resolve()
    graph = build_graph(extract_dir)
    out_json = args.out or (extract_dir / "relations.json")
    out_json.write_text(json.dumps(graph, indent=2), encoding="utf-8")
    mermaid = to_mermaid(graph)
    (extract_dir / "relations.mmd").write_text(mermaid, encoding="utf-8")
    (extract_dir / "relations.dot").write_text(to_dot(graph), encoding="utf-8")
    print(f"Wrote {out_json}")
    print(f"  nodes={graph['stats']['n_nodes']} edges={graph['stats']['n_edges']}")
    print(f"  also: relations.mmd relations.dot")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
