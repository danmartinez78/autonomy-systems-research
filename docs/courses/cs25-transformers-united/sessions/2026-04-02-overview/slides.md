---
title: "Slides: Overview of Transformers"
layout: default
parent: Session 1: Overview of Transformers
grand_parent: CS25: Transformers United V6
nav_order: 1
permalink: /courses/cs25-transformers-united/sessions/2026-04-02-overview/slides/
---

# Slides: Overview of Transformers

**Source:** [Google Drive PDF](https://drive.google.com/file/d/153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB/view)

---

## Key Insights Extracted

### 1. Transformer Architecture Core Components
- **Self-attention mechanism** — Enables processing relationships between all positions in a sequence simultaneously
- **Position encoding** — Provides sequential order information since attention is position-invariant
- **Feed-forward layers** — Non-linear transformations applied after attention
- **Layer normalization** — Stabilizes training, enables deeper networks

### 2. Evolution Timeline

| Era | Years | Key Developments |
|-----|-------|-----------------|
| Pre-Transformer | 2012-2017 | RNNs, LSTMs, Word2Vec, CNNs for text |
| Early Transformers | 2018-2019 | BERT, GPT-1, T5, RoBERTa |
| Scale Era | 2020-2022 | GPT-3, PaLM, Chinchilla scaling laws |
| Foundation Models | 2022+ | ChatGPT, GPT-4, LLaMA, multimodal |
| Reasoning | 2025+ | o1, DeepSeek R1, chain-of-thought |
| Efficiency | 2026+ | Mamba (SSMs), Flash Attention, linear attention |

### 3. Impact on Robotics/Autonomy

| Area | Application | Challenge |
|------|-------------|-----------|
| World Models | Predictive models for decision-making | Training data, sim-to-real gap |
| Embodied AI | VLMs for perception + control | Real-time inference constraints |
| Long-horizon Planning | Extended context for multi-step reasoning | Memory, efficiency |
| Edge Deployment | Smaller models for onboard compute | Performance vs capability tradeoff |

### 4. Current Challenges
- **Interpretability** — Black-box nature hinders trust
- **Hallucination** — Confident but incorrect outputs
- **Alignment** — Matching human intent
- **Compute cost** — Environmental + economic concerns
- **Robustness** — Distribution shift, adversarial inputs

### 5. Open Research Directions
- **Multimodality** — Vision + language + audio integration
- **Tool use** — Function calling, API integration
- **Personalization** — Domain-specific fine-tuning
- **Mixture of Experts** — Specialized model ensembles

---

## Speaker Citations
*From slide deck — to be cross-referenced with speaker research*

- Vaswani et al. (2017) — "Attention Is All You Need"
- Devlin et al. (2018) — BERT
- Radford et al. (2019) — Language Models are Unsupervised Multitask Learners
- Brown et al. (2020) — Language Models are Few-Shot Learners (GPT-3)

---

*Extracted: 2026-04-04*
