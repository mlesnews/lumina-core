# Voice Filter System - AI Background Voice Filtering

**Purpose**: Filter out TV voices, background conversations, and environmental sounds - only process user's voice.

**Tags**: #VOICE_FILTER #VOICE_PRINT #BACKGROUND_FILTER #AI_FILTERING @JARVIS @LUMINA

---

## Problem

The AI assistant is picking up background voices from:
- TV shows/movies
- Background conversations
- Environmental sounds
- Other people's voices (e.g., "Matt")

This causes confusion and incorrect command processing.

---

## Solution: Voice Print Profile System

### Components

1. **Voice Print Profile** (`VoicePrintProfile`)
   - Stores user's voice characteristics
   - Extracts voice features (pitch, spectral centroid, energy, zero crossing rate)
   - Matches incoming audio against profile
   - Trained with multiple samples

2. **Voice Filter System** (`VoiceFilterSystem`)
   - Filters audio in real-time
   - Only passes through audio that matches user's voice
   - Rejects background/TV/other voices
   - Updates background noise profile

---

## Usage

### Training Voice Profile

```bash
# Train voice profile (collect samples)
python scripts/python/voice_filter_system.py --train --user-id user

# Minimum 5 samples required for training
python scripts/python/voice_filter_system.py --train --min-samples 10
```

### Using Voice Filter

```python
from voice_filter_system import VoiceFilterSystem

# Initialize filter system
filter_system = VoiceFilterSystem(user_id="user")

# Filter audio
filtered_audio, is_user_voice = filter_system.filter_audio(audio_data, sample_rate)

if is_user_voice:
    # Process command
    process_command(filtered_audio)
else:
    # Ignore (background/TV/other voice)
    pass
```

---

## Voice Print Features

The system extracts:
- **Dominant Frequency** (pitch)
- **Spectral Centroid** (brightness)
- **Energy** (volume)
- **Zero Crossing Rate** (voice characteristics)

These features create a unique "fingerprint" of the user's voice.

---

## Background Noise Profile

The system also tracks background noise characteristics:
- TV voices
- Environmental sounds
- Background conversations

This helps with noise cancellation and filtering.

---

## Integration

### With JARVIS

```python
from voice_filter_system import VoiceFilterSystem
from jarvis_system import JARVISSystem

filter_system = VoiceFilterSystem(user_id="user")
jarvis = JARVISSystem(project_root=project_root)

# Filter audio before processing
filtered_audio, is_user_voice = filter_system.filter_audio(audio_data, sample_rate)

if is_user_voice:
    jarvis.process_voice_command(filtered_audio)
```

### With Kenny/Ace

```python
# Voice commands filtered before processing
# Only user's voice triggers actions
# TV/background voices are ignored
```

---

## Training Process

1. **Collect Samples**: User speaks clearly into microphone
2. **Extract Features**: System extracts voice characteristics
3. **Build Profile**: Average features across samples
4. **Train**: Mark profile as trained (minimum 5 samples)
5. **Match**: Compare incoming audio against profile

---

## Configuration

### Voice Match Threshold

Default: `0.7` (70% similarity required)

```python
filter_system.voice_match_threshold = 0.8  # Stricter (80%)
filter_system.voice_match_threshold = 0.6  # More lenient (60%)
```

### Minimum Training Samples

Default: `5` samples

```python
filter_system.voice_profile.train_profile(min_samples=10)
```

---

## Status

- ✅ Voice print profile system created
- ✅ Voice feature extraction implemented
- ✅ Background noise profile tracking
- ⏳ Integration with JARVIS/Kenny/Ace (pending)
- ⏳ Real-time audio filtering (pending)
- ⏳ Training UI/collection (pending)

---

## Next Steps

1. Integrate with JARVIS voice command system
2. Add real-time audio streaming and filtering
3. Create training UI for voice profile collection
4. Test with TV/background voices
5. Verify filtering accuracy

---

**Tags**: #VOICE_FILTER #VOICE_PRINT #BACKGROUND_FILTER #AI_FILTERING @JARVIS @LUMINA
