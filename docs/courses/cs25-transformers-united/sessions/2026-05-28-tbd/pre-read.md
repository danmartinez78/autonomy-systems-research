---
title: "Pre-Read: TBD Topic"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: TBD Topic

**Date:** May 28, 2026
**Speaker:** Charles Frye (Modal)

---

## Topic Overview

Topic TBD — check course site for updates. Speaker focuses on serverless GPU infrastructure, CUDA Python, and practical ML deployment.

---

## Key Concepts

Awaiting topic announcement.

---

## Speaker

### Charles Frye

**Affiliation:** Modal (AI Engineer)

**Background:** PhD from UC Berkeley (psychology/cognitive science), now focused on practical ML infrastructure and GPU computing. Creator of educational content including the GPU Glossary.

**Key contributions:**

- **Modal platform** — Serverless GPU infrastructure for GenAI workloads
- **GPU Glossary** — Educational resource on GPU architecture
- **CUDA Python advocacy** — Year of CUDA Python (GTC 2025 coverage)
- **Distributed inference patterns** — Practical deployment knowledge

---

## Resources

### 1. Modal Platform

**What it is:** Serverless GPU platform for running GenAI models without managing infrastructure.

**Key features:**
- Pay-per-use GPU compute
- Auto-scaling from 0 to hundreds of GPUs
- Built-in distributed inference support

🔗 [Modal docs](https://modal.com/docs)

---

### 2. GPU Glossary

**What it is:** Educational content explaining GPU architecture, CUDA concepts, and performance optimization.

**Topics covered:**
- Memory hierarchy (HBM, L2 cache, shared memory)
- Kernel optimization
- Tensor cores and matrix operations
- Multi-GPU communication (NVLink, PCIe)

🔗 [GPU Glossary](https://modal.com/gpu-glossary)

---

### 3. CUDA Python Coverage

**What it is:** Podcast and blog coverage of NVIDIA's CUDA Python initiative (GTC 2025).

**Topics covered:**
- Tensor memory accelerators
- Python-native GPU programming
- Performance comparisons

🔗 [Podcast](https://podcasts.apple.com/ky/podcast/034-the-year-of-cuda-python-nvidia-gtc-2025-recap/id1493295799?i=1000700913657)

---

## Why It Matters for Autonomy

| Aspect | Relevance to Robotics/Embodied AI |
|--------|-----------------------------------|
| **Deployment infrastructure** | Serverless GPU for on-demand autonomy workloads — burst compute for planning/inference |
| **Practical ML systems** | Real-world deployment patterns that go beyond toy examples |
| **Cost efficiency** | Running inference without managing hardware — relevant for fleet deployment |
| **Edge-cloud hybrid** | Understanding when to use cloud GPU vs edge deployment |
| **GPU optimization** | Making models run faster on constrained hardware |

---

## Question Bank

### Infrastructure Questions

1. What's the break-even point where serverless GPU becomes more expensive than dedicated hardware?
2. How does Modal handle cold starts for latency-sensitive autonomy workloads?
3. What are the patterns for hybrid edge-cloud inference?

### Optimization Questions

4. What are the most impactful GPU optimizations for transformer inference?
5. How much performance gain is realistic from CUDA kernel optimization vs just using better libraries?
6. What's the state of CUDA Python for production workloads vs C++?

### Deployment Questions

7. How do you handle model versioning and rollback in serverless GPU deployments?
8. What monitoring/observability patterns work best for GPU workloads?
9. How does Modal handle multi-GPU inference (tensor parallelism, pipeline parallelism)?

---

## Pre-Lecture Reading

### Essential
- [Modal GPU Glossary](https://modal.com/gpu-glossary) — quick reference
- [Modal docs](https://modal.com/docs) — platform overview

### Background
- [CUDA Python GTC 2025 recap podcast](https://podcasts.apple.com/ky/podcast/034-the-year-of-cuda-python-nvidia-gtc-2025-recap/id1493295799?i=1000700913657)
- [Modal blog](https://modal.com/blog)

---

## Cross-References

*To be populated once topic is announced.*

---

*Prepared: 2026-04-04 • Topic TBD*
