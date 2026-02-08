# Hybrid Wake Word Detection Approach

**Date:** 2026-01-14  
**Status:** 🎯 **RECOMMENDED APPROACH**

---

## 🔍 The Reality Check

**Windows Speech Recognition Limitation:**
- ❌ SAPI does NOT support custom wake words natively
- ❌ Can't detect "Hey JARVIS" directly
- ✅ But it's excellent for speech-to-text AFTER wake word detection

**Conclusion:** We still need a wake word detector, but we can use Windows Speech Recognition for the speech-to-text part.

---

## 🎯 Recommended Hybrid Approach

### Architecture: Best of Both Worlds

```
┌─────────────────────────────────────────┐
│  Wake Word Detection (Always Listening)│
│  ┌───────────────────────────────────┐  │
│  │ Option A: Porcupine (Primary)     │  │
│  │ - On-device, privacy-focused      │  │
│  │ - Custom wake word support        │  │
│  │ - Low latency                     │  │
│  └───────────────────────────────────┘  │
│  ┌───────────────────────────────────┐  │
│  │ Option B: Azure Speech (Fallback) │  │
│  │ - Production-tested, reliable      │  │
│  │ - Same as VS Code uses            │  │
│  │ - Better accuracy                  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
              ↓ "Hey JARVIS" detected
┌─────────────────────────────────────────┐
│  Speech-to-Text (After Wake Word)      │
│  ┌───────────────────────────────────┐  │
│  │ Windows Speech Recognition        │  │
│  │ - Native OS integration            │  │
│  │ - Free, no cloud dependency       │  │
│  │ - Reliable, well-tested           │  │
│  │ - Low latency                      │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
              ↓ Transcribed text
┌─────────────────────────────────────────┐
│  Process Command                        │
│  - Queue to transcript queue            │
│  - Apply Grammarly                      │
│  - Send to Cursor IDE                   │
└─────────────────────────────────────────┘
```

---

## 🚀 Implementation Plan

### Phase 1: Fix Porcupine (Primary Wake Word Detector)

**Why Porcupine First:**
- ✅ On-device (privacy)
- ✅ No cloud dependency
- ✅ Custom wake word support
- ✅ Low latency

**What We Need:**
1. **Porcupine Access Key** - Get from Picovoice Console
2. **Custom Keyword File** - Create "Hey JARVIS" keyword file (.ppn)
3. **Proper Configuration** - Fix current setup

**Implementation:**
```python
# Fix Porcupine initialization
import pvporcupine
import os

# Get access key from environment or config
PORCUPINE_ACCESS_KEY = os.getenv('PORCUPINE_ACCESS_KEY', '')
PORCUPINE_KEYWORD_PATH = os.path.join(
    project_root, 'models', 'wake_words', 'hey_jarvis.ppn'
)

# Initialize with proper config
if PORCUPINE_ACCESS_KEY and os.path.exists(PORCUPINE_KEYWORD_PATH):
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_ACCESS_KEY,
        keyword_paths=[PORCUPINE_KEYWORD_PATH]
    )
else:
    # Fallback to built-in keywords if custom not available
    porcupine = pvporcupine.create(
        keywords=['jarvis']  # Built-in keyword
    )
```

### Phase 2: Add Azure Speech Fallback

**Why Azure Fallback:**
- ✅ More reliable (production-tested)
- ✅ Better accuracy
- ✅ Same as VS Code uses
- ✅ Handles edge cases better

**Implementation:**
```python
# Azure Speech as fallback
from azure.cognitiveservices.speech import (
    SpeechConfig, SpeechRecognizer, 
    KeywordRecognitionModel
)

# Initialize Azure Speech
azure_speech_config = SpeechConfig(
    subscription=AZURE_SPEECH_KEY,
    region=AZURE_SPEECH_REGION
)

# Use keyword recognition model
keyword_model = KeywordRecognitionModel.from_file("hey_jarvis.table")
recognizer = SpeechRecognizer(
    speech_config=azure_speech_config,
    keyword_recognition_model=keyword_model
)

# Continuous recognition with wake word
recognizer.start_continuous_recognition()
```

### Phase 3: Integrate Windows Speech Recognition (STT)

**Why Windows Speech Recognition:**
- ✅ Native OS integration
- ✅ Free (no cloud costs)
- ✅ Reliable for speech-to-text
- ✅ Low latency

**Implementation:**
```python
# Windows Speech Recognition for STT
import win32com.client

class WindowsSpeechRecognizer:
    def __init__(self):
        self.recognizer = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
        self.context = self.recognizer.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        
    def start_listening(self):
        """Start listening for speech after wake word"""
        self.context.SetNotifyWin32Event()
        self.grammar.DictationSetState(1)  # Enable dictation
        
    def get_transcript(self) -> str:
        """Get transcribed text"""
        # Process recognition results
        pass
```

---

## 📊 Comparison: Hybrid vs Single Approach

| Approach | Wake Word | Speech-to-Text | Pros | Cons |
|----------|-----------|----------------|------|------|
| **Porcupine Only** | ✅ Porcupine | ⚠️ Whisper/OpenAI | Privacy, on-device | STT can be slow |
| **Azure Only** | ✅ Azure | ✅ Azure | Reliable, fast | Cloud dependency, cost |
| **Windows Only** | ❌ Not supported | ✅ Windows SAPI | Native, free | No wake word support |
| **Hybrid (Recommended)** | ✅ Porcupine/Azure | ✅ Windows SAPI | Best of all worlds | More complex setup |

---

## 🎯 Recommended Implementation Order

### Step 1: Fix Porcupine (Immediate)
- Get Porcupine access key
- Create "Hey JARVIS" keyword file
- Fix initialization in `voice_interface_system.py`
- Test wake word detection

### Step 2: Add Windows Speech Recognition (Short-term)
- Integrate Windows SAPI for speech-to-text
- Use after wake word detection
- Replace slow Whisper transcription

### Step 3: Add Azure Fallback (Optional)
- Add Azure Speech as fallback wake word detector
- Use if Porcupine fails or unavailable
- Provides reliability like VS Code

---

## 💡 Why This Hybrid Approach?

1. **Privacy-First:** Porcupine for wake word (on-device)
2. **Reliability:** Azure fallback (production-tested)
3. **Cost-Effective:** Windows SAPI for STT (free, native)
4. **Best Performance:** Each component optimized for its task
5. **Flexibility:** Can switch between components as needed

---

## 🔧 Configuration

```python
# config/voice_config.json
{
    "wake_word": {
        "primary": "porcupine",
        "fallback": "azure",
        "keyword": "hey_jarvis"
    },
    "speech_to_text": {
        "provider": "windows_sapi",
        "fallback": "whisper"
    },
    "porcupine": {
        "access_key": "${PORCUPINE_ACCESS_KEY}",
        "keyword_path": "models/wake_words/hey_jarvis.ppn"
    },
    "azure": {
        "subscription_key": "${AZURE_SPEECH_KEY}",
        "region": "eastus"
    }
}
```

---

## 📝 Next Steps

1. ✅ **Fix Porcupine Setup**
   - Get access key from Picovoice
   - Create "Hey JARVIS" keyword file
   - Update `voice_interface_system.py`

2. 🔄 **Integrate Windows Speech Recognition**
   - Add Windows SAPI integration
   - Use for speech-to-text after wake word
   - Replace slow transcript-based detection

3. 🔄 **Add Azure Fallback (Optional)**
   - Add Azure Speech Services
   - Use as fallback wake word detector
   - Provides VS Code-level reliability

---

**Tags:** `#VOICE` `#WAKE_WORD` `#HYBRID` `#PORCUPINE` `#WINDOWS_SAPI` `#AZURE_SPEECH` `@JARVIS` `@LUMINA`
