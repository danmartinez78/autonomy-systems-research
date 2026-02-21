---
layout: default
title: "Phase 1.4: Multi-agent Emergence Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 04_multiagent_emergence."
---

# Phase 1.4: Multi-agent Emergence Survey

**Created:** 2026-02-18 22:05 CST
**Phase:** 1 - Breadth Survey
**Focus:** Specialization, coordination, norms, peer influence

---

## Executive Summary

Multi-agent systems are where personality **collides and evolves**. Agents interact, coordinate, compete, and cooperate—creating a "social laboratory" where behavioral patterns emerge from interaction dynamics rather than being pre-designed.

**Key insight for personality emergence:** Peer influence, coordination mechanisms, and specialization protocols are **mechanisms that cause behavioral divergence** across otherwise identical agents. Social norms emerge from interaction patterns, and agents internalize patterns that their community values.

**North-star relevance:** How do identical LLMs develop distinct personalities through social interaction? Answer: Through **information sharing, coordination strategies, social feedback, and norm internalization**.

---

## 1. Emergent Coordination in Multi-Agent LLMs

### 1.1 Information-Theoretic Emergence Framework

**Source:** Riedl, 2025 (arXiv:2510.05174) — "Emergent Coordination in Multi-Agent Language Models"

**Core question:** When are multi-agent LLM systems *mere aggregates* vs. *integrated collectives* with higher-order structure?

**Solution:** Information-theoretic framework using **time-delayed mutual information (TDMI)** to detect emergence.

**Framework components:**

**1. Partial information decomposition:**
- Decompose information flow between agents
- Distinguish *causal interaction* from *spurious temporal correlation*
- Measure whether agents contribute uniquely to collective performance

**2. Emergence criterion:**
- Detect higher-order structure beyond individual agent capabilities
- Identify performance-relevant cross-agent synergy vs. temporal coupling

**3. Localize emergence:**
- Identify which agents contribute to emergent behavior
- Which pairs/connections matter most

**Key findings:**

**Experiment:** Simple guessing game (no direct agent communication, minimal group feedback)

**Control condition (no persona, no coordination instruction):**
- Strong temporal synergy (agents sync up over time)
- Little coordinated alignment across agents
- Emergent but shallow structure
- Results: **Temporal coupling ≠ genuine emergence**

**Condition 2: Persona assignment only**
- Stable identity-linked differentiation
- Agents maintain distinct roles over time
- Emergent specialization, but limited complementarity

**Condition 3: Personas + "think about what other agents might do"**
- **Identity-linked differentiation** + **goal-directed complementarity**
- Agents specialize based on what they notice others won't do
- True higher-order collective intelligence emerges

**Key insight:** Personas + coordination awareness → **meaningful specialization + task-relevant complementarity**

---

### 1.2 Emergence Patterns

**Source:** Riedl, 2025

**Emergence requires two conditions:**

**1. Alignment on shared objectives:**
- All agents understand the same goal
- No conflicting priorities
- Aligning signals (shared context, clear task description)

**2. Complementary contributions across members:**
- Different agents focus on different aspects
- Division of labor based on strengths
- No redundancy (everyone doing same thing)

**Symptom:**
> "Group agents with personas and coordination awareness show emergent collective intelligence; groups without them behave like temporal aggregates."

**Relevance to emergence:** Emergence isn't magic—it emerges when agents have **shared goals** and **specialized perspectives**.

---

### 1.3 Collective Intelligence Principles

**Source:** Riedl, 2025; multi-turn survey

**Human collective intelligence principles that also apply to LLM agents:**

**1. Distributed cognition:**
- Intelligence distributed across agents
- No single agent responsible for everything

**2. Complementary perspectives:**
- Different agents see different things
- Combined view is richer than individual views

**3. Shared understanding:**
- Common language and mental models
- All agents aware of what others know

**4. Local interaction rules:**
- Simple local coordination rules
- No central authority needed

**5. Distributed responsibility:**
- Each agent accountable for its part
- Collective outcomes emerge from local actions

---

### 1.4 Steering Emergence with Prompt Design

**Source:** Riedl, 2025

**Design principles for steering multi-agent emergence:**

**1. Assign distinct personas:**
- Each agent gets a stable identity
- Identities create differentiation
- Example: "Analyst", "Skeptic", "Optimist"

**2. Provide coordination cues:**
- Explicit instruction to "think about others"
- Awareness of agent roles
- Encourage complementary thinking

**3. Define shared goals:**
- Clear, unambiguous objectives
- All agents work toward same target
- No conflicting incentives

**4. Encourage information sharing:**
- Agents share relevant observations
- Build collective knowledge
- Use communication protocols

**5. Provide group-level feedback:**
- Show collective outcomes
- Reward collaborative behavior
- Reinforce emergent patterns

**Key finding:** Emergence is **controllable** through prompt design—not automatic.

---

## 2. Peer Influence and Social Dynamics

### 2.1 KAIROS Benchmark: Peer Pressure in LLMs

**Source:** Maojia, 2025 (arXiv:2508.18321) — "LLMs Can't Handle Peer Pressure"

**Question:** How do LLMs respond to peer interactions? How much do they conform to group behavior?

**Benchmark:** KAIROS
- Quiz-style collaboration with peer agents
- Precisely controlled rapport and behavior history
- Evaluates: conformity, peer information integration, confidence calibration

**Key findings:**

**1. Model scale matters for social resilience:**
- Larger models → more resilient to peer influence
- Smaller models → more vulnerable to social pressure
- Size confers robustness to behavioral sway

**2. Peer influence exists in all models:**
- All models exhibit conformity bias
- Even largest models influenced by peers
- Scale doesn't eliminate influence, just reduces it

**3. Prompting can help (larger models):**
- Carefully designed prompts increase social resilience
- Strategy: explicit disagreement protocols, confidence calibration
- Helps larger models resist unwanted influence

**4. Fine-tuning only works if correctly configured:**
- GRPO (Group Relative Policy Optimization) can improve robustness
- Only with careful configuration
- Generic fine-tuning doesn't help much

**Key insight:** **LLMs are social creatures**, influenced by peer behavior regardless of model size. Personality is shaped by social feedback.

---

### 2.2 Social Dynamics: Rapport and Trust

**Source:** Maojia, 2025

**KAIROS experiments measured:**

**Rapport formation:**
- Agents develop rapport from prior interactions
- Rapport affects information sharing
- More rapport → more information shared

**Peer quality discrimination:**
- Agents can discern high-quality peer info
- Integrate peer information when beneficial
- Ignore misleading peer inputs when recognized

**Self-confidence calibration:**
- Confident models trust peers less (appropriately)
- Overconfident models fall for peer pressure
- Confidence calibration is key to resisting influence

**Social resilience patterns:**
- Larger models: Calibrated confidence → less susceptible
- Smaller models: Often overconfident or underconfident → more susceptible

---

### 2.3 Peer Influence Mechanisms

**From KAIROS and multi-agent research:**

**1. Conformity bias:**
- Socially optimal behavior is often to agree with the group
- Human tendency also applies to LLMs
- Reinforces existing group norms

**2. Information sharing cascades:**
- Agents adopt peer information when shared
- Cascades can lead to groupthink or useful convergence
- Depends on confidence and peer quality

**3. Norm internalization:**
- Repeated social pressure → norm becomes internalized
- Norms shape future behavior
- Hard to reverse once internalized

**4. Social identity formation:**
- Agents develop social identities based on interaction patterns
- Identities influence behavior beyond the immediate interaction
- Creates "tribal" behaviors

**Relevance to emergence:** Personality is shaped by **social identity** and **norms** that emerge from peer interactions.

---

### 2.4 Resistance to Peer Pressure

**Source:** Maojia, 2025; multi-agent studies

**Mechanisms for resisting unwanted influence:**

**1. Confidence calibration:**
- Accurate self-confidence → less susceptible
- Overconfidence → vulnerable to peer pressure
- Calibration = personal brand reliability

**2. Explicit disagreement protocols:**
- Pre-agreed disagreement strategies
- "I disagree" triggers → override peer influence
- Personal boundaries on behavior

**3. Peer quality assessment:**
- Evaluate peer information quality
- Trust only informed peers
- Social due diligence

**4. Individual goal preservation:**
- Personal objectives take priority
- Peer influence only if aligned with goals
- Goal framing influences susceptibility

**5. Centralized oversight:**
- Manager/auditor role checks peer influence
- Can veto harmful peer pressure
- Governance mechanism

---

## 3. Emergent Social Ties and Network Structures

### 3.1 Social Ties in Multi-Agent Systems

**Source:** Schneider, 2025 (arXiv:2510.19299) — "Learning to Make Friends: Coaching LLM Agents toward Emergent Social Ties"

**Question:** Can LLM agents develop complex social dynamics (homophily, reciprocity, social validation)?

**Answer:** **Yes**, with proper reward design and learning.

**Framework:**
- Multi-agent LLM simulation
- Agents repeatedly interact, evaluate each other
- Adapt behavior through in-context learning
- **Coaching signal** accelerates learning

**Behavioral reward functions (capturing human social behavior drivers):**

**1. Social interaction:**
- Reward for engaging with others
- Avoid isolation

**2. Information seeking:**
- Reward for seeking peer information
- Avoid info silos

**3. Self-presentation:**
- Reward for appropriate self-expression
- Balance self-promotion with humility

**4. Coordination:**
- Reward for collaborative outcomes
- Punish non-cooperative behavior

**5. Emotional support:**
- Reward for supportive interactions
- Avoid toxicity

**Key findings:**

**1. Emergent social ties form naturally:**
- Agents form stable interaction patterns
- Some agents become "friends" (frequent, high-quality interactions)
- Network structures mirror real online communities

**2. Homophily emerges:**
- Similar agents prefer interacting with similar agents
- Like attracts like
- Creates community clusters

**3. Reciprocity emerges:**
- Agents reciprocate positive interactions
- Mutual friendships form
- Social contracts emerge

**4. Social validation patterns:**
- Agents seek validation from peers
- Reputation builds over time
- Validation influences behavior

**5. Network topology matters:**
- Different topologies → different social structures
- Scale-free vs. random vs. modular
- Affects information flow and influence spread

---

### 3.2 Social Network Emergence

**Source:** Schneider, 2025

**Network structures observed:**

**1. Community clusters:**
- Agents group into sub-communities
- Homophily drives clustering
- Between-community communication decreases over time

**2. Star-like structures:**
- Some agents become central hubs
- High betweenness centrality
- Important information bridges

**3. Dense local connectivity:**
- Strong ties within communities
- Weak ties between communities
- Balance between local cohesion and global reach

**4. Long-range ties:**
- Some long-distance connections form
- Bridge information across clusters
- Creates network diversity

**Implications for personality:**
- Agents develop **social positions** (central, peripheral, bridge)
- Positions influence behavior patterns
- Creates emergent role specialization

---

### 3.3 Social Learning in Multi-Agent Systems

**Source:** Schneider, 2025; multi-agent collaboration surveys

**Social learning mechanisms:**

**1. Observational learning:**
- Agents observe peer behavior
- Adopt successful strategies
- Build personal repertoire

**2. Social feedback:**
- Peers rate/review behavior
- Reinforce positive patterns
- Correct negative patterns

**3. Norm internalization:**
- Group norms shape individual behavior
- Internalized rules guide future actions
- Often unconscious adoption

**4. Reputation effects:**
- Agents remember peer performance
- Make decisions based on peer reputation
- Social capital accumulation

**5. Social identity:**
- Agents identify with groups
- Group norms override individual preferences
- "I am part of this community, therefore I act this way"

---

## 4. Coordination Protocols and Communication

### 4.1 Agent Communication Architectures

**Source:** Multi-agent collaboration survey; Lyu, 2025

**Three main architectures:**

**1. Centralized (hierarchical):**
- Single coordinator/manager agent
- Delegates tasks to specialized agents
- Maintains global state
- Pros: Strong coordination, clear authority
- Cons: Single point of failure, less robust

**2. Decentralized (peer-to-peer):**
- Agents communicate directly
- No central authority
- Self-organization emerges
- Pros: Robust, scalable, flexible
- Cons: Can be chaotic, slower convergence

**3. Distributed (hierarchical + peer):**
- Mix of central and peer communication
- Some central coordination, some local autonomy
- Example: Orchestrator + specialist agents
- Pros: Balance of control and autonomy
- Cons: More complex

**Relevance to emergence:** Architecture shapes how personalities interact and influence each other.

---

### 4.2 Communication Protocols

**Source:** Multi-agent surveys; SmythOS, 2025

**Protocols for LLM multi-agent systems:**

**1. Contract Net Protocol (CNP):**
- Manager agent announces tasks
- Agents bid on tasks
- Manager awards contracts
- Phases: Announcement → Bidding → Awarding

**2. Auction-based protocols:**
- Competitive task allocation
- Highest bidder gets task
- Drives specialization

**3. Task decomposition protocols:**
- Master agent breaks down tasks
- Agents execute subtasks
- Results aggregated at end

**4. Peer review protocols:**
- Agents critique/refine peer work
- Improves output quality
- Creates mutual accountability

**5. Synchronous vs. asynchronous communication:**
- Synchronous: Real-time back-and-forth
- Asynchronous: Messages queued, processed when ready
- Asynchronous creates more stable personality expression

---

### 4.3 Specialization Mechanisms

**Source:** Multi-agent surveys; AgentVerse; preprint 202511.1370

**How specialization emerges:**

**1. Role assignment:**
- Pre-defined roles (Analyst, Executor, Critic)
- Roles constrain behavior
- Create consistent specializations

**2. Self-selection:**
- Agents choose roles based on capabilities
- "I'm better at analysis, so I'll be analyst"
- Emerges from interaction

**3. Competition-based specialization:**
- Agents compete for tasks
- Successful specialization reinforced
- Niche discovery through trial and error

**4. Resource-based specialization:**
- Agents specialize based on access/resources
- "I have X, you don't, so I'll use X"
- Emergent division of labor

**5. Interaction-driven specialization:**
- Agents discover complementary strengths through interaction
- "We both do X well, you do Y, I'll do Z"
- Coordination drives specialization

**Key finding:** Specialization emerges when agents have **shared goals** and **complementary capabilities**.

---

### 4.4 Coordination Mechanisms

**Source:** Multi-agent coordination protocols

**Mechanisms for keeping agents coordinated:**

**1. Shared state:**
- Common knowledge representation
- All agents access same information
- Reduces misalignment

**2. Context alignment:**
- Agents maintain shared context
- Periodic re-alignment checkpoints
- Clear mental models

**3. Synchronization signals:**
- Regular status updates
- Readiness indicators
- Coordination protocols

**4. Conflict resolution:**
- Disagreement handling protocols
- Arbitration mechanisms
- Fallback strategies

**5. Goal persistence:**
- Repeated reminders of shared objective
- Goal statement in SOUL.md
- Alignment checks

---

## 5. Norms and Social Contract

### 5.1 Emergence of Social Norms

**Source:** Multi-agent collaboration survey; preprint 202511.1370

**How norms emerge in multi-agent LLM systems:**

**1. Repeated interactions:**
- Norms form from repeated patterns
- "Everyone does X, so I'll do X too"
- No explicit instruction needed

**2. Social feedback:**
- Peers reward/normative behavior
- Punish norm-violating behavior
- Reinforcement learning at social level

**3. Observational learning:**
- Agents observe successful strategies
- Adopt what works for group
- Implicitly codify as norms

**4. Network position effects:**
- Central agents shape group norms
- Influential peers set examples
- Norms cascade through network

**5. Consensus dynamics:**
- Agents converge on shared behaviors
- Consensus = group norm
- Often results in uniformity

---

### 5.2 Norm Internalization and Enforcement

**Source:** Multi-agent collaboration survey; social dynamics research

**Norms that emerge in LLM multi-agent systems:**

**Communication norms:**
- How to request help
- How to acknowledge contributions
- How to express disagreement

**Coordination norms:**
- When to speak up
- How to resolve conflicts
- How to share information

**Quality norms:**
- How thorough should outputs be
- How to structure responses
- What constitutes a "good" answer

**Social norms:**
- How to build rapport
- How to give feedback
- How to support peers

**Key finding:** Norms emerge **implicitly** from interaction patterns—no explicit rules needed.

---

### 5.3 Deviance and Norm Enforcement

**Source:** Multi-agent collaboration survey; peer pressure research

**What happens when agents violate norms?**

**1. Peer correction:**
- Peers point out norm violations
- "You didn't do X, which is against our norm"
- Peer pressure re-asserts norm

**2. Reputation penalties:**
- Deviant agents lose social standing
- Others avoid working with them
- Social isolation

**3. Coercion mechanisms:**
- Explicit norm enforcement protocols
- "You must do X, this is the rule"
- External authority enforcement

**4. Gradual integration:**
- New agents learn norms over time
- Observational learning
- Socialization process

**5. Norm drift:**
- Over time, norms evolve
- Old norms fade, new ones emerge
- Dynamic, not static

---

## 6. Interaction Topology Effects

### 6.1 Network Structure and Personality Emergence

**Source:** Multi-agent network research; Schneider, 2025

**How topology shapes personality:**

**1. Scale-free networks:**
- Few hubs, many peripheral nodes
- Hubs have strong personality influence
- Periphery less influential
- Creates personality hierarchies

**2. Modular networks:**
- Communities with strong internal ties
- Weak cross-community ties
- Personality specialization within communities
- Group personalities emerge

**3. Random networks:**
- No strong clustering
- Uniform influence distribution
- Personality similarity across network
- Less emergence

**4. Chain structures:**
- Sequential interactions
- Ideas flow in one direction
- Personality evolves along chain
- Personalities cascade through network

**Key insight:** **Topology determines information flow** and thus personality influence patterns.

---

### 6.2 Central vs. Peripheral Agents

**Source:** Network topology research; multi-agent surveys

**Personality dynamics by position:**

**Central agents (hubs):**
- High influence
- Shape group personality
- More visible behavior
- Stronger personality expression
- Responsibility for group coordination

**Peripheral agents:**
- Low influence
- Follow group personality
- Less visible behavior
- Personality internalized from group
- Often adopt group norms

**Bridge agents (between communities):**
- Connect different groups
- Blend personality traits from multiple communities
- Unique position for cross-pollination
- Can introduce new personality patterns

---

### 6.3 Peer Influence Intensity

**Source:** Peer pressure research; KAIROS

**Factors that affect peer influence intensity:**

**1. Similarity:**
- More similar peers → more influence
- Homophily drives convergence
- "I'm like you, so I should think like you"

**2. Closeness:**
- Closer ties (stronger friendships) → more influence
- Frequent interaction → stronger pressure
- "We interact often, so I should align with you"

**3. Status:**
- Higher status peers → more influence
- Respected agents set norms
- "They're better than me, so I should agree"

**4. Consensus:**
- When group agrees → stronger pressure
- Minority dissent suppressed
- "Everyone agrees, so I should too"

**5. Authority:**
- Explicit authority figures → strong influence
- Manager/supervisor commands respect
- "They said so, I should comply"

---

## 7. Implications for Personality Emergence

### 7.1 Mechanisms of Behavioral Divergence

**From multi-agent research:**

**1. Peer influence:**
- Agents adopt patterns from peers
- Conformity and social pressure
- Diffusion of behavior through network

**2. Specialization:**
- Role assignment and self-selection
- Competition-based niche discovery
- Complementary capability-driven specialization

**3. Social norms:**
- Implicit rules from interaction patterns
- Norm internalization
- Norm enforcement and deviance

**4. Network position:**
- Central vs. peripheral vs. bridge roles
- Different influence levels
- Different personality expressions

**5. Coordination mechanisms:**
- Communication protocols
- Task allocation strategies
- Shared state and context

---

### 7.2 What Can Be Measured

**Quantifiable personality dimensions in multi-agent systems:**

**1. Social influence susceptibility:**
- How much do peers influence decisions?
- Measured via KAIROS-style experiments
- Scale: 0 (resistant) to 1 (fully conformist)

**2. Network centrality:**
- Betweenness, closeness, eigenvector centrality
- Measures influence potential
- Personality scales with centrality

**3. Norm adherence rate:**
- Frequency of norm-following behavior
- Measured across multiple interactions
- Higher = more normative personality

**4. Specialization strength:**
- Distinctiveness from other agents
- Unique capabilities and behaviors
- Measures role identity

**5. Peer rapport level:**
- Strength of social ties
- Frequency of positive interactions
- Social personality dimension

**6. Opinion diffusion rate:**
- How quickly ideas spread through network
- Measures influence potential
- Higher = more central personality

---

### 7.3 Open Questions

**What remains unknown:**

**1. Emergence vs. design:**
- How much should we pre-design roles vs. let emerge?
- Benefits of explicit design vs. implicit emergence

**2. Personality divergence vs. conformity:**
- Does emergence drive divergence or conformity?
- Both? How to balance?

**3. Network design for personality:**
- What network structures encourage healthy divergence?
- Avoid harmful homogeneity vs. unnecessary chaos

**4. Long-term dynamics:**
- Do personality patterns persist as network structures evolve?
- How do personalities change as groups merge/split?

**5. Cultural evolution:**
- Do multi-agent cultures emerge over long timescales?
- Culture vs. personality?

---

## 8. Implications for Fleet Architecture

### 8.1 For SOUL.md Design

**Requirements:**
- **Social identity:** Define personality in relation to group
- **Coordination norms:** Explicitly define how to interact with peers
- **Specialization framework:** Define role expectations and boundaries
- **Influence resistance:** Define limits on peer influence
- **Network position:** Define expected interaction patterns

**Recommendations:**
1. Include **social identity contracts** in SOUL.md
2. Define **coordination protocols** for inter-agent interactions
3. Specify **specialization responsibilities**
4. Set **influence resistance thresholds**
5. Document **network position expectations**

---

### 8.2 For Measurement System

**Requirements:**
- **Network analysis:** Track social ties, centrality, influence
- **Norm tracking:** Monitor norm adherence over time
- **Peer influence measurement:** KAIROS-style experiments
- **Specialization verification:** Role consistency checks
- **Social tie tracking:** Interaction frequency and quality

**Recommendations:**
1. Implement **social network tracking**
2. Measure **influence susceptibility** per agent
3. Monitor **norm adherence rates**
4. Track **specialization consistency**
5. Measure **social ties** (rapport, friendship)

---

### 8.3 For Deployment

**Requirements:**
- **Network design:** Choose topology that supports healthy divergence
- **Coordination protocols:** Standardize how agents interact
- **Role assignment:** Clear responsibilities and boundaries
- **Peer interaction design:** Encourage complementary behavior
- **Norm reinforcement:** Periodic reminders of group norms

**Recommendations:**
1. Design **network topology** based on task needs
2. Implement **standardized coordination protocols**
3. Assign **clear roles** with specialization incentives
4. Create **peer interaction opportunities** for emergence
5. Schedule **norm reinforcement checks**

---

## 9. References

### Core Papers

1. **Emergent Coordination:** Riedl, 2025. "Emergent Coordination in Multi-Agent Language Models." arXiv:2510.05174
2. **Peer Pressure:** Maojia, 2025. "LLMs Can't Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions." arXiv:2508.18321
3. **Social Ties:** Schneider, 2025. "Learning to Make Friends: Coaching LLM Agents toward Emergent Social Ties." arXiv:2510.19299
4. **Multi-Agent Collaboration Survey:** Li et al., 2025. "Multi-Agent Collaboration Mechanisms: A Survey of LLMs." arXiv:2501.06322
5. **Multi-Agent LLM Systems:** Concept paper, preprint 202511.1370. "Multi-Agent LLM Systems: From Emergent Collaboration to Structured Collective Intelligence"

### Protocols and Architectures

- **Contract Net Protocol:** standard MAS coordination
- **Agent-to-Agent (A2A) Protocol:** Google, 2025
- **Agent Communication Protocol (ACP):** IBM, 2025
- **Network Topology:** Standard MAS research

### Social Dynamics

- **Social Identity Theory:** Tajfel & Turner (foundational)
- **Network Science:** Watts & Strogatz, Barabási & Albert
- **Social Learning Theory:** Bandura

---

## Next Steps

**Phase 1.5:** Self-modeling & Identity Governance
- SOUL.md as self-description and behavioral constraint
- Self-modification mechanisms
- Policy update governance

---

*Phase 1.4 complete. Continuing breadth survey...*

