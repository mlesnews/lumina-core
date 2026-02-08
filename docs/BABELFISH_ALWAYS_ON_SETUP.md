# 🐟 Babelfish Always-On Listener Setup

**Full-time, always-on listening for real-time Japanese translation with JARVIS voice summaries**

---

## ✅ What's Ready

1. **Always-On Listener** - Continuous listening for Japanese audio
2. **JARVIS Voice** - Speaks translations and summaries (no code blocks!)
3. **NAS Integration** - Finds anime files on your NAS (10.17.17.32)
4. **Real-Time Translation** - Japanese → English as it happens
5. **Periodic Summaries** - JARVIS summarizes every 60 seconds

---

## 🚀 Quick Start

### Start Always-On Listening

```bash
python scripts/python/babelfish_always_on_listener.py
```

JARVIS will speak: "Babelfish always-on listener activated. Ready to translate Japanese audio in real-time."

### Test with Sample Phrases

```bash
python scripts/python/babelfish_always_on_listener.py --test
```

### Find Anime on NAS

```bash
python scripts/python/babelfish_always_on_listener.py --find-anime
```

---

## 🎯 How It Works

### Always-On Listening

- **Continuously listens** for Japanese audio
- **Translates in real-time** (3-10 second delay)
- **JARVIS speaks** each translation immediately
- **Generates summaries** every 60 seconds

### JARVIS Voice Summaries

JARVIS will speak:
- Individual translations as they happen
- Periodic summaries of recent activity
- Common phrases detected
- Latest translations

**NO CODE BLOCKS** - JARVIS only speaks natural language summaries!

### NAS Anime Discovery

Automatically searches:
- `\\10.17.17.32\backups\MATT_Backups\Videos`
- `\\10.17.17.32\backups\MATT_Backups\Media`
- `\\10.17.17.32\backups\MATT_Backups\Anime`
- Mapped drives (Z:\, Y:\, X:\)

---

## 🔧 Requirements

### Installed Packages

```bash
pip install deep-translator pyttsx3
```

### NAS Access

If NAS path isn't accessible:
1. Map the NAS drive: `net use Z: \\10.17.17.32\backups`
2. Or provide NAS credentials when prompted
3. System will try alternative paths automatically

---

## 📋 Features

### Real-Time Translation

- Listens for Japanese audio
- Recognizes speech (Google Speech API)
- Translates to English
- JARVIS speaks the translation

### Periodic Summaries

Every 60 seconds, JARVIS speaks:
- Number of translations processed
- Common phrases detected
- Latest translation

### Translation History

All translations saved to:
- `data/babelfish/translations_*.jsonl`
- Can be reviewed later
- Used for summaries

---

## 🎤 JARVIS Voice Configuration

- **Voice**: Male, clear voice (David or similar)
- **Speed**: 150 words per minute (slightly faster)
- **Output**: Natural language only (no code blocks!)
- **Format**: Clean, conversational summaries

---

## 🐛 Troubleshooting

### "NAS path not accessible"

- Map the drive: `net use Z: \\10.17.17.32\backups`
- Or check NAS credentials
- System will try alternative paths

### "JARVIS TTS not working"

- Install: `pip install pyttsx3`
- Check Windows audio settings
- Verify default audio device

### "No audio detected"

- Check microphone/system audio settings
- Ensure audio source is configured
- For system audio, may need VB-Audio or Voicemeeter

---

## 💡 Usage Tips

1. **Start listener** before watching anime
2. **Let it run** in background
3. **JARVIS will speak** translations automatically
4. **Summaries every 60 seconds** keep you informed
5. **Press Ctrl+C** to stop

---

## 🎯 Next Steps

1. **Start always-on listener** - Run the script
2. **Play your anime** - System will detect Japanese audio
3. **Listen to JARVIS** - He'll speak translations
4. **Review summaries** - Every 60 seconds

---

**Last Updated**: 2025-12-28  
**Status**: ✅ Always-On Listener Ready | 🤖 JARVIS Voice Active

