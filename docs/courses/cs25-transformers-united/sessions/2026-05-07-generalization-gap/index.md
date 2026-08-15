---
title: "Session 7: Distinct Modes of Generalization from Parameters and Context"
layout: default
parent: CS25: Transformers United V6
nav_order: 7
permalink: /courses/cs25-transformers-united/sessions/2026-05-07-generalization-gap/
date: 2026-05-07
---

# Session 7: Distinct Modes of Generalization from Parameters and Context

**Date:** May 7, 2026
**Speaker:** Andrew Lampinen (Anthropic)
**Topic:** Distinct Modes of Generalization from Parameters and Context, and Paths to Bridge the Gap
**Slides:** [Link](https://drive.google.com/file/d/1-YIOa5Yal4RCjAsV-0tnW_NNDGbY1GTo/view)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=dJtHauhRasc)
**Status:** ✅ Enriched with lecture content

---

## Core Question

> How do language models generalize from information they learn — and what might that tell us about natural intelligence?

LMs have **two fundamentally different ways of "learning"**:
1. **In-context learning (ICL)** — information provided in the context window
2. **Parametric learning** — information encoded via gradient descent into model weights

---

## Part 1: Parameters vs. Context — The Generalization Gap

### The Reversal Curse

When models are fine-tuned on facts like "A is B," they often fail to answer questions about "B is A" — even though it's the same information in reverse. This is the **Reversal Curse**.

**Experiment:**
- Fine-tune GPT/LLaMA on synthetic facts in one order (e.g., "Daphne Barrington is the director of 'A Journey Through Time.'")
- Model succeeds on same-fact-order questions
- Model fails on reversed-order questions ("Who directed 'A Journey Through Time'?" → wrong answer)

**But here's the twist:** models handle reversals just fine when the information is in-context. "If Zepax are bigger than Quarples, then Quarples are..." — the model correctly infers the reversal. This is exactly the same structure as the reversal curse, but ICL handles it.

> **[added from lecture]** The inspiration for this work started from the Oayan Evans et al. paper on the Reversal Curse. When Andrew first saw that work, he found it surprising because if you try the same experiment in a chat (ICL) — e.g., tell the model "Zpacts are bigger than corpals" — the model immediately infers "corpals are smaller than Zpacts." This was his easy baseline, at ceiling for all models. This contrast made him ask: is it possible that how models generalize from in-context information is fundamentally different from how they generalize from parametric information?

### Why Does ICL Outperform Fine-Tuning on Latent Information?

Many training documents latently convey more than their explicit content. For example:
- **Reversals:** "X is Y's parent" implicitly contains "Y's parent was X"
- **Syllogisms:** Two statements about X→Y and Y→Z implicitly contain conclusions about X→Z
- **Multi-hop reasoning:** Explicit facts about X and Y can latently answer questions about their relationship

Models in context can reason over this latent information flexibly. Parametric learning consolidates it into a form that's more tied to the original explicit content — losing the flexibility.

> **[added from lecture]** Andrew's mental model: when you train parametrically, you consolidate information across many documents, but the consolidation is tied to *how the information was explicitly conveyed*. So at test time the model is less flexible. By contrast, ICL fits less information, but it's in richer detail and more flexibly usable. He emphasizes that parametric learning is NOT unimportant — it learns the statistical structures that enable ICL to work in the first place. ICL is better at using specific pieces of information flexibly; parametric learning is better at extracting *statistical structures common across many documents*, and those structures support ICL.

### Even Training from Scratch Doesn't Fix It

> **[added from lecture]** Andrew tested whether the problem is specific to fine-tuning (maybe models just don't learn much in fine-tuning). He trained a small model from scratch on a large synthetic dataset: 20,000 relationships, most with reversals, but 1% of reversals held out. The data had: (a) filler content for diversity, (b) trained relations like "X contains Y," (c) in-context training sequences showing forward + reverse. Even with training from scratch and enough data to support generalization in-context, models still got **zero generalization to held-out reversals**. This is not a fine-tuning artifact — it's something fundamental about how parametric learning generalizes from relational information.

The core issue: **many structures are latent in the data but parametric learning doesn't encode them in a way that's usable at test time.**

### The Codebooks Task

> **[added from lecture]** Andrew also tested generalization on a "codebooks" task — models trained on how to encode information using different "languages" (codebooks). They got examples of encoding words from each language but not all of them, then were tested on unseen encoding words. Again: models could use the information well if it was in context, but couldn't generalize to held-out tests. A questioner asked whether "no context" meant relying on world knowledge — Andrew clarified that "no context" meant providing the codebook and sequence to translate but testing generalization to novel encoding words, and that the model does generalize well to known encodings in novel sequences, it's not just overfit to the training set.

### Statistical Structure Can Mask Latent Generalization Failures

> **[added from lecture]** A crucial point Andrew emphasized: models often generalize better than 0% in practice *not* because they do the latent reasoning, but because they pick up on word co-occurrences in the training corpus. Example: if you train on "all birds have wings," "eagles are a type of bird," "hawks are a type of bird," "pigeons are a type of bird," etc. — the test "Eagles have wings" won't need latent reasoning at all; co-occurrence statistics suffice. But if you use a case like "penguins fly" (where co-occurrences would be misleading), both models and young children get it wrong. This is why these latent generalization failures aren't obvious unless you do controlled experiments with nonsense words. Statistical learning is helpful on average but can lead to incorrect generalizations in specific instances — and it can also let models skip needed structured reasoning.

### The Compression Analogy

> **[added from lecture]** In response to a question, Andrew discussed viewing parametric learning as compression: the forward direction is preserved (useful), the reverse is "lost in compression." He agreed this is partially valid — compression can be useful for extracting certain structures, but lossy compression loses information important for generalization. This is an important tension: compression enables useful statistical generalization but can destroy the very information needed for structured inference.

---

## Part 2: Paths to Bridge the Generalization Gap

### Approach 1: In-Context Augmentation

If ICL generalizes better, use it to augment the fine-tuning data.

**Method:**
1. Put the full training dataset in context
2. Prompt the model to generate reasoning traces that make explicit connections (reversals, syllogisms, missing links)
3. Add these generated conclusions to the dataset
4. Fine-tune on the augmented dataset

**Result:** Augmented fine-tuning matches or exceeds ICL performance on reversals and syllogisms.

**Why it works:** Augmentation makes explicit and accessible what was already latent in the data — it doesn't create new information, it surfaces what was already there.

> **[added from lecture]** Andrew walked through the exact prompt approach: take the training set, concatenate as context, pull out individual documents one at a time, and ask the model "make connections between this document and other documents in the corpus, including rephrasing and figuring out relations between entities." Example output: "I learned earlier that feps can zarp, and this document says dax are type of fat, therefore dax can zarp." He acknowledged the prompts are in the appendix of the paper and are quite tied to factual/entity settings — doing this in a fully general way is a hard problem. On prompt sensitivity: they did ablation on prompts and it mattered less than expected, but for math reasoning or other domains, those prompts probably wouldn't transfer well.

> **[added from lecture]** Andrew addressed a common reaction against synthetic data: his colleague Dave Fan once tweeted "please learn the data processing inequality — you can't discover new knowledge from synthetic data generated from existing knowledge." Andrew agreed it's not wrong but called it misleading: augmentation doesn't create new information, it extracts what's already latent and makes it explicit. Example: if the corpus has "all X are Y, no Y are Z," then "no X are Z" is already implied — augmentation just makes it explicit.

### Approach 2: Episodic Retrieval at Test Time

Bring relevant experiences into context at test time, turning parametric tasks into in-context ones.

**Method:** Oracle episodic memory that retrieves at least one relevant experience (plus some irrelevant ones). Use retrieved context to answer.

**Result:** Episodic retrieval unlocks flexible generalization that pure parametric learning can't achieve — even on latent structures like reversals.

**Connection to natural intelligence:** This parallels the hippocampal-cortical complement in brains. The hippocampus rapidly encodes specific experiences in rich detail; the neocortex consolidates information more slowly into abstract, generalized form. Retrieval is like bringing hippocampal content into neocortical "context."

> **[added from lecture]** Andrew used an **oracle episodic memory** (perfect recall, imperfect precision — always retrieves something useful plus distractors). He admitted this is "totally cheating" — he doesn't know how to do good retrieval yet. But the results show the mechanism: even for documents trained into the parameters, having them back in context allows much more flexible use. On a question about whether you can extract true content but not relations: Andrew clarified that models can extract relations from pre-training well, but they need to be *cued in the right way* — ask in the forward direction with the first part of the relation and they continue fine; but going backwards requires the information already be in context.

### Approach 3: Test-Time Thinking via RL

Can models learn to regenerate necessary context information via chain-of-thought, without explicit retrieval?

**Method:**
1. Instill knowledge via fine-tuning on dataset A
2. Use RL to teach the model to regenerate relevant context in its CoT when answering questions
3. Test on held-out dataset B (not augmented)

**Result:** RL thinking improves generalization beyond the augmented distribution — but struggles with pure reversals (tries exhaustive enumeration rather than structured inference).

> **[added from lecture]** Andrew explained the intuition: the model already knows the relations and already knows how to do reversals in-context — it just needs to put the pieces together in its chain of thought. The RL process: fine-tune on several non-overlapping datasets, then do RL on one dataset (A) and test generalization to another (B). Reversals get little benefit from this approach because the whole point of reversals is that going from one direction to the other is hard. The model basically enumerates entities until it hits the right one. For syllogisms it's better because you can "follow the chain of links" — "I know all dax are fep... what do I know about dax?" The difference from augmentation: augmentation has the documents present and generates reasoning traces from them (easier — information is available); RL thinking has to learn how to *pull out* relevant information without seeing it (harder).

---

## Part 3: Connections to Natural Intelligence

The same latent generalization problem exists in biological learning systems:

| Structure | Explicit | Latent |
|-----------|----------|--------|
| Reversal | "X is Y's parent" | "Y's parent was X?" |
| Multi-hop | X→Y, Y→Z statements | Who is X's grandchild? |
| Cross-lingual | Japanese: "XはYさんのお母です" | Who is X's child? |
| Alternative goals | Navigate to ◊ | Navigate to ♥ |

**Brain parallels:**
- **Parametric learning** ≈ neocortical slow consolidation
- **Episodic retrieval** ≈ hippocampal replay and memory consolidation
- **ICL** ≈ bringing relevant experiences into current context

> **[added from lecture]** Andrew went deeper on the neuroscience connection. The classic reason hippocampal-cortical complement evolved: cortex needs to learn *slowly* to integrate across experiences without interference (good for statistical generalization); hippocampus needs to learn *rapidly* from a single experience (you don't want to be in a car accident 50,000 times before learning). The hippocampus replays experiences — both offline (during sleep, reorganizing for future generalization) and online (helping solve current problems). The brain's approach to latent generalization is "throw everything at the wall and see what sticks" using both offline augmentation and online retrieval. Andrew noted James Wedington has done significant work comparing transformer attention to hippocampal memory — at the implementation level they're completely different (hippocampus isn't doing key-query-value attention), but computationally they share properties of weighted similarity-based lookup from past states.

> **[added from lecture]** Andrew noted a key place where the brain/hippocampus analogy breaks down: you can't fit a whole lifetime of experience in a brain's "context window." The hippocampus does much more generative retrieval — a non-trivial percentage of episodic memories never actually happened. The confabulation rate in hippocampus may be higher than in ICL at current scales. But at the scales we're currently operating with transformers, the confabulation rate from ICL may be lower than the hippocampal rate.

### Tradeoff Summary

| Method | Train cost | Test cost | Generalizes beyond augmentation? | Notes |
|--------|-----------|-----------|----------------------------------|-------|
| Augmentation (train-time) | High (long-context inference to generate traces) | Free | No — only what you augmented for | Best when you know what questions you'll face |
| Retrieval (test-time) | Free | High (longer context per query) | Yes (brings full experience back) | Needs good retrieval; Andrew used oracle |
| RL thinking (test-time) | High (RL training step + longer inference) | High (longer CoT) | Yes | Struggles with pure reversals; good for chain-followable structures |

> **[added from lecture]** Andrew's framing: augmentation is easiest for the model because it just generates inferences from documents it can see; retrieval is easiest because the model knows exactly what question it's answering; RL thinking is hardest because the model doesn't know which information will be useful. On hallucination risk in augmentation: in Andrew's experiments the hallucination rate was low enough that it was worth it — as long as hallucinations are roughly independent, the model learns the right answer on average. Fine-tuning on larger datasets without regularization can distort existing knowledge more.

---

## Key Takeaways

1. **ICL generalizes to latent information that parametric learning misses** — because parametric consolidation ties knowledge to its original explicit form
2. **Three paths to bridge the gap:**
   - **Augmentation** (train-time): surfaces latent info before consolidation
   - **Retrieval** (test-time): brings specific experiences into context on demand
   - **RL thinking** (test-time): teaches models to regenerate necessary context via CoT
3. **Tradeoffs:** augmentation is efficient at test-time but expensive at train-time; retrieval is free at train-time but costs at inference; RL thinking generalizes beyond augmented data but struggles with exhaustive enumeration
4. **The brain has an analogous architecture** — complementary learning systems (hippocampus + neocortex) solve the same problem
5. **Statistical structure can mask latent reasoning failures** — word co-occurrences in natural data often let models bypass the need for structured inference, which is why these failures aren't obvious without controlled experiments

---

## Papers Referenced

- *On the generalization of language models from in-context learning and finetuning* — Lampinen et al. (Google DeepMind + Stanford)
- *Latent learning: episodic memory complements parametric learning* — Lampinen et al.
- *Improving latent generalization using test-time compute* — Chaudhry et al.
- *Complementary Learning Systems* — McClelland, McNaughton, O'Reilly (1995)
- *A Theory of Usable Information under Computational Constraints* — Xu et al. (ICLR 2020)
- *Learning by Thinking in Natural and Artificial Minds* — Lombrozo (additional reading on augmentation philosophy)

---

## Speaker Info

**Andrew Lampinen** — Member of Technical Staff at Anthropic. Previously Staff Research Scientist at Google DeepMind, PhD in Cognitive Psychology at Stanford. Research bridges AI and cognitive science: learning, generalization, and representation in LMs, agents, and humans.

- Twitter/X: @AndrewLampinen
- Bluesky: lampinen.bsky.social
- Substack: infinitefaculty.substack.com

---

*Last updated: 2026-08-15*
