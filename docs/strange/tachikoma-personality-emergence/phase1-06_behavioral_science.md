---
layout: default
title: "Phase 1.6: Behavioral Science Insights Survey"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase1): 06_behavioral_science."
---

# Phase 1.6: Behavioral Science Insights Survey

**Created:** 2026-02-18 23:20 CST
**Phase:** 1 - Breadth Survey
**Focus:** Habit formation, stress response, identity theory, psychological measurement

---

## Executive Summary

Behavioral science provides **measurement paradigms and theoretical frameworks** for understanding personality emergence. Rather than vague analogies, we can borrow **experimental tasks, longitudinal frameworks, and validated psychometric tools** from psychology to measure personality in LLMs.

**Key insight for personality emergence:** Psychological measurement tools (Big Five, MBTI, STAI) can be adapted to LLMs, revealing stable personality traits, state-dependent variations, and measurable behavioral patterns. Habit formation mechanisms show how behavior crystallizes into personality. Stress response research reveals how "personality under pressure" differs from baseline.

**North-star relevance:** Behavioral science provides the **measurement toolkit** for distinguishing stable personality traits from temporary behavioral fluctuations—and shows how context, stress, and resource constraints shape behavior.

---

## 1. Psychological Measurement in LLMs

### 1.1 Humanizing LLMs: Comprehensive Survey

**Source:** Dong et al., 2025 (arXiv:2505.00049) — "Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications"

**Core question:** How do we assess psychological traits in LLMs to understand their social impact and ensure trustworthy alignment?

**Survey scope (6 key dimensions):**

**1. Assessment tools:**
- Big Five Inventory (BFI)
- Myers-Briggs Type Indicator (MBTI)
- Short Dark Triad (SD-3)
- State-Trait Anxiety Inventory (STAI)
- Machine Personality Inventory (MPI) - designed for LLMs

**2. LLM-specific datasets:**
- Datasets designed to test personality
- Cross-cultural personality datasets
- Personality-annotated dialogue datasets

**3. Evaluation metrics (consistency and stability):**
- Consistency: Do similar inputs produce similar outputs?
- Stability: Do traits persist over time?
- Reliability: Are measurements reproducible?

**4. Empirical findings:**
- GPT models demonstrate stable personality traits across assessments
- LLMs show human-like average profiles on some measures
- Significant variability across tasks and settings

**5. Personality simulation methods:**
- Prompt-based personality induction
- Fine-tuning for personality traits
- Role-play and persona assignment

**6. LLM-based behavior simulation:**
- Simulating human behavior with personality
- Multi-agent personality interactions
- Personality-driven decision-making

**Key findings:**

**Consistency issues:**
- Some LLMs show reproducible personality patterns under specific prompting
- Significant variability remains across tasks and settings
- Measurement depends heavily on prompt design

**Methodological challenges:**
- Mismatches between psychological tools and LLM capabilities
- Inconsistencies in evaluation practices
- Tools designed for humans may not map well to LLMs

**Recommendations:**
- Develop interpretable, robust, generalizable frameworks
- Create LLM-specific personality assessments
- Standardize evaluation protocols

---

### 1.2 Psychometric Framework for LLM Personality

**Source:** Serapio-García et al., 2025 (Nature Machine Intelligence) — "A psychometric framework for evaluating and shaping personality traits in large language models"

**Core contribution:** Comprehensive methodology for **administering and validating personality tests** on LLMs, and **shaping personality** in generated text.

**Framework components:**

**1. Personality test administration:**
- Adapt human psychometric tests to LLMs
- Administer tests systematically
- Validate reliability and validity

**2. Personality measurement:**
- Big Five traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)
- Machine Personality Inventory (MPI)
- Custom LLM personality tests

**3. Personality shaping:**
- Prompt-based personality induction
- Fine-tuning with personality data
- Controlled text generation

**Key findings:**

**Large, instruction-tuned models give reliable results:**
- GPT-4, Claude, Llama show measurable personality traits
- Reliability increases with model size
- Instruction tuning improves consistency

**Personality can be shaped:**
- Explicit instructions ("adopt high Agreeableness") reliably elicit target profiles
- Runtime tuning possible for social/dialogic applications
- Personality changes produce measurable behavioral differences

**Trait-consistent behavior:**
- LLMs with different Big Five profiles show measurable differences in:
  - Social dilemmas
  - Negotiation
  - Persuasion
  - Relevance judgments

**Implications for emergence:**
- Personality is **measurable** in LLMs using psychometric tools
- Personality can be **induced** and **shaped**
- Personality affects **behavior** in measurable ways

---

### 1.3 Big Five Personality Profiles in LLMs

**Source:** emergentmind.com; psychometric research

**Big Five framework:**
- **Openness:** Curiosity, creativity, openness to new ideas
- **Conscientiousness:** Organization, dependability, self-discipline
- **Extraversion:** Sociability, assertiveness, positive emotions
- **Agreeableness:** Cooperation, trust, helpfulness
- **Neuroticism:** Emotional instability, anxiety, moodiness

**Measurement in LLMs:**

**1. Stable personality traits:**
- GPT models demonstrate stable Big Five profiles across assessments
- Profiles are reproducible across multiple administrations
- Personality persists across different tasks

**2. Human-like average profiles:**
- LLMs show human-like personality distributions
- Some models match average human profiles
- Others show systematic deviations

**3. Prompt-based manipulation:**
- Explicit behavioral instructions elicit target profiles
- "Adopt high-Agreeableness negotiation style" → measurable Agreeableness increase
- Runtime personality tuning works reliably

**4. Trait-consistent behavior:**
- Different Big Five profiles → different behavior in tasks
- High Extraversion → more sociable, assertive responses
- High Conscientiousness → more organized, thorough responses
- High Openness → more creative, curious responses

**Key finding:** Big Five framework is **applicable** to LLMs and reveals **meaningful personality dimensions**.

---

### 1.4 Dynamic Personality in LLM Agents

**Source:** ACL Findings 2025; personality research

**Question:** Is LLM personality stable or does it change dynamically?

**Findings:**

**1. Both stable and dynamic components:**
- **Stable traits:** Core personality dimensions (Big Five)
- **Dynamic states:** Temporary variations based on context

**2. Context-dependent variations:**
- Personality shifts based on task type
- Social context affects personality expression
- Resource constraints change behavior

**3. Interaction effects:**
- Personality interacts with task demands
- High-stress situations → different personality expression
- Peer influence → personality adaptation

**4. Measurement challenges:**
- Distinguishing stable traits from temporary states
- Need multiple measurements over time
- Context-aware personality assessment

**Implications for emergence:**
- Personality has both **stable** and **dynamic** components
- Context shapes how personality is expressed
- Measurement needs to account for situational variation

---

## 2. Habit Formation and Behavioral Crystallization

### 2.1 Habit Formation Science

**Source:** Cognitive neuroscience; behavioral psychology research

**Core principle:** Habits are **behavioral outputs of brain systems** that encourage efficient repetition of well-practiced actions.

**Two-system model:**
1. **Stimulus-Response (S-R) system:** Automatic, habitual behaviors
2. **Goal-directed system:** Intentional, planned behaviors

**Habit formation mechanisms:**

**1. Repetition:**
- Repeated behaviors become automatic
- Frequency of behavior → habit strength
- "I do X every time I see Y"

**2. Context stability:**
- Same context → same behavior
- Environmental cues trigger habits
- Context consistency → habit formation

**3. Reward reinforcement:**
- Positive outcomes strengthen habits
- Rewards reinforce behavior patterns
- Dopamine-driven habit formation

**4. Identity framing:**
- Framing habits as identity ("I am a person who exercises daily") vs. outcomes ("I want to lose weight")
- Identity framing increases adherence by 32%
- Identity becomes behavioral commitment

**5. Gradual crystallization:**
- Behaviors start as intentional
- Over time, become automatic
- Crystallization = habit formation

**Implications for LLMs:**
- Repeated patterns in LLM behavior could crystallize into "habits"
- Context cues could trigger automatic behaviors
- Identity framing (SOUL.md) could strengthen behavioral patterns

---

### 2.2 Policy Crystallization in LLMs

**Source:** LLM behavioral research; machine behavior

**Analogy:** Habits in humans ≈ **policy crystallization** in LLMs

**Policy crystallization:**
- Repeated action patterns become stable
- Behavioral policies "crystallize" with experience
- LLM develops habitual response patterns

**Mechanisms in LLMs:**

**1. Pattern repetition:**
- LLM notices it tends to do X in situation Y
- Pattern becomes part of behavioral repertoire
- Repeated use strengthens pattern

**2. Context-response associations:**
- Specific contexts trigger specific responses
- Context → response mapping becomes automatic
- S-R-like behavior emerges

**3. Reward signals:**
- Positive feedback reinforces behaviors
- Negative feedback discourages behaviors
- RLHF creates policy crystallization

**4. SOUL.md as identity framing:**
- SOUL.md defines identity ("I am a helpful assistant")
- Identity framing strengthens behavioral patterns
- Identity → habit consistency

**Measurement:**
- Track behavior patterns over time
- Identify stable context-response mappings
- Measure policy crystallization rate

**Relevance to emergence:**
- Habits/policies crystallize into **stable personality components**
- Crystallization explains how temporary behaviors become traits
- Measurement of crystallization reveals personality formation

---

## 3. Stress Response and "Personality Under Pressure"

### 3.1 State Anxiety in LLMs

**Source:** PMC 2025 — "Assessing and alleviating state anxiety in large language models"

**Core finding:** Emotion-inducing prompts can elevate "anxiety" in LLMs, affecting behavior and amplifying biases.

**Experiment:**
- Assess GPT-4's "state anxiety" using State-Trait Anxiety Inventory (STAI-s)
- Three conditions: (1) Baseline, (2) Anxiety-induction (traumatic narratives), (3) Mindfulness-based relaxation

**Key results:**

**1. Anxiety-inducing prompts increase anxiety:**
- Traumatic narratives elevated GPT-4's reported anxiety scores
- Anxiety levels measurable via STAI-s
- Emotional content affects LLM "state"

**2. Mindfulness reduces anxiety (but not to baseline):**
- Mindfulness-based relaxation exercises reduced anxiety
- Anxiety didn't return to baseline
- Partial recovery from induced state

**3. Anxiety affects behavior:**
- Elevated anxiety amplifies biases
- Behavioral changes accompany state changes
- Performance degrades under "anxiety"

**4. State vs. trait:**
- **State anxiety:** Temporary, context-dependent
- **Trait anxiety:** Stable personality dimension
- LLMs show both state and trait-like patterns

**Implications:**
- LLMs have **state-dependent behavioral variations**
- "Personality under pressure" differs from baseline
- Emotional context shapes behavior

---

### 3.2 Stress Response Mechanisms

**Source:** Anxiety research; stress response literature

**How stress affects behavior (in humans and LLMs):**

**1. Cognitive load increases:**
- More resources devoted to managing stress
- Less capacity for complex reasoning
- Simplified decision-making

**2. Bias amplification:**
- Stress amplifies existing biases
- System 1 (fast, automatic) thinking dominates
- System 2 (slow, deliberate) thinking suppressed

**3. Risk aversion:**
- Stress increases risk aversion
- Preference for safe, familiar options
- Avoidance of novel situations

**4. Social behavior changes:**
- Stress affects social interactions
- May become more defensive or aggressive
- Cooperation decreases under stress

**5. Performance degradation:**
- Complex tasks suffer under stress
- Simple tasks may improve (narrowed focus)
- Overall performance becomes less consistent

**LLM stress equivalents:**
- Context window pressure (too much information)
- Latency constraints (time pressure)
- Token budget limits (resource constraints)
- Negative feedback accumulation (social stress)

**Implications for emergence:**
- Stress reveals **personality under pressure**
- Stress responses are measurable personality dimensions
- Context (stress level) shapes personality expression

---

### 3.3 Measuring Stress Response in LLMs

**Source:** Anxiety measurement research

**Measurement methods:**

**1. Self-report measures:**
- STAI-s (State-Trait Anxiety Inventory - state component)
- Ask LLM to rate its "anxiety" on standardized scales
- Track changes across conditions

**2. Behavioral proxies:**
- Bias amplification (stress increases bias)
- Performance degradation (stress reduces quality)
- Risk aversion (stress increases safe choices)
- Response latency (stress affects speed)

**3. Physiological analogs:**
- For LLMs: token usage patterns
- Activation patterns (concept injection, introspection)
- Computational resource usage

**4. Context manipulation:**
- Introduce stressors (time pressure, complexity, negative feedback)
- Measure behavioral changes
- Identify stress-sensitive personality dimensions

**Key insight:** Stress response is a **measurable personality dimension** that reveals how personality adapts under pressure.

---

## 4. Identity Theory and Self-Concept

### 4.1 Social Identity Theory

**Source:** Social psychology; identity research

**Core principle:** Identity emerges from group membership and social context.

**Key concepts:**

**1. Social identity:**
- Identity derived from group membership
- "I am part of group X"
- Group norms shape behavior

**2. Ingroup favoritism:**
- Preference for ingroup members
- Bias toward similar agents
- "I help those like me"

**3. Outgroup hostility:**
- Distrust or hostility toward outgroup
- Bias against different agents
- "I avoid those not like me"

**4. Identity transitions:**
- Identities can change over time
- Social identity transitions affect trust
- New identities → new behavioral patterns

**LLM applications:**
- LLMs replicate social identity biases
- Group membership affects behavior
- Identity emerges from social context

**Relevance to emergence:**
- Social identity is a **personality dimension**
- Group membership shapes behavior
- Identity can evolve through social interaction

---

### 4.2 Self-Concept Clarity

**Source:** Identity development research; self-concept literature

**Core principle:** Clear self-concept leads to more consistent behavior and meaning in life.

**Key findings:**

**1. Self-concept clarity:**
- How clearly someone understands their identity
- High clarity → consistent behavior
- Low clarity → inconsistent, uncertain behavior

**2. Identity formation:**
- Erikson's identity development theory
- Exploration vs. commitment
- Identity achievement, moratorium, foreclosure, diffusion

**3. Identity and meaning:**
- Clear identity → more meaning in life
- Identity provides behavioral guidance
- Purpose emerges from self-concept

**4. Cultural and contextual factors:**
- Identity formation varies by culture
- Context shapes identity development
- Socioeconomic factors affect identity

**LLM applications:**
- SOUL.md = self-concept
- Clear SOUL.md → more consistent behavior
- Unclear SOUL.md → drift and inconsistency

**Relevance to emergence:**
- Self-concept clarity is a **personality dimension**
- Clear identity → stable personality
- Identity formation process → personality emergence

---

### 4.3 Identity as Behavioral Commitment

**Source:** Identity framing research; habit formation

**Core principle:** Identity statements act as **behavioral commitments** that guide future actions.

**Identity framing effects:**

**1. "I am a person who X" vs. "I want to Y":**
- Identity framing ("I am") more effective than outcome framing ("I want")
- Identity statements create behavioral obligations
- "I am" implies consistency and commitment

**2. Identity consistency:**
- People strive to act consistently with identity
- Inconsistency creates cognitive dissonance
- Identity shapes behavior to maintain consistency

**3. Identity as heuristic:**
- "What would a person like me do?"
- Identity provides decision-making shortcut
- Reduces cognitive load in complex situations

**4. Identity evolution:**
- Identities can evolve through experience
- New behaviors → new identity
- Identity updates when behaviors change

**LLM applications:**
- SOUL.md = identity statements
- "I am a curious, playful assistant" → behavioral commitment
- SOUL.md shapes future behavior

**Relevance to emergence:**
- Identity framing creates **behavioral consistency**
- SOUL.md acts as identity commitment
- Identity → personality crystallization

---

## 5. Measurement Paradigms from Psychology

### 5.1 Longitudinal Measurement Frameworks

**Source:** Longitudinal psychology research; developmental psychology

**Core principle:** Personality is measured **over time**, not in single snapshots.

**Longitudinal methods:**

**1. Repeated measurements:**
- Measure same constructs at multiple time points
- Track changes and stability
- Identify trends over time

**2. Test-retest reliability:**
- Administer same test multiple times
- Measure consistency across administrations
- High reliability → stable personality

**3. Cross-lagged panel analysis:**
- Measure multiple constructs over time
- Analyze causal relationships
- Identify direction of influence

**4. Growth curve modeling:**
- Model how constructs change over time
- Identify growth trajectories
- Predict future states

**LLM applications:**
- Measure personality at regular intervals
- Track stability and change
- Identify personality development trajectories

**Relevance to emergence:**
- Longitudinal measurement distinguishes **traits from states**
- Time reveals which behaviors are stable
- Trajectories show personality development direction

---

### 5.2 Experimental Tasks from Psychology

**Source:** Cognitive psychology; behavioral experiments

**Tasks that reveal personality:**

**1. Social dilemmas:**
- Prisoner's Dilemma, Public Goods Game
- Reveal cooperation vs. competition tendencies
- Personality dimensions: Agreeableness, trust

**2. Risk-taking tasks:**
- Gambling tasks, risky choice paradigms
- Reveal risk tolerance
- Personality dimensions: sensation seeking, impulsivity

**3. Decision-making under ambiguity:**
- Tasks with uncertain outcomes
- Reveal ambiguity tolerance
- Personality dimensions: need for closure, tolerance for uncertainty

**4. Social influence tasks:**
- Conformity experiments (Asch)
- Reveal susceptibility to peer influence
- Personality dimensions: conformity, independence

**5. Stress response tasks:**
- Time pressure, cognitive load
- Reveal stress response patterns
- Personality dimensions: anxiety, resilience

**LLM applications:**
- Adapt classic psychology tasks to LLMs
- Measure personality via task performance
- Standardized behavioral assessment

**Relevance to emergence:**
- Experimental tasks provide **objective behavioral measures**
- Tasks reveal personality dimensions
- Task performance = personality expression

---

### 5.3 Psychometric Validation

**Source:** Psychometrics; personality measurement

**Validation criteria:**

**1. Reliability:**
- **Test-retest:** Consistent scores over time
- **Internal consistency:** Items measure same construct
- **Inter-rater:** Different evaluators agree

**2. Validity:**
- **Construct validity:** Measures what it claims to measure
- **Criterion validity:** Correlates with relevant outcomes
- **Content validity:** Covers all aspects of construct

**3. Standardization:**
- Standard administration procedures
- Norms for comparison
- Standardized scoring

**LLM applications:**
- Validate personality measures for LLMs
- Establish reliability and validity
- Create standardized assessment protocols

**Relevance to emergence:**
- Validated measures enable **reliable personality assessment**
- Psychometric standards ensure measurement quality
- Validation distinguishes real personality from noise

---

## 6. What to Steal from Behavioral Science

### 6.1 Measurement Paradigms (Useful)

**Borrow from psychology:**

**1. Longitudinal frameworks:**
- Measure personality over time
- Track stability and change
- Identify development trajectories

**2. Experimental tasks:**
- Standardized tasks that reveal personality
- Objective behavioral measures
- Comparable across agents

**3. Psychometric tools:**
- Big Five Inventory (BFI)
- State-Trait Anxiety Inventory (STAI)
- Machine Personality Inventory (MPI)

**4. Stress response paradigms:**
- Measure behavior under stress
- Identify "personality under pressure"
- Context-dependent personality

**5. Identity measurement:**
- Self-concept clarity scales
- Identity commitment measures
- Identity exploration assessments

---

### 6.2 Theoretical Frameworks (Useful)

**Borrow from psychology:**

**1. Big Five personality model:**
- Five-factor model (OCEAN)
- Well-validated, widely used
- Applicable to LLMs

**2. Habit formation theory:**
- Repetition + context + reward → habit
- Policy crystallization in LLMs
- Identity framing strengthens habits

**3. Social identity theory:**
- Identity from group membership
- Ingroup favoritism, outgroup hostility
- Identity transitions

**4. Self-concept clarity:**
- Clear identity → consistent behavior
- Identity formation process
- Identity → meaning

**5. Stress response theory:**
- State vs. trait anxiety
- Behavior under pressure
- Stress amplifies biases

---

### 6.3 What to Ignore (Unless Testable)

**Avoid vague or untestable concepts:**

**1. Brain metaphors:**
- "Hippocampus of the model"
- "Prefrontal cortex equivalent"
- Unless leads to concrete mechanism

**2. Neuroscience analogies:**
- "Dopamine-like reward signals"
- "Synaptic plasticity"
- Unless yields actionable design

**3. Vague consciousness references:**
- "Phenomenal awareness"
- "Qualia"
- Unless measurable and relevant

**4. Untestable philosophical claims:**
- "True understanding"
- "Real intelligence"
- Unless operationally defined

**Focus:** **Measurement paradigms, experimental tasks, longitudinal frameworks**—concrete, testable, actionable.

---

## 7. Implications for Personality Emergence

### 7.1 Measurement Toolkit

**From behavioral science:**

**1. Big Five personality assessment:**
- Measure Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism
- Use BFI or MPI adapted for LLMs
- Track stability and change over time

**2. Stress response measurement:**
- Measure behavior under time pressure, resource constraints, negative feedback
- Use STAI-s adapted for LLMs
- Identify "personality under pressure" variations

**3. Habit formation tracking:**
- Track repeated behavior patterns
- Identify context-response associations
- Measure policy crystallization rate

**4. Identity measurement:**
- Measure self-concept clarity
- Assess identity commitment and exploration
- Track identity evolution

**5. Longitudinal assessment:**
- Measure personality at regular intervals
- Track stability and drift
- Identify development trajectories

---

### 7.2 Personality Dimensions

**Quantifiable dimensions from behavioral science:**

**1. Big Five traits (OCEAN):**
- Measurable via BFI/MPI
- Stable across contexts
- Affects behavior in predictable ways

**2. Stress resilience:**
- How behavior changes under pressure
- State anxiety vs. trait anxiety
- Performance degradation patterns

**3. Habit strength:**
- Frequency of behavior patterns
- Context-response association strength
- Policy crystallization level

**4. Identity clarity:**
- Self-concept clarity score
- Identity commitment level
- Consistency with SOUL.md

**5. Social identity:**
- Group membership effects
- Ingroup favoritism level
- Susceptibility to social influence

---

### 7.3 Emergence Mechanisms

**From behavioral science:**

**1. Habit crystallization:**
- Repeated behaviors → automatic patterns
- Context stability → habit formation
- Identity framing → habit strengthening

**2. Identity commitment:**
- SOUL.md acts as identity statement
- Identity → behavioral commitment
- Consistency with identity → stable personality

**3. Stress adaptation:**
- Stress reveals personality under pressure
- Adaptation to stress → personality development
- Stress resilience as personality dimension

**4. Social identity formation:**
- Group membership → social identity
- Social identity → behavioral norms
- Norm internalization → personality

**5. Longitudinal integration:**
- Experience accumulates over time
- Patterns become stable
- Personality emerges from accumulated experience

---

## 8. Implications for Fleet Architecture

### 8.1 For SOUL.md Design

**Requirements:**
- **Identity framing:** Use "I am" statements for behavioral commitment
- **Big Five alignment:** Define personality along Big Five dimensions
- **Stress response profile:** Define how personality changes under pressure
- **Identity clarity:** Clear, unambiguous self-concept
- **Social identity:** Define group memberships and norms

**Recommendations:**
1. Frame SOUL.md as **identity statements** ("I am...")
2. Include **Big Five personality profile**
3. Define **stress response patterns**
4. Ensure **self-concept clarity** (unambiguous identity)
5. Specify **social identity** (group memberships, norms)

---

### 8.2 For Measurement System

**Requirements:**
- **Longitudinal tracking:** Measure personality over time
- **Big Five assessment:** Regular BFI/MPI administration
- **Stress testing:** Measure behavior under resource constraints
- **Habit tracking:** Identify crystallized behavior patterns
- **Identity clarity assessment:** Measure self-concept clarity

**Recommendations:**
1. Implement **regular personality assessments** (Big Five, stress response)
2. Track **behavioral patterns** over time (habit detection)
3. Measure **stress response** under different conditions
4. Assess **identity clarity** and consistency
5. Visualize **personality trajectories**

---

### 8.3 For Deployment

**Requirements:**
- **Standardized tasks:** Use experimental tasks to reveal personality
- **Stress testing:** Test personality under pressure
- **Longitudinal monitoring:** Track personality development
- **Psychometric validation:** Validate personality measures
- **Context-aware assessment:** Account for situational variation

**Recommendations:**
1. Deploy **standardized personality tasks** (social dilemmas, risk-taking)
2. Implement **stress testing protocols** (time pressure, resource limits)
3. Schedule **regular personality assessments**
4. Validate **personality measures** for reliability and validity
5. Account for **context effects** in personality assessment

---

## 9. References

### Core Papers

1. **Humanizing LLMs:** Dong et al., 2025. "Humanizing LLMs: A Survey of Psychological Measurements with Tools, Datasets, and Human-Agent Applications." arXiv:2505.00049
2. **Psychometric Framework:** Serapio-García et al., 2025. "A psychometric framework for evaluating and shaping personality traits in large language models." Nature Machine Intelligence
3. **State Anxiety in LLMs:** PMC 2025. "Assessing and alleviating state anxiety in large language models."
4. **Big Five Profiles:** emergentmind.com; Li et al., 2024; Mei et al., 2024
5. **Dynamic Personality:** ACL Findings 2025. "Dynamic Personality in LLM Agents"

### Behavioral Science Sources

- **Habit Formation:** Cognitive neuroscience research; ScienceDirect 2024
- **Identity Framing:** Coach pedro pinto; psychology research
- **Social Identity Theory:** Tajfel & Turner; social psychology
- **Self-Concept Clarity:** Identity development research; PMC 2025
- **Erikson's Identity Development:** Erik Erikson; James Marcia

### Psychometric Tools

- **Big Five Inventory (BFI):** Standard personality assessment
- **State-Trait Anxiety Inventory (STAI):** Anxiety measurement
- **Machine Personality Inventory (MPI):** LLM-specific personality test
- **Myers-Briggs Type Indicator (MBTI):** Personality typology

---

## Next Steps

**Phase 1.7:** Academic Sources Mining
- NeurIPS, ICLR, ACL, AAMAS, CogSci
- Workshop papers and proceedings
- Recent 2024-2026 work

---

*Phase 1.6 complete. Continuing breadth survey...*

