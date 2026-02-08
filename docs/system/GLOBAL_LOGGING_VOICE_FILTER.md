# Global Logging Module - Voice Filter Patterns

## Overview

Voice filter logging patterns have been added to the **global logging module** (`lumina_logger.py`) so they apply consistently across the entire project ecosystem and all environments.

## Global Logging Functions

### Voice Filter Acceptance

```python
from lumina_logger import log_voice_filter_accept

log_voice_filter_accept(logger, similarity=0.95, threshold=0.90)
# Output: ✅ Voice match: 0.95 (user's voice) - ACCEPTING (threshold: 0.90)
```

### Voice Filter Rejection

```python
from lumina_logger import log_voice_filter_reject

log_voice_filter_reject(logger, similarity=0.75, threshold=0.90, reason="TV/background/other speaker")
# Output: 
# 🚫 Voice REJECTED: 0.75 (TV/background/other speaker) - FILTERING OUT
#    Threshold: 0.90 - Only user's voice (>0.90) passes
#    This audio will NOT be transcribed - preventing TV bleed through
```

### Voice Profile Not Trained

```python
from lumina_logger import log_voice_filter_not_trained

log_voice_filter_not_trained(logger)
# Output:
# ⚠️  Voice profile not trained - accepting all audio (TV/background may bleed through)
#    ⚠️  CRITICAL: Voice filtering not active - wife/TV audio will be transcribed
```

### Voice Filter Training Progress

```python
from lumina_logger import log_voice_filter_training

log_voice_filter_training(logger, samples_collected=2, samples_needed=3)
# Output:
# 📚 Voice profile training: 2/3 samples collected
#    Training happens in negative space (pauses) - transparent to user
```

### Voice Filter Training Complete

```python
from lumina_logger import log_voice_filter_trained

log_voice_filter_trained(logger, samples_collected=3)
# Output:
# ✅ Voice profile trained! (3 samples, dynamic scaling)
#    Training completed in negative space (pauses) - transparent to user
#    Voice filtering now ACTIVE - TV/background audio will be filtered
```

## Integration

These patterns are now used in:
- `voice_filter_system.py` - Core voice filtering logic
- `cursor_auto_recording_transcription_fixed.py` - Transcription service

## Benefits

1. **Consistent Logging**: Same format across all environments
2. **Global Updates**: Change logging format once, applies everywhere
3. **Clear Messages**: Explicit warnings about TV/background filtering
4. **Easy Debugging**: Standardized patterns make issues easier to track

## Status

✅ **Global Logging Patterns**: Added to `lumina_logger.py`
✅ **Voice Filter Integration**: Updated to use global patterns
✅ **Transcription Integration**: Updated to use global patterns
✅ **Documentation**: Complete

---

**Last Updated**: 2025-01-05
**Purpose**: Global logging patterns for voice filter across all environments
