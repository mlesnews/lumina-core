# Kenny Voice Filter Fix - Complete

**Date:** 2026-01-09
**Status:** ✅ **ROOT CAUSE IDENTIFIED - FIXES PROVIDED**

---

## 🔍 ROOT CAUSE IDENTIFIED

### Problem 1: Voice Profile NOT Trained ❌

**Status:** Voice profile is **NOT trained** (0 samples collected)

**Impact:**
- When voice profile is not trained, `filter_audio()` returns:
  ```python
  return audio_data, True  # Accepts ALL audio!
  ```
- This means **ALL audio is accepted**, including:
  - ❌ Wife's voice → ACCEPTED (not filtered)
  - ❌ TV voices → ACCEPTED (not filtered)
  - ❌ Phone audio → ACCEPTED (not filtered)
  - ❌ Singing → ACCEPTED (not filtered)
  - ❌ Visitor voices → ACCEPTED (not filtered)

---

### Problem 2: Kenny NOT Using VoiceFilterSystem ❌

**Status:** Kenny (`kenny_imva_enhanced.py`) is **NOT using VoiceFilterSystem**

**Evidence:**
- ❌ No `VoiceFilterSystem` import
- ❌ No `filter_audio()` calls
- ❌ No `is_user_voice` checks

**Impact:**
- Even if voice profile was trained, Kenny wouldn't use it
- Voice filtering is completely bypassed

---

## 🔧 FIXES PROVIDED

### Fix 1: Integrate VoiceFilterSystem into Kenny

**File:** `scripts/python/kenny_imva_enhanced.py`

**Changes Needed:**

1. **Add Import:**
```python
# Add to imports section (around line 60):
try:
    from voice_filter_system import VoiceFilterSystem
    VOICE_FILTER_AVAILABLE = True
except ImportError:
    VOICE_FILTER_AVAILABLE = False
    VoiceFilterSystem = None
```

2. **Initialize in __init__:**
```python
# Add to __init__ method (around line 320, after other integrations):
# Voice Filter System - Filter out TV/background/wife/other voices
self.voice_filter = None
self.voice_filter_enabled = True
if VOICE_FILTER_AVAILABLE:
    try:
        self.voice_filter = VoiceFilterSystem(user_id="user", project_root=self.project_root)
        logger.info("✅ Voice filter system loaded - will filter TV/background/wife/other voices")
    except Exception as e:
        logger.warning(f"⚠️  Voice filter not available: {e}")
        self.voice_filter = None
```

3. **Add Voice Filtering Method:**
```python
# Add new method to KennyIMVAEnhanced class:
def filter_voice_audio(self, audio_data, sample_rate):
    """
    Filter audio to check if it's from user's voice

    Returns:
        (filtered_audio, is_user_voice)
        - filtered_audio: Filtered audio data (or zeros if rejected)
        - is_user_voice: True if user's voice, False if TV/background/wife/other
    """
    if not self.voice_filter_enabled or not self.voice_filter:
        # No filter available - accept all (for backward compatibility)
        return audio_data, True

    # Filter audio
    filtered_audio, is_user_voice = self.voice_filter.filter_audio(audio_data, sample_rate)

    # Debug logging
    if is_user_voice:
        logger.debug("✅ Voice ACCEPTED - user's voice")
    else:
        logger.warning("🚫 Voice REJECTED - TV/background/wife/other speaker")

    return filtered_audio, is_user_voice

def add_voice_training_sample(self, audio_data, sample_rate):
    """
    Add voice sample for training (call when user speaks)

    This collects samples to train the voice profile.
    After 5+ samples, profile will auto-train.
    """
    if not self.voice_filter or not self.voice_filter_enabled:
        return

    # Check if profile is already trained
    if self.voice_filter.voice_profile.profile_data.get("trained", False):
        return  # Already trained, no need to collect more

    # Add training sample
    self.voice_filter.add_training_sample(audio_data, sample_rate)

    # Auto-train if we have enough samples
    samples = self.voice_filter.voice_profile.profile_data.get("samples", [])
    if len(samples) >= 5:
        self.voice_filter.train_profile()
        logger.info("✅ Voice profile trained! Now filtering TV/background/wife/other voices")
```

4. **Use in Voice Recognition Code:**
```python
# When voice recognition is added, use like this:
# (This is a template - actual implementation depends on where voice recognition happens)

audio_data = ...  # Get audio from microphone
sample_rate = ...  # Get sample rate

# FILTER AUDIO - CRITICAL STEP (before transcription)
if self.voice_filter_enabled and self.voice_filter:
    filtered_audio, is_user_voice = self.filter_voice_audio(audio_data, sample_rate)

    if not is_user_voice:
        # REJECT: TV/background/wife/other speaker
        logger.debug("🚫 Voice REJECTED - not user's voice (TV/background/wife/other)")
        return  # Skip transcription - don't process this audio

    audio_data = filtered_audio  # Use filtered audio

    # If profile not trained yet, collect training sample
    if not self.voice_filter.voice_profile.profile_data.get("trained", False):
        self.add_voice_training_sample(audio_data, sample_rate)

# Only transcribe if is_user_voice == True
try:
    transcription = recognizer.recognize_google(audio_data)
    # Process transcription...
except Exception as e:
    logger.error(f"Transcription error: {e}")
```

---

### Fix 2: Train Voice Profile

**Steps to Train:**

1. **Automatic Training (Recommended):**
   - Speak clearly into microphone
   - System will collect voice samples automatically
   - After 5+ samples, profile will auto-train
   - Once trained, only user's voice will be accepted

2. **Manual Training:**
   ```bash
   python scripts/python/voice_filter_system.py --train --user-id user --min-samples 5
   ```

3. **Check Status:**
   ```bash
   python scripts/python/check_voice_filter_status.py
   ```

---

### Fix 3: Increase Threshold (If Needed)

**Current Threshold:** 0.90 (very strict)

**If Still Getting False Positives:**
- Increase threshold to 0.95 (even stricter)
- Or adjust in `voice_filter_system.py`:
  ```python
  self.voice_match_threshold = 0.95  # Very strict - only user's voice
  ```

---

## 📋 IMPLEMENTATION CHECKLIST

- [ ] Add VoiceFilterSystem import to `kenny_imva_enhanced.py`
- [ ] Initialize VoiceFilterSystem in `__init__`
- [ ] Add `filter_voice_audio()` method
- [ ] Add `add_voice_training_sample()` method
- [ ] Integrate voice filtering in voice recognition code
- [ ] Add debug logging
- [ ] Test voice filtering
- [ ] Train voice profile (5+ samples)
- [ ] Verify filtering works (TV/background/wife rejected)

---

## 🎯 EXPECTED BEHAVIOR AFTER FIX

### Before Fix:
- ❌ Wife's voice → Transcribed
- ❌ TV voices → Transcribed
- ❌ Phone audio → Transcribed
- ❌ Singing → Transcribed
- ❌ Visitor voices → Transcribed

### After Fix:
- ✅ User's voice → Transcribed
- ✅ Wife's voice → **REJECTED** (filtered out)
- ✅ TV voices → **REJECTED** (filtered out)
- ✅ Phone audio → **REJECTED** (filtered out)
- ✅ Singing → **REJECTED** (filtered out)
- ✅ Visitor voices → **REJECTED** (filtered out)

---

## 🔗 RELATED FILES

- `scripts/python/voice_filter_system.py` - Voice filter system
- `scripts/python/kenny_imva_enhanced.py` - Kenny IMVA (needs integration)
- `scripts/python/fix_kenny_voice_filtering.py` - Diagnostic script
- `scripts/python/check_voice_filter_status.py` - Status checker
- `data/voice_profiles/user_voice_profile.json` - Voice profile (created after training)

---

## 📝 NOTES

1. **Voice Profile Training:**
   - Requires at least 5 voice samples
   - Samples collected automatically when user speaks
   - Profile auto-trains after 5+ samples
   - Once trained, filtering is active

2. **Threshold:**
   - Current: 0.90 (very strict)
   - Only voices matching 90%+ similarity pass
   - TV/background/wife/other voices will be rejected

3. **Debug Logging:**
   - Logs when voice is accepted/rejected
   - Shows similarity score
   - Helps debug filtering issues

---

**Tags:** #VOICE_FILTER #KENNY #IMVA #FIX #WIFE #TV #BACKGROUND @JARVIS @LUMINA

**Status:** ✅ **ROOT CAUSE IDENTIFIED - FIXES PROVIDED - READY FOR IMPLEMENTATION**
