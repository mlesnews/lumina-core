# 🐟 LUMINA Babelfish - Quick Start Guide

**Real-Time Japanese Translation for Anime**

Inspired by the Babelfish from *Hitchhiker's Guide to the Galaxy*.

---

## 🎯 What Is This?

A system to translate Japanese audio/text to English in real-time, specifically designed for watching anime.

**The Problem**: You're watching Japanese anime, hearing Japanese dialogue, but want English translations.

**The Solution**: Babelfish extracts and translates subtitles, or captures audio and translates it.

---

## 🚀 Quick Start (3 Approaches)

### Phase 1: Subtitle Extraction (EASIEST - Start Here!)

**If your video has subtitles, extract and translate them.**

```bash
# Extract subtitles from video file
python scripts/python/babelfish_subtitle_extractor.py video.mp4 --translate

# Or extract from existing .srt file
python scripts/python/babelfish_subtitle_extractor.py subtitles.srt --translate
```

**Requirements:**
- `pip install deep-translator` (or `googletrans==4.0.0rc1`)
- `pip install pysrt` (for .srt files)
- `ffmpeg` (for extracting from video files)

**This is the "right under our noses" solution!**

---

### Phase 2: Real-Time Audio Translation

**Capture audio and translate in real-time.**

```bash
# Start real-time translation (microphone)
python scripts/python/lumina_babelfish_translator.py

# Translate a single text string
python scripts/python/lumina_babelfish_translator.py --text "こんにちは"
```

**Requirements:**
- `pip install SpeechRecognition`
- `pip install pyaudio`
- `pip install deep-translator`

**Note**: System audio capture on Windows is tricky. You may need:
- VB-Audio Virtual Cable
- Voicemeeter
- Or use microphone pointed at speakers

---

### Phase 3: Hybrid System (Future)

Combine subtitle extraction + audio translation + context awareness.

---

## 📋 Installation

```bash
# Core dependencies
pip install deep-translator SpeechRecognition pyaudio pysrt

# Optional: For video subtitle extraction
# Install ffmpeg from https://ffmpeg.org/download.html
```

---

## 🎬 Usage Examples

### Example 1: Extract & Translate Subtitles

```bash
# Video file with embedded subtitles
python scripts/python/babelfish_subtitle_extractor.py anime_episode.mp4 --translate

# Output:
# - translated_subtitles_YYYYMMDD_HHMMSS.json
# - translated_YYYYMMDD_HHMMSS.srt (can be loaded in video player)
```

### Example 2: Real-Time Translation

```bash
# Start listening and translating
python scripts/python/lumina_babelfish_translator.py

# Output in console:
# 🇯🇵 こんにちは、世界
# 🇺🇸 Hello, world
```

### Example 3: Single Text Translation

```bash
# Translate a single Japanese phrase
python scripts/python/lumina_babelfish_translator.py --text "ありがとうございます"

# Output:
# 🇯🇵 Original: ありがとうございます
# 🇺🇸 Translated: Thank you very much
```

---

## 🔧 Technical Details

### How It Works

1. **Subtitle Extraction**:
   - Extract subtitles from video file (using ffmpeg)
   - Or read from existing .srt file
   - Translate each subtitle line
   - Save as translated .srt file

2. **Real-Time Audio**:
   - Capture audio chunks (3 seconds)
   - Recognize Japanese speech (Google Speech API)
   - Translate to English (Google Translate)
   - Display in real-time

### Limitations

**@MARVIN's Reality Check:**
- System audio capture is hard on Windows
- Speech recognition has 1-3 second delay
- Translation adds 0.5-2 second delay
- Total: 2-5 seconds latency (not truly "real-time")
- Machine translation loses nuance and context

**JARVIS's Optimism:**
- Subtitle extraction is fast and accurate
- Can cache common translations
- Can learn from existing subtitles
- Can improve with context awareness

---

## 💡 Recommendations

### Start Simple

1. **Use Subtitle Extraction First** (Phase 1)
   - Fastest
   - Most accurate
   - Easiest to implement
   - Works with most video files

2. **Add Audio Translation Later** (Phase 2)
   - More complex
   - Requires system audio setup
   - Has latency
   - Good for videos without subtitles

3. **Build Hybrid System** (Phase 3)
   - Best of both worlds
   - Subtitle extraction + audio fallback
   - Context-aware translation

---

## 🐛 Troubleshooting

### "No subtitles found"
- Video may not have embedded subtitles
- Try extracting with ffmpeg manually
- Or use external .srt file

### "Translation service not available"
- Install: `pip install deep-translator`
- Or: `pip install googletrans==4.0.0rc1`
- Check internet connection (uses Google Translate API)

### "Speech recognition error"
- Install: `pip install SpeechRecognition`
- Check internet connection (uses Google Speech API)
- Ensure microphone/system audio is working

### "System audio capture not working"
- Windows: Use VB-Audio Virtual Cable or Voicemeeter
- Or use microphone pointed at speakers
- Or use screen capture software (OBS)

---

## 📁 Output Files

All output files are saved to: `data/babelfish/`

- `translated_subtitles_*.json` - JSON format with all subtitle data
- `translated_*.srt` - SRT file with translations (can load in video player)
- `translations_*.jsonl` - Real-time translation log (JSON Lines format)
- `session_*.json` - Complete translation session

---

## 🎯 Next Steps

1. **Try Phase 1** (Subtitle Extraction) - It's the easiest!
2. **Test with your anime** - See how it works
3. **Report issues** - Help improve the system
4. **Request features** - What would make it better?

---

## 🤖 @MARVIN & JARVIS Assessment

Run the assessment to see their perspectives:

```bash
python scripts/python/babelfish_marvin_jarvis_assessment.py
```

---

## 📚 References

- **Hitchhiker's Guide to the Galaxy** - Douglas Adams
- **Babelfish**: "The Babelfish is small, yellow, leech-like, and probably the oddest thing in the Universe."

---

**Last Updated**: 2025-12-28  
**Status**: ✅ Phase 1 Ready | ⏸️ Phase 2 In Progress

