# Father Spitzer's Universe - SYPHON

## Overview

Comprehensive intelligence extraction system for **Father Spitzer's Universe** content from EWTN.

## What is Father Spitzer's Universe?

**Father Spitzer's Universe** is a program on EWTN where Fr. Robert Spitzer addresses viewer questions on topics such as:
- Reason and faith
- Suffering and virtue
- The existence of God
- Cosmology and philosophy
- Science and theology

## Sources

### Primary Sources

1. **EWTN YouTube Channel**
   - URL: `https://www.youtube.com/@EWTN`
   - Filtered for "Father Spitzer's Universe" content
   - Search terms: "father spitzer's universe", "fr spitzer's universe", "spitzer universe"

2. **EWTN OnDemand**
   - URL: `https://ondemand.ewtn.com/Home/Series/ondemand/video/en/fr-spitzers-universe`
   - Official series page

3. **Apple Podcasts**
   - Available as podcast episodes
   - Can be syphoned separately if needed

## Script

**Location**: `scripts/python/syphon_father_spitzer_universe.py`

### Features

- ✅ **YouTube Search**: Searches for "Father Spitzer's Universe" content
- ✅ **Channel Filtering**: Filters EWTN channel videos for relevant content
- ✅ **SYPHON Integration**: Extracts intelligence using SYPHON system
- ✅ **R5 Ingestion**: Ingests extracted data to R5 Living Context Matrix
- ✅ **Unified Queue**: Adds sources to unified queue for processing
- ✅ **Resume Support**: Can resume from previous state
- ✅ **Transcript Extraction**: Extracts video transcripts when available
- ✅ **Metadata Preservation**: Saves all video metadata

### Usage

```bash
# Basic usage (process up to 500 videos)
python scripts/python/syphon_father_spitzer_universe.py

# Limit number of videos
python scripts/python/syphon_father_spitzer_universe.py --max-videos 200

# Resume from previous state
python scripts/python/syphon_father_spitzer_universe.py --resume

# Custom output directory
python scripts/python/syphon_father_spitzer_universe.py --output-dir data/custom
```

### Output

**Location**: `data/syphon/father_spitzer_universe/`

- `spitzer_universe_{video_id}.json` - Individual video extraction results
- `syphon_state.json` - State file for resuming
- `syphon_summary.json` - Summary of all processed videos

### Data Structure

Each video extraction includes:

```json
{
  "video": {
    "video_id": "...",
    "title": "...",
    "url": "...",
    "duration": "...",
    "upload_date": "...",
    "view_count": "...",
    "description": "..."
  },
  "syphon_data": {
    "data_id": "spitzer_universe_{video_id}",
    "content": "...",
    "metadata": {
      "title": "...",
      "source": "Father Spitzer's Universe - EWTN",
      "series": "Father Spitzer's Universe",
      "video_id": "...",
      "transcript_available": true/false
    },
    "actionable_items": [],
    "tasks": [],
    "intelligence": {}
  },
  "extracted_at": "..."
}
```

## Integration

### Unified Queue

All videos are automatically added to the unified queue as **SOURCE** items:
- **Type**: `source`
- **Source Type**: `youtube`
- **Priority**: 5 (high)
- **Metadata**: Includes series, channel, video_id, duration, etc.

### R5 Living Context Matrix

Extracted intelligence is ingested to R5:
- **Session Type**: `youtube_video_syphon`
- **Content**: Video title, URL, description, transcript
- **Metadata**: Full video metadata + SYPHON intelligence

### AI Orchestrator

Sources added to queue are processed by AI Orchestrator:
- **Workflow**: Discovery → Download → Extract → Process → Complete
- **Real-time Updates**: Status visible in IDE footer
- **Intelligent Routing**: AI decides download vs. direct extraction

## Search Strategy

The script uses multiple methods to find Father Spitzer's Universe content:

1. **Direct YouTube Search**
   - Queries: "Father Spitzer's Universe EWTN", "Fr Spitzer's Universe", etc.
   - Returns up to 100 results per query

2. **Channel Filtering**
   - Fetches EWTN channel videos
   - Filters by title/description for search terms
   - Pattern matching: "fr. spitzer", "father spitzer", "spitzer's universe"

3. **Deduplication**
   - Removes duplicate videos by video_id
   - Ensures unique content only

## Processing Flow

```
1. Search YouTube for "Father Spitzer's Universe"
   ↓
2. Fetch EWTN channel videos
   ↓
3. Filter for Father Spitzer's Universe content
   ↓
4. Deduplicate videos
   ↓
5. For each video:
   - Add to unified queue
   - Extract with SYPHON
   - Save extracted data
   - Ingest to R5
   - Update state
```

## Status

✅ **READY** - Script created and running

The syphon is currently processing Father Spitzer's Universe content in the background. All sources are being added to the unified queue and will be visible in the IDE footer.

## Next Steps

1. Monitor progress in unified queue
2. Check `data/syphon/father_spitzer_universe/` for results
3. Review `syphon_summary.json` for completion status
4. Access extracted intelligence in R5 Living Context Matrix

---

**Tags**: @SYPHON @FATHER_SPITZER @UNIVERSE @EWTN @YOUTUBE @INTELLIGENCE_EXTRACTION
