---
title: "Session 1: Overview of Transformers"
layout: default
parent: CS25: Transformers United V6
nav_order: 1
permalink: /courses/cs25-transformers-united/sessions/2026-04-02-overview//
date: 2026-04-02
---

# Session 1: Overview of Transformers

**Video:** Not yet confirmed on the official YouTube playlist or recordings page

**Status:** ⚠️ Slide insights only — awaiting lecture video for complete synthesis

---

## Session Overview

Brief intro and overview of the history of ML/NLP, Transformers and how they work, and their impact on robotics, autonomy, and embodied AI. Discussion about recent trends, breakthroughs, applications, and current challenges/weaknesses.

[View the full slide deck](https://drive.google.com/file/d/153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB/view?usp=sharing){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

---

## Key Insights from Slides
*(Extracted manually from Week 1 Overview slides - 2026-04-02)*

### 1. Transformers Architecture: The Core components
- **Self-attention mechanism** — Enables processing of relationships between words in sequences
- **Position encoding** — Provides information about token position in the sequence
- **Feed-forward layers** — Allow the model to consider information from previous positions when making predictions
- **Layer normalization** — Stabilizes training, enables faster convergence

### 2. Evolution of NLP/ML
**Timeline of Transformers impact:**
| Year | Era | Key Developments |
|------|-----|-----------------|
| 2017 | Pre-Transformer | RNNs, LSTMs, Word2Vec, CNNs for text |
| 2018 | Early Transformers | BERT, GPT-1, T5 | ULM (ULMFiT), Encoder-only |
| 2019- Architecture refinements | XLNet, RoBERTa, DistilBERT |
| 2020- GPT-3 era | In-context learning, prompt engineering, larger models |
| 2021+ | Vision Transformers (ViT, Swin, CLIP) | Scale laws and self-attention for vision |
| 2022+ | Foundation models | ChatGPT, GPT-4 | LLaMA, PaLM | Chinchilla |
| 2023+ | Scaling breakthroughs | GPT-4, Llama 2 | Mixtral of Mixture of Experts |
| 2024+ | Efficiency improvements | Sparse attention, Flash Attention, Linear attention variants |
| 2025+ | Reasoning models | o1, Chain-of-Thought, DeepSeek R1, Claude |
| 2026+ | State Space Models | **Mamba** — Linear-time O(n) complexity for long sequences |
| **SSMs (State Space Models)** — Alternative to attention for long-context tasks. See Week 3 (Albert Gu) for details.

### 3. Impact on Robotics/Autonomy
- **World models** — Transformers enable learning predictive models for robot decision-making
- **Embodied AI** — Vision-language models (VLMs) for robot perception and control
- **Long-horizon planning** — Extended context windows enable multi-step reasoning
- **Efficiency for Edge deployment** — Smaller, quantized models for real-time control on robots
- **Safety-critical applications** — Medical AI (Med-PaLM) demonstrates validation patterns for high-stakes domains
- **Sim-to-real transfer** — Challenges in transferring simulation success to real-world deployment
- **Interpretability** — Understanding how models make decisions is crucial for trustworthy autonomy
- **Catastrophic forgetting** — Models can lose information over long sequences
- **Sample efficiency** — Training requires massive datasets
- **Computational cost** — Inference can be expensive without optimization
- **Robustness** — Distribution shifts, adversarial inputs can cause unpredictable behavior

### 4. Current Trends
- **Multimodality** — Vision, language, audio integration
- **Tool use** — Function calling, API integration
- **Personalization** — Fine-tuning for specific domains
- **Mixture of Experts** — Combining specialized models

### 5. Open Challenges
- **Interpretability** — Black-box nature makes understanding difficult
- **Hallucination** — Models can generate confident but incorrect outputs
- **Alignment** — Ensuring model behavior matches human intent
- **Compute sustainability** — Environmental cost of training and deployment
- **Regulation** — Governance frameworks for autonomous systems

---

## Reference Links
- **Course Site:** [CS25: Transformers United](https://web.stanford.edu/class/cs25/)
- **Slides:** [Week 1 Overview (PDF)](https://drive.google.com/file/d/153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB/view?usp=sharing)
- **YouTube Playlist:** [CS25 V6 Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM)
- **Related Reading:** [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — foundational paper

---

## Next Steps
- [ ] Watch Week 1 lecture on YouTube once posted
- [ ] Fill in Key Takeaways section with detailed notes
- [ ] Complete Open Questions section with questions for the speakers
- [ ] Add connections to autonomy research section

---

## Awaiting Video

Current check status: no direct Week 1 video confirmed yet on the official playlist or recordings page.

The following sections will be populated once the lecture video is posted:

- **Transcript highlights** — Key moments with timestamps
- **Answers to pre-read questions** — Which questions from the [Pre-Read](pre-read) were addressed?
- **Additional papers mentioned** — Any papers referenced in lecture not in pre-read
- **Speaker insights** — Perspectives shared verbally vs. slides

---

## Related Sessions
- **Week 2: JEPA** — Hazel Nam & Lucas Maes (Brown University) — world models for robotics
- **Week 3: SSMs** — Albert Gu (CMU) — Mamba creator, efficient long-context alternatives
- **Week 6: Interpretability** — Andrew Lampinen (Anthropic) — understanding transformer reasoning
- **Week 7: Med-PaLM** — Vivek Natarajan (DeepMind) — safety-critical deployment patterns

---

*Last updated: 2026-04-04*
