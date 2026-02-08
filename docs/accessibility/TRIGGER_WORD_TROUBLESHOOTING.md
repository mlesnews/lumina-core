# Trigger Word Troubleshooting

**Date**: 2026-01-14  
**Status**: 🔧 **TROUBLESHOOTING GUIDE**  
**Tags**: `#VOICE_INPUT` `#TROUBLESHOOTING` `#TRIGGER_WORD` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🚨 Issue: Trigger Word Not Working

**Problem**: Saying "Hey Jarvis" doesn't activate the system

---

## 🔍 Quick Diagnostic

### Run Test Script

```powershell
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts\python\test_trigger_word.py
```

This will test:
1. ✅ Dependencies installed
2. ✅ Microphone working
3. ✅ Speech recognition working
4. ✅ Trigger word detection

---

## 🔧 Common Issues & Fixes

### Issue 1: Script Not Running

**Symptom**: Nothing happens when you say trigger word

**Check**:
```powershell
Get-Process python | Where-Object {$_.CommandLine -like "*passive_active*"}
```

**Fix**: Start the script
```powershell
python scripts\python\passive_active_voice_system.py
```

---

### Issue 2: Dependencies Missing

**Symptom**: Error about missing modules

**Check**:
```powershell
python -c "import speech_recognition; print('OK')"
```

**Fix**: Install dependencies
```powershell
pip install SpeechRecognition pyaudio pyautogui
```

---

### Issue 3: Microphone Not Working

**Symptom**: No audio detected

**Check**:
1. Windows Settings → Privacy → Microphone → Allow access
2. Check microphone is selected in Windows
3. Test microphone in Windows Voice Recorder

**Fix**:
1. Enable microphone access
2. Select correct microphone device
3. Adjust microphone volume

---

### Issue 4: Speech Recognition Not Working

**Symptom**: Can't understand audio

**Check**:
- Internet connection (uses Google Speech API)
- Microphone quality
- Background noise

**Fix**:
1. Check internet connection
2. Speak clearly and loudly
3. Reduce background noise
4. Adjust energy threshold in script

---

### Issue 5: Trigger Word Not Detected

**Symptom**: Speech recognized but trigger not detected

**Possible Causes**:
1. Not saying exact phrase
2. Speech recognition mishears
3. Energy threshold too high/low

**Fix**:
1. Say clearly: "Hey Jarvis" (pause between words)
2. Try just "Jarvis"
3. Check what was actually heard (see test output)
4. Adjust energy threshold in script

---

## 🎯 Quick Fixes

### Fix 1: Lower Energy Threshold

**If microphone is too sensitive or not sensitive enough:**

Edit `passive_active_voice_system.py`:
```python
self.recognizer.energy_threshold = 3000  # Lower = more sensitive
```

### Fix 2: Add More Trigger Words

**If "Hey Jarvis" isn't being recognized:**

Edit trigger words:
```python
trigger_words=["hey jarvis", "jarvis", "activate", "wake up"]
```

### Fix 3: Use Offline Recognition

**If internet is the issue:**

Switch to offline recognition (requires different library):
- Use `vosk` for offline recognition
- Or use Windows Speech Recognition

---

## 🧪 Step-by-Step Testing

### Step 1: Test Microphone

```powershell
python -c "import speech_recognition as sr; r = sr.Recognizer(); print('Testing mic...'); with sr.Microphone() as source: r.adjust_for_ambient_noise(source); print('✅ Mic OK')"
```

### Step 2: Test Speech Recognition

```powershell
python scripts\python\test_trigger_word.py
```

Say "Hey Jarvis" when prompted.

### Step 3: Check What Was Heard

The test script will show exactly what was recognized.

### Step 4: Adjust If Needed

If it heard something different:
- Add that phrase as trigger word
- Or speak more clearly
- Or adjust recognition settings

---

## 🔧 Advanced Troubleshooting

### Check Audio Devices

```powershell
python -c "import speech_recognition as sr; print([i for i in range(sr.Microphone.list_microphone_names())])"
```

### Test Specific Microphone

Edit script to use specific device:
```python
with sr.Microphone(device_index=1) as source:  # Use device 1
```

### Increase Timeout

If trigger word takes time to say:
```python
audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=15)
```

---

## 💡 Alternative: Use F23 Key Instead

**If trigger word continues to have issues:**

Use F23 key (already configured):
- Press F23 → Activates voice input
- No trigger word needed
- More reliable

**F23 is already set up and working!**

---

## 📝 What to Check

1. ✅ Script is running
2. ✅ Dependencies installed
3. ✅ Microphone working
4. ✅ Internet connection (for Google Speech API)
5. ✅ Speaking clearly
6. ✅ Trigger word phrase correct

---

**Status**: 🔧 **TROUBLESHOOTING GUIDE**  
**Test Script**: `scripts/python/test_trigger_word.py`  
**Tags**: `#VOICE_INPUT` `#TROUBLESHOOTING` `#TRIGGER_WORD` `@LUMINA` `@JARVIS` `#PEAK`
