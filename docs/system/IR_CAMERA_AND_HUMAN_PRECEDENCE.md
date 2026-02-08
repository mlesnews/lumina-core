# IR Camera & Human Precedence - REQUIRED

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED - IR CAMERA + HUMAN TAKES PRECEDENCE**

---

## 🎯 REQUIREMENTS

**User Feedback:**
1. "Also would like you to use the IR camera, not the normal one"
2. "We need to work together as well, so one can pause and say not control the mouse/keyboard when the other is active. Sorry human takes precedence."

**Problems:**
- System was using normal camera instead of IR camera
- Automation was conflicting with human mouse/keyboard usage
- Need human precedence - pause automation when human is active

**Solutions:**
- ✅ Use IR camera for all visual detection
- ✅ Detect human mouse/keyboard activity
- ✅ Pause automation when human is active
- ✅ Resume automation when human stops
- ✅ Human always takes precedence

---

## ✅ IMPLEMENTATION

### 1. IR Camera Helper

**File:** `ir_camera_helper.py`

**Features:**
- Finds IR camera device index
- Tries multiple backends (MSMF, default, DirectShow)
- Falls back gracefully if IR camera not available
- Configures IR camera settings

**How it works:**
1. Tries index 1, 2, 3 (common IR camera indices)
2. Tries different backends (MSMF, default, DirectShow)
3. Detects IR camera by characteristics (grayscale, resolution)
4. Falls back to index 1 if IR camera not found

### 2. Human Activity Detector

**File:** `human_activity_detector.py`

**Features:**
- Detects mouse movement, clicks, scrolling
- Detects keyboard presses
- Tracks activity timestamps
- Pauses automation when human active
- Resumes automation when human stops

**How it works:**
1. Hooks into mouse/keyboard events
2. Tracks last activity timestamp
3. If activity within 2 seconds → human active
4. If no activity for 2+ seconds → human inactive
5. Calls callbacks to pause/resume automation

### 3. Integration with Automation

**Files Updated:**
- `aggressive_button_clicker.py` - Checks human activity before clicking
- All camera systems - Use IR camera instead of normal camera

**Changes:**
- Button clicker checks `is_automation_allowed()` before clicking
- All camera systems use `open_ir_camera()` instead of `cv2.VideoCapture(0)`
- Automation pauses when human is active

---

## 🚀 USAGE

### Start Human Activity Detector:

```bash
python scripts/python/human_activity_detector.py
```

**This will:**
- Monitor mouse/keyboard activity
- Pause automation when you're using mouse/keyboard
- Resume automation when you stop

### IR Camera Usage:

All camera-based systems now automatically use IR camera:
- Unified visual-audio listening
- Hand wave detection
- Lip movement detection
- Keyboard reach detection

---

## 📋 HOW IT WORKS

### IR Camera Detection:

1. **Try index 1** (common IR camera index)
2. **Try different backends** (MSMF, default, DirectShow)
3. **Check characteristics** (grayscale, resolution)
4. **Fallback to index 1** if IR camera not found

### Human Activity Detection:

1. **Monitor mouse events** (move, click, scroll)
2. **Monitor keyboard events** (key presses)
3. **Track timestamps** (last activity time)
4. **If activity < 2s ago** → Human active → Pause automation
5. **If no activity > 2s** → Human inactive → Resume automation

### Automation Pause/Resume:

- **Human active** → All automation paused
  - Button clicking paused
  - Mouse/keyboard control paused
  - Human has full control

- **Human inactive** → Automation resumed
  - Button clicking resumes
  - Mouse/keyboard control resumes
  - System has control

---

## 🔧 CONFIGURATION

### Activity Timeout:
- `activity_timeout = 2.0` - Seconds of no activity before considering human inactive
- Adjust if too sensitive/not sensitive enough

### IR Camera Index:
- Default: Index 1 (common IR camera index)
- Falls back to regular camera if IR not found

---

## 🎯 BENEFITS

1. **IR Camera** - Better detection, privacy, works in low light
2. **Human Precedence** - No conflicts between automation and manual use
3. **Smooth Cooperation** - System pauses when you're active
4. **Automatic Resume** - System resumes when you stop

---

**Tags:** #IR_CAMERA #HUMAN_PRECEDENCE #AUTOMATION_PAUSE #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - IR CAMERA + HUMAN TAKES PRECEDENCE**
