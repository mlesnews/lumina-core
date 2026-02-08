# Right Alt → @DOIT Remapping & MM-HMM Detection

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED**

---

## 🎯 OVERVIEW

### Right Alt → @DOIT Remapping
- **Request:** Remap Right Alt key to automatically type "@DOIT"
- **Purpose:** Quick execution trigger without typing
- **Status:** ✅ Implemented

### MM-HMM Voice Detection
- **Problem:** Wife's "mm-hmm" sounds being transcribed instead of user's
- **Solution:** Speech pathologist analysis to distinguish between user's and wife's "mm-hmm"
- **Status:** ✅ Implemented

---

## ⌨️ RIGHT ALT → @DOIT REMAPPING

### Implementation

**File:** `right_alt_doit_remap.py`

**Features:**
- Hooks Right Alt key press
- Automatically types "@DOIT" when Right Alt is pressed
- Cooldown protection (500ms) to prevent multiple triggers
- Uses keyboard library for reliable key detection

**Usage:**
```python
from right_alt_doit_remap import RightAltDoitRemap

remap = RightAltDoitRemap()
remap.start()  # Right Alt now types "@DOIT"
```

**Integration:**
- ✅ Integrated into `startup_all_automation.py`
- ✅ Starts automatically on system boot
- ✅ Runs in background (daemon thread)

---

## 🎤 MM-HMM VOICE DETECTION

### Speech Pathologist Analysis

**File:** `mmhmm_voice_detection.py`

**Approach:**
- Uses speech pathologist principles to analyze vocal patterns
- Detects "mm-hmm" sounds based on:
  - Duration (0.1-0.8 seconds)
  - Nasal quality (nasal resonance)
  - Pitch characteristics
  - Formant patterns (vocal tract)
  - Voice quality markers

**Speaker Identification:**
- Compares detected "mm-hmm" with learned patterns
- Uses pitch differences (male vs female)
- Formant analysis (vocal tract differences)
- Nasal quality differences
- Duration patterns

**Learning System:**
- Learns user's "mm-hmm" patterns
- Learns wife's "mm-hmm" patterns
- Improves identification accuracy over time

### Integration with Voice Filtering

**Enhanced `voice_filter_system.py`:**
- Checks for MM-HMM sounds FIRST (before normal filtering)
- Uses speech pathologist analysis to identify speaker
- Filters out wife's "mm-hmm" immediately
- Accepts user's "mm-hmm" with confidence

**Enhanced `unified_visual_audio_listening.py`:**
- Analyzes MM-HMM sounds during conversation
- Prevents starting listening for wife's sounds
- Uses speech pathologist insights for natural flow

---

## 🔬 SPEECH PATHOLOGIST PRINCIPLES

### Analysis Methods:

1. **Vocal Tract Resonance (Formants)**
   - F1 (First formant) - Vowel quality
   - F2 (Second formant) - Vowel quality
   - Differences between speakers

2. **Nasal Quality**
   - Nasal resonance frequency range (200-400 Hz)
   - "mm-hmm" has characteristic nasal quality
   - Different nasal patterns between speakers

3. **Pitch Characteristics**
   - Male voices: 85-180 Hz
   - Female voices: 165-255 Hz
   - Pitch differences help identify speaker

4. **Duration Patterns**
   - Quick acknowledgment: < 0.3s
   - Emphatic acknowledgment: > 0.5s
   - Pattern differences between speakers

5. **Voice Quality Markers**
   - Clear, nasal, muffled
   - Different quality patterns

### Insights Provided:

- "High nasal resonance - typical of 'mm-hmm'"
- "Higher pitch suggests female speaker"
- "Lower pitch suggests male speaker"
- "Short duration - quick acknowledgment"
- "Longer duration - more emphatic acknowledgment"

---

## 🚀 USAGE

### Right Alt Remapping:

**Start manually:**
```bash
python scripts/python/right_alt_doit_remap.py
```

**Automatic (on startup):**
- Integrated into `startup_all_automation.py`
- Starts automatically on system boot
- No manual intervention needed

### MM-HMM Detection:

**Automatic:**
- Integrated into `voice_filter_system.py`
- Automatically detects and filters "mm-hmm" sounds
- Uses speech pathologist analysis

**Learning:**
```python
from mmhmm_voice_detection import MMHMMVoiceDetector

detector = MMHMMVoiceDetector()
# Learn user's pattern
detector.learn_user_mmhmm(pattern)
# Learn wife's pattern
detector.learn_wife_mmhmm(pattern)
```

---

## 📊 HOW IT WORKS

### Right Alt → @DOIT:

1. **Key Hook:** Right Alt key press detected
2. **Cooldown Check:** Prevents multiple triggers (500ms)
3. **Type @DOIT:** Uses pyautogui to type "@DOIT"
4. **Logging:** Logs action for debugging

### MM-HMM Detection:

1. **Audio Analysis:** Analyzes audio for "mm-hmm" characteristics
2. **Pattern Extraction:** Extracts vocal patterns (pitch, formants, nasal quality)
3. **Speaker Identification:** Compares with learned patterns
4. **Filtering Decision:** Filters out wife's "mm-hmm", accepts user's

### Speech Pathologist Analysis:

1. **Feature Extraction:** Pitch, formants, nasal quality, duration
2. **Pattern Comparison:** Compares with learned patterns
3. **Confidence Scoring:** Provides confidence in identification
4. **Insights Generation:** Provides speech pathologist insights

---

## 🔑 KEY FEATURES

### Right Alt Remapping:
- ✅ Automatic typing of "@DOIT"
- ✅ Cooldown protection
- ✅ Background operation
- ✅ Integrated into startup

### MM-HMM Detection:
- ✅ Speech pathologist analysis
- ✅ Speaker identification (user vs wife)
- ✅ Learning system
- ✅ Integration with voice filtering
- ✅ Natural conversation flow

---

## 📚 TRAINING MM-HMM DETECTION

### Collecting Samples:

**For User:**
```bash
python scripts/python/collect_mmhmm_samples.py --speaker user --samples 5
```

**For Wife:**
```bash
python scripts/python/collect_mmhmm_samples.py --speaker wife --samples 5
```

**What It Does:**
- Records "mm-hmm" sounds from the speaker
- Analyzes vocal patterns (speech pathologist approach)
- Learns patterns specific to that speaker
- Improves identification accuracy over time

**After Training:**
- System can distinguish between user's and wife's "mm-hmm"
- Wife's "mm-hmm" automatically filtered out
- User's "mm-hmm" accepted and processed
- Speech pathologist insights provided

---

## 🎯 SPEECH PATHOLOGIST INSIGHTS

### What the System Analyzes:

1. **Pitch Differences**
   - User (male): Typically 85-180 Hz
   - Wife (female): Typically 165-255 Hz
   - Helps identify speaker

2. **Formant Patterns**
   - F1 (First formant): Vowel quality
   - F2 (Second formant): Vowel quality
   - Vocal tract differences between speakers

3. **Nasal Quality**
   - Nasal resonance (200-400 Hz)
   - Different nasal patterns
   - Characteristic of "mm-hmm" sounds

4. **Duration Patterns**
   - Quick vs emphatic acknowledgments
   - Pattern differences between speakers

5. **Voice Quality**
   - Clear, nasal, muffled
   - Quality markers for identification

### Insights Generated:

- "High nasal resonance - typical of 'mm-hmm'"
- "Higher pitch suggests female speaker"
- "Lower pitch suggests male speaker"
- "Short duration - quick acknowledgment"
- "Longer duration - more emphatic acknowledgment"

---

**Tags:** #RIGHT_ALT #DOIT #MMHMM #VOICE_DETECTION #SPEECH_PATHOLOGY #VOICE_FILTER #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - READY FOR USE**

**Next Steps:**
1. Run `collect_mmhmm_samples.py --speaker user` to train your "mm-hmm"
2. Run `collect_mmhmm_samples.py --speaker wife` to train wife's "mm-hmm"
3. System will automatically distinguish between them
4. Right Alt remapping starts automatically on boot
