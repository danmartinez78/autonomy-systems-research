---
title: "Pre-Read: TBD Topic"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: TBD Topic

**Date:** May 14, 2026
**Speaker:** Vivek Natarajan (DeepMind)

---

## Topic Overview

Topic TBD — check course site for updates. Speaker leads AI × Science × Medicine research at Google DeepMind, with focus on medical AI systems.

---

## Key Concepts

Awaiting topic announcement.

---

## Speaker

### Vivek Natarajan

**Affiliation:** Google DeepMind, Research Lead for AI × Science × Medicine

**Background:** Leading researcher in applying transformers to healthcare. 18,300+ citations. Focus on making AI reliable in safety-critical medical domains.

**Key contributions:**

- **Med-PaLM** — First AI to pass US Medical License Exam
- **Med-PaLM 2** — Expert-level scores on medical benchmarks
- **Medical AI validation frameworks** — Patterns for deploying AI in high-stakes domains

---

## Papers

### 1. Med-PaLM: Large Language Models Encode Medical Knowledge (Nature, 2023)

**Contribution:** First AI system to pass the US Medical Licensing Examination.

**Key insight:** Scaling + medical domain fine-tuning enables expert-level medical reasoning.

**Result:** 67.6% accuracy on USMLE (passing threshold: ~60%).

🔗 [Nature paper](https://www.nature.com/articles/s41586-023-06291-2)

---

### 2. Med-PaLM 2: Towards Expert-Level Medical AI (Nature Medicine, 2025)

**Contribution:** Improved architecture and training, achieving expert-level scores.

**Key insight:** Instruction fine-tuning + medical reasoning chains improve performance.

**Result:** 86.5% accuracy on USMLE (expert doctors: ~87%).

🔗 [Nature Medicine paper](https://www.nature.com/articles/s41591-024-03417-8)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Safety-critical deployment** | Medical AI is the gold standard for high-stakes domains — patterns transfer to autonomous systems |
| **Validation patterns** | How to make transformers reliable in critical applications — testing, uncertainty quantification |
| **Domain-specific fine-tuning** | Relevant to specialized autonomy applications (industrial, defense, space) |
| **Human-AI collaboration** | Medical AI interfaces provide patterns for human-in-the-loop autonomy |

---

## Question Bank

### Validation/Safety Questions

1. What validation approaches from Med-PaLM translate to robotics/autonomy?
2. How do you quantify uncertainty in medical diagnoses? Does that translate to action selection?
3. What's the process for detecting out-of-distribution inputs in medical settings?

### Domain Adaptation Questions

4. How much medical knowledge is in the base LLM vs added through fine-tuning?
5. What's the minimal dataset size for reliable domain adaptation?
6. How do you handle edge cases where medical consensus is unclear?

### Autonomy Transfer Questions

7. Are there medical AI safety patterns that apply directly to autonomous vehicle decision-making?
8. How do you balance model confidence with appropriate caution in high-stakes settings?
9. What's the role of human oversight in Med-PaLM deployment? How might that translate to autonomous systems?

---

## Pre-Lecture Reading

### Essential
- [Google Research profile](https://research.google/people/106654/)
- [Med-PaLM paper summary](https://www.nature.com/articles/s41586-023-06291-2)

### Background
- [Med-PaLM 2 paper](https://www.nature.com/articles/s41591-024-03417-8)
- [Google Health AI research](https://health.google/health-research/)

---

## Cross-References

*To be populated once topic is announced.*

---

*Prepared: 2026-04-04 • Topic TBD*
