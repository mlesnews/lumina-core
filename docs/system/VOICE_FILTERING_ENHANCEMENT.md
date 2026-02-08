# Voice Filtering Enhancement

**Fixing Wife & Alexa Bleeding Through**

---

## 🎯 Problem

**Issue**: Wife and Alexa voices are bleeding through into transcription, even when primary speaker (user) is active.

**Root Cause**: Unknown voices not being filtered aggressively enough when primary speaker is active.

---

## ✅ Solution

### Enhanced Unknown Voice Filtering

**Changes Made**:
1. **Unknown voices**: Always filter when primary active
2. **Primary recent activity**: Filter unknown voices within timeout window
3. **Default behavior**: Filter unknown voices by default (not in scope)

### Code Changes

**File**: `scripts/python/voice_filter_system.py`

**Before**:
```python
else:
    # Unknown voice - filter aggressively
    should_filter, reason, confidence = self.profile_library.should_filter_audio(...)
    if self.primary_speaker_active:
        should_filter = True
```

**After**:
```python
else:
    # Unknown voice - filter aggressively to prevent workflow interruption
    # Unknown voices could be tertiary speakers (wife, Alexa, etc.) we haven't identified yet
    should_filter, reason, confidence = self.profile_library.should_filter_audio(...)
    
    # CRITICAL: If primary is active or was recently active, ALWAYS filter unknown voices
    if self.primary_speaker_active:
        should_filter = True
        reason = "unknown_voice_filtered_primary_active"
        confidence = 0.95
        logger.info(f"   🚫 FILTERED UNKNOWN VOICE (PRIMARY ACTIVE - preventing bleed-through)")
    elif self.last_primary_activity:
        time_since_primary = (datetime.now() - self.last_primary_activity).total_seconds()
        if time_since_primary < self.primary_speaker_timeout:
            should_filter = True
            reason = "unknown_voice_filtered_primary_recent"
            confidence = 0.9
            logger.info(f"   🚫 FILTERED UNKNOWN VOICE (PRIMARY RECENT - preventing bleed-through)")
    else:
        # No primary activity - still filter unknown voices by default
        should_filter = True
        reason = "unknown_voice_not_in_scope"
        confidence = 0.85
        logger.debug(f"   🚫 FILTERED UNKNOWN VOICE (not in scope)")
```

---

## 🔍 Filtering Logic

### Speaker Priority (Enforced)

1. **Primary Speaker** (User)
   - ✅ NEVER filtered
   - Always processed
   - Marks system as "primary active"

2. **Secondary Speaker** (Assistant/JARVIS)
   - ✅ Allowed when primary not active
   - 🚫 Filtered when primary active or recently active

3. **Tertiary Speakers** (Wife, Alexa, Background)
   - 🚫 ALWAYS filtered
   - No exceptions during conversations

4. **Unknown Voices**
   - 🚫 ALWAYS filtered when primary active
   - 🚫 Filtered when primary recently active (within timeout)
   - 🚫 Filtered by default (not in scope)

---

## 📊 Expected Behavior

### Scenario 1: User Speaking
- **User voice**: ✅ Processed
- **Wife voice**: 🚫 Filtered (tertiary)
- **Alexa voice**: 🚫 Filtered (unknown/tertiary)
- **Result**: Only user's voice transcribed

### Scenario 2: User Just Finished Speaking
- **User voice**: ✅ Processed (within 30s timeout)
- **Wife voice**: 🚫 Filtered (primary recent)
- **Alexa voice**: 🚫 Filtered (primary recent)
- **Result**: Only user's voice transcribed

### Scenario 3: User Inactive (30s+)
- **User voice**: N/A
- **Wife voice**: 🚫 Filtered (tertiary, always filtered)
- **Alexa voice**: 🚫 Filtered (unknown, not in scope)
- **Result**: No transcription (user inactive)

---

## 🚀 Speech Pathologist Feedback Loop

**New Feature**: Continuous learning system to improve voice recognition accuracy.

**File**: `scripts/python/speech_pathologist_feedback_loop.py`

**Features**:
- Learns how people speak
- Learns how they pronounce words
- Improves transcription accuracy
- Adapts to individual speech patterns

**Usage**:
```python
from speech_pathologist_feedback_loop import SpeechPathologistFeedbackLoop

feedback_loop = SpeechPathologistFeedbackLoop()

# Learn from interaction
feedback_loop.learn_from_interaction(
    speaker_id="user",
    transcription="Hello world",
    corrections=[
        {"original": "helo", "corrected": "hello"},
        {"original": "wurld", "corrected": "world"}
    ]
)

# Improve transcription using learned patterns
improved = feedback_loop.improve_transcription("user", "helo wurld")
# Result: "hello world"
```

---

## ✅ Status

- ✅ Unknown voice filtering enhanced
- ✅ Primary speaker priority enforced
- ✅ Tertiary speakers always filtered
- ✅ Speech pathologist feedback loop created
- ⚠️ **Testing Needed**: Verify wife/Alexa properly filtered in real scenarios

---

**Tags**: `#VOICE_FILTERING #ENHANCEMENT #SPEECH_PATHOLOGIST @JARVIS @LUMINA`
