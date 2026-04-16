---
title: "Session 2: JEPA & World Models — Slides"
layout: default
parent: CS25: Transformers United V6
nav_order: 2
nav_exclude: true
permalink: /courses/cs25-transformers-united/sessions/2026-04-09-jepa/slides/
---

# Session 2: JEPA & World Models — Slides

*Source: [JEPA_cs25.pdf](https://drive.google.com/file/d/1bF5Yfzf-FG5iNIAgsXn2DwVD3l3ymvZW/view) (accessed 2026-04-16)*

---

## Slide 1–2: Title & Outline

**Title:** Joint Embedding Predictive World Models
**Authors:** Heejeong Nam, Lucas Maes (Stanford CS25)

**Outline:**
1. Concepts of JEPA and World Models
2. How to make a model understand object interaction
3. How to train JEPA end-to-end without collapse

---

## Slide 3: What is a World Model?

**Diagram:** World Model block with inputs `x` (current state), `a` (action) and output `x'` (next state).

Three properties of a good world model:
1. **Good State Representation** — compact, informative encoding of the environment
2. **Good Transition Model** — predicts `x → x'` given action `a`
3. **Good Dynamics Model** — captures how the world responds to your actions

**Purpose:** Act as a *simulator* of the environment for planning, imagination, or policy learning.

*(Note: Generative world models (Sora, Gaia) explicitly marked as out of scope)*

---

## Slide 4–5: JEPA → V-JEPA Progression

- **V-JEPA** — Video-Joint Embedding Predictive Architecture (Bardes et al., 2024)
- **V-JEPA 2** — Next-generation V-JEPA (Assran et al., 2025)

**Architecture (V-JEPA):**
```
frozen DINOv2 encoder → predictor → [Auxiliary Variables ℒ!]
History Frames: t, t-1, t-2, t-3 → Future Frame: t+1
(frames are patch representations)
```

**Key detail:** frozen DINOv2 encoder — the visual encoder is frozen during JEPA training, only the predictor is trained.

---

## Slide 6: Autoregressive DINO-WM

- **Autoregressive DINO-WM** (Zhou et al., 2024) — patch-based world model baseline

Architecture mirrors V-JEPA but uses an autoregressive predictor instead of latent prediction:
- Same frozen DINOv2 encoder
- AR predictor with auxiliary variables ℒ!
- Patch-level representation (not object-centric)

---

## Slide 7: Causal-JEPA

**Title:** Causal-JEPA: Learning World Models through Object-Level Latent Interventions

**Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero

**Collaborators / benchmarks:** Push-T, CLEVRER, PHYRE

**Goal:** Object-level latent interventions — mask and predict at the object/slot level rather than patch level.

*(The index.md covers C-JEPA in detail — see the object-centric representation section.)*

---

## Slide 8: Patch-Based vs Object-Centric

**Patch-Based (DINO-WM):**
- Patch representation from frozen DINOv2 encoder
- History: t, t-1, t-2, t-3 → Future: t+1
- Each frame is a grid of patch tokens

**Object-Centric (OC-DINO-WM):**
- Object representation from object-centric encoder
- Same temporal structure but objects replace patches as the representational unit
- The object-centric encoder groups patches into coherent object slots

*(The index.md covers the distinction between these in detail — see "Two Ways to Represent a Scene.")*

---

## Slide 9: Object-Centric Learning

**Reference:** Object-Centric Learning with Slot Attention (Locatello et al., NeurIPS 2020)

**Image credit:** nano banana (presumably an illustration source for slot attention diagrams)

*(The index.md covers Slot Attention in detail — see the Slot Attention section.)*

---

## Slide 10: Temporal Frame Ordering

**Timeline shown:**
```
t-2  t-1  t  t-3  t+1
```

*Note: The ordering t-3, t-2, t-1 is "history," t is "current," t+1 is "future." The slide shows t appearing between t-1 and t-3, suggesting a different visualization than strict chronological order.*

---

## Key Takeaways from Slides

| Slide | Key Addition |
|-------|-------------|
| V-JEPA → V-JEPA 2 | Named progression; V-JEPA 2 is the 2025 follow-on |
| AR DINO-WM | Explicit patch-based baseline to compare against OC variants |
| C-JEPA author list | Full author list + benchmark names (Push-T, CLEVRER, PHYRE) |
| OC-DINO-WM | Object-centric extension of DINO-WM; the target architecture for C-JEPA |
| Temporal ordering | Confirms multi-frame temporal structure (4 history frames → 1 future) |
| Slide credit | "nano banana" — presumably an open-source visualization used in slot attention figures |

---

*Slide extraction: 2026-04-16. Video synthesis still pending — expected ~April 30.*
