---
title: "Pre-Read: State Space Models & Mamba (Updated)"
layout: default
parent: CS25: Transformers United V6
grand_parent: Sessions
nav_exclude: true
---

# Pre-Read: State Space Models & Mamba (Updated)

**Date:** April 16, 2026
**Speaker:** Albert Gu (CMU)
**Updated:** 2026-04-15

---

## Updated Paper Details

Based on existing research and pre-read, here's what's known about the Mamba papers:

### Mamba (2023)
- **arXiv:** 2312.00752
- **Key contribution:** Selective state spaces enable O(n) inference with content-dependent dynamics
- **Why it matters:** First practical SSM that can compete with transformers on long sequences

### Mamba-2 (ICML 2024)
- **arXiv:** 2405.21060
- **Key contribution:** State Space Duality (SSD) — shows mathematical equivalence between SSMs and attention
- **Why it matters:** 2-8X faster than Mamba-1, enables cross-pollination between SSM and transformer research

### Mamba-3 (2026)
- **arXiv:** 2603.15569
- **Key contribution:** Latest iteration with architectural improvements
- **Why it matters:** Continues the trajectory of quality + efficiency improvements

---

## What's Missing (Due to Sandbox Constraints)

This research was conducted without live web access. The following would enhance the research:

1. **Recent papers (2026):** Any papers beyond Mamba-3 on arXiv
2. **Lab page updates:** Albert Gu's current projects and collaborations
3. **Citation metrics:** Current impact numbers
4. **Slides:** Not yet posted to Stanford course site

---

## Key Questions to Ask

### Highest Priority for Autonomy:
1. **Edge deployment story** — What's the minimum hardware for Mamba-3?
2. **Multimodal sensor fusion** — Any work on combining vision + proprioception?
3. **Action-conditioned SSMs** — Is there SSM work for robot control?
4. **Irregular sensor sampling** — How does Mamba handle sensors at different rates?

### Technical Depth:
5. How does Mamba-3 differ architecturally from Mamba-2?
6. What's the quality/compute tradeoff at different state dimensions?
7. Where does Mamba significantly underperform transformers?

### Research Futures:
8. Path to 1M+ context windows — fundamental limits?
9. Practical transformer-to-SSM conversion — theoretical or real?
10. Hybrid SSM-transformer architectures — what's the state of the art?

---

*Prepared: 2026-04-15 | Constraints: No live web access*
