# 🔄 MANUS Chained Ask Cycle

## Overview

Continuous conversation loops orchestrated by MANUS:

```
🎤 LISTEN → 📝 TRANSCRIBE → 🧠 PROCESS → ⚡ EXECUTE → 🔊 RESPOND → 🔄 LOOP
```

No manual triggers needed. Speak naturally and JARVIS handles everything automatically.

## How It Works

```
┌─────────────────────────────────────────┐
│  🎤 LISTENING (Always Open Mic)         │
│  └→ Speech detected                     │
│     └→ 📝 TRANSCRIBE (Azure Speech)     │
│        └→ Text received                 │
│           └→ 🧠 PROCESS (Intent Parse)  │
│              └→ Command identified      │
│                 └→ ⚡ EXECUTE (Cursor)   │
│                    └→ Action completed  │
│                       └→ 🔊 RESPOND     │
│                          └→ Speech out  │
│                             └→ 🔄 LOOP  │
└─────────────────────────────────────────┘
```

## Quick Start

```bash
python scripts/python/manus_chained_ask_cycle.py
```

This starts:
- **Always-listening microphone** (continuously open)
- **Real-time transcription** (Azure Speech SDK)
- **Intelligent command processing**
- **Automatic Cursor IDE control** (keyboard shortcuts)
- **Voice responses** (Azure TTS)
- **Auto-recycling** (when Cursor needs refresh)

## Features

✅ **Continuous Listening** - Mic is always open  
✅ **Chained Cycles** - Each response leads to next listen  
✅ **Hands-Free** - No clicking, no button presses  
✅ **Keyboard First** - Primary control via shortcuts  
✅ **Mouse Fallback** - Backup if keyboard fails  
✅ **Auto-Recycle** - Cursor refreshed when needed  
✅ **Voice Feedback** - JARVIS speaks responses  

## Cycle States

| State | Description |
|-------|-------------|
| LISTENING | Mic open, waiting for speech |
| TRANSCRIBING | Converting speech to text |
| PROCESSING | Parsing intent from text |
| EXECUTING | Running action in Cursor |
| RESPONDING | Speaking response |
| WAITING | Brief pause before next cycle |
| IDLE | System stopped |

## Commands

### Stop Commands
- "goodbye JARVIS"
- "stop listening"
- "exit"
- "quit"

### Cursor Control Commands
- "open chat" - Opens Cursor chat (Ctrl+L)
- "open file" - Opens file dialog (Ctrl+P)
- "save file" - Saves current file (Ctrl+S)
- "format code" - Formats document
- "toggle terminal" - Opens/closes terminal
- "go to definition" - Navigates to definition
- "start debug" - Starts debugging
- "open composer" - Opens Cursor Composer

### System Commands
- "recycle cursor" - Warm recycles Cursor IDE
- "restart cursor" - Same as recycle
- "refresh cursor" - Same as recycle

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    MANUS Chained Ask Cycle                    │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────┐     ┌────────────────────────────────┐  │
│  │ Always         │────▶│ Hands-Free Cursor Control      │  │
│  │ Listening      │     │ - Keyboard shortcuts (primary) │  │
│  │ (Azure Speech) │     │ - Mouse control (fallback)     │  │
│  └────────────────┘     └────────────────────────────────┘  │
│          │                           │                       │
│          ▼                           ▼                       │
│  ┌────────────────┐     ┌────────────────────────────────┐  │
│  │ Voice Response │     │ Intelligent Warm Recycle       │  │
│  │ (Azure TTS)    │     │ - Memory monitoring            │  │
│  └────────────────┘     │ - CPU monitoring               │  │
│                         │ - Auto-recycle when needed     │  │
│                         └────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Integration with MANUS MCP Server

The Dockerfile has been updated to include chained ask cycle scripts:

```dockerfile
# Copy Chained Ask Cycle and related scripts
COPY scripts/python/manus_chained_ask_cycle.py /app/scripts/python/
COPY scripts/python/jarvis_always_listening.py /app/scripts/python/
COPY scripts/python/jarvis_hands_free_cursor_control.py /app/scripts/python/
COPY scripts/python/cursor_intelligent_warm_recycle.py /app/scripts/python/
```

## Configuration

```python
config = {
    "auto_recycle_check_interval": 120,  # seconds
    "response_delay": 0.5,               # seconds between cycles
    "max_silence_before_prompt": 30,     # seconds
    "enable_proactive_suggestions": True,
}
```

## Example Session

```
🔄 Starting MANUS Chained Ask Cycle...
   ┌─────────────────────────────────┐
   │  🎤 LISTENING                   │
   │  └→ 📝 TRANSCRIBE              │
   │     └→ 🧠 PROCESS              │
   │        └→ ⚡ EXECUTE           │
   │           └→ 🔊 RESPOND        │
   │              └→ 🔄 LOOP        │
   └─────────────────────────────────┘

   Speak naturally - I'm always listening.
   Say 'goodbye JARVIS' to stop.

🗣️  You said: "Open chat"
🔄 Cycle 0: Processing "Open chat"
   ↪️ Response: "Opening Cursor chat for you."
🔊 JARVIS: "Opening Cursor chat for you."

🗣️  You said: "Help me with this code"
🔄 Cycle 1: Processing "Help me with this code"
   ↪️ Response: "Opening chat so we can discuss that."
🔊 JARVIS: "Opening chat so we can discuss that."

🗣️  You said: "Goodbye JARVIS"
🛑 Stopping MANUS Chained Ask Cycle...
✅ Stopped after 2 cycles
```

## Files

- `manus_chained_ask_cycle.py` - Main orchestrator
- `jarvis_always_listening.py` - Continuous speech recognition
- `jarvis_hands_free_cursor_control.py` - Cursor IDE control
- `cursor_intelligent_warm_recycle.py` - Auto-recycle system

## Requirements

- Azure Speech SDK credentials (in Key Vault)
- `pynput` for keyboard control
- `pygetwindow` for window management
- Cursor IDE running

## Troubleshooting

### No Speech Recognition
- Check Azure Speech credentials
- Verify microphone is working
- Check audio device settings

### Commands Not Executing
- Ensure Cursor window is active
- Check keyboard shortcuts are correct
- Try mouse fallback

### Cycle Stuck
- Say "stop listening" to stop
- Press Ctrl+C to force stop
- Check logs for errors

---

**Created**: 2025-12-31  
**Status**: ✅ Operational  
**Mode**: Continuous Chained Cycles
