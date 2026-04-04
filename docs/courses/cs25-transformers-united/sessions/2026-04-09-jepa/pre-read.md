---
title: "Pre-Read: JEPA & World Models"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: JEPA & World Models

**Date:** April 9, 2026
**Speakers:** Hazel Nam & Lucas Maes (Brown University)

---

## Topic Overview

JEPA (Joint Embedding Predictive Architecture) is Yann LeCun's proposed alternative to generative and autoregressive models for learning world representations. Instead of predicting pixels or tokens, JEPA predicts in *latent embedding space* — learning abstract structure without reconstruction. This lecture covers C-JEPA (object-centric) and recent advances in stable training.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **JEPA** | Joint Embedding Predictive Architecture — learns by predicting latent representations, not pixels |
| **I-JEPA** | Image JEPA (Meta, 2023) — foundational work on non-generative, non-contrastive learning |
| **V-JEPA** | Video JEPA (Meta, 2024) — temporal extension without pixel reconstruction |
| **C-JEPA** | Causal/Object-centric JEPA (2026) — adds object-level reasoning and interventions |
| **Latent prediction** | Predicting embeddings rather than reconstructing observations |
| **Object-centric learning** | Learning representations that explicitly represent objects, not just features |
| **World model** | Learned model of environment dynamics for planning |

---

## Speakers

### Hazel Nam (Heejeong Nam)
- **Affiliation:** Brown University, Mila, NYU collaboration
- **Focus:** World models, self-supervised learning, object-centric representations
- **Key contribution:** C-JEPA — extending JEPA to object-level reasoning

### Lucas Maes
- **Affiliation:** Brown University
- **Focus:** Training stability in JEPA architectures
- **Key contribution:** LeWorldModel — techniques to prevent collapse and improve convergence

**Connection:** Both work with Yann LeCun on advancing the JEPA framework toward autonomous machine intelligence.

---

## Papers

### 1. C-JEPA: Learning World Models through Object-Level Latent Interventions (ICLR 2026)

**Contribution:** Extends masked joint embedding prediction from image patches to object-centric representations.

**Key insight:** World models require interaction-dependent dynamics, not just object detection. Objects matter because of how they *interact*, not just because they exist.

**Method:** Uses object-level masking and interventions to learn causal structure in scenes.

**Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero

🔗 [Project Page](https://hazel-heejeong-nam.github.io/cjepa/)

---

### 2. LeWorldModel: Stable End-to-End JEPA from Pixels (arXiv 2026)

**Contribution:** Addresses training stability in JEPA architectures — a key practical challenge.

**Key insight:** Proposes techniques to prevent collapse and improve convergence, making JEPA more practical for real-world use.

🔗 [GitHub](https://github.com/lucas-maes/le-wm)

---

### 3. A Path Towards Autonomous Machine Intelligence (LeCun, 2022)

**Why read:** The original JEPA proposal and vision for autonomous systems.

**Key insight:** Proposes JEPA as the core architecture for world models that enable planning and reasoning without explicit supervision.

🔗 [OpenReview](https://openreview.net/pdf?id=BZ5a1r-kVsf)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Sample efficiency** | Predicting in latent space requires less data than pixel reconstruction — crucial for real-world robot learning |
| **Object-centric representations** | Robots need to reason about objects, not pixels; C-JEPA learns this automatically |
| **World models** | JEPA-style prediction could enable planning in learned representation spaces |
| **Causal reasoning** | Object-level interventions may enable learning cause-effect relationships |
| **No reconstruction** | Avoids wasting capacity on irrelevant visual details |
| **LeCun's thesis** | JEPA is central to the proposed path to autonomous machine intelligence |

---

## Question Bank

### Technical Questions

1. How does C-JEPA's object discovery mechanism compare to Slot Attention or other object-centric methods?
2. What causes training instability in JEPA, and how does LeWorldModel specifically address it?
3. How do you balance the encoder and predictor capacities? Is there a risk of the predictor being too weak or too strong?
4. Can C-JEPA generalize to novel objects not seen during training, or does it overfit to training categories?
5. How does prediction error in latent space correlate with downstream task performance?

### Robotics/Autonomy Questions

6. Have you tested C-JEPA representations for planning or control tasks? What domains?
7. How might JEPA-style world models scale to high-DOF manipulation or navigation?
8. Is there a natural way to incorporate action conditioning into the prediction framework?
9. How does JEPA compare to diffusion-based world models (like those used in robot planning) in terms of sample efficiency?
10. What's the path from learned representations to actionable plans for embodied agents?

### Research Direction Questions

11. How closely does this work align with Yann LeCun's full autonomous machine intelligence vision?
12. Are there plans to combine C-JEPA object-centric representations with V-JEPA temporal modeling?

---

## Pre-Lecture Reading

### Essential (15-20 min)
- [C-JEPA project page](https://hazel-heejeong-nam.github.io/cjepa/) — paper, code, visualizations
- [LeWorldModel GitHub](https://github.com/lucas-maes/le-wm) — implementation

### Background (30-45 min)
- [Yann LeCun's "A Path Towards Autonomous Machine Intelligence"](https://openreview.net/pdf?id=BZ5a1r-kVsf) — original JEPA proposal
- [I-JEPA (Meta)](https://arxiv.org/abs/2301.08243) — foundational image JEPA work

### Related Work
- [Slot Attention](https://arxiv.org/abs/2006.15085) — alternative object-centric learning
- [World Models (Ha & Schmidhuber)](https://arxiv.org/abs/1803.10122) — classic approach
- [Dreamer (Danijar Hafner)](https://danijar.com/project/dreamerv3/) — latent dynamics for RL

---

## Cross-References

- **Week 3 (SSMs/Mamba)** — Alternative architecture for long-horizon reasoning
- **Week 7 (Med-PaLM)** — Safety-critical validation patterns applicable to world model deployment

---

*Prepared: 2026-04-04*
