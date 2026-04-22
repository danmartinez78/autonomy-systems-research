---
title: "Pre-Read: Ultra-Scale Training"
layout: default
parent: Session 4: Ultra-Scale Training
nav_exclude: true
---

# Pre-Read: Ultra-Scale Training — Nouamane Tazi

**Date:** April 23, 2026
**Topic:** Scaling Training to Thousands of GPUs
**Speaker:** Nouamane Tazi (Hugging Face)
**Slides:** Slides not yet posted — check course site Thursday

---

## Speaker Bio

**Nouamane Tazi** is a research engineer at Hugging Face and contributor to the BigCode project. He's known for work on efficient training, code generation models (StarCoder), and small language models (SmolLM3). His current focus is on the infrastructure and systems work required to train and deploy large models at scale.

**Key affiliations:**
- Hugging Face (research engineer)
- BigCode project contributor

---

## Topic: Ultra-Scale Training

The topic is about **scaling training infrastructure** — how to efficiently train models across thousands of GPUs. This covers:
- Distributed training strategies
- Pipeline and tensor parallelism
- Memory optimization (gradient checkpointing, ZeRO)
- Hardware topology and network bottlenecks
- Training stability at scale

---

## Research: Nouamane Tazi's Recent Work

### 1. StarCoder 2 (BigCode, 2024)
**arXiv:** [2402.19173](https://arxiv.org/abs/2402.19173)

**Contribution:** Family of open-source code generation LLMs (StarCoder 2-3B/7B/15B) trained on The Stack v2 dataset.

**Key details:**
- Trained on permissively-licensed code from 300+ languages
- Context window: 8192 tokens
- Competitive with proprietary code models on HumanEval

---

### 2. SmolLM3 (Hugging Face, 2025)
**Blog:** [huggingface.co/blog/smollm3](https://huggingface.co/blog/smollm3)

**Contribution:** Small (135M/360M/1.7B parameters), multilingual, long-context reasoner demonstrating efficiency techniques.

**Key details:**
- Uses speculative decoding for fast inference
- Focus on quality per parameter — small but capable
- Long context (8K-32K) in small footprint

---

### 3. Layer Normalization Research (2025)
**Paper:** Understanding Layer Normalization in Transformers

**Contribution:** Discovered tanh-like S-shaped curves in transformer input-output mappings — shows that transformers have structured internal representations that emerge from training.

**Relevance:** Understanding this could help with training stability and model interpretability.

---

### 4. GPU Memory Prediction for MoE Models (2025)
**Paper:** Predicting GPU Memory Usage for Mixture-of-Experts Models

**Contribution:** Infrastructure work predicting GPU memory requirements for MoE models during training — critical for planning resource allocation.

---

## Key Contributions & Why They Matter

| Contribution | Why It Matters |
|--------------|----------------|
| **StarCoder 2** | Demonstrated that open code models can match proprietary. Foundation for code generation research. |
| **SmolLM3** | Shows small models can still be capable. Important for edge/robotics deployment. |
| **Layer norm insights** | Understanding transformer internals helps with debugging and optimization. |
| **GPU memory prediction** | Practical infrastructure work that makes large-scale training more predictable. |

---

## Relevance to Autonomy / Robotics

| Aspect | Relevance |
|--------|-----------|
| **Training infrastructure** | Training autonomous models requires similar infrastructure |
| **Edge deployment** | SmolLM3's efficiency techniques translate to robotics edge deployment |
| **MoE for robotics** | Mixture-of-experts could enable specialized sub-models for different robot tasks |
| **Memory efficiency** | Critical for onboard GPU systems with limited VRAM |
| **Speculative decoding** | Fast inference for real-time robot responses |

---

## Key Insights to Listen For

Based on Nouamane's work and topic:

1. **Distributed training bottlenecks** — Where do bottlenecks typically occur? (communication, memory, compute)
2. **Pipeline parallelism strategies** — How to partition model across GPUs efficiently
3. **Memory optimization techniques** — ZeRO, gradient checkpointing, mixed precision
4. **Training stability at scale** — What breaks when you scale, and how to fix it
5. **MoE infrastructure** — How Hugging Face handles mixture-of-experts training

---

## Papers Referenced in Talk

*To be populated after lecture / when slides are posted.*

---

## Question Bank

### Technical Questions

1. **What are the main bottlenecks when scaling to thousands of GPUs?**
   - Is it communication bandwidth? Memory? Compute? Need to know where the pinch points are.

2. **How does pipeline parallelism interact with transformer architecture?**
   - Different strategies (FSDP, DeepSpeed, Megatron) have different tradeoffs. What works best?

3. **What's your approach to training stability at extreme scale?**
   - Loss spikes, gradient explosion, NaN issues — how do you diagnose and fix?

4. **How does speculative decoding work in practice, and what's the quality/speed tradeoff?**
   - Relevant for robotics: fast inference is critical.

5. **What memory optimization techniques are most impactful?**
   - Gradient checkpointing, ZeRO stages, quantization — what's the priority order?

### Infrastructure Questions

6. **How do you handle GPU failures during training?**
   - Thousands of GPUs, failures are inevitable. Checkpoint strategy?

7. **What's the role of network topology in distributed training?**
   - InfiniBand vs RoCE vs Ethernet — does it matter for training efficiency?

8. **How do you profile and debug training performance?**
   - What tools/metrics do you use to find bottlenecks?

### Robotics/Autonomy Questions

9. **How do these large-scale training techniques transfer to robot-specific training?**
   - RL training, behavior cloning, world model training — different from language?

10. **SmolLM3 shows small models can be capable. What's the path to truly capable edge models for robotics?**
    - Can we get robot-capable models in 1-3B parameter range?

11. **MoE seems promising for robotics — specialized experts for navigation, manipulation, language. Any plans in that direction?**
    - Practical question about whether HF is exploring robotics-specific MoE.

### Research Philosophy Questions

12. **What's surprised you most about transformer training behavior at scale?**
    - Curious about unexpected findings from the layer normalization work.

13. **Open or closed models for code generation — what's your take on the future?**
    - BigCode vs Codex/GitHub Copilot — where is the field heading?

---

## Cross-References

- **Week 3 (SSMs):** Mamba's efficient inference is relevant to the efficiency discussion
- **Week 10 (Modal):** Serverless GPU deployment — complementary infrastructure topic
- **Related research:** PEFT methods (LoRA, QLoRA) for fine-tuning at scale

---

## Slide Link

*Slides not yet posted. Check [course schedule](https://web.stanford.edu/class/cs25/schedule) Thursday for updates.*

---

## Session Summary

*To be filled in after lecture.*

---

*Last updated: 2026-04-22*
