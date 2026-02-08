# Cursor IDE Voice Filter Integration

**Purpose**: Sync voice filter system with Cursor IDE microphone features. Works independently of Kenny/Ace virtual assistants.

**Tags**: #CURSOR #VOICE_FILTER #MICROPHONE @JARVIS @LUMINA

---

## Problem

The voice filtering functionality we're building into Kenny also needs to work with Cursor IDE's microphone features. Sometimes users (including yourself) don't want to use or see the virtual assistants - they just want to use Cursor IDE interface.

The voice filter needs to:
- Work with Cursor IDE's microphone/voice input
- Filter out TV voices, background conversations, other people (like "Matt")
- Work independently of Kenny/Ace virtual assistants
- Be toggleable on/off

---

## Solution: Cursor Voice Filter Integration

### Architecture

```
Cursor IDE Microphone
    ↓
Voice Filter System (filters background/TV/other voices)
    ↓
Cursor IDE Voice Processing (only user's voice)
```

### Key Features

1. **Independent Operation**
   - Works even when Kenny/Ace are not running
   - Syncs with Cursor IDE microphone settings
   - Can be enabled/disabled independently

2. **Voice Print Profile**
   - Identifies user's voice (not Matt, not TV)
   - Filters background voices before Cursor processes audio
   - Trained with user's voice samples

3. **Toggle Control**
   - Enable/disable voice filtering
   - Sync with Cursor settings
   - Auto-enable option

---

## Usage

### Enable Voice Filtering

```bash
# Enable voice filtering for Cursor IDE
python scripts/python/cursor_voice_filter_integration.py --enable

# Disable voice filtering
python scripts/python/cursor_voice_filter_integration.py --disable

# Toggle voice filtering
python scripts/python/cursor_voice_filter_integration.py --toggle

# Check status
python scripts/python/cursor_voice_filter_integration.py --status

# Sync with Cursor settings
python scripts/python/cursor_voice_filter_integration.py --sync
```

### Training Voice Profile

```bash
# Train voice profile (collect samples)
python scripts/python/voice_filter_system.py --train --user-id user
```

---

## Configuration

### Config File: `config/cursor_voice_filter_config.json`

```json
{
  "version": "1.0.0",
  "voice_filter_enabled": true,
  "cursor_microphone_enabled": true,
  "sync_with_cursor": true,
  "auto_enable": true,
  "voice_filter_threshold": 0.7,
  "filter_background_voices": true,
  "filter_tv_voices": true,
  "filter_other_people": true
}
```

### Settings

- **`voice_filter_enabled`**: Enable/disable voice filtering
- **`cursor_microphone_enabled`**: Enable/disable Cursor microphone
- **`sync_with_cursor`**: Auto-sync with Cursor IDE settings
- **`auto_enable`**: Auto-enable when Cursor starts
- **`voice_filter_threshold`**: Voice match threshold (0.7 = 70%)
- **`filter_background_voices`**: Filter background conversations
- **`filter_tv_voices`**: Filter TV voices
- **`filter_other_people`**: Filter other people's voices (e.g., "Matt")

---

## Integration with Cursor IDE

### How It Works

1. **Audio Input**: Cursor IDE captures audio from microphone
2. **Voice Filter**: Audio is filtered through voice filter system
3. **Voice Matching**: Audio is matched against user's voice print profile
4. **Processing**: Only user's voice is processed by Cursor IDE
5. **Rejection**: Background/TV/other voices are rejected (not processed)

### Flow

```
User speaks → Microphone → Voice Filter → [User's voice?] → Cursor IDE
                                    ↓
                            [Background/TV/Other?] → Rejected (ignored)
```

---

## Independent Operation

### Works Without Virtual Assistants

The voice filter works independently of Kenny/Ace:
- ✅ Works when Kenny/Ace are not running
- ✅ Works when virtual assistants are disabled
- ✅ Works in Cursor IDE only (no desktop assistants)
- ✅ Can be toggled on/off independently

### Use Cases

1. **Cursor IDE Only**: User wants to use Cursor IDE without virtual assistants
2. **Voice Commands**: User wants voice commands in Cursor IDE
3. **Background Filtering**: Filter out TV/background voices
4. **Privacy**: Only process user's voice, not other people

---

## Voice Print Profile

### Training

1. Collect voice samples (minimum 5 samples)
2. Extract voice features (pitch, spectral centroid, energy)
3. Build voice profile
4. Match incoming audio against profile

### Features

- **Dominant Frequency** (pitch)
- **Spectral Centroid** (brightness)
- **Energy** (volume)
- **Zero Crossing Rate** (voice characteristics)

---

## Status

- ✅ Cursor voice filter integration created
- ✅ Independent operation (works without Kenny/Ace)
- ✅ Toggle control (enable/disable)
- ✅ Config file structure
- ⏳ Integration with Cursor IDE microphone API (pending)
- ⏳ Real-time audio filtering (pending)
- ⏳ Training UI (pending)

---

## Next Steps

1. Integrate with Cursor IDE microphone API
2. Add real-time audio streaming and filtering
3. Create training UI for voice profile collection
4. Test with TV/background voices
5. Verify filtering accuracy

---

## Example Usage

```python
from cursor_voice_filter_integration import CursorVoiceFilterIntegration

# Initialize integration
integration = CursorVoiceFilterIntegration(user_id="user")

# Filter audio for Cursor IDE
filtered_audio, is_user_voice, should_process = integration.filter_audio_for_cursor(
    audio_data, sample_rate
)

if should_process:
    # Process in Cursor IDE (user's voice)
    cursor.process_voice_input(filtered_audio)
else:
    # Reject (background/TV/other voice)
    pass
```

---

**Tags**: #CURSOR #VOICE_FILTER #MICROPHONE @JARVIS @LUMINA
