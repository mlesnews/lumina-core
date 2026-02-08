# Hybrid Passive-Active Listening - REQUIRED

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED - TRIGGER WORD SWITCHES TO ACTIVE MODE**

---

## 🎯 REQUIREMENT

**User Feedback:**
> "Think we are going to have to do a hybrid of me saying the trigger, 'Hey Jarvis', and then have you change from passive listening to active listening mode, this would reset after long pauses."

**Problem:**
- Need hybrid approach: passive + active modes
- Trigger word "Hey Jarvis" switches to active mode
- Long pauses reset back to passive mode

**Solution:**
- ✅ Passive listening mode (waits for trigger)
- ✅ Active listening mode (after trigger)
- ✅ "Hey Jarvis" trigger switches to active
- ✅ Long pauses reset to passive

---

## ✅ IMPLEMENTATION

### Hybrid Passive-Active Listening

**File:** `hybrid_passive_active_listening.py`

**Modes:**
1. **PASSIVE Mode:**
   - Low-power listening
   - Only listens for "Hey Jarvis" trigger
   - Minimal processing
   - Long timeout (30s) - just waiting

2. **ACTIVE Mode:**
   - Full attention listening
   - Processes all speech
   - More responsive
   - Shorter timeout (5s) - actively listening
   - Integrates with unified visual-audio listener

3. **RESET:**
   - After 10 seconds of silence in active mode
   - Resets back to passive mode
   - Waits for next "Hey Jarvis" trigger

---

## 🚀 USAGE

### Start Hybrid Listening:

```bash
python scripts/python/hybrid_passive_active_listening.py
```

**Flow:**
1. **Passive Mode** → Say "Hey Jarvis"
2. **Active Mode** → System actively listens
3. **Long Pause (10s)** → Resets to passive mode
4. **Repeat** → Say "Hey Jarvis" again to reactivate

---

## 📋 HOW IT WORKS

### Mode Transitions:

1. **Start:** Passive mode (waiting for trigger)
2. **Trigger Detected:** "Hey Jarvis" → Switch to active mode
3. **Active Listening:** Full attention, processes all speech
4. **Long Pause:** 10 seconds of silence → Reset to passive mode
5. **Repeat:** Back to step 1

### Trigger Word:

- **"Hey Jarvis"** → Switches to active mode
- **"Jarvis"** → Also switches to active mode
- **Confidence:** 0.5 (low threshold for better detection)

### Timeouts:

- **Passive Mode:** 30 seconds (long - just waiting)
- **Active Mode:** 5 seconds (short - actively listening)
- **Reset Threshold:** 10 seconds of silence

---

## 🔧 CONFIGURATION

### Active Mode Timeout:
- `active_mode_timeout = 10.0` - Seconds of silence before resetting to passive
- Adjust if too sensitive/not sensitive enough

### Trigger Word:
- `trigger_word = "hey jarvis"` - Primary trigger
- Also accepts "jarvis" alone

---

## 🎯 BENEFITS

1. **Energy Efficient** - Passive mode uses less resources
2. **Natural Activation** - Say "Hey Jarvis" to activate
3. **Automatic Reset** - Resets after pauses
4. **Clear States** - Know when system is passive vs active

---

**Tags:** #HYBRID #PASSIVE_ACTIVE #TRIGGER_WORD #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - TRIGGER WORD SWITCHES TO ACTIVE MODE**
