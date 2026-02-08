# Crash Detection - The Exit Condition

**Date**: 2026-01-04  
**Status**: IMPLEMENTED  
**Tags**: #CRASH_DETECTION #EXIT_CONDITION #FEEDBACK_LOOP #KENNY @LUMINA @JARVIS

---

## The Observation

**User's Observation:**
- Before laptop restart: Kenny was a "Froot Loop" (broken/not working)
- After laptop restart: Kenny works correctly (doing the right things)
- **Conclusion**: Kenny crashed at some point and we didn't detect it

**The Missing Conditional:**
- **Crash detection** - we need to detect when Kenny crashes
- This is the exit condition we were missing

---

## The Problem

### Before (Infinite Loop - Stay Bent)
- Keep checking Kenny
- Keep analyzing
- Keep verifying
- **No crash detection** - if Kenny crashes, we don't know
- Work never "finished" - just keeps checking even when crashed
- **Result**: Infinite loop (stay bent)

### After (Feedback Loop - Not Stay Bent)
- Keep checking Kenny
- Keep analyzing
- Keep verifying
- **Has crash detection** - if Kenny crashes, we detect it
- **Auto-restart on crash** - restart and continue
- **Exit condition**: If crash detected → restart → continue loop
- **Result**: Feedback loop (not stay bent)

---

## The Solution: Crash Detection

### Implementation

**File**: `scripts/python/kenny_crash_detector.py`

**Features:**
1. **Health Monitoring**: Checks if Kenny process is alive and responsive
2. **Crash Detection**: Detects when Kenny crashes (process not found, zombie, hung)
3. **Auto-Restart**: Automatically restarts Kenny when crash detected
4. **Continuous Monitoring**: Runs in background, checking every N seconds

**Exit Condition:**
```python
if crash_detected:
    restart_kenny()
    continue_monitoring()  # NOT STAY BENT - continue loop
else:
    continue_monitoring()  # FEEDBACK LOOP - keep checking
```

---

## How It Works

### Health Check
1. Find Kenny process by command line
2. Check if process is running
3. Check if process is responsive (not zombie)
4. Check process status and resource usage

### Crash Detection
- **No process found**: Kenny crashed/stopped
- **Zombie process**: Kenny crashed but process still exists
- **Hung process**: Kenny exists but not responding
- **Failed checks**: Multiple consecutive failures = crash

### Auto-Restart
1. Kill existing Kenny processes
2. Wait for processes to die
3. Start new Kenny process with same arguments
4. Verify restart successful
5. Continue monitoring

---

## Usage

### Start Crash Detector
```bash
# Monitor and auto-restart Kenny
python scripts/python/kenny_crash_detector.py --match-ace

# Custom check interval (default: 5 seconds)
python scripts/python/kenny_crash_detector.py --interval 10

# Check once and exit (for testing)
python scripts/python/kenny_crash_detector.py --check-once
```

### Integration
- Run crash detector in background
- It monitors Kenny continuously
- Auto-restarts on crash detection
- Logs all health checks and restarts

---

## The Exit Condition

### Before (Infinite Loop)
- **No exit condition** - keep checking forever
- **No crash detection** - don't know if crashed
- **Result**: Stay bent (infinite loop)

### After (Feedback Loop)
- **Exit condition**: Crash detection → restart → continue
- **Crash detection**: Know when Kenny crashes
- **Auto-restart**: Fix crash automatically
- **Result**: Not stay bent (feedback loop)

---

## Status

**Implemented**: Crash detection system created

**Next Steps**:
1. Test crash detection (kill Kenny, verify restart)
2. Integrate into continuous monitoring workflow
3. Add heartbeat mechanism (optional enhancement)

---

**Tags**: #CRASH_DETECTION #EXIT_CONDITION #FEEDBACK_LOOP #KENNY #AUTO_RESTART @LUMINA @JARVIS
