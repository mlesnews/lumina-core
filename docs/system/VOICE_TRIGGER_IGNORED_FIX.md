# Voice Trigger Ignored - Fix Guide

**Date:** 2026-01-14  
**Issue:** Voice triggers are being ignored/filtered  
**Status:** 🔍 **INVESTIGATING**

---

## 🔍 Problem Analysis

### Symptoms
- User says "Hey JARVIS, test" or other wake word commands
- Voice trigger is ignored
- No response from voice system

### Root Causes (Potential)

1. **Voice Filter Too Aggressive**
   - Unknown voices filtered by default (line 711-719 in voice_filter_system.py)
   - Primary speaker not recognized
   - Ultra-aggressive filtering blocking user's voice

2. **Wake Word Detection Issues**
   - Wake word not detected
   - Porcupine not initialized
   - Transcript-based fallback not working

3. **Voice Identification Failure**
   - User's voice not recognized as primary speaker
   - Profile ID mismatch
   - Confidence threshold too high

4. **Filter Applied Before Wake Word**
   - Voice filtered before wake word detection
   - No bypass for wake word + command sequences

---

## ✅ Fixes to Apply

### Fix 1: Bypass Filtering for Wake Word Commands

**Location:** `voice_filter_system.py` - `filter_voice_audio()` method

**Change:** Add wake word detection bypass

```python
def filter_voice_audio(self, audio_data, transcription_text=None, ...):
    # BYPASS: If wake word detected, allow through regardless of filtering
    if transcription_text:
        wake_words = ["hey jarvis", "jarvis", "hey jarvis,"]
        transcript_lower = transcription_text.lower()
        if any(wake in transcript_lower for wake in wake_words):
            logger.info("   ✅ WAKE WORD DETECTED - bypassing filter")
            # Mark as primary speaker and allow through
            self.primary_speaker_active = True
            self.last_primary_activity = datetime.now()
            return FilterResult(
                should_process=True,
                should_filter=False,
                reason="wake_word_bypass",
                confidence=1.0,
                profile_id=self.primary_speaker_id
            )
```

### Fix 2: Lower Unknown Voice Filtering Threshold

**Location:** `voice_filter_system.py` - Unknown voice handling

**Change:** Allow unknown voices if wake word present

```python
# Current (line 711-719): Filters all unknown voices
# Change: Check for wake word before filtering
if not profile_id:
    # Check if wake word is present
    if transcription_text:
        wake_words = ["hey jarvis", "jarvis"]
        if any(wake in transcription_text.lower() for wake in wake_words):
            # Wake word present - allow through as primary
            profile_id = self.primary_speaker_id
            should_filter = False
            self.primary_speaker_active = True
            self.last_primary_activity = datetime.now()
            logger.info("   ✅ WAKE WORD - treating as primary speaker")
    else:
        # No wake word - filter unknown voice
        should_filter = True
```

### Fix 3: Ensure Primary Speaker Recognition

**Location:** `voice_filter_system.py` - Primary speaker initialization

**Change:** Ensure user voice is recognized as primary

```python
# In __init__:
self.primary_speaker_id = f"user_{user_id}"  # Should match user
self.primary_speaker_active = False  # Start inactive

# Add method to force primary speaker:
def force_primary_speaker(self, profile_id=None):
    """Force set primary speaker (for wake word bypass)"""
    if profile_id:
        self.primary_speaker_id = profile_id
    self.primary_speaker_active = True
    self.last_primary_activity = datetime.now()
    logger.info(f"   ✅ Primary speaker forced: {self.primary_speaker_id}")
```

### Fix 4: Wake Word Detection Enhancement

**Location:** `voice_interface_system.py` - `_check_wake_word_in_buffer()`

**Change:** Improve wake word detection reliability

```python
def _check_wake_word_in_buffer(self, wake_word: str) -> bool:
    # ... existing code ...
    
    # ENHANCED: More lenient transcript matching
    if transcript:
        # Check for variations
        wake_variations = [
            wake_word.lower(),
            "hey jarvis",
            "jarvis",
            "hey jarvis,",
            "hey jarvis.",
            "hey jarvis!"
        ]
        transcript_lower = transcript.lower()
        if any(variation in transcript_lower for variation in wake_variations):
            self.logger.info(f"   ✅ Wake word detected (lenient): {wake_word}")
            return True
```

---

## 🧪 Testing Steps

### Test 1: Wake Word Detection
1. Say "Hey JARVIS, test"
2. Check logs for wake word detection
3. Verify voice command is captured

### Test 2: Filter Bypass
1. Say "Hey JARVIS, test" (unknown voice)
2. Check logs for "WAKE WORD - bypassing filter"
3. Verify transcript is queued

### Test 3: Primary Speaker Recognition
1. Say "Hey JARVIS, test"
2. Check if primary_speaker_active is set to True
3. Verify voice is not filtered

---

## 📊 Diagnostic Commands

### Check Voice Interface Status
```bash
python scripts/python/voice_interface_system.py --status
```

### Check Voice Filter Status
```python
from voice_filter_system import get_voice_filter_system
filter_system = get_voice_filter_system()
print(f"Primary Speaker: {filter_system.primary_speaker_id}")
print(f"Primary Active: {filter_system.primary_speaker_active}")
print(f"Aggressive Filtering: {filter_system.aggressive_tertiary_filtering}")
```

### Check Wake Word Detection
```python
from voice_interface_system import get_voice_interface
voice = get_voice_interface()
print(f"Listening: {voice.listening_active}")
print(f"Wake Word Detected: {voice.wake_word_detected}")
```

---

## 🎯 Quick Fix (Immediate)

**Temporary Workaround:** Disable aggressive filtering for testing

```python
# In voice_filter_system.py __init__:
self.aggressive_tertiary_filtering = False  # Temporarily disable
self.primary_speaker_active = True  # Assume primary is always active
```

**Warning:** This will allow all voices through - use only for testing.

---

## 📝 Implementation Priority

1. **HIGH:** Fix 1 - Bypass filtering for wake word commands
2. **HIGH:** Fix 2 - Lower unknown voice filtering when wake word present
3. **MEDIUM:** Fix 3 - Ensure primary speaker recognition
4. **MEDIUM:** Fix 4 - Enhance wake word detection

---

**Tags:** `#VOICE` `#FILTER` `#WAKE_WORD` `#DEBUGGING` `@JARVIS` `@LUMINA`
