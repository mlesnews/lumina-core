# MCP Browser Configuration - NEO vs Edge

## Issue

**Problem**: Cursor IDE MCP browser extension uses Microsoft Edge by default, not NEO browser.

**User Preference**: NEO browser should be used for all browser operations.

## Current Status

- **System Default Browser**: ✅ NEO (verified)
- **MCP Browser Extension**: ❌ Uses Edge (Cursor IDE limitation)
- **NEO Browser**: ✅ Installed and configured
- **Path**: `C:\Users\mlesn\AppData\Local\Neo\Application\neo.exe`

## MCP Browser Extension Behavior

The Cursor IDE MCP browser extension (`cursor-ide-browser`) uses:
- **Microsoft Edge** as the underlying browser engine
- This is a **Cursor IDE limitation**, not a system configuration issue
- The extension may not respect system default browser settings

## Workarounds

### 1. Use NEO Browser Directly

For YouTube extraction and other operations, use NEO browser directly:

```python
from set_neo_default_browser import NeoDefaultBrowserSetter

setter = NeoDefaultBrowserSetter()
setter.open_url_in_neo("https://youtube.com/watch?v=VIDEO_ID")
```

### 2. Silent Mode for @SYPHON

When using @syphon for YouTube extraction:
- Use silent mode: `?autoplay=0&mute=1`
- Close tabs after extraction
- Prevent multiple playback

### 3. Post-SYPHON Cleanup

After @syphon extraction:
- Close all browser tabs
- Stop any playing videos
- Verify no audio is playing

## Configuration Files

- **Browser Config**: `config/browser_config.json`
- **NEO Setter**: `scripts/python/set_neo_default_browser.py`
- **SYPHON YouTube**: `scripts/python/syphon_youtube_extraction.py`

## Recommendations

1. **For MCP Browser Operations**: Accept that Edge will be used (Cursor IDE limitation)
2. **For Direct Browser Operations**: Always use NEO browser via `set_neo_default_browser.py`
3. **For YouTube Extraction**: Use silent mode to prevent audio playback
4. **Post-Extraction**: Always close tabs and stop playback

## Future Improvements

- Request Cursor IDE to support custom browser selection for MCP extension
- Create wrapper that intercepts MCP browser calls and routes to NEO
- Monitor for MCP browser configuration options

## Tags

- `#MCP_BROWSER` `#NEO_BROWSER` `#EDGE` `#CURSOR_IDE` `@JARVIS` `@LUMINA`

---

**Last Updated**: 2026-01-16  
**Status**: ⚠️ Workaround Required
