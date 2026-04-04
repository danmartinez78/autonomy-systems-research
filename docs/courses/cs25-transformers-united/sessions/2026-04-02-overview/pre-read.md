---
title: "Pre-Read: Overview of Transformers"
layout: default
parent: Session 1: Overview of Transformers
grand_parent: CS25: Transformers United V6
nav_order: 2
permalink: /courses/cs25-transformers-united/sessions/2026-04-02-overview/pre-read/
---

# Pre-Read: Overview of Transformers

**Date:** April 2, 2026
**Speakers:** Course Instructors (Steven Feng, Karan Singh, Michael C. Frank, Christopher Manning)

---

## Topic Overview

The kickoff session provides a historical overview of transformers, core architectural components, and their explosive impact across NLP, vision, robotics, and multimodal AI. Expect a survey of the landscape rather than deep technical dives — this sets context for the rest of the course.

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Self-Attention** | Mechanism allowing each token to attend to all other tokens in a sequence, capturing relationships regardless of distance |
| **Position Encoding** | Injects positional information since attention is permutation-invariant |
| **Multi-Head Attention** | Parallel attention heads learning different relationship types |
| **Transformer Block** | Stack of attention + feed-forward + layer norm + residual connections |
| **Encoder-Decoder** | Original Transformer: encoder processes input, decoder generates output |
| **Encoder-only (BERT)** | Bidirectional understanding, good for classification/extraction |
| **Decoder-only (GPT)** | Autoregressive generation, good for text completion |
| **Foundation Model** | Large pretrained model adaptable to many downstream tasks |
| **Scaling Laws** | Predictable relationship between compute, data, model size, and performance |
| **Emergent Capabilities** | Abilities that appear suddenly at certain scale thresholds (e.g., in-context learning) |

---

## Speakers

### Christopher Manning
**Affiliation:** Stanford AI Lab Director, Professor of Computer Science and Linguistics

**Why he matters:** Pioneer of neural NLP, helped create CoreNLP, key figure in the deep learning NLP revolution. His textbook *Foundations of Statistical Natural Language Processing* is foundational.

**Recent focus:** Interpretability, efficient transformers, embodied AI + language

### Steven Feng
**Affiliation:** PhD Student, Stanford

**Research:** Multimodal AI, vision-language models

### Karan Singh
**Affiliation:** PhD Student, Stanford

**Research:** Efficient ML, long-context modeling

### Michael C. Frank
**Affiliation:** Professor of Psychology, Stanford

**Research:** Language acquisition, human-AI interaction, cognitive development

---

## Key Papers

### 1. Attention Is All You Need (2017)
**Authors:** Vaswani et al. (Google Brain)

**Why it matters:** The paper that started it all. Introduced the Transformer architecture, replacing RNNs/CNNs with pure attention.

**Key insight:** Self-attention enables parallel processing of sequences and captures long-range dependencies efficiently.

🔗 [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

---

### 2. BERT: Pre-training of Deep Bidirectional Transformers (2018)
**Authors:** Devlin et al. (Google AI Language)

**Why it matters:** Showed that bidirectional pretraining on massive unlabeled text creates powerful language representations.

**Key insight:** Masked language modeling + next sentence prediction create generalizable understanding.

🔗 [arXiv:1810.04805](https://arxiv.org/abs/1810.04805)

---

### 3. Language Models are Few-Shot Learners (GPT-3) (2020)
**Authors:** Brown et al. (OpenAI)

**Why it matters:** Demonstrated that scale enables in-context learning — models can perform tasks from examples without weight updates.

**Key insight:** Emergent capabilities appear at scale; 175B parameters was a turning point.

🔗 [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

---

### 4. An Image is worth 16x16 words: Transformers for Image Recognition at Scale (ViT) (2020)
**Authors:** Dosovitskiy et al. (Google Brain)

**Why it matters:** Proved transformers work for vision too, not just language.

**Key insight:** Patch-based tokenization + transformer = competitive with CNNs when scaled.

🔗 [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)

---

### 5. Scaling Laws for Neural Language Models (2020)
**Authors:** Kaplan et al. (OpenAI)

**Why it matters:** Established predictable relationships between compute, data, parameters, and performance.

**Key insight:** Power laws govern scaling — bigger is predictably better.

🔗 [arXiv:2001.08361](https://arxiv.org/abs/2001.08361)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Foundation models** | Pretrained transformers can be fine-tuned for robot perception/control |
| **Multimodal transformers** | Vision-language models enable natural language robot commands |
| **Long-context reasoning** | Extended context windows support multi-step planning |
| **In-context learning** | Robots can adapt to new tasks from few demonstrations |
| **World models** | Transformers can learn predictive models for decision-making |
| **Efficiency challenges** | Edge deployment requires quantization, distillation, sparse attention |
| **Interpretability gaps** | Black-box nature is problematic for safety-critical autonomy |

---

## Question Bank

### Architecture Questions
1. What are the fundamental differences between encoder-only, decoder-only, and encoder-decoder transformers? When would you choose each?
2. How does multi-head attention learn different relationship types? What determines the optimal number of heads?
3. Why did transformers replace RNNs/LSTMs despite having O(n²) attention complexity?

### Scaling Questions
4. What capabilities emerge at scale that don't exist in smaller models? Can we predict emergence?
5. How do scaling laws inform decisions about model size vs. training compute vs. data?
6. Is there a point of diminishing returns for transformer scale, or will bigger always be better?

### Multimodal Questions
7. How do vision transformers differ from CNNs in terms of inductive bias and data efficiency?
8. What makes vision-language models like CLIP effective for cross-modal understanding?
9. Can transformers unified across modalities (text, image, audio, action) enable embodied AI?

### Autonomy Questions
10. What are the biggest barriers to deploying transformers on robots (latency, memory, power)?
11. How can transformers be used for world modeling and predictive control?
12. What interpretability techniques exist for understanding transformer decision-making?

---

## Pre-Lecture Reading

### Essential
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — The original paper
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Visual explanation

### Background
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — Manning's course
- [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) — Line-by-line implementation

---

## Cross-References

- **Week 2 (JEPA):** Alternative to transformers for world modeling
- **Week 3 (SSMs/Mamba):** Linear-time alternatives to quadratic attention
- **Week 6 (Interpretability):** Understanding what transformers learn
- **Week 7 (Med-PaLM):** Safety-critical deployment patterns

---

*Prepared: 2026-04-04 • Session 1 Overview*
