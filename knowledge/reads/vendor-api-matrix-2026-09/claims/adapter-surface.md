---
type: Claim
title: Adapter surface is Established from docs; compile mapping is Hypothesis
tags: [rql, adapters]
status: provisional
---

# Claims

1. **[Established]** Major vector stores expose **incompatible** filter DSLs, hybrid fusion primitives, and filter+ANN composition modes (see matrix).
2. **[Established]** RRF appears as a **named** server feature in Qdrant, Elasticsearch, OpenSearch, and Milvus docs; elsewhere often client-side.
3. **[Hypothesis]** RQL LogicalPlan can compile to these shims via capability negotiation (PRE/POST/iterative/native-RRF/client-RRF/late-interaction).
4. **[Provisional]** Live smoke may refine UNKNOWN cells; until then do not upgrade UNKNOWN → Established.
