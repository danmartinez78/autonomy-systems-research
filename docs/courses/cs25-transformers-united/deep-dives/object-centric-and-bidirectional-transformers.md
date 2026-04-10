---
title: "Object-Centric vs. Patch-Based Representations & Bidirectional Transformers"
layout: default
parent: Deep Dives
nav_order: 1
permalink: /courses/cs25-transformers-united/deep-dives/object-centric-representations
---

# Object-Centric vs. Patch-Based Representations

*Deep dive supplementing the JEPA lecture (Week 2)*

---

## Two Ways to Represent a Scene

### Patch-Based Representation

You take an image, chop it into a fixed grid of small patches (e.g., 16×16 pixels), linearly embed each patch into a vector, and feed all the patch tokens into a transformer identically:

```
Image → [16×16 patch, 16×16 patch, ..., 16×16 patch] → Transformer (treats all equally)
```

- **No inherent notion of "objects"** — just a set of decontextualized patches
- Each patch token carries its own spatial position (positional encoding), but there's no grouping
- The transformer *implicitly* has to figure out which patches cohere into objects
- Standard in ViT (Vision Transformer), MAE, BEiT, etc.

### Object-Centric Representation

The representation explicitly separates different entities/objects in the scene:

```
Scene → [Object A (red ball), Object B (green box), Object C (background)] → Each has own slot
```

- Each object gets its own **dedicated slot** — a vector that represents that entire object
- "Slot" is the key term: think of it as a container that binds to one object
- The representation is structured around **entities**, not spatial grid positions
- Requires a mechanism for *binding* — figuring out which patches belong to which object

---

## Why This Distinction Matters for JEPA

JEPA predicts future states in latent space. The representational structure of those states determines what kinds of predictions are tractable:

| Representation | What you predict | Problem |
|---------------|-----------------|---------|
| Patch-based | Pixel values of masked patches | Astronomical entropy — billions of equally valid futures |
| Object-centric | Object positions, attributes, relations | Much lower entropy — physics is predictable in object space |

**The key insight:** Physics happens at the object level, not the pixel level. A ball moves left regardless of which specific camera pixels capture it. Object-centric representations capture this invariance.

With object-centric JEPA (C-JEPA specifically):
- You mask at the **object/slot level**, not the patch level
- Instead of "predict pixels 47-163," you predict "object A (the ball) will be at position X"
- The model learns that objects persist, have properties, and interact causally

---

## Bidirectional Transformer in JEPA Context

### What "Bidirectional" Means

Standard autoregressive transformers (like GPT) are **unidirectional** — they process tokens left-to-right (or right-to-left), so each token can only attend to tokens before it. This is natural for sequence generation.

JEPA uses a **bidirectional transformer** — the same architecture as BERT's encoder, where every patch/token can attend to every other patch/token, in both directions:

```
Left → → → → →
← ← ← ← ← ← Right

OR (bidirectional):

← ↔ ↔ ↔ ↔ ↔ →
All positions attend to all positions simultaneously
```

### Why Bidirectional for JEPA?

1. **No sequential generation** — JEPA doesn't generate pixels token-by-token. It encodes entire frames into latent representations. Bidirectional attention lets the encoder see the full context simultaneously.

2. ** Rich context for prediction** — To predict the future latent state, you need to understand the full current state. With bidirectional attention, every position sees the entire input, not just the prefix.

3. **掩码 (Masked) prediction** — Like BERT, JEPA trains by masking some fraction of inputs and predicting them from the bidirectional context. This requires full bidirectional attention to fill in any masked region.

### How It Relates to Slot Attention

The bidirectional transformer processes the **input features** to produce the contextualized representations that Slot Attention then queries:

```
Input image patches → Bidirectional Transformer (ViT encoder) → Per-patch contextualized features
                                                                            ↓
                                                               Slot Attention (K rounds)
                                                                            ↓
                                                       K object slots, each binding to one object
```

The bidirectional transformer handles "what goes with what spatially" (patch-level context). Slot Attention then resolves "which patches belong to which object" (object-level binding).

---

## Slot Attention: How Binding Works

*Paper: [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) — Locatello et al., NeurIPS 2020*

### The Core Idea

You have K slots (e.g., 5 slots for up to 5 objects). Slots are **exchangeable** — slot 1 could bind to the dog, the ball, or the background, depending on the input content. The binding emerges through competition.

### Iterative Attention Mechanism

Slot Attention runs for R rounds (typically 3-6):

```
Round 1:
  - Each slot sends queries to all input features
  - Attention weights determine which features "vote" for which slot
  - Slots with strong support win (slots that many features point to)

Round 2:
  - Slots update based on new attention from round 1
  - Competition continues — strong slots get stronger, weak slots fade

Round R:
  - Each slot converges to representing one coherent object/group
```

### Key Properties

| Property | What It Means |
|----------|--------------|
| **Exchangeable slots** | Slot 1 can bind to any object; no pre-assigned identity |
| **Competitive binding** | Slots compete — one feature region can only "vote" for one slot's representation |
| **Iterative refinement** | Multiple rounds sharpen the binding |
| **Object count flexibility** | If you have 7 objects but only 5 slots, some slots represent multiple things or empty space |

### What Makes It Different from Standard Attention

Standard self-attention: every query attends to all keys. All queries participate equally.

Slot Attention:
- Fixed number K of slot "query" vectors (not one per input position)
- Iterative refinement over rounds (not one-shot)
- Competitive normalization (slots must share a fixed capacity budget — what one gains, others lose)

---

## Putting It Together

```
Image
  ↓
[Patchify] → N patches (e.g., 16×16 pixels each)
  ↓
[Linear embed + positional encoding] → N patch tokens
  ↓
[Bidirectional Transformer] → N contextualized feature vectors (each sees full image context)
  ↓
[Slot Attention, R rounds] → K slots, each binding to one object
  ↓
Per-slot representations: [ball_slot, dog_slot, background_slot, ...]
```

The bidirectional transformer provides rich **patch-level** context. Slot Attention then resolves **object-level** structure via competitive binding.

In C-JEPA (JEPA + causal/object-centric):
- Objects in slots are the units of masking and prediction
- Predicting "where will the ball be in frame T+1" is predicting the ball_slot's future value
- Object-level causal structure makes predictions interpretable andComposable

---

## Key Takeaways

1. **Patch-based = grid of patches, processed equally** — the transformer must learn object structure from scratch
2. **Object-centric = structured around entities** — the representation has slots that bind to objects
3. **Binding problem** — the hard part is figuring out which patches belong to which object; this doesn't require supervision
4. **Slot Attention** = competitive iterative attention that resolves binding, making slots specialize
5. **Bidirectional transformer** = enables masking at any position with full context; powers the patch-level features that Slot Attention then works on
6. **Object-centric JEPA** = mask at slot level, not patch level; predict where objects will be, not raw pixels

---

## Papers Referenced

| Paper | Venue | Relevance |
|-------|-------|-----------|
| [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) | NeurIPS 2020 | Slot Attention mechanism |
| [Masked Autoencoder (MAE)](https://arxiv.org/abs/2111.06377) | CVPR 2022 | Patch-based masked prediction |
| [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) | 2018 | Bidirectional transformer architecture |
| [C-JEPA](https://arxiv.org/abs/2502.04704) | 2025 | Object-centric JEPA for planning |

---

*Last updated: 2026-04-09*
