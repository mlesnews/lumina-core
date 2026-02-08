# IDM-CLI Web Crawler & Scraper

**Date**: 2026-01-02  
**Status**: ✅ **IMPLEMENTED**  
**Tags**: @IDM @IDM-CLI @WEB-CRAWLER @SCRAPER @SOURCES #ADAPT-IMPROVISE-OVERCOME

---

## Overview

Uses **Internet Download Manager (IDM) CLI** as an alternative web crawler/scraper for sources. This provides a robust, Windows-native solution for downloading web content, videos, and entire websites.

**Philosophy**: Adapt, Improvise, Overcome - Use IDM when other tools fail or are slow.

---

## Why IDM-CLI?

### Advantages:
- ✅ **Windows Native** - Built for Windows, highly optimized
- ✅ **Fast Downloads** - Multi-threaded, accelerated downloads
- ✅ **Resume Capability** - Can resume interrupted downloads
- ✅ **Queue Management** - Built-in queue system
- ✅ **Reliable** - Proven download manager
- ✅ **Video Support** - Excellent for video downloads
- ✅ **Website Crawling** - Can download entire websites

### Use Cases:
- Large website crawling (when yt-dlp times out)
- Video batch downloads
- Website mirroring
- Content aggregation
- Alternative to traditional scrapers

---

## Installation

### Option 1: IDM-CLI (Recommended)
```bash
# Install IDM-CLI via npm
npm install -g idm-cli

# Or via pip
pip install idm-cli
```

### Option 2: IDM with CLI Support
1. Install Internet Download Manager
2. Configure IDM path in script
3. Use IDMan.exe command line interface

---

## Usage

### Crawl Website
```bash
python scripts/python/idm_cli_web_crawler.py \
  --crawl https://www.ewtn.com \
  --max-pages 1000 \
  --output data/ewtn_crawl
```

### Download Video
```bash
python scripts/python/idm_cli_web_crawler.py \
  --download https://www.youtube.com/watch?v=VIDEO_ID \
  --output data/videos
```

### Batch Download
```bash
# Create URLs file (urls.txt)
echo "https://www.ewtn.com/page1" > urls.txt
echo "https://www.ewtn.com/page2" >> urls.txt

# Batch download
python scripts/python/idm_cli_web_crawler.py \
  --batch urls.txt \
  --output data/batch_downloads
```

---

## Integration with EWTN/Magis Center Import

The import system automatically uses IDM-CLI when available:

```bash
# Import will use IDM-CLI if available
python scripts/python/import_ewtn_magiscenter_complete.py --source ewtn_website
```

**Fallback**: If IDM-CLI is not available, falls back to:
1. Existing SYPHON web extraction
2. Traditional web scraping (requests/BeautifulSoup)

---

## Features

### Website Crawling
- Discovers all URLs from a website
- Queues downloads in IDM
- Processes downloaded content with SYPHON
- Ingests to R5 Living Context Matrix

### Video Downloading
- Queues videos in IDM
- Supports YouTube, Vimeo, and other platforms
- Batch video processing

### Batch Processing
- Process multiple URLs at once
- Queue management
- Error handling and retry

---

## IDM Command Line Syntax

### Basic Download
```bash
IDMan.exe /d URL /p OUTPUT_PATH /f FILENAME /n /a
```

### Parameters:
- `/d` - Download URL
- `/p` - Save path
- `/f` - Filename
- `/n` - Don't start immediately (queue)
- `/a` - Add to queue

---

## Configuration

### Auto-Detection
The script automatically detects IDM in common locations:
- `C:/Program Files (x86)/Internet Download Manager/IDMan.exe`
- `C:/Program Files/Internet Download Manager/IDMan.exe`
- `C:/IDM/IDMan.exe`
- PATH (if IDM-CLI is installed)

### Manual Configuration
Edit `idm_cli_web_crawler.py` to set custom path:
```python
self.idm_cli_path = Path("C:/Custom/Path/IDMan.exe")
```

---

## Advantages Over Traditional Scrapers

| Feature | IDM-CLI | yt-dlp | requests/BeautifulSoup |
|--------|---------|--------|----------------------|
| Speed | ⚡⚡⚡ Very Fast | ⚡⚡ Fast | ⚡ Moderate |
| Resume | ✅ Yes | ✅ Yes | ❌ No |
| Queue | ✅ Built-in | ❌ No | ❌ No |
| Windows | ✅ Native | ⚠️ Cross-platform | ⚠️ Cross-platform |
| Video | ✅ Excellent | ✅ Excellent | ❌ Limited |
| Website | ✅ Good | ⚠️ Limited | ✅ Good |

---

## Use Cases

### 1. Large Channel Import (EWTN)
When yt-dlp times out on large channels:
```bash
# Use IDM-CLI to download video list first
# Then process with SYPHON
```

### 2. Website Mirroring
Download entire websites for offline access:
```bash
python scripts/python/idm_cli_web_crawler.py \
  --crawl https://www.magiscenter.com \
  --max-pages 1000
```

### 3. Batch Video Download
Download multiple videos efficiently:
```bash
python scripts/python/idm_cli_web_crawler.py \
  --batch video_urls.txt \
  --output data/videos
```

---

## Integration Points

### EWTN/Magis Center Import
- Automatically uses IDM-CLI when available
- Falls back to SYPHON if IDM not available
- Processes downloaded content with SYPHON
- Ingests to R5 with accessibility features

### YouTube Deep Crawl
- Can be used as alternative to yt-dlp
- Better for large channels
- Queue management for thousands of videos

---

## Status

✅ **IDM-CLI Web Crawler**: Implemented  
✅ **EWTN/Magis Import Integration**: Integrated  
✅ **Fallback Methods**: Available  
✅ **Batch Processing**: Supported  
✅ **Resume Capability**: Supported

---

## Related Files

- `scripts/python/idm_cli_web_crawler.py` - Main IDM-CLI crawler
- `scripts/python/import_ewtn_magiscenter_complete.py` - Integrated import system
- `scripts/python/youtube_deep_crawl_sme_mapper.py` - YouTube crawler (alternative)

---

**Created**: 2026-01-02  
**Last Updated**: 2026-01-02  
**Status**: Ready for Use
