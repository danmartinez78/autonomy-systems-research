---
layout: default
title: "Example Strange Seed: Terrain Texture as an Implicit Velocity Estimator"
parent: "The Backlog of the Strange"
date: 2026-02-20
tags: [strange, state-estimation, perception]
summary: "Hypothesis: optical-flow statistics over terrain texture could serve as a low-latency velocity cue, bypassing IMU integration drift for ground vehicles."
---

# Example Strange Seed: Terrain Texture as an Implicit Velocity Estimator

**Date captured**: 2026-02-20

---

## The Idea

Ground vehicles traverse textured surfaces constantly. Optical-flow vectors over terrain have a direct geometric relationship to vehicle velocity and heading. The hypothesis is that a lightweight CNN trained on flow-field statistics — rather than point-tracked features — could produce a velocity estimate that is inherently drift-free, since each frame is independent of the last.

This differs from standard visual odometry: instead of tracking keypoints across frames, the model learns the *statistical texture signature* of motion (blur direction, spatial frequency shift, motion-field divergence) and directly regresses velocity from a single flow field.

---

## Why It Might Work

- Terrain texture carries dense motion information that is largely ignored by sparse feature trackers
- Flow-field statistics are theoretically drift-free (no accumulated integration error)
- CNNs have demonstrated surprising ability to extract subtle spatial signals from image statistics
- Ground vehicles operate in a constrained motion manifold (mostly 2D), reducing the regression complexity

---

## Why It Might Fail

- Textureless or repetitive terrain (wet pavement, snow, sand) would likely break the signal entirely
- Illumination changes and shadows introduce confounds that are hard to disentangle from velocity signals
- The network would require a large, diverse training set paired with ground-truth velocity — expensive to collect
- High speeds introduce motion blur that may corrupt the very statistics the model relies on
- Not obviously better than existing methods (LiDAR odometry, IMU + wheel encoder fusion) in normal conditions

---

## Cheap Next Test

1. **Collect a small dataset**: Drive a ground vehicle at controlled speeds (0.5–3 m/s) over varied terrain with a downward-facing camera and a high-accuracy GPS/IMU reference.
2. **Compute optical flow** on each frame pair using a standard algorithm (RAFT or Farnebäck).
3. **Extract flow statistics** (mean magnitude, dominant direction, spatial frequency histogram) as a feature vector.
4. **Fit a linear regressor** from flow statistics to ground-truth speed.
5. **Evaluate correlation**: If R² > 0.8 on held-out terrain types, the signal is real and worth pursuing with a proper network.

Total cost: a few hours of data collection + an afternoon of Python. No new hardware required.

---

## Uncertainty Level

**High** — this is an untested hypothesis. No literature search has been done to confirm or refute it. Treat all claims above as speculation until the cheap next test is run.

---

**Tags**: strange, state-estimation, perception
