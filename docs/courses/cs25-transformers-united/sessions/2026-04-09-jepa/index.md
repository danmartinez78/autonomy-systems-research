---
title: "Session 2: JEPA & World Models"
layout: default
parent: CS25: Transformers United V6
nav_order: 2
permalink: /courses/cs25-transformers-united/sessions/2026-04-09-jepa/
date: 2026-04-09
---

# Session 2: JEPA & World Models

**Date:** April 9, 2026
**Speakers:** Hazel Nam (Heejeong Nam) & Lucas Maes (Brown University / Mila)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=GBd7iuJkW08)
**Status:** ✅ Enriched with lecture content

---

## Talk Description

*From the course page:* World models are increasingly moving away from reconstruction and toward prediction in latent space. This talk presents two recent JEPA-based approaches that illustrate this shift from complementary angles.

**Causal-JEPA** induces object-level relational bias to promote representations that capture entities *and interactions*, leading to stronger reasoning and more efficient planning. **LeWorldModel** shows that such predictive world models can also be trained stably end-to-end from raw pixels using a minimal objective and a clean architectural recipe, while remaining competitive on control tasks.

**Unified thesis:** Predictive latent learning becomes most powerful when combined with both **structural bias** and **architectural simplicity**. This suggests a promising path toward robust world models that support abstraction, reasoning, and control.

---

## Personal Framing

> **[added from lecture]** Hazel opened by acknowledging nervousness: "This is my first time giving a talk in English, but at the same time, I'm really, really excited to talk about JEPA world model." She framed the talk as motivated by the question: *Are we patchifying the image to predict the next step? Probably not* — humans don't represent scenes as grids of pixels, and models shouldn't either.

---

## JEPA vs Generative World Models: Deeper Verbal Explanation

> **[added from lecture]** Hazel elaborated on the distinction between generative world models and JEPA:

- **Generative modeling** learns a *normalized likelihood* over future frames — the model tries to assign high probability to the exact future that actually occurred. JEPA instead learns whether a predicted future is *compatible* with the current state — lower entropy, more robust to ambiguity.
- **JEPA as an energy-based model** (Yann LeCun's framing): the energy score is high when x and y are incompatible, low when they're compatible. "Compatible" means y is a plausible future of x. This sidesteps the high-entropy problem of pixel-level prediction.
- **Why no decoder in JEPA?** It's not merely an architectural choice — it's fundamental to handling uncertainty. When humans think about what happens next, they don't predict at pixel level — there are many equally valid pixel-level futures. JEPA works at the abstraction level where prediction is meaningful.

---

## V-JEPA Training Details

> **[added from lecture]** Hazel explained the regularization mechanisms in V-JEPA more explicitly:

- **EMA (Exponential Moving Average) encoder:** The target encoder is a slow-moving average of the online encoder — prevents the model from trivially collapsing by ensuring the target representation is stable and informative.
- **Stop gradient on target encoder:** The target doesn't backprop — only the predictor and online encoder train. Prevents information from leaking backward and causing collapse.
- **Masking:** Spatiotemporal masking forces the model to reason about the full context before predicting masked regions — the model can't just copy nearby pixels.

**V-JEPA 2** scales V-JEPA up and adds action-conditioned control as a post-training step. The predictor takes robot action and proprioceptive signals alongside the encoded state. Lucas Maes later clarified: this is essentially *supervised learning* on top of a frozen pretrained encoder — not fully self-supervised.

---

## The Monkey and Banana Intuition

> **[added from lecture]** Hazel used a vivid intuitive example throughout:

- If a model truly understands the mechanics of "monkey eating banana," it should be able to infer what happens to the banana when it's covered by an invisible cloth (monkey's mouth moves → banana gets smaller), and vice versa (if the banana disappears while the monkey is eating, infer the monkey ate it).
- This is what Causal-JEPA is designed to capture: **predicting what would happen under counterfactual interventions** — not just predicting the most likely future, but reasoning about causal structure.
- The monkey example also illustrates why patching (standard DINO World Model) fails: if you mask a banana patch, the model might just interpolate from neighboring patches rather than reason about the actual mechanism.

---

## Object Masking and Slot Identity

> **[added from lecture]** Hazel addressed how they handle the non-Markovian nature of object-centric representations and the challenge of masking without identity cues:

- **Problem:** Slot attention fixes the number of slots K, but the number of actual objects varies per frame. Masking only one slot may not be enough — the model can take shortcuts.
- **Solution:** Do not mask the *first time step* (frame t-3). Use it as the identity anchor for each object slot. Masked tokens are defined by their *identity token* + a learnable masked token + positional encoding.
- **Result:** The model has initial conditions for each object, making it more meaningful to predict masked tokens — it knows which object is being masked.

---

## Action Conditioning: Graph Node vs. Feature Concatenation

> **[added from lecture]** Hazel contrasted the DINO World Model's approach with Causal-JEPA's:

- **DINO World Model (concatenation):** Duplicate action embedding to match the number of patches, append after patch representation (e.g., 384-dim DINOv2-Small features + 10-dim action → 394-dim per patch). "This is not really optimal."
- **Causal-JEPA (graph node):** Treat the action as a *separate node in the causal graph*, not as an augmentation of patch features. The action gets its own representation that interacts with object representations through the predictor — more principled causal structure.

---

## C-JEPA Results: What Masking Actually Adds

> **[added from lecture]** Hazel walked through the three experiment types:

**1. CLEVRER counterfactual questions:** The biggest gain from C-JEPA vs. OC-JEPA is on *counterfactual* questions ("what if the blue cylinder didn't exist?"), not predictive ones. This directly validates the masking approach — counterfactuals require understanding object interaction, which masking forces the model to learn.

**2. Push-T planning:** 
- Replacing patch representations (196 patches × 384-dim DINOv2) with object-centric representations dramatically reduces token count and semantic density — object features are naturally lower-dimensional because they only need to capture color, shape, pose, position (not texture details).
- The OC-JEPA (object-centric without masking) actually *drops* performance vs. DINO World Model — because bidirectional transformers + static image representations lose velocity/acceleration information that the causal transformer in DINO World Model captures.
- Adding action as a graph node (+15%), then object masking (+28%) recovers and surpasses DINO World Model.

**3. Physical plausibility (PHYRE):** OC-JEPA generates physically impossible scenes (bars floating, objects passing through each other) — it learned correlations, not physics. C-JEPA with masking produces plausible scenes because it was trained to ask "what would happen if X didn't exist?" — forcing genuine dynamics learning.

---

## Attention Probing: Why C-JEPA Works Mechanically

> **[added from lecture]** Hazel showed attention probing visualizations:

- OC-JEPA fails by attending to the *wrong object* (e.g., the cup containing the blue ball, instead of the bar that actually caused the motion)
- C-JEPA correctly attends to the *relevant interacting object* for each prediction
- The predictor discovers an "influence neighborhood" — the minimal sufficient set of other objects needed to predict a given object's future state

**Causal terminology clarification:**
> "We call it temporally directed predictive dependencies — because we're predicting the future from history, the edge is directed in time. This is not the conventional causal definition, but modern causal ML uses this kind of definition too."

---

## C-JEPA Limitations

> **[added from lecture — Q&A)**:

- **Occlusion handling:** The biggest practical pain point — slot attention doesn't handle objects appearing/disappearing mid-video well. When an object is occluded, the slot representation degrades.
- **Imperfect object-centric representations:** A small degree of imperfection is tolerable — masking still provides an inductive bias even if binding isn't perfect. But severe failures in object representation cause proportional failure in causal reasoning.
- **Number of masks:** The ideal is masking exactly one foreground object per frame, but since slot count is fixed, you need to sweep based on dataset statistics.
- **True causal graph recovery:** Not possible with C-JEPA due to confounders — confounders are unavoidable in real-world object-centric representations.

---

## LeWorldModel: Lucas Maes

### The Collapse Problem and Why Existing Solutions Are Complex

> **[added from lecture]** Lucas opened by framing the problem: pure JEPA suffers from collapse — the encoder can trivially map all inputs to a constant vector (e.g., all zeros), making prediction trivially easy but useless. Preventing collapse requires auxiliary objectives.

**Existing approaches and their complexity:**
- **V-JEPA:** Uses EMA + stop gradient — two auxiliary mechanisms
- **DINO World Model:** Uses a frozen pretrained encoder — relies on external supervision
- **PLDM:** Uses VICReg (variance + covariance regularization) + inverse dynamics loss + prediction loss = **6 hyperparameter terms** to tune

> "PLDM has six terms in its loss function — six hyperparameters to tune. That's why we propose LeWorldModel."

### LeWorldModel: The Pure Essence

> **[added from lecture]** LeWorldModel uses no EMA, no stop gradient, no pretrained encoder, no masking — just JEPA in its simplest form:

1. Encode current observation (ot) and next observation (ot+1) through a shared encoder → zt, zt+1
2. Predict zt+1 from zt + action using a predictor
3. MSE between predicted and actual zt+1
4. **SIGReg** (Sketched Isotropic Gaussian Regularizer) to prevent collapse — the **only** hyperparameter

The pseudocode IS the actual code — it's that simple.

### SIGReg: Projecting to Gaussian

> **[added from lecture]** SIGReg works by:
1. Sample many random directions in latent space
2. Project all embeddings onto each direction → many 1D marginal distributions
3. Push each marginal toward Gaussian using a statistical test
4. **Cramér-Wold theorem:** If all 1D marginals are Gaussian, the joint distribution is Gaussian

> "It's a statistical test that your embedding distribution is isotropic Gaussian, without needing a generative model or KL divergence."

**Limitation discovered:** If the true intrinsic dimensionality of a task is much smaller than the embedding dimension (e.g., TwoRoom needs only x,y positions — 2D — but embeddings are high-dimensional), SIGReg forces the model to "fill up" extra dimensions with meaningless variation to maintain Gaussian marginals. This hurts performance on tasks with low intrinsic dimensionality.

### Planning Results

> **[added from lecture]** Planning is done by sampling random action sequences, rolling out futures via the world model, and gradient-based optimization of the action sequence to minimize distance to the goal state in latent space.

**Key results:**
- LeWorldModel (16M params, no proprioception) beats DINO World Model (pretrained encoder + proprioception) on **Push-T** with 50× faster planning (under 1 second vs. 47 seconds)
- Removing proprioception from DINO World Model drops its performance significantly — LeWorldModel without it still wins
- On **TwoRoom**, most baselines trivially solve it, but LeWorldModel struggles due to the SIGReg dimensionality issue — a known limitation
- On **OG-Bench Cube**, LeWorldModel beats PLDM at equal FLOP budget, but DINO World Model (pretrained on 124M natural images) still wins — real-world pretraining provides richer object/3D understanding

### Planning speed: Why LeWorldModel is 50× faster

> "[added from lecture]" DINO World Model must predict future representations for every patch (196 patches × 384-dim) — quadratic cost in the number of patches. LeWorldModel uses a single CLS token per frame → constant-time state representation. At equal FLOP budget, LeWorldModel planning success rate exceeds DINO World Model's.

### Intuitive Physics: Violations and Probing

> **[added from lecture]** Lucas tested three types of perturbations:

1. **Cube color change:** Prediction error barely increases — world model correctly ignores color (not relevant to dynamics). "Pretty cool — you don't need to model color for physics."
2. **Cube teleportation:** Prediction error spikes dramatically — the world model predicts physically continuous motion and flags the impossible event.
3. **t-SNE of embedding space:** Recovering agent + T positions from embeddings works up to axis permutation and reflection — the latent space encodes spatial structure faithfully.

**Decoder visualization:** When a decoder is trained on frozen world model predictions, gripper rotation errors appear at frames 15–20 (while cube placement is correct) — revealing that the world model didn't learn gripper rotation despite solving the task otherwise. "There are many research opportunities."

### Stable-WorldModel Library

> **[added from lecture]** Lucas briefly promoted the **Stable-WorldModel** GitHub library (stable-worldmodel on GitHub) — an open-source implementation of JEPA baselines, planners, and environments (including DeepMind Control Suite and Minecraft), heavily tested and documented, with the goal of making world model research accessible.

---

## Q&A Highlights

*Added from lecture.*

**Q: How do world models transfer to physical AI / robotics?**
> **Lucas:** "I'm very skeptical that current VLA models have good physical understanding — they're not trained to predict consequences of actions. For physical interaction, you need world models. VLA is fine for purely self-referential tasks (like robot dancing) where only internal body dynamics matter. But to interact with the world, you need to predict outcomes."

**Q: Is masking truly necessary to learn a world model?**
> **Hazel:** "Without object-centric masking, what models learn is self-dynamics — they learn what happens to an object given its own state, not how objects interact. Masking forces the model to infer from other objects. It's not strictly necessary but it strongly reinforces interaction-based dynamics."

**Q: Does C-JEPA learn to plan beyond the next frame?**
> **Hazel:** "We follow DINO World Model's evaluation protocol — autoregressive rollout of future frames for multi-step planning. Parameters are reused from the single-step predictor."

**Q: Are JEPA models less prone to hallucination than transformer-based models?**
> **Lucas:** "JEPA is a framework, not an architecture — LeWorldModel uses transformers for encoder and predictor. Hallucination in world models is fundamentally different from LLM hallucination. LLM hallucination has multiple sources: no grounding, spurious correlations, no world model. World models can address the grounding problem. But you can still have 'action hallucination' — the optimizer proposing out-of-range actions (e.g., action = −2 when valid range is [−1, 1]). That's a different failure mode."

**Q: World models vs. diffusion-based models for robot control?**
> **Hazel:** "World models can use diffusion as the prediction head. Diffusion has strengths and limitations. The future is not exclusively world model or diffusion — they can combine."

**Q: Hierarchical planning and temporal abstraction?**
> **Hazel:** "We currently operate at a single temporal level. Human planning has hierarchies — to go to the airport, you think 'go to car' → 'drive to airport' → 'muscle movements.' We need multi-level temporal abstraction. This is future work."

**Q: Combining world model planning with policy distillation?**
> **Hazel:** "Yes — once you have a world model, you can either do zero-shot planning via model predictive control, or train a policy (like Dreamer) on world model rollouts. You can also distill slow planning into a fast direct policy once you've learned the dynamics — analogous to how humans go from conscious effort to automatic behavior with practice."

---

## Papers Referenced

| Paper | Venue | Relevance |
|-------|-------|-----------|
| [Object-Centric Learning with Slot Attention](https://arxiv.org/abs/2006.15055) | NeurIPS 2020 | Slot Attention mechanism |
| [C-JEPA](https://arxiv.org/abs/2602.11389) | 2026 | Object-centric JEPA for planning |
| [LeWorldModel](https://arxiv.org/abs/2603.15569) | 2026 | Stable end-to-end JEPA from pixels |
| [A Path Towards Autonomous Machine Intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf) | 2022 | LeCun's JEPA vision |

---

## Speaker Info

**Hazel Nam (Heejeong Nam)** — First-year master's student at Brown University, working with Professor Randall Balestriero. Research on JEPA, self-supervised learning, and theory.

**Lucas Maes** — Third-year PhD student at Mila and Université de Montréal, advised by Damien Scieur, working closely with Randall Balestriero.

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
- **Video:** [▶ YouTube](https://www.youtube.com/watch?v=GBd7iuJkW08)

---

*Last updated: 2026-08-17*
