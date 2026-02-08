# Passive Mode Trigger-Only Fix - CRITICAL

**Date:** 2026-01-09
**Status:** ✅ **FIXED - PASSIVE MODE ONLY LISTENS FOR TRIGGERS**

---

## 🎯 PROBLEM

**User Feedback:**
- "Still missing trigger wake word 'Jarvis' to begin ACTIVE listening"
- System was transcribing everything in passive mode instead of only listening for "Hey Jarvis"
- Wife's voice still bleeding through despite filtering

**Root Causes:**
1. Passive mode was transcribing all speech instead of only checking for trigger words
2. Voice filtering wasn't aggressive enough
3. System wasn't properly switching between passive (trigger-only) and active (transcribing) modes

---

## ✅ FIXES APPLIED

### 1. Passive Mode - Trigger Only (No Transcription)

**File:** `cursor_auto_recording_transcription_fixed.py`

**Changes:**
- Added `passive_mode` flag to transcription service
- In passive mode, ONLY check for trigger words - DON'T transcribe or record
- Skip all transcription/recording logic in passive mode

**Code:**
```python
# CRITICAL: In PASSIVE mode, ONLY check for trigger words - DON'T transcribe anything
if self.passive_mode:
    # Only recognize speech to check for trigger words - don't transcribe or record
    text = self.recognizer.recognize_google(audio, language="en-US")
    
    # Check for trigger words ONLY
    for trigger in self.trigger_words:
        if trigger_text in search_text or "jarvis" in search_text:
            logger.info(f"🎯 TRIGGER DETECTED in passive mode: '{trigger.word}' -> switching to active mode")
            self._handle_trigger(trigger, text)
            break
    
    # CRITICAL: In passive mode, DON'T transcribe or record - just check triggers
    continue  # Skip transcription/recording in passive mode
```

### 2. Hybrid System - Set Passive Mode

**File:** `hybrid_passive_active_listening.py`

**Changes:**
- Set `transcription_service.passive_mode = True` when starting passive listening
- Disable passive mode when switching to active mode
- Re-enable passive mode when resetting after long pause

**Code:**
```python
# CRITICAL: Set passive mode - only listen for triggers, don't transcribe
self.transcription_service.passive_mode = True

# When switching to active mode:
self.transcription_service.passive_mode = False
logger.info("   ✅ Passive mode DISABLED - now transcribing all speech")

# When resetting to passive mode:
self.transcription_service.passive_mode = True
logger.info("   ✅ Passive mode ENABLED - only listening for 'Hey Jarvis' trigger")
```

### 3. More Aggressive Voice Filtering

**File:** `voice_filter_system.py`

**Changes:**
- Increased `voice_match_threshold` from 0.90 to 0.95 (extremely strict)
- Lowered exclusion threshold check from 75% to 50% (more sensitive)
- Added ultra-cautious check: reject if ANY similarity (>0.15) to excluded voice

**Code:**
```python
# Extremely strict threshold
self.voice_match_threshold = 0.95  # EXTREMELY STRICT

# More aggressive exclusion
elif excluded_similarity > (exclude_threshold * 0.5):  # 50% of threshold
    logger.warning(f"🚫 Possible {excluded_id}'s voice - FILTERING OUT (very cautious)")
    return np.zeros_like(audio_data), False

# Ultra-cautious: reject if ANY similarity
elif excluded_similarity > 0.15:  # Even lower - if ANY similarity, reject
    logger.warning(f"🚫 Low similarity to {excluded_id} - FILTERING OUT (ultra-cautious)")
    return np.zeros_like(audio_data), False
```

---

## 🚀 USAGE

### Expected Behavior:

1. **PASSIVE Mode (Default):**
   - ✅ Mic ON - continuously listening
   - ✅ ONLY checking for "Hey Jarvis" trigger word
   - ✅ NO transcription - ignores all other speech
   - ✅ Wife's voice filtered out (won't even check triggers from wife)

2. **ACTIVE Mode (After "Hey Jarvis"):**
   - ✅ Mic ON - actively listening
   - ✅ Transcribing ALL speech (after trigger)
   - ✅ Voice filtering active (only OP's voice)
   - ✅ Auto-send after pauses

3. **Reset to PASSIVE (After Long Pause):**
   - ✅ 10 seconds of silence → reset to passive
   - ✅ Mic stays ON
   - ✅ Back to trigger-only mode

---

## 📋 HOW IT WORKS

### Passive Mode Flow:
1. Listen for audio
2. Recognize speech (to check for triggers)
3. Check if "Hey Jarvis" or "Jarvis" in text
4. If trigger found → switch to ACTIVE mode
5. If no trigger → continue listening (don't transcribe)

### Active Mode Flow:
1. Listen for audio
2. Voice filter check (exclude wife's voice)
3. If OP's voice → transcribe and send
4. If wife's voice → reject and skip
5. After 10s pause → reset to PASSIVE mode

### Voice Filtering:
1. Check excluded profiles FIRST (wife, etc.)
2. If ANY similarity to excluded voice → reject immediately
3. If OP's voice profile trained → check match (threshold 0.95)
4. If match → accept and transcribe
5. If no match → reject (TV/background)

---

## 🔧 CONFIGURATION

### Passive Mode:
- `passive_mode = True` - Only listen for triggers, don't transcribe

### Active Mode:
- `passive_mode = False` - Transcribe all speech (after trigger)

### Voice Filter Threshold:
- `voice_match_threshold = 0.95` - Extremely strict (only OP's voice passes)

### Exclusion Threshold:
- `exclude_threshold = 0.3` - Very sensitive (catches wife's voice easily)
- Reject if similarity > 50% of threshold (0.15)
- Reject if similarity > 0.15 (ultra-cautious)

---

## 🎯 BENEFITS

1. **No Unwanted Transcription** - Passive mode only listens for triggers
2. **Proper Trigger Detection** - "Hey Jarvis" properly switches to active mode
3. **Wife's Voice Filtered** - More aggressive filtering prevents bleed-through
4. **Clear Mode Separation** - Passive (trigger-only) vs Active (transcribing)
5. **Automatic Reset** - Long pauses reset to passive mode

---

**Tags:** #PASSIVE_MODE #TRIGGER_ONLY #VOICE_FILTER #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **FIXED - PASSIVE MODE ONLY LISTENS FOR TRIGGERS**
