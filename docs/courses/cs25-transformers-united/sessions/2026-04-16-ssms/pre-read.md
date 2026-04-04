---
title: "Pre-Read: State Space Models & Mamba"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: State Space Models & Mamba

**Date:** April 16, 2026
**Speaker:** Albert Gu (CMU)

---

## Topic Overview

State Space Models (SSMs) offer an alternative to attention-based transformers with O(n) complexity instead of O(n²). Albert Gu's Mamba architecture has emerged as the leading SSM, enabling 100K+ context windows and efficient inference. This lecture covers the evolution from S4 to Mamba-3 and their implications for long-horizon reasoning.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **State Space Model (SSM)** | Sequence model based on continuous-time dynamics, discretized for neural networks |
| **Mamba** | Selective state space model with content-aware reasoning (2023) |
| **S4** | Structured State Space — foundational SSM work (Gu et al., 2021) |
| **Selective SSM** | SSM with input-dependent state transitions (key Mamba innovation) |
| **Linear attention** | Attention approximation with O(n) complexity |
| **Hardware-aware algorithm** | Algorithm designed to exploit GPU memory hierarchy |

---

## Speaker

### Albert Gu

**Affiliation:** Carnegie Mellon University, co-creator of Mamba

**Background:** PhD at Stanford under Chris Ré, pioneering work on structured state spaces. Now at CMU continuing SSM research.

**Key contributions:**
- S4 (Structured State Spaces) — first practical SSM for long sequences
- Mamba — selective SSM with content-dependent reasoning
- Mamba-2 — 2-8X faster with algorithmic improvements
- Mamba-3 — latest iteration (2026)

---

## Papers

### 1. Mamba: Linear-Time Sequence Modeling with Selective State Spaces (2023)

**Contribution:** O(n) complexity alternative to attention's O(n²).

**Key insight:** Selective state spaces enable content-aware reasoning — the model can choose what to remember based on input content.

**Method:** Input-dependent state transition matrices + hardware-efficient scan algorithm.

🔗 [arXiv](https://arxiv.org/abs/2312.00752) • [GitHub](https://github.com/state-spaces/mamba)

---

### 2. Transformers are SSMs: Generalized Models and Efficient Algorithms (ICML 2024)

**Contribution:** Shows mathematical equivalence between transformers and state space models.

**Key insight:** Many attention variants can be reformulated as SSMs, enabling cross-pollination of techniques.

**Result:** Mamba-2 is 2-8X faster than Mamba-1 with better quality.

🔗 [arXiv](https://arxiv.org/abs/2405.21060)

---

### 3. Mamba-3: Improved Sequence Modeling using State Space Principles (2026)

**Contribution:** Latest iteration with further improvements in quality and efficiency.

**Key changes:** (Check paper for specifics — recent release)

🔗 [arXiv](https://arxiv.org/abs/2603.15569)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Long-horizon memory** | 100K+ context windows enable multi-session recall — critical for persistent autonomy |
| **Efficient inference** | Linear scaling makes edge deployment feasible on constrained hardware |
| **Real-time processing** | No KV-cache explosion — sustained performance over long missions |
| **Alternative to attention** | Could be crucial for long-term autonomy tasks where transformer context limits bite |
| **Streaming inference** | Natural fit for continuous sensor streams |

---

## Question Bank

### Technical Questions

1. How does selective SSM compare to linear attention variants like Performer or Linformer in practice?
2. What's the memory/quality tradeoff when reducing state dimension?
3. How does Mamba handle structured vs unstructured data (code vs natural language)?
4. Are there tasks where Mamba underperforms transformers significantly?
5. How does Mamba-3 improve over Mamba-2 specifically?

### Robotics/Autonomy Questions

6. Have you tested Mamba on multimodal sensor fusion (vision + proprioception + language)?
7. How might SSMs handle irregularly-sampled sensor data (common in robotics)?
8. Is there work on action-conditioned SSMs for control?
9. How does Mamba compare to transformers for offline RL / behavior cloning?
10. What's the minimum hardware to run Mamba-3 efficiently? Edge deployment story?

### Research Direction Questions

11. Is the transformer-SSM equivalence practical for model conversion, or mostly theoretical?
12. What's the path to 1M+ context windows? Are there fundamental limits?

---

## Pre-Lecture Reading

### Essential (15-20 min)
- [Mamba GitHub](https://github.com/state-spaces/mamba) — code and examples
- [Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/) — technical deep dive

### Background (30-45 min)
- [Mamba paper](https://arxiv.org/abs/2312.00752) — foundational work
- [Mamba Wikipedia](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)) — quick overview

### Related Work
- [S4 paper](https://arxiv.org/abs/2111.00396) — Albert's earlier SSM work
- [Hungry Hungry Hippos](https://arxiv.org/abs/2212.14052) — SSM for language modeling
- [RWKV](https://arxiv.org/abs/2305.13048) — alternative RNN-based approach

---

## Cross-References

- **Week 2 (JEPA)** — World models for planning (complementary to long-context)
- **Week 10 (Modal/GPU)** — Deployment infrastructure for efficient inference

---

*Prepared: 2026-04-04*
