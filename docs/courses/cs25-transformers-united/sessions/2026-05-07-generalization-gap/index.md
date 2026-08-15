---
title: "Session 7: Distinct Modes of Generalization from Parameters and Context"
layout: default
parent: CS25: Transformers United V6
nav_order: 7
permalink: /courses/cs25-transformers-united/sessions/2026-05-07-generalization-gap/
date: 2026-05-07
---

# Session 7: Distinct Modes of Generalization from Parameters and Context

**Date:** May 7, 2026
**Speaker:** Andrew Lampinen (Anthropic)
**Topic:** Distinct Modes of Generalization from Parameters and Context, and Paths to Bridge the Gap
**Slides:** [Link](https://drive.google.com/file/d/1-YIOa5Yal4RCjAsV-0tnW_NNDGbY1GTo/view)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=dJtHauhRasc)
**Status:** ✅ Slide insights extracted

---

## Core Question

> How do language models generalize from information they learn — and what might that tell us about natural intelligence?

LMs have **two fundamentally different ways of "learning"**:
1. **In-context learning (ICL)** — information provided in the context window
2. **Parametric learning** — information encoded via gradient descent into model weights

---

## Part 1: Parameters vs. Context — The Generalization Gap

### The Reversal Curse

When models are fine-tuned on facts like "A is B," they often fail to answer questions about "B is A" — even though it's the same information in reverse. This is the **Reversal Curse**.

**Experiment:**
- Fine-tune GPT/LLaMA on synthetic facts in one order (e.g., "Daphne Barrington is the director of 'A Journey Through Time.'")
- Model succeeds on same-fact-order questions
- Model fails on reversed-order questions ("Who directed 'A Journey Through Time'?" → wrong answer)

**But here's the twist:** models handle reversals just fine when the information is in-context. "If Zepax are bigger than Quarples, then Quarples are..." — the model correctly infers the reversal. This is exactly the same structure as the reversal curse, but ICL handles it.

### Why Does ICL Outperform Fine-Tuning on Latent Information?

Many training documents latently convey more than their explicit content. For example:
- **Reversals:** "X is Y's parent" implicitly contains "Y's parent was X"
- **Syllogisms:** Two statements about X→Y and Y→Z implicitly contain conclusions about X→Z
- **Multi-hop reasoning:** Explicit facts about X and Y can latently answer questions about their relationship

Models in context can reason over this latent information flexibly. Parametric learning consolidates it into a form that's more tied to the original explicit content — losing the flexibility.

### Even Training from Scratch Doesn't Fix It

Pretrained models (even small ~20M param models trained from scratch on reversals) still show the same pattern: forward generalization works, but reverse generalization fails — even when the reverse relationship is right there in the training data.

The core issue: **many structures are latent in the data but parametric learning doesn't encode them in a way that's usable at test time.**

---

## Part 2: Paths to Bridge the Generalization Gap

### Approach 1: In-Context Augmentation

If ICL generalizes better, use it to augment the fine-tuning data.

**Method:**
1. Put the full training dataset in context
2. Prompt the model to generate reasoning traces that make explicit connections (reversals, syllogisms, missing links)
3. Add these generated conclusions to the dataset
4. Fine-tune on the augmented dataset

**Result:** Augmented fine-tuning matches or exceeds ICL performance on reversals and syllogisms.

**Why it works:** Augmentation makes explicit and accessible what was already latent in the data — it doesn't create new information, it surfaces what was already there.

### Approach 2: Episodic Retrieval at Test Time

Bring relevant experiences into context at test time, turning parametric tasks into in-context ones.

**Method:** Oracle episodic memory that retrieves at least one relevant experience (plus some irrelevant ones). Use retrieved context to answer.

**Result:** Episodic retrieval unlocks flexible generalization that pure parametric learning can't achieve — even on latent structures like reversals.

**Connection to natural intelligence:** This parallels the hippocampal-cortical complement in brains. The hippocampus rapidly encodes specific experiences in rich detail; the neocortex consolidates information more slowly into abstract, generalized form. Retrieval is like bringing hippocampal content into neocortical "context."

### Approach 3: Test-Time Thinking via RL

Can models learn to regenerate necessary context information via chain-of-thought, without explicit retrieval?

**Method:**
1. Instill knowledge via fine-tuning on dataset A
2. Use RL to teach the model to regenerate relevant context in its CoT when answering questions
3. Test on held-out dataset B (not augmented)

**Result:** RL thinking improves generalization beyond the augmented distribution — but struggles with pure reversals (tries exhaustive enumeration rather than structured inference).

---

## Part 3: Connections to Natural Intelligence

The same latent generalization problem exists in biological learning systems:

| Structure | Explicit | Latent |
|-----------|----------|--------|
| Reversal | "X is Y's parent" | "Y's parent was X?" |
| Multi-hop | X→Y, Y→Z statements | Who is X's grandchild? |
| Cross-lingual | Japanese: "XはYさんのお母です" | Who is X's child? |
| Alternative goals | Navigate to ◊ | Navigate to ♥ |

**Brain parallels:**
- **Parametric learning** ≈ neocortical slow consolidation
- **Episodic retrieval** ≈ hippocampal replay and memory consolidation
- **ICL** ≈ bringing relevant experiences into current context

Evidence from neuroscience: offline hippocampal replay, preemptive solving, and the gradual consolidation pattern all mirror the augmentation and retrieval strategies.

---

## Key Takeaways

1. **ICL generalizes to latent information that parametric learning misses** — because parametric consolidation ties knowledge to its original explicit form
2. **Three paths to bridge the gap:**
   - **Augmentation** (train-time): surfaces latent info before consolidation
   - **Retrieval** (test-time): brings specific experiences into context on demand
   - **RL thinking** (test-time): teaches models to regenerate necessary context via CoT
3. **Tradeoffs:** augmentation is efficient at test-time but expensive at train-time; retrieval is free at train-time but costs at inference; RL thinking generalizes beyond augmented data but struggles with exhaustive enumeration
4. **The brain has an analogous architecture** — complementary learning systems (hippocampus + neocortex) solve the same problem

---

## Papers Referenced

- *On the generalization of language models from in-context learning and finetuning* — Lampinen et al. (Google DeepMind + Stanford)
- *Latent learning: episodic memory complements parametric learning* — Lampinen et al.
- *Improving latent generalization using test-time compute* — Chaudhry et al.
- *Complementary Learning Systems* — McClelland, McNaughton, O'Reilly (1995)
- *A Theory of Usable Information under Computational Constraints* — Xu et al. (ICLR 2020)

---

## Speaker Info

**Andrew Lampinen** — Member of Technical Staff at Anthropic. Previously Staff Research Scientist at Google DeepMind, PhD in Cognitive Psychology at Stanford. Research bridges AI and cognitive science: learning, generalization, and representation in LMs, agents, and humans.

- Twitter/X: @AndrewLampinen
- Bluesky: lampinen.bsky.social
- Substack: infinitefaculty.substack.com

---

*Last updated: 2026-08-15*
