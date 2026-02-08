# EWTN Sermon on TIME - SYPHON Extraction Guide

## Overview
Extract intelligence from recent televised EWTN sermon on "TIME" topic using SYPHON system.

**Source:** Comcast Cable (Xfinity) / YouTubeTV  
**Topic:** TIME  
**Network:** EWTN (Eternal Word Television Network)

## Quick Start

### Option 1: If you have the YouTube URL

```bash
python scripts/python/extract_ewtn_sermon_time_syphon.py <youtube_url>
```

Example:
```bash
python scripts/python/extract_ewtn_sermon_time_syphon.py https://www.youtube.com/watch?v=VIDEO_ID
```

### Option 2: Find the Sermon First

1. **Search on YouTube:**
   - Go to: https://www.youtube.com/@EWTN
   - Search for: "sermon time" or "TIME sermon"
   - Look for recent uploads (within last 30 days)

2. **Check EWTN Website:**
   - Visit: https://www.ewtn.com
   - Navigate to: Programs > Daily Mass or Sermons
   - Look for recent sermons on TIME

3. **Check Your YouTubeTV/Comcast History:**
   - If you recorded it, check your DVR
   - Look for EWTN channel recordings
   - Find the sermon that aired recently

## What the Script Does

1. **SYPHON Extraction:**
   - Extracts video metadata (title, description, transcript if available)
   - Identifies actionable items
   - Extracts tasks and decisions
   - Captures intelligence points

2. **R5 Ingestion:**
   - Stores extracted content in R5 Living Context Matrix
   - Creates searchable session with all metadata
   - Links actionable items and intelligence

3. **TODO Update:**
   - Updates master TODO tracker
   - Marks task as IN_PROGRESS
   - Tracks completion status

## Expected Output

The script will:
- ✅ Extract intelligence using SYPHON
- ✅ Ingest to R5 Living Context Matrix
- ✅ Update TODO status
- ✅ Display summary of extracted items

## Tags

- `@SYPHON` - Intelligence extraction system
- `@EWTN` - Eternal Word Television Network
- `@YOUTUBE` - YouTube platform
- `@SOURCES` - Source material tracking
- `#EXTRACTION` - Content extraction
- `#SERMON` - Sermon content
- `#TIME` - Topic: TIME
- `#COMCAST` - Comcast/Xfinity provider
- `#XFINITY` - Xfinity provider

## Related Scripts

- `scripts/python/extract_ewtn_sermon_time_syphon.py` - Main extraction script
- `scripts/python/ingest_youtube_r5_syphon.py` - General YouTube ingestion
- `scripts/python/ingest_youtube_channel_syphon.py` - Channel processing

## Notes

- If the sermon was recorded from cable TV, you may need to upload it to YouTube first
- YouTube Data API v3 integration would enable automatic search
- Transcript extraction requires video to have captions enabled
- Full video/audio processing requires additional tools (yt-dlp, ffmpeg)

## Next Steps

1. Find the EWTN sermon URL
2. Run extraction script
3. Review extracted intelligence in R5
4. Mark TODO as complete when done

---

**Created:** 2026-01-02  
**Status:** PENDING  
**Priority:** HIGH
