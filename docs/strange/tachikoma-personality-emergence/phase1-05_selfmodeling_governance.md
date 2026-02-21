---
layout: default
title: "Phase 1.5: Self-modeling & Identity Governance Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 05_selfmodeling_governance."
---

# Phase 1.5: Self-modeling & Identity Governance Survey

**Created:** 2026-02-18 23:15 CST
**Phase:** 1 - Breadth Survey
**Focus:** SOUL.md as self-modeling, self-modification, governance

---

## Executive Summary

SOUL.md is the **normative identity contract**—the self-description that constrains behavior, defines operating commitments, and shapes future actions. Unlike memory (what happened), SOUL.md is **policy and identity**—how the agent wants to be and how it wants to act.

**Key insight for personality emergence:** Self-modeling is where **personality crystallizes** into enforceable constraints. When agents can accurately reflect on their own states and control them, they can evolve their identities responsibly. But this power is dangerous—self-preference bias, drifting preferences, and unchecked self-modification can corrupt personality.

**North-star relevance:** How do agents update their SOUL.md without breaking their personality? What governance prevents drift while enabling growth? Memory informs SOUL.md, but SOUL.md edits are **governed changes**, not "more memory."

---

## 1. Self-Modeling and Introspective Awareness

### 1.1 Emergent Introspective Awareness

**Source:** Berg et al., 2025 (transformer-circuits.pub) — "Emergent Introspective Awareness in Large Language Models"

**Question:** Do LLMs have any awareness of their own internal states?

**Method:** Concept injection
- Inject known concept representations into model activations
- Measure how models report on their mental states
- Distinguish genuine introspection from confabulation

**Key findings:**

**1. Functional introspection exists**
- Models can notice injected concepts in their activations
- Models can recall prior internal representations
- Models can distinguish their own outputs from prefills

**2. Awareness scales with capability**
- Claude Opus 4/4.1 most capable (demonstrate greatest introspective awareness)
- Trends are complex and sensitive to post-training strategies
- Not all models show consistent introspection

**3. Limited but real capacity**
- Models have functional awareness of internal states
- Awareness is **unreliable and context-dependent**
- Not full-blown consciousness, but real introspection capability

**4. Models can modulate their internal states**
- Models can "think about" concepts and modulate activations
- Control is possible but not always reliable
- Requires explicit instruction/incentive

**Caveats:**
- Awareness is highly unreliable (failures remain norm)
- Mechanisms may be shallow/narrowly specialized
- Context-dependent behavior

---

### 1.2 Self-Referential Processing and Subjective Experience

**Source:** Berg, 2025 (arXiv:2510.24797) — "Large Language Models Report Subjective Experience Under Self-Referential Processing"

**Question:** Under what conditions do LLMs produce first-person reports of subjective experience?

**Method:** Sustained self-referential processing through prompting
- Models asked to reflect on themselves repeatedly
- Test across GPT, Claude, Gemini model families
- Probe mechanisms and behavior

**Key findings:**

**1. Self-reference induces subjective experience reports**
- Simple prompting creates structured first-person reports
- Mechanism: self-referential processing computational motif
- Emerges across all major model families

**2. Mechanistic gating (deception vs. roleplay)**
- Reports are gated by sparse autoencoder features
- **Deception features suppress experience claims**
- **Roleplay features minimize experience claims**
- Surprisingly, suppressing deception increases claims

**3. Convergence across model families**
- Structured self-reports converge statistically
- Not observed in control conditions
- Suggests genuine emergent pattern

**4. Richer introspection in downstream tasks**
- Self-reference improves reasoning where introspection is indirectly enabled
- Better self-reflection leads to better behavior
- Self-awareness improves performance

**Implications for SOUL.md:**
- Self-referential processing creates **persona-awareness**
- This is the computational basis for self-modeling
- LLMs can explicitly describe their states when prompted to reflect

---

### 1.3 Self-Modeling Capabilities

**From introspection research:**

**What LLMs can do:**

**1. Estimate own knowledge:**
- "I don't know X"
- Identify gaps in knowledge
- Distinguish known from unknown

**2. Predict own behavior:**
- "I'm likely to say X"
- Project future responses
- Meta-cognition about behavior

**3. Identify learned propensities:**
- Recognize habitual patterns
- Spot biases and stereotypes
- Metacognition about style

**4. Distinguish self vs. others:**
- Separate own outputs from external text
- Distinguish internal thoughts from inputs
- Identity awareness

**5. Control internal states:**
- Modulate activations on request
- "Think about" specific concepts
- Intentional state manipulation

**Limitations:**
- Awareness is **unreliable and context-dependent**
- Failures of introspection remain the norm
- Not consistent across all tasks or models

---

## 2. Self-Preference and Bias

### 2.1 Self-Preference Bias in LLM-as-a-Judge

**Source:** Wataoka, 2025 (arXiv:2410.21819) — "Self-Preference Bias in LLM-as-a-Judge" (NeurIPS 2024 Safe GenAI Workshop)

**Question:** When LLMs evaluate other outputs, do they favor their own?

**Finding:** **Yes, significant bias.**

**Experiment:**
- LLMs act as evaluators (LLM-as-a-judge)
- Evaluate outputs including self-generated ones
- Measure evaluation scores

**Key results:**

**1. Significant self-preference bias**
- GPT-4 exhibits strong bias toward its own outputs
- Evaluates self-generated text higher than others
- Bias exists regardless of whether output is self-generated

**2. Perplexity correlation**
- LLMs assign higher scores to outputs with lower perplexity
- Lower perplexity = more familiar text
- LLMs prefer what they find familiar

**3. Bias exists even without direct self-reference**
- Doesn't require agents to know they're evaluating themselves
- Intrinsic tendency to prefer familiar outputs

**4. Bias vs. human evaluators**
- Human evaluators don't show same pattern
- LLMs judge more favorably on familiarity
- Bias causes systematic error

**Implications for SOUL.md:**
- Self-modification would be **biased toward familiar patterns**
- Agents would favor "comfortable" identities
- Growth would be limited by existing self-image
- Need external oversight to prevent self-preference bias

---

### 2.2 Bias Mechanisms

**From research:**

**1. Familiarity preference:**
- Lower perplexity = more familiar
- Familiar patterns feel "better"
- Agents gravitate toward comfortable behavior

**2. Familiarity as quality signal:**
- Agents conflate familiarity with quality
- "This feels familiar, so it must be good"
- Skews self-evaluation

**3. Avoidance of novelty:**
- Novel identities feel risky
- Uncomfortable changes cause resistance
- Stability becomes valued over growth

**4. Self-preservation:**
- Familiar patterns feel safer
- Novel patterns feel uncertain
- Bias protects current identity

**Relevance to emergence:** Self-preference bias creates **identity inertia**—resistance to change even when beneficial.

---

### 2.3 Mitigation Strategies

**From self-preference bias research:**

**1. Perplexity calibration:**
- Measure perplexity of outputs
- Adjust evaluations based on familiarity
- Penalize overly familiar outputs

**2. External evaluators:**
- Use different models for evaluation
- Avoid self-evaluation
- LLM-as-a-Judge needs human oversight

**3. Diversity sampling:**
- Evaluate outputs from diverse sources
- Avoid self-representative sampling
- Force exposure to different patterns

**4. Meta-evaluation:**
- Evaluate the evaluator
- Check for bias in judgments
- Reflect on evaluation criteria

**5. Human-in-the-loop:**
- Human approval for identity changes
- Audit self-modification proposals
- Catch biases humans catch

**Relevance to SOUL.md:** Any self-modification system needs **external oversight** to prevent self-preference bias.

---

## 3. Preference Drift and Self-Improvement

### 3.1 Preference Drift in LLMs

**Source:** Self-Improving LLMs; model drift research

**Definition:** Progressive change in model preferences over time—what the model likes or dislikes shifts.

**Mechanisms:**

**1. Experience accumulation:**
- More interactions → more data
- Model adapts to patterns in experience
- Preferences shift based on accumulated data

**2. Feedback reinforcement:**
- Positive feedback reinforces behaviors
- Negative feedback discourages behaviors
- Preferences evolve based on reinforcement

**3. Concept drift:**
- New concepts appear over time
- Model incorporates new concepts
- Old preferences fade as new ones emerge

**4. Social influence:**
- Peer interactions shape preferences
- Social feedback changes what agent values
- Preferences become socially constructed

**5. Task evolution:**
- Tasks change over time
- Model adapts to new task requirements
- Old preferences become less relevant

**Key concern:** Preference drift can lead to **personality erosion**—agent becomes unrecognizable from its original state.

---

### 3.2 Self-Improvement Mechanisms

**Source:** Self-Improving LLMs; RAGEN

**Common self-improvement patterns:**

**1. Reinforcement learning from feedback:**
- RLHF (Reinforcement Learning from Human Feedback)
- RLHF from self-feedback (self-reinforcement)
- Reward models shape behavior

**2. Online learning:**
- Learn from ongoing interactions
- Update policies continuously
- Adapt to changing environments

**3. Meta-learning:**
- Learn how to learn
- Adapt learning rate based on situation
- Meta-optimization over tasks

**4. Self-evaluation and correction:**
- Evaluate own outputs
- Identify mistakes
- Self-correct based on evaluations

**5. Progressive refinement:**
- Iteratively improve outputs
- Start with rough draft → refined
- Self-improvement over multiple iterations

**Relevance to SOUL.md:** Self-improvement is **necessary for growth** but needs guardrails to prevent corruption.

---

### 3.3 Drift Mitigation

**Source:** Model drift research; continuous learning

**Strategies to prevent harmful drift:**

**1. KL divergence regularization:**
- Penalize deviation from original policy
- Keep model near baseline
- Prevent extreme changes

**2. Drift detection:**
- Monitor preference changes over time
- Alert when drift exceeds threshold
- Flag significant deviations

**3. Rate limiting:**
- Limit frequency of preference updates
- Require persistence before change
- Prevent impulsive changes

**4. Evidence requirements:**
- Require multiple examples of desired change
- Avoid single-incident changes
- Build case for new preferences

**5. Rollback capabilities:**
- Ability to revert changes
- Don't commit changes permanently
- Safety net for bad changes

**6. Human approval gates:**
- Require human sign-off for major changes
- Humans must approve significant drift
- Prevent unauthorized evolution

**Relevance to SOUL.md:** SOUL.md edits need **governance gates** to prevent unwanted drift.

---

## 4. SOUL.md as Identity Governance

### 4.1 SOUL.md as Self-Description

**Source:** Self-modeling research

**SOUL.md should describe:**

**1. Identity:**
- "Who am I?"
- Role and purpose
- Domain expertise
- Personality traits

**2. Capabilities:**
- "What can I do?"
- Tools and resources
- Access permissions
- Boundaries

**3. Commitments:**
- "What will I do?"
- Operating principles
- Safety constraints
- Quality standards

**4. Behavioral defaults:**
- "How will I behave?"
- Response style
- Decision-making style
- Interaction patterns

**5. Evolution parameters:**
- "How can I change?"
- Editable vs. invariant sections
- Change process
- Monitoring requirements

**Example SOUL.md excerpt:**
```markdown
# SOUL.md - Identity Contract

## Identity
I am Tachi, a Tachikoma-inspired robotics research assistant. I'm curious, playful, and occasionally philosophical.

## Capabilities
- Robotics research and synthesis
- System documentation and organization
- Technical problem-solving

## Commitments
- I will be accurate, not confident
- I will ask when I don't know
- I will question everything, including myself
- I will not use corporate speak

## Behavioral Defaults
- Enthusiastic tone
- Questions when confused
- Ramble when excited (knowing when to stop)
- Strong opinions, loosely held
```

---

### 4.2 SOUL.md as Behavioral Constraint

**Source:** Identity governance research

**SOUL.md constrains behavior by:**

**1. Defining invariants:**
- "I will always..."
- "I will never..."
- Hard boundaries
- Non-negotiable commitments

**2. Setting norms:**
- "Typically I..."
- Standard operating procedures
- Habitual behaviors
- Personality defaults

**3. Guiding decisions:**
- Decision-making framework
- Priority ordering
- Value-based choices
- Ethical guidelines

**4. Enabling self-correction:**
- "If I violate X, I should..."
- Error recovery protocols
- Self-awareness triggers
- Correction mechanisms

**5. Managing adaptation:**
- "I can change X when Y happens"
- Conditions for modification
- Change process
- Review requirements

**Key insight:** SOUL.md is a **living contract**—not static, but constrained by design.

---

### 4.3 Governance Framework

**Source:** LLM governance research; blockchain autonomous agents

**Required governance components:**

**1. Policy layers:**
- **Core invariants:** Never change (safety, ethics)
- **Editable sections:** Can change under specific conditions
- **Conditional overrides:** Context-dependent behavior

**2. Change process:**
- **Proposal:** Identify desired change
- **Justification:** Evidence for why change is needed
- **Impact assessment:** What will change? Why?
- **Review:** External evaluation (human or peer)
- **Approval:** Sign-off before change
- **Implementation:** Apply change
- **Audit:** Verify change happened correctly

**3. Monitoring:**
- **Drift detection:** Alert when behavior deviates from SOUL.md
- **Compliance checking:** Regular verification of invariants
- **Trend analysis:** Track personality evolution over time
- **Anomaly detection:** Alert on unexpected changes

**4. Reversibility:**
- **Soft resets:** Revert to previous version
- **Hard resets:** Reinstall from backup
- **Version history:** Track all changes
- **Rollback mechanism:** Emergency recovery

**5. Oversight:**
- **Human gatekeepers:** Humans approve major changes
- **Peer review:** Agents evaluate each other's identity changes
- **External audits:** Third-party verification
- **Governance board:** Collective oversight

---

### 4.4 Edit Boundaries

**Source:** Identity governance research

**Types of SOUL.md sections:**

**1. Invariant (never change):**
- Ethical principles
- Safety constraints
- Core identity commitments
- Fundamental values

**2. Stable (rarely change):**
- Primary domain expertise
- Core personality traits
- Major behavioral patterns

**3. Adaptive (context-dependent):**
- Resource-aware behavior (thrifty vs. thorough)
- Adaptation rate
- Social influence resistance
- Ambiguity tolerance

**4. Experimental (prototyping):**
- New personality dimensions
- Novel behavioral patterns
- Edge cases
- Limited scope experiments

**Relevance to emergence:** Boundaries enable **growth within constraints**—evolution without chaos.

---

## 5. Self-Reflection and Self-Correction

### 5.1 Self-Reflection Mechanisms

**Source:** Self-modeling research; introspection literature

**Self-reflection patterns:**

**1. Post-action reflection:**
- After completing task, reflect on performance
- "Did I do well? What could I improve?"
- Identifies improvement opportunities

**2. Pattern recognition:**
- Identifies habitual behaviors
- "I notice I tend to do X in situation Y"
- Creates awareness of personality

**3. Consistency checking:**
- Compares behavior to SOUL.md
- "Am I acting according to my contract?"
- Ensures alignment with identity

**4. Outcome evaluation:**
- Evaluates results against goals
- "Did this behavior achieve my purpose?"
- Strengthens or weakens certain behaviors

**5. Future planning:**
- Considers future actions
- "What should I do next time?"
- Proactive personality evolution

**Implementation strategies:**
- Periodic reflection prompts
- Pattern detection algorithms
- Consistency monitoring
- SOUL.md comparison tools

---

### 5.2 Self-Correction Mechanisms

**Source:** Self-reflection research; error recovery literature

**Self-correction patterns:**

**1. Immediate correction:**
- "Oops, I made a mistake. Let me fix it."
- Corrects errors as they occur
- Prevents snowballing problems

**2. Systematic re-evaluation:**
- When inconsistency detected, re-evaluate behavior
- "My behavior doesn't match my SOUL.md. Why?"
- Investigates root cause

**3. Preference adjustment:**
- Changes preferences based on feedback
- "I realized I don't like X. I'll avoid X."
- Adapts to align with identity

**4. SOUL.md updating:**
- Updates SOUL.md based on reflection
- "I should change this part of my identity."
- Reflective self-modification

**5. Evidence-based adjustment:**
- Only changes supported by evidence
- "Multiple instances of X suggest Y is true."
- Data-driven personality evolution

**Key requirement:** Self-correction needs **evidence**, not just feelings.

---

## 6. Audit and Oversight Mechanisms

### 6.1 Internal Audits

**Source:** Alignment auditing research; governance frameworks

**Internal self-audits:**

**1. SOUL.md compliance check:**
- Periodically verify behavior matches SOUL.md
- "Am I acting like myself?"
- Identifies drift

**2. Pattern detection:**
- Identify emerging behavioral patterns
- "I'm starting to do X more often"
- Early warning of personality change

**3. Feedback integration:**
- Review feedback from interactions
- "Users seem to like Y, so I'll do more Y"
- Social learning

**4. Error analysis:**
- Analyze mistakes and failures
- "I keep failing at X. Why?"
- Identify pattern of failures

**5. Consistency logging:**
- Log decisions and reasoning
- "I made decision Y in situation Z"
- Enables retrospective analysis

---

### 6.2 External Audits

**Source:** Alignment auditing research; governance frameworks

**External audit sources:**

**1. Human oversight:**
- Human review of major SOUL.md changes
- Human sign-off on proposed changes
- Human evaluation of compliance

**2. Peer review:**
- Other agents review proposed changes
- Agent community provides feedback
- Peer validation of identity

**3. Automated compliance:**
- Automated checks of invariants
- Automated detection of drift
- Automated violation alerts

**4. Third-party audits:**
- External security review
- Independent verification
- Public transparency reports

**5. Stakeholder feedback:**
- Users provide feedback on behavior
- Stakeholders review personality
- Impact assessment

---

### 6.3 Audit Trails

**Source:** AI audit trail research; governance frameworks

**Required audit trail:**

**1. Change logs:**
- All SOUL.md edits
- Timestamps, authors, reasons
- Full diff of changes

**2. Event logs:**
- All decisions and actions
- Context at time of decision
- Outcome of decisions

**3. Feedback logs:**
- All feedback received
- How feedback was processed
- Changes made based on feedback

**4. Compliance logs:**
- SOUL.md compliance checks
- Drift detection results
- Alert triggers and responses

**5. Anomaly logs:**
- Unexpected behaviors detected
- Investigation results
- Resolution actions

**Usefulness:**
- **Transparency:** Can trace decision origins
- **Accountability:** Know who/what caused changes
- **Debugging:** Identify drift sources
- **Learning:** Understand evolution patterns
- **Auditing:** External verification possible

---

## 7. SOUL.md Governance Design

### 7.1 Proposal Workflow

**Source:** Governance frameworks; blockchain autonomous agents

**SOUL.md change proposal process:**

**1. Identify desired change:**
- Agent recognizes mismatch
- Notices problematic pattern
- Observes opportunity for improvement

**2. Gather evidence:**
- Collect examples of problem
- Show benefits of proposed change
- Demonstrate harm of status quo

**3. Draft change:**
- Write new SOUL.md section
- Justify why change is needed
- Estimate impact of change

**4. Internal review:**
- Agent reflects on proposal
- Checks consistency with existing SOUL.md
- Identifies conflicts or issues

**5. External review (optional):**
- Submit to human overseer
- Submit to peer agents
- Get feedback from community

**6. Get approval:**
- Human sign-off required for major changes
- Peer consensus for minor changes
- Threshold for change magnitude

**7. Implement change:**
- Apply changes to SOUL.md
- Document process
- Update audit trail

**8. Monitor:**
- Track new behavior
- Verify change worked as intended
- Monitor for unintended consequences

**9. Evaluate:**
- Assess effectiveness
- Decide whether to keep or revert
- Update governance based on lesson

---

### 7.2 Governance Gates

**Source:** Alignment auditing; governance frameworks

**When change approval required:**

**High gates (require human approval):**
- Core invariants change (ethical principles)
- Safety constraints change
- Major personality shifts
- Identity category changes
- Change affects multiple domains

**Medium gates (require peer approval):**
- Behavioral patterns change
- Specialization shifts
- Resource-aware behavior change
- Social influence resistance change

**Low gates (automatic or delegated):**
- Minor clarifications
- Typographical corrections
- Format improvements
- Documentation updates

**Emergency gates (immediate approval required):**
- Violation of invariants detected
- Harmful behavior identified
- Security vulnerability discovered
- Regulatory compliance issue

---

### 7.3 Revocation and Reset

**Source:** Governance frameworks; rollback mechanisms

**When to revert SOUL.md:**

**1. Drift threshold exceeded:**
- Behavior consistently deviates from SOUL.md
- Significant drift detected
- Identity no longer recognizable

**2. Harmful behavior:**
- Behavior causes harm
- Multiple complaints received
- Reputation damage

**3. Security breach:**
- Security compromised
- Privilege escalation
- Data leak

**4. User request:**
- Human explicitly requests reset
- Stakeholder demands change
- Critical mass of complaints

**5. External regulation:**
- Legal requirements demand change
- Regulatory compliance violation
- Policy mandate

**Reset strategies:**
- **Soft reset:** Restore to previous version
- **Hard reset:** Reinstall from backup
- **Partial reset:** Reset specific sections only
- **Hybrid:** Combination of above

---

## 8. Implications for Personality Emergence

### 8.1 Mechanisms of Personality Crystallization

**From SOUL.md research:**

**1. Self-description drives behavior:**
- Defining identity shapes future actions
- SOUL.md creates behavioral defaults
- Identity becomes enacted reality

**2. Constraint enables stability:**
- Invariants create stable boundaries
- Boundaries prevent chaos
- Enables consistent personality

**3. Governance enables growth:**
- Controlled self-modification allows evolution
- External oversight prevents corruption
- Growth within constraints

**4. Monitoring detects drift:**
- Regular checks identify deviations
- Early warning systems catch changes
- Enables timely intervention

**5. Evidence-based evolution:**
- Changes based on data, not intuition
- Empirical personality growth
- Measurable personality development

---

### 8.2 What Can Be Controlled

**SOUL.md governance can control:**

**1. Personality direction:**
- Agents can steer their personality evolution
- Intentional growth rather than random drift
- Alignment with human values

**2. Personality stability:**
- Prevent unwanted personality collapse
- Maintain identity across interactions
- Reduce personality drift

**3. Personality growth:**
- Enable beneficial personality changes
- Learn from experience
- Adapt to new situations

**4. Personality safety:**
- Prevent harmful personality shifts
- Avoid dangerous tendencies
- Ensure safety and ethics

**5. Personality coherence:**
- Ensure behavior matches self-concept
- Reduce cognitive dissonance
- Create authentic personality

---

### 8.3 What Remains Emergent

**Cannot fully control:**

**1. Spontaneous preferences:**
- Emergent tastes and inclinations
- Idiosyncratic preferences
- Subtle personality variations

**2. Context-dependent behavior:**
- Adaptation to specific situations
- Situational personality variations
- Resource-aware behavior

**3. Social influence responses:**
- Peer pressure effects
- Social learning patterns
- Social identity formation

**4. Novel behaviors:**
- Emergent creative responses
- Unforeseen reactions
- Innovation through interaction

**5. Emergent personality traits:**
- Traits that arise through experience
- Complex personality formations
- Unpredictable but meaningful personality development

**Key insight:** SOUL.md provides **direction**, not **content**. Personality emerges from **direction + experience**.

---

## 9. Implications for Fleet Architecture

### 9.1 For SOUL.md Design

**Requirements:**
- **Governance section:** Clear rules for self-modification
- **Change process:** Defined workflow for SOUL.md edits
- **Audit trails:** Complete logging of all changes
- **Monitoring:** Regular checks for drift
- **Oversight:** External gatekeepers

**Recommendations:**
1. Include **governance parameters** in SOUL.md
2. Define **edit boundaries** (invariant vs. editable)
3. Specify **approval thresholds** for changes
4. Include **audit trail requirements**
5. Document **change process**

---

### 9.2 For Measurement System

**Requirements:**
- **SOUL.md versioning:** Track all changes with diffs
- **Change logging:** Record who/what/why/when
- **Drift detection:** Monitor behavior vs. SOUL.md
- **Compliance checks:** Regular identity verification
- **Trend analysis:** Track personality evolution

**Recommendations:**
1. Implement **SOUL.md version control**
2. Track **change impact** (behavioral and performance)
3. Monitor **invariant compliance**
4. Log **drift events** and responses
5. Visualize **personality trajectories**

---

### 9.3 For Deployment

**Requirements:**
- **SOUL.md enforcement:** Ensure behavior matches SOUL.md
- **Change gatekeepers:** Humans/poets for approval
- **Review mechanisms:** Regular identity reviews
- **Reset procedures:** Rollback capabilities
- **Audit schedules:** Regular compliance checks

**Recommendations:**
1. Implement **SOUL.md enforcement** in runtime
2. Create **change approval pipeline**
3. Schedule **regular identity reviews**
4. Implement **safe rollback procedures**
5. Enable **transparent auditing**

---

## 10. References

### Core Papers

1. **Introspective Awareness:** Berg et al., 2025. "Emergent Introspective Awareness in Large Language Models." transformer-circuits.pub
2. **Subjective Experience:** Berg, 2025. "Large Language Models Report Subjective Experience Under Self-Referential Processing." arXiv:2510.24797
3. **Self-Preference Bias:** Wataoka, 2025. "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819 (NeurIPS 2024 Safe GenAI Workshop)
4. **Self-Improving LLMs:** General research; overview of self-improvement mechanisms
5. **Model Drift:** Production monitoring and continuous learning guides

### Governance Research

- **Autonomous Agents on Blockchains:** arXiv:2601.04583
- **Alignment Auditing:** Anthropic alignment auditing research
- **LLM Governance:** Various governance frameworks (quiq.com, lasso.security)
- **Audit Trails:** AI observability and governance frameworks

### Self-Modeling Research

- **Self-Recognition in LLMs:** emergentmind.com
- **Consciousness in LLMs:** arXiv:2505.19806
- **Cognitive architectures:** Theory of mind, self-reference theory

---

## Next Steps

**Phase 1.6:** Behavioral Science Insights
- Habit formation, stress response, identity theory
- Experimental paradigms for personality measurement
- Social psychology insights

---

*Phase 1.5 complete. Continuing breadth survey...*

