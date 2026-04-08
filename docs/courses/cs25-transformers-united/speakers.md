---
title: "Speaker Research Notes"
layout: default
parent: CS25: Transformers United V6
nav_order: 2
permalink: /courses/cs25-transformers-united/speakers/
---

# Speaker Research Notes

Pre-lecture research on each speaker, their key papers, and relevance to autonomy research.

---

## Week 2 (April 9): JEPA

### Speakers: Hazel Nam & Lucas Maes (Brown University)

**Affiliations:** Brown University, Mila, NYU collaboration with Yann LeCun

**Background:** Hazel Nam (Heejeong Nam) and Lucas Maes are working on world models and self-supervised learning under the JEPA umbrella. Their work pushes JEPA beyond patch-level representation learning toward object-centric and dynamics-aware prediction, which is exactly the direction embodied AI needs if latent world models are going to become useful for planning.

#### Recent / Relevant Papers

**C-JEPA: Learning World Models through Object-Level Latent Interventions** (ICLR 2026)
- **Why it matters:** Moves JEPA from passive masked prediction toward object-level reasoning and interaction-sensitive latent dynamics.
- **Key contribution:** Learns object-centric world models through latent interventions rather than simple reconstruction.
- **Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero
- [Project Page](https://hazel-heejeong-nam.github.io/cjepa/)

**LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels** (arXiv 2026)
- **Why it matters:** Training stability is one of the practical bottlenecks for JEPA-style systems.
- **Key contribution:** Focuses on making end-to-end JEPA training from pixels more stable and usable.
- [GitHub](https://github.com/lucas-maes/le-wm)

**A Path Towards Autonomous Machine Intelligence** (LeCun, 2022)
- **Why it matters:** Not their paper, but the clearest statement of the research program they are advancing.
- **Key contribution:** Frames JEPA as a non-generative route to world models, prediction, and planning.
- [OpenReview](https://openreview.net/pdf?id=BZ5a1r-kVsf)

#### Key Contributions and Why They Matter

- **Object-centric JEPA**: Better fit for robotics than plain patch prediction, because robots act on objects and relations, not image patches.
- **Latent intervention framing**: Suggests a path from passive perception to causal, action-relevant structure learning.
- **Training stability work**: Important because a beautiful world-model idea is not very useful if it is fragile to train end-to-end from raw pixels.
- **Alignment with LeCun's program**: Their work is among the clearest current attempts to turn JEPA from architectural thesis into something experimentally credible.

#### Relevance to Autonomy / Robotics / Embodied AI

| Aspect | Relevance |
|--------|-----------|
| **Latent prediction** | More sample-efficient than pixel reconstruction, which matters for real robot data collection |
| **Object-centric structure** | Better match for manipulation, navigation, and scene interaction |
| **World models** | Could support planning in latent space rather than model-free behavior cloning only |
| **Causal interventions** | Important for action-conditioned prediction and controllable behavior |
| **Training stability** | Necessary for scaling world models from toy domains to robot-relevant environments |
| **Alternative to autoregression** | Offers a different path than next-token prediction for embodied intelligence |

#### Question Bank

1. What failure mode in JEPA training worries you most today, collapse, underfitting, or learning the wrong invariances?
2. How does C-JEPA's object discovery compare with Slot Attention or other object-centric baselines in cluttered scenes?
3. What evidence suggests C-JEPA latents are actually useful for planning rather than just representation benchmarks?
4. Do your current models incorporate action conditioning, or is that still the missing bridge to robotics control?
5. How do you think JEPA compares to diffusion-based world models for long-horizon robot planning?
6. What is the right evaluation benchmark for JEPA if the end goal is embodied intelligence rather than image understanding?
7. Can these methods generalize to novel objects and contact-rich manipulation, or are they still mostly clean-domain learners?
8. Which part of LeWorldModel was most important for stability, architecture, objective design, or optimization details?
9. If you had robot interaction data instead of passive video, what would you change first in the JEPA setup?
10. How close is current C-JEPA work to the broader autonomous machine intelligence agenda LeCun describes?

#### Cross-Links

- Related session: [Pre-Read: JEPA & World Models](sessions/2026-04-09-jepa/pre-read)
- Related theme: [World Models & Embodiment](themes)
- Forward link: Week 3 SSMs, useful contrast for long-horizon memory and efficient sequence modeling

---

*Last updated: 2026-04-08*
