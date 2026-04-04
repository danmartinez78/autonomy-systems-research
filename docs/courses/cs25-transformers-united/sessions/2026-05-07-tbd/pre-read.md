---
title: "Pre-Read: TBD Topic"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: TBD Topic

**Date:** May 7, 2026
**Speaker:** Andrew Lampinen (Anthropic)

---

## Topic Overview

Topic TBD — check course site for updates. Speaker's research spans interpretability, cognitive science, and efficient transformer architectures.

---

## Key Concepts

Awaiting topic announcement.

---

## Speaker

### Andrew Lampinen

**Affiliation:** Anthropic (Research Scientist), formerly Google DeepMind

**Background:** PhD at Stanford, bridges cognitive science and AI. Studies how complex behaviors and representations emerge from learning experiences. Particularly interested in language as a cognitive tool and how explanations shape reasoning.

**Key contributions:**

- **Puzzle Framework** (ICML 2025) — Efficient transformer variants through block importance analysis
- **Anthropic Interpretability** — Attribution graphs for understanding Claude's reasoning
- **Cognitive science × AI** — Understanding emergence of capabilities

---

## Papers

### 1. Puzzle: Efficient Transformer Variants through Block Importance (ICML 2025)

**Contribution:** Created efficient transformer variants (Nemotron-Super-49B, Nemotron-Ultra-253B) by analyzing which blocks matter most.

**Key insight:** Not all transformer blocks are equally important — understanding block importance enables efficient architectures.

🔗 [LinkedIn summary](https://www.linkedin.com/posts/andrew-lampinen-926398a0/)

---

### 2. On the Biology of a Large Language Model (Anthropic, 2025)

**Contribution:** Attribution graphs for Claude 3.5 Haiku — mapping how information flows through the model.

**Key insight:** Can trace specific reasoning paths and identify which circuits are responsible for which behaviors.

🔗 [Anthropic paper](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Interpretability** | Essential for trustworthy autonomous systems — need to understand *why* decisions are made |
| **Block importance** | Could inform efficient deployment for edge robotics — prune/compress intelligently |
| **Cognitive science angle** | Understanding emergence of capabilities informs how we might build more robust systems |
| **Safety** | Attribution graphs enable debugging of failure modes |

---

## Question Bank

### Interpretability Questions

1. How do attribution graphs scale to multimodal inputs (vision + language)?
2. Can we use attribution to detect when a model is operating outside its training distribution?
3. How stable are attribution patterns across different prompts about the same topic?

### Efficiency Questions

4. What's the tradeoff between block pruning and capability degradation?
5. Are certain blocks more important for reasoning vs retrieval?
6. How does block importance change with model scale?

### Cognitive Science Questions

7. What have you learned about how explanations shape model behavior?
8. Are there parallels between human cognitive development and model capability emergence?

---

## Pre-Lecture Reading

### Essential
- [Andrew's website](https://lampinen.github.io/)
- [Attribution graphs paper](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

### Background
- [Anthropic interpretability research](https://www.anthropic.com/research)
- [Circuit analysis overview](https://distill.pub/2020/circuits/zoom-in/)

---

## Cross-References

*To be populated once topic is announced.*

---

*Prepared: 2026-04-04 • Topic TBD*
