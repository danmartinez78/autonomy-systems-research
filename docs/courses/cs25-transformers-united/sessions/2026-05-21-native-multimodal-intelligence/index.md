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
**Status:** ✅ Enriched with lecture content

---

## Core Premise

Language models trained purely on text have demonstrated remarkable emergent capabilities — but the physical world is fundamentally multimodal. Next-token prediction at scale works for text, but moving beyond language toward real-world interaction requires **native multimodal intelligence**: perceiving, reasoning about, and generating across visual, auditory, and temporal modalities.

> **[added from lecture]** Victoria opened by noting that while today's state-of-the-art models (Gemini, Qwen, Kimi) are described as "native multimodal," the primary product mode for most is still multimodal input → text-only output. The vision for "native multimodal" is broader: both input AND output across modalities.

---

## Core Architecture: Tokenization + Global Autoregression

Native multimodal LLMs share two fundamental design principles with text-only LLMs:

1. **Tokenization across the board** — All modalities (text tokens, image patches, audio frames) are treated as discrete tokens in a unified vocabulary
2. **Globally autoregressive generation** — The same next-token prediction objective applies across all modalities

A shared Transformer processes mixed sequences of T (text), V (image patch), and A (audio frame) tokens.

**Training objective:** Joint training across modalities, with text output as the anchor.

> **[added from lecture]** Victoria gave more detail on the tokenization process: for images, "patchify" divides an image into predefined standard-sized patches (e.g., 16×16 pixels). Each patch goes through an encoder to get a vector representation, which is then quantized via a learned vector codebook (VQ-VAE) to get a discrete token index. For audio, similar process: waveform → transforms → tokenization. For video: treated as a sequence of image frames, each patchified, tokens concatenated across the temporal sequence. She emphasized that "tokens" can be dense vectors or discrete indices — what matters is the sequential representation enabling global autoregression.

---

## Two Broad Categories of Multimodal Models

### Type 1: Multimodal Input → Text Output

Condition on multimodal sequences (image + text, video + text), calculate loss on text tokens only. Examples: Gemini, Qwen, Kimi. Enables strong understanding capabilities.

### Type 2: Omni-Models (Multimodal Input AND Output)

Generate not just text but also images and audio. Examples: GPT-4o (named "Omni" for this reason), Chameleon.

> **[added from lecture]** Victoria noted that while many companies have developed Omni models, the core product use cases are often still multimodal-in / text-out. The Omni capability is important for the full vision but understanding-driven applications dominate current deployments.

---

## Key Research Questions for Omni-Models

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

> **[added from lecture]** Victoria walked through the Chameleon architecture in more detail: image → patchify → continuous encoder → VQ-VAE codebook lookup → discrete tokens. These discrete image tokens are interleaved with text tokens in a single sequence, trained with cross-entropy language modeling objective across all tokens. The model can generate mixed text-image documents in original order. The key hypothesis: if you can reduce everything to discrete tokens, language model properties transfer directly. Key limitations discovered: (1) discretization causes significant information loss for image understanding — there's a large gap vs. continuous encoders like SigLIP; (2) discrete generation requires much more training data to produce well-formed images due to token efficiency issues.

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

> **[added from lecture]** Victoria explained the Transfusion architecture more fully: for text, standard causal autoregressive modeling with standard causal attention. For images: take a segment of image representations, apply *bidirectional* attention across the image region (not causal), run multiple diffusion steps to denoise into a clear image, then feed that as input for the next autoregressive step. The architectural change: text uses causal attention; image patches use bidirectional attention within the image region. This is what enables much better image generation quality with much fewer tokens than discrete approaches. Victoria noted the key open problem the paper still faces: the VAE representation used for generation is not efficient for understanding — you need different encodings for the two directions, which is why SOTA omni models today often use two separate encoding pathways.

---

## Multimodal Architecture Design

### Modality-Aware Sparsity (Mixture-of-Transformers / MoT)

**Key insight:** Different modalities have different optimal parameterizations. Dense multimodal models are inefficient because a single set of parameters must handle text, images, and audio optimally.

**MoT architecture:**
- Input: mixed-modality token sequences
- Each token routed (deterministically, by modality) to modality-specific transformer parameters (QKV projection matrices and feed-forward layers)
- Output: independent transformer parameters per modality
- Attention: cross-modal attention enables interaction across modalities

**Benefits:**
- Substantially improves generation quality for non-text modalities
- Improves training efficiency, stability, and controllability
- Enables asynchronous training of different modalities across stages
- Powers real-world systems like **BAGEL** (multi-modal model) and **Pi 0.7** (robotic foundation model)

**Combination with MoE:** MoT + MoE (Mixture-of-Experts) is complementary — both provide sparsity along different axes.

> **[added from lecture]** Victoria explained that MoT is complementary to MoE — MoT adds sparsity by modality (each token uses its modality's parameters), MoE adds sparsity within each modality's parameters (multiple experts per modality). She noted that allocating more experts helps text performance more than image generation — the scaling curves differ. This means you can customize expert counts per modality. MoT enables a practical scenario: you have a strong off-the-shelf text model, and you want to add image or speech generation. Instead of full fine-tuning (which risks degrading text performance), you add new modality-specific parameters, freeze the text model, and only train the new modality parameters.

---

## The Understanding vs. Generation Transfer Problem

A central open question: **does training to generate images/audio improve the model's ability to understand them?**

**Challenges to positive transfer:**
- Language is a highly compressed abstraction of human cognition — rich semantic signal
- Images/videos are sensory data with high redundancy and frame correlation
- Poor loss landscape for cross-modal generation ↔ understanding alignment

**Current state (2026):** Evidence for positive transfer is mixed. Understanding and generation may require different representations — hence the prevalence of separate encoding pathways in practice.

> **[added from lecture]** Victoria broke this down in both directions:
>
> **Does understanding help generation? Strongly yes.** Better base understanding capabilities → better information processing, planning, reasoning → generates images with more fine-grained details, more accurate infographics, less hallucination.
>
> **Does generation training help understanding? Little evidence so far.** Training an omni model heavily on image generation does not reliably improve its image understanding. Victoria cited Berkeley professor Sergey Levine's observation: it's puzzling that next-token prediction gives LLMs such amazing abilities, but next-frame prediction doesn't similarly strengthen video models. Her hypotheses for why: (1) Language is a highly compressed abstraction of human cognition — training on language means training on human reasoning and intent; images/videos are passive sensory observation, not subjective abstraction. (2) The loss landscape for image/video is more complicated — generation loss can look fine to humans even when the model isn't learning what we actually care about. (3) Video frames are highly redundant across time, making next-frame prediction a less informative signal. Victoria noted this is an open, actively researched question.

---

## The MoT Family in Practice

> **[added from lecture]** Victoria discussed follow-up work building on MoT:

**BAGEL (2025):** Uses MoT-inspired architecture with separate parameters for image generation. The base model is a multimodal language model. Has separate encoding representations for image understanding features. Key capability: because it's modeling mixed sequences autoregressively, the model can plan before generating — it can first generate a thinking trace in text, then generate the final image. This "thinking before generation" technique is now used by many state-of-the-art image generation models.

**Robotics / Embodied AI:** MoT-style architecture is being used to predict action vectors (a distinct modality from text/image). The overall language modeling structure and self-attention allow base LLM world knowledge to transfer to action prediction through the shared attention mechanism — even with modality-specific parameters.

---

## Where We Stand Today

Today's multimodal LLMs excel at **digital multimodal information processing** — reading documents with figures, answering questions about images, transcribing audio. But they still fall far short of **full physical-world multimodal intelligence**:

- True sensory grounding in the physical world
- Real-time perception-action loops
- Long-horizon multimodal planning

> **[added from lecture]** Victoria noted that multimodal models are more computationally heavy than text models, creating additional infrastructure challenges for training and inference. She predicted that in the short term, we'll see increasing specialization: different customized multimodal models for different capability areas (document understanding, robotics, real-time interaction), with the interesting research question being how to unify them into a coherent system.

---

## Interaction Models (Thinking Machines)

Victoria's lab is working on **Interaction Models** — natively multimodal models that perceive visual, auditory, and textual information jointly, and generate text and audio.

**Key design features:**
1. **Multi-stream, micro-turn architecture** — continuous perception and response (not turn-based like current chat models)
2. **System 1 & 2 design** — fast reflexive responses + background model for long-horizon reasoning
3. **Real-time interactivity** — sees and hears continuously, responds in real-time

**Research grant available** for researchers working on interactivity: thinkingmachines.ai/news/interactivity-research-grants

---

## Q&A Highlights

> **[added from lecture]** Key exchange on MoT vs. MoE: Victoria clarified that MoT's benefit comes from having separate parameters per modality (text, image, audio), not from the mixture-of-experts mechanism. They can be combined (MoT + MoE), where each modality has multiple experts. On the question of whether MoT helps image *understanding*: Victoria said they didn't find modality separation to help understanding — what matters for understanding is whether you're outputting text. Both text and image input tokens should go through the same set of parameters for understanding tasks. MoT's gains are specifically on the generation side.

> **[added from lecture]** On Jeff Hinton's world models: Victoria sees them as an architecture specifically designed to be more efficient at modeling physical world spatiotemporal relations — a different problem from document understanding where current patch + encoder paradigms work well. She believes we may need different representation schemes for different application domains.

> **[added from lecture]** On training multimodal models for video generation to improve knowledge work: Victoria's view is that so far, video generation training hasn't transferred well back to generic task capability. However, robotics applications are showing more promising signals — using video models for future state prediction as feedback for action prediction. Not a pure transfer from generation to knowledge, but a more integrated use.

> **[added from lecture]** On rendering text as images (OCR as modality unification): Victoria hasn't tried it but finds the idea interesting. Her prediction: it would be less efficient than training on raw text because text already has a nice symbolic structure. However, OCR could be more context-efficient for representing large amounts of text (a screenshot of a paragraph vs. tokenizing it). She noted someone should run this experiment.

> **[added from lecture]** On whether everything should be autoregressive: Victoria's view is that next-token prediction has proven very effective. Even if it looks like surface-level next-token prediction, the network connections are complicated enough that structure learning is emerging in latent space — the network may be doing more than the training objective appears to prescribe. She doesn't think autoregression is flawed — it's just that the surface simplicity of the objective belies the complex internal representations.

> **[added from lecture]** On spatial reasoning and physical environments: Victoria isn't a spatial reasoning expert but notes that robotics labs are seeing progress in vision-language-action models, and that multimodal language model backbones are helping — Physical Intelligence and similar labs leverage VLMs as backbones rather than training from scratch. There's also work going in the opposite direction (less language-dependent, more vision-signal-focused), though she's less familiar with those approaches.

---

## Key Takeaways

1. **Tokenization + global autoregression** — the two principles that make LLM architecture transfer to multimodal settings
2. **Multiple viable approaches** for image generation: discrete tokens (Chameleon), diffusion + AR hybrid (Transfusion), modality-specific routing (MoT)
3. **Separate understanding/generation representations** are still mainstream — the unified representation dream remains open
4. **Understanding → generation transfer is strong; generation → understanding transfer is weak** — language is a compressed human abstraction; images/videos are sensory data with different loss landscape
5. **MoT is a promising architecture direction** — modality-specific parameters with cross-modal attention enables better generation quality and efficient mixed-modal training; also enables extending existing text models with new modalities without fine-tuning the original capabilities
6. **Future is specialized** — given the complexity of the problem space, we'll see increasing specialization (embodiment vs. document understanding vs. real-time interaction)
7. **Autoregression works — but may be doing more than it appears** — the surface simplicity of next-token prediction belies complex internal structure learning

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
