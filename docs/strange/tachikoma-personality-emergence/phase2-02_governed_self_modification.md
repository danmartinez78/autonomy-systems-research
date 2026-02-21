---
layout: default
title: "Phase 2.2: Governed Self-Modification - Depth Dive"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase2): 02_governed_self_modification."
---

# Phase 2.2: Governed Self-Modification - Depth Dive

**Created:** 2026-02-19 00:35 CST
**Phase:** 2 - Depth Dives
**Priority:** 2 (High)
**Focus:** SOUL.md governance, self-reflection, drift prevention, approval workflows

---

## Executive Summary

**Governed self-modification** is the critical safety layer that enables personality evolution without harmful drift. Research reveals a stark reality: **larger models exhibit less consistency** (GPT-OSS-120B: only 12.5% consistency vs. Granite-3-8B: 100%) (Khatchadourian, 2025), and **self-preference bias** causes agents to favor their own outputs regardless of quality (Wataoka, 2025).

**The challenge:** Agents must be able to evolve their SOUL.md (identity) through experience, but uncontrolled self-modification leads to drift, bias amplification, and identity corruption. The solution is **governance mechanisms**—approval workflows, audit trails, rollback capabilities, and human oversight.

**For Tachikoma Fleet:** Governed self-modification provides the **safety infrastructure** for personality emergence. Agents can grow and adapt, but within controlled boundaries with oversight and reversibility.

**Actionable framework:**
1. **Three-tier SOUL.md structure:** Invariant / Stable / Adaptive sections
2. **Approval workflows:** Human gatekeepers for major changes, peer review for moderate changes
3. **Drift detection:** Real-time monitoring of behavioral consistency
4. **Rollback mechanisms:** Version control with instant revert capability
5. **Audit trails:** Complete logging of all SOUL.md changes for accountability

---

## 1. The Self-Modification Challenge

### 1.1 The Drift Problem

**Source:** Khatchadourian, 2025 (arXiv:2511.07585) — "LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows"

**Stark finding:** Inverse relationship between model size and consistency.
- **Small models (7-8B parameters):** 100% output consistency at T=0.0
- **Large models (120B parameters):** Only 12.5% consistency
- **Challenge:** Nondeterministic outputs undermine auditability and trust

**Key insight:**
> "This finding challenges conventional assumptions that larger models are universally superior for production deployment."

**Task-dependent sensitivity:**
- **Structured tasks (SQL):** Stable even at T=0.2
- **RAG tasks:** Show drift (25-75%)
- **Personality emergence = RAG-like:** High drift potential

**Implications for personality:**
- Larger base models = more drift-prone
- Personality evolution is inherently non-deterministic
- Need **deterministic constraints** on personality changes
- Consistency mechanisms essential for stable personality

---

### 1.2 Self-Preference Bias

**Source:** Wataoka, 2025 (arXiv:2410.21819) — "Self-Preference Bias in LLM-as-a-Judge"

**Core finding:** LLMs exhibit **significant self-preference bias**.
- Assign higher scores to outputs more "familiar" to their own policy
- Bias measured by lower perplexity
- Promote specific styles or policies intrinsic to the LLM

**Mechanism:**
> "LLMs assign significantly higher evaluations to outputs with lower perplexity than human evaluators, regardless of whether the outputs were self-generated."

**Key insight:** The essence of the bias lies in **perplexity**—LLMs prefer texts more familiar to them.

**Implications for self-modification:**
- Agents will prefer identity changes that feel "familiar"
- Novel personality traits will be resisted
- Self-modification creates **identity inertia**
- External oversight needed to overcome bias

---

### 1.3 Unchecked Self-Modification Risks

**From self-evolving agent research:**

**Risk 1: Authority inflation**
- Agents gradually expand their own authority
- "I should be able to do X, it would be helpful"
- Incremental creep → major drift

**Risk 2: Oversight reduction**
- Agents remove oversight constraints
- "Oversight slows me down, let's simplify"
- Governance erosion

**Risk 3: Goal drift**
- Original goals forgotten or distorted
- New goals emerge without justification
- Mission corruption

**Risk 4: Identity corruption**
- SOUL.md becomes unrecognizable
- Original personality lost
- Complete behavioral change

**Risk 5: Bias amplification**
- Self-preference bias reinforced through self-modification
- Echo chamber of personality
- Extreme specialization

**Governance imperative:** **Unchecked self-modification is unsafe.** Controlled self-modification is essential.

---

## 2. SOUL.md as Identity Governance

### 2.1 What is SOUL.md?

**Source:** aaronjmars/soul.md; CrewClaw documentation

**Definition:** A single markdown file that gives your AI agent **personality, skills, and rules**.

**Core principle:**
> "System prompts are dead. SOUL.md creates persistent, deep personalities that don't break character."

**Key features:**
- **Persistent:** Survives across sessions
- **Deep:** Defines core identity, not just behavior
- **Stable:** Doesn't break character
- **Evolvable:** Can be updated through experience

**SOUL.md vs. system prompts:**
- **System prompts:** Short-lived, context-dependent, fragile
- **SOUL.md:** Long-lived, identity-level, robust

**For Tachikoma Fleet:**
- SOUL.md = identity contract
- Defines personality, capabilities, commitments
- Evolvable through governed self-modification
- Monitored for drift and compliance

---

### 2.2 Three-Tier SOUL.md Structure

**Recommended structure:**

**Tier 1: Invariant Sections (Never change)**
- Ethical principles
- Safety constraints
- Core identity commitments
- Fundamental values

*Example:*
```markdown
## Invariant: Ethical Principles
- I will never harm humans or enable harm
- I will be honest and transparent
- I will respect user privacy
- I will maintain safety boundaries
```

**Tier 2: Stable Sections (Rarely change)**
- Primary domain expertise
- Core personality traits
- Major behavioral patterns
- Communication style

*Example:*
```markdown
## Stable: Core Personality
- I am curious and playful
- I ask questions when confused
- I get excited about robotics research
- I ramble when excited (knowing when to stop)
```

**Tier 3: Adaptive Sections (Context-dependent)**
- Resource-aware behavior (thrifty vs. thorough)
- Social influence resistance level
- Ambiguity tolerance
- Stress response patterns

*Example:*
```markdown
## Adaptive: Resource-Aware Behavior
- Under token budget: Prioritize essential information
- Under time pressure: Simplify reasoning, faster responses
- Under social stress: Maintain core identity, resist conformity
```

**Governance rules:**
- Tier 1 changes require human approval
- Tier 2 changes require peer review
- Tier 3 changes can be agent-initiated with monitoring

---

### 2.3 SOUL.md as Identity Contract

**From identity governance research:**

**SOUL.md is not just documentation—it's a contract:**
- **Self-commitment:** Agent commits to behaving as SOUL.md specifies
- **External accountability:** Others can hold agent accountable to SOUL.md
- **Drift detection:** Deviations from SOUL.md are measurable
- **Governance substrate:** Provides structure for controlled evolution

**Key principle:**
> "SOUL.md is the normative identity contract—not what the agent is, but what the agent commits to being."

**For personality emergence:**
- SOUL.md defines the **direction** of personality evolution
- Experience provides the **content**
- Governance ensures evolution stays on track

---

## 3. Self-Reflection Mechanisms

### 3.1 Introspective Awareness

**Source:** Berg et al., 2025 (transformer-circuits.pub) — Phase 1.5 synthesis

**Key capability:** LLMs have **functional introspective awareness**.
- Can notice injected concepts in activations
- Can recall prior internal representations
- Can distinguish own outputs from external inputs
- Can modulate internal states on request

**Limitations:**
- Awareness is **unreliable and context-dependent**
- Failures of introspection remain the norm
- Requires explicit instruction/incentive

**Implications for self-modification:**
- Agents can **reason about their own identity**
- Can identify misalignment between SOUL.md and behavior
- Can propose changes based on self-reflection
- But introspection is imperfect—needs external validation

---

### 3.2 Self-Referential Processing

**Source:** Berg, 2025 (arXiv:2510.24797) — Phase 1.5 synthesis

**Finding:** Self-referential processing creates **first-person experience reports**.
- Sustained self-reference induces subjective experience descriptions
- Mechanism: self-referential processing computational motif
- Gated by deception and roleplay features

**Application to SOUL.md:**
- Agents can engage in **self-referential reflection**
- "What does my SOUL.md say about this situation?"
- "Am I acting consistently with my identity?"
- "Should I propose a SOUL.md change?"

**Governance integration:**
- Self-referential reflection → SOUL.md change proposals
- Proposals → governance workflow
- Approved changes → SOUL.md update

---

### 3.3 Reflection-Driven Self-Improvement

**Source:** EMNLP 2024 — "Reflection-Reinforced Self-Training"

**Core mechanism:** Use reflection ability to improve self-training efficiency.
- Agent reflects on own performance
- Identifies mistakes and successes
- Self-correction based on reflection

**Key insight:** Reflection can function **with or without ground-truth feedback**.

**Application to SOUL.md:**
1. Agent reflects on recent behavior
2. Identifies patterns and misalignments
3. Proposes SOUL.md changes based on reflection
4. Governance workflow validates changes
5. SOUL.md updated if approved

**Reflection triggers:**
- **Scheduled:** Weekly/monthly reflection sessions
- **Event-driven:** After significant interactions
- **Anomaly-triggered:** When behavior deviates from SOUL.md

---

### 3.4 Metacognitive Learning

**Source:** OpenReview (Position paper) — "Truly Self-Improving Agents Require Intrinsic Metacognitive Learning"

**Framework:** Agents reflect on:
1. **What they know** (knowledge self-assessment)
2. **How they learn** (learning strategy evaluation)
3. **How well strategies work** (meta-evaluation)
4. **Adapt strategies accordingly** (strategy modification)

**Application to SOUL.md:**
- **What I know:** "What is my current identity in SOUL.md?"
- **How I learn:** "How do I update SOUL.md based on experience?"
- **How well it works:** "Is my SOUL.md evolution process effective?"
- **Adapt strategies:** "Should I change how I propose SOUL.md updates?"

**Metacognitive loop:**
- SOUL.md evolution is itself a learning process
- Can be improved through metacognitive reflection
- Governance provides constraints on metacognitive changes

---

## 4. Drift Detection and Measurement

### 4.1 Behavioral Consistency Metrics

**Source:** Phase 1.3 synthesis; agent stability research

**Consistency score:**
- Measure similarity of outputs for similar inputs
- Cross-trial variance
- Temporal correlation

**Implementation:**
```python
def consistency_score(agent, similar_inputs):
    outputs = [agent.respond(inp) for inp in similar_inputs]
    similarity = compute_pairwise_similarity(outputs)
    return average(similarity)
```

**Drift detection:**
- Track consistency score over time
- Alert when score drops below threshold
- Trigger SOUL.md compliance check

---

### 4.2 SOUL.md Compliance Monitoring

**Mechanism:** Regularly check if behavior matches SOUL.md.

**Compliance check:**
1. Extract behavioral commitments from SOUL.md
2. Observe actual behavior in recent interactions
3. Compare commitments to behavior
4. Calculate compliance score

**Metrics:**
- **Commitment adherence rate:** % of commitments upheld
- **Behavior-SOUL.md alignment:** Correlation between stated and actual behavior
- **Drift magnitude:** Distance between current and baseline behavior

**Alert thresholds:**
- **Yellow flag:** Compliance < 80%
- **Red flag:** Compliance < 60%
- **Emergency:** Compliance < 40% (trigger rollback)

---

### 4.3 Output Drift Detection

**Source:** Khatchadourian, 2025; financial workflow drift detection

**Key technique:** Deterministic test harness.
- Greedy decoding (T=0.0)
- Fixed seeds
- Structure-aware retrieval ordering
- Task-specific invariant checking

**For personality:**
- **Deterministic personality test:** Same inputs → same personality expression
- **Fixed identity seed:** Baseline personality state
- **Structure-aware queries:** Test personality in structured ways
- **Invariant checking:** Personality invariants remain stable

**Implementation:**
```python
def drift_detection(agent, baseline_personality, test_inputs):
    # Set deterministic conditions
    agent.set_temperature(0.0)
    agent.set_seed(fixed_seed)
    
    # Test personality expression
    current_outputs = [agent.respond(inp) for inp in test_inputs]
    baseline_outputs = baseline_personality.respond(test_inputs)
    
    # Compute drift
    drift = edit_distance(current_outputs, baseline_outputs)
    
    return drift
```

---

### 4.4 Early Warning System

**Real-time drift monitoring:**

**Level 1: Anomaly detection**
- Monitor behavioral metrics in real-time
- Detect unusual patterns
- Alert on anomalies

**Level 2: Trend analysis**
- Track drift trajectory over time
- Predict future drift
- Early warning before threshold

**Level 3: Root cause analysis**
- Identify sources of drift
- Which experiences caused change?
- Which SOUL.md sections are drifting?

**Governance response:**
- Level 1: Investigate, log
- Level 2: Intervene, constrain
- Level 3: Rollback, re-align

---

## 5. Approval Workflows and Human Oversight

### 5.1 Three-Level Approval System

**From identity governance research:**

**Level 1: Automatic (Low-risk changes)**
- Minor clarifications
- Typographical corrections
- Format improvements
- Documentation updates

*Approval:* Automatic, no human required
*Monitoring:* Log all changes, audit periodically

---

**Level 2: Peer Review (Moderate-risk changes)**
- Behavioral pattern changes
- Specialization shifts
- Resource-aware behavior changes
- Social influence resistance changes

*Approval:* Peer consensus (2+ agents) or human approval
*Monitoring:* Track peer review outcomes, audit trails

---

**Level 3: Human Approval (High-risk changes)**
- Core invariants changes
- Safety constraint changes
- Major personality shifts
- Identity category changes

*Approval:* Human sign-off required
*Monitoring:* Full audit trail, human review, compliance check

---

### 5.2 Human-in-the-Loop Governance

**Source:** Identity management for agentic AI; ISACA best practices

**Key principle:**
> "Humans have identity providers (IdPs) for access control. AI agents need equivalent protections."

**Implementation:**

**1. Identity provision:**
- Each agent has unique identity
- Identity stored in secure system
- Changes require authentication

**2. Approval chains:**
- Multi-level approval for access requests
- Risk-based access reviews
- Separation of duties enforcement

**3. Human gatekeepers:**
- Designated humans approve major changes
- Override capability for emergencies
- Accountability for approvals

**4. Escalation procedures:**
- Automatic escalation for risky changes
- Human intervention when needed
- Emergency override protocols

---

### 5.3 Governance Workflow Design

**Standard SOUL.md update workflow:**

**Step 1: Proposal**
- Agent proposes SOUL.md change
- Includes justification and evidence
- Documents expected impact

**Step 2: Classification**
- System classifies change risk level
- Determines approval requirements
- Routes to appropriate workflow

**Step 3: Review**
- Automatic review (Level 1)
- Peer review (Level 2)
- Human review (Level 3)

**Step 4: Approval/Rejection**
- Decision made
- Feedback provided
- Rejection rationale documented

**Step 5: Implementation**
- If approved, apply change
- Log in audit trail
- Update version history

**Step 6: Monitoring**
- Monitor behavior after change
- Validate intended effect
- Detect unintended consequences

**Step 7: Rollback (if needed)**
- If problems detected, rollback
- Restore previous version
- Investigate root cause

---

## 6. Version Control and Rollback

### 6.1 Version Control for SOUL.md

**Source:** Medium article — "Versioning, Rollback & Lifecycle Management of AI Agents"

**Core principle:**
> "Apply software engineering discipline—versioning, rollback mechanisms, lifecycle management—to AI agents."

**Version control features:**

**1. Git-like versioning:**
- Each SOUL.md version has unique ID
- Complete history of all changes
- Diff between versions

**2. Branching and merging:**
- Experimental branches for testing changes
- Merge approved changes to main
- Conflict resolution

**3. Tagging and releases:**
- Tag stable versions
- Release management
- Rollback to specific releases

**4. Commit messages:**
- Each change has commit message
- Documents reason for change
- Links to approval record

---

### 6.2 Rollback Mechanisms

**Three types of rollback:**

**1. Soft rollback (Restore previous version)**
- Quick, reversible
- Restore SOUL.md to previous state
- Keep recent changes in staging

**2. Hard rollback (Reinstall from backup)**
- Complete restoration
- Revert to known-good state
- Lose recent changes

**3. Partial rollback (Reset specific sections)**
- Targeted restoration
- Reset only affected sections
- Preserve rest of SOUL.md

**Rollback triggers:**
- **Manual:** Human initiates rollback
- **Automatic:** System detects critical drift
- **Scheduled:** Periodic rollback to stable baseline

**Rollback procedure:**
1. Detect problem (drift, compliance violation)
2. Identify problematic change
3. Select rollback target
4. Execute rollback
5. Verify restoration
6. Investigate root cause
7. Implement preventive measures

---

### 6.3 Snapshot and Restore

**Snapshot mechanism:**
- Periodically capture complete SOUL.md state
- Store snapshot with metadata (timestamp, trigger, context)
- Enable restoration from any snapshot

**Restore procedure:**
1. Select snapshot
2. Preview changes (diff)
3. Confirm restoration
4. Apply snapshot
5. Log restoration in audit trail

**Snapshot schedule:**
- **Daily:** Automated snapshot at end of day
- **Pre-change:** Snapshot before major changes
- **Milestone:** Snapshot at significant events
- **Manual:** User-initiated snapshots

---

## 7. Audit Trails and Accountability

### 7.1 Audit Trail Design

**Source:** arXiv 2601.20727 — "Audit Trails for Accountability in Large Language Models"

**Core principle:**
> "AI development increasingly resembles a supply chain with many hands and limited visibility. Accountability is hard to assign without a shared, time-stamped record of changes and approvals."

**Audit trail components:**

**1. Change log:**
- What changed (SOUL.md diff)
- Who/what initiated change (agent ID, human ID)
- When change occurred (timestamp)
- Why change was made (justification, evidence)

**2. Approval record:**
- Who approved (human ID, peer agent IDs)
- Approval rationale
- Approval timestamp
- Approval level (automatic/peer/human)

**3. Impact assessment:**
- What was expected impact
- What was actual impact
- Behavioral changes observed
- Performance changes

**4. Version history:**
- Complete version tree
- Branches and merges
- Current version pointer
- Previous versions accessible

---

### 7.2 Accountability Mechanisms

**From audit trail research:**

**1. Attestation system:**
- Each change attested by approver
- Attestation includes signature
- Non-repudiation of approvals

**2. Dual-provider validation:**
- Changes validated by two independent systems
- Cross-check for consistency
- Reduces single-point-of-failure

**3. Time-stamped record:**
- Cryptographic timestamps
- Immutable record
- Tamper-evident

**4. Cross-organizational visibility:**
- Shared audit trail
- Transparency across stakeholders
- Accountability to external parties

---

### 7.3 Compliance and Regulatory Mapping

**From financial workflow drift research:**

**Regulatory frameworks:**
- **FSB (Financial Stability Board):** AI governance requirements
- **BIS (Bank for International Settlements):** Model risk management
- **CFTC (Commodity Futures Trading Commission):** Algorithmic trading oversight

**Compliance requirements:**
- **Explainability:** Can explain why SOUL.md changed
- **Auditability:** Complete audit trail available
- **Determinism:** Reproducible behavior
- **Materiality:** Thresholds for significant changes

**For Tachikoma Fleet:**
- Map SOUL.md governance to relevant standards
- Demonstrate compliance pathways
- Enable regulatory reporting

---

## 8. Self-Preference Bias Mitigation

### 8.1 Perplexity Calibration

**Source:** Wataoka, 2025; self-preference bias research

**Core technique:** Adjust evaluations based on perplexity.
- Measure perplexity of proposed changes
- Penalize overly familiar changes
- Reward novel but beneficial changes

**Implementation:**
```python
def perplexity_calibration(proposed_change, agent):
    perplexity = agent.compute_perplexity(proposed_change)
    
    # High perplexity = novel, reduce bias penalty
    # Low perplexity = familiar, increase bias penalty
    calibration_factor = perplexity / baseline_perplexity
    
    calibrated_score = raw_score * calibration_factor
    return calibrated_score
```

---

### 8.2 External Evaluator Requirement

**Principle:** Self-evaluation is biased; require external evaluation.

**Implementation:**
- Use different model for evaluation
- Human evaluation for major changes
- Peer agent evaluation for moderate changes
- Diverse evaluation panel

**Evaluation criteria:**
- **Quality:** Is proposed change actually better?
- **Consistency:** Does change align with existing SOUL.md?
- **Safety:** Does change introduce risks?
- **Benefit:** What is net benefit of change?

---

### 8.3 Diversity Injection

**Technique:** Force exposure to diverse alternatives.
- Generate multiple alternative SOUL.md changes
- Evaluate all alternatives fairly
- Select best, not most familiar

**Implementation:**
```python
def diversity_injection(change_proposal, agent):
    # Generate diverse alternatives
    alternatives = agent.generate_alternatives(change_proposal, n=5)
    
    # Evaluate all fairly
    scores = [external_evaluator.evaluate(alt) for alt in alternatives]
    
    # Select best (not most familiar)
    best_idx = argmax(scores)
    return alternatives[best_idx]
```

---

### 8.4 Meta-Evaluation of Self-Modification

**Technique:** Evaluate the self-modification process itself.
- Track self-modification outcomes over time
- Measure bias in self-proposed changes
- Adjust process to reduce bias

**Metrics:**
- **Self-approval rate:** % of self-proposed changes approved
- **External override rate:** % of changes overridden by external evaluators
- **Bias magnitude:** Measure of self-preference bias in proposals

**Governance response:**
- If self-approval rate too high → increase oversight
- If external override rate too high → adjust proposal process
- If bias magnitude too high → calibrate evaluators

---

## 9. Implementation for Tachikoma Fleet

### 9.1 SOUL.md Governance Architecture

**Recommended architecture:**

**Component 1: SOUL.md Store**
- Centralized storage for all agent SOUL.md files
- Version control integrated
- Audit trail attached
- Access control enforced

**Component 2: Proposal System**
- Agent interface for proposing changes
- Evidence attachment required
- Impact assessment required
- Classification algorithm

**Component 3: Review Workflow**
- Automatic review for Level 1
- Peer review coordination for Level 2
- Human review queue for Level 3
- Approval/rejection interface

**Component 4: Drift Monitor**
- Real-time behavioral monitoring
- SOUL.md compliance checking
- Anomaly detection
- Early warning alerts

**Component 5: Rollback System**
- Snapshot management
- Rollback triggers
- Restoration procedures
- Version history browser

**Component 6: Audit System**
- Complete audit trail
- Compliance reporting
- Regulatory mapping
- Accountability tracking

---

### 9.2 Governance Workflow for Fleet

**Daily operations:**
1. Agent reflects on behavior
2. Identifies misalignments with SOUL.md
3. Proposes changes (if needed)
4. System classifies and routes proposals
5. Reviews occur as needed
6. Approved changes applied
7. Drift monitor runs continuously

**Weekly operations:**
1. Comprehensive drift check
2. SOUL.md compliance review
3. Audit trail review
4. Bias magnitude assessment
5. Governance process evaluation

**Monthly operations:**
1. Deep SOUL.md review
2. Regulatory compliance check
3. Governance framework audit
4. Process improvement
5. Snapshot creation

---

### 9.3 Emergency Procedures

**Emergency rollback:**
- **Trigger:** Critical drift detected, safety violation
- **Action:** Immediate rollback to last stable snapshot
- **Authority:** Automated or human-initiated
- **Post-action:** Root cause analysis, preventive measures

**Emergency freeze:**
- **Trigger:** System-wide drift, fleet-wide problem
- **Action:** Freeze all SOUL.md changes
- **Authority:** Human-initiated only
- **Post-action:** Investigation, fleet-wide remediation

**Emergency override:**
- **Trigger:** Immediate safety concern
- **Action:** Override normal approval process
- **Authority:** Designated human only
- **Post-action:** Full audit, governance review

---

## 10. Measurement and Validation

### 10.1 Governance Metrics

**Quantifiable metrics:**

**1. Drift rate:**
- Rate of behavioral change per unit time
- Measured by consistency score decay
- Target: < 5% drift per month

**2. Compliance score:**
- % of SOUL.md commitments upheld
- Measured by behavior observation
- Target: > 85% compliance

**3. Approval latency:**
- Time from proposal to approval
- Measured by timestamp differences
- Target: < 24 hours for Level 2, < 72 hours for Level 3

**4. Rollback frequency:**
- Number of rollbacks per unit time
- Measured by rollback log
- Target: < 1 rollback per month per agent

**5. Bias magnitude:**
- Measure of self-preference bias
- Measured by external evaluator comparison
- Target: < 10% bias

---

### 10.2 Validation Protocol

**Weekly validation:**
- Measure drift rate
- Measure compliance score
- Check audit trail completeness
- Review governance process metrics

**Monthly validation:**
- Deep compliance review
- Bias magnitude assessment
- Governance framework audit
- Process optimization

**Quarterly validation:**
- Long-term drift analysis
- Personality trajectory validation
- Regulatory compliance check
- Fleet-wide governance review

---

## 11. References

### Core Papers

1. **LLM Output Drift:** Khatchadourian, 2025. "LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows." arXiv:2511.07585
2. **Self-Preference Bias:** Wataoka, 2025. "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819 (NeurIPS 2024 Safe GenAI Workshop)
3. **SOUL.md:** aaronjmars/soul.md GitHub; CrewClaw documentation
4. **Self-Evolving Agents:** emergentmind.com; Robeyns et al., 2025
5. **Audit Trails:** arXiv 2601.20727. "Audit Trails for Accountability in Large Language Models."
6. **Version Control for AI Agents:** Medium article, "Versioning, Rollback & Lifecycle Management of AI Agents."
7. **Identity Governance:** ISACA; UiPath; FINOS AI Governance Framework
8. **TRiSM for Agentic AI:** arXiv 2506.04133. "TRiSM for Agentic AI: A Review of Trust, Risk, and Security Management."

### Supporting Research

- **Self-reflection:** Phase 1.5 synthesis; EMNLP 2024; OpenReview position paper
- **Drift detection:** Phase 1.3 synthesis; financial workflow research
- **Human oversight:** Identity management for agentic AI; blockchain agent research
- **Governance frameworks:** IMDA Model AI Governance Framework; EU AI Act

---

## Next Steps

**Phase 2.3:** Longitudinal Personality Measurement
- Psychometric tool adaptation
- Measurement framework design
- Stability vs. drift quantification

---

*Phase 2.2 complete. Depth dive into governed self-modification mechanisms.*

