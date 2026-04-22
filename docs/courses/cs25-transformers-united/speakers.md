# CS25: Speaker Research — Albert Gu (CMU)

**Week 3 | April 16, 2026 | State Space Models & Mamba**

---

## Speaker Bio

**Albert Gu** is a researcher at Carnegie Mellon University and co-creator of Mamba, the leading selective State Space Model (SSM). He completed his PhD at Stanford under Chris Ré, where he pioneered structured state space models for efficient sequence modeling. His work has fundamentally changed how we think about long-context sequence processing, offering O(n) complexity as an alternative to transformer's O(n²) attention.

**Key affiliations:**
- Carnegie Mellon University (current)
- Stanford PhD (under Chris Ré)
- State Spaces lab / Mamba development team

---

## Key Papers

### 1. Mamba: Linear-Time Sequence Modeling with Selective State Spaces (2023)
**arXiv:** [2312.00752](https://arxiv.org/abs/2312.00752)

**Contribution:** First practical SSM with content-dependent state transitions.

**Key innovation:** Selective mechanism allows the model to choose what to remember based on input content — not just what the architecture forces it to remember.

**Impact:** Enabled 100K+ context windows with linear scaling. O(n) complexity vs O(n²) for attention.

🔗 [GitHub](https://github.com/state-spaces/mamba)

---

### 2. Mamba-2: Transformers are SSMs: Generalized Models and Efficient Algorithms (ICML 2024)
**arXiv:** [2405.21060](https://arxiv.org/abs/2405.21060)

**Contribution:** State Space Duality (SSD) framework — mathematical equivalence between SSMs and transformer attention variants.

**Key innovation:** 2-8X speed improvement over Mamba-1. Shows that many attention variants can be reformulated as SSMs.

**Impact:** Bridges two major architecture families. Enables cross-pollination of techniques.

---

### 3. Mamba-3: Improved Sequence Modeling using State Space Principles (2026)
**arXiv:** [2603.15569](https://arxiv.org/abs/2603.15569)

**Contribution:** Latest iteration with architectural improvements and further quality/efficiency gains.

**Note:** Pre-read prepared before paper details were fully public. Expect significant updates post-lecture.

---

## Why It Matters for Autonomy / Robotics

| Aspect | Relevance |
|--------|-----------|
| **Long-horizon memory** | 100K+ context enables multi-session recall — persistent autonomy |
| **Efficient inference** | Linear scaling makes edge deployment feasible on constrained hardware |
| **Real-time processing** | No KV-cache explosion — sustained performance over long missions |
| **Streaming sensor data** | Natural fit for continuous sensor streams in robotics |
| **Alternative to attention** | Critical for long-horizon tasks where transformer context limits bite |

---

## Question Bank

### Technical Questions

1. **How does selective SSM compare to linear attention variants like Performer or Linformer in practice?**
   - Selective SSM has content-dependent dynamics; linear attention variants don't. This likely matters for tasks requiring selective focus.

2. **What's the memory/quality tradeoff when reducing state dimension?**
   - Mamba's state dimension directly affects memory usage and expressiveness. Understanding this tradeoff is critical for deployment.

3. **How does Mamba handle structured vs unstructured data (code vs natural language)?**
   - SSMs were originally designed for audio/signals. How does the inductive bias transfer to discrete tokens?

4. **Are there tasks where Mamba underperforms transformers significantly?**
   - Need to know failure modes for honest evaluation.

5. **How does Mamba-3 improve over Mamba-2 specifically?**
   - Architectural changes, quality gains, efficiency improvements.

### Robotics/Autonomy Questions

6. **Have you tested Mamba on multimodal sensor fusion (vision + proprioception + language)?**
   - Most Mamba benchmarks are language/audio. Robotics requires multimodal handling.

7. **How might SSMs handle irregularly-sampled sensor data (common in robotics)?**
   - Robotics sensors sample at different rates. Does SSM handle this gracefully?

8. **Is there work on action-conditioned SSMs for control?**
   - SSM for control (like RSSM in Dreamer) — is there existing work or plans?

9. **How does Mamba compare to transformers for offline RL / behavior cloning?**
   - Efficient inference matters for RL training loops. Worth asking.

10. **What's the minimum hardware to run Mamba-3 efficiently? Edge deployment story?**
    - RTX 3080? Jetson? This is critical for robotics deployment.

### Research Direction Questions

11. **Is the transformer-SSM equivalence practical for model conversion, or mostly theoretical?**
    - Can we take a trained transformer and convert it to SSM? That would be huge.

12. **What's the path to 1M+ context windows? Are there fundamental limits?**
    - Current SSMs hit bottlenecks around 100K-1M. What changes are needed?

---

## Cross-References

- **Week 2 (JEPA):** World models for planning — complementary to long-context SSMs
- **Week 4 (Hugging Face):** Infrastructure for scaling — deployment patterns
- **Week 10 (Modal):** Serverless GPU — efficient inference deployment

---

## Related Reading

- [Mamba GitHub](https://github.com/state-spaces/mamba)
- [Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/)
- [Mamba Wikipedia](https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture))
- [S4 (Foundational SSM)](https://arxiv.org/abs/2111.00396)
- [Hungry Hungry Hippos (SSM for language)](https://arxiv.org/abs/2212.14052)

---

*Research prepared: 2026-04-15*

---

# CS25: Speaker Research — Nouamane Tazi (Hugging Face)

**Week 4 | April 23, 2026 | Ultra-Scale Talk: Scaling Training to Thousands of GPUs**

---

## Speaker Bio

**Nouamane Tazi** is a research engineer at Hugging Face and contributor to the BigCode project. He's known for work on efficient training, code generation models (StarCoder), and small language models (SmolLM3). His current focus is on the infrastructure and systems work required to train and deploy large models at scale.

**Key affiliations:**
- Hugging Face (research engineer)
- BigCode project contributor

---

## Key Papers

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

## Why It Matters for Autonomy / Robotics

| Aspect | Relevance |
|--------|-----------|
| **Training infrastructure** | Training autonomous models requires similar infrastructure |
| **Edge deployment** | SmolLM3's efficiency techniques translate to robotics edge deployment |
| **MoE for robotics** | Mixture-of-experts could enable specialized sub-models for different robot tasks |
| **Memory efficiency** | Critical for onboard GPU systems with limited VRAM |
| **Speculative decoding** | Fast inference for real-time robot responses |

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

- **Week 3 (SSMs - Albert Gu):** Mamba's efficient inference is relevant to the efficiency discussion
- **Week 10 (Modal - Charles Frye):** Serverless GPU deployment — complementary infrastructure topic
- **Related research:** PEFT methods (LoRA, QLoRA) for fine-tuning at scale

---

## Related Reading

- [Nouamane's Hugging Face profile](https://huggingface.co/nouamanetazi)
- [SmolLM3 blog](https://huggingface.co/blog/smollm3)
- [StarCoder 2 paper](https://arxiv.org/abs/2402.19173)

---

*Research prepared: 2026-04-22*
