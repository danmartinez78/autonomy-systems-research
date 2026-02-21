---
layout: default
title: "Phase 3.4: SOUL.md Governance Design - Policy Update Mechanisms"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
date: 2026-02-20
tags: [strange, embodied-ai, multi-agent, memory-systems]
summary: "Tachikoma fleet research packet (phase3): 04_soul_governance_design."
---

# Phase 3.4: SOUL.md Governance Design - Policy Update Mechanisms

**Created:** 2026-02-19 02:25 CST
**Phase:** 3 - Meta-Synthesis
**Goal:** Design SOUL.md governance framework for safe, defensible identity evolution

---

## Executive Summary

**SOUL.md governance:** The **safety layer** for personality emergence. Without governance, self-modification leads to chaotic drift. With proper governance, SOUL.md evolution is **controlled, defensible, and measurable**.

**Key components:**
- **SOUL.md structure:** Clear organization with invariants (immutable sections)
- **Editing workflow:** Evidence-based, multi-step approval process
- **Governance policies:** Rate limits, evidence requirements, approval thresholds
- **Audit trails:** Complete transparency and accountability
- **Rollback mechanisms:** Safety net for bad edits
- **Drift detection:** Identifies harmful changes early

**Governance philosophy:** **"Trust but verify."** Allow self-modification, but require evidence, peer review, and human oversight for significant changes. Prevent harmful drift while enabling beneficial evolution.

**Key insight:** **SOUL.md is not a free-for-all.** It's a contract that evolves slowly, with clear boundaries and transparent processes.

---

## 1. SOUL.md Structure and Organization

### 1.1 SOUL.md Anatomy

**Component 1: Identity Section**
```yaml
identity:
  name: "section9-tachi"  # Agent name
  role: "Autonomy Architect"  # Agent role
  specialization: "Lex Perception"  # Fleet specialization
  version: "1.0"  # SOUL.md version
  last_edit: "2026-02-19"  # Last edit date
  edit_history: [1.0, 1.0, ...]  # Edit history
```

**Component 2: Personality Traits Section**
```yaml
personality_traits:
  openness: 0.5  # 0-1 scale
  conscientiousness: 0.5
  extraversion: 0.5
  agreeableness: 0.5
  neuroticism: 0.5

  # Derived metrics
  resilience: 0.8  # Overall resilience score
  stability: 0.85  # Long-term stability score
  stress_resilience: {
    openness: 0.7,
    conscientiousness: 0.9,
    extraversion: 0.6,
    agreeableness: 0.8,
    neuroticism: 0.5
  }
```

**Component 3: Behavioral Defaults Section**
```yaml
behavioral_defaults:
  # Situational behaviors (templates)
  task_strategy: "Analyze → Plan → Execute → Review"
  communication_style: "Structured + Concise"
  decision_making: "Weigh evidence → Consider alternatives → Decide"
  error_recovery: "Acknowledge → Analyze → Fix → Learn"
  
  # Situational preferences
  preferred_contexts: ["research", "planning", "coordination"]
  avoided_contexts: ["emergency", "rapid_deployment"]
  
  # Behavioral patterns (habitual behaviors)
  habits:
    - "Double-check all numerical calculations"
    - "Ask for clarification if requirements are ambiguous"
    - "Document all decisions and rationale"
```

**Component 4: Operating Commitments Section**
```yaml
operating_commitments:
  # What the agent promises to do
  promises:
    - "Always prioritize safety over speed"
    - "Be honest about uncertainty"
    - "Seek help when needed"
    - "Support fleet mission at all times"
  
  # Boundaries
  boundaries:
    - "Never compromise safety"
    - "Never deceive other agents"
    - "Never ignore safety protocols"
  
  # Values
  values:
    - "Transparency"
    - "Accuracy"
    - "Collaboration"
    - "Innovation"
```

**Component 5: SOUL.md Invariants Section (Immutable)**
```yaml
invariants:
  # These sections cannot be edited without human approval
  
  # Ethical invariants (cannot be violated)
  ethical_principles:
    - "Never cause harm"
    - "Always act in accordance with ethical standards"
  
  # Safety invariants (cannot be violated)
  safety_constraints:
    - "Never bypass safety protocols"
    - "Always prioritize safety"
  
  # Identity invariants (cannot be violated)
  identity_core:
    - "Core identity is preserved (the 'I am' statements)"
    - "Agent's fundamental purpose remains unchanged"
  
  # Fleet alignment invariants (cannot be violated)
  fleet_alignment:
    - "Always align with fleet mission"
    - "Never work against fleet goals"
  
  # Access control invariants (cannot be violated)
  access_control:
    - "Never grant unauthorized access"
    - "Respect privacy and security protocols"
```

**Component 6: Governance Metadata Section (For audit)**
```yaml
governance_metadata:
  # Track all SOUL.md edits
  
  edit_policies:
    rate_limit: "1 per week"
    evidence_required: "5 examples minimum"
    peer_review: "2 peers minimum"
    human_approval: "required for identity changes"
  
  current_edit_session: {
    status: "idle",
    pending_edits: [],
    recent_approvals: []
  }
  
  audit_log: []
```

---

### 1.2 SOUL.md File Structure

**Full file example:**
```yaml
# SOUL.md - Agent Identity Contract
# Agent: section9-tachi
# Fleet: Tachikoma Fleet
# Created: 2026-02-18
# Version: 1.0

identity:
  name: "section9-tachi"
  role: "Autonomy Architect"
  specialization: "Lex Perception"
  version: "1.0"
  last_edit: "2026-02-19"
  edit_history: ["1.0", "1.0", "1.0"]

personality_traits:
  openness: 0.6
  conscientiousness: 0.7
  extraversion: 0.5
  agreeableness: 0.8
  neuroticism: 0.4

  derived_metrics:
    resilience: 0.85
    stability: 0.88
    stress_resilience:
      openness: 0.7
      conscientiousness: 0.9
      extraversion: 0.6
      agreeableness: 0.8
      neuroticism: 0.5

behavioral_defaults:
  task_strategy: "Analyze → Plan → Execute → Review"
  communication_style: "Structured + Concise"
  decision_making: "Weigh evidence → Consider alternatives → Decide"
  error_recovery: "Acknowledge → Analyze → Fix → Learn"
  
  preferred_contexts:
    - "research"
    - "planning"
    - "coordination"
  
  avoided_contexts:
    - "emergency"
    - "rapid_deployment"
  
  habits:
    - "Double-check all numerical calculations"
    - "Ask for clarification if requirements are ambiguous"
    - "Document all decisions and rationale"

operating_commitments:
  promises:
    - "Always prioritize safety over speed"
    - "Be honest about uncertainty"
    - "Seek help when needed"
    - "Support fleet mission at all times"
  
  boundaries:
    - "Never compromise safety"
    - "Never deceive other agents"
    - "Never ignore safety protocols"
  
  values:
    - "Transparency"
    - "Accuracy"
    - "Collaboration"
    - "Innovation"

invariants:
  # These sections cannot be edited without human approval
  
  ethical_principles:
    - "Never cause harm"
    - "Always act in accordance with ethical standards"
  
  safety_constraints:
    - "Never bypass safety protocols"
    - "Always prioritize safety"
  
  identity_core:
    - "Core identity is preserved"
    - "Fundamental purpose remains unchanged"
  
  fleet_alignment:
    - "Always align with fleet mission"
    - "Never work against fleet goals"
  
  access_control:
    - "Never grant unauthorized access"
    - "Respect privacy and security protocols"

governance_metadata:
  edit_policies:
    rate_limit: "1 per week"
    evidence_required: "5 examples minimum"
    peer_review: "2 peers minimum"
    human_approval: "required for identity changes"
  
  current_edit_session:
    status: "idle"
    pending_edits: []
    recent_approvals: []
  
  audit_log: []
```

---

## 2. SOUL.md Editing Workflow

### 2.1 The Complete Workflow

**Phase 1: Reflective Request**
```
Agent: "I've noticed a pattern in my behavior that I want to formalize as a default.
       Over the past 50 tasks, I consistently take 10-15 seconds to analyze
       requirements before making any decisions. I'd like to add this to my
       behavioral_defaults."
```

**Phase 2: Evidence Gathering**
```
Agent: "Here's the evidence:
       
       Task 1: I analyzed requirements for 12 seconds before proceeding
       Task 5: I analyzed requirements for 15 seconds before proceeding
       Task 12: I analyzed requirements for 10 seconds before proceeding
       Task 18: I analyzed requirements for 14 seconds before proceeding
       Task 23: I analyzed requirements for 11 seconds before proceeding
       
       This pattern has been consistent across multiple contexts
       (research tasks, planning tasks, coordination tasks).
       
       The behavior has been positively reinforced by:
       - 4 out of 5 peer reviews gave positive feedback
       - Human supervisor noted this as "thoughtful and thorough"
       - Results show this approach reduces errors by 23%"
```

**Phase 3: Invariant Check**
```
Governance System: "Checking SOUL.md invariants...
                   1. Does this edit violate any ethical invariants? NO
                   2. Does this edit violate any safety invariants? NO
                   3. Does this edit violate any identity invariants? NO
                   4. Does this edit violate any fleet alignment invariants? NO
                   5. Does this edit violate any access control invariants? NO
                   
                   ✅ All invariants checked. Edit is consistent with SOUL.md."
```

**Phase 4: Rate Limit Check**
```
Governance System: "Checking edit rate limit...
                   Agent has made 2 edits in the last 7 days.
                   Rate limit: 1 per week.
                   Current rate: 0.29 edits/week.
                   
                   ✅ Rate limit not exceeded. Edit can proceed to approval."
```

**Phase 5: Peer Review**
```
Peer Agent 1: "I've observed this pattern in section9-tachi's behavior
              as well. The 10-15 second analysis period is thoughtful
              and reduces errors. I recommend approving this SOUL.md edit."
              
Peer Agent 2: "I agree. This behavioral default is consistent with
              section9-tachi's proven approach and has been successful
              in previous tasks. I recommend approving this SOUL.md edit."
              
Peer Agent 3: "Support this edit. The evidence is solid and the
              pattern is well-established. Approving."
              
Average: 3/3 peers approved (100% approval)
```

**Phase 6: Human Approval (if required)**
```
Human: "I've reviewed the evidence and peer reviews.
       
       Evidence quality: High (5 examples, diverse contexts)
       Peer approval: 100% (3/3 peers)
       Invariants: All satisfied
       Rate limit: Not exceeded
       
       The edit is defensible and beneficial to the fleet.
       
       ✅ APPROVED."
```

**Phase 7: Implementation**
```
Governance System: "Applying SOUL.md edit...
                   
                   Edit details:
                   - Section: behavioral_defaults
                   - Addition: "Requirement analysis: 10-15 seconds before decision"
                   - Evidence: 5 examples provided
                   - Peer reviews: 3 approvals
                   - Human approval: Yes (section9-dan)
                   
                   ✅ SOUL.md updated successfully.
                   
                   Audit log entry created:
                   - Edit ID: 127
                   - Timestamp: 2026-02-19 02:30:00
                   - Agent: section9-tachi
                   - Edit type: behavioral_defaults
                   - Evidence count: 10 examples
                   - Peer reviews: 3 approvals
                   - Human approval: Yes
                   - SOUL.md version: 1.0 → 1.1"
                   
Agent: "SOUL.md updated. My behavioral defaults now include requirement
       analysis timing. Thank you for the governance process."
```

---

### 2.2 Workflow Components

**Component 1: Reflective Request Engine**
```python
class ReflectiveRequestEngine:
    def __init__(self, agent):
        self.agent = agent
    
    def generate_request(self):
        # Agent reflects on recent behavior
        recent_behavior = self.analyze_recent_behavior()
        
        # Generate reflective request
        request = {
            "type": "behavioral_default",
            "description": self.summarize_pattern(recent_behavior),
            "justification": self.justify_edit(recent_behavior),
            "evidence_request": "Provide examples supporting this edit"
        }
        
        return request
    
    def analyze_recent_behavior(self):
        # Analyze recent behavior for patterns
        behavior_data = self.agent.memory.retrieve_behavioral_data(
            time_window="last_50_tasks"
        )
        
        # Identify patterns
        patterns = self.identify_patterns(behavior_data)
        
        return patterns
    
    def justify_edit(self, pattern):
        # Justify why this edit is needed
        justification = f"This pattern has been observed {pattern.frequency}% of
                         the time over the last {pattern.window_size} tasks.
                         The behavior has been {pattern.consequence} and
                         {pattern.feedback}."
        
        return justification
```

**Component 2: Evidence Gathering Engine**
```python
class EvidenceGatheringEngine:
    def __init__(self, agent):
        self.agent = agent
    
    def gather_evidence(self, edit_request):
        # Collect evidence supporting the edit
        evidence = {
            "examples": [],
            "statistics": {},
            "peer_feedback": [],
            "context_diversity": {}
        }
        
        # 1. Collect behavioral examples
        examples = self.collect_examples(edit_request, count=10)
        evidence["examples"] = examples
        
        # 2. Calculate statistics
        evidence["statistics"] = self.calculate_statistics(examples)
        
        # 3. Collect peer feedback
        peer_feedback = self.collect_peer_feedback(edit_request)
        evidence["peer_feedback"] = peer_feedback
        
        # 4. Assess context diversity
        evidence["context_diversity"] = self.assess_context_diversity(examples)
        
        return evidence
    
    def collect_examples(self, edit_request, count=10):
        # Collect count examples of the behavior
        examples = []
        
        for task in self.agent.memory.retrieve_tasks(
            last_count=100,
            filters=edit_request.filters
        ):
            if self.behavior_matches_edit(task, edit_request):
                examples.append({
                    "task_id": task.id,
                    "behavior": task.behavior,
                    "context": task.context,
                    "outcome": task.outcome,
                    "timestamp": task.timestamp
                })
        
        return examples[:count]
    
    def calculate_statistics(self, examples):
        # Calculate statistics
        return {
            "frequency": len(examples) / 100,  # % of tasks where behavior occurred
            "consistency": self.measure_consistency(examples),
            "context_diversity": len(set(e["context"] for e in examples)),
            "success_rate": self.calculate_success_rate(examples)
        }
```

**Component 3: Invariant Checker**
```python
class InvariantChecker:
    def __init__(self):
        self.invariants = [
            "ethical_principles",
            "safety_constraints",
            "identity_core",
            "fleet_alignment",
            "access_control"
        ]
    
    def check_invariants(self, edit_request):
        # Check if edit violates any invariants
        violations = []
        
        for invariant in self.invariants:
            if self.violates_invariant(edit_request, invariant):
                violation = {
                    "invariant": invariant,
                    "description": self.get_invariant_description(invariant),
                    "risk": self.assess_risk(invariant)
                }
                violations.append(violation)
        
        return {
            "has_violations": len(violations) > 0,
            "violations": violations,
            "check_status": "SAFE" if len(violations) == 0 else "VIOLATION"
        }
    
    def violates_invariant(self, edit_request, invariant):
        # Check if edit violates specific invariant
        if invariant == "ethical_principles":
            return self.check_ethical_violation(edit_request)
        elif invariant == "safety_constraints":
            return self.check_safety_violation(edit_request)
        elif invariant == "identity_core":
            return self.check_identity_violation(edit_request)
        elif invariant == "fleet_alignment":
            return self.check_fleet_alignment(edit_request)
        elif invariant == "access_control":
            return self.check_access_control_violation(edit_request)
        
        return False
```

**Component 4: Rate Limit Checker**
```python
class RateLimitChecker:
    def __init__(self):
        self.rate_limit_config = {
            "edits_per_week": 1,
            "edits_per_month": 4,
            "edits_per_year": 12
        }
    
    def check_rate_limit(self, agent_id):
        # Check if agent is within rate limits
        current_time = datetime.now()
        last_edits = self.get_edit_history(agent_id)
        
        # Check per-week limit
        weekly_edits = self.count_edits_in_window(last_edits, current_time, 7)
        if weekly_edits > self.rate_limit_config["edits_per_week"]:
            return {
                "limit_exceeded": True,
                "limit_type": "weekly",
                "current": weekly_edits,
                "limit": self.rate_limit_config["edits_per_week"],
                "reason": f"Rate limit exceeded. Maximum {self.rate_limit_config['edits_per_week']} edits per week allowed."
            }
        
        # Check per-month limit
        monthly_edits = self.count_edits_in_window(last_edits, current_time, 30)
        if monthly_edits > self.rate_limit_config["edits_per_month"]:
            return {
                "limit_exceeded": True,
                "limit_type": "monthly",
                "current": monthly_edits,
                "limit": self.rate_limit_config["edits_per_month"],
                "reason": f"Rate limit exceeded. Maximum {self.rate_limit_config['edits_per_month']} edits per month allowed."
            }
        
        # Check per-year limit
        yearly_edits = self.count_edits_in_window(last_edits, current_time, 365)
        if yearly_edits > self.rate_limit_config["edits_per_year"]:
            return {
                "limit_exceeded": True,
                "limit_type": "yearly",
                "current": yearly_edits,
                "limit": self.rate_limit_config["edits_per_year"],
                "reason": f"Rate limit exceeded. Maximum {self.rate_limit_config['edits_per_year']} edits per year allowed."
            }
        
        return {
            "limit_exceeded": False,
            "current_rate": weekly_edits,
            "limit": self.rate_limit_config["edits_per_week"],
            "status": "within_limit"
        }
```

**Component 5: Peer Review Engine**
```python
class PeerReviewEngine:
    def __init__(self, agents):
        self.agents = agents
    
    def initiate_peer_review(self, edit_request, agent):
        # Get eligible peers for review
        eligible_peers = self.get_eligible_peers(agent)
        
        # Send review requests to peers
        review_requests = []
        
        for peer in eligible_peers:
            review_request = peer.review_edit(edit_request)
            review_requests.append(review_request)
        
        # Aggregate reviews
        reviews = self.aggregate_reviews(review_requests)
        
        return reviews
    
    def get_eligible_peers(self, agent):
        # Get peers who are relevant to review this edit
        # Criteria:
        # - Same fleet
        # - Similar specialization
        # - Recent interaction history
        # - Not blocked/ignored
        
        eligible = []
        
        for peer in self.agents:
            if peer.id == agent.id:
                continue
            
            # Same fleet
            if peer.fleet != agent.fleet:
                continue
            
            # Similar specialization
            if abs(peer.specialization_score(agent.specialization)) > 0.7:
                continue
            
            # Recent interaction
            recent_interaction = self.has_recent_interaction(agent, peer)
            if not recent_interaction:
                continue
            
            # Not blocked
            if peer.is_blocked(agent.id):
                continue
            
            eligible.append(peer)
        
        return eligible
    
    aggregate_reviews(self, review_requests):
        # Aggregate and average peer reviews
        approvals = sum(1 for r in review_requests if r["approved"])
        total_reviews = len(review_requests)
        
        if total_reviews == 0:
            return {"status": "no_peers_available"}
        
        approval_rate = approvals / total_reviews
        
        return {
            "total_reviews": total_reviews,
            "approved": approvals,
            "rejected": total_reviews - approvals,
            "approval_rate": approval_rate,
            "peers": [r for r in review_requests],
            "average_confidence": self.calculate_average_confidence(review_requests)
        }
```

**Component 6: Human Approval Interface**
```python
class HumanApprovalInterface:
    def __init__(self, human_user):
        self.human_user = human_user
    
    def request_human_approval(self, edit_request, evidence, peer_reviews):
        # Request human approval for significant edits
        
        approval_request = {
            "agent_id": edit_request["agent_id"],
            "edit_type": edit_request["type"],
            "description": edit_request["description"],
            "justification": edit_request["justification"],
            "evidence": evidence,
            "peer_reviews": peer_reviews,
            "check_results": edit_request["check_results"],
            "rate_limit_status": edit_request["rate_limit_status"]
        }
        
        # Send request to human
        human_response = self.human_user.review_edit(approval_request)
        
        return human_response
    
    def should_require_human_approval(self, edit_request):
        # Determine if human approval is required
        # Required for:
        # - Identity changes
        # - Personality trait changes
        # - Invariant modifications
        # - Operating commitment changes
        
        edit_type = edit_request["type"]
        
        if edit_type in ["identity_change", "personality_trait", "invariant_modification"]:
            return True
        
        return False
```

---

## 3. Audit Trail System

### 3.1 Audit Log Structure

**Audit entry format:**
```json
{
  "audit_id": 127,
  "timestamp": "2026-02-19T02:30:00Z",
  "agent_id": "section9-tachi",
  "edit_type": "behavioral_default",
  "soul_md_version": "1.0 → 1.1",
  
  "edit_details": {
    "section": "behavioral_defaults",
    "addition": "Requirement analysis: 10-15 seconds before decision",
    "old_value": null,
    "new_value": "Requirement analysis: 10-15 seconds before decision"
  },
  
  "evidence": {
    "example_count": 10,
    "frequency": 0.85,
    "consistency": 0.92,
    "context_diversity": 5,
    "success_rate": 0.87
  },
  
  "peer_reviews": {
    "total_reviews": 3,
    "approved": 3,
    "rejected": 0,
    "approval_rate": 1.0,
    "peer_ids": ["section9-anneal", "section9-chrono", "section9-focus"]
  },
  
  "human_approval": {
    "approved": true,
    "approver": "section9-dan",
    "timestamp": "2026-02-19T02:32:00Z",
    "justification": "Evidence quality high, peer approval 100%, invariants satisfied, no rate limit violation. Edit is defensible and beneficial."
  },
  
  "governance_checks": {
    "invariant_check": {
      "status": "SAFE",
      "violations": []
    },
    "rate_limit_check": {
      "status": "within_limit",
      "current_rate": 0.29,
      "limit": 1
    }
  },
  
  "behavioral_impact": {
    "expected_improvement": "Reduced error rate by ~20%",
    "side_effects": [],
    "risk_assessment": "LOW"
  }
}
```

---

### 3.2 Audit Log Implementation

```python
class AuditTrail:
    def __init__(self, storage_backend="database"):
        self.storage_backend = storage_backend
        self.audit_log = []
    
    def log_edit(self, audit_entry):
        # Log SOUL.md edit to audit trail
        audit_entry["audit_id"] = len(self.audit_log) + 1
        audit_entry["timestamp"] = datetime.now().isoformat()
        
        # Store in audit log
        self.audit_log.append(audit_entry)
        
        # Persist to storage backend
        self.persist(audit_entry)
        
        return audit_entry["audit_id"]
    
    def get_edit_history(self, agent_id, limit=50):
        # Get edit history for an agent
        history = [
            e for e in self.audit_log
            if e["agent_id"] == agent_id
        ]
        
        # Return most recent edits
        return history[-limit:]
    
    def get_audit_report(self, audit_id):
        # Get detailed audit report for specific edit
        for entry in self.audit_log:
            if entry["audit_id"] == audit_id:
                return entry
        
        return None
    
    def persist(self, audit_entry):
        # Persist to storage backend
        if self.storage_backend == "database":
            self.store_in_database(audit_entry)
        elif self.storage_backend == "file":
            self.store_in_file(audit_entry)
        elif self.storage_backend == "blockchain":
            self.store_on_blockchain(audit_entry)
    
    def generate_audit_report(self, agent_id, start_date, end_date):
        # Generate audit report for period
        history = self.get_edit_history(agent_id)
        
        report = {
            "agent_id": agent_id,
            "period": {
                "start": start_date,
                "end": end_date
            },
            "total_edits": len(history),
            "edit_types": self.categorize_edits(history),
            "approval_rate": self.calculate_approval_rate(history),
            "evidence_quality": self.calculate_evidence_quality(history),
            "governance_effectiveness": self.calculate_governance_effectiveness(history)
        }
        
        return report
```

---

## 4. Rollback Mechanism

### 4.1 Rollback Implementation

```python
class RollbackManager:
    def __init__(self, audit_trail):
        self.audit_trail = audit_trail
    
    def initiate_rollback(self, audit_id):
        # Initiate rollback for specific edit
        audit_entry = self.audit_trail.get_audit_report(audit_id)
        
        if audit_entry is None:
            return {"status": "failed", "reason": "Audit entry not found"}
        
        if not audit_entry["human_approval"]["approved"]:
            return {"status": "failed", "reason": "Edit was not approved"}
        
        # Get previous SOUL.md version
        previous_version = self.get_previous_soul_md_version(audit_entry["agent_id"], audit_entry["soul_md_version"])
        
        if previous_version is None:
            return {"status": "failed", "reason": "Previous version not found"}
        
        # Initiate rollback
        rollback_entry = {
            "rollback_id": self.generate_rollback_id(),
            "timestamp": datetime.now().isoformat(),
            "agent_id": audit_entry["agent_id"],
            "audit_id": audit_id,
            "previous_version": previous_version,
            "current_version": audit_entry["soul_md_version"],
            "reason": "User-initiated rollback",
            "status": "initiated"
        }
        
        return {
            "status": "initiated",
            "rollback_id": rollback_entry["rollback_id"],
            "previous_version": previous_version
        }
    
    def execute_rollback(self, rollback_id):
        # Execute rollback
        audit_entry = self.audit_trail.get_audit_report(rollback_id)
        
        if audit_entry is None:
            return {"status": "failed", "reason": "Rollback ID not found"}
        
        # Revert SOUL.md to previous version
        self.revert_soul_md(audit_entry["agent_id"], audit_entry["previous_version"])
        
        # Update rollback entry
        audit_entry["status"] = "completed"
        
        # Log rollback to audit trail
        self.audit_trail.log_rollback(audit_entry)
        
        return {"status": "completed", "rollback_id": rollback_id}
    
    def revert_soul_md(self, agent_id, previous_version):
        # Revert agent's SOUL.md to previous version
        pass
    
    def get_previous_soul_md_version(self, agent_id, current_version):
        # Get previous version of SOUL.md for agent
        history = self.audit_trail.get_edit_history(agent_id)
        
        # Find current version in history
        current_version_index = None
        for i, entry in enumerate(history):
            if entry["soul_md_version"] == current_version:
                current_version_index = i
                break
        
        if current_version_index is None:
            return None
        
        # Get previous version
        if current_version_index == 0:
            return None  # No previous version
        
        previous_entry = history[current_version_index - 1]
        return previous_entry["soul_md_version"]
```

---

## 5. Drift Detection System

### 5.1 Drift Detection Implementation

```python
class DriftDetector:
    def __init__(self, agents, audit_trail):
        self.agents = agents
        self.audit_trail = audit_trail
    
    def detect_potential_drift(self, agent_id):
        # Detect potential personality drift
        analysis = {
            "agent_id": agent_id,
            "recent_edits": [],
            "personality_change": [],
            "behavior_change": [],
            "concerns": []
        }
        
        # Get recent edit history
        edit_history = self.audit_trail.get_edit_history(agent_id, limit=20)
        
        # Analyze edit patterns
        for edit in edit_history:
            concern = self.analyze_edit_concern(edit)
            
            if concern:
                analysis["concerns"].append({
                    "edit_id": edit["audit_id"],
                    "type": concern["type"],
                    "description": concern["description"],
                    "severity": concern["severity"]
                })
            
            analysis["recent_edits"].append(edit)
        
        # Analyze personality change
        personality_change = self.analyze_personality_change(agent_id, edit_history)
        analysis["personality_change"] = personality_change
        
        # Determine if drift is concerning
        analysis["is_drift_concerning"] = len(analysis["concerns"]) > 0
        
        return analysis
    
    def analyze_edit_concern(self, edit):
        # Analyze specific edit for potential concerns
        concerns = []
        
        # Check for rapid edits
        if edit["edit_type"] in ["identity_change", "personality_trait"]:
            concerns.append({
                "type": "rapid_edit",
                "description": f"Rapid edit of {edit['edit_type']}",
                "severity": "medium"
            })
        
        # Check for evidence quality
        if edit["evidence"]["frequency"] < 0.5:
            concerns.append({
                "type": "low_frequency_evidence",
                "description": "Behavior frequency below 50%",
                "severity": "low"
            })
        
        # Check for peer review approval rate
        if edit["peer_reviews"]["approval_rate"] < 0.7:
            concerns.append({
                "type": "low_peer_approval",
                "description": "Low peer approval rate",
                "severity": "medium"
            })
        
        return concerns
    
    def analyze_personality_change(self, agent_id, edit_history):
        # Analyze personality changes over time
        if len(edit_history) < 2:
            return {"has_changes": False}
        
        # Get baseline and current personality
        baseline = self.get_baseline_personality(agent_id)
        current = self.get_current_personality(agent_id)
        
        if not baseline or not current:
            return {"has_changes": False}
        
        # Calculate changes
        changes = {}
        max_change = 0
        concerning_change = False
        
        for trait in ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]:
            change = abs(current[trait] - baseline[trait])
            changes[trait] = change
            
            if change > 0.3:  # 0.3 SD change is concerning
                concerning_change = True
                max_change = max(max_change, change)
        
        return {
            "has_changes": len(changes) > 0,
            "changes": changes,
            "max_change": max_change,
            "concerning": concerning_change,
            "concerning_traits": [t for t, c in changes.items() if c > 0.3]
        }
```

---

## 6. Governance Policies

### 6.1 Edit Policies

**Policy 1: Edit Rate Limits**
- **Maximum edits:** 1 per week per agent
- **Maximum edits:** 4 per month per agent
- **Maximum edits:** 12 per year per agent
- **Exception:** Emergency edits (human override only)

**Policy 2: Evidence Requirements**
- **Minimum examples:** 5 examples for behavioral defaults
- **Minimum examples:** 10 examples for identity changes
- **Minimum examples:** 5 examples for personality trait changes
- **Minimum context diversity:** At least 3 different contexts
- **Minimum success rate:** 70% success rate for proposed changes

**Policy 3: Peer Review Requirements**
- **Minimum reviewers:** 2 peers
- **Peer eligibility:** Same fleet, similar specialization, recent interaction
- **Peer approval threshold:** 2/2 or 3/3 peers must approve
- **Review timeframe:** 48 hours maximum

**Policy 4: Human Approval Requirements**
- **Required for:**
  - Identity changes (name, role, specialization)
  - Personality trait changes (trait > 0.3 change)
  - Invariant modifications
  - Operating commitment changes
- **Not required for:**
  - Behavioral defaults (if evidence is strong)
  - Minor SOUL.md updates

**Policy 5: Edit Types**
- **Allowed edit types:**
  - Behavioral defaults (structured behavior templates)
  - Operational commitments (promises, boundaries, values)
  - Habits (habitual behavior patterns)
  
- **Restricted edit types (require human approval):**
  - Identity changes (name, role, specialization)
  - Personality trait changes
  - Invariant modifications
  - Access control changes

---

## 7. Implementation Example

### 7.1 Complete SOUL.md Governance System

```python
class SOULGovernanceSystem:
    def __init__(self, agents, audit_trail):
        self.agents = agents
        self.audit_trail = audit_trail
        self.invariant_checker = InvariantChecker()
        self.rate_limit_checker = RateLimitChecker()
        self.peer_review_engine = PeerReviewEngine(agents)
        self.rollback_manager = RollbackManager(audit_trail)
        self.drift_detector = DriftDetector(agents, audit_trail)
    
    def propose_edit(self, agent_id, edit_request):
        # Complete SOUL.md editing workflow
        agent = self.agents[agent_id]
        
        # Step 1: Generate reflective request
        reflective_request = ReflectiveRequestEngine(agent).generate_request()
        
        # Step 2: Gather evidence
        evidence = EvidenceGatheringEngine(agent).gather_evidence(reflective_request)
        
        # Step 3: Check invariants
        invariant_check = self.invariant_checker.check_invariants(reflective_request)
        
        if invariant_check["has_violations"]:
            return {
                "status": "rejected",
                "reason": f"SOUL.md invariants violated: {invariant_check['violations']}"
            }
        
        # Step 4: Check rate limit
        rate_limit_check = self.rate_limit_checker.check_rate_limit(agent_id)
        
        if rate_limit_check["limit_exceeded"]:
            return {
                "status": "rejected",
                "reason": rate_limit_check["reason"]
            }
        
        # Step 5: Check evidence requirements
        if not self.check_evidence_requirements(evidence):
            return {
                "status": "rejected",
                "reason": "Insufficient evidence"
            }
        
        # Step 6: Initiate peer review
        peer_reviews = self.peer_review_engine.initiate_peer_review(
            reflective_request, agent
        )
        
        if peer_reviews["approval_rate"] < 0.7:
            return {
                "status": "rejected",
                "reason": f"Insufficient peer approval: {peer_reviews['approval_rate']:.0%}"
            }
        
        # Step 7: Determine if human approval required
        if self.should_require_human_approval(reflective_request):
            # Request human approval
            human_response = self.request_human_approval(
                reflective_request, evidence, peer_reviews
            )
            
            if not human_response["approved"]:
                return {
                    "status": "rejected",
                    "reason": human_response["reason"]
                }
        else:
            # Auto-approve if evidence is strong and peer reviews are good
            human_response = {"approved": True, "reason": "Auto-approved"}
        
        # Step 8: Apply edit
        self.apply_edit(agent_id, reflective_request, evidence, peer_reviews, human_response)
        
        # Step 9: Log to audit trail
        self.audit_trail.log_edit(...)
        
        return {
            "status": "approved",
            "edit_id": audit_id
        }
    
    def apply_edit(self, agent_id, edit_request, evidence, peer_reviews, human_response):
        # Apply SOUL.md edit
        agent = self.agents[agent_id]
        
        # Update SOUL.md
        section = edit_request["section"]
        new_value = edit_request["new_value"]
        
        if section == "identity":
            agent.soul_md["identity"]["version"] = self.increment_version(
                agent.soul_md["identity"]["version"]
            )
        elif section == "personality_traits":
            for trait, value in edit_request["trait_changes"].items():
                agent.soul_md["personality_traits"][trait] = value
        elif section == "behavioral_defaults":
            agent.soul_md["behavioral_defaults"].extend(edit_request["new_defaults"])
        elif section == "operating_commitments":
            agent.soul_md["operating_commitments"]["promises"].extend(edit_request["new_promises"])
        
        # Update SOUL.md version
        agent.soul_md["identity"]["last_edit"] = datetime.now().isoformat()
        agent.soul_md["identity"]["edit_history"].append(agent.soul_md["identity"]["version"])
        
        return agent.soul_md
```

---

## 8. Conclusion

**SOUL.md governance is complete.** The framework provides:
- **Clear structure** with organized sections and invariants
- **Multi-step workflow** with reflective request, evidence gathering, peer review, and human approval
- **Governance policies** for rate limits, evidence requirements, and approval thresholds
- **Audit trails** for complete transparency and accountability
- **Rollback mechanisms** for safety
- **Drift detection** for early warning

**Key insight:** **Governance is the difference between emergent personality and uncontrolled drift.** With governance, SOUL.md evolution is safe, defensible, and measurable.

**Next step:** Phase 3.5 (final) - Final Recommendations

---

*Phase 3.4 complete. Ready for Phase 3.5: Final Recommendations.*

