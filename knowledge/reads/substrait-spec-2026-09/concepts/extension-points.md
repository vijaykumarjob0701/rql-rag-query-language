---
type: Concept
title: Substrait extension points
tags: [substrait, extensions]
status: established-docs
---

# Extension points

| Mechanism | Role |
|-----------|------|
| YAML simple extensions | Types, type variations, scalar/agg/window/table functions; identified by `extension::OWNER:ID`-style URNs |
| `AdvancedExtension.optimization` | Hints that may be ignored |
| `AdvancedExtension.enhancement` | Semantic changes consumers must understand |
| ExtensionLeaf/Single/MultiRel | Entirely new relational ops; output schema derivation is producer/consumer agreement via `detail` |
| ExtensionTable / write objects | Custom sources/sinks |

**RQL adjacency `[hypothesis]`:** Retrieval-specific ops (`Search_late`, `Fuse_rrf`, `FilterExec` modes) would map most naturally to **custom relations** or enhancements — only if/when an interchange goal appears. Today RQL keeps its own JSON IR.
