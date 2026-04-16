---
title: "Pre-Read: State Space Models & Tradeoffs"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: State Space Models & Tradeoffs

**Date:** April 16, 2026
**Speaker:** Albert Gu (CMU / Cartesia AI)

---

## Talk Overview

> "This talk will provide a high level overview of a recently popular subquadratic alternative to the Transformer, the state space model (SSM). We will discuss the core characteristics and design choices of SSMs and other related modern linear models, and focus on the fundamental tradeoffs between SSMs and Transformers both from a modeling perspective and their strengths and weaknesses on different application areas. A central theme is that different architectures have very different performance characteristics depending on the resolution of the data and its tokenization scheme; we will also talk about recent progress on tokenizer-free models such as H-Nets."
>
> — Course site, CS25 Spring 2026

**Key themes:**
- SSMs vs Transformers: when does each win? (hint: depends heavily on tokenization and data resolution)
- Subquadratic alternatives: linear attention, gated convolutions, SSMs
- The **selective state** breakthrough: content-based reasoning in SSMs
- **Tokenizer-free models (H-Nets)**: emerging alternative to discretized token inputs
- **Mamba-3**: inference-first improvements — expressive recurrence, complex-valued state, MIMO formulation

---

## Key Concepts

| Term | Definition |
|------|------------|
| **SSM** | State Space Model — continuous-time dynamics discretized for neural networks |
| **Selective SSM** | SSM with input-dependent state transitions (Mamba's key innovation) |
| **S4** | Structured State Space — foundational SSM (Gu et al., 2021) |
| **SSD (State Space Duality)** | Mathematical framework showing SSMs ↔ attention equivalence via structured semiseparable matrices |
| **Mamba** | Selective SSM with content-aware reasoning (2023) |
| **H-Nets** | tokenizer-free models — tokenization-free alternative to standard LM inputs |
| **Linear attention** | Attention approximation with O(n) complexity |
| **Hardware-aware scan** | Algorithm exploiting GPU memory hierarchy for efficient SSM computation |
| **MIMO-SSM** | Multi-input multi-output SSM formulation — parallelize multiple streams without decode latency |

---

## Speaker

### Albert Gu

**Affiliations:**
- Assistant Professor, Machine Learning Dept., Carnegie Mellon University
- Chief Scientist, **Cartesia AI** (commercializing SSM technology)

**Recognition:** TIME AI100 — most influential AI researchers (2024)

**Background:** PhD at Stanford under Chris Ré. Research spans theoretical and empirical foundations of deep sequence modeling. Created S4 → Mamba → Mamba-2 → Mamba-3 lineage.

**Key contributions:**
- **S4** — first practical SSM for long sequences (2021)
- **Mamba** — selective SSM, 5× throughput vs Transformers, linear scaling (2023)
- **Mamba-2** — SSD framework, proves SSM-attention equivalence, 2-8× faster (ICML 2024)
- **Mamba-3** — inference-first design, complex-valued state, MIMO (2026)

---

## Papers

### 1. Mamba: Linear-Time Sequence Modeling with Selective State Spaces
**arXiv: [2312.00752](https://arxiv.org/abs/2312.00752)** | [GitHub](https://github.com/state-spaces/mamba)

**What it does:** Replaces attention with a selective state space model. SSM parameters become functions of the input — the model can selectively propagate or forget information based on content.

**Key results:**
- 5× higher throughput than Transformers during inference
- Linear scaling in sequence length (vs quadratic for attention)
- Improves on real data up to **million-length sequences**
- Mamba-3B matches Transformers 2× its size on language modeling

**Why it matters for autonomy:** KV-cache-free inference means constant memory over arbitrarily long contexts — huge for robot memory across missions.

---

### 2. Mamba-2: Generalized Models and Efficient Algorithms Through Structured State Space Duality
**arXiv: [2405.21060](https://arxiv.org/abs/2405.21060)** | ICML 2024

**What it does:** Proves that attention variants and SSMs are both decompositions of structured semiseparable matrices — a unified theoretical framework (SSD). This cross-pollination enables techniques from both worlds.

**Key results:**
- Mamba-2 is **2-8× faster** than Mamba-1
- Maintains competitive language modeling quality
- Core layer is a refinement of Mamba's selective SSM

**Why it matters:** The SSM-Transformer equivalence means we can mix and match techniques from both architectures.

---

### 3. Mamba-3
**arXiv: [2603.15569](https://arxiv.org/abs/2603.15569)**

**What it does:** "Inference-first" redesign. Current linear models trade off model quality (especially state tracking) for algorithmic efficiency and remain hardware-inefficient in practice. Mamba-3 addresses all three with three core improvements:

1. **More expressive recurrence** derived from SSM discretization
2. **Complex-valued state update** for richer state tracking (crucial for multi-entity reasoning)
3. **MIMO formulation** — better performance without increasing decode latency (handles multiple input streams in parallel)

**Key tension explored:** Linear-complexity models that actually match Transformer quality. State tracking (where Transformers excel) is the testbed.

**Why it matters for autonomy:** Complex-valued state could be critical for tracking multiple entities in the world simultaneously — a core robotics problem.

---

## Why It Matters for Autonomy

| SSM Property | Autonomy Relevance |
|---|---|
| **O(n) inference, no KV cache explosion** | Sustained performance over 1M+ token missions without memory degradation |
| **100K+ context windows** | Multi-session memory — robot recalls prior missions without retraining |
| **Streaming sensor fit** | Continuous sensor streams (LiDAR, IMU, cameras) map naturally to SSM's continuous-time formulation |
| **Linear scaling** | Edge deployment on constrained hardware (Jetson, robot compute) |
| **Complex-valued state (Mamba-3)** | Better multi-entity tracking — robots must track many moving objects |
| **MIMO formulation** | Handle multiple sensor modalities simultaneously without added decode latency |

---

## Pre-Lecture Reading

### Essential (~20 min)
- **[Mamba GitHub](https://github.com/state-spaces/mamba)** — code, pretrained models, examples
- **[Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/)** (Goomba Lab) — technical deep dive on SSD framework

### Paper Abstracts (~15 min)
- [Mamba paper abstract](https://arxiv.org/abs/2312.00752) — understand the core selection mechanism
- [Mamba-2 paper abstract](https://arxiv.org/abs/2405.21060) — understand SSD duality
- [Mamba-3 paper abstract](https://arxiv.org/abs/2603.15569) — understand inference-first improvements

### Background (~30 min)
- [S4 paper](https://arxiv.org/abs/2111.00396) — the SSM foundation
- [Hungry Hungry Hippos](https://arxiv.org/abs/2212.14052) — SSM at scale for language

---

## Question Bank

### Technical
1. You say the tokenization scheme affects which architecture wins — can you quantify that? Is there a theory?
2. What's the actual hardware efficiency of "linear-time" SSMs vs optimized attention on modern GPUs?
3. Mamba-3 uses complex-valued states for state tracking. What's the intuition — why does complex help?
4. The MIMO formulation — does this mean Mamba-3 can process multiple sequences in parallel with zero overhead?
5. Where do SSMs clearly lose to Transformers on practical tasks?

### Autonomy-Specific
6. Have you tested Mamba on multimodal sensor fusion — vision + proprioception + language in a single model?
7. How do SSMs handle the irregularly-sampled, heterogeneous sensor streams typical in robotics?
8. What's the smallest efficient Mamba deployment on edge hardware? (Jetson Orin, etc.)
9. For offline RL and behavior cloning — does Mamba's compression vs Transformers' full context hurt or help?
10. Is there work on action-conditioned SSMs for receding-horizon control?

### Research Directions
11. H-Nets (tokenizer-free) — what's the actual story? Is tokenization a fundamental bottleneck for SSM quality?
12. The SSM-Transformer equivalence — practically, can we convert a trained Transformer to Mamba and back?
13. What's beyond Mamba-3? Is there a theoretical ceiling on SSM expressivity?

---

## Cross-References

- **Week 2 (JEPA)** — World models for planning; JEPA also predicts in latent space, complementary to SSM long-context
- **Week 4 (Ultra-Scale)** — Training large SSMs; how does MoE interact with SSM architecture?
- **Week 10 (Modal/GPU)** — Edge deployment of large models; SSM inference efficiency fits naturally here

---

*Pre-read updated: 2026-04-16 (critical review against course site and arXiv abstracts)*
