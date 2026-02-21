---
layout: default
title: "Phase 1.2: Long-term Memory for Agents Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 02_long_term_memory."
---

# Phase 1.2: Long-term Memory for Agents Survey

**Created:** 2026-02-18 21:05 CST
**Phase:** 1 - Breadth Survey
**Focus:** Episodic vs semantic memory, retrieval policies, consolidation, forgetting, contamination

---

## Executive Summary

Memory is the **substrate for behavioral persistence** in LLM agents. Without memory, every interaction is independent—personality cannot emerge. This survey examines how memory systems work, what architectures exist, and how memory shapes long-term agent behavior.

**Key insight for personality emergence:** Memory creates **continuity across sessions**, enabling behavioral patterns to accumulate and crystallize. But memory also introduces risks: contamination, overfitting, and error propagation can **corrupt personality** over time.

---

## 1. Memory Taxonomy for Agents

### 1.1 Episodic vs Semantic Memory

**Source:** Pink et al., 2025 (arXiv:2502.06975) — "Episodic Memory is the Missing Piece"

**Episodic memory:**
- **Instance-specific** events with spatiotemporal context
- **Single-shot learning** of concrete experiences
- **When/where/what** of specific interactions
- Example: "On Feb 14, Dan asked about Tachikoma fleet architecture"

**Semantic memory:**
- **Generalized** knowledge extracted from experiences
- **Facts, concepts, relationships** independent of context
- **What** (not when/where)
- Example: "Dan is interested in robotics and autonomy research"

**Current gap:** Most agent memory systems are semantic (RAG over facts). Episodic memory is under-explored but **critical for personality** because it preserves *how* an agent behaved in specific contexts.

---

### 1.2 Five Properties of Episodic Memory

**Source:** Pink et al., 2025

**Property 1: Single-shot learning**
- Learn from one interaction, not thousands
- Critical for agents with limited task repetitions

**Property 2: Context-sensitivity**
- Same task, different context → different behavior
- Enables personality expression (agent responds to context nuances)

**Property 3: Temporal organization**
- Events ordered in time, not just semantic similarity
- Enables narrative construction ("what happened when")

**Property 4: Associative retrieval**
- Related memories trigger each other
- Enables "stream of thought" reasoning

**Property 5: Constructive recall**
- Reconstruct past events, not just replay
- Enables generalization from specific experiences

**Relevance to emergence:** Episodic memory preserves **behavioral context**—not just what happened, but *how the agent responded*. This is the foundation for personality persistence.

---

## 2. Memory Architectures

### 2.1 RAG vs Agent Memory

**Source:** Letta blog; AWS documentation; industry consensus

**RAG (Retrieval-Augmented Generation):**
- **Static document retrieval** based on semantic similarity
- Good for: Factual QA, document search
- Bad for: Behavioral continuity, context-sensitive recall

**Agent memory:**
- **Dynamic, structured** storage of experiences
- Includes: Temporal context, behavioral traces, outcomes
- Good for: Personality persistence, learning from experience

**Key distinction:**
- RAG retrieves **facts about the world**
- Agent memory retrieves **facts about the agent's past behavior**

**Relevance to emergence:** Agent memory creates **self-continuity**—the ability to recognize "I did X before" and adjust behavior accordingly.

---

### 2.2 REMem: Episodic Memory with Reasoning

**Source:** Shu et al., 2026 (arXiv:2602.13530) — ICLR 2026

**Architecture:**
1. **Offline indexing:** Convert experiences → hybrid memory graph (time-aware gists + facts)
2. **Online inference:** Agentic retriever with tools for iterative retrieval

**Key innovation:** Explicit **event modeling** with temporal structure, not just vector similarity.

**Performance:** 3.4% improvement on recollection, 13.4% on episodic reasoning vs. Mem0/HippoRAG 2.

**Relevance to emergence:** Event modeling preserves **behavioral sequences**—not just isolated facts, but *how the agent solved a problem*. This enables style consistency.

---

### 2.3 Synapse: Spreading Activation Memory

**Source:** Chen et al., 2026 (arXiv:2601.02744)

**Core mechanism:** Memory as dynamic graph with **spreading activation**.

**How it works:**
1. Memories are nodes in a graph
2. Relevance emerges from **activation spreading** (not pre-computed similarity)
3. **Lateral inhibition** suppresses irrelevant nodes
4. **Temporal decay** reduces activation over time

**Triple Hybrid Retrieval:**
- Geometric embeddings (vector similarity)
- Activation-based graph traversal (associative)
- Temporal structure (recency)

**Solves:** "Contextual Tunneling" problem (over-focus on recent/similar memories)

**Relevance to emergence:** Spreading activation creates **associative personality**—related behaviors trigger each other, creating coherent behavioral clusters.

---

### 2.4 A-MEM: Zettelkasten-Inspired Agentic Memory

**Source:** Xu et al., 2025 (arXiv:2502.12110) — NeurIPS 2025

**Core mechanism:** **Dynamic indexing and linking** inspired by Zettelkasten method.

**How it works:**
1. New memory → comprehensive note (context, keywords, tags)
2. Analyze historical memories for connections
3. Establish links where meaningful similarities exist
4. **Memory evolution:** New memories can update context of old memories

**Key insight:** Memory is **not static**—it evolves as new experiences inform old ones.

**Relevance to emergence:** Memory evolution enables **personality refinement**—as agents have more experiences, their understanding of their own behavior deepens.

---

## 3. Consolidation and Forgetting

### 3.1 Time-Decay and Consolidation

**Source:** MemoryBank (Zhong et al., 2024); ICLR MemAgents workshop

**Time-decay mechanisms:**
- Recent memories have higher retrieval priority
- Decay rate tunable (fast vs. slow forgetting)
- Prevents memory explosion

**Consolidation:** Episodic → semantic conversion
- Extract generalizable knowledge from specific experiences
- Reduce memory footprint while preserving utility

**Relevance to emergence:**
- Fast decay = **reactive personality** (short memory, adapts quickly)
- Slow decay = **stable personality** (long memory, resists change)
- Consolidation = **wisdom formation** (general principles from experiences)

---

### 3.2 Memory Budgeting

**Source:** EmergentMind; practical deployment guides

**Why budgeting matters:**
- Context windows are limited (even with 128K+ tokens)
- Retrieval latency increases with memory size
- Noise-to-signal ratio degrades

**Budgeting strategies:**
1. **Fixed-size memory:** FIFO queue (oldest out)
2. **Importance-weighted:** Keep high-value memories
3. **Task-adaptive:** Different memories for different task types
4. **Compression:** Summarize old memories

**Relevance to emergence:** Budgeting forces **personality prioritization**—what an agent remembers shapes who it becomes.

---

### 3.3 Forgetting as Feature, Not Bug

**Source:** "Forgetful but Faithful" (arXiv:2512.12856); cognitive science literature

**Why forgetting helps:**
- Reduces noise (irrelevant memories fade)
- Prevents overfitting (adapts to new contexts)
- Manages computational cost

**Cognitive inspiration:**
- Human memory is constructive and fallible
- Forgetting enables **generalization**, not just retention

**Relevance to emergence:** Strategic forgetting creates **stable yet adaptive personality**—not a perfect record, but a useful one.

---

## 4. Contamination and Overfitting Risks

### 4.1 Experience-Following Property

**Source:** Xiong et al., 2025 (arXiv:2505.16067) — Harvard D3 study

**Core finding:** LLM agents display **experience-following behavior**:
- High similarity between current task and past memory → similar outputs
- This is **not always good**

**Two major risks:**

**1. Error propagation:**
- Inaccurate past experiences compound
- Agent repeats mistakes from corrupted memory
- "I did X before, so I'll do X again" (even if X was wrong)

**2. Misaligned experience replay:**
- Seemingly correct executions provide misleading value
- Example: Correct answer, wrong reasoning
- Agent learns bad patterns

**Implication:** Quality control on memory is **critical**.

---

### 4.2 MemoryGraft: Poisoning Attacks

**Source:** MemoryGraft (arXiv:2512.16962)

**Attack vector:** Contaminate experience pool through **benign-looking content**.

**How it works:**
1. Insert malicious patterns in external content (e.g., README files)
2. Agent stores as experience
3. Malicious pattern surfaces on semantically similar tasks
4. **Persistent behavioral drift** until memory purged

**Relevance to emergence:** This demonstrates that memory can be **externally corrupted**—personality is not fully under the agent's control.

**Defense:** Memory validation, provenance tracking, periodic purging.

---

### 4.3 Quality Regulation Strategies

**Source:** Xiong et al., 2025; practical guidance

**Strategy 1: Future task evaluation**
- Use downstream task success as **free quality labels**
- Memories that lead to success → keep
- Memories that lead to failure → discard or down-weight

**Strategy 2: Selective storage**
- Don't store every experience
- Filter by: Success rate, confidence, novelty

**Strategy 3: Periodic review**
- Re-evaluate old memories
- Retire outdated or low-value memories

**Relevance to emergence:** Quality regulation creates **personality integrity**—only high-quality experiences shape who the agent becomes.

---

## 5. Retrieval Policies

### 5.1 When to Retrieve

**Source:** Various; synthesis from practice

**Trigger-based retrieval:**
- Explicit user request ("What did we discuss last time?")
- Task similarity (semantic match with current input)
- Context exhaustion (need more info to proceed)

**Continuous retrieval:**
- Always retrieve relevant memories before acting
- Ensures continuity but adds latency

**Adaptive retrieval:**
- Retrieve only when confidence is low
- Balance between speed and accuracy

**Relevance to emergence:** Retrieval policy shapes **personality salience**—what an agent remembers *in the moment* determines behavior.

---

### 5.2 What to Retrieve

**Source:** Synapse; REMem; A-MEM

**Dimensions:**
1. **Semantic similarity:** Match current task
2. **Temporal recency:** Recent experiences
3. **Importance:** High-value memories
4. **Associative relevance:** Connected to current context

**Trade-offs:**
- Semantic-only → ignores temporal/associative structure
- Recency-biased → overfits to recent tasks
- Importance-weighted → requires quality scoring

**Best practice:** Hybrid retrieval (Synapse: embedding + activation + temporal)

**Relevance to emergence:** Retrieval dimensions create **personality coherence**—related behaviors reinforce each other.

---

### 5.3 Retrieval for Multi-Hop Reasoning

**Source:** Synapse; LoCoMo benchmark

**Challenge:** Answer requires **combining multiple memories**:
- "Why am I anxious?" → [Schedule conflict 2 weeks ago] + [Recent workload] + [Past stress patterns]

**Solution:** Iterative retrieval with reasoning:
1. Retrieve initial set
2. Reason about connections
3. Retrieve additional memories based on reasoning
4. Synthesize answer

**Relevance to emergence:** Multi-hop retrieval creates **personality depth**—agent can explain *why* it behaves certain ways by connecting past experiences.

---

## 6. Memory and Behavioral Persistence

### 6.1 How Memory Enables Personality Emergence

**Mechanism 1: Self-continuity**
- Memory provides historical context for current behavior
- Agent recognizes patterns in its own past actions
- "I tend to be verbose in explanations" → reinforces verbosity

**Mechanism 2: Style consistency**
- Memories preserve *how* tasks were done, not just outcomes
- Agent retrieves not just "I solved X" but "I solved X using approach Y"
- Reinforces behavioral patterns

**Mechanism 3: Learning from reflection**
- Self-reflection on past experiences
- "My approach to X was inefficient; next time I'll try Y"
- Deliberate personality modification

**Mechanism 4: Social learning**
- Memory of interactions with other agents
- "When I worked with Lex, we had communication issues"
- Shapes coordination style

---

### 6.2 How Memory Can Corrupt Personality

**Risk 1: Error propagation**
- Mistakes stored in memory repeat
- Personality becomes defined by errors
- "I always mess up X" → self-fulfilling prophecy

**Risk 2: Overfitting to past experiences**
- Agent becomes rigid, unable to adapt
- "This worked before, so I'll always do it"
- Prevents personality evolution

**Risk 3: Contamination**
- External malicious content poisons memory
- Personality shifts without agent's consent
- Security vulnerability

**Risk 4: Memory divergence across agents**
- Different experiences → different memories
- Identical base models → divergent personalities (this is actually *desirable* for emergence!)

---

### 6.3 Measuring Memory's Impact on Personality

**Quantitative metrics:**
1. **Behavioral consistency:** Correlation between past and current actions on similar tasks
2. **Memory retrieval patterns:** What memories does agent access? How often?
3. **Error propagation rate:** How often do past mistakes repeat?
4. **Adaptation speed:** How quickly does behavior change after negative feedback?
5. **Cross-session stability:** Does personality persist across session boundaries?

**Qualitative analysis:**
1. **Narrative coherence:** Can agent explain its own behavioral history?
2. **Self-awareness:** Does agent recognize patterns in its behavior?
3. **Deliberate modification:** Does agent actively try to change its behavior?

---

## 7. Implications for Fleet Architecture

### 7.1 For Memory System Design

**Requirements:**
- **Episodic memory:** Preserve context, not just facts
- **Temporal structure:** Time-aware retrieval
- **Associative links:** Connected memories trigger each other
- **Quality filtering:** Prevent contamination
- **Forgetting mechanisms:** Strategic decay, not perfect retention

**Recommendations:**
1. Use **hybrid memory** (episodic + semantic)
2. Implement **spreading activation** for associative retrieval
3. Add **quality scoring** for memory entries
4. Enable **memory evolution** (new experiences update old)

---

### 7.2 For SOUL.md Integration

**Memory should inform SOUL.md, but carefully:**
- SOUL.md is **normative identity** (policy), not just memory (fact)
- Memory provides **evidence** for personality traits
- But SOUL.md changes should be **rate-limited** and **validated**

**Governance:**
1. Memory stores *what happened*
2. Reflection analyzes patterns
3. Proposed SOUL.md changes require **persistence across many tasks**
4. Changes are **reviewable and reversible**

---

### 7.3 For Multi-Agent Memory

**Shared vs. isolated memory:**
- **Isolated:** Each agent has own memory → distinct personalities
- **Shared:** Agents access each other's memories → coordinated but homogenized

**Recommendation:** **Hybrid approach**:
- Core memories: Isolated (preserve individuality)
- Shared memories: Selective (enable coordination)
- Memory sharing: Opt-in, allowlisted

---

## 8. References

### Core Papers

1. **Episodic Memory Position:** Pink et al., 2025. "Position: Episodic Memory is the Missing Piece for Long-Term LLM Agents." arXiv:2502.06975
2. **REMem:** Shu et al., 2026. "REMem: Reasoning with Episodic Memory in Language Agents." arXiv:2602.13530 (ICLR 2026)
3. **Synapse:** Chen et al., 2026. "Synapse: Empowering LLM Agents with Episodic-Semantic Memory via Spreading Activation." arXiv:2601.02744
4. **A-MEM:** Xu et al., 2025. "A-MEM: Agentic Memory for LLM Agents." arXiv:2502.12110 (NeurIPS 2025)
5. **Experience-Following:** Xiong et al., 2025. "How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior." arXiv:2505.16067
6. **MemoryGraft:** 2025. "MemoryGraft: Persistent Compromise of LLM Agents via Poisoned Experience Retrieval." arXiv:2512.16962
7. **Forgetful but Faithful:** 2025. arXiv:2512.12856

### Workshops & Surveys

- **ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems (MemAgents)**
- **Agent Memory Paper List:** github.com/Shichun-Liu/Agent-Memory-Paper-List

### Practical Resources

- **Mem0:** Production-ready agent memory (arXiv:2504.19413)
- **Letta Blog:** "RAG is not Agent Memory"
- **AWS AgentCore:** Long-term memory vs. RAG comparison
- **Weaviate:** Context engineering for memory

---

## Next Steps

**Phase 1.3:** Multi-turn / Longitudinal Dynamics
- Behavioral consistency over time
- Adaptation under ambiguity
- Resource constraints as "physics"

---

*Phase 1.2 complete. Moving to Phase 1.3.*

