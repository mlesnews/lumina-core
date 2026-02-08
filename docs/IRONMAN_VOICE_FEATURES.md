# 🎤 IRON MAN Virtual Assistant - Voice & Listening Features

**Date**: 2025-01-24  
**Status**: ✅ **IMPLEMENTED**  
**Version**: 1.0.0

---

## Overview

The IRON MAN Virtual Assistant now includes comprehensive voice and listening capabilities, allowing hands-free interaction through speech recognition and voice commands.

---

## ✨ Voice Features

### Speech Recognition (Listening)

- ✅ **Microphone Input** - Listens to your voice commands
- ✅ **Wake Word Detection** - Responds to "Hey Jarvis" or "Hey Iron Man"
- ✅ **Continuous Listening** - Background wake word monitoring
- ✅ **Manual Trigger** - Click IRON MAN to start listening
- ✅ **Visual Feedback** - Arc reactor turns yellow when listening
- ✅ **Google Speech Recognition** - Uses Google's speech recognition API

### Text-to-Speech (Voice Output)

- ✅ **ElevenLabs TTS** - High-quality voice output (if available)
- ✅ **Windows SAPI Fallback** - Built-in Windows voice as backup
- ✅ **Visual Feedback** - Arc reactor turns cyan and pulses when speaking
- ✅ **Non-blocking** - Voice output doesn't freeze the interface

---

## 🎯 Voice Commands

### Wake Words

Say any of these to activate:
- **"Hey Jarvis"**
- **"Hey Iron Man"**
- **"Jarvis"**
- **"Iron Man"**

### Available Commands

#### Model Control
- **"Cycle model"** - Switch to next AI model
- **"Next model"** - Switch to next AI model
- **"Switch model"** - Switch to next AI model
- **"Change model"** - Switch to next AI model

#### Status & Information
- **"Status"** - Get system status
- **"How are you"** - Get system status
- **"What's up"** - Get system status

#### Help
- **"Help"** - Get list of commands
- **"What can you do"** - Get list of capabilities
- **"Commands"** - Get list of commands

#### Control
- **"Stop"** - Exit the assistant
- **"Exit"** - Exit the assistant
- **"Quit"** - Exit the assistant
- **"Goodbye"** - Exit the assistant

#### JARVIS Integration
- Any other command is forwarded to JARVIS agent (if available)

---

## 🎨 Visual Feedback

### Listening State

When listening:
- **Arc Reactor**: Turns **yellow** and slightly larger
- **Indicator**: Shows listening state

### Speaking State

When speaking:
- **Arc Reactor**: Turns **cyan** and larger
- **Pulse**: Continues pulsing animation

### Normal State

When idle:
- **Arc Reactor**: Standard cyan color
- **Size**: Normal size

---

## ⚙️ Configuration

### Enable/Disable Wake Word

**Right-click** IRON MAN to toggle wake word detection on/off.

When disabled:
- Wake word detection is off
- Must click IRON MAN to start listening
- Saves battery/CPU

### Listening Settings

Configured in code (can be moved to config):
- **Wake Word Timeout**: 1.0 seconds
- **Listening Timeout**: 5.0 seconds
- **Phrase Timeout**: 2.0 seconds

---

## 🔧 Setup & Requirements

### Required Libraries

#### Speech Recognition

```bash
pip install SpeechRecognition
```

**Also requires**:
- **pyaudio** (for microphone access)
  ```bash
  pip install pyaudio
  ```
  
  **Windows**: May need to install from wheel:
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```

#### Text-to-Speech

**ElevenLabs** (Optional, recommended):
- Requires `jarvis_elevenlabs_integration.py`
- High-quality voice output

**Windows SAPI** (Fallback):
- Built into Windows
- Requires `pywin32`:
  ```bash
  pip install pywin32
  ```

### Microphone Setup

1. **Check Microphone**:
   - Windows: Settings → Privacy → Microphone
   - Ensure microphone access is enabled

2. **Test Microphone**:
   - Use Windows Sound settings
   - Test recording

3. **Default Microphone**:
   - Speech recognition uses default microphone
   - Change in Windows Sound settings if needed

---

## 🚀 Usage

### Starting Voice Features

Voice features start automatically when the assistant launches (if speech recognition is available).

### Using Wake Words

1. **Say wake word**: "Hey Jarvis" or "Hey Iron Man"
2. **Wait for confirmation**: IRON MAN will indicate listening (yellow arc reactor)
3. **Give command**: Speak your command
4. **Get response**: IRON MAN responds with voice

### Manual Trigger

1. **Click IRON MAN**: Left-click to start listening
2. **Speak command**: Give your command
3. **Get response**: IRON MAN responds with voice

### Toggle Wake Word

1. **Right-click IRON MAN**: Toggle wake word on/off
2. **Get confirmation**: Voice confirmation of state

---

## 🎯 Example Interactions

### Example 1: Check Status

**You**: "Hey Jarvis, what's the status?"

**IRON MAN**: "All systems operational. Current model: Mark I. JARVIS online. R5 online. KAIJU online."

### Example 2: Cycle Model

**You**: "Hey Jarvis, cycle model"

**IRON MAN**: "Switched to Mark II"

### Example 3: Get Help

**You**: "Hey Jarvis, what can you do?"

**IRON MAN**: "I can cycle AI models, check system status, respond to questions, and interact with JARVIS. Say 'cycle model' or 'what's the status'."

---

## 🔍 Troubleshooting

### Speech Recognition Not Working

1. **Check Installation**:
   ```bash
   python -c "import speech_recognition; print('OK')"
   ```

2. **Check Microphone**:
   - Verify microphone is working in Windows
   - Check microphone permissions

3. **Check pyaudio**:
   ```bash
   python -c "import pyaudio; print('OK')"
   ```

4. **Check Internet**:
   - Google Speech Recognition requires internet
   - Check network connection

### Voice Output Not Working

1. **Check ElevenLabs**:
   - Verify ElevenLabs integration available
   - Check API key configured

2. **Check Windows SAPI**:
   ```bash
   python -c "import win32com.client; print('OK')"
   ```

3. **Check Windows Voice**:
   - Settings → Time & Language → Speech
   - Verify Windows voice is configured

### Wake Word Not Detecting

1. **Check Wake Word Enabled**:
   - Right-click IRON MAN to check status
   - Voice confirmation when toggled

2. **Check Microphone**:
   - Ensure microphone is working
   - Check microphone levels

3. **Try Manual Trigger**:
   - Click IRON MAN to test listening
   - If manual works, wake word may need adjustment

### Background Noise

1. **Ambient Noise Adjustment**:
   - Script automatically adjusts for ambient noise
   - Wait a few seconds after startup

2. **Quiet Environment**:
   - Use in quieter environment
   - Position microphone closer

3. **Noise Cancellation**:
   - Use noise-cancelling microphone
   - Enable noise cancellation in Windows

---

## 🔐 Privacy & Security

### Speech Recognition

- **Google Speech Recognition**: Audio sent to Google for processing
- **Privacy**: Check Google's privacy policy
- **Offline Option**: Can be configured for offline recognition (requires setup)

### Data Storage

- **No Audio Storage**: Audio is not stored locally
- **Command Logging**: Commands are logged (text only)
- **Privacy**: Voice data not saved

---

## 📊 Performance

### Resource Usage

- **CPU**: Low (speech recognition is lightweight)
- **Memory**: Minimal
- **Network**: Only when using Google Speech Recognition
- **Battery**: Minimal impact

### Optimization

- **Wake Word Detection**: Runs in background thread
- **Listening**: Only active when triggered
- **TTS**: Non-blocking (doesn't freeze UI)

---

## 🎨 Advanced Features (Future)

Potential enhancements:
- **Offline Speech Recognition** (Vosk, etc.)
- **Custom Wake Words**
- **Voice Profiles**
- **Multi-language Support**
- **Voice Commands for JARVIS**
- **Natural Language Processing**
- **Voice Training**
- **Noise Cancellation**
- **Echo Cancellation**

---

## ✅ Status

- ✅ **Speech Recognition**: IMPLEMENTED
- ✅ **Wake Word Detection**: IMPLEMENTED
- ✅ **Voice Commands**: IMPLEMENTED
- ✅ **Text-to-Speech**: IMPLEMENTED
- ✅ **Visual Feedback**: IMPLEMENTED
- ✅ **JARVIS Integration**: IMPLEMENTED
- ✅ **Configuration**: IMPLEMENTED

---

**Status**: ✅ **READY FOR USE**  
**Last Updated**: 2025-01-24
