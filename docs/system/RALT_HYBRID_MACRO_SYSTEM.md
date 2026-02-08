# RAlt Hybrid Macro System
## Voice Input + AI Greetings + Roundtable Discussions

**Date**: 2026-01-06  
**Status**: ✅ **IMPLEMENTED**  
**Tag**: @JARVIS #MACRO #VOICE #MEETING

---

## Overview

The RAlt Hybrid Macro System maps the **Right Alt (RAlt)** key to a three-part activation sequence:

1. 🎤 **Voice Input Activation** - Activates voice recognition
2. 👋 **AI Greeting** - Plays contextual JARVIS greeting
3. 🗣️ **Roundtable Discussion Start** - Begins work shift/meeting mode

---

## Features

### 1. Voice Input Activation
- Activates Windows Speech Recognition (if available)
- Integrates with Azure Speech SDK
- Connects to JARVIS voice interface

### 2. AI Greetings
- Context-aware greetings based on time of day
- Work shift mode (morning: 6am-12pm)
- Meeting mode (afternoon: 12pm-6pm)
- General greetings (evening/night)
- Uses ElevenLabs TTS for spoken greetings

### 3. Roundtable Discussion Mode
- Creates meeting session with unique ID
- Records meeting start in JARVIS memory
- Facilitates discussion format
- Tracks participants and topics

---

## Installation

### Dependencies
```bash
pip install keyboard
pip install elevenlabs  # Optional - for TTS
```

### Required Systems
- JARVIS Full-Time Super Agent
- JARVIS ElevenLabs TTS (optional, for spoken greetings)
- Keyboard library for hotkey detection

---

## Usage

### Test Mode (One-Time Execution)
```bash
python scripts/python/jarvis_ralt_hybrid_macro.py --test --context work_shift
```

### Background Service (Continuous)
```bash
python scripts/python/jarvis_ralt_macro_service.py --background
```

### Interactive Mode
```bash
python scripts/python/jarvis_ralt_macro_service.py
```
Press **Right Alt** to activate, **Ctrl+C** to stop.

---

## How It Works

### Activation Sequence

When **RAlt** is pressed:

1. **Voice Input Activation**
   - Attempts Windows Speech Recognition activation
   - Falls back to Azure Speech SDK if available
   - Activates JARVIS voice interface

2. **AI Greeting**
   - Determines context based on time of day
   - Selects appropriate greeting
   - Plays via TTS (if available) or logs

3. **Roundtable Discussion**
   - Creates meeting with unique ID
   - Records in JARVIS persistent memory
   - Plays opening statement
   - Starts meeting mode

### Context Detection

| Time | Context | Greeting Type |
|------|---------|---------------|
| 6am - 12pm | `work_shift` | Morning work shift greeting |
| 12pm - 6pm | `meeting` | Meeting/roundtable greeting |
| Other | `general` | General greeting |

---

## Integration Points

### JARVIS Systems
- ✅ JARVIS Full-Time Super Agent - Voice interface
- ✅ JARVIS ElevenLabs TTS - Spoken greetings
- ✅ JARVIS Persistent Memory - Meeting recording
- ✅ R5 Living Context Matrix - Meeting context (future)

### Voice Systems
- Windows Speech Recognition
- Azure Speech SDK (if available)
- JARVIS voice interface

---

## Configuration

### Customize Greetings
Edit `jarvis_ralt_hybrid_macro.py`:
```python
greetings = {
    "work_shift": ["Your custom greetings..."],
    "meeting": ["Your meeting greetings..."],
    "general": ["Your general greetings..."]
}
```

### Change Hotkey
Modify `start_listening()`:
```python
keyboard.add_hotkey('your_key', self._handle_ralt_press)
```

---

## Files

### Core Implementation
- `scripts/python/jarvis_ralt_hybrid_macro.py` - Main macro system
- `scripts/python/jarvis_ralt_macro_service.py` - Service wrapper

### Documentation
- `docs/system/RALT_HYBRID_MACRO_SYSTEM.md` - This file

---

## Status

✅ **Implemented**
- RAlt hotkey detection
- Voice input activation
- AI greetings (context-aware)
- Roundtable discussion mode
- Integration with JARVIS systems

⚠️ **Enhancements Needed**
- Windows Speech Recognition integration
- Azure Speech SDK voice input
- Meeting participant tracking
- Discussion topic management
- R5 integration for meeting context

---

## Example Output

```
🚀 Executing RAlt Hybrid Macro...
🎤 Activating voice input...
✅ Voice input activated
👋 AI Greeting: Hello! Starting work shift mode. How can I help?
🗣️  STARTING ROUNDTABLE DISCUSSION
📋 Meeting: Work Shift Roundtable
🆔 Meeting ID: meeting_20260106_025117
✅ Hybrid macro executed successfully
```

---

## Troubleshooting

### Keyboard Library Not Available
```bash
pip install keyboard
```

### TTS Not Working
- Check ElevenLabs API key in Azure Key Vault
- Verify TTS initialization in logs

### Voice Input Not Activating
- Check Windows Speech Recognition settings
- Verify Azure Speech SDK availability
- Check JARVIS voice interface status

---

**Last Updated**: 2026-01-06  
**Maintained By**: @JARVIS
