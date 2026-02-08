# SYPHON Video/Audio Building Blocks - Core Message Extraction

**Status**: ✅ OPERATIONAL  
**Purpose**: Break down video/audio into building blocks, extract @ask-requested as core messages

---

## 🎯 Core Concept

SYPHON processes video and audio as **basic building blocks**:
1. **Break Down**: Videos/audio split into reusable time-based blocks
2. **Extract**: @ask-requested patterns identified as core messages
3. **Rebuild**: Videos created with @ask-requested as central theme

---

## 🔬 System Architecture

### Video Building Blocks

Each video is broken down into:
- **VideoBuildingBlock**: Time-based segments with extracted content
- **AudioBuildingBlock**: Audio transcript segments
- **CoreMessage**: @ask-requested patterns extracted and ranked by confidence

### Core Message Extraction

SYPHON extracts @ask-requested patterns using multiple regex patterns:
1. `@ask` followed by request text
2. `@ASK-REQUESTED` (uppercase variant)
3. "ask for", "request", "requested" patterns

Core messages are:
- Ranked by confidence (frequency across blocks)
- Linked to source building blocks
- Used as the central theme for video production

---

## 🎬 Video Production Flow

```
Source Video
    ↓
[SYPHON Breakdown]
    ├─→ Extract Audio
    ├─→ Transcribe (when audio available)
    ├─→ Split into Building Blocks
    └─→ Extract @ask-requested Patterns
         ↓
[Core Message Extraction]
    ├─→ Aggregate @ask patterns
    ├─→ Rank by confidence
    └─→ Select primary message
         ↓
[Video Creation]
    └─→ Create video with @ask-requested as core content
```

---

## 📋 Usage

### Process Existing Videos

```python
from lumina_syphon_video_production import LuminaSyphonVideoProduction

producer = LuminaSyphonVideoProduction()
results = producer.process_existing_videos_for_core_messages()
```

### Create Video from @ask-requested

```python
producer = LuminaSyphonVideoProduction()

# Create video with @ask-requested as core message
video_path = producer.create_video_from_ask_requested(
    ask_requested_text="Add breaking down with SYPHON video and audio as basic building blocks"
)
```

---

## ✅ Current Status

- ✅ SYPHON video/audio breakdown system created
- ✅ @ask-requested pattern extraction working
- ✅ Core message ranking by confidence
- ✅ Video creation with core messages
- ✅ Integration with video production pipeline

### Known Limitations

- Videos without audio tracks: Text-only videos (like our trailers) don't have audio to extract
- Audio transcription: Requires Whisper or similar for full transcription
- Visual extraction: Frame-by-frame analysis not yet implemented

### Next Steps

1. **Handle silent videos**: Extract text from video metadata/scripts
2. **Visual analysis**: Extract visual building blocks (scenes, shots)
3. **Enhanced transcription**: Integrate Whisper for audio transcription
4. **Block library**: Build reusable block library from processed videos

---

## 🔗 Integration

SYPHON video processing integrates with:
- **Video Production Executor**: Creates actual video files
- **Pilot Trailer System**: Processes trailer videos
- **Production Pipeline**: End-to-end video creation workflow

---

**Status**: Ready for production use. Core message extraction working.  
**Next**: Enhance with visual analysis and improved transcription.

