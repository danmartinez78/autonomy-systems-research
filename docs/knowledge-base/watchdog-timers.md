---
title: "Watchdog Timers in Autonomous Systems"
parent: Knowledge Base
date: 2026-02-18
tags: [safety, reliability, system-architecture]
summary: "Pattern for detecting and recovering from software failures in autonomous systems"
---

# Knowledge Base: Watchdog Timers

<details class="toc-wrapper" open markdown="block">
<summary>Table of Contents</summary>
{: .no_toc }

1. TOC
{:toc}

</details>

## Definition

A watchdog timer is a hardware or software mechanism that monitors system activity and takes corrective action if the system fails to respond within a specified time period. In autonomous systems, watchdogs detect software hangs, infinite loops, or deadlocks and can trigger recovery actions such as restarting processes, entering safe mode, or performing emergency stops.

**Also Known As**: Deadman switch, heartbeat monitor, liveness checker

---

## When to Use

Watchdog timers are essential safety mechanisms in autonomous systems where software failures could lead to unsafe behavior.

**Use This When**:
- System must continue operating or fail safely despite software bugs
- Long-running processes that might hang or deadlock
- Real-time systems requiring guaranteed response times
- Safety-critical applications (vehicles, medical devices, industrial automation)
- Systems with potential for resource exhaustion (memory leaks, runaway computation)

**Don't Use This When**:
- Non-critical applications where restart overhead is unacceptable
- Systems with naturally variable response times where timeout is ambiguous
- As a substitute for fixing underlying bugs (watchdogs are last resort, not primary solution)
- When recovery actions themselves might be unsafe

---

## How It Works

A watchdog timer runs independently of the monitored system. The monitored system must periodically "pet" or "kick" the watchdog to indicate it's still functioning. If the watchdog doesn't receive updates within the timeout period, it assumes the system has failed and triggers recovery.

### Key Components
1. **Timer**: Counts down from a specified timeout value
2. **Reset Mechanism**: Allows monitored system to reset the timer ("pet the dog")
3. **Timeout Handler**: Executes recovery action when timer expires
4. **Independence**: Watchdog must be independent of monitored system (separate thread, process, or hardware)

### Process or Flow
1. System initialization: Set watchdog timeout (e.g., 1 second)
2. Normal operation: Main loop pets watchdog periodically (e.g., every 500ms)
3. Failure scenario: Main loop hangs or crashes, stops petting watchdog
4. Timeout: Watchdog timer expires after 1 second without being pet
5. Recovery: Watchdog triggers recovery action (restart, safe mode, emergency stop)

---

## Tradeoffs and Considerations

### Advantages
- **Fault detection**: Catches software failures that might otherwise go unnoticed
- **Automatic recovery**: Can restore operation without human intervention
- **Safety backstop**: Prevents indefinite unsafe behavior from software bugs
- **Simple concept**: Easy to understand and explain to safety reviewers

### Disadvantages
- **False positives**: May trigger on legitimate slow operations (e.g., sensor initialization)
- **Recovery complexity**: Determining safe recovery action can be difficult
- **Overhead**: Adds code complexity and runtime overhead (usually minimal)
- **Tuning challenge**: Timeout value is critical - too short causes false alarms, too long delays recovery

### Design Considerations
- Timeout value must be longer than worst-case legitimate execution time
- Recovery action must be safer than allowing failure to continue
- Watchdog itself must be reliable (prefer hardware watchdogs for critical systems)
- Consider hierarchical watchdogs (process-level, system-level)
- Log watchdog events for debugging and analysis

---

## Common Pitfalls

### Pitfall 1: Watchdog in Same Thread as Monitored Code
**Problem**: If the monitored code hangs, the watchdog petting code also hangs, so watchdog never fires  
**Why It Happens**: Misunderstanding of independence requirement  
**Solution**: Watchdog must run in separate thread, process, or hardware. The petting action should be the ONLY thing preventing timeout.

### Pitfall 2: Timeout Too Short
**Problem**: False positives from legitimate slow operations (sensor init, file I/O, network requests)  
**Why It Happens**: Underestimating worst-case execution time or not accounting for system load  
**Solution**: Measure actual execution times under worst-case conditions. Add margin (2-3x typical time). Consider suspending watchdog during known slow operations.

### Pitfall 3: Unsafe Recovery Action
**Problem**: Recovery action itself causes unsafe behavior (e.g., sudden stop while moving at high speed)  
**Why It Happens**: Not thinking through consequences of recovery in all possible states  
**Solution**: Design recovery to be safe from any state. Often this means gentle degradation (reduce speed, then stop) rather than immediate action. May need state-dependent recovery strategies.

### Pitfall 4: Petting Watchdog in Exception Handler
**Problem**: Code has subtle bug, throws exception, exception handler pets watchdog before restart, watchdog never fires  
**Why It Happens**: Trying to be "too smart" about keeping watchdog happy  
**Solution**: Pet watchdog only in main loop, AFTER all critical operations succeed. Exception handlers should NOT pet watchdog.

### Pitfall 5: No Logging or Diagnostics
**Problem**: Watchdog fires, system recovers, but root cause remains unknown  
**Why It Happens**: Focus on recovery without thinking about debugging  
**Solution**: Log watchdog events with context (what was executing, system state). Preserve crash dumps if possible. Track watchdog event frequency.

---

## Examples

### Example 1: ROS Node Health Monitor

**Context**: ROS-based autonomous robot with multiple nodes. Critical nodes must be monitored for health.

**Implementation**:
- Each critical node publishes heartbeat message every 100ms
- Separate watchdog node subscribes to heartbeats
- If no heartbeat for 500ms, watchdog triggers recovery (restart node or enter safe mode)
- Watchdog itself monitored by system-level watchdog timer

**Outcome**: Successfully caught several failure modes in testing: node deadlocks, network issues, resource exhaustion. False positive rate reduced to near-zero after tuning timeout values.

### Example 2: Hardware Watchdog for Flight Controller

**Context**: Quadrotor flight controller running on embedded processor. Software bugs could cause crashes.

**Implementation**:
- Hardware watchdog timer on microcontroller (independent of main CPU)
- Main control loop pets watchdog every iteration (50Hz)
- Watchdog timeout set to 100ms (2x loop period)
- On timeout, hardware forces system reset and enters safe mode (land immediately)

**Outcome**: Caught several hard-to-reproduce bugs in development. In one case, prevented crash when main loop hung due to I2C peripheral failure. System landed safely and logged diagnostic information.

---

## References

### Related Papers
- Kopetz & Veríssimo (1993) - "Real-time and dependability concepts" - [Link](https://doi.org/10.1007/978-1-4615-3218-2_6)
- Dubrova (2013) - "Fault-Tolerant Design" - Chapter on watchdog timers

### Related KB Pages
- [Graceful Degradation](./graceful-degradation.md) (to be created)
- [Fail-Safe Design Patterns](./fail-safe-patterns.md) (to be created)
- [System Health Monitoring](./health-monitoring.md) (to be created)

### Related Syntheses
- [Safety Mechanisms in Autonomous Systems](../syntheses/safety-mechanisms.md) (to be created)

### External Resources
- [Wikipedia: Watchdog Timer](https://en.wikipedia.org/wiki/Watchdog_timer)
- [Embedded Systems Design: Watchdog Timers](https://www.embedded.com/how-to-use-watchdog-timers/)
- [ROS 2 Lifecycle Nodes](https://design.ros2.org/articles/node_lifecycle.html) - Related concept

---

## Implementation Notes

Practical guidance for implementing watchdog timers.

### Quick Checklist
- [ ] Identify critical components to monitor
- [ ] Determine appropriate timeout value (measure worst-case execution time)
- [ ] Ensure watchdog runs independently (separate thread/process/hardware)
- [ ] Design safe recovery action for all possible states
- [ ] Implement logging and diagnostics
- [ ] Test with injected failures (hang simulation)
- [ ] Verify false positive rate is acceptable
- [ ] Document timeout values and rationale

### Code Snippet Example (Python)

```python
import threading
import time

class Watchdog:
    def __init__(self, timeout_sec, callback):
        self.timeout = timeout_sec
        self.callback = callback
        self.last_pet = time.time()
        self.running = True
        self.thread = threading.Thread(target=self._monitor, daemon=True)
        self.thread.start()
    
    def pet(self):
        """Reset the watchdog timer (call regularly from monitored code)"""
        self.last_pet = time.time()
    
    def _monitor(self):
        """Internal monitoring loop (runs in separate thread)"""
        while self.running:
            time.sleep(0.1)  # Check every 100ms
            if time.time() - self.last_pet > self.timeout:
                print(f"WATCHDOG TIMEOUT after {self.timeout}s!")
                self.callback()  # Trigger recovery
                self.last_pet = time.time()  # Reset to avoid repeated triggers
    
    def stop(self):
        self.running = False
        self.thread.join()

# Usage example
def recovery_action():
    print("Recovery: Entering safe mode")
    # Implement safe recovery here

def perform_task():
    """Placeholder for your critical task"""
    # Replace this with your actual task logic
    pass

watchdog = Watchdog(timeout_sec=1.0, callback=recovery_action)

# Main loop
try:
    while True:
        # Do critical work
        perform_task()
        
        # Pet watchdog only after successful completion
        watchdog.pet()
        
        time.sleep(0.5)  # Loop rate: 2Hz
finally:
    watchdog.stop()
```

---

**Tags**: safety, reliability, system-architecture
