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

#### Key Papers

**C-JEPA: Learning World Models through Object-Level Latent Interventions** (ICLR 2026)
- **Contribution:** Extends masked joint embedding prediction from image patches to object-centric representations
- **Key insight:** World models require interaction-dependent dynamics, not just object detection
- **Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero
- [Project Page](https://hazel-heejeong-nam.github.io/cjepa/)

**LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels** (arXiv 2026)
- **Contribution:** Addresses training stability in JEPA architectures
- [GitHub](https://github.com/lucas-maes/le-wm)

#### Why It Matters for Autonomy

- **World models for robotics:** JEPA learns by predicting in latent space, not pixel space — more sample-efficient
- **Object-centric representations:** Could enable better scene understanding for embodied agents
- **Yann LeCun's favored approach:** Alternative to autoregressive/predictive models

#### Pre-Lecture Reading

- [C-JEPA project page](https://hazel-heejeong-nam.github.io/cjepa/)
- [LeWorldModel GitHub](https://github.com/lucas-maes/le-wm)
- [V-JEPA 2 (Meta)](https://openreview.net/pdf?id=tjimrqc2BU)

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
