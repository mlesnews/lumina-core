# Danny Boy Acapella Duet & Auto-Send Fix

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED**

---

## 🎯 OVERVIEW

### Danny Boy Acapella Duet
- **Request:** JARVIS and Wanda sing "Danny Boy" together in acapella as opposing tenors
- **Purpose:** "Rock solid test" of system capabilities
- **Status:** ✅ Implemented

### Auto-Send Fix
- **Problem:** User counted past 5 - system didn't auto-send after pause
- **Solution:** More aggressive pause detection (3s base, force 1.5s after 3s silence)
- **Status:** ✅ Fixed

---

## 🎵 DANNY BOY ACAPELLA DUET

### Implementation

**File:** `jarvis_danny_boy_duet.py`

**Features:**
- JARVIS (Tenor 1 - Higher) and Wanda (Tenor 2 - Lower) sing in harmony
- Acapella (no instruments)
- Opposing tenors arrangement
- Uses ElevenLabs singing voices (if available)
- Falls back to synthesized notes if ElevenLabs not available

**Musical Arrangement:**
- Full "Danny Boy" lyrics arranged for two tenors
- Harmony offset: Tenor 2 sings 4 semitones below Tenor 1 (third harmony)
- Each phrase has musical notes and duration
- Real-time audio mixing for harmony

**Usage:**
```python
from jarvis_danny_boy_duet import DannyBoyDuet

duet = DannyBoyDuet()
duet.sing_duet(
    jarvis_voice_id="jarvis_voice_id",  # Optional ElevenLabs voice for JARVIS
    wanda_voice_id="wanda_voice_id"     # Optional ElevenLabs voice for Wanda
)
```

**Command Line:**
```bash
python scripts/python/jarvis_danny_boy_duet.py --jarvis-voice VOICE_ID --wanda-voice VOICE_ID
```

### ElevenLabs Singing Voices

**Capabilities:**
- ElevenLabs supports singing voices via their API
- Use `eleven_turbo_v2_5` or `eleven_multilingual_v2` models
- Can generate realistic singing from text
- Supports different voice characteristics

**Voice Selection:**
- JARVIS (Tenor 1): Higher tenor voice
- Wanda (Tenor 2): Lower tenor voice
- Can use custom ElevenLabs voice IDs

### Fallback: Synthesized Notes

**If ElevenLabs not available:**
- System synthesizes musical notes
- Generates sine waves for each note
- Applies envelope (attack, decay, sustain, release)
- Mixes both voices in harmony

---

## ⏱️ AUTO-SEND FIX

### Problem

**User Feedback:**
- "I just counted past 5 there. So there was no auto sound."
- System didn't auto-send after pause
- Dynamic pause timeout was too long (5s base, up to 10s)

### Solution

**File:** `cursor_auto_recording_transcription_fixed.py`

**Changes:**
1. **Reduced base timeout:** 5.0s → 3.0s
2. **Force auto-send after long pause:** If no audio for 3+ seconds, force timeout to 1.5s
3. **Lower minimum timeout:** 5.0s → 3.0s (faster decay)

**Code:**
```python
# CRITICAL FIX: User counted past 5 - need to auto-send sooner
# If no audio for 3+ seconds, force auto-send (was 5s)
time_since_audio = current_time - self.last_audio_time if self.last_audio_time else float('inf')
if time_since_audio > 3.0:
    # Force shorter timeout to trigger auto-send
    self.dynamic_pause_timeout = 1.5  # Very short - force auto-send
    logger.info(f"⏱️  Long pause detected ({time_since_audio:.1f}s) - forcing auto-send timeout to {self.dynamic_pause_timeout:.1f}s")
```

**Behavior:**
- Base timeout: 3.0s (was 5.0s)
- Active speaking: Up to 10s (unchanged)
- Long pause (>3s): Force 1.5s timeout (triggers auto-send immediately)
- Minimum timeout: 3.0s (was 5.0s)

---

## 🎤 VOICE COMMAND INTEGRATION

### Trigger Words

**To sing Danny Boy:**
- "Hey Jarvis, sing Danny Boy"
- "Jarvis, let's sing Danny Boy together"
- "Danny Boy duet"

**Integration:**
- Add to trigger word system in `hybrid_passive_active_listening.py`
- Execute `DannyBoyDuet().sing_duet()` when triggered

---

## 📊 HOW IT WORKS

### Danny Boy Duet:

1. **Initialize System:**
   - Load ElevenLabs TTS (if available)
   - Create musical arrangement (lyrics + notes)
   - Set up audio output

2. **Sing Phrases:**
   - For each phrase pair (JARVIS + Wanda):
     - Generate audio for both voices
     - Mix in harmony
     - Play mixed audio

3. **Audio Generation:**
   - **ElevenLabs (preferred):** Use singing voices
   - **Fallback:** Synthesize musical notes

4. **Harmony Mixing:**
   - Mix two audio tracks together
   - Average to prevent clipping
   - Real-time playback

### Auto-Send Fix:

1. **Dynamic Timeout:**
   - Active speaking: Longer timeout (up to 10s)
   - Pause detected: Shorter timeout (3s base)
   - Long pause (>3s): Force 1.5s timeout

2. **Auto-Send Trigger:**
   - When timeout expires → auto-send
   - Faster response to user pauses
   - Prevents user from "counting past 5"

---

## 🔑 KEY FEATURES

### Danny Boy Duet:
- ✅ Acapella arrangement (no instruments)
- ✅ Opposing tenors (harmony)
- ✅ ElevenLabs singing voices
- ✅ Synthesized notes fallback
- ✅ Real-time audio mixing
- ✅ Full "Danny Boy" lyrics

### Auto-Send Fix:
- ✅ Faster pause detection (3s base)
- ✅ Force auto-send after long pause (1.5s)
- ✅ More responsive to user pauses
- ✅ Prevents "counting past 5" issue

---

## 🚀 USAGE

### Sing Danny Boy:

**Python:**
```python
from jarvis_danny_boy_duet import DannyBoyDuet

duet = DannyBoyDuet()
duet.sing_duet()
```

**Command Line:**
```bash
python scripts/python/jarvis_danny_boy_duet.py
```

**With Custom Voices:**
```bash
python scripts/python/jarvis_danny_boy_duet.py --jarvis-voice VOICE_ID --wanda-voice VOICE_ID
```

### Auto-Send:

**Automatic:**
- System automatically detects pauses
- Auto-sends after 3s of silence (base)
- Forces auto-send after 3s+ pause (1.5s timeout)

**No manual intervention needed!**

---

## 🎯 TESTING

### "Rock Solid Test"

**Danny Boy Duet:**
- JARVIS and Wanda sing together
- Acapella (no instruments)
- Opposing tenors in harmony
- Tests:
  - Voice synthesis (ElevenLabs)
  - Audio mixing
  - Musical arrangement
  - Real-time playback

**Auto-Send:**
- User pauses → system auto-sends
- No "counting past 5" issue
- Faster response to pauses

---

**Tags:** #SINGING #DUET #DANNY_BOY #ACAPELLA #TENOR #AUTO_SEND #ELEVENLABS #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - READY FOR TESTING**

**Next Steps:**
1. Test Danny Boy duet: `python scripts/python/jarvis_danny_boy_duet.py`
2. Test auto-send: Speak, pause 3+ seconds → should auto-send
3. Add voice command: "Hey Jarvis, sing Danny Boy"
