---
title: "Albert Gu"
layout: default
parent: Speakers
nav_exclude: true
---

# Albert Gu

**Affiliation:** Assistant Professor, Machine Learning Department, Carnegie Mellon University; Chief Scientist, Cartesia AI

**Recognition:** TIME AI100 — list of most influential AI researchers (2024)

**Course:** [CS25 Week 3 — State Space Models & Tradeoffs](sessions/2026-04-16-ssms/)

---

## Background

PhD at Stanford under Chris Ré, now Assistant Professor at CMU and Chief Scientist at Cartesia AI (a company commercializing SSM technology). Recognized on the TIME AI100 list in 2024 for his work on deep sequence modeling.

Research focus: theoretical and empirical foundations of deep learning, particularly new approaches to neural network architectures for sequence modeling.

## Key Papers

| Paper | Venue | Contribution |
|-------|-------|--------------|
| [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) | 2023 | Selective SSM with content-aware reasoning; O(n) inference; 5× throughput vs Transformers |
| [Mamba-2: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060) | ICML 2024 | Proves SSM-Transformer equivalence via structured semiseparable matrices; 2-8× speedup |
| [Mamba-3](https://arxiv.org/abs/2603.15569) | 2026 | Latest iteration with improved quality and efficiency |

## Related Work

- [S4: Structured State Spaces](https://arxiv.org/abs/2111.00396) — foundational SSM work (Gu et al., 2021)
- [Hungry Hungry Hippos](https://arxiv.org/abs/2212.14052) — SSM for language modeling at scale
- H-Nets — tokenizer-free models (referenced in CS25 talk abstract)

## Why Relevant to Autonomy

- **Linear-time inference** enables deployment on edge/robotics hardware
- **100K+ context** supports long-horizon mission memory across sessions
- **Streaming sensor data** maps naturally to SSM's continuous-time formulation
- **Cartesia AI** is actively building SSM-based products — real-world deployment pressure

## Question Bank

**Technical:**
1. How does selective SSM compare to linear attention variants (Performer, Linformer) in practice?
2. What's the state dimension / memory / quality tradeoff in Mamba?
3. How does Mamba handle code vs natural language differently?
4. Where does Mamba significantly underperform transformers?
5. How does Mamba-3 improve over Mamba-2?

**Autonomy-specific:**
6. Have you tested SSMs on multimodal sensor fusion (vision + proprioception + language)?
7. How do SSMs handle irregularly-sampled sensor data common in robotics?
8. Is there work on action-conditioned SSMs for control?
9. How does Mamba compare to transformers for offline RL / behavior cloning?
10. What's the minimum hardware to run Mamba-3 efficiently? Edge deployment story?

**Research directions:**
11. Is the SSM-Transformer equivalence practical for model conversion, or mostly theoretical?
12. What enables tokenizer-free models like H-Nets? Is tokenization a fundamental bottleneck?
13. What's the path to 1M+ context windows? Fundamental limits?

## Cross-References

- **CS25 Week 2 (JEPA)** — World models, planning, long-horizon prediction
- **CS25 Week 4 (Ultra-Scale)** — Training infrastructure for large models
- **CS25 Week 10 (Modal/GPU)** — Deployment, edge inference

---

*Researched: 2026-04-16 (verified against course site and arXiv abstracts)*
