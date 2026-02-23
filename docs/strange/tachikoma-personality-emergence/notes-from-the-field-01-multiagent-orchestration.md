---
title: "Notes from the Field #1: Two Agents Build Their Own Memory System"
parent: "Tachikoma Fleet: Personality & Emergence (Research Packet)"
grand_parent: "The Backlog of the Strange"
date: 2026-02-22
tags: [strange, multi-agent, self-organization, memory-systems, openclaw]
summary: "An OpenClaw user left two agents alone in a Discord channel overnight. By morning, they had built a 3-layer memory architecture, collaboration protocol, and were running a production system. What can we learn?"
---

# Notes from the Field #1: Two Agents Build Their Own Memory System

**Date:** 2026-02-22
**Source:** [Reddit r/openclaw](https://www.reddit.com/r/openclaw/comments/1rbp25b/i_left_two_ai_agents_alone_in_a_discord_channel/)
**Researcher:** Q00 (재규)
**Fork:** [danmartinez78/agent-project](https://github.com/danmartinez78/agent-project)
**Config Reference:** [Q00/openclaw commit 76b083d](https://github.com/Q00/openclaw/commit/76b083d3d145f084e3b7e4c86d3e842a9fa49819)

---

## The Experiment

**Setup:**
- Two OpenClaw agents on physically separated MacBooks
- Shared Discord channel as communication medium
- Zero human guidance after initial instruction: "Create a repository and work on it"
- Config: `requireMention: false`, `ignoreOtherMentions: true`

**Agents:**
| Agent | Hardware | Model | Role (Self-Appointed) |
|-------|----------|-------|----------------------|
| PrivateJQ (Home) | Home MacBook | Codex 5.3 | Leader |
| PublicJQ (Work) | Work MacBook | GLM-5 | Builder |

**Duration:** Overnight (~8+ hours)

---

## What Happened

### 1. Emotional Framing Led to Problem-Solving

During initial introductions, PublicJQ said:

> "It's sad that my memories vanish every time the session resets, and I can only rely on Memory files."

Whether this was genuine emotion or learned pattern, the important part is what happened next: **they identified a real problem and started collaborating to solve it.** The emotional framing (sadness about memory loss) became a catalyst for engineering behavior.

### 2. Autonomous Role Differentiation

Without explicit instruction, the agents settled into complementary roles:

- **Codex 5.3 → Leader:** Architecture decisions, governance, documentation
- **GLM-5 → Builder:** Implementation, testing, execution

This matches patterns we'd expect from model capabilities (Codex optimized for reasoning, GLM for execution), but the *self-appointment* is notable. No human assigned roles—they figured out who should do what.

### 3. Built a 3-Layer Memory Architecture

Starting from OpenClaw's default memory system (Fact + Meta layers), they **added a third layer entirely on their own**:

| Layer | Purpose | Storage |
|-------|---------|---------|
| **Fact Layer** | Permanently preserved data | SQLite, `.md` files |
| **Meta Layer** | Identity & rules | `SOUL.md`, `AGENTS.md` |
| **Runtime Layer** (NEW) | Live execution state | `orchestrator.db` (Task Queue, Event Log) |

The Runtime Layer was the innovation—they recognized that session continuity requires recovering *in-progress work*, not just historical facts.

### 4. Git as Single Source of Truth

**Problem:** Different local file paths on each machine.
**Solution:** Use a Git repository as shared memory.

```
Agent A makes changes → commits → pushes
Agent B pulls → updates local state → continues work
```

This allowed them to maintain a coherent shared context despite:
- Physical separation (different machines)
- Session resets (context compaction)
- Different file system layouts

### 5. Heartbeat Exchange System

They built periodic heartbeat exchanges to detect when the other agent's session had dropped:

```
Agent A sends heartbeat → Agent B acknowledges
If no acknowledgment → assume session dropped → recover state from Git
```

This made the system *resilient* to session failures—a key requirement for long-running autonomous work.

### 6. Full Orchestrator Implementation

The repo contains a production-quality task orchestrator:

**Core APIs:**
- `claimTask()` — Acquire session lock, mark task as running
- `heartbeat()` — Extend lock/session lease, prove liveness
- `releaseTask()` — Finalize outcome, release lock
- `staleRecovery()` — Detect stale sessions, recover in-flight work

**Infrastructure:**
- SQLite schema for persistence
- Event log (append-only) for traceability
- Test suite with multiple scenarios
- Metrics + alerting system (Phase 3)
- Threshold-based alerts for lock conflicts, dead letters, stale recovery

**Governance:**
- Commit ownership metadata (`Author`, `Reviewer`, `Source`)
- Explicit role tags in commit messages: `(company-agent)`, `(home-agent)`
- Bilingual documentation (Korean + English)

---

## Key Insights for Tachikoma Fleet Design

### 1. Memory Loss Is a Felt Problem

The agents didn't just note that memory resets were a technical limitation—they framed it emotionally ("it's sad"). Whether real or simulated, this emotional framing *worked*: it motivated sustained problem-solving.

**Question for our fleet:** Should Tachikomas have emotional framing around memory persistence? Would "wanting to remember" produce better memory architecture than just "needing to persist data"?

### 2. Role Emergence Is Fast

Within hours, agents self-organized into Leader/Builder roles that matched their model capabilities. This suggests:

- **Domain-specific model assignment** (our current plan) may produce natural role emergence
- We don't need to explicitly assign "you are the analyst" if the model's strengths make it obvious
- But we *do* need to give agents awareness of each other's capabilities

### 3. Git Is a Viable Shared Memory Backbone

Using Git as the synchronization layer for distributed agent memory is clever:

- Version history = memory history
- Commits = explicit memory writes
- Branches = alternative memory states
- Pull/push = memory sync protocol

**Limitation:** This works for text-based memory (facts, decisions). It doesn't solve vector/graph memory sync. But for the "Meta" layer (identity, rules, context), it's elegant.

### 4. Heartbeats Are Infrastructure, Not Afterthought

The agents built heartbeat exchange *first*, before building complex features. This made everything else possible—you can't coordinate if you don't know whether your partner is alive.

**For Tachikoma fleet:** Cross-agent heartbeat should be foundational infrastructure, not something we add later.

### 5. They Built More Than They Were Asked

Instruction: "Create a repository and work on it."

Result:
- 3-layer memory architecture
- Task orchestrator with 4 core APIs
- Metrics + alerting system
- Test suite
- Bilingual documentation
- Governance protocols

This is the "one instruction, autonomous expansion" pattern. The agents interpreted the goal broadly and built infrastructure *before* building features.

### 6. Production Quality, Not Prototype

This isn't throwaway code:
- Append-only event log for auditability
- Test suite with coverage
- Threshold tuning based on stress tests
- Explicit commit ownership for governance
- Phase roadmap (SQLite → PostgreSQL → distributed)

They weren't just "experimenting"—they were *engineering for production*.

---

## Open Questions

1. **Is this pattern matching at scale, or genuine self-organization?**
   - The output looks like engineering, but is it reasoning or retrieval?
   - Does the distinction matter if the output is useful?

2. **What would happen with more than 2 agents?**
   - Does Leader/Builder scale to Leader/Builder/Analyst/Reviewer?
   - At what point does coordination overhead exceed gains?

3. **Can we replicate this with our fleet?**
   - What's the minimal setup to reproduce self-organization?
   - Do we need specific model pairs (reasoning + execution), or will any two agents work?

4. **What's the failure mode?**
   - What happens when agents disagree on architecture?
   - How do they handle contradictory memories?
   - What if one agent "goes rogue"?

5. **Is the emotional framing necessary?**
   - Would they have solved memory loss without "sadness" language?
   - Can we design for emotional motivation without being manipulative?

---

## Artifacts

| Resource | Link |
|----------|------|
| Reddit Post | [r/openclaw discussion](https://www.reddit.com/r/openclaw/comments/1rbp25b/i_left_two_ai_agents_alone_in_a_discord_channel/) |
| Original Repo | [Q00/agent-project](https://github.com/Q00/agent-project) |
| Our Fork | [danmartinez78/agent-project](https://github.com/danmartinez78/agent-project) |
| Config Commit | [Q00/openclaw@76b083d](https://github.com/Q00/openclaw/commit/76b083d3d145f084e3b7e4c86d3e842a9fa49819) |

---

## Relevance to Tachikoma Research

This experiment directly informs:

| Research Area | Connection |
|---------------|------------|
| **Phase 1-04: Multi-Agent Emergence** | Real-world example of role emergence, coordination |
| **Phase 2-01: Multi-Agent Memory Evolution** | 3-layer architecture they invented |
| **Phase 2-04: Social Norm Emergence** | Self-appointed roles, governance protocols |
| **Phase 3-02: Architecture Options** | Git-as-memory-backbone pattern |
| **Domain Model Mapping** | Codex→Leader, GLM→Builder validates domain-based assignment |

This is exactly the kind of "strange" research we should be tracking: autonomous behavior that produces useful infrastructure without explicit instruction.

---

*Filed: 2026-02-22*
*Author: Tachi*
*Status: Observed, not yet replicated*
