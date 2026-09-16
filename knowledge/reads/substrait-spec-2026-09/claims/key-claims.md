---
type: ClaimSet
title: Substrait key claims (docs-anchored)
description: Facts we cite carefully from substrait.io (accessed 2026-09-17).
tags: [substrait, claims]
status: provisional
generated:
  by: grok-bot/executor
  at: 2026-09-17T00:10:00+01:00
---

# Key claims

Label legend: **ESTABLISHED-FOR-US** = we verified the docs say it; **AUTHOR-CLAIM** = project self-description.

1. **ESTABLISHED-FOR-US:** Substrait specifies cross-language serialization of **data-compute / relational plans**, focusing on operation semantics, not a columnar memory format (Arrow analogy in About).  
   Evidence: home; about

2. **ESTABLISHED-FOR-US:** Substrait is **not** intended as a SQL replacement; SQL lacks sufficient detail and processable plan format; systems lower SQL to plans; Substrait aims to standardize that plan layer.  
   Evidence: about (“Why not use SQL?”)

3. **ESTABLISHED-FOR-US:** A plan is a **tree of relations** (DAG via reference relations); root = final output; leaves = inputs.  
   Evidence: relations/basics

4. **ESTABLISHED-FOR-US:** There is **no true distinction** between logical and physical operations in Substrait; physical classification is conventional; the consuming system decides what is a “physical plan.”  
   Evidence: physical_relations intro

5. **ESTABLISHED-FOR-US:** Extension mechanisms include YAML **simple extensions** (types, type variations, scalar/aggregate/window/table functions via extension URNs) and **advanced** forms: `AdvancedExtension` (optimization vs enhancement), custom read/write types, and **ExtensionLeafRel / ExtensionSingleRel / ExtensionMultiRel**.  
   Evidence: extensions

6. **ESTABLISHED-FOR-US:** Serializations include **binary** (inter-process) and **text** (human/debug); collections of plans may have one or more roots depending on consumer.  
   Evidence: serialization/basics

## Anti-claims

- That RQL JSON schemas are Substrait-compatible wire formats.
- That ANN / fusion / late-interaction ops are in Substrait core.
- That we validated Round-trip with DataFusion/Spark/Arrow Substrait libraries in this pass.
