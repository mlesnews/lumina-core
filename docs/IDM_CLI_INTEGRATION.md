# IDM-CLI Web Crawler & Scraper Integration

## Overview

**Adapt, Improvise, Overcome** - IDM-CLI (Internet Download Manager CLI) has been integrated as an alternative web crawler/scraper for all sources, including YouTube channels and websites.

## Purpose

IDM-CLI provides a robust alternative to traditional scraping tools like `yt-dlp` and `requests/BeautifulSoup`, especially when:
- `yt-dlp` times out on large channels
- Traditional scrapers fail due to rate limiting
- We need resume capability for large downloads
- We want to leverage IDM's download acceleration

## Integration Points

### 1. YouTube Channel Import

**Location**: `scripts/python/import_ewtn_magiscenter_complete.py`

**Method**: `_import_youtube_channel()`

**Flow**:
1. **Try IDM-CLI first** (Adapt, Improvise, Overcome)
   - Uses `IDMCLIWebCrawler.crawl_youtube_channel()`
   - Discovers videos via channel page HTML parsing
   - Falls back to `yt-dlp` if IDM method fails or finds no videos

2. **Process videos with SYPHON**
   - Extracts intelligence from each video
   - Ingests to R5 with accessibility metadata
   - Extracts transcripts for visually impaired users

### 2. Website Import

**Location**: `scripts/python/import_ewtn_magiscenter_complete.py`

**Method**: `_import_website()`

**Flow**:
1. **Try IDM-CLI first** (Adapt, Improvise, Overcome)
   - Uses `IDMCLIWebCrawler.crawl_website()`
   - Discovers URLs and queues downloads in IDM
   - Processes downloaded HTML files with SYPHON

2. **Fallback to specialized scrapers**
   - Magis Center: Uses `syphon_magiscenter.py`
   - Other sites: Uses SYPHON directly

### 3. IDM-CLI Web Crawler

**Location**: `scripts/python/idm_cli_web_crawler.py`

**Key Methods**:
- `crawl_website()`: Crawl entire websites
- `crawl_youtube_channel()`: Discover YouTube channel videos
- `download_video()`: Download individual videos
- `batch_download_urls()`: Batch download multiple URLs

**Features**:
- Auto-detects IDM installation
- Falls back to requests/BeautifulSoup if IDM not available
- Supports PowerShell script integration
- Resume capability for interrupted downloads

## Usage

### Import EWTN/Magis Center with IDM

```python
from scripts.python.import_ewtn_magiscenter_complete import EWTNMagisCenterImporter

importer = EWTNMagisCenterImporter()
results = importer.import_all_sources()
```

### Direct IDM-CLI Usage

```python
from scripts.python.idm_cli_web_crawler import IDMCLIWebCrawler

crawler = IDMCLIWebCrawler()

# Crawl website
result = crawler.crawl_website("https://www.ewtn.com", max_pages=1000)

# Crawl YouTube channel
result = crawler.crawl_youtube_channel("https://www.youtube.com/@EWTN", max_videos=500)

# Download video
result = crawler.download_video("https://www.youtube.com/watch?v=VIDEO_ID")
```

## IDM Installation Detection

The system automatically checks for IDM in these locations:
- `D:/Program Files (x86)/Internet Download Manager/IDMan.exe` (prioritized)
- `D:/Program Files/Internet Download Manager/IDMan.exe`
- `C:/Program Files (x86)/Internet Download Manager/IDMan.exe`
- `C:/Program Files/Internet Download Manager/IDMan.exe`
- `C:/IDM/IDMan.exe`
- `D:/IDM/IDMan.exe`
- PowerShell script: `scripts/powershell/Invoke-IDMDownload.ps1`

## Fallback Behavior

If IDM is not available or fails:
1. **YouTube Channels**: Falls back to `yt-dlp`
2. **Websites**: Falls back to `requests/BeautifulSoup` or specialized scrapers
3. **All methods**: Still process content with SYPHON and ingest to R5

## Benefits

1. **Resume Capability**: IDM can resume interrupted downloads
2. **Speed**: IDM's acceleration can speed up large downloads
3. **Reliability**: Alternative when other tools fail or timeout
4. **Batch Processing**: Queue multiple downloads efficiently
5. **Accessibility**: All content processed with accessibility features

## Adapt, Improvise, Overcome

This integration embodies the "Adapt, Improvise, Overcome" philosophy:
- **Adapt**: Use IDM when traditional tools fail
- **Improvise**: Parse HTML when API access is limited
- **Overcome**: Multiple fallback methods ensure content is always imported

## Related Files

- `scripts/python/idm_cli_web_crawler.py` - Core IDM-CLI crawler
- `scripts/python/import_ewtn_magiscenter_complete.py` - EWTN/Magis Center importer
- `scripts/python/import_sources_with_idm.py` - General source importer using IDM
- `scripts/powershell/Invoke-IDMDownload.ps1` - PowerShell IDM helper

## Tags

@IDM @IDM-CLI @WEB-CRAWLER @SCRAPER @SOURCES @ADAPT-IMPROVISE-OVERCOME @SYPHON @EWTN @MAGISCENTER
