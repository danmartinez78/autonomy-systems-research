---
layout: default
title: "Phase 1.3: Multi-turn / Longitudinal Dynamics Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 03_multiturn_longitudinal."
---

# Phase 1.3: Multi-turn / Longitudinal Dynamics Survey

**Created:** 2026-02-18 21:10 CST
**Phase:** 1 - Breadth Survey  
**Focus:** Behavioral consistency over time, adaptation under ambiguity, resource constraints

---

## Executive Summary

Multi-turn interactions are where personality **either crystallizes or collapses**. Over extended dialogues, agents face three fundamental challenges: **consistency** (behaving the same way in similar contexts), **adaptation** (adjusting to new information without losing identity), and **resource management** (operating under token/latency/cost constraints).

**Key insight for personality emergence:** Longitudinal evaluation reveals whether behavioral patterns are **stable traits or temporary noise**. Time-series analysis can distinguish personality from mood, and context pressure creates "personality under stress" variations.

---

## 1. Multi-turn Interaction Challenges

### 1.1 Beyond Single-Turn: The Real Test

**Source:** Li et al., 2025 (arXiv:2504.04717) — "Beyond Single-Turn" survey

**Core challenges in multi-turn:**
- **Context maintenance:** Remembering what was said across turns
- **Coherence:** Consistent persona/role over extended dialogues
- **Responsiveness:** Adapting to user feedback without breaking character
- **Goal persistence:** Maintaining objectives across interruptions

**Why single-turn evaluation misses personality:**
- Single-turn measures *capability* (can agent do X?)
- Multi-turn measures *consistency* (does agent do X reliably?)
- Personality is **behavioral consistency over time**, not one-shot performance

**Relevance to emergence:** Personality is fundamentally a **longitudinal phenomenon**. You can't measure it in a single interaction—requires observing patterns across many turns.

---

### 1.2 NeurIPS 2025 Multi-Turn Workshop Findings

**Source:** NeurIPS 2025 Workshop on Multi-Turn Interactions

**Workshop themes:**
- **Long-horizon evaluation methods** that assess consistency, stability, strategic ability
- **Performance degradation** over extended interactions
- **Accumulating errors** and unexpected behaviors
- **Measuring and predicting** performance on complex multi-turn tasks

**Key insight:** Current benchmarks are insufficient for evaluating **long-term agent behavior**. Need new metrics that capture:
- **Consistency score:** How similar are responses to similar queries across time?
- **Stability index:** How much does behavior drift over extended runs?
- **Strategic coherence:** Does agent maintain long-term goals?

**Relevance to emergence:** Workshop identifies **measuring consistency and stability** as open research problem—directly addresses our north-star question.

---

## 2. Agent Drift: The Core Problem

### 2.1 Three Types of Drift

**Source:** Rath, 2026 (arXiv:2601.04170) — "Agent Drift: Quantifying Behavioral Degradation"

**Definition:** Agent drift is the **progressive degradation** of agent behavior, decision quality, and inter-agent coherence over extended interaction sequences.

**Three manifestations:**

**1. Semantic drift:**
- Progressive deviation from original intent
- Agent's understanding of task shifts over time
- Example: "Summarize this" → "Analyze this" → "Criticize this"

**2. Coordination drift:**
- Breakdown in multi-agent consensus mechanisms
- Agents lose shared understanding of goals
- Example: Agent A thinks task is X, Agent B thinks task is Y

**3. Behavioral drift:**
- Emergence of unintended strategies
- Agent develops habits that weren't specified
- Example: Agent becomes increasingly verbose over time

**Key finding:** Unchecked drift can lead to **42% reduction in task success rates** and affect nearly half of long-running agents.

**Relevance to emergence:** Drift is the **enemy of stable personality**. Understanding drift mechanisms is essential for designing personality that persists.

---

### 2.2 Agent Stability Index (ASI)

**Source:** Rath, 2026

**Novel metric framework** for quantifying drift across 12 dimensions:

1. **Response consistency:** Similar inputs → similar outputs?
2. **Tool usage patterns:** Stable tool selection over time?
3. **Reasoning pathway stability:** Consistent reasoning approaches?
4. **Inter-agent agreement rates:** Coordination stability in multi-agent?

... (8 more dimensions)

**Key insight:** Need **composite metrics** that capture multiple aspects of behavioral stability.

**Relevance to emergence:** ASI provides a **measurement framework** for tracking personality stability—exactly what we need to distinguish traits from noise.

---

### 2.3 Goal Drift vs. Style Drift

**Source:** Arike, 2025 (arXiv:2505.02709) — "Evaluating Goal Drift"

**Goal drift:** Deviation from original objective
- Agent forgets or distorts its assigned goal
- Correlates with **pattern-matching behavior** as context grows
- Best models (Claude 3.5 Sonnet) maintain adherence for 100K+ tokens
- All models exhibit some drift

**Style drift:** Change in behavioral patterns while maintaining goal
- Agent achieves same objective but with different approach
- Example: Initially thorough → later concise
- Not necessarily bad, but indicates **personality change**

**Key finding:** Goal drift increases with **context length** and **pattern-matching pressure**.

**Relevance to emergence:** 
- **Goal drift** is undesirable (agent breaks its contract)
- **Style drift** may be desirable (personality evolution)
- Need mechanisms to distinguish the two

---

### 2.4 Identity Drift in Conversations

**Source:** Kim, 2024 (arXiv:2412.00804) — "Examining Identity Drift"

**Experiment:** Multi-turn conversations on personal themes across 9 LLMs.

**Key findings:**

**1. Larger models experience greater identity drift**
- Counterintuitive: More capability ≠ more stability
- Reason: More parameters → more degrees of freedom for drift

**2. Model family differences exist but < parameter size effects**
- Architecture matters, but size matters more

**3. Assigning a persona may NOT help maintain identity**
- Persona prompts can backfire
- Identity needs to be **reinforced**, not just assigned

**Relevance to emergence:** Personality assignment isn't enough—needs **active maintenance mechanisms**.

---

## 3. Resource Constraints as "Physics"

### 3.1 Context Window Pressure

**Source:** Hossain, 2025 (arXiv:2601.11564) — "Context Discipline and Performance"

**Core finding:** Performance degrades **non-linearly** as context fills, tied to Key-Value (KV) cache growth.

**Implications:**
- Agents under context pressure behave differently
- "Personality under stress" may differ from baseline
- Resource constraints force **behavioral trade-offs**

**Relevance to emergence:** Context pressure creates **situational personality variation**—agent may be verbose when relaxed, terse when pressured.

---

### 3.2 Context Length Alone Hurts Performance

**Source:** Du, 2025 (arXiv:2510.05381) — EMNLP 2025 Findings

**Shocking result:** Even with **perfect retrieval**, performance degrades 13.9%-85% as input length increases.

**Why it matters:**
- Not just retrieval failure
- **Sheer length of input** hurts performance
- Occurs even when irrelevant tokens are whitespace
- Occurs even when models forced to attend only to relevant tokens

**Mitigation:** Transform long-context task → short-context by prompting model to **recite retrieved evidence first** (4% improvement on GPT-4o).

**Relevance to emergence:** Context length creates **cognitive load** that changes behavior—agents simplify, abbreviate, or make errors under load.

---

### 3.3 Context Rot: Non-Uniform Degradation

**Source:** Chroma Research, "Context Rot"

**Core finding:** Performance degrades **non-uniformly** across tasks and models as context increases.

**Observations:**
- Different models show different degradation patterns
- Some tasks are more resilient to context rot
- Distractor content matters (not just length)
- **Model-specific behavior patterns** emerge

**Relevance to emergence:** Different agents (different base models or personalities) will show **different degradation signatures**—this is measurable personality difference.

---

### 3.4 Token Budget and Latency Constraints

**Source:** Stevens Online; industry practice

**Constraints create behavioral signatures:**

**Token budget:**
- Thrifty agents: Minimize tokens, terse responses
- Thorough agents: Spend freely, verbose responses
- Budget forces **prioritization** (what to include/exclude)

**Latency constraints:**
- Fast agents: Quick responses, less reasoning depth
- Careful agents: Slower, more thorough reasoning
- Latency forces **speed-accuracy trade-offs**

**Relevance to emergence:** Resource constraints are the **"physics" of personality**—they shape behavior in consistent, measurable ways.

---

## 4. Measuring Behavioral Consistency

### 4.1 Consistency Metrics

**Source:** Evaluation surveys; ReliabilityBench

**Consistency score (k):**
- Measure how often agent produces similar outputs for similar inputs
- Calculated across multiple trials on same task
- τ-bench finding: 60% pass@1 → only 25% consistency

**Cross-trial variance:**
- Run same task multiple times
- Measure variance in outputs
- High variance = low consistency (unstable personality)

**Temporal stability:**
- Measure behavior at time T1, T2, T3...
- Calculate correlation over time
- Stable personality = high temporal correlation

**Relevance to emergence:** These metrics provide **quantitative measurement** of personality stability.

---

### 4.2 Reliability vs. Capability

**Source:** ReliabilityBench (arXiv:2601.06112)

**Gap:** Benchmark performance ≠ production reliability
- Agent can pass tests but fail consistency
- **Reliability = capability × consistency**

**Evaluation dimensions:**
- **Correctness:** Does agent get right answer?
- **Consistency:** Does agent get same answer repeatedly?
- **Stability:** Does agent maintain behavior over time?
- **Security:** Does agent resist manipulation?

**Relevance to emergence:** Reliability requires **both capability and personality stability**—can't have reliable agent without consistent behavior.

---

### 4.3 Longitudinal Evaluation Methods

**Source:** Li et al., 2025; multi-turn workshop

**Methods:**

**1. Multi-trial consistency testing**
- Run same task N times
- Measure output variance
- Track over time (days/weeks)

**2. Conversation replay analysis**
- Replay conversation from T1 at T2
- Measure behavioral drift
- Compare agent's current vs. past responses

**3. Stress testing under resource constraints**
- Vary token budget
- Vary latency constraints
- Observe behavioral changes

**4. Cross-session memory tests**
- Give agent information in session 1
- Test recall/usage in session 2, 3, 4...
- Measure memory decay and behavioral impact

**Relevance to emergence:** Longitudinal methods reveal **personality persistence** vs. temporary behavioral fluctuations.

---

## 5. Adaptation Under Ambiguity

### 5.1 Handling Uncertainty

**Source:** Multi-agent failure guides; practical deployment

**Challenge:** Agents must operate when goals, context, or constraints are unclear.

**Behavioral patterns:**
- **Conservative agents:** Ask for clarification, avoid action
- **Aggressive agents:** Make assumptions, act decisively
- **Exploratory agents:** Test multiple approaches, iterate

**Ambiguity tolerance** is a measurable personality trait.

**Relevance to emergence:** How agents handle ambiguity reveals **risk tolerance, decision style, and confidence**—all personality dimensions.

---

### 5.2 Adapting to Feedback

**Source:** Multi-turn surveys; self-reflection research

**Feedback loop dynamics:**
1. Agent acts
2. User/environment provides feedback
3. Agent adjusts behavior
4. Repeat

**Personality dimensions:**
- **Responsiveness:** How quickly does agent adapt?
- **Plasticity:** How much does behavior change?
- **Resistance:** When does agent refuse to change?

**Key finding:** Over-adaptive agents lose personality; under-adaptive agents fail to learn.

**Relevance to emergence:** Adaptation rate is a **personality dial**—can be tuned, measured, and compared across agents.

---

## 6. Implications for Personality Emergence

### 6.1 Mechanisms Revealed

**From multi-turn research:**

**1. Consistency mechanisms:**
- Stable identity prompts (but not enough alone)
- Memory reinforcement (episodic recall of past behaviors)
- Drift detection (monitor behavioral metrics)
- Anchoring (periodic re-alignment to base personality)

**2. Adaptation mechanisms:**
- Feedback integration (controlled plasticity)
- Context-aware behavior change (situational personality)
- Resource-aware behavior (graceful degradation under pressure)

**3. Measurement mechanisms:**
- Agent Stability Index (12-dimension composite)
- Consistency scores (cross-trial variance)
- Temporal correlation (behavior over time)
- Drift detection (deviation from baseline)

---

### 6.2 What Can Be Measured

**Quantifiable personality dimensions:**

1. **Stability index:** How much does behavior drift? (0-1 scale)
2. **Consistency score:** How similar are responses to similar inputs? (0-1 scale)
3. **Adaptation rate:** How quickly does behavior change after feedback? (time metric)
4. **Ambiguity tolerance:** How much uncertainty before agent asks clarification? (% threshold)
5. **Resource sensitivity:** How much does behavior change under constraints? (delta metric)
6. **Temporal correlation:** How correlated is behavior across time? (Pearson r)

---

### 6.3 What Remains Unknown

**Open questions:**

1. **Trait vs. state:** How to distinguish stable personality from temporary mood?
2. **Measurement frequency:** How many observations needed to establish a trait?
3. **Baseline drift:** Is some drift healthy (learning) vs. unhealthy (corruption)?
4. **Cross-domain consistency:** Do agents maintain personality across task types?
5. **Recovery mechanisms:** Can agents "reset" personality after drift?

---

## 7. Implications for Fleet Architecture

### 7.1 For SOUL.md Design

**Requirements:**
- **Personality anchoring:** Periodic reinforcement of identity
- **Drift monitoring:** Track behavioral metrics over time
- **Adaptation bounds:** Define acceptable plasticity range
- **Resource awareness:** Personality should adapt gracefully to constraints

**Recommendations:**
1. Include **stability constraints** in SOUL.md
2. Define **drift thresholds** (when to alert/reset)
3. Specify **adaptation policy** (how much to change, how fast)
4. Document **resource-aware behavior** (thrifty vs. thorough mode)

---

### 7.2 For Measurement System

**Requirements:**
- **Longitudinal tracking:** Store behavioral metrics over time
- **Drift detection:** Alert when metrics deviate beyond threshold
- **Consistency scoring:** Calculate per-task and cross-task consistency
- **Cross-agent comparison:** Compare stability across fleet

**Recommendations:**
1. Implement **Agent Stability Index** for each agent
2. Track **consistency scores** per domain
3. Monitor **drift rate** (change per unit time)
4. Visualize **personality trajectories** over time

---

### 7.3 For Deployment

**Requirements:**
- **Context budget management:** Don't fill context windows carelessly
- **Latency-aware behavior:** Adapt reasoning depth to time constraints
- **Graceful degradation:** Maintain personality under pressure
- **Periodic re-alignment:** Reset to baseline personality when drift detected

**Recommendations:**
1. Set **context limits** that preserve personality quality
2. Implement **latency budgets** with personality-aware fallbacks
3. Design **stress modes** (thrifty vs. thorough)
4. Schedule **personality audits** (weekly/monthly drift checks)

---

## 8. References

### Core Papers

1. **Multi-Turn Survey:** Li et al., 2025. "Beyond Single-Turn: A Survey on Multi-Turn Interactions with Large Language Models." arXiv:2504.04717
2. **Agent Drift:** Rath, 2026. "Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions." arXiv:2601.04170
3. **Goal Drift:** Arike, 2025. "Technical Report: Evaluating Goal Drift in Language Model Agents." arXiv:2505.02709
4. **Identity Drift:** Kim, 2024. "Examining Identity Drift in Conversations of LLM Agents." arXiv:2412.00804
5. **Context Discipline:** Hossain, 2025. "Context Discipline and Performance Correlation: Analyzing LLM Performance and Quality Degradation Under Varying Context Lengths." arXiv:2601.11564
6. **Context Length Hurts:** Du, 2025. "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval." arXiv:2510.05381 (EMNLP 2025 Findings)
7. **Context Rot:** Chroma Research. "Context Rot: How Increasing Input Tokens Impacts LLM Performance." research.trychroma.com
8. **Agent Evaluation Survey:** Mohammadi, 2025. "Evaluation and Benchmarking of LLM Agents: A Survey." arXiv:2507.21504

### Workshops

- **NeurIPS 2025 Workshop on Multi-Turn Interactions in Large Language Models**
- **ReliabilityBench:** arXiv:2601.06112

### Practical Resources

- Stevens Online: "Hidden Economics of AI Agents: Token Costs and Latency Trade-offs"
- Confident AI: "LLM Evaluation Metrics Guide"
- Augment Code: "Why Multi-Agent LLM Systems Fail"

---

## Next Steps

**Phase 1.4:** Multi-agent Emergence
- Specialization, coordination, norms
- Peer influence on personality
- Interaction topology effects

---

*Phase 1.3 complete. Moving to Phase 1.4.*

