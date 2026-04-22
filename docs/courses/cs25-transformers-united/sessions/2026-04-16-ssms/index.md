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
**Speaker:** Albert Gu (CMU)
**Status:** Awaiting Video (~3 week upload delay per Stanford policy)

---

## Talk Description

State Space Models (SSMs) offer an alternative to attention-based transformers with O(n) complexity instead of O(n²). Albert Gu's Mamba architecture has emerged as the leading SSM, enabling 100K+ context windows and efficient inference. This lecture covers the evolution from S4 to Mamba-3 and their implications for long-horizon reasoning.

---

## Slides

**Slides:** Not yet posted (~3 week upload delay per Stanford policy)

---

## Speaker Background

**Affiliation:** Carnegie Mellon University, co-creator of Mamba

**Background:** PhD at Stanford under Chris Ré, pioneering work on structured state spaces. Now at CMU continuing SSM research.

**Key contributions:**
- S4 (Structured State Spaces) — first practical SSM for long sequences
- Mamba — selective SSM with content-dependent reasoning
- Mamba-2 — 2-8X faster with algorithmic improvements
- Mamba-3 — latest iteration (2026)

---

## Papers Referenced

| Paper | Venue | Relevance |
|-------|-------|-----------|
| [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) | 2023 | Foundational SSM work |
| [Mamba-2: Transformers are SSMs](https://arxiv.org/abs/2405.21060) | ICML 2024 | SSM-transformer equivalence |
| [Mamba-3: Improved Sequence Modeling using State Space Principles](https://arxiv.org/abs/2603.15569) | 2026 | Latest iteration |

---

## Key Takeaways

*Pending lecture video and slides.*

---

## Awaiting Video

- **Key Insights** — Major structural arguments from the lecture
- **Technical Details** — Novel contributions and methods
- **Q&A Highlights** — Answers to questions from the pre-read
- **Connections to Autonomy** — Relevance to robotics/embodied AI

---

## Pre-Read Questions

See [pre-read.md](./pre-read.md) for the full question bank (12 questions total).

---

## Related Sessions

- **Week 2: JEPA** — Hazel Nam & Lucas Maes (Brown University) — world models for planning
- **Week 4: Nouamane Tazi (Hugging Face)** — infrastructure for scaling
- **Week 10: Charles Frye (Modal)** — serverless GPU deployment

---

## References

- [Mamba GitHub](https://github.com/state-spaces/mamba)
- [Mamba-2 blog series](https://goombalab.github.io/blog/2024/mamba2-part1-model/)
- [Albert Gu's website](https://arogeyangu.com/)

---

*Session notes compiled from pre-read research. Video synthesis pending post-production upload.*

---

## Pre-Lecture Lightning Talks

### MongoDB: Vision RAG for Document Processing

**Speaker:** MongoDB representative

**Key insight:** Vision RAG replaces OCR → text → embed pipeline with direct visual encoding.

| Approach | Pipeline | Limitation |
|----------|----------|------------|
| **Traditional RAG** | Image → OCR → Text → Embed | OCR errors propagate, layout lost, handwriting fails |
| **Vision RAG** | Image → Direct vision encode → Embed | Preserves layout, handles handwriting, no text extraction |

**Example use case:** Insurance agent querying for similar claims — photo + context interleaved in a single embedding.

**Model referenced:** Voyage Multimodal 3.5 — interleaved text+image embeddings in one vector.

**Relevance to ShadowHound:**
- Found pet photo + location text → single vector query
- Duplicate case detection: photo-similar AND description-similar in one search
- Intake photos (QR codes, shelter documents) handled natively without OCR pipeline
- Petco Love Lost-style photo matching but with retrieval layer

---

### Main Lecture: SSM Resurgence

**Key theme:** Return of recurrent/linear models as subquadratic alternatives to transformers.

**Models in focus:**
- **Mamba** — selective SSM, content-dependent state
- **xLSTM** — extended LSTM with modern training improvements (Hochreiter group)
- **DeltaNet / Gated DeltaNet** — linear attention variants with gating mechanisms
- **Test-time training** — adapting model weights during inference

**Why now:** Transformer context windows hit limits at very long sequences. SSMs offer O(n) instead of O(n²), enabling 100K+ token contexts with constant memory during inference.

---

**Taxonomy note:** Lecturer (Albert Gu) uses "State Space Model" as an umbrella term for all compressed-state sequence models — not just the classic Mamba/S4 family. Under this definition, SSMs include:
- Recurrent models (xLSTM)
- Linear attention variants (DeltaNet, Gated DeltaNet)
- Selective SSMs (Mamba)
- Test-time training models

**Shared property:** Maintain a compressed state rather than a full KV cache — O(n) memory during inference instead of O(n²).

---

**Topic: Autoregressive modeling** — how SSMs handle sequential prediction vs transformers.

---

**Transformer inference bottleneck:** During autoregressive generation, transformers must cache all previous KV pairs to compute attention for the next token. The KV cache grows linearly with context length — memory pressure increases indefinitely as you generate longer sequences.

**Contrast with SSMs:** Compressed state — fixed memory footprint regardless of sequence length during generation.

**Implication:** Transformers are effectively O(n²) during training (full attention over n tokens) but O(n) in *storage* during inference (KV cache). SSMs are O(n) in both training and inference, but trade information capacity for memory efficiency.

---

**Transformers generate quadratically** — each new token requires re-computing attention across all previous tokens (O(n²) compute per token as sequence grows). The longer the generation, the more expensive each step becomes.

**SSM advantage:** Constant compute per token — same cost whether generating token 100 or token 100,000.

---

**SSM core mechanic:** Token arrives → update hidden state → token discarded. The state is a fixed-size compression of all previous input. No KV cache, no quadratic compute.

**Tradeoff:** Information is compressed into fixed state. Important details from early tokens may be overwritten by later ones — selection of what to keep becomes critical.

**Linear time:** Both training and inference scale O(n) with sequence length, constant per-token compute.

---

**Key insight:** KV cache = transformer's state space.

Both transformers and SSMs are stateful sequence models — they maintain state as they process tokens. The difference is in *how* they store that state:

| Model | State storage | State size | Information |
|-------|--------------|------------|-------------|
| **Transformer** | KV cache (uncompressed) | Grows O(n) with sequence | Full, exact — every token preserved |
| **SSM** | Compressed hidden state | Fixed size (constant) | Approximate — compression is lossy |

**Implication:** Transformers and SSMs are more similar than they appear — they're both trying to maintain useful state about the sequence so far. The architectural difference is compression strategy: transformers preserve everything (expensive but lossless), SSMs compress (cheap but lossy).

This frames the transformer/SSM tradeoff not as "stateful vs stateless" but as "lossless compression vs lossy compression of sequence history."

The Mamba-2 paper formalizes this equivalence — "Transformers are SSMs."

---

**Analogy:** Transformers ≈ databases (exact retrieval, complete history). SSMs ≈ brains (compressed patterns, efficient inference).

**Transformer (database):** Store every token exactly — like a lookup table. Query = full recall of everything seen.

**SSM (brain):** Compress to patterns — like how biological brains generalize. Query = pattern match from compressed representation.

**Implication:** Neither is universally better. Databases win when you need exact recall. Brains win when you need generalization, efficiency, and speed over long sequences.

**For robotics/autonomy:** Continuous sensor streams over hours/days — a brain-like model (SSM) that generalizes from compressed patterns may be more practical than a database (transformer) that needs to store everything verbatim.

---

**SSM tradeoff: Bad at retrieval.** Because SSMs compress state, they lose access to exact token information. If an important detail was overwritten during compression, the SSM literally cannot retrieve it — it's gone.

**Scenarios where SSMs underperform transformers:**
- Exact lookup of specific tokens ("What was the 47th token?")
- Tasks requiring verbatim recall (copying exact strings)
- Any problem where compression destroys needed signal

**When SSMs excel:** Problems where generalization and pattern completion matter more than exact recall.

---

**Hybrid models: Intelligence = brain + tools.**

**Analogy:** Biological brain handles fast, compressed, generalized reasoning. Tools (databases, calculators, search) handle exact retrieval and precise computation.

**Why hybrid:** SSMs are great at pattern recognition and efficient inference. But for exact retrieval — the KV cache wins. Hybrid systems combine both: SSM for fast inference, transformer/database for exact recall.

**Architecture pattern:** SSM as the core "brain" with external tool hooks for retrieval when needed.

**For embodied AI:** Robot runs an SSM for continuous sensor streams, but queries a vector database for exact stored information (maps, waypoints, known objects) when needed.

**Frontier:** Models that learned when to "delegate" to external tools vs handle internally — like agents that decide "do I know this, or do I need to look it up?"

---

**Hybrid SSM architectures — papers discussed:**
- **H3** (Hungry Hungry Hippos) — SSM for language modeling
- **Jamba** — hybrid attention + SSM (AI21)
- **Mamba** — selective SSM
- **Walleffe et al.** — recent work on SSM-Transformer hybrids

**These models explore:** Where to place attention vs SSM layers, how to interleave compressed state with KV cache for best of both worlds.

---

**Optimal hybrid ratio: 10 SSM layers : 1 attention layer.** Empirical finding from hybrid architecture experiments.

**Implication:** Most of the computation is SSM-based (fast, compressed), with occasional attention layers for retrieval and exact tasks. This gives the model most of SSM's efficiency with targeted attention for when it matters.

**Practical design principle:** If building a hybrid model, heavily weight toward SSM layers with sparse attention checkpoints rather than many attention layers.

---

**Myth-busting: "Attention is all you need" (the paper title).**

| Belief | Reality |
|--------|---------|
| Just throw data at a transformer — attention handles everything | Attention most effective on **pre-compressed** data |
| Transformers are learn-everything-from-scratch models | Attention works best when input is already structured/compressed |

**The lesson:** Compression before attention improves attention's effectiveness. SSMs pre-process and compress sequence information; attention then retrieves from that compressed state more efficiently than from raw tokens.

**Architecture implication:** SSM (compress) → Attention (retrieve) outperforms raw attention over raw tokens.

**For robotics:** Sensor streams → SSM compression → attention-based planning may outperform raw attention over full sensor history.

---

**Tokenization — root of all suffering (Karpathy).**

**Karpathy's position:** Tokenizers themselves are the problem — not just bad design. Tokenization imposes an artificial discretization that lossy-compresses information before the model even sees it. Any tokenizer is a compression bottleneck.

**His argument:** The alternative is tokenizer-free models — process raw bytes or pixels directly. No discrete token vocabulary means no compression loss. Models like H-Nets (mentioned in this lecture) work at the raw representation level.

**What happens without proper tokenization:**
- Model wastes capacity on meaningless sub-tokens
- Semantic relationships lost in tokenization boundary decisions
- Information compressed into ambiguous tokens → downstream confusion

**Karpathy framing:** Tokenization is the root of all suffering in LLMs — not "bad tokenizers are the problem" but "tokenization as a concept imposes constraints that no downstream architecture can fully recover from."

**For our multimodal RAG discussion:** Voyage Multimodal 3.5's interleaved text+image embedding is a step toward tokenizer-free — treating image patches and text tokens as first-class citizens in the same space, rather than projecting images into a text-based token vocabulary.

---

**Isometric representations:** A representation is isometric when geometric relationships in the input space are preserved in the model's internal space — distances between tokens remain consistent through the transformation.

| Model type | Isometric? | What it means |
|------------|-----------|---------------|
| **Transformer (KV cache)** | ✅ Isometric | All tokens preserved exactly, distances exact, no information loss |
| **SSM (compressed state)** | ❌ Non-isometric by nature | Lossy compression, geometric relationships distorted by state compression |

**Why this matters:** Isometric ≠ better in all cases. Isometry is a fidelity guarantee — exact preservation of structure. Non-isometric models (SSMs) trade this fidelity for efficiency and generalization. The question is which trade-off you need for the task.

**For robotics:** For exact spatial reasoning (exact waypoints, precise trajectories), we need isometric representations. For behavioral generalization and pattern completion, non-isometric SSM compression may actually be beneficial — the model learns to represent structure, not exact positions.

---

### Softmax vs Hard Attention

**Softmax attention:** Every token attends to every other token with a weighted probability. The output is a weighted sum of all values — smooth, differentiable, but requires storing all KV pairs. Classic transformer attention.

**Hard attention:** Each token attends to exactly one position (or a discrete set). Binary or near-binary decision — "look at THIS token, not the others." Not differentiable, harder to train, but dramatically more memory-efficient.

**Tradeoffs:**

| Property | Softmax | Hard |
|----------|---------|------|
| Memory | O(n) KV cache | O(1) — just index |
| Compute | O(n²) per layer | O(n) |
| Differentiable | ✅ Yes | ❌ Requires tricks (REINFORCE, etc.) |
| Exact retrieval | ✅ Full | ✅ If correct choice |
| Generalization | ✅ Smooth | ❌ Brittle — wrong choice = fail |

**Why this matters for SSMs:** SSMs can be viewed as a form of hard attention — the compressed state is a single discrete representation, not a weighted blend over all tokens. The state IS the "hard choice" about what to retain.

**The hybrid answer:** Some models use soft attention for training (differentiable) and hard attention at inference for efficiency. Or SSM-style compression followed by targeted soft attention for retrieval (the 10:1 ratio mentioned earlier).

---

**Attention works well at certain granularities — not universally.**

| Token type | Attention effectiveness | Why |
|------------|------------------------|-----|
| **Word/subword tokens** | ✅ Effective | Rich semantic content per token — attention finds meaningful relationships |
| **Character tokens** | ❌ Inefficient | Low semantic density — most attention compute wasted on noise |
| **DNA tokens** | ❌ Inefficient | Meaning distributed across long k-mers, not single nucleotides |
| **Amino acid tokens** | ❌ Inefficient | Protein function emerges from sequence patterns, not individual residues |
| **Image pixels/patches** | ❌ Inefficient without proper encoding | Raw pixels have little semantic meaning individually |

**The granularity problem:** Softmax attention's strength is *selective weighted combination* of rich vectors. When each vector is semantically weak (character, pixel), attention has to do much more work to extract signal.

**Implication:** Tokenization determines whether attention is effective. A tokenizer that produces semantically thin tokens (character-level, raw pixel patches) undermines attention's core advantage. This is why ViT uses patch encoders — not raw pixels — and why DNA models use k-mer tokenization rather than individual nucleotides.

**Connection to Karpathy:** "Tokenization is the root of all suffering" — at the wrong granularity, attention can't do its job even with infinite compute.

---

### SSM as Learned Tokenizer (H-Nets Architecture)

**Question:** Why is SSM encoder → Transformer (H-Nets) better than classic tokenizer → Transformer?

**Answer:** SSM is a *learned, task-optimized* tokenizer — not a fixed rules-based one.

| Tokenizer type | How it chunks | What it optimizes |
|----------------|---------------|------------------|
| **Classic (BPE, WordPiece)** | Fixed rules on training corpus frequency | What tokenizes well in training data |
| **SSM encoder (H-Nets)** | Data-driven, learned from prediction target | What preserves predictive power for the task |

**SSM chunking mechanics:**
1. SSM scans a window of raw input (characters, nucleotides, pixels)
2. Decides which tokens group together — learned from training
3. Compresses each chunk into a compact representation — some information kept, some discarded
4. The compressed chunk becomes the "token" for the downstream transformer

**Classic tokenizer limitation:** No discard mechanism — every token is preserved. But not every token matters for prediction.

**SSM advantage:** Learns which information in a chunk is predictive and which is noise. Chunks aren't just larger tokens — they're compressed representations with task-relevant information retained.

**Key property:** The chunking is learned to optimize prediction of the next target — not to minimize tokenization vocabulary size or training corpus frequency.

**For robotics:** An SSM encoder over sensor streams would learn to compress proprioceptive/visual sequences into chunks that predict next state — learned representations optimized for physical prediction, not statistical tokenization.

---

### Tokenization as Feature Engineering (Inductive Bias in Compression)

**Key theme emerging:** Tokenization is never neutral — it always encodes prior assumptions about what matters in the data.

**Classic tokenizer as feature engineering:**
- BPE/WordPiece = developer decisions about what subword units are meaningful
- Human-designed rules encoding assumptions: "this subword boundary makes sense"
- Explicit feature engineering disguised as preprocessing

**SSM tokenizer as feature engineering:**
- Architecture choices (recurrence, state size, discretization) = inductive biases
- What the SSM compresses vs preserves = learned feature selection
- Still encodes priors — just learned from data instead of hand-coded

**Inductive bias无处不在 (everywhere):**
- Softmax attention has a bias toward smooth weighted combinations
- SSM recurrence has a bias toward temporal compression
- Even "no tokenization" (raw bytes) has a bias — each byte is equally weighted

**The lecturer's point:** There's no escaping feature engineering. The question is whose priors you're using — human-designed rules, data-learned compression, or architectural constraints. Each choice encodes assumptions about what structure matters.

**Practical implication:** When designing a system, the tokenizer/compression choice is the first and most impactful feature engineering decision. It's not "preprocessing" — it's the model's first representation of reality.

---
