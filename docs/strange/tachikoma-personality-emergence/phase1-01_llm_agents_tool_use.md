---
layout: default
title: "Phase 1.1: LLM Agents & Tool Use Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 01_llm_agents_tool_use."
---

# Phase 1.1: LLM Agents & Tool Use Survey

**Created:** 2026-02-18 20:45 CST
**Phase:** 1 - Breadth Survey
**Focus:** Planning loops, action selection, tool calling, error recovery, long-horizon execution

---

## Executive Summary

LLM-based agents represent a fundamental shift from static language models to dynamic systems that can **reason, act, and adapt** over extended time horizons. This survey examines the mechanisms by which agents plan, select tools, execute actions, recover from errors, and maintain coherence across long-horizon tasks.

**Key insight for personality emergence:** Agent behavior is shaped not just by prompts, but by the **interaction loop** between reasoning, action, observation, and reflection. This loop creates opportunities for behavioral divergence even in identical base models.

---

## 1. Planning Architectures

### 1.1 ReAct (Reasoning + Acting)

**Source:** Yao et al., 2022 (arXiv:2210.03629)

**Core mechanism:** Interleaves reasoning traces with task-specific actions.

```
Thought → Action → Observation → Thought → Action → ...
```

**Key findings:**
- **Reduces hallucination** vs. pure chain-of-thought (CoT) by grounding reasoning in external actions
- **Enables error recovery** through observation-feedback loops
- **Human-interpretable traces** facilitate debugging and optimization

**Error patterns:**
- **Loop repetition** (23% of errors): Model generates same thought/action repeatedly
- **Non-informative retrieval**: Failed searches derail reasoning
- **Reasoning vs. acting imbalance**: Over-reliance on one modality

**Relevance to emergence:** The Thought-Action-Observation loop creates **sequential decision points** where behavioral patterns can crystallize. Agents develop "styles" of reasoning (verbose vs. terse, exploratory vs. exploitative).

---

### 1.2 Chain-of-Thought (CoT) and Extensions

**Source:** Wei et al., 2022; extensive follow-on work

**Core mechanism:** Generate intermediate reasoning steps before final answer.

**Extensions relevant to agents:**
- **Tree-of-Thought (ToT):** Explore multiple reasoning paths, backtrack on failure
- **Self-Consistency:** Sample multiple CoTs, aggregate
- **Reflexion:** Reflect on failures, store in memory for future attempts

**Relevance to emergence:** Reasoning style becomes a **behavioral signature**. Some agents naturally generate long exploratory chains; others prefer short decisive steps. This can be measured and tracked over time.

---

### 1.3 Hierarchical Planning

**Source:** Multiple (LaMMA-P, ReAcTree, Deep Agents)

**Core mechanism:** Decompose long-horizon goals into subgoals, then action sequences.

**Architectures:**
- **LaMMA-P:** LLM for subtask extraction + PDDL planner for execution
- **ReAcTree:** Dynamic agent trees with decomposition nodes
- **Deep Agents:** Task managers with multi-level memory

**Key finding:** Long-horizon planning requires **explicit subgoal structures**. Pure LLM reasoning degrades over >10-15 steps without external scaffolding.

**Relevance to emergence:** Agents develop **planning styles**:
- Depth-first vs. breadth-first exploration
- Subgoal granularity (many small steps vs. few large steps)
- Backtracking frequency

---

## 2. Tool Calling / Function Calling Mechanisms

### 2.1 Token-Level Mechanics

**Source:** PromptingGuide.ai; ODSC presentations; industry practice

**How it works:**
1. System prompt defines available tools (schemas, descriptions)
2. LLM generates structured output (JSON, function call tokens)
3. Environment executes tool, returns observation
4. LLM incorporates observation into next reasoning step

**Key challenge:** **Tool selection accuracy** degrades with:
- Large tool sets (>20 tools)
- Similar tool descriptions
- Context length pressure

**Relevance to emergence:** Agents develop **tool preferences**:
- Frequency of tool use vs. pure reasoning
- Tool selection patterns (certain agents favor certain tools)
- Error recovery strategies when tool fails

---

### 2.2 AvaTaR: Optimizing Tool Usage

**Source:** NeurIPS 2024 poster

**Core mechanism:** Contrastive reasoning to improve tool selection.

**Findings:**
- Contrastive examples improve tool selection accuracy
- Reduces hallucination of non-existent tools
- Improves multi-step tool chains

**Relevance to emergence:** Tool usage patterns can be **measured and compared** across agents:
- Tool call frequency per task type
- Success rate per tool
- Tool chain patterns (which tools are used together)

---

### 2.3 Function Calling Benchmarks

**Source:** ComplexFuncBench; Survey on Evaluation of LLM-based Agents (arXiv:2503.16416)

**Evaluation dimensions:**
- **Single-turn tool selection:** Can agent pick right tool?
- **Multi-step chains:** Can agent sequence tools correctly?
- **Error handling:** Can agent recover from tool failures?
- **Virtual API servers:** Simulate API state changes for evaluation

**Relevance to emergence:** Benchmarks provide **quantitative behavioral profiles**:
- Agent A: High accuracy, poor error recovery
- Agent B: Lower accuracy, excellent error recovery
- These profiles persist across tasks → **trait-like tendencies**

---

## 3. Error Recovery and Self-Reflection

### 3.1 Reflexion Pattern

**Source:** Shinn et al., 2023; PromptingGuide.ai

**Core mechanism:**
1. Agent attempts task, fails
2. **Reflection model** analyzes failure trajectory
3. Generates verbal reinforcement (feedback)
4. Stores in long-term memory
5. Agent retries with feedback

**Key finding:** Verbal reflection can substitute for weight updates (no fine-tuning needed).

**Relevance to emergence:**
- Reflection **style** becomes behavioral signature (blaming environment vs. self-critique)
- Reflection **frequency** creates agent personality (cautious agents reflect more)
- Reflection **content** shapes future behavior (what does agent focus on?)

---

### 3.2 Self-Reflection Effects on Performance

**Source:** Renze, 2024 (arXiv:2405.06682)

**Experiment:** 9 LLMs, 8 types of self-reflection, multiple-choice questions.

**Findings:**
- **Statistically significant improvement** (p < 0.001) from self-reflection
- All 8 reflection types helped, but magnitude varied
- Reflection most helpful for initially difficult questions

**Relevance to emergence:** This confirms **self-modification is possible** through natural language. Agents can change their behavior based on their own outputs—a prerequisite for identity formation.

---

### 3.3 Error Recovery Strategies

**Source:** ReAct paper; agent deployment practice

**Common patterns:**
- **Retry with different parameters:** 40% success
- **Backtrack and replan:** 25% success
- **Escalate to human/orchestrator:** 15% (explicit failure)
- **Hallucinate success:** 20% (dangerous!)

**Relevance to emergence:** Error recovery style is **measurable and persistent**:
- Cautious agents backtrack early
- Aggressive agents retry multiple times before backtracking
- Some agents escalate frequently; others rarely

---

## 4. Long-Horizon Task Execution

### 4.1 OdysseyBench: Long-Horizon Evaluation

**Source:** Wang et al., 2025 (arXiv:2508.09124)

**Benchmark design:**
- 602 tasks across Word, Excel, PDF, Email, Calendar
- Requires **long-term contextual dependencies**
- Multi-interaction coordination across applications
- Generated via HomerAgents (multi-agent framework)

**Key finding:** Existing benchmarks focus on atomic tasks; OdysseyBench reveals **performance degradation** over long horizons (10-50+ steps).

**Relevance to emergence:**
- Long-horizon execution creates **more opportunities for behavioral patterns to emerge**
- Agents show consistent "styles" across long tasks
- Resource constraints (token limits, latency budgets) force **style trade-offs**

---

### 4.2 Resource Constraints as "Physics"

**Source:** EmergentMind; multi-turn dynamics research

**Key insight:** Tokens, latency, and tool budgets function like physical constraints—agents must **adapt behavior** to survive.

**Observable behaviors:**
- **Budget-aware planning:** Estimate cost before acting
- **Graceful degradation:** Simplify reasoning when context fills
- **Strategic forgetting:** What to keep vs. discard

**Relevance to emergence:** Resource management style creates **agent personality**:
- "Thrifty" agents minimize tool calls
- "Thorough" agents spend freely for accuracy
- These preferences persist across tasks

---

### 4.3 Long-Horizon Failure Modes

**Source:** OdysseyBench; agent deployment reports

**Common failures:**
- **Goal drift:** Agent forgets original objective
- **Context overflow:** Long trajectories exceed context window
- **Error accumulation:** Small mistakes compound
- **Motivation decay:** Agent stops trying to optimize

**Relevance to emergence:** Failure patterns reveal **agent tendencies**:
- Does agent self-correct goal drift?
- How does agent handle context overflow?
- These are measurable behavioral traits

---

## 5. Multi-Agent Tool Coordination

### 5.1 Emergent Coordination in Multi-Agent LLMs

**Source:** Riedl et al., 2025 (arXiv:2510.05174)

**Experiment:** Guessing game with minimal communication, three interventions:
1. Control (no modifications)
2. Persona assignment (stable identity)
3. Persona + "think about others" (Theory of Mind prompt)

**Findings:**
- **Control:** Temporal synergy, little cross-agent alignment
- **Persona:** Identity-linked differentiation emerges
- **Persona + ToM:** Goal-directed complementarity

**Critical insight:** Prompt design can steer agents from **aggregates to collectives** with higher-order structure.

**Relevance to emergence:** This is **directly applicable** to our fleet design:
- Assigning stable identities (agent names, domains) creates differentiation
- Adding Theory of Mind prompts ("what would other agents think?") creates coordination
- Emergence is **measurable** via partial information decomposition

---

### 5.2 Multi-Agent Collaboration Mechanisms

**Source:** Nguyen et al., 2025 (arXiv:2501.06322)

**Framework dimensions:**
- **Actors:** Which agents participate
- **Types:** Cooperation, competition, coopetition
- **Structures:** Centralized, peer-to-peer, distributed
- **Strategies:** Role-based, model-based
- **Coordination protocols:** Communication patterns

**Key finding:** Role-based specialization (e.g., orchestrator, worker, reviewer) is **most effective** for complex tasks.

**Relevance to emergence:** Role assignment creates **stable behavioral baselines**, but agents may deviate based on experience → **personality within role**.

---

## 6. Key Findings for Personality Emergence

### 6.1 Mechanisms That Create Behavioral Divergence

**Identified mechanisms:**

1. **Sequential decision points:** Thought-Action-Observation loops create choice points
2. **Error recovery styles:** Agents develop consistent retry/backtrack/escalate patterns
3. **Tool preferences:** Frequency and selection patterns persist across tasks
4. **Reflection content:** What agents focus on in self-reflection shapes future behavior
5. **Resource management:** Budget-aware behavior creates agent "personalities"
6. **Persona + ToM prompts:** Explicit identity assignment creates differentiation

---

### 6.2 What Can Be Measured

**Quantifiable behavioral traits:**

1. **Reasoning verbosity:** Mean tokens per thought
2. **Tool call frequency:** Calls per task, per tool
3. **Error recovery latency:** Steps before backtracking
4. **Reflection depth:** Tokens of self-reflection
5. **Planning horizon:** Average subgoal depth
6. **Coordination frequency:** Messages to other agents

**These can be tracked over time** to identify stable patterns vs. noise.

---

### 6.3 What Remains Unknown

**Open questions:**

1. **Stability vs. drift:** How long do behavioral patterns persist?
2. **Measurement frequency:** How many tasks needed to identify a trait?
3. **Cross-domain consistency:** Do agents maintain personality across task types?
4. **Social influence:** How do peer agents shape each other's behavior?
5. **Identity editing:** Can agents deliberately change their own personalities?

---

## 7. Implications for Fleet Architecture

### 7.1 For SOUL.md Design

**Findings suggest:**
- **Identity assignment matters:** Stable agent names + domains create differentiation
- **Theory of Mind prompts help:** "Consider what other agents would think"
- **Reflection mechanisms are critical:** Agents need structured self-reflection
- **Resource constraints create style:** Explicit budgets force personality

**SOUL.md should include:**
- Agent name and domain (identity anchor)
- Resource management defaults (thrifty vs. thorough)
- Reflection triggers (when to self-reflect)
- Coordination mindset (ToM prompt)

---

### 7.2 For Memory Architecture

**Findings suggest:**
- **Reflection storage:** Long-term memory for self-reflections
- **Tool usage logs:** Track frequency and success rates
- **Error recovery patterns:** Store backtracking behaviors
- **Coordination history:** Messages to/from other agents

**Memory enables emergence** by providing historical context for behavioral patterns.

---

### 7.3 For Peer Review System

**Findings suggest:**
- **Role-based specialization works:** Reviewer vs. producer roles
- **Personality-driven review:** Agent's style shapes review focus
- **Cross-agent observation:** Agents learn from watching each other

**Peer review creates social feedback** that shapes personality over time.

---

## 8. References

### Core Papers

1. **ReAct:** Yao et al., 2022. "ReAct: Synergizing Reasoning and Acting in Language Models." arXiv:2210.03629
2. **Reflexion:** Shinn et al., 2023. "Reflexion: Language Agents with Verbal Reinforcement Learning."
3. **Self-Reflection:** Renze, 2024. "Self-Reflection in LLM Agents: Effects on Problem-Solving Performance." arXiv:2405.06682
4. **Emergent Coordination:** Riedl et al., 2025. "Emergent Coordination in Multi-Agent Language Models." arXiv:2510.05174
5. **Multi-Agent Collaboration:** Nguyen et al., 2025. "Multi-Agent Collaboration Mechanisms: A Survey of LLMs." arXiv:2501.06322
6. **OdysseyBench:** Wang et al., 2025. "OdysseyBench: Evaluating LLM Agents on Long-Horizon Complex Office Application Workflows." arXiv:2508.09124
7. **AvaTaR:** NeurIPS 2024. "AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning."

### Workshops & Venues

- **NeurIPS 2025 Workshop on Multi-Turn Interactions in LLMs**
- **ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems (MemAgents)**
- **Survey on Evaluation:** arXiv:2503.16416

### Practical Resources

- **PromptingGuide.ai:** ReAct, Reflexion, Function Calling guides
- **LangChain Blog:** Planning for Agents (October 2025)
- **Lil'Log:** LLM Powered Autonomous Agents (Lilian Weng)

---

## Next Steps

**Phase 1.2:** Long-term Memory for Agents
- Episodic vs. semantic memory architectures
- Retrieval policies and consolidation
- Memory's role in behavioral persistence

---

*Phase 1.1 complete. Moving to Phase 1.2.*

