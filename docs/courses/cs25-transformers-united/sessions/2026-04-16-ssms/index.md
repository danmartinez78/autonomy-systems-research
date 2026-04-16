---
title: "Session 3: State Space Models & Tradeoffs"
layout: default
parent: CS25: Transformers United V6
nav_order: 3
permalink: /courses/cs25-transformers-united/sessions/2026-04-16-ssms/
date: 2026-04-16
---

# Session 3: State Space Models & Tradeoffs

**Speaker:** Albert Gu (CMU / Cartesia AI)
**Status:** Awaiting lecture — talk is today (April 16, 2026)

---

## Talk Abstract

> "This talk will provide a high level overview of a recently popular subquadratic alternative to the Transformer, the state space model (SSM). We will discuss the core characteristics and design choices of SSMs and other related modern linear models, and focus on the fundamental tradeoffs between SSMs and Transformers both from a modeling perspective and their strengths and weaknesses on different application areas. A central theme is that different architectures have very different performance characteristics depending on the resolution of the data and its tokenization scheme; we will also talk about recent progress on tokenizer-free models such as H-Nets."

---

## Key Papers

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) (2023)
- [Mamba-2: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060) (ICML 2024)
- [Mamba-3](https://arxiv.org/abs/2603.15569) (2026)

---

## Slides

**Slides not yet posted** — Stanford typically posts slides 1-3 weeks after the lecture. Check the [course site](https://web.stanford.edu/class/cs25/) for updates.

---

## Session Notes

*[To be populated after video is posted — check back Thursday/Friday]*

---

## Pre-Read Questions

1. How does selective SSM compare to linear attention variants (Performer, Linformer) in practice?
2. What's the state dimension / memory / quality tradeoff in Mamba?
3. How does Mamba handle code vs natural language differently?
4. Where does Mamba significantly underperform transformers?
5. How does Mamba-3 improve over Mamba-2?
6. Have you tested SSMs on multimodal sensor fusion (vision + proprioception + language)?
7. How do SSMs handle irregularly-sampled sensor data common in robotics?
8. Is there work on action-conditioned SSMs for control?
9. How does Mamba compare to transformers for offline RL / behavior cloning?
10. What's the minimum hardware to run Mamba-3 efficiently?
11. Is the SSM-Transformer equivalence practical for model conversion?
12. What enables tokenizer-free models like H-Nets?
13. What's the path to 1M+ context windows?

---

## Relevant Autonomy Connections

- **Long-horizon memory:** 100K+ context windows critical for multi-session robot missions
- **Edge deployment:** Linear scaling enables robots with constrained compute
- **Streaming sensors:** SSM continuous-time formulation fits LiDAR/IMU/camera streams naturally
- **Complex-valued state (Mamba-3):** Better multi-entity world tracking — core robotics problem
- **Cartesia AI:** Real-world SSM deployment pressure beyond research

---

*Last updated: 2026-04-16 (pre-lecture)*
