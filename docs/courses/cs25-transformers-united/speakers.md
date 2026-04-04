---
title: "Speaker Research Notes"
layout: default
parent: CS25: Transformers United V6
nav_order: 2
permalink: /courses/cs25-transformers-united/speakers/
---

# Speaker Research Notes

Pre-lecture research on each speaker, their key papers, and relevance to autonomy research.

---

## Week 2 (April 9): JEPA

### Speakers: Hazel Nam & Lucas Maes (Brown University)

**Affiliations:** Brown University, Mila, NYU (collaboration with Yann LeCun)

**Background:** Hazel Nam (Heejeong Nam) and Lucas Maes are PhD researchers working on world models and self-supervised learning. Their work extends Yann LeCun's JEPA (Joint Embedding Predictive Architecture) framework, which proposes learning by predicting in latent representation space rather than reconstructing pixels.

#### Key Papers

**C-JEPA: Learning World Models through Object-Level Latent Interventions** (ICLR 2026)
- **Contribution:** Extends masked joint embedding prediction from image patches to object-centric representations
- **Key insight:** World models require interaction-dependent dynamics, not just object detection
- **Method:** Uses object-level masking and interventions to learn causal structure in scenes
- **Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero
- [Project Page](https://hazel-heejeong-nam.github.io/cjepa/)

**LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels** (arXiv 2026)
- **Contribution:** Addresses training stability in JEPA architectures — a key practical challenge
- **Key insight:** Proposes techniques to prevent collapse and improve convergence
- [GitHub](https://github.com/lucas-maes/le-wm)

#### JEPA Context (Why This Architecture Matters)

Yann LeCun's "A Path Towards Autonomous Machine Intelligence" (2022) proposed JEPA as an alternative to:
- Generative models (VAEs, diffusion) that predict in pixel space
- Autoregressive models that predict next tokens
- Contrastive methods that require negative samples

**JEPA's core idea:** Learn representations by predicting *latent* embeddings of missing/occluded parts, not their pixels. This is more sample-efficient and learns abstract structure rather than low-level details.

**Variants:**
- **I-JEPA** (Image JEPA): Meta, 2023 — non-generative, non-contrastive
- **V-JEPA** (Video JEPA): Meta, 2024 — learns from video without pixel reconstruction
- **C-JEPA** (Causal/Object-centric): Nam, Maes et al., 2026 — adds object-level reasoning

#### Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Sample efficiency** | Predicting in latent space requires less data than pixel reconstruction — crucial for real-world robot learning |
| **Object-centric representations** | Robots need to reason about objects, not pixels; C-JEPA learns this automatically |
| **World models** | JEPA-style prediction could enable planning in learned representation spaces |
| **Causal reasoning** | Object-level interventions may enable learning cause-effect relationships |
| **No reconstruction** | Avoids wasting capacity on irrelevant visual details |
| **Yann LeCun's thesis** | JEPA is central to his proposed path to autonomous machine intelligence |

#### Relevance to Current Trends

- **Embodied AI:** JEPA-style world models are a leading candidate for robot planning/reasoning
- **Video understanding:** V-JEPA (Meta) shows strong results on video benchmarks without pixel prediction
- **Alternative to LLMs:** Non-autoregressive approach to sequence modeling
- **Sample efficiency:** Could reduce data requirements for robot learning by orders of magnitude

#### Question Bank for Lecture

**Technical Questions:**
1. How does C-JEPA's object discovery mechanism compare to Slot Attention or other object-centric methods?
2. What causes training instability in JEPA, and how does LeWorldModel specifically address it?
3. How do you balance the encoder and predictor capacities? Is there a risk of the predictor being too weak or too strong?
4. Can C-JEPA generalize to novel objects not seen during training, or does it overfit to training categories?
5. How does prediction error in latent space correlate with downstream task performance?

**Robotics/Autonomy Questions:**
6. Have you tested C-JEPA representations for planning or control tasks? What domains?
7. How might JEPA-style world models scale to high-DOF manipulation or navigation?
8. Is there a natural way to incorporate action conditioning into the prediction framework?
9. How does JEPA compare to diffusion-based world models (like those used in robot planning) in terms of sample efficiency?
10. What's the path from learned representations to actionable plans for embodied agents?

**Collaboration/Research Direction Questions:**
11. How closely does this work align with Yann LeCun's full autonomous machine intelligence vision?
12. Are there plans to combine C-JEPA object-centric representations with V-JEPA temporal modeling?

#### Pre-Lecture Reading

**Essential:**
- [C-JEPA project page](https://hazel-heejeong-nam.github.io/cjepa/) — includes paper, code, visualizations
- [LeWorldModel GitHub](https://github.com/lucas-maes/le-wm) — implementation and experiments

**Background:**
- [Yann LeCun's "A Path Towards Autonomous Machine Intelligence"](https://openreview.net/pdf?id=BZ5a1r-kVsf) — the original JEPA proposal
- [I-JEPA (Meta)](https://arxiv.org/abs/2301.08243) — foundational image JEPA work
- [V-JEPA (Meta)](https://openreview.net/pdf?id=tjimrqc2BU) — video extension

**Related Work:**
- [Slot Attention](https://arxiv.org/abs/2006.15085) — alternative object-centric learning
- [World Models (Ha & Schmidhuber)](https://arxiv.org/abs/1803.10122) — classic approach to learning world models
- [Dreamer (Danijar Hafner)](https://danijar.com/project/dreamerv3/) — latent dynamics for RL

#### Cross-References

- See also: **Week 3 (SSMs/Mamba)** — alternative architecture for long-horizon reasoning
- See also: **Week 7 (Med-PaLM)** — safety-critical validation patterns applicable to world model deployment

---

## Week 3 (April 16): SSMs

### Speaker: Albert Gu (CMU)

**Affiliation:** Carnegie Mellon University, co-creator of Mamba

#### Key Papers

**Mamba: Linear-Time Sequence Modeling with Selective State Spaces** (2023)
- **Contribution:** O(n) complexity alternative to attention's O(n²)
- **Key insight:** Selective state spaces enable content-aware reasoning
- [arXiv](https://arxiv.org/abs/2312.00752) • [GitHub](https://github.com/state-spaces/mamba)

**Transformers are SSMs: Generalized Models and Efficient Algorithms** (ICML 2024)
- **Contribution:** Shows equivalence between transformers and state space models
- **Key insight:** Mamba-2 is 2-8X faster than Mamba-1
- [arXiv](https://arxiv.org/abs/2405.21060)

**Mamba-3: Improved Sequence Modeling using State Space Principles** (2026)
- Latest iteration with further improvements
- [arXiv](https://arxiv.org/abs/2603.15569)

#### Why It Matters for Autonomy

- **Long-horizon memory:** 100K+ context windows enable multi-session recall
- **Efficient inference:** Linear scaling makes edge deployment feasible
- **Alternative to attention:** Could be crucial for long-term autonomy tasks

#### Pre-Lecture Reading

- [Mamba GitHub](https://github.com/state-spaces/mamba)
- [Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/)
- [Mamba Wikipedia](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture))

---

## Week 4 (April 23): TBD

### Speaker: Nouamane Tazi (Hugging Face)

**Affiliation:** Hugging Face, BigCode contributor

#### Known For

**StarCoder 2** (BigCode, 2024)
- Open LLM for code generation
- [arXiv](https://arxiv.org/abs/2402.19173)

**SmolLM3** (Hugging Face, 2025)
- Small, multilingual, long-context reasoner
- [Blog](https://huggingface.co/blog/smollm3)

**Layer Normalization Research**
- Discovered tanh-like S-shaped curves in transformer input-output mappings

**GPU Memory Prediction for MoE Models**
- Practical infrastructure work for deployment

#### Why It Matters for Autonomy

- **Code assistants:** Directly relevant to coding agents
- **Small model efficiency:** Edge deployment patterns
- **GPU infrastructure:** Practical deployment knowledge

#### Pre-Lecture Reading

- [Nouamane's Hugging Face profile](https://huggingface.co/nouamanetazi)
- [SmolLM3 blog](https://huggingface.co/blog/smollm3)

---

## Week 6 (May 7): TBD

### Speaker: Andrew Lampinen (Anthropic)

**Affiliation:** Anthropic, formerly Google DeepMind

#### Research Focus

**Bridging Cognitive Science and AI**
- How complex behaviors/representations emerge from learning experiences
- Language (especially explanations) as a cognitive tool

**Puzzle Framework** (ICML 2025)
- Efficient transformer variants by block importance
- Created Nemotron-Super-49B and Nemotron-Ultra-253B
- [LinkedIn post](https://www.linkedin.com/posts/andrew-lampinen-926398a0/)

**Anthropic Interpretability Work**
- Attribution graphs for Claude 3.5 Haiku
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

#### Why It Matters for Autonomy

- **Interpretability:** Essential for trustworthy autonomous systems
- **Block importance:** Could inform efficient deployment for edge robotics
- **Cognitive science angle:** Understanding emergence of capabilities

#### Pre-Lecture Reading

- [Andrew's website](https://lampinen.github.io/)
- [Attribution graphs paper](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)

---

## Week 7 (May 14): TBD

### Speaker: Vivek Natarajan (DeepMind)

**Affiliation:** Google DeepMind, Research Lead for AI × Science × Medicine

#### Key Papers

**Med-PaLM** (Nature, 2023)
- First AI to pass US Medical License Exam
- [Nature paper](https://www.nature.com/articles/s41586-023-06291-2)

**Med-PaLM 2** (Nature Medicine, 2025)
- Expert-level scores on medical exams
- [Nature Medicine paper](https://www.nature.com/articles/s41591-024-03417-8)

**18,300+ citations** across AI/healthcare work

#### Why It Matters for Autonomy

- **Safety-critical deployment:** Medical AI is the gold standard for high-stakes domains
- **Validation patterns:** How to make transformers reliable in critical applications
- **Domain-specific fine-tuning:** Relevant to specialized autonomy applications

#### Pre-Lecture Reading

- [Google Research profile](https://research.google/people/106654/)
- [Med-PaLM paper](https://www.nature.com/articles/s41586-023-06291-2)

---

## Week 10 (May 28): TBD

### Speaker: Charles Frye (Modal)

**Affiliation:** Modal, AI Engineer

#### Research Focus

**Serverless GPU Infrastructure**
- Modal platform for running GenAI models without managing infrastructure
- [Modal docs](https://modal.com/docs)

**GPU Glossary**
- Educational content on GPU architecture
- [GPU Glossary](https://modal.com/gpu-glossary)

**CUDA Python & Distributed Inference**
- Year of CUDA Python (GTC 2025)
- Tensor memory accelerators

#### Why It Matters for Autonomy

- **Deployment infrastructure:** Serverless GPU for on-demand autonomy workloads
- **Practical ML systems:** Real-world deployment patterns
- **Cost efficiency:** Running inference without managing hardware

#### Pre-Lecture Reading

- [Modal GPU Glossary](https://modal.com/gpu-glossary)
- [Podcast: CUDA Python GTC 2025 recap](https://podcasts.apple.com/ky/podcast/034-the-year-of-cuda-python-nvidia-gtc-2025-recap/id1493295799?i=1000700913657)

---

## Priority Reading List

### For Embodied AI / Autonomy
1. C-JEPA (Week 2) — world models for robotics
2. Med-PaLM work (Week 7) — safety-critical deployment patterns

### For Efficiency / Deployment
1. Mamba / SSMs (Week 3) — long-context, efficient inference
2. Puzzle framework (Week 6) — efficient transformer variants
3. Modal (Week 10) — serverless GPU deployment

### For Interpretability / Trustworthiness
1. Anthropic attribution graphs (Week 6)
2. Med-PaLM validation approach (Week 7)

---

*Last updated: 2026-04-04*
