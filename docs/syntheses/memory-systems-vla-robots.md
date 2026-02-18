---
title: "Memory Systems for Autonomous Robots with VLA Architectures"
last_updated: 2026-02-18
tags: [robotics, vla, memory-systems, semantic-memory, knowledge-graphs, embodied-ai]
summary: "A synthesis of memory architectures for Vision-Language-Action models and autonomous robotic systems, covering working, episodic, semantic, and procedural memory approaches."
---

# Synthesis: Memory Systems for Autonomous Robots with VLA Architectures

## Problem Statement

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for robotic control, enabling robots to leverage web-scale visual and linguistic knowledge for manipulation and navigation tasks. However, current VLA architectures face a fundamental limitation: **they typically operate on the current observation alone**, struggling with:

- **Long-horizon tasks** requiring temporal reasoning across many steps
- **Non-Markovian dependencies** where past actions influence current decisions
- **Multi-episode understanding** across days, weeks, or months of operation
- **Experience reuse** from prior deployments to new situations

This synthesis examines how memory systems—inspired by cognitive science and neuroscience—can address these limitations in VLA-based autonomous robots.

**Context**: Critical for embodied AI systems that must operate persistently in real environments, accumulate knowledge over time, and adapt to changing conditions.

**Scope**: Memory architectures specifically applicable to VLA models and robotic manipulation/navigation systems. Excludes purely software agent memory systems without embodied deployment considerations.

---

## Memory Taxonomy for Robotics

Cognitive science distinguishes several memory systems, each with robotics analogues:

### Working Memory (Short-Term)

**Human analogue**: Neural activity in prefrontal cortex, holding ~7±2 items for seconds to minutes.

**Robotics implementation**: 
- Current observation buffer
- Token sequences in transformer context
- Limited by attention window (typically 4-32 frames)

**Key constraint**: Context length limits what can be held simultaneously. VLA models like RT-2, OpenVLA, and π₀ process single frames or short sequences, missing longer temporal dependencies.

### Episodic Memory (Experience Storage)

**Human analogue**: Hippocampus storing temporally-indexed experiences—"what, where, when."

**Robotics implementation**:
- Trajectory replay buffers
- Experience replay for policy learning
- Spatio-temporal observation logs
- Scene-graph world instances

**Critical insight**: Manipulation tasks are inherently non-Markovian. Push-buttons tasks show nearly identical pre/post states visually, requiring temporal memory to know whether an action completed.

### Semantic Memory (Knowledge)

**Human analogue**: Neocortical storage of facts, concepts, relationships—independent of specific experiences.

**Robotics implementation**:
- Knowledge graphs (object affordances, spatial relationships)
- Language model priors (frozen in VLM backbones)
- Object property databases
- Environmental maps with semantic annotations

**Key advantage**: Composable and generalizable. "Hammers are for hitting" transfers across instances.

### Procedural Memory (Skills)

**Human analogue**: Motor skill memory—instrumental conditioning, automatic behaviors.

**Robotics implementation**:
- Dynamic Movement Primitives (DMPs)
- Policy networks
- Motor primitives and skill libraries
- Learned controllers for specific actions

**Challenge**: Transferring procedural knowledge across embodiments and tasks remains open.

---

## Key Architectures

### 1. MemoryVLA: Perceptual-Cognitive Memory Bank

**Paper**: Shi et al., "MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation" (arXiv:2508.19236, August 2025)

**Core innovation**: Dual-stream memory inspired by hippocampal-cortical systems.

**Architecture**:
```
VLM Encoder → Working Memory (perceptual + cognitive tokens)
                    ↓
         Perceptual-Cognitive Memory Bank (PCMB)
                    ↓
         Retrieval → Gate Fusion → Consolidation
                    ↓
         Diffusion Action Expert → Actions
```

**Key mechanisms**:

1. **Perceptual tokens**: Fine-grained visual details (256 tokens from DINOv2 + SigLIP)
2. **Cognitive tokens**: High-level semantic summary (1 token from LLaMA-7B)
3. **PCMB**: Stores both streams with temporal positional encoding
4. **Gate fusion**: Learned gating between current and retrieved memories
5. **Consolidation**: Merges temporally adjacent, semantically similar entries when capacity reached

**Results**:
- 71.9% success on SimplerEnv-Bridge (+14.6 over CogAct)
- 83% success on long-horizon temporal tasks (+26 over baselines)
- Real-world validation on 150+ tasks across 3 robots

**Key insight**: Both perceptual (low-level) AND cognitive (high-level) memory needed. Perceptual-only: 64.6%. Cognitive-only: 63.5%. Combined: 71.9%.

### 2. Mind Palace: Scene Graph World Instances

**Paper**: Ginting et al., "Enter the Mind Palace: Reasoning and Planning for Long-term Active Embodied Question Answering" (arXiv:2507.12846, July 2025)

**Core innovation**: Hierarchical scene graphs organized by temporal episodes, inspired by the method of loci memory technique.

**Architecture**:
```
Long-term Memory (M)
      ↓
Episodic Chunking (by hours/days)
      ↓
World Instances [G₁, G₂, ..., Gₙ]
      ↓
Hierarchical Scene Graphs per instance
      ├── Area nodes (v) - spatial clusters
      ├── Viewpoint nodes (w) - observations
      └── Object detections + captions
      ↓
LLM-guided retrieval and planning
```

**Key mechanisms**:

1. **Macro-temporal chunking**: Natural breakpoints (recharging, deployment shifts)
2. **Hierarchical scene graphs**: Areas contain viewpoints, viewpoints contain objects
3. **Value-of-Information stopping**: Decide when memory retrieval won't improve exploration
4. **Cross-episode reasoning**: Query spans multiple world instances

**Results**:
- 12-28% improvement in answer correctness over baselines
- 77% fewer retrieved images while maintaining accuracy
- Real-world deployment over 6 months, 2.4km trajectories

**Key insight**: Structured spatial organization enables efficient retrieval. Questions typically need only a few relevant frames across thousands of observations.

### 3. RoboMemory: Multi-Memory Agentic Framework

**Paper**: "RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning" (arXiv:2508.01415, October 2025)

**Core innovation**: Explicit multi-memory architecture with metamemory governance.

**Architecture**:
- **Spatial memory**: Environmental layout, landmarks
- **Episodic memory**: Temporally-situated experiences
- **Semantic memory**: Facts and relationships
- **Procedural memory**: Skills and motor patterns
- **Metamemory**: Self-awareness of memory processes (what to retain, update, forget)

**Key focus**: Interactive environmental learning—acquiring, integrating, and retrieving knowledge during task execution.

### 4. Topological Memory for Navigation

**Papers**: Multiple (SPTM, HTM, Neural Topological SLAM, Pose-Invariant Topological Memory)

**Core concept**: Non-parametric graph where nodes = locations, edges = reachability.

**Variants**:
- **Semi-Parametric Topological Memory (SPTM)**: Neural network predicts reachability
- **Hallucinative Topological Memory (HTM)**: Generates unexplored edges
- **Neural Topological SLAM**: Graph construction + retrieval network
- **Graph Convolutional Networks**: Encode cognitive features for decision-making

**Application**: Visual navigation where metric maps drift or are unavailable.

---

## Technical Approaches

### Vector Embedding Retrieval (RAG for Robotics)

**Concept**: Store observations as embeddings, retrieve by similarity.

**Implementation**:
```python
# Simplified
memory_bank = VectorDatabase()
memory_bank.store(trajectory_embedding, pose, timestamp, metadata)

# Query
relevant_memories = memory_bank.retrieve(
    query=current_observation_embedding,
    k=10,
    filter=metadata_filter
)
```

**Advantages**:
- Scalable to large memory banks
- Semantic similarity matching
- Well-established infrastructure (vector DBs)

**Limitations**:
- Loses spatial structure
- Chunk-based retrieval misses relationships
- Doesn't capture temporal dependencies

### Scene Graph Representations

**Concept**: Structured graph with objects, relationships, spatial hierarchy.

**3D Scene Graph layers** (Kimera-style):
```
Layers:
  5: Places (navigable areas)
  4: Rooms (semantic regions)
  3: Objects (manipulable entities)
  2: Panes (surfaces)
  1: Mesh (geometry)
```

**Dynamic updates**: DovSG (Dynamic Open-Vocabulary 3D Scene Graphs) enables local updates without full reconstruction.

**Functional scene graphs**: ArtiSG adds affordance information from human demonstrations (e.g., "this drawer can be opened by pulling handle").

### Knowledge Graph Embeddings

**Concept**: Map entities and relations to low-dimensional vectors for efficient reasoning.

**Approaches**:
- TransE, RotatE: Geometric relation modeling
- GNN-based: Graph neural networks for neighborhood aggregation
- Multi-modal: Vision + language + spatial embeddings

**Robotics application**: Semantic reasoning over object affordances, spatial relationships, task constraints.

### Diffusion-Based Policies with Memory

**Concept**: Diffusion models for action generation, conditioned on memory-augmented representations.

**MemoryVLA approach**:
- Memory-conditioned diffusion action expert
- 10-step DDIM denoising
- Cognitive tokens provide high-level guidance
- Perceptual tokens supply fine-grained detail

**Advantage**: Continuous, multimodal action distributions with temporal awareness.

---

## VLA-Specific Memory Challenges

### Temporal Context Length

**Problem**: Standard attention has O(n²) complexity. Concatenating frames scales poorly.

**Solutions**:
- Memory banks (external to context window)
- Attention sinks / streaming attention
- Hierarchical compression (perceptual → cognitive tokens)
- Episode chunking (Mind Palace)

### Distribution Mismatch

**Problem**: VLA models pretrained on single frames. Multi-frame input creates distribution shift.

**Finding**: MemoryVLA uses single-frame input with external memory retrieval, avoiding retraining the VLM backbone.

### Non-Markovian Tasks

**Problem**: Visual observations before/after actions may be nearly identical (push buttons, toggle switches).

**Solution**: Explicit temporal indexing in memory. MemoryVLA uses sinusoidal timestep positional encoding to distinguish temporally adjacent but semantically similar states.

### Long-Horizon Reasoning

**Problem**: Multi-step tasks require tracking state across many actions.

**Approaches**:
- Episodic memory with structured retrieval
- Chain-of-thought reasoning over memory
- Hierarchical task decomposition in scene graphs

---

## Practical Implementation Patterns

### Memory Bank Design

| Parameter | Recommendation | Rationale |
|-----------|----------------|-----------|
| Capacity | 16-64 entries | MemoryVLA: 16 optimal, 64 degrades |
| Streams | Dual (perceptual + cognitive) | 7% improvement over single stream |
| Retrieval | Cross-attention with timestep PE | +2.1% over without positional encoding |
| Fusion | Learned gates | +4.2% over simple addition |
| Consolidation | Token merge (adjacent + similar) | +5.2% over FIFO |

### Scene Graph Construction

**Hierarchical structure**:
1. Sample dense viewpoints from trajectory
2. Detect objects, generate captions per viewpoint
3. Cluster viewpoints → areas (spatial + semantic similarity)
4. Link neighboring areas and viewpoints
5. Associate temporal metadata (episode index, timestamp)

**Update strategy**: Local updates for changed regions, periodic global consolidation.

### Retrieval Strategy

**Mind Palace retrieval cascade**:
1. LLM selects relevant world instances (episodes) from question
2. LLM estimates object location probabilities per area
3. Forward search planner selects area sequence
4. LLM selects specific viewpoints within areas
5. Retrieve images, update working memory
6. Replan based on observations

**Early stopping**: Value-of-Information criteria halt retrieval when exploration more valuable.

---

## Open Challenges

### Memory Consolidation

**Current state**: Simple merging of similar entries, FIFO eviction.

**Needed**: 
- Biologically-inspired consolidation (hippocampal replay)
- Importance-weighted retention
- Forgetting mechanisms that preserve critical memories
- Cross-episode abstraction (extract patterns from multiple experiences)

### Cross-Embodiment Transfer

**Challenge**: Memory acquired on one robot may not transfer to different morphology.

**Approaches**:
- Abstract action representations (task space vs joint space)
- Semantic memory (embodiment-agnostic)
- Shared latent spaces across platforms

### Scalability

**Problem**: Memory grows unboundedly over months/years of operation.

**Solutions needed**:
- Hierarchical compression (summarize old episodes)
- Importance sampling
- Event-based memory (store salient moments, not continuous logs)

### Metamemory

**Gap**: Systems don't know what they don't know.

**Needed**:
- Uncertainty-aware retrieval
- "I need more information" detection
- Proactive memory gathering

---

## Source Map

### Foundational Papers

1. **MemoryVLA** (Shi et al., 2025) - arXiv:2508.19236
   - Primary contribution: PCMB architecture, dual-stream memory

2. **Mind Palace** (Ginting et al., 2025) - arXiv:2507.12846
   - Primary contribution: Scene graph world instances, LA-EQA benchmark

3. **RT-2** (Brohan et al., 2023) - arXiv:2307.15818
   - VLA foundation, web knowledge transfer

4. **OpenVLA** (Kim et al., 2024) - arXiv:2406.09246
   - Open-source VLA baseline

5. **π₀** (Black et al., 2024) - arXiv:2410.24164
   - Diffusion-based VLA

### Knowledge Graph References

1. "Semantic Representation of Robot Manipulation with Knowledge Graph" (2023)
   - Multi-layer knowledge representation for manipulation

2. "3D Scene Graphs in Robotics" (2024/2025)
   - Unified geometry-semantics-action representation

3. Kimera (Rosinol et al., 2021)
   - 3D Dynamic Scene Graphs for spatial perception

### Episodic Memory References

1. "Elements of episodic memory: insights from artificial agents" (Phil. Trans. B, 2024)
   - Cognitive science perspective on artificial episodic memory

2. "Episodic Memory Banks for Lifelong Robot Learning" (OpenReview, 2024)
   - Long-term memory for continual learning

3. "ReEXplore" (arXiv:2511.19033, 2025)
   - Retrospective experience replay for embodied exploration

### Spatial Memory References

1. "Cognitive Navigation for Intelligent Mobile Robots" (IEEE JAS, 2024)
   - Topological memory with graph convolutional networks

2. "Spatial memory-augmented visual navigation" (KNOSYS, 2023)
   - Hippocampal-inspired navigation

3. "Neural Topological SLAM" (Chaplot & Salakhutdinov)
   - Graph + neural network hybrid

### Procedural Memory References

1. "Movement Primitives in Robotics: A Comprehensive Survey" (arXiv:2601.02379, 2025)
   - DMPs and skill transfer

2. "Transfer Learning in Robotics" (arXiv:2311.18044, 2023)
   - Cross-task skill transfer review

---

## Open Questions and Research Directions

### 1. Memory Reflection and Chain-of-Thought

**Current gap**: Memories retrieved but not reasoned over in embedding space.

**Direction**: MemoryVLA future work—"memory reflection" aligning long-term memory to LLM input space for embedding-space chain-of-thought reasoning.

**Why it matters**: Enables reasoning over memory contents without explicit retrieval-to-text bottleneck.

### 2. Lifelong Memory and Biological Consolidation

**Current gap**: Simple eviction/merging, no sophisticated importance weighting.

**Direction**: Biologically-inspired consolidation that distills frequently reused experiences into permanent representations.

**Why it matters**: Robots operating for years need mechanisms to retain critical knowledge while discarding noise.

### 3. Multi-Agent Memory Sharing

**Current gap**: Single-robot memory systems.

**Direction**: Distributed memory banks shared across robot teams, with privacy and relevance filtering.

**Why it matters**: Multi-robot deployments could benefit from collective experience.

### 4. Safety-Critical Memory Verification

**Current gap**: No verification that memories are accurate or safe.

**Direction**: Confidence estimation, cross-validation across episodes, uncertainty-aware retrieval.

**Why it matters**: Incorrect memories could lead to unsafe actions in critical domains.

### 5. Procedural-Semantic Integration

**Current gap**: Procedural (skills) and semantic (facts) memories largely separate.

**Direction**: Unified representations linking "how to do X" with "what X is and when to use it."

**Why it matters**: Enables more flexible skill composition and transfer.

---

## Practical Implications for System Design

### When to Use Which Memory Type

| Task Type | Primary Memory | Supporting Memory |
|-----------|----------------|-------------------|
| Single-step manipulation | Working memory | — |
| Multi-step task execution | Episodic | Working |
| Navigation in known env | Semantic (map) | Episodic |
| Novel environment exploration | Working + Episodic | — |
| Long-term question answering | Episodic + Semantic | — |
| Skill acquisition | Procedural | Episodic (demos) |
| Multi-robot coordination | Semantic (shared) | Episodic (local) |

### Architecture Recommendations

**For manipulation tasks**:
- MemoryVLA-style dual-stream (perceptual + cognitive)
- PCMB with ~16 entry capacity
- Diffusion policy conditioned on memory-augmented tokens

**For navigation tasks**:
- Topological graph as base representation
- Scene graphs for semantic queries
- Hierarchical retrieval (area → viewpoint → observation)

**For long-term deployment**:
- Mind Palace-style episodic chunking
- Scene graph per deployment session
- Value-of-Information for retrieval decisions

---

## Next Steps

- [ ] Deep dive into MemoryVLA implementation details
- [ ] Survey GraphRAG approaches for robotics
- [ ] Investigate neuro-symbolic integration (scene graphs + LLMs)
- [ ] Review hippocampal replay mechanisms for consolidation
- [ ] Compare topological SLAM approaches for dynamic environments

---

**Last Updated**: 2026-02-18  
**Tags**: vla, memory-systems, semantic-memory, knowledge-graphs, embodied-ai, robotics
