---
title: "Session 2: JEPA & World Models"
layout: default
parent: CS25: Transformers United V6
nav_order: 2
---

# Session 2: JEPA & World Models

**Date:** April 9, 2026
**Speakers:** Hazel Nam & Lucas Maes (Brown University)
**Status:** Awaiting Video (~3 week upload delay per Stanford policy)

---

## Talk Description

*From the course page:* World models are increasingly moving away from reconstruction and toward prediction in latent space. This talk presents two recent JEPA-based approaches that illustrate this shift from complementary angles.

**Causal-JEPA** induces object-level relational bias to promote representations that capture entities *and interactions*, leading to stronger reasoning and more efficient planning. **LeWorldModel** shows that such predictive world models can also be trained stably end-to-end from raw pixels using a minimal objective and a clean architectural recipe, while remaining competitive on control tasks.

**Unified thesis:** Predictive latent learning becomes most powerful when combined with both **structural bias** and **architectural simplicity**. This suggests a promising path toward robust world models that support abstraction, reasoning, and control.

---

## What JEPA Actually Is: A Framework, Not an Architecture

JEPA stands for **Joint Embedding Predictive Architecture** — and this distinction matters enormously.

JEPA is **not a specific neural network architecture**. It's a **training framework / self-supervised learning objective** that defines how to train encoders and predictors to learn world models.

The components of JEPA are existing, well-known architectures:
- **Encoder**: Encodes current frame → latent (typically a ViT / transformer)
- **Predictor**: Predicts future latent from current latent (typically a transformer)
- **Target encoder**: Encodes the target frame for contrastive alignment

JEPA tells you *how to connect and train these pieces* via a latent prediction objective, not *what those pieces must be*. You still use transformers. You just train them differently.

| Term | What it is | JEPA analogy |
|------|-----------|--------------|
| BERT | Pre-training framework (masked language modeling) | JEPA is the "masked world modeling" equivalent |
| ViT | Vision transformer architecture | JEPA uses ViT as its encoder |
| JEPA | Training framework for latent world modeling | "BERT for video/world prediction" |

This means: when speakers say "we don't want generative models," they're describing JEPA as an alternative *training objective*, not a new architecture. The "generative" critique is about the *training approach* (pixel-level prediction) — JEPA replaces it with latent-level prediction while keeping the same transformer building blocks.

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

2. **Rich context for prediction** — To predict the future latent state, you need to understand the full current state. With bidirectional attention, every position sees the entire input, not just the prefix.

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
- Object-level causal structure makes predictions interpretable and composable

---

## Confounders and Why Object-Centric Representations Help

Hazel Nam mentioned confounders multiple times — this is a concept from causal inference that is central to why JEPA's object-centric approach matters for physical AI.

### What Is a Confounder?

A **confounder** is a variable Z that causally influences *both* X and Y, creating a spurious correlation between X and Y that isn't causal:

```
Z → X
Z → Y

X ─ ? ─ Y   (spurious correlation, not causal)
```

Classic example: age is a confounder between shoe size and reading ability. Larger shoes don't cause better reading — both are caused by age. If you don't control for age, you incorrectly conclude shoes cause reading.

### Confounders in Video Prediction / World Models

In world model training for robotics, confounders appear at the pixel level:
- **Camera angle** — affects both current frame and future frames identically
- **Lighting conditions** — causes both observations in similar ways
- **Background static elements** — consistent confounder across frames

If you want to learn "does action A cause outcome B" in the world, but camera angle causes both the current and future observations — the confounder poisons your representation. The model learns to predict camera-consistent futures (confounded) rather than actual causal dynamics (actual causal structure).

### How Object-Centric Representations Handle Confounders

Object-centric slots factor out confounders automatically:
- The **background slot** absorbs camera angle, lighting, and static scene elements
- **Object slots** (ball, robot arm, door) capture the causally relevant dynamics
- When predicting future latents, you predict ball_slot → ball_slot, not background_slot → background_slot

The confounder (background/camera) gets isolated into its own slot where it can't contaminate object-level predictions. This is why C-JEPA specifically talks about causal object structure — it factors out confounders at the representation level, making the learned dynamics genuinely causal rather than confounded.

---

## World Models in Physical AI and Robotics

Lucas Maes articulated a critique of VLA (Vision Language Action) models and proposed world models as the path forward for physical AI. Hazel Nam added the "policy evaluator" framing.

### The VLA Critique

VLA models learn end-to-end mappings from observations to actions via imitation learning or RL. The problem: VLAs have no model of the world — they learn correlations (obs → action) but can't predict what happens if they do something different. This means:

- **No counterfactual reasoning**: "What happens if I do X instead of Y?" — VLA can't answer this, it just picks the action it saw in training
- **No physical understanding**: A robot trained to stack blocks might succeed 90% of the time but fail in new configurations — it learned pattern-matching, not physics
- **Brittle to distributional shift**: VLA fails when the scene differs from training even in subtle ways

### The World Model Response

World models address this by learning a predictive model of how the world evolves:

```
Current state + Action → Predicted future state
```

If you have a good world model, you can ask: "If I do action A, will the outcome be good?" — and get an answer from simulation, not physical trial. This is safe, fast, and allows planning over many candidate actions before executing any.

### Robot Dancing Exception

Lucas Maes made an interesting point: a robot dancing only really needs understanding of **internal dynamics** (its own body mechanics, joint torques, etc.), not a full world model. For purely self-referential tasks, the world model only needs to model the robot's own body, not external objects.

But for tasks where the robot interacts with the world (manipulation, navigation, tool use), you need a world model that predicts both the robot's dynamics AND how external objects respond to those dynamics.

### Policy Evaluation (Hazel Nam's Framework)

World models as **policy evaluators**: instead of learning a policy directly from observations→actions, you can:

1. Train a world model that predicts: `state_t → state_{t+1}` given an action
2. For a candidate policy/plan, simulate it through the world model
3. Evaluate whether the simulated outcome achieves the goal
4. Only execute actions that look promising in simulation

This is fundamentally different from VLA's direct mapping approach. It decouples "understanding the world" (world model) from "deciding what to do" (policy/planning). The world model is reusable across many tasks; the policy layer can be lighter because it can query the world model.

### Hierarchical Temporal Reasoning for Long-Horizon Planning

JEPA requires **hierarchies of temporal reasoning** for longer-horizon planning:

- **Single-step JEPA** (frame T → frame T+1): predicts immediate next state — useful for fine-grained manipulation, reactive control
- **Multi-scale JEPA** (frame T → frame T+N at multiple N): predicts at multiple temporal horizons — captures both low-level dynamics and high-level structure
- **Hierarchical planning**: "go to the kitchen" (high-level, abstract) → "walk forward 3m, turn left, open door" (low-level, executable). The world model must operate at multiple granularities to support both.

The hierarchy question is still open in JEPA research — how to architect the multi-scale temporal prediction, and how to connect high-level goal reasoning to low-level motor control.

---

## Kalman Filter Analogy

Both Kalman filters and JEPA operate in **latent space** (not pixel space), sidestepping pixel-level entropy. The key difference:

| Aspect | Kalman Filter | JEPA |
|--------|--------------|------|
| State vector | Hand-specified (x, y, vx, vy) | Learned end-to-end from data |
| Disentanglement | By design — each dimension has meaning | Emergent — not guaranteed interpretable |
| Structure | Fixed, known physics model | Flexible, learned from observations |
| Expressiveness | Limited to linear-Gaussian assumptions | Can capture complex nonlinear dynamics |
| Interpretability | High — you know what each state dimension means | Black-box — structure is learned, not guaranteed parseable |

Trade-off: Kalman = interpretable but limited expressiveness. JEPA = powerful but black-box. JEPA's learned representations can capture rich structure that would be intractable to hand-specify, but you lose the guaranteed interpretability of a Kalman filter.

---

## Papers Referenced

| Paper | Venue | Relevance |
|-------|-------|-----------|
| [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) | NeurIPS 2020 | Slot Attention mechanism |
| [C-JEPA](https://arxiv.org/abs/2602.11389) | 2026 | Object-centric JEPA for planning |
| [LeWorldModel](https://arxiv.org/abs/2603.19312) | 2026 | Stable end-to-end JEPA from pixels |
| [A Path Towards Autonomous Machine Intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf) | 2022 | LeCun's JEPA vision |

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Abstraction** | Latent prediction enforces compact representations — good for generalization |
| **Reasoning** | Object-centric JEPA enables interaction reasoning — predict how objects affect each other |
| **Control** | LeWorldModel competitive at 48× faster inference — practical for real-time robotics |
| **Sample efficiency** | Predicting in latent space requires less data than pixel reconstruction |
| **Efficient planning** | C-JEPA uses only 1% of latent features vs patch-based → 8× faster planning |
| **Hierarchical planning** | Multi-scale JEPA for long-horizon tasks still an open research question |

---

## Pre-Read

For background and pre-lecture material, see [pre-read.md](./pre-read.md).

---

## Slides & Video

- **Slides:** Not yet posted (~3 week upload delay per Stanford policy)
- **Video:** Not yet posted (expected ~April 30, 2026)

*This document will be updated when slides and video become available.*

---

*Session notes compiled during live lecture. Video synthesis pending post-production upload.*
