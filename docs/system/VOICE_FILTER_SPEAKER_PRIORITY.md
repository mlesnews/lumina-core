# Voice Filter - Speaker Priority System

**CRITICAL FIX: Tertiary Speaker Filtering When Primary Active**

---

## 🎯 Problem

When the **primary speaker (user)** is speaking, **tertiary speakers (wife, background voices)** were bleeding through into the conversation/transcription.

**Speaker Hierarchy:**
- **PRIMARY**: User (you) - Always allowed
- **SECONDARY**: Assistant (JARVIS) - Allowed when primary not active
- **TERTIARY**: Wife, background voices - **FILTERED when primary is active**

---

## ✅ Solution

**Enhanced Voice Filter System** with **Speaker Priority Enforcement**:

1. **Primary Speaker Detection**: When primary speaker is detected, system marks them as active
2. **Tertiary Filtering**: When primary is active, ALL tertiary speakers are automatically filtered
3. **Timeout Protection**: After primary stops speaking (2 second timeout), tertiary filtering relaxes
4. **Strict Mode**: In strict mode, tertiary speakers are always filtered

---

## 🔧 Implementation

### Speaker Priority Logic

```python
# PRIMARY SPEAKER (User)
if profile_id == primary_speaker_id:
    primary_speaker_active = True
    NEVER FILTER  # Always allow primary

# SECONDARY SPEAKER (Assistant)
elif profile_id == secondary_speaker_id:
    if primary_active and within_timeout:
        FILTER  # Primary has priority
    else:
        ALLOW  # Primary timeout passed

# TERTIARY SPEAKER (Wife, background)
else:
    if primary_active:
        FILTER  # CRITICAL: Filter when primary active
    elif primary_recent (within 2 seconds):
        FILTER  # Filter if primary was recently active
    else:
        # Use normal filtering logic
```

---

## 📋 Configuration

### Register Tertiary Speaker

```python
from voice_filter_system import VoiceFilterSystem

filter_system = VoiceFilterSystem(user_id="user")

# Register wife's voice as tertiary speaker
filter_system.register_tertiary_speaker(
    profile_id="wife_voice",
    name="Wife",
    audio_features=audio_features  # Optional
)
```

### Check Speaker Status

```python
status = filter_system.get_speaker_status()
# Returns:
# {
#     "primary_speaker_id": "user_user",
#     "secondary_speaker_id": "assistant",
#     "primary_speaker_active": True/False,
#     "last_primary_activity": "2026-01-10T17:30:00",
#     "primary_speaker_timeout": 2.0,
#     "hierarchy": "PRIMARY > SECONDARY > NO TERTIARY"
# }
```

---

## 🎛️ Settings

- **Primary Speaker Timeout**: `2.0 seconds` (configurable)
  - After primary stops speaking, wait 2 seconds before allowing tertiary
  - Prevents bleed-through immediately after primary stops

- **Strict Mode**: When enabled, tertiary speakers are always filtered
  - Even when primary is not active
  - Use for maximum filtering

---

## 🔍 How It Works

1. **Audio Input** → Voice Filter System
2. **Voice Identification** → Identify speaker (primary/secondary/tertiary)
3. **Priority Check**:
   - If **PRIMARY**: Mark active, allow through
   - If **TERTIARY** and **PRIMARY ACTIVE**: **FILTER** ❌
   - If **TERTIARY** and **PRIMARY RECENT**: **FILTER** ❌
   - If **TERTIARY** and **PRIMARY INACTIVE**: Use normal filtering
4. **Result**: Only primary (and secondary when appropriate) passes through

---

## ✅ Expected Behavior

**Before Fix:**
- User speaking → Wife's voice bleeds through ❌
- Both voices transcribed ❌

**After Fix:**
- User speaking → Wife's voice **FILTERED** ✅
- Only user's voice transcribed ✅
- After user stops (2 sec timeout) → Wife's voice still filtered (strict mode) or normal filtering

---

## 🚀 Status

**✅ IMPLEMENTED**

- Speaker priority tracking
- Tertiary filtering when primary active
- Timeout protection
- Strict mode support
- Status monitoring

**Tags**: `#VOICE_FILTER #SPEAKER_PRIORITY #PRIMARY #SECONDARY #TERTIARY @JARVIS @LUMINA`
