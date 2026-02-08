# 🐟 Babelfish Testing Guide

**How to test the Babelfish translation system with your anime**

---

## ✅ Quick Test (Sample Phrases)

Test the system with sample Japanese anime phrases:

```bash
python scripts/python/test_babelfish_anime.py --sample
```

**Expected Output:**
```
✅ Using deep-translator

 1. 🇯🇵 こんにちは           → 🇺🇸 Hello
 2. 🇯🇵 ありがとうございます      → 🇺🇸 thank you
 3. 🇯🇵 すみません           → 🇺🇸 sorry
 ...
```

---

## 🎬 Test with Your Anime File

### Option 1: Automatic File Finder

Let the system find your anime files automatically:

```bash
python scripts/python/find_and_test_anime.py
```

This will:
1. Search common locations (Downloads, Videos, Desktop)
2. List all found video and subtitle files
3. Let you select one to test
4. Automatically extract and translate

### Option 2: Direct File Test

Test with a specific file:

```bash
# Subtitle file (.srt)
python scripts/python/test_babelfish_anime.py "path/to/subtitles.srt"

# Video file (.mp4, .mkv, etc.)
python scripts/python/test_babelfish_anime.py "path/to/anime.mp4"
```

---

## 📋 What Happens During Testing

### With Subtitle Files (.srt, .ass, .vtt)

1. **Extract subtitles** from the file
2. **Translate** each subtitle line (Japanese → English)
3. **Save results**:
   - `translated_subtitles_*.json` - Full data
   - `translated_*.srt` - Translated subtitle file (can load in video player)

### With Video Files (.mp4, .mkv, .avi)

1. **Extract subtitles** from video (requires ffmpeg)
2. **Translate** each subtitle line
3. **Save results** (same as above)

**Note**: Video files must have embedded subtitles. If not, use a separate .srt file.

---

## 🔧 Requirements

### Installed Packages

```bash
pip install deep-translator pysrt
```

### Optional (for video files)

- **ffmpeg**: For extracting subtitles from video files
  - Download: https://ffmpeg.org/download.html
  - Or: `choco install ffmpeg` (Windows)

---

## 📁 Output Files

All output files are saved to: `data/babelfish/`

- `test_translation_*.json` - Sample phrase test results
- `translated_subtitles_*.json` - Full subtitle data
- `translated_*.srt` - Translated subtitle file (load in video player)

---

## 🎯 Using Translated Subtitles

### In VLC Media Player

1. Open your video file
2. Go to: **Subtitles** → **Add Subtitle File**
3. Select the `translated_*.srt` file
4. Enjoy English subtitles!

### In Other Players

Most video players support .srt files:
- **MPC-HC**: Right-click → Subtitles → Load subtitles
- **PotPlayer**: Right-click → Subtitles → Open subtitle
- **Windows Media Player**: Drag and drop .srt file

---

## 🐛 Troubleshooting

### "No subtitles found in video file"

- The video may not have embedded subtitles
- Try using a separate .srt file instead
- Or extract subtitles manually with ffmpeg

### "Translation service not available"

- Check internet connection (uses Google Translate API)
- Install: `pip install deep-translator`

### "pysrt not installed"

- Install: `pip install pysrt`

### "ffmpeg not found"

- Install ffmpeg from https://ffmpeg.org/download.html
- Or use subtitle files directly (no ffmpeg needed)

---

## 💡 Tips

1. **Start with .srt files** - Easier and faster than video files
2. **Check subtitle quality** - Better source = better translation
3. **Review translations** - Machine translation isn't perfect
4. **Save originals** - Keep original subtitles as backup

---

## 🚀 Next Steps

After testing:

1. **Review translations** - Check accuracy
2. **Adjust if needed** - Edit translated .srt file manually
3. **Use in video player** - Load translated subtitles
4. **Request improvements** - Tell us what to improve!

---

**Last Updated**: 2025-12-28  
**Status**: ✅ Ready to Test

