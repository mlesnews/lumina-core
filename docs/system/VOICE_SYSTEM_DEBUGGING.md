# Voice System Debugging Guide

**Date:** 2026-01-13  
**Issue:** "Hey JARVIS, test." - Nothing happens

---

## 🔍 Problem Analysis

### User Report
- User said "Hey JARVIS, test." with `::handsfree::` prefix
- **Result:** Nothing happened

### Potential Issues

1. **Voice Interface Not Running**
   - The voice interface system might not be started
   - Check: `python voice_interface_system.py --status`

2. **Wake Word Detection Not Working**
   - "Hey JARVIS" might not be detected
   - Porcupine might not be initialized
   - Transcript-based fallback might not be working

3. **Chat Field Not Focused**
   - After removing Ctrl+L, chat field might not be focused
   - Typing won't work if chat isn't focused
   - Need alternative focus method

4. **Auto-Send Monitor Not Running**
   - Monitor might not be started
   - Pause detection might not be working

---

## ✅ Verification Steps

### Step 1: Check Voice Interface Status

```bash
cd "c:\Users\mlesn\Dropbox\my_projects\.lumina\scripts\python"
python voice_interface_system.py --status
```

**Expected Output:**
```
🎤 Voice Interface Status
============================================================
State: LISTENING
Listening: True
Wake Word Detected: False
Current Conversation: None
```

### Step 2: Start Voice Interface (if not running)

```bash
python voice_interface_system.py --start
```

**Expected Output:**
```
✅ Voice interface started
   Say 'Hey JARVIS' to start conversation
   Press Ctrl+C to stop
```

### Step 3: Check Auto-Send Monitor

```python
from cursor_auto_send_monitor import get_auto_send_monitor
monitor = get_auto_send_monitor()
print(f"Running: {monitor.running}")
print(f"Pause threshold: {monitor.pause_threshold}")
```

### Step 4: Check Transcript Queue

```python
from voice_transcript_queue import get_voice_transcript_queue
queue = get_voice_transcript_queue()
print(f"Processing: {queue.processing}")
print(f"Queue size: {queue.request_queue.qsize()}")
```

---

## 🔧 Fixes Applied

### Fix 1: Chat Field Focus (Alternative Method)

**Problem:** Ctrl+L was removed to prevent layout switching, but chat field needs to be focused.

**Solution:** Use Tab key to navigate to chat field instead of Ctrl+L.

**Code Change:**
```python
# Try using Tab to navigate to chat (if it's the next focusable element)
# This is safer than Ctrl+L which switches layouts
keyboard.press_and_release('tab')
time.sleep(0.1)
```

**Location:** `voice_transcript_queue.py` - `_type_to_chat_field()` method

---

## 🧪 Testing Checklist

- [ ] Voice interface is running (`--status` shows `Listening: True`)
- [ ] Wake word detection is working (say "Hey JARVIS" and check logs)
- [ ] Transcription is working (check for transcript in logs)
- [ ] Chat field is focused (Tab navigation works)
- [ ] Text is typed into chat field (check Cursor IDE)
- [ ] Auto-send monitor is running (check `monitor.running`)
- [ ] Pause detection works (wait for pause threshold)
- [ ] Message is sent (check Cursor IDE chat)

---

## 📝 Debugging Commands

### Check All Components

```python
# Check voice interface
from voice_interface_system import get_voice_interface
voice = get_voice_interface()
print(f"Listening: {voice.listening_active}")
print(f"State: {voice.state}")

# Check transcript queue
from voice_transcript_queue import get_voice_transcript_queue
queue = get_voice_transcript_queue()
print(f"Processing: {queue.processing}")

# Check auto-send monitor
from cursor_auto_send_monitor import get_auto_send_monitor
monitor = get_auto_send_monitor()
print(f"Running: {monitor.running}")
print(f"Has pending: {monitor.has_pending_message}")
```

### Manual Test Flow

1. **Start voice interface:**
   ```bash
   python voice_interface_system.py --start
   ```

2. **Say "Hey JARVIS, test"**

3. **Check logs for:**
   - Wake word detected
   - Voice command captured
   - Transcript generated
   - Transcript queued
   - Text typed to chat
   - Auto-send triggered

4. **Check Cursor IDE:**
   - Is text in chat field?
   - Was message sent?

---

## 🐛 Common Issues

### Issue 1: Voice Interface Not Running

**Symptom:** Nothing happens when you speak.

**Fix:** Start voice interface:
```bash
python voice_interface_system.py --start
```

### Issue 2: Wake Word Not Detected

**Symptom:** Voice interface is running but doesn't respond to "Hey JARVIS".

**Fix:** 
- Check Porcupine initialization
- Check transcript-based fallback
- Verify wake word is "hey jarvis" (case-insensitive)

### Issue 3: Chat Field Not Focused

**Symptom:** Text is typed but not in chat field.

**Fix:** 
- Use Tab to navigate to chat
- Manually focus chat field before speaking
- Check if Tab navigation works

### Issue 4: Auto-Send Not Working

**Symptom:** Text is in chat but not sent.

**Fix:**
- Check if auto-send monitor is running
- Check pause threshold
- Verify `mark_speech_end()` is called

---

**Tags:** `#JARVIS_VOICE` `#DEBUGGING` `#TROUBLESHOOTING` `@JARVIS` `@LUMINA`
