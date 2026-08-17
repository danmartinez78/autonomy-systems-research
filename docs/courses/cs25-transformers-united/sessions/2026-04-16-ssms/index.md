---
title: "Session 3: State Space Models & Mamba"
layout: default
parent: CS25: Transformers United V6
nav_order: 3
permalink: /courses/cs25-transformers-united/sessions/2026-04-16-ssms/
date: 2026-04-16
---

# Session 3: State Space Models & Mamba

**Date:** April 16, 2026
**Speaker:** Albert Gu (CMU, Cartesia AI)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=OyimE74UMF8)
**Status:** ✅ Enriched with lecture content

---

## Talk Description

State Space Models (SSMs) offer an alternative to attention-based transformers with O(n) complexity instead of O(n²). Albert Gu's Mamba architecture has emerged as the leading SSM, enabling 100K+ context windows and efficient inference. This lecture covers the evolution from S4 to Mamba-3 and their implications for long-horizon reasoning.

---

## Personal Framing

> **[added from lecture]** Albert opened with a personal note: "Good to be back. I haven't been back on campus in a while, even though it's only been two years since I graduated." He gave a disclaimer that this talk overlaps significantly with his blog post version, with a little new content — setting expectations accordingly.

---

## SSM Taxonomy: What to Call These Models

> **[added from lecture]** Albert acknowledged the confusing naming landscape and unified the terminology for the talk:

| Term | What it refers to |
|------|-----------------|
| **State-space models (SSMs)** | The umbrella term used in this talk |
| **Linear attention** | A related lineage of work |
| **Modern recurrent models** | vs. older RNNs like LSTMs |
| **Linear RNNs** | Another name |
| **Linear models** | Most generic term |
| **Hybrid models** | Any of the above + quadratic attention |

> "Usually these days when people say any of these words, it broadly refers to any of these models."

---

## The Current Model Zoo

> **[added from lecture]** Albert listed production-grade models using these architectures:

- **Mamba** (original, 2023), **Mamba-2**, **Mamba-3** (just published a month ago)
- **xLSTM** — Hochreiter group's modern LSTM revival
- **DeltaNet / Gated DeltaNet** — combines DeltaNet with Mamba-2; most widely used hybrid variant
- **Jamba** (AI21), **Zamba** (Zyphra), **Samba** (Microsoft)
- **Hunyuan** (Tencent) — several hundred billion parameters, hybrid
- **Qwen** (latest versions) — now based on Gated DeltaNet
- **Kimi-Linear** — hybrid, based on follow-up DeltaNet
- **AI2's Olmo** — hybrid, Gated DeltaNet + attention
- **Nemotron-3** (NVIDIA) — hundreds of billions of parameters, uses Mamba-2
- **Test-Time Training** — treats recurrence as test-time weight updates optimizing an objective

---

## The Core Architectural Tradeoff: KV Cache vs. Compressed State

> **[added from lecture]** Albert's central framing:

**Transformers = database:** The KV cache stores every past token exactly. Query = exact retrieval of everything seen. Memory grows O(n) with context; compute grows quadratically because each new token attends to the full KV cache.

**SSMs = brain:** Fixed-size state (a compressed "ball") summarizes all previous tokens. Individual tokens are "thrown away" — the model only interacts with data through the state. Every inference step takes constant time; total generation scales linearly.

> "I think of transformers as the canonical model that caches every past token. Because it needs to cache every token to do these comparisons... At an even higher level, a transformer is just a model that stores this cache."

**Key consequence:** SSMs are O(n) in both training AND inference. Transformers are O(n) in inference storage (KV cache) but O(n²) in compute per generation step. SSM constant compute per token means generating token 100 costs the same as token 100,000.

---

## The Three Ingredients That Made Mamba Work

> **[added from lecture]** Albert gave the canonical explanation of why Mamba succeeded where earlier linear RNNs failed:

**Ingredient 1: Large state size**
- Classic RNNs had hidden state roughly the same size as the input
- SSMs: input is a scalar, hidden state is N-dimensional (N = 64–128, so 100× larger than input)
- The state is the bottleneck of context — larger state = more information the model can remember
- Critical for information-dense modalities like language

**Ingredient 2: Selectivity (input-dependent parameters)**
- Parameters A, B (in the SSM recurrence) are *functions of the input*, not fixed matrices
- This lets the model decide: "do I want to remember this input, or throw it away?"
- If the input says "ignore me": set A=1, B=0 (keep prior state, discard input)
- If the input says "remember me": set A=0 (overwrite with new input)
- Called "selectivity" — the model can actively control what information persists
- Different from LSTMs' gating (which was fixed functions of input) — SSM selectivity is a learned function of input

**Ingredient 3: Efficient computation via associative scan**
- Linear recurrence + large state = exponentially harder to compute naively
- Mamba rewrites the computation using associative scan (parallel prefix sum), exploiting linearity
- Mamba-2 and Gated DeltaNet use chunked matrix multiplication for the same purpose
- 2–8× speedup over naive recurrent computation

**Historical note:**
> "All three ingredients existed prior to Mamba. Linear attention (2020) had state size expansion. GRUs/LSTMs had gating. Many models exploited efficient computation. Mamba was the first to *combine all three* — and that was critical."

---

## Why SSMs Struggle at Retrieval

> **[added from lecture]** Albert was direct about the fundamental weakness:

> "SSMs are not good at retrieval. Because they compress state, they lose access to exact token information. This is exactly how brains work — humans are notoriously bad at remembering exact strings of numbers."

**Haystack / associative recall tasks:** Models must find a specific fact buried in context. SSMs compress it and can't recover the exact detail. The human analogy: you know the concept of "telephone" but not the specific conversation you had about it three weeks ago.

**Tradeoff:** Transformers preserve everything (lossless, expensive). SSMs compress (lossy, efficient). Neither is universally better.

---

## The Brain + Tools Analogy: Hybrid Models

> **[added from lecture]** The SSM weakness suggests the hybrid solution:

> "Humans don't just use their brain — we use external tools, databases, calculators. Intelligence = brain + scratchpads. This is the high-level inspiration for hybrid models."

**Optimal hybrid ratio:** Multiple labs independently converged on ~**10:1 SSM layers to attention layers** (from a perplexity standpoint). Current practice settles around 3:1–4:1 as models improve.

> "We tend to think of the brain as the main processing unit and external databases as supplements. The fact that ablations confirm you want more linear layers than quadratic — this is interesting that it follows the analogy."

---

## Transformers and Tokenization: The Hidden Dependency

> **[added from lecture]** Albert's central critique of transformer triumphalism:

> "There's a prevailing mindset that transformers work on everything. And this is true. But there are nuances. Attention is actually most effective when your data is at the right level of abstraction."

**The argument:** Transformers succeed partly because data is pre-processed by tokenizers (BPE, WordPiece). The tokenizer acts as a learned compressor — it does much of the work transformers "learn." Without good tokenization, transformers degrade significantly.

**Tokenization problems (Karpathy's criticism):**
- Edge cases in spelling, spaces, Unicode
- Requires deliberate engineering to handle
- The better the tokenizer, the better the transformer appears to work

**The lesson:**
> "Not just for efficiency reasons — from a modeling perspective, what features and transformations the transformer captures depends heavily on tokenization quality. Tokenization is low-hanging and notorious."

---

## SSMs vs. Transformers: Byte-Level Modeling

> **[added from lecture]** The clearest empirical test of the tokenization hypothesis:

**MambaByte (and follow-up work):** Compare Mamba vs. transformer on raw byte-level language modeling (no BPE tokenizer).

**Results:** Mamba is **2–3× more data-efficient** than transformers at byte level. Even when transformers use global attention (2× more compute), Mamba still wins.

> "There's a fundamental difference here. It's not just that attention is slower. The comparison between two bottom lines is the same model size, same data, same sequence length — just letting attention do its quadratic thing with much more compute. It's still a bit worse."

**Why:** At byte level, most tokens are low-semantic-value characters. Attention wastes capacity storing exact bytes; SSM compression keeps only what matters.

---

## DNA Modeling: When There Is No Good Tokenizer

> **[added from lecture]** DNA sequences have no natural tokenizer — individual nucleotides carry almost no meaning; semantic information is in k-mer patterns.

**Result:** Mamba is ~3× more efficient than transformers on DNA modeling (from the original Mamba paper).

> "These are settings that don't have tokenization. When you don't have very well-defined tokenizers, the power of transformers goes down and the power of models doing implicit compression goes up."

**Scaling laws for DNA:** H-Net experiments show linear scaling trends on DNA that are fundamentally better than BPE-based approaches — because H-Net learns semantic chunking from raw sequence, rather than relying on a fixed tokenizer.

---

## H-Net: End-to-End Tokenizer-Free Modeling

> **[added from lecture]** H-Net (Hierarchical Network) is the latest from Albert's group — an end-to-end model that operates on raw bytes and learns to chunk them internally.

**Core idea:**
1. **Encoder:** Processes raw fine-grained data (bytes)
2. **Routing mechanism:** For every character, predicts whether it's a boundary (end of a chunk)
3. **Chunk summarization:** Each chunk is compressed into one representation
4. **Main model:** A generic sequence model (transformer) operates on chunks
5. **Decoder + expansion:** Expands back to original resolution for prediction

> "The outer stages strongly benefit from being SSMs. Any part of the model that touches byte-level data is way better as an SSM than a transformer."

**What chunking looks like in practice:** Early in training, the model explores many boundaries. Later in training, it stabilizes on semantically meaningful ones — often coinciding with word boundaries (because of spaces) but also subword patterns.

**Why the outer layers must be SSMs:** Even when operating on BPE tokens (not raw bytes), the outer encoder/decoder layers are better as SSMs — because their role is compression, not just token processing. The finite-state compression bias of SSMs helps even at the BPE level.

**Multi-stage chunking:** H-Net can be nested — output of one H-Net can be input to another, creating multiple levels of abstraction (bytes → subwords → words → phrases). First model that can learn chunking hierarchies end-to-end.

**Results:** Single-stage H-Net on bytes eventually outperforms BPE-transformer at scale. Two-stage H-Net scales even better, though harder to train.

---

## The Deeper Thesis: Compression = Abstraction

> **[added from lecture]** Albert crystallized the philosophical point:

> "The benefit of SSMs is not just about the resolution of data they're seeing. It's about an implicit inductive bias toward compression. The encoder layers aren't just interfacing with data — they're creating a temporal compression. Even when operating on BPE tokens, Mamba in the outer layers makes the model better."

> "Compressiveness is not just a weakness. When the goal is creating better abstractions — chunking bytes into words, words into phrases — compression and abstraction are fundamentally the same thing. And SSMs empirically seem very important for that."

> "I think of the future of modeling as requiring not just transformers, but a lot of other ideas. Most people view transformers as a very powerful tool and design the whole pipeline around them. But there's really a lot of room for major improvements in architecture design."

---

## Key Architectural Design Question

> **[added from lecture]** Albert's final framing:

> "The central question in architecture design is: is my model using every flop wisely? There may be settings where you really do need quadratic attention — where you need to cache and memorize everything. And there may be settings where you need the compression that SSMs provide. The efficiency argument for either model is a bit of a distraction. We should focus on what we want the model to model."

---

## Q&A Highlights

*Added from lecture.*

**Q: Does the brain use backprop through time? There's little evidence for storing C copies of the brain.**
> "I'm a big fan of work looking at alternative computation paradigms. I'm not a neuroscientist, but I do think there's probably a physical memory constraint — if you can't fit the full sequence in memory, you literally can't learn long-range dependencies. That could be a real limitation of current approaches. There might be fundamentally different solvers inside the brain."

**Q: Do SSMs outperform transformers in data-constrained or small model settings?**
> "I don't know the full answer. I did hear that OpenAI's recent parameter golf challenge saw that even a little attention was critical for tiny models. At small scales, the tradeoff dynamics might be different."

**Q: Is chunking the elegant future of models?**
> "I fundamentally believe chunking is a really critical primitive. The version we published is just the first step — there's a lot of room for improvement. Philosophically, it feels like something that should be important for learning abstractions from scratch. We haven't validated it at large scales yet — that's the next step."

**Q: How does H-Net handle variable-length chunk sequences mechanically?**
> "One key advantage: there's no lookup table of embeddings for chunks. After the first encoding stage, everything is just in embedding space — we pool or copy embeddings for each chunk. The chunking decision is learned and dynamic. We don't need a fixed vocabulary."

**Q: For SSMs in external memory / cache curation for attention models?**
> "I think that's a very natural application — using SSMs to compress context into higher-level abstractions or memories that an attention model can then attend over. That's directly in the philosophy of why one might want to do chunking."

**Q: Is there an interpretability tool for SSMs like attention maps?**
> "It's harder but there's a correspondence. SSMs can be viewed as a form of linear attention. You can visualize dependence between tokens — it tends to be more diffuse than attention's localized patterns. SSMs squish everything together; attention can be very selective. Mechanistic interpretability of SSMs is ongoing work."

---

## Papers Referenced

| Paper | Venue | Relevance |
|-------|-------|-----------|
| [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) | 2023 | Foundational SSM work |
| [Mamba-2: Transformers are SSMs](https://arxiv.org/abs/2405.21060) | ICML 2024 | SSM-transformer equivalence |
| [Mamba-3: Improved Sequence Modeling using State Space Principles](https://arxiv.org/abs/2603.15569) | 2026 | Latest iteration |
| [H-Net: Tokenizer-Free Language Modeling with Hierarchical Chunking](https://arxiv.org/abs/2603.XXXXX) | 2026 | Dynamic chunking, end-to-end |

---

## Speaker Info

**Albert Gu** — Assistant Professor, Machine Learning Department at Carnegie Mellon University; Chief Scientist at Cartesia AI. PhD at Stanford (2024) under Chris Ré. Recognized on the Time AI 100 list of most influential researchers in 2024. Pioneer of structured state spaces (S4 → Mamba → Mamba-2 → Mamba-3).

**Links:**
- [Mamba GitHub](https://github.com/state-spaces/mamba)
- [Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/)
- [Albert Gu's website](https://arogeyangu.com/)

---

## Pre-Read

For background and pre-lecture material, see [pre-read.md](./pre-read.md).

---

## Related Sessions

- **Week 2: JEPA** — Hazel Nam & Lucas Maes (Brown University) — world models for planning
- **Week 4: Nouamane Tazi (Hugging Face)** — infrastructure for scaling
- **Week 10: Charles Frye (Modal)** — serverless GPU deployment

---

*Last updated: 2026-08-17*
