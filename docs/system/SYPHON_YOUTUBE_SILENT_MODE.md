# @SYPHON YouTube Extraction - Silent Mode

## Issue Resolution

**Problem**: Multiple copies of YouTube videos playing out loud during @syphon extraction process.

**Solution**: Silent extraction mode with NEO browser preference.

## Configuration

**File**: `config/browser_config.json`

**Settings**:
- `default_browser`: "NEO"
- `prevent_video_autoplay`: true
- `mute_videos_by_default`: true
- `silent_extraction_mode`: true
- `prevent_multiple_playback`: true
- `close_tabs_after_extraction`: true

## YouTube URL Parameters

When extracting from YouTube, URLs are automatically modified:
- Add `?autoplay=0` to prevent autoplay
- Add `&mute=1` to mute audio
- Example: `https://youtu.be/VIDEO_ID?autoplay=0&mute=1`

## Usage

### Silent YouTube Extraction

```python
from syphon_youtube_extraction import extract_youtube_content_silent

result = extract_youtube_content_silent(
    url="https://youtu.be/j55FBPLV0zQ",
    use_neo=True  # Use NEO browser instead of default
)
```

### Command Line

```bash
python scripts/python/syphon_youtube_extraction.py <YOUTUBE_URL> --neo
```

## Browser Preference

**NEO Browser** is the preferred browser for all operations:
- Path: `C:\Users\mlesn\AppData\Local\Neo\Application\neo.exe`
- Status: ✅ Set as default browser
- MCP Browser: May still use Edge (needs configuration update)

## MCP Browser Configuration

**Note**: The Cursor IDE MCP browser extension may still use Edge by default. To force NEO:

1. Check MCP browser configuration
2. Update to use NEO browser path
3. Or use `set_neo_default_browser.py` to ensure NEO is system default

## Best Practices

1. **Always use silent mode** for YouTube extraction
2. **Close tabs after extraction** to prevent multiple playback
3. **Use NEO browser** for all browser operations
4. **Monitor for multiple tabs** and close duplicates
5. **Mute by default** during extraction processes

## Tags

- `#SYPHON` `#YOUTUBE` `#SILENT_MODE` `#NEO_BROWSER` `@JARVIS` `@LUMINA`

---

**Last Updated**: 2026-01-16  
**Status**: ✅ Active
