# TV Channel Monitoring System

**Date**: 2025-01-28  
**Status**: ✅ Implemented  
**Version**: 1.0.0

## Overview

The TV Channel Monitoring System monitors television channels for meaningful content, filters noise, and extracts actionable intelligence. It integrates with IDM (Internet Download Manager) on Kaiju for video downloads and SYPHON for content extraction.

## Key Features

### 1. **Channel Monitoring**
- Monitor multiple TV channels simultaneously
- Support for various channel types:
  - YouTube channels
  - Live stream URLs
  - RSS feeds
  - API-based sources

### 2. **Noise Filtering**
- Automatic filtering of commercials, advertisements, and filler content
- Relevance scoring (Critical, High, Medium, Low, Noise)
- Keyword-based filtering (include/exclude keywords)

### 3. **IDM Integration**
- Automatic video downloads using IDM on Kaiju
- Organized file naming: `Channel_Show_YYYYMMDD_HHMMSS_video.mp4`
- Downloads to Kaiju's download directory

### 4. **SYPHON Extraction**
- Automatic content extraction for high-relevance content
- Integration with SYPHON intelligence extraction system
- Stores extracted data for HK-47 processing

## Architecture

### Components

1. **`idm_kaiju_integration.py`**
   - IDM executable detection (local and network paths)
   - Download directory management
   - Video download orchestration

2. **`tv_channel_monitor.py`**
   - Channel configuration management
   - Content extraction and filtering
   - Relevance scoring
   - SYPHON integration

3. **`config/tv_channels.json`**
   - Channel definitions
   - Monitoring settings
   - IDM configuration

## Usage

### Check IDM Status

```bash
python scripts/python/idm_kaiju_integration.py --status
```

### Monitor All Channels

```bash
python scripts/python/tv_channel_monitor.py --monitor-all
```

### Monitor Specific Channel

```bash
python scripts/python/tv_channel_monitor.py --channel "EWTN"
```

### View Relevant Content

```bash
# Show medium relevance and above
python scripts/python/tv_channel_monitor.py --relevant --min-relevance medium

# Show only critical content
python scripts/python/tv_channel_monitor.py --relevant --min-relevance critical
```

### Download Video via IDM

```bash
python scripts/python/idm_kaiju_integration.py "https://example.com/video.mp4" \
  --channel "EWTN" \
  --show "Father Spitzer's Universe"
```

## Configuration

### Channel Configuration (`config/tv_channels.json`)

```json
{
  "channels": [
    {
      "name": "EWTN",
      "url": "https://www.ewtn.com/tv/watch-live",
      "type": "livestream",
      "description": "Eternal Word Television Network",
      "keywords": ["faith", "religion", "catholic", "spitzer"],
      "exclude_keywords": ["commercial", "advertisement"],
      "check_interval_minutes": 60,
      "enabled": true
    }
  ]
}
```

### Channel Fields

- **name**: Channel name (unique identifier)
- **url**: Channel URL or API endpoint
- **type**: Channel type (`youtube`, `livestream`, `rss`, `api`)
- **description**: Channel description
- **keywords**: Keywords to identify relevant content
- **exclude_keywords**: Keywords that indicate noise (ads, filler)
- **check_interval_minutes**: How often to check for new content
- **enabled**: Enable/disable monitoring

### IDM Configuration

IDM paths are automatically detected from:
1. `config/lumina_idm_config.json`
2. Standard Windows installation paths
3. Network paths to Kaiju (`\\kaiju_no_8\...`)

Download directories:
- Primary: `\\kaiju_no_8\downloads` (Kaiju network share)
- Fallback: `Z:\downloads` (mapped drive)
- Final fallback: User Downloads folder

## Relevance Scoring

Content is scored on a 5-point scale:

1. **CRITICAL**: Breaking news, emergencies, major events
   - Keywords: "breaking", "urgent", "alert", "emergency", "crisis", "war", "attack", "disaster"

2. **HIGH**: Important news, significant events
   - Keywords: "major", "significant", "important", "developing", "election", "policy", "economy"

3. **MEDIUM**: Notable news, interesting topics
   - Keywords: "news", "report", "update", "analysis", "investigation"

4. **LOW**: Routine news, minor events
   - Default for content without specific keywords

5. **NOISE**: Ads, filler, irrelevant content
   - Filtered out automatically

## Automatic Actions

### For CRITICAL Content
- ✅ Video download via IDM
- ✅ SYPHON extraction
- ✅ Saved to content history

### For HIGH Content
- ✅ Video download via IDM
- ✅ SYPHON extraction
- ✅ Saved to content history

### For MEDIUM Content
- ✅ SYPHON extraction
- ✅ Saved to content history

### For LOW Content
- ✅ Saved to content history only

### For NOISE
- ❌ Filtered out (not saved)

## Data Storage

### Content History
- **Location**: `data/tv_monitor/content_history.jsonl`
- **Format**: JSON Lines (one content item per line)
- **Includes**: Channel, title, URL, description, timestamp, relevance, keywords matched

### SYPHON Extraction
- **Location**: SYPHON storage system (`data/syphon/...`)
- **Format**: SYPHON data format
- **Includes**: Extracted intelligence, metadata, actionable items

### Video Downloads
- **Location**: Kaiju download directory (`\\kaiju_no_8\downloads`)
- **Format**: MP4 video files
- **Naming**: `Channel_Show_YYYYMMDD_HHMMSS_video.mp4`

## Integration with Kaiju

### IDM on Kaiju

IDM is installed on Kaiju in its download directory. The system attempts to:
1. Detect IDM on network paths (`\\kaiju_no_8\...`)
2. Use Kaiju's download directory for storage
3. Queue downloads via IDM command-line interface

### Network Access

The system handles network path access gracefully:
- Network paths that require authentication are skipped
- Falls back to local paths if network is unavailable
- Logs warnings for inaccessible paths (debug level)

## Future Enhancements

### Planned Features
1. **YouTube API Integration**: Direct YouTube channel monitoring
2. **RSS Feed Parsing**: Monitor RSS-based news sources
3. **Stream URL Extraction**: Extract direct video URLs from streaming services
4. **Scheduled Monitoring**: Cron-based automatic monitoring
5. **Content Analysis**: AI-powered content analysis and summarization
6. **Alert System**: Notifications for critical content
7. **Duplicate Detection**: Smart duplicate content detection
8. **Multi-language Support**: Monitor channels in multiple languages

## Example Workflow

### Monitor EWTN for Multiverse Discussion

1. **Configure Channel** (`config/tv_channels.json`):
   ```json
   {
     "name": "EWTN Father Spitzer's Universe",
     "url": "https://www.ewtn.com/tv/shows/father-spitzers-universe",
     "keywords": ["multiverse", "universe", "physics", "cosmology"],
     "check_interval_minutes": 60
   }
   ```

2. **Run Monitor**:
   ```bash
   python scripts/python/tv_channel_monitor.py --monitor-all
   ```

3. **Review Results**:
   ```bash
   python scripts/python/tv_channel_monitor.py --relevant --min-relevance high
   ```

4. **Videos Automatically Downloaded**:
   - Location: `\\kaiju_no_8\downloads\EWTN_Father_Spitzers_Universe_20250128_143022_video.mp4`
   - Processed via IDM on Kaiju

5. **Content Extracted via SYPHON**:
   - Stored in SYPHON system
   - Available for HK-47 processing

## Troubleshooting

### IDM Not Found
- **Symptom**: `idm_available: false`
- **Solution**: 
  - Install IDM on Kaiju
  - Configure network path in `config/lumina_idm_config.json`
  - Ensure network share is accessible

### Network Path Access Denied
- **Symptom**: `OSError: [WinError 1326] The user name or password is incorrect`
- **Solution**: 
  - System automatically falls back to local paths
  - Configure network credentials if needed
  - Use mapped drives (e.g., `Z:\downloads`)

### No Content Extracted
- **Symptom**: Monitor runs but finds no content
- **Solution**:
  - Check channel URL is accessible
  - Verify keywords are appropriate
  - Review noise filter settings
  - Check channel type is supported

## See Also

- **IDM Configuration**: `docs/system/LUMINA_IDM_CONFIG.md`
- **SYPHON System**: `docs/system/SYPHON_SYSTEM.md`
- **Kaiju Integration**: `docs/system/KAIJU_IRON_LEGION.md`

