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

## Talk Description

*From the course page:* World models are increasingly moving away from reconstruction and toward prediction in latent space. This talk presents two recent JEPA-based approaches that illustrate this shift from complementary angles.

**Causal-JEPA** induces object-level relational bias to promote representations that capture entities *and interactions*, leading to stronger reasoning and more efficient planning. **LeWorldModel** shows that such predictive world models can also be trained stably end-to-end from raw pixels using a minimal objective and a clean architectural recipe, while remaining competitive on control tasks.

**Unified thesis:** Predictive latent learning becomes most powerful when combined with both **structural bias** and **architectural simplicity**. This suggests a promising path toward robust world models that support abstraction, reasoning, and control.

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
- **Affiliation:** Brown University, working on representation learning, causality, and self-supervised learning
- **Focus:** World models, self-supervised learning, object-centric representations
- **Key contribution:** C-JEPA — extending JEPA to object-level reasoning via latent interventions

### Lucas Maes
- **Affiliation:** Mila and University of Montreal, PhD student
- **Focus:** JEPA and planning, training stability in JEPA architectures
- **Key contribution:** LeWorldModel — stable end-to-end training from pixels

**Connection:** Both work with Yann LeCun on advancing the JEPA framework toward autonomous machine intelligence.

---

## Technical Deep Dive

### C-JEPA — Object-Level Latent Interventions

**Key innovation:** C-JEPA treats object masking as a *structured latent intervention* — forces the model to infer masked objects from their interactions with other objects. This prevents "shortcut solutions" where the model relies on low-level visual features rather than reasoning about relationships.

**Method:** Applies object-level masking throughout the history window (except for a minimal identity anchor). The model must use interactions with other entities to minimize prediction error.

**Results:**
- **20% absolute improvement** in counterfactual reasoning vs same architecture without object-level masking
- **Only 1% of latent features** vs patch-based world models → **8× faster planning**
- Formal analysis: object-level masking induces causal inductive bias via latent interventions

**Paper:** [C-JEPA on arXiv](https://arxiv.org/abs/2602.11389) | [Project Page](https://hazel-heejeong-nam.github.io/cjepa/)

---

### LeWorldModel — SIGReg for Stable End-to-End Training

**The core problem:** JEPA tends toward representation collapse without careful loss balancing. Existing methods rely on complex multi-term losses, exponential moving averages, pre-trained encoders, or auxiliary supervision.

**LeWorldModel's solution:** Only **two loss terms**:
1. Next-embedding prediction loss
2. SIGReg — regularizer enforcing Gaussian-distributed latent embeddings

**Result:** Reduces loss hyperparameters from 6 to 1 vs other end-to-end approaches. Trainable on a single GPU (~15M params) in a few hours.

**Performance:** Plans **48× faster** than foundation-model-based world models while remaining competitive across 2D and 3D control tasks. The latent space also encodes meaningful physical structure.

**Paper:** [LeWorldModel on arXiv](https://arxiv.org/abs/2603.19312) | [GitHub](https://github.com/lucas-maes/le-wm)

---

## Unified Thesis

**"Predictive latent learning becomes most powerful when combined with both structural bias and architectural simplicity"**

| Component | C-JEPA | LeWorldModel |
|-----------|--------|--------------|
| **Structural bias** | Object-level masking (causal/relational) | None — purely end-to-end |
| **Architectural simplicity** | Joint embedding + predictor | Only 2 loss terms, no EMA, no pre-trained encoder |
| **Result** | Interaction reasoning, efficient planning | Stable training, 48× faster inference |

Both works argue: neither structural bias alone nor architectural simplicity alone is sufficient — you need both for robust world models.

---

## Papers

### 1. C-JEPA: Learning World Models through Object-Level Latent Interventions (ICLR 2026)

**Contribution:** Extends masked joint embedding prediction from image patches to object-centric representations.

**Key insight:** World models require interaction-dependent dynamics, not just object detection. Objects matter because of how they *interact*, not just because they exist.

**Method:** Uses object-level masking and interventions to learn causal structure in scenes.

**Authors:** Heejeong Nam, Quentin Le Lidec*, Lucas Maes*, Yann LeCun, Randall Balestriero
(* equal contribution)

🔗 [Project Page](https://hazel-heejeong-nam.github.io/cjepa/) | [arXiv](https://arxiv.org/abs/2602.11389)

---

### 2. LeWorldModel: Stable End-to-End JEPA from Pixels (arXiv 2026)

**Contribution:** First JEPA that trains stably end-to-end from raw pixels using only two loss terms.

**Key insight:** SIGReg (Gaussian regularizer) prevents collapse — that's the key trick. Reduces loss hyperparameters from 6 to 1.

**Authors:** Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, Randall Balestriero

🔗 [GitHub](https://github.com/lucas-maes/le-wm) | [arXiv](https://arxiv.org/abs/2603.19312)

---

### 3. A Path Towards Autonomous Machine Intelligence (LeCun, 2022)

**Why read:** The original JEPA proposal and vision for autonomous systems.

**Key insight:** Proposes JEPA as the core architecture for world models that enable planning and reasoning without explicit supervision.

🔗 [OpenReview](https://openreview.net/pdf?id=BZ5a1r-kVsf)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Abstraction** | SIGReg enforces compact, Gaussian-distributed latent representations — good for generalization |
| **Reasoning** | C-JEPA's counterfactual-like interventions enable interaction reasoning — robots need to predict how objects affect each other |
| **Control** | LeWorldModel achieves competitive control at 48× faster inference — practical for real-time robotics |
| **Sample efficiency** | Predicting in latent space requires less data than pixel reconstruction — crucial for real-world robot learning |
| **Efficient planning** | C-JEPA uses only 1% of latent features vs patch-based → 8× faster planning, essential for online control |
| **Structural bias** | Object-level causal inductive bias helps robots learn physical intuitions without supervision |
| **LeCun's thesis** | JEPA is central to the proposed path to autonomous machine intelligence |

---

## Question Bank

### Technical Questions

1. How does C-JEPA's object discovery mechanism compare to Slot Attention or other object-centric methods?
2. What causes training instability in JEPA, and how does LeWorldModel's SIGReg specifically address it?
3. The unified thesis says you need both structural bias *and* architectural simplicity. Is there a spectrum here — can you trade one for the other?
4. How do you balance the encoder and predictor capacities? Is there a risk of the predictor being too weak or too strong?
5. Can C-JEPA generalize to novel objects not seen during training, or does it overfit to training categories?

### Robotics/Autonomy Questions

6. Have you tested C-JEPA representations for planning or control tasks? What domains?
7. How might JEPA-style world models scale to high-DOF manipulation or navigation?
8. Is there a natural way to incorporate action conditioning into the prediction framework?
9. How does JEPA compare to diffusion-based world models (like those used in robot planning) in terms of sample efficiency?
10. What's the path from learned representations to actionable plans for embodied agents?

### Research Direction Questions

11. The unified thesis argues that "predictive latent learning + structural bias + architectural simplicity" is the winning combination. How does this compare to diffusion-based world models that rely on reconstruction?
12. How closely does this work align with Yann LeCun's full autonomous machine intelligence vision?
13. Are there plans to combine C-JEPA object-centric representations with V-JEPA temporal modeling?
14. LeWorldModel encodes "meaningful physical structure" in its latent space. Does this generalize to complex physics (fluids, deformable objects)?

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

*Prepared: 2026-04-04 | Updated: 2026-04-09 with expanded description and technical deep dive*
