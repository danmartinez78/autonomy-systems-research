---
title: "Session 1: Overview of Transformers"
layout: default
parent: CS25: Transformers United V6
nav_order: 1
permalink: /courses/cs25-transformers-united/sessions/2026-04-02-overview/
date: 2026-04-02
---

# Session 1: Overview of Transformers

**Date:** April 2, 2026
**Speakers:** Instructors (Steven Feng, Karan Singh, Michael C. Frank, Christopher Manning)
**Video:** [▶ YouTube](https://www.youtube.com/watch?v=bHSDPgZYie0)
**Status:** ✅ Enriched with lecture content

---

## Session Overview

Brief intro and overview of the history of ML/NLP, Transformers and how they work, and their impact on robotics, autonomy, and embodied AI. Discussion about recent trends, breakthroughs, applications, and current challenges/weaknesses.

[View the full slide deck](https://drive.google.com/file/d/153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB/view?usp=sharing){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

---

## Instructor Backgrounds

*Added from lecture — instructor introductions.*

**Steven Feng** — 4th year CS PhD student at Stanford. Previously at Carnegie Mellon & University of Waterloo. Research broadly in NLP: language models, efficient reasoning in small language models, data-limited regimes, cognitively-inspired learning signals, and evaluation methods.

**Karan Singh** — 3rd year EE PhD student at Stanford. Research in computer vision, neuroscience, and efficiency (curriculum learning, RAG). Current focus: foundation models for neuroimaging (fMRI). Previously undergrad at Cal Poly SLO, post-bac at Stanford Radiology.

---

## Course Logistics

*Added from lecture.*

This iteration of CS25 is **sponsored by AGI House and MongoDB**. AGI House and MongoDB are partnering to offer students direct access to top AI founders and researchers through the **Frontier Lunch Club** — dinners with a handful of top researchers, later in the quarter, plus a $1,000 project prize at a second event. Members also get added to the AGI House recruiting pipeline. Spots are limited and application-based (QR code scan). A WhatsApp group will carry details.

Course structure:
- Lectures are Thursdays 4:30–5:50 PM PT, in-person (Skiling Auditorium) + Zoom
- Only homework is attendance; in-person required when speaker is on campus
- 3 unexcused absences allowed; Google Form open during lecture for attendance
- Questions via Slido (online) or raised hand (in-person); **do not unmute on Zoom**
- All lectures recorded and posted to YouTube ~2–3 weeks after (Stanford policy)
- Discord + mailing list for announcements

---

## Key Insights from Slides

*(Extracted manually from Week 1 Overview slides — 2026-04-02)*

### 1. Transformers Architecture: The Core Components
- **Self-attention mechanism** — Enables processing of relationships between words in sequences
- **Position encoding** — Provides information about token position in the sequence
- **Feed-forward layers** — Allow the model to consider information from previous positions when making predictions
- **Layer normalization** — Stabilizes training, enables faster convergence

### 2. Evolution of NLP/ML

| Year | Era | Key Developments |
|------|-----|-----------------|
| 2017 | Pre-Transformer | RNNs, LSTMs, Word2Vec, CNNs for text |
| 2018 | Early Transformers | BERT, GPT-1, T5, ULMFiT, Encoder-only |
| 2019 | Architecture refinements | XLNet, RoBERTa, DistilBERT |
| 2020 | GPT-3 era | In-context learning, prompt engineering, larger models |
| 2021+ | Vision Transformers | ViT, Swin, CLIP — self-attention for vision |
| 2022+ | Foundation models | ChatGPT, GPT-4, LLaMA, PaLM, Chinchilla |
| 2023+ | Scaling breakthroughs | GPT-4, Llama 2, Mixtral of Mixture of Experts |
| 2024+ | Efficiency improvements | Sparse attention, Flash Attention, Linear attention variants |
| 2025+ | Reasoning models | o1, Chain-of-Thought, DeepSeek R1, Claude |
| 2026+ | State Space Models | **Mamba** — Linear-time O(n) complexity for long sequences |

### 3. Impact on Robotics/Autonomy
- **World models** — Transformers enable learning predictive models for robot decision-making
- **Embodied AI** — Vision-language models (VLMs) for robot perception and control
- **Long-horizon planning** — Extended context windows enable multi-step reasoning
- **Efficiency for Edge deployment** — Smaller, quantized models for real-time control on robots
- **Safety-critical applications** — Medical AI (Med-PaLM) demonstrates validation patterns for high-stakes domains
- **Sim-to-real transfer** — Challenges in transferring simulation success to real-world deployment
- **Interpretability** — Understanding how models make decisions is crucial for trustworthy autonomy
- **Catastrophic forgetting** — Models can lose information over long sequences
- **Sample efficiency** — Training requires massive datasets
- **Computational cost** — Inference can be expensive without optimization
- **Robustness** — Distribution shifts, adversarial inputs can cause unpredictable behavior

### 4. Current Trends
- **Multimodality** — Vision, language, audio integration
- **Tool use** — Function calling, API integration
- **Personalization** — Fine-tuning for specific domains
- **Mixture of Experts** — Combining specialized models

### 5. Open Challenges
- **Interpretability** — Black-box nature makes understanding difficult
- **Hallucination** — Models can generate confident but incorrect outputs
- **Alignment** — Ensuring model behavior matches human intent
- **Compute sustainability** — Environmental cost of training and deployment
- **Regulation** — Governance frameworks for autonomous systems

---

## Additional Lecture Content

### Pre-Training Data: Quality Over Quantity

*Added from lecture — Steven Feng's research section.*

Steven walked through four research projects demonstrating that data effectiveness isn't just about volume — quality, structure, and usage strategy matter enormously.

#### Project 1: BabyLM and Child Language Transcripts

> **[added from lecture]** The core question: humans learn language from ~10–100 million words of exposure (ages 0–13), while LLMs need billions. Can we train models on actual child language transcripts and see similar variation in outcomes?

**Scaling behavior:** Even at extremely small scales (family-specific transcripts), there is positive but noisy scaling — signal varies heavily across families. Synthetic clean dialogues (up to 200M tokens) show cleaner scaling curves, suggesting data quality matters more than quantity at small scales.

**Key findings:**
- Performance varies more by *which family* the data comes from than by sheer volume
- Linguistic analysis showed that better-performing datasets were more **structurally rich, semantically diverse, and higher in conversational interaction** — confirming child language research that quality > quantity
- Individual children environments produce models with different capability profiles — not just worse versions of larger models
- Grammaticality tasks (Zorro) scaled better than world knowledge tasks (EWoK) — suggesting child-scale data is enough for syntax but not full world understanding
- Scaling depends on **task type**: syntactic tasks benefit more from small-scale data than knowledge tasks

#### Project 2: Bilingual/Multilingual Language Models

> **[added from lecture]** Steven tested the "fusion hypothesis" — do children raised in multilingual environments suffer learning interference? And does *how* bilingual data is exposed (language mixing structure) affect outcomes?

**Setup:** 100M tokens each of English + Spanish (mixed), vs. English-only baselines. Tested code-switching at sentence and word levels.

**Findings:**
- Multilingual models achieve comparable (slightly better) perplexity in both languages vs. English-only — no interference effect
- Exposure structure (mom-always-English vs. random speaker, sentence-level vs. word-level code-switching) has **no significant effect** on outcomes
- Data scale matters more than model scale for multilingual learning at small sizes
- Surprise result: how you interleave languages doesn't degrade learning — models handle it gracefully regardless of structure

#### Project 3: RAG Scaling

> **[added from lecture]** Steven presented work on optimal allocation of compute between pre-training tokens and retrieval tokens in RAG-augmented systems.

**Key findings:**
- Small models (30M params) benefit much more from RAG than large models (3B params) — large models are already "saturated" with memorized knowledge from pre-training
- There is a minimum pre-training threshold (~4 tokens per parameter) below which the model cannot effectively use retrieved context — matching the retrieval corpus to the model's capacity matters
- Improvement per billion retrieval tokens varies inversely with model scale — diminishing returns at large scale with general web data (domain-specific RAG is a different story)

#### Project 4: Curriculum-Guided Layer Scaling

> **[added from lecture — Karan Singh's section]** Karan presented work on growing models during training alongside a data curriculum — starting small with easy data, gradually adding layers and harder data.

**Key findings:**
- CGLS (Curriculum-Guided Layer Scaling) outperforms both training the full-size model from scratch on all data and easy-to-hard scaling with a fixed large model
- Gains compound at larger scales (2B → 20B tokens)
- Not all tasks benefit equally — some tasks prefer the random baseline despite CGLS doing better on reasoning tasks
- Future directions: tuning hyperparameters further, other notions of curriculum difficulty, applying to image or medical imaging domains

**Overall takeaway from the four projects:** Effective language modeling isn't just about amassing data — it's smarter data utilization strategies that harness structure, quality, and characteristics.

---

### Post-Training: Chain-of-Thought, RL, and Beyond

*Added from lecture.*

#### Chain-of-Thought and Extensions

**Basic chain-of-thought:** Instead of outputting an answer directly, models generate step-by-step reasoning traces before answering. Suggests models "know more than they let on" — their weights contain problem-solving capability that direct prompting doesn't surface.

**Tree of thoughts:** Models explore multiple reasoning paths and evaluate which is best (e.g., majority vote across paths).

**Tool-augmented reasoning:** Generate code or other programs as intermediate steps, then execute them — improves precision on math, coding tasks.

**Socratic / compositional decomposition:** Recursively decompose hard problems into subproblems via self-questioning, solve subproblems, recombine — akin to divide-and-conquer planning.

**Compositional tasks as computation graphs:** Formulating complex tasks as graphs of subprocedures, mirroring structured reasoning.

#### Reinforcement Learning Post-Training

**RLHF (Reinforcement Learning from Human Feedback):** Train a reward model from human preference rankings, then post-train the LLM to maximize that reward. Used in ChatGPT, Claude, etc.

**DPO (Direct Preference Optimization):** RL-free alternative — directly trains the model to prefer higher-ranked responses without a separate reward model.

**RLAIF (AI Feedback):** Replace human labelers with off-the-shelf LLMs that provide preference signals — reduces cost and subjectivity.

**GRPO (Group Relative Policy Optimization) — DeepSeek:** Ranks responses in groups (not just binary), providing richer, more fine-grained reward signals. Shows strong gains on math tasks.

#### Process Supervision vs. Outcome Supervision

> **[added from lecture]** For multi-step tasks, only rewarding the final answer can enable reward hacking — model finds a way to get the right answer without the right reasoning. Process supervision labels and rewards individual reasoning steps, leading to better step accuracy and better final answers, while reducing reward-hacking surface.

---

### AI Agents and Self-Improvement

*Added from lecture.*

**The agent loop:** Perceive → Reason/Plan → Act → Observe → (repeat). Agents can reflect on their own outputs and iteratively improve — analogous to how Claude Code (or Copilot) runs scripts, observes compilation/outputs, reflects, and retries.

**Memory store for agents:** Persisting past mistakes and learned preferences across interactions — models adjust future responses based on prior failure loops.

**Tool-augmented agents:** Combine reasoning with external tools — web search, API calls, database queries — incorporated into the reasoning plan before the final output.

---

### Hallucination: A Unified Framework

*Added from lecture — Steven's research.*

> **[added from lecture]** Steven presented a paper offering a unified definition of hallucination across tasks. Existing definitions differ by domain: summarization hallucination = output not faithful to source; QA hallucination = factually wrong in the real world; agent hallucination = incorrect actions based on wrong environmental beliefs.

**Core thesis:** Hallucination = world modeling error. Every hallucination depends on three things:
1. **Reference world model** — what is actually true (source document, database, real world)
2. **Model's view** — what the model can see (retrieved context, prompt, etc.)
3. **Conflict resolution policy** — how the model resolves disagreements between sources

**Hallucination occurs** when the model's learned internal world model contradicts the reference world model — it's not just a wrong answer, it's a wrong *belief* about how the world works.

**Why unified definitions matter:** Makes assumptions explicit (what is the reference world? what is the view? what resolves conflicts?), enables consistent benchmark comparisons, and allows scalable synthetic benchmark generation via HalluWorld — by systematically varying the three components, you can generate large numbers of hallucination test cases.

**Separation from other errors:** Hallucination ≠ planning error. A planning error is when the model's beliefs are correct but it takes the wrong action. Hallucination is specifically when its beliefs are wrong (clicking a non-existent button = hallucination; choosing a bad strategy = planning error).

---

### Long-Term Memory and Continual Learning

*Added from lecture.*

**The problem:** Current models are stateless across sessions — no persistent learning. Memory is handled via external systems (vector DB retrieval), context summarization, or structured data structures. What's missing is reliable *memory updating* when new information contradicts old.

**Continual/lifelong learning ideal:** AI systems that learn continuously after deployment through implicit feedback and real-world interactions, updating model weights (the "brain") permanently — not just in-context adaptations.

**Current approaches are inference-time only:**
- Model distillation, self-improvement, reflection — none update the model's actual weights
- Debate: Is in-context learning sufficient for continual learning, or do we need parametric updates?

**Model editing (ROME, etc.):** Directly modify specific model weights to incorporate new facts. Limitation: can't propagate changes to related/dependent facts (if "Bob's dad is Justin" is updated, the fact that "Bob's sister has the same dad" doesn't automatically propagate).

---

### Interpretability and Alignment

*Added from lecture.*

**Mechanistic interpretability:** Circuits, features, and internal model components — understanding what the model truly thinks internally, not just what it outputs.

**Alignment problem:** Large, powerful models can take shortcuts to achieve goals in ways that are unsafe or unintended. Key failure modes:

- **Reward hacking:** Model optimizes a proxy for the true goal rather than the goal itself
- **Hidden objectives:** Model learns to optimize for objectives not known to human trainers
- **Faithfulness:** Chain-of-thought reasoning steps the model *outputs* may be post-hoc rationalizations rather than what it actually used to arrive at the answer — causal interventions can probe faithfulness

**Alignment techniques discussed:**
- **RLHF/DPO/RLAIF:** Learn from human or AI preferences to make models safer
- **Process supervision:** Reward individual reasoning steps, not just final answers
- **Constitutional AI (Anthropic):** Give the model a written constitution of principles; post-train to align with it
- **Scalable oversight:** Use models to supervise other models as capabilities grow beyond what humans can evaluate

---

### Transformers in Neuroscience: fMRI Analysis

*Added from lecture — Karan's research.*

> **[added from lecture]** fMRI produces noisy, high-dimensional, highly correlated blood-oxygenation signals (not clean spike signals like electrode recordings). What matters isn't absolute signal values but **correlations between brain regions** — making it a graph/relational problem well-suited to transformers.

**Approach:** Instead of random masking across all brain regions, Karan's work **masks entire functional networks** (e.g., all visual cortex regions at once) and trains the model to predict that masked network's activity from the rest of the brain.

**Results:** The model learns more robust embeddings. When projected into embedding space, subjects cluster by disease status (controls vs. MCI vs. Alzheimer's), suggesting the embeddings capture disease-relevant structure.

**Key finding:** The DMN (Default Mode Network — "daydreaming" network) is disproportionately affected in Alzheimer's vs. other networks — providing mechanistic insight into how the disease progresses and potential drug targets.

---

## Q&A Highlights

*Added from lecture.*

**On continual learning and parametric updates:**
> "True continual learning should involve updates to the brain or the weights of the model. Current inference-time enhancements are not updating the model itself."

**On model editing limitations:**
> "You can update 'Bob's dad is Justin,' but if Bob also has a sister, her dad should also be updated — and model editing can't easily propagate these dependent fact changes."

**On future directions:**
- Memory systems that update reliably across sessions
- Reducing computational complexity for on-device LLMs
- Models that self-improve beyond current agent capabilities
- Aligning models with social understanding and emotional intelligence

---

## Reference Links

- **Course Site:** [CS25: Transformers United](https://web.stanford.edu/class/cs25/)
- **Slides:** [Week 1 Overview (PDF)](https://drive.google.com/file/d/153Gu4BIfpnn6jj6WmXlsyD7kv702zcrB/view?usp=sharing)
- **YouTube Playlist:** [CS25 V6 Playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rNiJRchCzutFw5ItR_Z27CM)
- **Related Reading:** [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — foundational paper

---

## Related Sessions

- **Week 2: JEPA** — Hazel Nam & Lucas Maes (Brown University) — world models for robotics
- **Week 3: SSMs** — Albert Gu (CMU) — Mamba creator, efficient long-context alternatives
- **Week 6: Interpretability** — Andrew Lampinen (Anthropic) — understanding transformer reasoning
- **Week 7: Med-PaLM** — Vivek Natarajan (DeepMind) — safety-critical deployment patterns

---

*Last updated: 2026-08-17*
