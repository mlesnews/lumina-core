# Voice Filter System - Quick Reference

**Core Values: Adapt, Improvise, Overcome**

---

## 🚀 Quick Start

### Basic Usage

```python
from voice_filter_system import VoiceFilterSystem

# Initialize
filter_system = VoiceFilterSystem(
    user_id="user",
    session_id="session_123"
)

# Filter audio
result = filter_system.should_filter(audio_data)
if not result.should_filter:
    # Process audio
    process_audio(audio_data)
```

### Add Voice to Session

```python
filter_system.add_voice_to_session(
    profile_id="voice_001",
    name="User Voice"
)
```

### Configure Session

```python
# Strict mode: Filter all unknowns
filter_system.set_session_strict_mode(strict=True)

# Auto-learn: Learn from unknowns
filter_system.set_session_auto_learn(auto_learn=True)
```

---

## 📊 Filter Result

```python
result = filter_system.should_filter(audio_data)

# Properties
result.should_process      # bool: Should process audio?
result.should_filter       # bool: Should filter out?
result.reason              # str: Reason for decision
result.confidence          # float: Confidence score (0.0-1.0)
result.profile_id          # str: Identified profile ID (if known)
result.confidence_level    # str: Confidence level (UNKNOWN, LOW, MEDIUM, HIGH, CERTAIN)
result.adaptation_applied  # bool: Was adaptation applied?
```

---

## 🎯 Confidence Levels

- **CERTAIN** (≥0.95): Always include
- **HIGH** (≥0.8): Include
- **MEDIUM** (≥0.6): May filter
- **LOW** (≥0.3): Filter out
- **UNKNOWN** (<0.3): Filter out

---

## 🔄 Evolution

```python
# Evolve all profiles
filter_system.evolve()

# Get statistics
stats = filter_system.get_statistics()
```

---

## 📝 Integration Example

```python
# In transcription system
from voice_filter_system import VoiceFilterSystem

class TranscriptionSystem:
    def __init__(self):
        self.voice_filter = VoiceFilterSystem(
            user_id="user",
            project_root=self.project_root
        )
    
    def process_audio(self, audio_data):
        # Filter audio
        result = self.voice_filter.should_filter(audio_data)
        
        if result.should_filter:
            logger.debug(f"Filtered: {result.reason}")
            return None
        
        # Process transcription
        transcript = self.transcribe(audio_data)
        return transcript
```

---

## 🎛️ Session Scope

Each session has:
- **Active Profiles**: Voices in scope
- **Confidence Floor**: Minimum confidence to allow
- **Auto-Learn**: Learn from unknowns
- **Strict Mode**: Filter all unknowns

---

**Tags:** #VOICE_FILTER #QUICK_REFERENCE #ADAPT #IMPROVISE #OVERCOME
