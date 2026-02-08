# MANUS RDP Screenshot & Video Capture

**Date**: 2026-01-02  
**Status**: ✅ **IMPLEMENTED**  
**Tag**: #MANUS #RDP #SCREENSHOT #VIDEO #AUTOMATION

**Remote desktop**: Prefer **TightVNC** over RDP for the remote session you are capturing; see [REMOTE_DESKTOP_TIGHTVNC.md](REMOTE_DESKTOP_TIGHTVNC.md). RDP remains supported.

---

## Overview

Automated screenshot and video capture from RDP sessions to avoid manual screenshots. Similar to OpenAI Atlas features - automatic visual context capture for troubleshooting and documentation.

**Problem Solved**: No more manually taking pictures of desktop/DSM interface!

---

## Features

✅ **Automatic Screenshot Capture**  
✅ **Video Recording Support**  
✅ **Context-Aware Captures** (with descriptions)  
✅ **Automatic Timestamping**  
✅ **Organized Storage**  

---

## Usage

### Quick Screenshot

```powershell
# Capture screenshot automatically
python scripts/python/manus_rdp_screenshot_capture.py --screenshot
```

### Capture with Context

```powershell
# Capture screenshot with description
python scripts/python/manus_rdp_screenshot_capture.py --context "DSM LDAP configuration error"
```

### List All Captures

```powershell
# List all captured screenshots/videos
python scripts/python/manus_rdp_screenshot_capture.py --list
```

### Video Recording

```powershell
# Start video recording
python scripts/python/manus_rdp_screenshot_capture.py --video
```

---

## Integration with MANUS

### From MANUS Unified Control

```python
from manus_rdp_screenshot_capture import MANUSRDPScreenshotCapture

# Initialize
capture = MANUSRDPScreenshotCapture(manus_ip="10.17.17.11")

# Capture screenshot
screenshot = capture.capture_screenshot()

# Capture with context
metadata = capture.capture_with_context("DSM configuration step 3")
```

---

## Output Location

**Default**: `data/manus_rdp_captures/`

**Files**:
- Screenshots: `rdp_screenshot_YYYYMMDD_HHMMSS.png`
- Videos: `rdp_recording_YYYYMMDD_HHMMSS.mp4`
- Metadata: `metadata_YYYYMMDD_HHMMSS.json`

---

## Requirements

### Windows
- PowerShell (built-in)
- Optional: Pillow (`pip install Pillow`) for better screenshot quality

### Video Recording
- **Option 1**: OBS Studio (recommended)
- **Option 2**: FFmpeg
- **Option 3**: Windows Game Bar (Win+G)

---

## Use Cases

1. **Troubleshooting**: Auto-capture error screens
2. **Documentation**: Capture configuration steps
3. **Debugging**: Visual context for issues
4. **Training**: Record procedures
5. **Support**: Share visual context easily

---

## Examples

### Capture DSM Error

```powershell
# When you see an error in DSM
python scripts/python/manus_rdp_screenshot_capture.py --context "DSM LDAP authentication error - incorrect auth info"
```

### Capture Configuration Step

```powershell
# During configuration
python scripts/python/manus_rdp_screenshot_capture.py --context "DSM SSO Server configuration - IdP Entity ID"
```

### Batch Capture

```powershell
# Capture multiple screenshots during setup
python scripts/python/manus_rdp_screenshot_capture.py --context "Step 1: Install SSO Server"
python scripts/python/manus_rdp_screenshot_capture.py --context "Step 2: Configure IdP"
python scripts/python/manus_rdp_screenshot_capture.py --context "Step 3: Configure Azure AD"
```

---

## Future Enhancements

- [ ] Automatic capture on error detection
- [ ] Integration with Cursor IDE chat (auto-attach screenshots)
- [ ] Video recording automation
- [ ] Cloud storage sync
- [ ] OCR text extraction from screenshots
- [ ] AI analysis of captured screens

---

## Integration Points

### With JARVIS
- Auto-capture on error detection
- Attach screenshots to JARVIS chat
- Visual context for troubleshooting

### With MANUS Unified Control
- Integrated into MANUS workflows
- Automatic capture during automation
- Context-aware captures

### With Cursor IDE
- Auto-attach screenshots to chat
- Visual context in conversations
- No more manual screenshots!

---

**Last Updated**: 2026-01-02  
**Status**: Ready to use  
**Script**: `scripts/python/manus_rdp_screenshot_capture.py`
