---
title: "Pre-Read: The Future of Pretraining"
layout: default
parent: Session 5: The Future of Pretraining
nav_exclude: true
---

# Pre-Read: The Future of Pretraining

**Date:** April 30, 2026
**Speaker:** Shrimai Prabhumoye (Mistral AI, previously NVIDIA)
**Topic:** From Next-Token Prediction to Next-Generation Intelligence: The Future of Pretraining
**Slides:** [Course slide deck](https://drive.google.com/open?id=1dxdC76Rk_o6UEd5AqhHjp0rapsxYOR6j&usp=drive_fs)

---

## Topic Overview

The course description frames this session around three levers for shaping future model capability during pretraining:

1. **Data ordering and sequencing**
2. **Reasoning-rich data earlier in training**
3. **Reinforcement-style objectives during pretraining**

That combination matters because it treats reasoning as a first-class training objective instead of a post-training garnish.

---

## Speaker Context

Shrimai Prabhumoye works on large-model pretraining and reasoning at Mistral AI, after prior work at NVIDIA. The announced talk lines up with her background in data curation, curriculum design, and scaling foundation-model training.

---

## Why It Matters for Autonomy

- Pretraining choices may determine whether downstream robot policies learn robust abstractions or brittle shortcuts.
- Reasoning-heavy curricula connect directly to long-horizon planning and failure recovery.
- Reinforcement during pretraining blurs the line between "world knowledge" and "behavior shaping."

---

## Questions To Bring

1. Which gains from reasoning-rich pretraining survive strong post-training?
2. How do you tell whether data ordering is helping causal reasoning versus benchmark mimicry?
3. Does reinforcement during pretraining help multimodal or action-conditioned models yet?
4. What parts of this recipe look plausible for smaller edge-deployable models?

---

*Created: 2026-06-18 from the live Stanford course description*
