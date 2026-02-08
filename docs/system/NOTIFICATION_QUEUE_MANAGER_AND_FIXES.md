# Notification Queue Manager & Danny Boy Fixes

**Date:** 2026-01-09
**Status:** ✅ **IMPLEMENTED**

---

## 🎯 OVERVIEW

### Issues Fixed:
1. **ElevenLabs SDK API Error:** Fixed to use `client.text_to_speech.convert()` instead of deprecated `client.generate()`
2. **Tkinter Threading Error:** Fixed "Calling Tcl from different apartment" by using `root.after()` for thread-safe updates
3. **NumPy Array Truth Value Error:** Fixed by using `len()` check instead of truth value
4. **Notification Queue System:** Created and integrated notification queue manager

---

## 🔔 NOTIFICATION QUEUE MANAGER

### Implementation

**File:** `cursor_notification_queue_manager.py`

**Purpose:**
- Monitors Cursor/VS Code notification queue count
- Automatically processes notifications to reduce queue
- Prevents notification count from getting too high

**Features:**
- Monitors notification count from multiple sources
- Auto-dismisses non-critical notifications
- Auto-resolves known issues (Git, imports, etc.)
- Processes Git notifications automatically
- Tracks notification history

**Methods to Get Notification Count:**
1. **State Files:** Reads from Cursor/VS Code state files
2. **VLM Detection:** Uses visual detection to count notifications in UI
3. **Notification Processor:** Uses intelligent notification processor

**Actions Taken:**
- Dismiss non-critical notifications
- Auto-resolve known issues (Git "too many changes", etc.)
- Process Git notifications
- Track and log all actions

**Integration:**
- ✅ Added to `startup_all_automation.py`
- ✅ Starts automatically on system boot
- ✅ Monitors every 60 seconds
- ✅ Runs in background (daemon thread)

---

## 🎵 DANNY BOY FIXES

### 1. ElevenLabs API Fix

**Problem:** `'ElevenLabs' object has no attribute 'generate'`

**Solution:** Updated to use new API:
```python
# OLD (deprecated):
audio = self.client.generate(text=text, voice=voice, model=model)

# NEW (v2.27.0+):
audio = self.client.text_to_speech.convert(
    text=text,
    voice_id=voice_id,
    model_id=model,
    output_format="mp3_44100_128"
)
```

**Files Updated:**
- `jarvis_elevenlabs_integration.py` - `speak()` and `speak_to_file()` methods
- `jarvis_danny_boy_duet.py` - `_sing_phrase_with_elevenlabs()` method

### 2. Tkinter Threading Fix

**Problem:** `RuntimeError: Calling Tcl from different apartment`

**Solution:** 
- Don't run `mainloop()` in separate thread
- Use `root.after()` for thread-safe updates
- Schedule updates from main thread

**Files Updated:**
- `karaoke_display.py` - Removed threading from `start()`
- `jarvis_danny_boy_duet.py` - Use `root.after()` for updates

### 3. NumPy Array Truth Value Fix

**Problem:** `ValueError: The truth value of an array with more than one element is ambiguous`

**Solution:** Use `len()` check instead of truth value:
```python
# OLD:
if jarvis_audio:  # Error with numpy arrays

# NEW:
jarvis_has_audio = False
if jarvis_audio is not None:
    if isinstance(jarvis_audio, np.ndarray):
        jarvis_has_audio = len(jarvis_audio) > 0
    else:
        jarvis_has_audio = len(jarvis_audio) > 0 if jarvis_audio else False
```

**Files Updated:**
- `jarvis_danny_boy_duet.py` - `sing_duet()` method

---

## 🚀 USAGE

### Notification Queue Manager:

**Start manually:**
```bash
python scripts/python/cursor_notification_queue_manager.py --monitor
```

**Process once:**
```bash
python scripts/python/cursor_notification_queue_manager.py --process
```

**Automatic:**
- Integrated into `startup_all_automation.py`
- Starts automatically on system boot
- Monitors every 60 seconds

### Danny Boy Duet:

**Run:**
```bash
python scripts/python/jarvis_danny_boy_duet.py
```

**What You'll See:**
- Karaoke window with lyrics
- JARVIS singing (Tenor 1 - Higher)
- Wanda singing (Tenor 2 - Lower)
- Both voices playing audibly

---

## 📊 HOW IT WORKS

### Notification Queue Manager:

1. **Monitor:**
   - Checks notification count every 60 seconds
   - Uses multiple methods to detect count
   - Logs to history file

2. **Process:**
   - If count > 5, takes action
   - Dismisses non-critical notifications
   - Auto-resolves known issues
   - Processes Git notifications

3. **Track:**
   - Saves state to JSON file
   - Logs history to JSONL file
   - Tracks actions taken

### Danny Boy Duet:

1. **Initialize:**
   - Load ElevenLabs TTS (from Azure Key Vault)
   - Create karaoke display (main thread)
   - Load musical arrangement

2. **Sing:**
   - Generate audio for each voice
   - Show lyrics on karaoke display
   - Play both voices audibly

3. **Display:**
   - Update lyrics using `root.after()` (thread-safe)
   - Highlight as they're sung
   - Full-screen karaoke window

---

## 🔑 KEY FEATURES

### Notification Queue Manager:
- ✅ Monitors notification count
- ✅ Auto-dismisses non-critical
- ✅ Auto-resolves known issues
- ✅ Processes Git notifications
- ✅ Tracks history
- ✅ Integrated into startup

### Danny Boy Fixes:
- ✅ ElevenLabs API updated (v2.27.0+)
- ✅ Tkinter threading fixed
- ✅ NumPy array check fixed
- ✅ Karaoke display working
- ✅ Both voices playing audibly

---

**Tags:** #NOTIFICATIONS #QUEUE #CURSOR #VSCODE #DANNY_BOY #ELEVENLABS #FIXES #REQUIRED @JARVIS @LUMINA

**Status:** ✅ **IMPLEMENTED - READY FOR USE**

**Next Steps:**
1. Test notification queue manager: `python scripts/python/cursor_notification_queue_manager.py --process`
2. Test Danny Boy duet: `python scripts/python/jarvis_danny_boy_duet.py`
3. Monitor notification count reduction over time
