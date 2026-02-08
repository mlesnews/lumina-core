# Passive/Active Voice Listening System

**Date**: 2026-01-14  
**Status**: ✅ **IMPLEMENTED**  
**Tags**: `#VOICE_INPUT` `#PASSIVE_LISTENING` `#ACTIVE_LISTENING` `#TRANSCRIPTION_EDITING` `#RSI` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Overview

**Complete hands-free voice system** with:
- **PASSIVE MODE**: Always listening for trigger word (low CPU, filters everything)
- **ACTIVE MODE**: After trigger word, actively transcribes to Cursor IDE
- **VOICE EDITING**: Fix transcription mistakes using voice commands

**Perfect for RSI**: Zero typing required - everything by voice!

---

## 🎤 How It Works

### Passive Mode (Always On)

**Behavior**:
- 👂 Always listening (low CPU usage)
- 🔇 Filters out all normal conversation
- 🎯 Only responds to trigger words
- ⚡ Low resource usage

**Trigger Words** (default):
- "Hey Jarvis" (primary)
- "Jarvis"
- "Hey Cursor"

**When Trigger Detected**:
- ✅ Switches to ACTIVE mode
- ✅ Starts transcribing to Cursor IDE

---

### Active Mode (After Trigger)

**Behavior**:
- 🎤 Actively transcribes all speech
- 📝 Types transcription into Cursor IDE
- ✏️ Allows voice editing commands
- 🚀 Can send message by voice

**Voice Editing Commands**:
- **"Scratch that"** → Delete last phrase
- **"Change [word] to [word]"** → Replace word
- **"Delete [word]"** → Remove word
- **"Add [text]"** → Insert text
- **"Clear all"** → Clear entire transcription
- **"New line"** → Insert line break
- **"Send it"** → Send message
- **"Stop listening"** → Return to passive mode

---

## 🚀 Quick Start

### Start the System

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts\python\passive_active_voice_system.py
```

### Custom Trigger Words

```powershell
python scripts\python\passive_active_voice_system.py --trigger-words "hey cursor" "jarvis" "activate"
```

---

## 📋 Usage Workflow

### Step 1: Start System

1. Run the script (starts in PASSIVE mode)
2. System is listening for trigger word
3. Normal conversation is ignored

### Step 2: Activate (Say Trigger Word)

1. Say: **"Hey Jarvis"** (or "Jarvis")
2. System switches to ACTIVE mode
3. Ready to transcribe

### Step 3: Speak Your Message

1. Speak naturally
2. Transcription appears in Cursor IDE
3. Can use voice commands to edit

### Step 4: Edit Mistakes (Voice Commands)

**If you make a mistake**:
- Say: **"Scratch that"** → Deletes last phrase
- Say: **"Change hello to hi"** → Replaces word
- Say: **"Delete that"** → Removes word
- Say: **"Add please"** → Inserts text

### Step 5: Send Message

1. Say: **"Send it"** (or "Do it", "Execute")
2. Message is sent
3. System returns to PASSIVE mode

### Step 6: Return to Passive

- Say: **"Stop listening"** → Returns to passive mode
- Or automatically after sending

---

## 🎯 Voice Commands Reference

### Editing Commands

| Command | Action |
|---------|--------|
| "Scratch that" | Delete last phrase |
| "Undo that" | Delete last phrase |
| "Delete that" | Delete last phrase |
| "Clear all" | Clear entire transcription |
| "Start over" | Clear entire transcription |
| "Delete [word]" | Remove specific word |
| "Change [word] to [word]" | Replace word |
| "Replace [word] with [word]" | Replace word |
| "Add [text]" | Insert text |
| "Insert [text]" | Insert text |
| "New line" | Insert line break |

### Control Commands

| Command | Action |
|---------|--------|
| "Send it" | Send message |
| "Do it" | Send message |
| "Execute" | Send message |
| "Stop listening" | Return to passive mode |
| "Pause" | Return to passive mode |
| "Resume" | Return to active mode |
| "Wake up" | Return to active mode |

---

## 💡 Example Usage

### Example 1: Basic Message

```
[PASSIVE MODE - waiting]
You: "Hey Jarvis"
System: ✅ ACTIVE MODE ACTIVATED

You: "Create a new file called test.py"
System: [Types: "Create a new file called test.py"]

You: "Send it"
System: [Sends message, returns to PASSIVE]
```

### Example 2: Editing Mistakes

```
[ACTIVE MODE]
You: "Create a new file called test.py"
System: [Types: "Create a new file called test.py"]

You: "Scratch that"
System: [Deletes: "Create a new file called test.py"]

You: "Create a new Python file called test.py"
System: [Types: "Create a new Python file called test.py"]

You: "Change Python to JavaScript"
System: [Changes to: "Create a new JavaScript file called test.py"]

You: "Send it"
System: [Sends message]
```

### Example 3: Complex Editing

```
[ACTIVE MODE]
You: "Add a function that calculates the sum"
System: [Types: "Add a function that calculates the sum"]

You: "Add of two numbers"
System: [Adds: "Add a function that calculates the sum of two numbers"]

You: "Change sum to product"
System: [Changes to: "Add a function that calculates the product of two numbers"]

You: "Delete Add"
System: [Removes "Add": "a function that calculates the product of two numbers"]

You: "Send it"
System: [Sends message]
```

---

## 🔧 Configuration

### Default Settings

- **Trigger Words**: `["hey jarvis", "jarvis", "hey cursor"]`
- **Wake Word**: `"hey jarvis"` (primary)
- **Deactivate Word**: `"stop listening"`
- **Energy Threshold**: 4000 (filters quiet background)
- **Pause Threshold**: 0.8 seconds
- **Phrase Time Limit**: 10 seconds

### Customization

Edit `passive_active_voice_system.py`:

```python
system = PassiveActiveVoiceSystem(
    trigger_words=["hey cursor", "jarvis", "activate"],
    wake_word="hey cursor",
    deactivate_word="stop listening"
)
```

---

## 🎯 Benefits for RSI

### Zero Typing Required

✅ **Trigger activation**: Say "Hey Cursor" (no typing)  
✅ **Transcription**: All speech transcribed automatically  
✅ **Editing**: Voice commands fix mistakes  
✅ **Sending**: Voice command sends message  

### Hands-Free Operation

- **No keyboard use**: Everything by voice
- **No mouse use**: Voice commands handle everything
- **Rest hands**: Keep hands off keyboard entirely
- **Better posture**: Voice allows better positioning

---

## 🚨 Troubleshooting

### System Not Responding

**Check**:
1. Script is running
2. Microphone is working
3. Speech recognition is working

**Test**:
```powershell
# Test microphone
python -c "import speech_recognition as sr; r = sr.Recognizer(); print('✅ Microphone OK')"
```

### Trigger Word Not Detected

**Solutions**:
1. Speak clearly and loudly
2. Check microphone sensitivity
3. Try different trigger words
4. Adjust energy threshold

### Transcription Not Appearing

**Check**:
1. Cursor IDE is focused
2. Chat field is active
3. pyautogui is working

**Test**:
```powershell
python -c "import pyautogui; pyautogui.write('test'); print('✅ pyautogui OK')"
```

### Editing Commands Not Working

**Check**:
1. Say command clearly
2. Use exact phrase (see reference)
3. Check transcription buffer has content

---

## 📝 Integration

### With F23 Key

**Option 1**: Use F23 to activate voice input, then use passive system for editing

**Option 2**: Use passive system for everything (no F23 needed)

### With AutoHotkey

Can run alongside AutoHotkey scripts:
- F23 → Quick voice input
- Passive system → Always-on listening

---

## 🎯 Next Steps

1. **Start System**: Run `passive_active_voice_system.py`
2. **Test Trigger**: Say "Hey Cursor"
3. **Test Transcription**: Speak a message
4. **Test Editing**: Say "Scratch that"
5. **Test Sending**: Say "Send it"

---

**Status**: ✅ **IMPLEMENTED**  
**File**: `scripts/python/passive_active_voice_system.py`  
**Usage**: `python scripts/python/passive_active_voice_system.py`  
**Tags**: `#VOICE_INPUT` `#PASSIVE_LISTENING` `#ACTIVE_LISTENING` `#TRANSCRIPTION_EDITING` `#RSI` `@LUMINA` `@JARVIS` `#PEAK`
