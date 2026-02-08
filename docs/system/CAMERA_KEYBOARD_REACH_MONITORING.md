# Camera Keyboard Reach Monitoring - REQUIRED

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED - REQUIRED FEATURE**

---

## 🎯 PURPOSE

**REQUIRED (Not Optional):** Use laptop camera to:
1. **Identify user** (basic recognition, not detailed)
2. **Detect when user reaches for keyboard** (indicates automation failure)
3. **Count keyboard reach events** (track manual interventions)
4. **Correlate with system activity** (understand when automation fails)

---

## 🔍 HOW IT WORKS

### Camera Monitoring
- Uses laptop camera (OpenCV)
- Detects hand movements toward keyboard area
- Uses MediaPipe for hand detection (if available)
- Falls back to motion detection if MediaPipe unavailable

### Keyboard Reach Detection
- Monitors lower portion of frame (keyboard zone)
- Detects when hand moves into keyboard area
- Tracks frequency of reaches
- Records timestamps and correlates with automation status

### User Recognition
- Basic recognition (not detailed)
- Captures baseline frame for comparison
- Detects user presence via motion/activity
- Focuses on identifying when YOU (the user) are present

---

## 📊 WHAT IT TRACKS

1. **Keyboard Reach Count**
   - Total number of times you reach for keyboard
   - Indicates automation failures (you had to manually click)

2. **Reaches Per Hour**
   - Frequency metric
   - Helps identify patterns

3. **Correlation with Automation**
   - When reach happens, checks if voice input was active
   - Identifies automation failures
   - Automatically reactivates voice input when failure detected

4. **Session Statistics**
   - Session duration
   - User presence status
   - Recent events (last 10)

---

## 🚀 USAGE

### Start Camera Monitoring with Auto Voice Input (REQUIRED)

```bash
python scripts/python/auto_voice_input_with_camera_monitor.py --start
```

**This will:**
- ✅ Automatically activate voice input (REQUIRED - not optional)
- ✅ Monitor camera for keyboard reaches
- ✅ Detect automation failures
- ✅ Automatically reactivate voice input when failures detected
- ✅ Track and correlate all events

### View Statistics

```bash
python scripts/python/auto_voice_input_with_camera_monitor.py --stats
```

**Shows:**
- Voice activations
- Keyboard reaches
- Automation failures
- Correlation data

### Camera-Only Monitoring

```bash
python scripts/python/camera_keyboard_reach_detector.py --start
```

---

## 📋 FEATURES

### 1. Automatic Voice Input Activation (REQUIRED)
- **Not optional** - automatically activates voice input
- Reactivates every 5 seconds if not active
- Uses keyboard shortcut (Control+Shift+Space) - most reliable
- Falls back to VLM detection + MANUS clicking

### 2. Camera-Based Reach Detection
- Detects when you reach for keyboard
- Uses hand tracking (MediaPipe) or motion detection
- Focuses on lower portion of frame (keyboard zone)
- Cooldown: 2 seconds (prevents duplicate counts)

### 3. Automation Failure Detection
- When keyboard reach detected → automation failure
- Correlates with voice input status
- Automatically attempts reactivation
- Tracks all failures for analysis

### 4. Statistics & Correlation
- Total reaches
- Reaches per hour
- Automation failures
- Correlation timestamps
- User presence status

---

## 🔧 TECHNICAL DETAILS

### Dependencies
- **OpenCV** (`opencv-python`) - Camera access
- **MediaPipe** (`mediapipe`) - Hand detection (optional, falls back to motion)
- **NumPy** - Image processing

### Detection Methods

1. **MediaPipe Hand Detection** (if available)
   - Detects hand landmarks
   - Checks if hand is in keyboard zone (lower 40% of frame)
   - Most accurate method

2. **Motion Detection** (fallback)
   - Compares frames in keyboard zone
   - Detects significant motion
   - Simpler but effective

### Keyboard Zone
- Lower 40% of camera frame
- Where keyboard is typically located
- Monitors this area for hand movements

---

## 📈 INTERPRETING RESULTS

### Low Reach Count
- ✅ Automation working well
- Voice input staying active
- Minimal manual intervention needed

### High Reach Count
- ⚠️ Automation failing frequently
- Voice input not staying active
- Need to investigate why

### Correlation Analysis
- Reaches when voice inactive → Voice activation failing
- Reaches when voice active → Other automation issues
- Pattern analysis → Identify root causes

---

## 🎯 GOAL

**Track how many times you have to reach for keyboard**
**Correlate with video/activity to understand automation failures**

This helps identify:
- When automation fails
- Why automation fails
- How often you need to manually intervene
- Patterns in automation failures

---

**Tags:** #CAMERA #KEYBOARD_REACH #AUTOMATION_MONITORING #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - REQUIRED FEATURE**
