---
title: "Themes & Connections"
layout: default
parent: CS25: Transformers United V6
nav_order: 99
permalink: /courses/cs25-transformers-united/themes/
has_toc: false
---

# Themes & Connections

Cross-lecture patterns and connections emerging across the course.

---

## Current Themes

*Tracking major themes as the course progresses.*

### Efficiency & Scaling
- **Linear-time alternatives** to O(n²) attention (SSMs, state space models)
- **Model compression** — Smaller models for edge deployment
- **Long-context** — Extending context windows beyond training sequences

### World Models & Embodiment
- **JEPA architectures** — Learning by prediction, not reconstruction
- **Object-centric representations** — Scene understanding for embodied AI
- **Simulation** — Training world models without real robots

### Interpretability & Control
- **Mechanistic interpretability** — Understanding how models reason
- **Circuit analysis** — Mapping model computations to interpretable concepts
- **Steering** — Controlling model behavior explicitly

### Multimodality & Integration
- **Vision-language models** — Combining visual and text understanding
- **Robotics applications** — Transformers for control, planning, perception
- **Code generation** — Program synthesis, program understanding

---

## Cross-Lecture Connections

*Speakers whose work spans multiple themes*

### Albert Gu (Week 3: SSMs)
- **Efficiency** — Mamba's primary contribution
- **Long-context** — 100K+ context windows
- **Connections to:** JEPA world models (Week 2), Modal deployment (Week 10)

### Vivek Natarajan (Week 7: Med-PaLM)
- **Safety-critical validation** patterns
- **Domain adaptation** — Transfer learning across domains
- **Multimodal** — Text + medical imaging

### Andrew Lampinen (Week 6: Interpretability)
- **Efficiency** — Puzzle framework for efficient transformers
- **Interpretability** — Attribution graphs, understanding reasoning
- **Control** — Block importance for steering generation

### Charles Frye (Week 10)
- **Efficiency** — Serverless GPU for inference
- **Deployment** — Infrastructure patterns for autonomous systems
- **Multimodal** — Video + language + sensor fusion

---

## Relevance to Autonomy Research

| Theme | Relevance | Key Lectures |
|-------|-----------|--------------|
| **World Models** | Essential for embodied AI | JEPA (Week 2), Simulation |
| **Efficiency** | Edge deployment, real-time control | SSMs (Week 3), Puzzle (Week 6), Modal (Week 10) |
| **Interpretability** | Trustworthy decision-making | Lampinen (Week 6) |
| **Safety-Critical** | Validation patterns for high-stakes domains | Med-PaLM (Week 7) |
| **Multimodal** | Sensor fusion for robotics | Frye (Week 10), Vision-Language |

---

*Last updated: 2026-04-04*
