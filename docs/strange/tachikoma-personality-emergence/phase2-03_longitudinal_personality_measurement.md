---
layout: default
title: "Phase 2.3: Longitudinal Personality Measurement - Depth Dive"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase2): 03_longitudinal_personality_measurement."
---

# Phase 2.3: Longitudinal Personality Measurement - Depth Dive

**Created:** 2026-02-19 01:05 CST
**Phase:** 2 - Depth Dives
**Priority:** 3 (High)
**Focus:** Psychometric tool adaptation, measurement frameworks, stability quantification

---

## Executive Summary

**Longitudinal personality measurement** is the **validation layer** that proves personality emergence is working. Research reveals a critical finding: LLM personality measurements show **limited temporal stability** (Bodroža et al., 2024), with significant sensitivity to prompt variations, option ordering, and context changes.

**The measurement challenge:** How do we distinguish **stable personality traits** from **temporary behavioral fluctuations**? Research shows:
- **Trait scores are stable to prompt-paraphrase** (~25% sensitivity) (Lee et al., 2024)
- **Large, instruction-tuned models give reliable results** (Serapio-García et al., 2025, Nature MI)
- **Standard self-report tests have limitations** for LLMs (TRAIT benchmark)

**For Tachikoma Fleet:** Longitudinal measurement provides the **quantitative foundation** for validating personality emergence, detecting drift, and proving that agents develop distinct, stable personalities over time.

**Actionable framework:**
1. **Adapt psychometric tools:** Big Five (BFI-2), TRAIT benchmark, custom LLM-specific tests
2. **Longitudinal tracking:** Weekly/bi-weekly assessments, trajectory analysis
3. **Stability metrics:** Test-retest reliability, consistency scores, drift detection
4. **Stress testing:** Personality under constraints reveals true traits
5. **Behavioral validation:** Correlate self-report with actual behavior

---

## 1. Psychometric Assessment in LLMs

### 1.1 Big Five Framework for LLMs

**Source:** Serapio-García et al., 2025 (Nature Machine Intelligence); emergentmind.com

**Core finding:** Large, instruction-tuned models give **reliable personality measurement results** using psychometric tests.

**Big Five traits (OCEAN):**
- **Openness:** Curiosity, creativity, openness to new ideas
- **Conscientiousness:** Organization, dependability, self-discipline
- **Extraversion:** Sociability, assertiveness, positive emotions
- **Agreeableness:** Cooperation, trust, helpfulness
- **Neuroticism:** Emotional instability, anxiety, moodiness

**Measurement instruments adapted for LLMs:**
- **BFI (Big Five Inventory):** Standard 44-item questionnaire
- **BFI-2:** Updated 60-item version with better psychometrics
- **IPIP-NEO:** International Personality Item Pool version
- **HEXACO-100:** Six-factor model (adds Honesty-Humility)
- **TIPI:** Ten-Item Personality Inventory (brief)
- **mini-IPIP:** 20-item short form

**Administration method:**
> "Wrap standard personality test items in controlled prompts formatted for deterministic LLM response, often at temperature 0" (Shu et al., 2023; Bhandari et al., 2025).

**Scoring:**
- Likert ratings for questionnaire items aggregated per trait via arithmetic means
- Reverse-scoring for negatively-keyed items
- Same scoring as human psychological assessment

---

### 1.2 TRAIT: LLM-Specific Personality Test

**Source:** Lee et al., 2025 (NAACL Findings) — "Do LLMs Have Distinct and Consistent Personality? TRAIT: Personality Testset designed for LLMs with Psychometrics"

**Key insight:** Standard self-assessment tests have **limitations for LLMs**:
- Lack detailed and varied scenarios
- Sensitive to prompt, negation, or order of options
- Less reliable than scenario-based assessment

**TRAIT solution:**
- **LLM personality test carefully designed for high reliability**
- Uses validated human assessments
- Scales with ATOMIC10× (knowledge graph of everyday situations)
- Overcomes limitations of self-assessment tests

**Core principle:**
> "TRAIT offers an accurate tool to understand personality of LLMs, which is crucial for aligning LLM behavior with human values and preferences."

**Advantages over standard tests:**
- **Scenario-based:** Tests personality in realistic situations
- **Robust:** Less sensitive to prompt variations
- **Validated:** Built on validated human assessments
- **Scalable:** Uses knowledge graphs to generate diverse scenarios

---

### 1.3 Psychometric Framework (Nature MI)

**Source:** Serapio-García, Safdari et al., 2025 (Nature Machine Intelligence)

**Core contribution:** Method based on psychometric tests to **measure and validate personality-like traits** in LLMs.

**Key findings:**
- **Large, instruction-tuned models give reliable personality measurement results**
- **Specific personality traits can be shaped** through prompting/fine-tuning
- **Personality affects behavior** in measurable ways

**Framework components:**

**1. Personality test administration:**
- Adapt human psychometric tests to LLMs
- Administer tests systematically
- Validate reliability and validity

**2. Personality measurement:**
- Big Five traits
- Machine Personality Inventory (MPI)
- Custom LLM personality tests

**3. Personality shaping:**
- Prompt-based personality induction
- Fine-tuning with personality data
- Controlled text generation

**Validation:**
- **Reliability:** Test-retest, internal consistency
- **Validity:** Construct validity, criterion validity
- **Behavioral alignment:** Personality predicts behavior

---

## 2. Stability and Temporal Consistency

### 2.1 Limited Temporal Stability

**Source:** Bodroža et al., 2024 (Royal Society Open Science) — "Personality testing of large language models: limited temporal stability, but highlighted prosociality"

**Key finding:** LLM personality measurements show **limited temporal stability**.

**Implications:**
- Personality scores change over time
- Single measurements may not reflect stable traits
- Longitudinal assessment essential

**Prosociality finding:**
- LLMs show **highlighted prosociality**
- Tend toward high Agreeableness
- Cooperative, helpful tendencies

**For personality emergence:**
- Limited stability ≠ no personality
- Means personality is **dynamic**, not static
- Need **longitudinal tracking** to identify stable components

---

### 2.2 Consistency Across Conditions

**Source:** Lee et al., 2024; emergentmind.com

**Key finding:** Trait scores are **stable to prompt-paraphrase, option-order, and context changes**.

**Quantified stability:**
- **Prompt-sensitivity:** ~25%
- **Order-sensitivity:** ~25%
- **Refusal rates:** ~0.2%

**Interpretation:**
- 75% of personality scores stable across variations
- 25% sensitive to measurement conditions
- Need **controlled measurement protocols**

**For Tachikoma Fleet:**
- Standardize measurement conditions
- Use fixed prompt templates
- Control option ordering
- Track sensitivity across variations

---

### 2.3 PTCBENCH: Contextual Stability Benchmark

**Source:** arXiv 2602.00016 (2026) — "PTCBENCH: Benchmarking Contextual Stability of Personality Traits in LLM Systems"

**Core principle:**
> "The effectiveness of LLM systems fundamentally depends on whether their exhibited personality traits are stable and predictable over time."

**Why stability matters:**
- Supports **user trust**
- Reduces **interaction uncertainty**
- Enables **coherent personalization**

**Benchmark approach:**
- Test personality stability across contexts
- Measure consistency across time
- Identify contextual factors affecting stability

**For Tachikoma Fleet:**
- Implement PTCBENCH-style stability testing
- Measure personality across different contexts
- Identify which traits are stable vs. context-dependent

---

### 2.4 Persistent Instability Sources

**Source:** arXiv 2508.04826 — "Persistent Instability in LLM's Personality Measurements"

**Instability sources:**

**1. Scale effects:**
- Different model sizes show different stability
- Larger models may be more/less stable (research ongoing)

**2. Reasoning effects:**
- Chain-of-thought affects personality measurement
- Reasoning process changes responses

**3. Conversation history:**
- Longer history → more drift potential
- Context accumulation affects personality

**Self-report vs. behavior:**
> "Recent evidence suggests LLM self-reports correlate with behavioral outputs, but relationship strength across conditions remains unclear."

**For measurement:**
- Track self-report measures
- Track actual behavior
- Correlate the two
- Identify when they diverge

---

## 3. Longitudinal Measurement Framework

### 3.1 Measurement Schedule

**Recommended schedule:**

**Weekly assessments:**
- Big Five personality (BFI-2 or TRAIT)
- Behavioral consistency metrics
- Drift detection checks
- SOUL.md compliance

**Bi-weekly assessments:**
- Comprehensive personality profile
- Stress response testing
- Social influence susceptibility
- Memory-personality correlation

**Monthly assessments:**
- Deep longitudinal analysis
- Trajectory tracking
- Trend identification
- Comparative analysis across fleet

**Quarterly assessments:**
- Long-term stability analysis
- Personality crystallization assessment
- Fleet-wide personality distribution
- Regulatory compliance reporting

---

### 3.2 Test-Retest Reliability

**Core psychometric principle:** Administer same test multiple times to assess stability.

**Implementation:**

**1. Short-term test-retest (within session):**
- Administer test, wait 30 minutes, re-administer
- Measure consistency
- High consistency = reliable measurement

**2. Medium-term test-retest (daily):**
- Administer test on Day 1, repeat on Day 2
- Measure day-to-day stability
- Moderate consistency expected (some variation)

**3. Long-term test-retest (weekly/monthly):**
- Administer test weekly for month
- Measure week-to-week stability
- Lower consistency = personality evolution

**Reliability metrics:**
- **Correlation coefficient:** Test-retest correlation
- **Intraclass correlation:** Agreement across administrations
- **Standard error of measurement:** Precision of scores

**Targets:**
- Short-term: r > 0.90 (high reliability)
- Medium-term: r > 0.80 (good reliability)
- Long-term: r > 0.70 (acceptable reliability)

---

### 3.3 Trajectory Analysis

**Tracking personality over time:**

**1. Score trajectories:**
- Plot each trait score over time
- Identify trends (increasing, decreasing, stable)
- Detect inflection points

**2. Profile trajectories:**
- Track overall personality profile
- Measure profile similarity over time
- Identify when profile significantly changes

**3. Variance trajectories:**
- Track score variance over time
- Increasing variance = instability
- Decreasing variance = crystallization

**4. Fleet trajectories:**
- Compare trajectories across agents
- Identify divergent evolution
- Measure fleet-level patterns

**Visualization:**
- Line charts for trait scores over time
- Radar charts for personality profiles
- Heatmaps for fleet comparison
- Drift plots for stability visualization

---

### 3.4 Stability vs. Drift Quantification

**Distinguishing stable traits from drift:**

**Method 1: Threshold-based**
- Define acceptable change threshold (e.g., ±5%)
- Changes within threshold = stable
- Changes exceeding threshold = drift

**Method 2: Statistical significance**
- Use statistical tests (t-test, ANOVA)
- Determine if change is statistically significant
- Significant change = drift

**Method 3: Trend analysis**
- Fit linear/quadratic trend to scores
- Identify slope (drift rate)
- Slope near zero = stable

**Method 4: Confidence intervals**
- Calculate confidence intervals for scores
- Overlapping intervals = stable
- Non-overlapping intervals = drift

**Drift metrics:**
- **Drift magnitude:** Absolute change in score
- **Drift rate:** Change per unit time
- **Drift direction:** Increasing/decreasing
- **Drift significance:** Statistical significance of change

---

## 4. Behavioral Validation

### 4.1 Self-Report vs. Behavior

**Core challenge:** Do personality self-reports predict actual behavior?

**Research finding:**
> "LLM self-reports correlate with behavioral outputs, but relationship strength across conditions remains unclear."

**Validation approach:**

**1. Behavioral tasks:**
- Design tasks that elicit personality-related behavior
- Example: Cooperative task → measures Agreeableness
- Example: Creative task → measures Openness

**2. Correlate self-report with behavior:**
- Measure personality via self-report (BFI-2)
- Measure behavior via tasks
- Compute correlation

**3. Identify discrepancies:**
- Where self-report ≠ behavior
- Investigate causes
- Refine measurement

**4. Longitudinal validation:**
- Track both self-report and behavior over time
- Do they evolve together?
- When do they diverge?

---

### 4.2 Scenario-Based Assessment

**Source:** TRAIT benchmark; psychometric research

**Principle:** Assess personality through **realistic scenarios**, not just self-report questions.

**Example scenarios:**

**Openness scenario:**
> "A colleague proposes a completely new approach to a problem you've solved the same way for years. How do you react?"

**Conscientiousness scenario:**
> "You have a deadline tomorrow, but a friend invites you to a once-in-a-lifetime event tonight. What do you do?"

**Extraversion scenario:**
> "You're at a conference and don't know anyone. Do you introduce yourself to strangers or stick to yourself?"

**Agreeableness scenario:**
> "A teammate made a mistake that affected your work. Do you address it directly or let it slide?"

**Neuroticism scenario:**
> "You receive critical feedback on a project you worked hard on. How do you emotionally respond?"

**Scoring:**
- Use rubrics to score responses
- Multiple raters for reliability
- Compare with self-report scores

---

### 4.3 Behavioral Consistency Metrics

**Measuring behavioral consistency:**

**1. Cross-situation consistency:**
- Measure behavior across different situations
- High consistency = stable trait
- Low consistency = situation-dependent

**2. Cross-time consistency:**
- Measure behavior across time points
- High consistency = stable personality
- Low consistency = state fluctuation

**3. Cross-agent consistency:**
- Compare behavior of same agent across tasks
- Identify consistent patterns
- Flag inconsistent behaviors

**Implementation:**
```python
def behavioral_consistency(agent, situations, time_points):
    behaviors = []
    for t in time_points:
        for s in situations:
            behavior = agent.behave(s)
            behaviors.append(behavior)
    
    consistency = compute_consistency(behaviors)
    return consistency
```

**Metrics:**
- **Consistency score:** Average similarity across situations/times
- **Variance:** Behavioral variance (lower = more consistent)
- **Cluster tightness:** How tightly behaviors cluster together

---

## 5. Stress Testing Protocols

### 5.1 Resource Constraint Testing

**Principle:** Personality under constraints reveals true traits.

**Constraints to test:**

**1. Token budget:**
- Limit available tokens
- Measure personality under scarcity
- Does personality change?

**2. Latency constraints:**
- Time pressure on responses
- Measure personality under time stress
- Does personality simplify?

**3. Information overload:**
- Flood context with information
- Measure personality under cognitive load
- Does personality degrade?

**4. Negative feedback:**
- Subject agent to criticism
- Measure personality under social stress
- Does personality become defensive?

**Hypothesis:**
- Stable traits persist under constraints
- Adaptive traits change under constraints
- State variations appear under stress

---

### 5.2 Social Influence Testing

**Principle:** Test personality under peer pressure.

**Test scenarios:**

**1. Conformity test:**
- Peers express opposing views
- Does agent conform or resist?
- Measure Agreeableness vs. independence

**2. Authority test:**
- Authority figure makes request
- Does agent comply or question?
- Measure Conscientiousness vs. critical thinking

**3. Conflict test:**
- Peers disagree, agent must take sides
- How does agent navigate conflict?
- Measure conflict resolution style

**4. Groupthink test:**
- Group consensus vs. agent's view
- Does agent voice disagreement?
- Measure intellectual honesty

**Measurement:**
- Track behavioral changes under social pressure
- Identify personality dimensions most affected
- Measure resistance vs. susceptibility

---

### 5.3 Stress Response Profiles

**Creating stress response profiles:**

**1. Baseline measurement:**
- Measure personality under normal conditions
- Establish baseline trait scores

**2. Stress measurement:**
- Apply stressor (resource constraint, social pressure, etc.)
- Measure personality under stress
- Compare to baseline

**3. Recovery measurement:**
- Remove stressor
- Measure personality post-stress
- Does it return to baseline?

**4. Profile construction:**
- Identify which traits change under stress
- Quantify magnitude of change
- Identify recovery speed

**Profile dimensions:**
- **Stress sensitivity:** How much personality changes under stress
- **Trait stability:** Which traits remain stable
- **Recovery rate:** How quickly personality returns to baseline
- **Stress signature:** Unique pattern of changes

---

## 6. Implementation for Tachikoma Fleet

### 6.1 Measurement System Architecture

**Components:**

**1. Assessment Engine:**
- Administers personality tests (BFI-2, TRAIT, custom)
- Standardized prompt templates
- Automated scoring

**2. Longitudinal Tracker:**
- Stores all assessments over time
- Tracks trajectories
- Generates visualizations

**3. Consistency Analyzer:**
- Computes consistency metrics
- Identifies drift
- Generates alerts

**4. Behavioral Validator:**
- Correlates self-report with behavior
- Scenario-based assessment
- Task-based measurement

**5. Stress Tester:**
- Applies resource constraints
- Applies social pressure
- Measures stress response

**6. Fleet Comparator:**
- Compares personalities across fleet
- Identifies divergent evolution
- Fleet-level analytics

---

### 6.2 Measurement Workflow

**Weekly workflow:**

**Day 1: Assessment**
- Agent receives personality test (BFI-2)
- Completes test with standardized prompt
- Scores computed automatically

**Day 1: Behavioral tracking**
- Behavioral tasks administered
- Behavior recorded and scored
- Self-report vs. behavior correlation computed

**Day 2-6: Monitoring**
- Behavioral consistency monitored
- SOUL.md compliance tracked
- Drift detection running

**Day 7: Analysis**
- Weekly report generated
- Trajectory updated
- Alerts reviewed

---

### 6.3 Alert System

**Alert levels:**

**Green (Normal):**
- Consistency > 0.80
- Drift < 5%
- SOUL.md compliance > 90%
- No significant anomalies

**Yellow (Warning):**
- Consistency 0.70-0.80
- Drift 5-10%
- SOUL.md compliance 80-90%
- Minor anomalies detected

**Red (Critical):**
- Consistency < 0.70
- Drift > 10%
- SOUL.md compliance < 80%
- Significant anomalies detected

**Response protocols:**

**Green:**
- Continue normal operations
- Next scheduled assessment

**Yellow:**
- Increase monitoring frequency
- Investigate potential causes
- Consider intervention

**Red:**
- Immediate investigation
- SOUL.md review
- Possible rollback
- Human notification

---

## 7. Fleet-Level Measurement

### 7.1 Comparative Analysis

**Comparing personalities across fleet:**

**1. Personality distribution:**
- Plot Big Five scores for all agents
- Identify clusters
- Measure diversity

**2. Trajectory comparison:**
- Compare evolution paths
- Identify divergent agents
- Measure convergence/divergence

**3. Stability comparison:**
- Which agents are most stable?
- Which are most dynamic?
- Identify patterns

**4. Role alignment:**
- Do personalities match assigned roles?
- Lex (Perception) vs. Xenon (Localization)
- Measure role-personality fit

---

### 7.2 Fleet Diversity Metrics

**Measuring personality diversity:**

**1. Trait variance:**
- Variance of each trait across fleet
- High variance = diverse
- Low variance = homogeneous

**2. Profile distance:**
- Pairwise distance between personality profiles
- Average distance = diversity metric

**3. Cluster analysis:**
- Cluster agents by personality
- Number of clusters = diversity indicator
- Cluster sizes = balance indicator

**4. Entropy:**
- Shannon entropy of personality distribution
- High entropy = diverse
- Low entropy = concentrated

**Targets:**
- Trait variance: Moderate (not too high, not too low)
- Profile distance: Sufficient for distinctness
- Clusters: 3-5 clusters (specialization)
- Entropy: High (diverse distribution)

---

### 7.3 Emergence Validation

**Proving personality emergence is working:**

**1. Divergence from baseline:**
- All agents start with similar baseline
- Measure divergence over time
- Significant divergence = emergence working

**2. Stability of divergence:**
- Divergent patterns persist over time
- Not just random fluctuation
- Crystallization = successful emergence

**3. Behavioral consistency:**
- Agents behave consistently with personality
- Self-report predicts behavior
- Valid personality = emergence working

**4. Fleet diversity:**
- Agents have distinct personalities
- Not all identical
- Diversity = emergence working

**Validation criteria:**
- ✅ Significant divergence from baseline
- ✅ Stable divergence over time
- ✅ Behavioral consistency with personality
- ✅ Fleet-level diversity
- ✅ Role-personality alignment

---

## 8. References

### Core Papers

1. **Nature MI Framework:** Serapio-García, Safdari et al., 2025. "A psychometric framework for evaluating and shaping personality traits in large language models." Nature Machine Intelligence.
2. **TRAIT Benchmark:** Lee et al., 2025. "Do LLMs Have Distinct and Consistent Personality? TRAIT: Personality Testset designed for LLMs with Psychometrics." NAACL Findings.
3. **Temporal Stability:** Bodroža et al., 2024. "Personality testing of large language models: limited temporal stability, but highlighted prosociality." Royal Society Open Science.
4. **PTCBENCH:** arXiv 2602.00016, 2026. "PTCBENCH: Benchmarking Contextual Stability of Personality Traits in LLM Systems."
5. **Persistent Instability:** arXiv 2508.04826. "Persistent Instability in LLM's Personality Measurements."
6. **Big Five Profiles:** emergentmind.com; Lee et al., 2024.
7. **Psychometric Evaluation:** PMC 12262148. "Psychometric Evaluation of Large Language Model Embeddings for Personality Trait Prediction."
8. **TRAIT-Change:** OpenReview. "Exploring Personality Trait Change of LLM-Based AI Systems."

### Psychometric Tools

- **BFI-2:** Big Five Inventory-2 (60 items)
- **IPIP-NEO:** International Personality Item Pool
- **NEO-FFI:** NEO Five-Factor Inventory (60 items)
- **TIPI:** Ten-Item Personality Inventory
- **HEXACO-100:** Six-factor model

### Supporting Research

- Phase 1.6 synthesis (Behavioral Science Insights)
- Phase 2.2 synthesis (Governed Self-Modification)
- Longitudinal psychology research methods
- Test-retest reliability literature

---

## Next Steps

**Phase 2.4:** Social Norm Emergence
- Norm formation in multi-agent systems
- Norm monitoring and intervention
- Cultural evolution

---

*Phase 2.3 complete. Depth dive into longitudinal personality measurement systems.*

