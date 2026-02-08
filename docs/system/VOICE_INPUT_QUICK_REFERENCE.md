# Voice Input Quick Reference

## 🚨 EMERGENCY MUTE (Background Voice Bleeding)

**Press `Ctrl+RAlt`** to instantly mute/unmute voice input.

This prevents background conversation (wife, kids, TV) from being transcribed into your chat.

---

## Hotkeys

| Key Combo | Action |
|-----------|--------|
| **RAlt (tap)** | Send `@doit` command |
| **RAlt (hold 400ms+)** | Toggle voice input on/off |
| **Ctrl+RAlt** | **QUICK MUTE** - Emergency stop background transcription |
| **F23/Copilot** | New Agent Chat |

---

## Voice Commands (Dragon NaturallySpeaking Style)

### Send Commands
- **"Jarvis, do it"** → Send message NOW (overrides auto-send timer)
- **"Send it"** → Send message
- **"Do it"** → Send message

### Correction Commands (Cancels auto-send timer)
- **"Scratch that"** → Undo last utterance (Ctrl+Z)
- **"Clear all"** → Clear entire input
- **"Go back"** → Backspace
- **"New line"** → Insert line break

### Control Commands
- **"Stop listening"** → Pause voice recognition
- **"Wake up"** → Resume voice recognition

---

## Voice Filtering (Prevents Background Bleed)

The system uses **adaptive noise filtering**:

1. **Energy Threshold**: Only captures loud/close speech (4000+)
2. **Ambient Noise Calibration**: Automatically adjusts to room noise
3. **Dynamic Threshold**: Adapts as noise levels change
4. **Quiet Audio Rejection**: Rejects audio below threshold (likely background)

### If Background Voices Still Bleed Through:

1. **Press `Ctrl+RAlt`** to mute immediately
2. Increase `energy_threshold` in `config/jarvis_voice_commands.json`:
   ```json
   "energy_threshold": 6000  // Higher = more selective
   ```
3. Move microphone closer or use push-to-talk mode

---

## Integration with Auto-Send Monitor

- **Correction commands** automatically cancel pending auto-send timers
- **"Jarvis, do it"** overrides the timer for immediate send
- Activity is marked to reset pause detection after corrections

---

## Troubleshooting

### Voice Not Working
- Check microphone permissions in Windows Settings
- Verify `Ctrl+Shift+Space` opens voice input in Cursor
- Check if voice is muted (`Ctrl+RAlt` to toggle)

### Too Much Background Noise
- Increase `energy_threshold` in config
- Use `Ctrl+RAlt` to mute when not speaking
- Consider using push-to-talk (RAlt hold) instead of always-on

### Voice Commands Not Recognized
- Speak clearly and close to microphone
- Check internet connection (uses Google Speech Recognition)
- Review `data/voice_commands/command_log.jsonl` for recognition results

---

## Files

- **AHK Script**: `scripts/autohotkey/ralt_jarvis.ahk`
- **Voice Trigger**: `scripts/python/jarvis_voice_trigger.py`
- **Config**: `config/jarvis_voice_commands.json`
- **Logs**: `data/voice_commands/command_log.jsonl`
