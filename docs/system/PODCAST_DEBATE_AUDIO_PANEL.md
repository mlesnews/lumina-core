# @MARVIN @RR @JARVIS @PODCAST Audio Panel System

**Enhanced Podcast Debate with ElevenLabs Audio Generation and Panel Discussion Format**

**Tags:** #MARVIN #RR #JARVIS #PODCAST #DEBATE #AUDIO #ELEVENLABS #PANEL #LUMINA

---

## 🎙️  Overview

The enhanced podcast debate system generates full audio podcasts with distinct voices for each participant (@MARVIN, @RR, @JARVIS, @PODCAST) using ElevenLabs TTS. Includes panel discussion format with introductions and natural conversation flow.

---

## ✅  Features

### **1. Audio Generation**
- ✅ Full audio podcast generation using ElevenLabs TTS
- ✅ Distinct voices for each participant
- ✅ Natural conversation flow
- ✅ Audio segment combination into complete podcast

### **2. Panel Discussion Format**
- ✅ Panel introductions
- ✅ Participant name announcements
- ✅ Professional podcast structure
- ✅ Natural transitions between speakers

### **3. Voice Mapping**
- **@MARVIN** → `sam` (Raspy, pessimistic) - Lower stability for variation
- **@RR** → `adam` (Deep, analytical) - Consistent, analytical tone
- **@JARVIS** → `josh` (Clear, optimistic) - High stability, clear voice
- **@PODCAST** → `rachel` (Calm, professional) - Balanced, moderator tone

### **4. Audio Settings**
- **Stability**: Controls voice variation (0-1, lower = more expressive)
- **Similarity Boost**: Controls voice consistency (0-1, higher = more consistent)
- **Model**: `eleven_multilingual_v2` (supports 29+ languages)

---

## 🚀  Usage

### **Generate Panel Discussion with Audio**
```bash
python scripts/python/marvin_rr_jarvis_podcast_debate.py --panel
```

**Output:**
- JSON transcript: `data/podcast_debates/debate_YYYYMMDD_HHMMSS.json`
- Audio podcast: `data/podcast_debates/audio/podcast_YYYYMMDD_HHMMSS.mp3`
- Individual segments: `data/podcast_debates/audio/segment_*.mp3`

### **Generate Audio Podcast (Standard Format)**
```bash
python scripts/python/marvin_rr_jarvis_podcast_debate.py --audio
```

### **Generate Text Transcript Only**
```bash
python scripts/python/marvin_rr_jarvis_podcast_debate.py --transcript
```

### **Generate Debate JSON**
```bash
python scripts/python/marvin_rr_jarvis_podcast_debate.py --debate --json
```

---

## 📋  Panel Discussion Structure

### **1. Introduction (Panel Mode)**
```
Welcome to the @MARVIN @RR @JARVIS @PODCAST Panel Discussion.
Today we're exploring @LUMINA and the finer points of physics and astronomy.
Our panel includes @MARVIN, the reality checker; @RR, the root cause analyst;
@JARVIS, the optimistic problem solver; and @PODCAST, your moderator.
Let's begin.
```

### **2. Debate Segments**
Each segment includes:
- Participant name announcement (panel mode)
- Their perspective/statement
- Natural voice characteristics

### **3. Audio Combination**
- Segments combined with 0.5-second pauses
- Volume normalization
- MP3 export at 192kbps

---

## 🎯  Voice Characteristics

### **@MARVIN (sam - Raspy Male)**
- **Stability**: 0.3 (More variation, expressive)
- **Similarity**: 0.7 (Moderate consistency)
- **Tone**: Pessimistic but truthful
- **Use**: Reality checks, critical analysis

### **@RR (adam - Deep Male)**
- **Stability**: 0.6 (Consistent, analytical)
- **Similarity**: 0.8 (High consistency)
- **Tone**: Analytical, systematic
- **Use**: Root cause analysis, deep thinking

### **@JARVIS (josh - Clear Male)**
- **Stability**: 0.7 (Very consistent)
- **Similarity**: 0.9 (High consistency)
- **Tone**: Optimistic, solution-oriented
- **Use**: Problem solving, execution

### **@PODCAST (rachel - Calm Female)**
- **Stability**: 0.5 (Balanced)
- **Similarity**: 0.75 (Moderate consistency)
- **Tone**: Neutral, professional
- **Use**: Moderation, introductions

---

## 🔧  Technical Details

### **Dependencies**
- `elevenlabs` - ElevenLabs Python SDK
- `pydub` - Audio processing (for combining segments)
- `requests` - HTTP requests (fallback if SDK unavailable)

### **Installation**
```bash
pip install elevenlabs pydub
```

### **API Key**
- Stored in Azure Key Vault: `elevenlabs-api-key`
- Fallback to environment variable: `ELEVENLABS_API_KEY`

### **File Structure**
```
data/podcast_debates/
├── debate_YYYYMMDD_HHMMSS.json      # Transcript
└── audio/
    ├── podcast_YYYYMMDD_HHMMSS.mp3  # Combined podcast
    ├── intro_000.mp3                 # Introduction (panel mode)
    ├── segment_000.mp3               # Segment 1
    ├── segment_001.mp3               # Segment 2
    └── ...
```

---

## 📊  Example Output

### **Panel Discussion Generation**
```python
from marvin_rr_jarvis_podcast_debate import PodcastDebateSystem
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
podcast = PodcastDebateSystem(project_root)

# Generate panel discussion with audio
panel = podcast.generate_panel_discussion()

print(f"✅ Panel Discussion Complete")
print(f"   Transcript: {panel['transcript_file']}")
print(f"   Audio: {panel['audio_file']}")
print(f"   Segments: {panel['debate']['total_segments']}")
```

### **Audio Generation Only**
```python
# Generate debate first
debate = podcast.debate_lumina_physics_astronomy()

# Generate audio
audio_result = podcast.generate_audio_podcast(debate, panel_mode=True)

if audio_result['success']:
    print(f"✅ Audio Podcast: {audio_result['audio_file']}")
```

---

## 🎨  Customization

### **Custom Voices**
Modify `voice_map` in `__init__`:
```python
self.voice_map = {
    "marvin": {
        "voice": "custom_voice_id",  # Your custom voice
        "stability": 0.3,
        "similarity_boost": 0.7
    },
    # ... other participants
}
```

### **Custom Topics**
Extend `debate_lumina_physics_astronomy()` or create new debate methods:
```python
def debate_custom_topic(self, topic: str) -> Dict[str, Any]:
    # Custom debate logic
    pass
```

### **Audio Settings**
Adjust pause duration, bitrate, normalization:
```python
# In _combine_audio_segments method
pause = AudioSegment.silent(duration=1000)  # 1 second pause
combined.export(str(output_file), format="mp3", bitrate="256k")
```

---

## 🔍  Troubleshooting

### **ElevenLabs Not Available**
- Check API key in Azure Key Vault
- Verify `elevenlabs` package installed: `pip install elevenlabs`
- Check network connectivity

### **Audio Not Combining**
- Install `pydub`: `pip install pydub`
- Check audio file permissions
- Verify all segments generated successfully

### **Voice Not Matching**
- Check voice IDs in `ELEVENLABS_VOICES` dictionary
- Verify voice exists in ElevenLabs account
- Test individual voice synthesis

---

## 📈  Future Enhancements

1. **Background Music** → Add intro/outro music
2. **Sound Effects** → Add transition sounds
3. **Multiple Formats** → WAV, OGG, FLAC export
4. **Streaming** → Real-time audio generation
5. **Voice Cloning** → Custom voices for each participant
6. **Multilingual** → Support for multiple languages
7. **Podcast Distribution** → Auto-upload to platforms

---

## 📚  Related Documentation

- `ELEVENLABS_CAPABILITIES_FOR_LUMINA.md` - ElevenLabs features
- `marvin_rr_jarvis_podcast_debate.py` - Implementation
- `elevenlabs_tts_integration.py` - TTS integration

---

**Status:** ✅ Enhanced with audio generation and panel format  
**Priority:** High for podcast content generation  
**Tags:** #MARVIN #RR #JARVIS #PODCAST #AUDIO #ELEVENLABS #PANEL
