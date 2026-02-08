# Download Routing System

**Date**: 2025-01-28  
**Status**: ✅ Implemented  
**Version**: 1.0.0

## Overview

The Download Routing System intelligently routes downloads to appropriate cloud storage providers via the NAS DSM Cloud Sync package. The NAS acts as a cloud aggregator, managing and routing downloads to shared spaces like Dropbox, OneDrive, and Google Drive.

## Architecture

### NAS as Cloud Aggregator

The system leverages the existing **DSM Cloud Sync package** on the NAS to:
- Aggregate multiple cloud storage providers (Dropbox, OneDrive, Google Drive)
- Route downloads to appropriate cloud sync paths on the NAS
- Automatically sync files to configured cloud providers
- Provide centralized download management

### Routing Strategy

Downloads are routed based on intelligent rules:

1. **Source-based routing**: TV monitor, YouTube, IDM, browser downloads
2. **Keyword-based routing**: Shared, collaboration, media, document keywords
3. **File type routing**: Documents, media, videos, large files
4. **Size-based routing**: Small, medium, large, very large files
5. **File extension routing**: Specific file extensions
6. **Default routing**: Fallback to configured default (Dropbox)

## Configuration

### Provider Configuration (`config/download_routing_config.json`)

```json
{
  "cloud_storage_providers": {
    "dropbox": {
      "enabled": true,
      "priority": 1,
      "nas_sync_path": "/volume1/dropbox",
      "local_path": "C:\\Users\\mlesn\\Dropbox",
      "file_types": ["documents", "media", "videos", "general"],
      "max_file_size_mb": 2048
    }
  }
}
```

### Routing Rules

The system supports multiple routing rule types:

- **by_source**: Route based on download source (tv_monitor → dropbox)
- **by_keywords**: Route based on keywords (shared → dropbox)
- **by_file_type**: Route based on file type (documents → dropbox)
- **by_size**: Route based on file size (large → nas_direct)
- **by_file_extensions**: Route based on specific extensions

## Usage

### Route Existing File

```bash
python scripts/python/download_router.py "path/to/file.pdf" --source "tv_monitor"
```

### Route with Keywords

```bash
python scripts/python/download_router.py "video.mp4" --keywords shared media
```

### Download via IDM with Routing

```bash
python scripts/python/download_router.py "output.mp4" --idm "https://example.com/video.mp4" --source "youtube"
```

### Copy Instead of Move

```bash
python scripts/python/download_router.py "file.pdf" --copy
```

## Integration with DSM Cloud Sync

### How It Works

1. **Download Request**: User/script requests download routing
2. **Routing Decision**: System determines appropriate cloud provider based on rules
3. **NAS Path Resolution**: File is routed to NAS Cloud Sync path (e.g., `/volume1/dropbox`)
4. **DSM Cloud Sync**: DSM Cloud Sync package automatically syncs to cloud provider
5. **Cloud Access**: File becomes available in Dropbox/OneDrive/etc.

### NAS Cloud Sync Paths

The system uses NAS paths that correspond to DSM Cloud Sync configurations:

- **Dropbox**: `/volume1/dropbox` → Syncs to Dropbox account
- **OneDrive**: `/volume1/onedrive` → Syncs to OneDrive account
- **Google Drive**: `/volume1/google_drive` → Syncs to Google Drive account

### Local Path Fallback

If NAS path is unavailable, the system falls back to:
- Local Dropbox path: `C:\Users\mlesn\Dropbox`
- Mapped network drives: `Z:\downloads`
- Network UNC paths: `\\nas-host\share`

## Integration Points

### IDM Integration

Downloads via IDM can be routed automatically:

```python
from download_router import DownloadRouter

router = DownloadRouter()
router.route_download_via_idm(
    url="https://example.com/video.mp4",
    filename="video.mp4",
    source="tv_monitor",
    keywords=["shared", "media"]
)
```

### TV Channel Monitor Integration

TV channel monitor can route downloads automatically:

```python
from download_router import DownloadRouter

router = DownloadRouter()
decision = router.route_download(
    file_path=Path("downloaded_video.mp4"),
    source="tv_monitor",
    keywords=["multiverse", "shared"]
)
```

## Provider Configuration

### Dropbox (Default)

- **Priority**: 1 (highest)
- **File Types**: Documents, media, videos, general
- **Max Size**: 2048 MB
- **NAS Path**: `/volume1/dropbox`
- **Local Path**: `C:\Users\mlesn\Dropbox`

### OneDrive

- **Priority**: 2
- **File Types**: Office documents
- **Max Size**: 1024 MB
- **NAS Path**: `/volume1/onedrive`
- **Status**: Disabled by default

### Google Drive

- **Priority**: 3
- **File Types**: General
- **Max Size**: 5120 MB
- **NAS Path**: `/volume1/google_drive`
- **Status**: Disabled by default

### NAS Direct (Fallback)

- **Priority**: 4 (lowest)
- **File Types**: Large files, temporary, local-only
- **Max Size**: Unlimited
- **NAS Path**: `/volume1/downloads`
- **Network Path**: `\\10.17.17.32\downloads`
- **Mapped Drive**: `Z:\downloads`

## Routing Examples

### TV Monitor Downloads

- **Source**: `tv_monitor`
- **Routing**: → Dropbox (via `by_source` rule)
- **Reason**: TV content is typically shared/collaborative

### YouTube Downloads

- **Source**: `youtube`
- **Routing**: → Dropbox
- **Reason**: Media files go to shared space

### LLM Model Downloads

- **Source**: `llm_models`
- **File Type**: Large files (`.gguf`, `.bin`)
- **Routing**: → NAS Direct
- **Reason**: Large files stay on NAS, not synced to cloud

### Documents

- **File Type**: Documents (`.pdf`, `.docx`)
- **Routing**: → Dropbox
- **Reason**: Documents are typically shared/collaborative

## Benefits

### Centralized Management

- Single point of control for download routing
- NAS acts as cloud aggregator
- Unified configuration

### Intelligent Routing

- Automatic routing based on file characteristics
- Keyword and source-aware routing
- Size and type optimization

### Cloud Integration

- Leverages existing DSM Cloud Sync package
- No additional cloud API integration needed
- Automatic sync to cloud providers

### Flexibility

- Multiple routing strategies
- Fallback mechanisms
- Configurable rules

## Troubleshooting

### NAS Path Not Accessible

- **Symptom**: Routing falls back to local paths
- **Solution**: Verify network connectivity, check NAS credentials, verify DSM Cloud Sync is running

### Provider Not Found

- **Symptom**: Routing fails or uses default
- **Solution**: Check provider is enabled in config, verify NAS sync path exists

### File Too Large

- **Symptom**: File routed to NAS Direct instead of cloud
- **Solution**: This is expected behavior for files exceeding provider max size

## See Also

- **DSM Cloud Sync**: Synology DSM Cloud Sync package documentation
- **IDM Integration**: `docs/system/LUMINA_IDM_CONFIG.md`
- **TV Channel Monitor**: `docs/system/TV_CHANNEL_MONITORING.md`
- **NAS Integration**: `docs/system/LUMINA_NAS_SSH_API.md`

