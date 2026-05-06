---
title: "Pre-Read: Andrew Lampinen (Anthropic)"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: Andrew Lampinen (Anthropic)

**Date:** May 7, 2026
**Speaker:** Andrew Lampinen (Anthropic)
**Topic:** TBD — likely Interpretability &/ Efficient Transformers

---

## Topic Overview

Andrew Lampinen's research bridges **cognitive science and AI**, with recent work focusing on two major threads:

1. **Interpretability:** Understanding *how* transformers reason via attribution graphs and circuit analysis
2. **Efficiency:** Identifying which transformer blocks matter most (block importance) to create efficient variants

His CS25 talk is likely to focus on one or both of these themes. Both are highly relevant to building trustworthy autonomous systems.

---

## Speaker Bio

**Andrew Lampinen** is a Research Scientist at Anthropic, formerly at Google DeepMind. He completed his PhD at Stanford, where he bridged cognitive science and AI research. His work explores how complex behaviors and representations emerge from learning experiences — with a particular focus on language as a cognitive tool and how explanations shape reasoning.

---

## Key Papers

### 1. Puzzle: Efficient Transformer Variants through Block Importance (ICML 2025)
**arXiv:** [2408.07478](https://arxiv.org/abs/2408.07478)

**Contribution:** Identified which transformer blocks are most important for different capabilities, then used this analysis to create efficient variants.

**Key details:**
- Introduced "block importance" as a pruning signal
- Produced Nemotron-Super-49B and Nemotron-Ultra-253B — efficient models derived from larger parents
- Won an ICML 2025 award

**Why it matters:** Understanding which parts of a transformer actually carry capabilities enables targeted compression and efficient deployment — directly relevant to edge robotics.

🔗 [GitHub](https://github.com/NVIDIA/Puzzle)

---

### 2. On the Biology of a Large Language Model (Anthropic, 2025)
**URL:** [transformer-circuits.pub/2025/attribution-graphs/biology.html](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

**Contribution:** Built attribution graphs for Claude 3.5 Haiku — mapping how information flows through the model during reasoning.

**Key details:**
- Shows that LLM reasoning can be traced through interpretable circuits
- Enables verification of *which* internal computations produce specific outputs
- Bridges mechanistic interpretability with practical model analysis

**Why it matters:** Attribution graphs are a step toward understanding the internal mechanics of frontier models — critical for safety and trust in autonomous deployments.

---

### 3. Language as a Cognitive Tool (Stanford PhD Research)
**Context:** Andrew's Stanford research explored how language functions as a cognitive mechanism in both humans and AI systems.

**Relevance:** Frames language not just as communication but as a tool for structured reasoning — implications for robot instruction following and world model architectures.

---

## Why It Matters for Autonomy / Robotics

| Aspect | Relevance |
|--------|-----------|
| **Interpretability** | Essential for trustworthy autonomous systems — need to understand *why* the robot made a decision |
| **Block importance** | Could enable targeted compression for edge deployment — prune the parts that don't matter for your task |
| **Cognitive science** | How capabilities emerge from learning is directly relevant to training embodied AI systems |
| **Safety & control** | Attribution graphs offer a path to verifying model reasoning in safety-critical scenarios |
| **Efficient inference** | Puzzle framework's insights enable smaller, faster models without capability loss |

---

## Question Bank

### Interpretability Questions

1. **How do attribution graphs scale to multimodal models (vision + language + proprioception)?**
   - Current work is on text-only models. Robotics requires understanding across modalities.

2. **Can attribution graphs detect distributional shift or out-of-distribution inputs in real time?**
   - Critical for autonomous robots that encounter novel situations.

3. **How stable are attribution patterns across semantically equivalent prompts?**
   - If I ask the same question two ways, do I get the same internal reasoning path?

4. **What's the relationship between block importance and circuit-level analysis?**
   - Are important blocks doing the same computation across different tasks?

### Efficiency Questions

5. **What's the minimal block subset needed for a specific capability (e.g., instruction following vs. scene understanding)?**
   - Task-specific pruning could dramatically reduce compute for robotics applications.

6. **Does block importance vary by domain? Would a block important for code be unimportant for visual reasoning?**
   - This has implications for building specialist vs. generalist robot brains.

7. **How does the Puzzle framework compare to sparse pruning methods like Magnav.jl or Wanda?**
   - Need to understand the state of the art in practical transformer compression.

### Cognitive Science / Emergence Questions

8. **What have you learned about how explanations shape model behavior?**
   - Does prompting with explanations improve reasoning consistency?

9. **Are there parallels between capability emergence in your transformer variants and human cognitive development?**
   - Do we see similar critical periods or scaffolding effects in trained models?

### Robotics / Autonomy Questions

10. **How might block importance analysis inform action-conditioned transformers for robot control?**
    - If some blocks matter more for temporal sequences, that could guide architecture choices.

11. **Could attribution graphs help debug failure modes in autonomous robot policies?**
    - Trace the internal computation that led to a bad decision — then fix the root cause.

12. **Is there work on using interpretability tools to verify safety properties in robot control loops?**
    - e.g., "can we prove this policy never takes an unsafe action in region X?"

---

## Pre-Lecture Reading

### Essential
- [Puzzle paper (arXiv)](https://arxiv.org/abs/2408.07478)
- [Attribution graphs — On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

### Background
- [Andrew's website](https://lampinen.github.io/)
- [Anthropic interpretability research](https://www.anthropic.com/research)
- [Circuit analysis overview (Distill)](https://distill.pub/2020/circuits/zoom-in/)

---

## Cross-References

- **Week 3 (SSMs — Albert Gu):** Mamba's selective mechanism is another example of understanding *what matters* in sequence models
- **Week 4 (Hugging Face — Nouamane Tazi):** SmolLM3 shows small models can be capable; Puzzle shows *why* they can be small
- **Week 7 (Med-PaLM — Vivek Natarajan):** Safety-critical deployment needs interpretability for trust

---

## Slides Status

**Slides not yet posted** (as of 2026-05-06). Will check again post-lecture.

---

*Prepared: 2026-05-06 • Updated with full speaker research*
