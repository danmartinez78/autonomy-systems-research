---
title: "Session 8: From Language Models to Native Multimodal Intelligence"
layout: default
parent: CS25: Transformers United V6
nav_order: 8
permalink: /courses/cs25-transformers-united/sessions/2026-05-21-native-multimodal-intelligence/
date: 2026-05-21
---

# Session 8: From Language Models to Native Multimodal Intelligence

**Date:** May 21, 2026
**Speaker:** Victoria Lin (Thinking Machines)
**Topic:** From Language Models to Native Multimodal Intelligence
**Slides:** [Link](https://drive.google.com/file/d/10Doblrt3Le_FpbVQoMP0DbuCIO3rtWPW/view)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=NDdc39KYqDU)
**Status:** ✅ Slide insights extracted

---

## Core Premise

Language models trained purely on text have demonstrated remarkable emergent capabilities — but the physical world is fundamentally multimodal. Next-token prediction at scale works for text, but moving beyond language toward real-world interaction requires **native multimodal intelligence**: perceiving, reasoning about, and generating across visual, auditory, and temporal modalities.

---

## Core Architecture: Tokenization + Global Autoregression

Native multimodal LLMs share two fundamental design principles with text-only LLMs:

1. **Tokenization across the board** — All modalities (text tokens, image patches, audio frames) are treated as discrete tokens in a unified vocabulary
2. **Globally autoregressive generation** — The same next-token prediction objective applies across all modalities

A shared Transformer processes mixed sequences of T (text), V (image patch), and A (audio frame) tokens.

**Training objective:** Joint training across modalities, with text output as the anchor.

---

## Core Architecture: Joint Training

The three ingredients for native multimodal training:
1. Unified tokenization across modalities
2. Globally autoregressive generation
3. Joint training across all modalities together

This is how models like **Gemini 3.1**, **Qwen 3.7**, **Kimi K2.6**, and **Omni** are built.

---

## Key Research Questions

1. **How to generate non-text modalities?** (images, audio, video)
2. **Is there positive transfer between understanding and generation of non-text modalities?**

---

## Approaches to Multimodal Generation

### Chameleon (Meta, 2024)

**Approach:** Encode all modalities as discrete tokens via Vector Quantized VAE (VQ-VAE). One Transformer processes interleaved text-image sequences.

**Strengths:**
- Early fusion — one unified model handles arbitrary text-image orderings
- First model to show interleaved text-image generation from scratch while preserving text-only performance

**Limitations:**
- VQ-VAE image tokens were later found less effective than continuous embeddings (e.g., SigLIP) for fine-grained visual semantics
- By 2026, diffusion- and flow-matching-based approaches proved more scalable and efficient for image generation

---

### Transfusion (Zhou et al., 2024)

**Approach:** Unifies autoregressive next-token prediction with diffusion-based image generation in one architecture.

- Text tokens → standard next-token prediction (cross-entropy)
- Image tokens → diffusion process applied to decoder outputs

**Strengths:**
- First seamless unification of AR + diffusion in one model
- Significantly better image generation quality and training efficiency vs. discrete VQ-VAE approaches

**Limitations:**
- VAE representations remain ineffective for visual understanding — a key open problem
- State-of-the-art omni models today use **separate representations** for understanding vs. generation, though active research aims to unify them

---

## Multimodal Architecture Design

### Modality-Aware Sparsity (Mixture-of-Transformers / MoT)

**Key insight:** Different modalities have different optimal parameterizations. Dense multimodal models are inefficient because a single set of parameters must handle text, images, and audio optimally.

**MoT architecture:**
- Input: mixed-modality token sequences
- Each token routed (deterministically, by modality) to modality-specific transformer parameters
- Output: independent transformer parameters per modality
- Attention: cross-modal attention enables interaction across modalities

**Benefits:**
- Substantially improves generation quality for non-text modalities
- Improves training efficiency, stability, and controllability
- Enables asynchronous training of different modalities across stages
- Powers real-world systems like **BAGEL** (multi-modal model) and **Pi 0.7** (robotic foundation model)

**Combination with MoE:** MoT + MoE (Mixture-of-Experts) is complementary — both provide sparsity along different axes.

---

## The Understanding vs. Generation Transfer Problem

A central open question: **does training to generate images/audio improve the model's ability to understand them?**

**Challenges to positive transfer:**
- Language is a highly compressed abstraction of human cognition — rich semantic signal
- Images/videos are sensory data with high redundancy and frame correlation
- Poor loss landscape for cross-modal generation ↔ understanding alignment

**Current state (2026):** Evidence for positive transfer is mixed. Understanding and generation may require different representations — hence the prevalence of separate encoding pathways in practice.

---

## Where We Stand Today

Today's multimodal LLMs excel at **digital multimodal information processing** — reading documents with figures, answering questions about images, transcribing audio. But they still fall far short of **full physical-world multimodal intelligence**:

- True sensory grounding in the physical world
- Real-time perception-action loops
- Long-horizon multimodal planning

---

## Interaction Models (Thinking Machines)

Victoria's lab is working on **Interaction Models** — natively multimodal models that perceive visual, auditory, and textual information jointly, and generate text and audio.

**Key design features:**
1. **Multi-stream, micro-turn architecture** — continuous perception and response (not turn-based like current chat models)
2. **System 1 & 2 design** — fast reflexive responses + background model for long-horizon reasoning
3. **Real-time interactivity** — sees and hears continuously, responds in real-time

**Research grant available** for researchers working on interactivity: thinkingmachines.ai/news/interactivity-research-grants

---

## Key Takeaways

1. **Tokenization + global autoregression** — the two principles that make LLM architecture transfer to multimodal settings
2. **Multiple viable approaches** for image generation: discrete tokens (Chameleon), diffusion + AR hybrid (Transfusion), modality-specific routing (MoT)
3. **Separate understanding/generation representations** are still mainstream — the unified representation dream remains open
4. **MoT is a promising architecture direction** — modality-specific parameters with cross-modal attention enables better generation quality and efficient mixed-modal training
5. **Future is specialized** — given the complexity of the problem space, we'll see increasing specialization (embodiment vs. document understanding vs. real-time interaction)

---

## Papers Referenced

- *Chameleon: Mixed-Modal Early-Fusion Foundation Models* — Chameleon Team (Meta, 2024)
- *Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model* — Zhou et al. (2024)
- *Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models* — Liang et al. (2024)
- *BAGEL: Emerging Properties in Unified Multimodal Pretraining* — Deng et al. (2025)
- *Pi 0.7: A Steerable Generalist Robotic Foundation Model with Emergent Capabilities* — Ai et al. (2026)

---

## Speaker Info

**Victoria Lin** — Thinking Machines. Research focuses on multimodal intelligence, moving from language-only LLMs to systems that perceive and reason across visual, auditory, and temporal modalities.

- Email: victoria@thinkingmachines.ai
- Twitter: @VictoriaLinML

---

*Last updated: 2026-08-15*
