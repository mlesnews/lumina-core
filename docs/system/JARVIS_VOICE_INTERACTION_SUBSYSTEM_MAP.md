# JARVIS Voice Interaction - Complete Subsystem Map

**Date:** 2026-01-13  
**Status:** 🗺️ **COMPREHENSIVE MAPPING IN PROGRESS**

---

## 🎯 Complete Voice Interaction Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    VOICE INTERACTION SUBSYSTEMS                          │
└─────────────────────────────────────────────────────────────────────────┘

[1] VOICE CAPTURE
    ├── PyAudio (Real-time microphone input)
    ├── Pre-Buffer (Ring buffer, 1 second)
    ├── Continuous Streaming
    └── Audio Format: 16kHz, mono, 16-bit PCM

[2] WAKE WORD DETECTION
    ├── Porcupine (Primary - instant detection)
    ├── Transcript-based (Fallback)
    └── Pre-buffered audio access (no lag)

[3] VOICE ACTIVITY DETECTION (VAD)
    ├── Energy-based detection
    ├── Speech endpoint detection
    ├── Silence timeout (3 seconds default)
    └── Adaptive thresholds

[4] SPEECH-TO-TEXT TRANSCRIPTION
    ├── Whisper (Local - Primary)
    ├── OpenAI Whisper API (Fallback 1)
    └── Google STT (Fallback 2)

[5] VOICE FILTERING
    ├── TV audio filtering
    ├── Wife/Glenda voice filtering
    ├── Background noise filtering
    └── Ultra-aggressive mode (primary active)

[6] TRANSCRIPTION CORRECTION
    ├── Detect transcription mistakes
    ├── Wrong word detection
    ├── Confidence scoring
    └── Manual correction support

[7] GRAMMARLY CLI/API INTEGRATION
    ├── Auto-accept corrections
    ├── Grammar checking
    ├── Spell checking
    └── Style suggestions

[8] TRANSCRIPT QUEUE
    ├── FIFO queue (priority-aware)
    ├── Control conflict prevention
    ├── Works with active agents
    └── Full-time listening

[9] PAUSE DETECTION
    ├── Dynamic pause threshold
    ├── Speech end detection
    ├── Activity tracking
    └── Auto-send trigger

[10] AUTO-SEND MONITOR
    ├── Pause threshold monitoring
    ├── Dynamic scaling
    ├── Keyboard activity tracking
    └── Auto-send after pause

[11] CURSOR IDE INTEGRATION
    ├── Chat field focus (Ctrl+L)
    ├── Text typing
    ├── Enter key press
    └── Works with active agents

[12] INTERRUPT/STOP/RESUME
    ├── F23 key handler (stop)
    ├── Cancel pending messages
    ├── Resume listening mode
    └── User control flags

[13] VOICE OUTPUT (TTS)
    ├── pyttsx3 (Local)
    ├── gTTS (Google)
    └── ElevenLabs (Natural voice)
```

---

## 🔄 Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    VOICE INPUT → CURSORIDE FLOW                         │
└─────────────────────────────────────────────────────────────────────────┘

[START] User speaks
    ↓
[1] Microphone captures audio (PyAudio)
    ↓
[2] Pre-buffer stores audio (ring buffer)
    ↓
[3] Wake word detection (Porcupine/Transcript)
    ↓
[4] VAD detects speech activity
    ↓
[5] Audio captured until silence (3s timeout)
    ↓
[6] Speech-to-text transcription (Whisper)
    ↓
[7] Voice filtering (TV/wife/background)
    ├── [FILTERED] → Stop, mark speech end, return
    └── [ALLOWED] → Continue
    ↓
[8] Transcription correction check
    ├── Low confidence → Flag for review
    └── High confidence → Continue
    ↓
[9] Queue transcript (VoiceTranscriptQueue)
    ├── Mark activity (auto-send monitor)
    └── Process in queue
    ↓
[10] Grammarly CLI/API processing
    ├── Auto-accept corrections
    ├── Apply grammar fixes
    └── Update transcript
    ↓
[11] Type transcript into chat field (Ctrl+L, type, DON'T send)
    ↓
[12] Mark speech end (auto-send monitor)
    ├── Start dynamic wait timer
    └── Monitor for pause
    ↓
[13] Pause detection (auto-send monitor)
    ├── Check pause threshold
    ├── Dynamic scaling
    └── Wait for sufficient pause
    ↓
[14] Auto-send trigger
    ├── Focus chat field (Ctrl+L)
    ├── Press Enter
    └── Send to CursorIDE
    ↓
[END] Message sent to active agent
```

---

## 🛠️ Subsystem Details

### 1. Voice Capture (`voice_interface_system.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- PyAudio capture (16kHz, mono, 16-bit)
- Pre-buffer (ring buffer, 1 second)
- Continuous streaming

**Key Methods:**
- `_pre_buffer_capture_loop()` - Real PyAudio capture
- `_get_buffered_audio()` - Get pre-buffered audio
- `_get_recent_buffered_audio()` - Get recent audio chunks

---

### 2. Wake Word Detection (`voice_interface_system.py`)

**Status:** ⚠️ PARTIAL  
**Components:**
- Porcupine (if available)
- Transcript-based fallback

**Key Methods:**
- `_check_wake_word_in_buffer()` - Check for wake word
- `_get_recent_buffered_audio()` - Get audio for detection

**Issues:**
- Porcupine not always available
- Transcript-based has latency

---

### 3. Voice Activity Detection (VAD) (`voice_interface_system.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- Energy-based detection
- Speech endpoint detection
- Silence timeout (3 seconds)

**Key Methods:**
- `_detect_voice_activity()` - Energy-based VAD
- `_listening_loop()` - VAD integration

---

### 4. Speech-to-Text Transcription (`voice_interface_system.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- Whisper (local) - Primary
- OpenAI Whisper API - Fallback 1
- Google STT - Fallback 2

**Key Methods:**
- `_transcribe_audio()` - Multi-method transcription

**Issues:**
- Needs Whisper model download
- API keys may be required

---

### 5. Voice Filtering (`voice_filter_system.py`)

**Status:** ✅ OPERATIONAL  
**Components:**
- TV audio filtering
- Wife/Glenda voice filtering
- Background noise filtering

**Integration:**
- Called from `voice_transcript_queue.py`
- `_filter_voice_transcript()` method

---

### 6. Transcription Correction

**Status:** ⚠️ NEEDS IMPLEMENTATION  
**Components:**
- Confidence scoring
- Wrong word detection
- Manual correction support

**Needs:**
- Confidence threshold checking
- User feedback mechanism
- Correction interface

---

### 7. Grammarly CLI/API Integration (`grammarly_ai_driven_cli.py`)

**Status:** ⚠️ NEEDS VERIFICATION  
**Components:**
- Auto-accept corrections
- Grammar checking
- Spell checking

**Integration:**
- Called from `voice_transcript_queue.py`
- `_handle_request()` method (line 477)

**Key Method:**
- `process_transcript()` - Process with Grammarly

**Issues:**
- Needs verification that it's working
- Auto-accept may need configuration

---

### 8. Transcript Queue (`voice_transcript_queue.py`)

**Status:** ✅ OPERATIONAL  
**Components:**
- FIFO queue (priority-aware)
- Control conflict prevention
- Full-time listening

**Key Methods:**
- `queue_voice_transcript()` - Queue transcript
- `_handle_request()` - Process request
- `_type_to_chat_field()` - Type into chat (don't send)

**Integration:**
- Calls `mark_activity()` (line 268)
- Calls `mark_speech_end()` (line 532)
- Calls Grammarly (line 477)

---

### 9. Pause Detection (`cursor_auto_send_monitor.py`)

**Status:** ⚠️ NOT WORKING PROPERLY  
**Components:**
- Dynamic pause threshold
- Speech end detection
- Activity tracking

**Key Methods:**
- `mark_activity()` - Mark user activity
- `mark_speech_end()` - Mark speech end
- `_monitor_loop()` - Monitor for pauses

**Issues:**
- Duplicate `main()` calls (lines 535-537)
- Pause detection may not trigger correctly
- Connection to voice input needs verification

---

### 10. Auto-Send Monitor (`cursor_auto_send_monitor.py`)

**Status:** ⚠️ NOT WORKING PROPERLY  
**Components:**
- Pause threshold monitoring
- Dynamic scaling
- Keyboard activity tracking

**Key Methods:**
- `_auto_send()` - Send message
- `_monitor_loop()` - Main monitoring loop
- `_adjust_pause_threshold()` - Dynamic scaling

**Issues:**
- Duplicate `main()` calls
- May not be detecting pauses correctly
- Auto-send may not trigger

---

### 11. Cursor IDE Integration (`voice_transcript_queue.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- Chat field focus (Ctrl+L)
- Text typing
- Enter key press

**Key Methods:**
- `_type_to_chat_field()` - Type into chat
- `_send_to_cursor_ide()` - Send message

---

### 12. Interrupt/Stop/Resume (`cursor_auto_send_monitor.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- F23 key handler (stop)
- Cancel pending messages
- Resume listening mode

**Key Methods:**
- `stop()` - Stop and cancel
- `cancel_pending_message()` - Cancel pending
- `resume_listening()` - Resume

**Integration:**
- F23 key handler (line 145)
- User control flags

---

### 13. Voice Output (TTS) (`jarvis_voice_interface.py`)

**Status:** ✅ IMPLEMENTED  
**Components:**
- pyttsx3 (Local)
- gTTS (Google)
- ElevenLabs (Natural voice)

**Key Methods:**
- `speak()` - Text-to-speech

---

## 🔧 Integration Points

### Voice Input → Transcript Queue

**Connection:** ✅ WORKING
- `voice_interface_system.py` → `queue_voice_transcript()`
- Line 264 in `voice_interface_system.py`

### Transcript Queue → Auto-Send Monitor

**Connection:** ⚠️ NEEDS FIXING
- `mark_activity()` called (line 268)
- `mark_speech_end()` called (line 532)
- Auto-send monitor may not be detecting pauses correctly

### Transcript Queue → Grammarly

**Connection:** ⚠️ NEEDS VERIFICATION
- `process_transcript()` called (line 477)
- Auto-accept enabled
- Needs verification that it's working

### Auto-Send Monitor → Cursor IDE

**Connection:** ⚠️ NEEDS FIXING
- `_auto_send()` method (line 371)
- May not be triggering correctly
- Needs pause detection fix

---

## 🐛 Known Issues

### 1. Auto-Send Not Working

**Problem:**
- Auto-send monitor not detecting pauses
- Auto-send not triggering after pause

**Root Causes:**
- Duplicate `main()` calls in `cursor_auto_send_monitor.py` (lines 535-537)
- Pause detection may not be connected properly
- `mark_speech_end()` may not be triggering auto-send

**Fix Required:**
- Remove duplicate `main()` calls
- Verify pause detection logic
- Ensure `mark_speech_end()` triggers auto-send

---

### 2. Pause Detection Not Working

**Problem:**
- Pause detection not detecting speech end
- Dynamic threshold not adjusting

**Root Causes:**
- `mark_speech_end()` may not be called correctly
- Pause threshold calculation may be wrong
- Monitor loop may not be checking correctly

**Fix Required:**
- Verify `mark_speech_end()` is called after transcription
- Check pause threshold calculation
- Verify monitor loop logic

---

### 3. Grammarly Integration

**Problem:**
- Grammarly may not be processing transcripts
- Auto-accept may not be working

**Fix Required:**
- Verify `grammarly_ai_driven_cli.py` is working
- Check auto-accept configuration
- Test Grammarly processing

---

### 4. Transcription Correction

**Problem:**
- No mechanism for handling transcription mistakes
- Wrong words not detected/corrected

**Fix Required:**
- Add confidence threshold checking
- Add wrong word detection
- Add correction interface

---

## ✅ Next Steps

1. **Fix Auto-Send Monitor**
   - Remove duplicate `main()` calls
   - Fix pause detection logic
   - Verify auto-send trigger

2. **Fix Pause Detection**
   - Verify `mark_speech_end()` integration
   - Check pause threshold calculation
   - Test pause detection

3. **Verify Grammarly Integration**
   - Test `grammarly_ai_driven_cli.py`
   - Verify auto-accept
   - Check processing flow

4. **Add Transcription Correction**
   - Implement confidence checking
   - Add wrong word detection
   - Create correction interface

5. **Test End-to-End Flow**
   - Test complete voice input flow
   - Verify all integration points
   - Test interrupt/stop/resume

---

**Tags:** `#JARVIS_VOICE` `#SUBSYSTEM_MAP` `#INTEGRATION` `@JARVIS` `@LUMINA`
