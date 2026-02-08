# Cursor IDE Chat Screenshot Integration

**Date**: 2026-01-02  
**Status**: ✅ **IMPLEMENTED**  
**Tag**: #CURSOR #CHAT #SCREENSHOT #AUTOMATION #ATLAS-LIKE

---

## Overview

Automatically captures and attaches screenshots when errors are mentioned in Cursor IDE chat. Similar to OpenAI Atlas features - automatic visual context capture without manual screenshots.

**Problem Solved**: No more manually taking pictures when reporting errors in chat!

---

## How It Works

### Automatic Detection

The integration monitors chat messages for:
- **Error keywords**: error, failed, incorrect, not working, issue, problem, etc.
- **Screenshot requests**: screenshot, capture, show me, etc.

### Automatic Capture

When an error is detected or screenshot is requested:
1. ✅ Automatically captures screenshot
2. ✅ Saves with context description
3. ✅ Makes screenshot available for attachment
4. ✅ Provides path for easy sharing

---

## Usage

### In Cursor IDE Chat

Just mention an error or request a screenshot:

```
"I'm getting an authentication error"
→ Automatically captures screenshot

"Can you take a screenshot?"
→ Captures screenshot immediately

"The connection failed"
→ Automatically captures screenshot
```

### Manual Trigger

```powershell
# Analyze a message and capture if needed
python scripts/python/cursor_chat_screenshot_integration.py --message "I'm getting an error"
```

### Test Scenarios

```powershell
# Test different message types
python scripts/python/cursor_chat_screenshot_integration.py --test
```

---

## Integration Points

### With Cursor IDE

The integration can be:
- **Manual**: Run script when needed
- **Automatic**: Hook into Cursor chat (future enhancement)
- **On-demand**: Use `@manus capture` or similar trigger

### With MANUS

- Integrated with MANUS Unified Control
- Uses MANUS RDP Screenshot Capture
- Part of MANUS automation workflows

---

## Error Keywords That Trigger Capture

- error, failed, failure
- incorrect, wrong
- not working, doesn't work
- issue, problem, bug
- exception, crash, timeout
- authentication.*fail, auth.*error
- connection.*fail, can't connect
- unable to, screenshot, capture
- show me, see error

---

## Screenshot Request Phrases

- screenshot
- capture screen
- show screen
- take picture
- snap shot
- what you see
- what's showing

---

## Output

Screenshots are saved to:
- **Location**: `data/manus_rdp_captures/`
- **Format**: `rdp_screenshot_YYYYMMDD_HHMMSS.png`
- **Metadata**: `metadata_YYYYMMDD_HHMMSS.json`

---

## Examples

### Example 1: Error Mention

**Chat Message**: "I'm getting an incorrect authentication error"

**Result**:
- ✅ Error detected
- ✅ Screenshot captured automatically
- ✅ Path provided: `data/manus_rdp_captures/rdp_screenshot_20260102_120000.png`

### Example 2: Explicit Request

**Chat Message**: "Can you take a screenshot of the DSM error?"

**Result**:
- ✅ Screenshot requested
- ✅ Screenshot captured immediately
- ✅ Ready for attachment

### Example 3: No Action

**Chat Message**: "This is working fine now"

**Result**:
- ℹ️ No error detected
- ℹ️ No screenshot capture needed

---

## Future Enhancements

- [ ] **Auto-attach to chat**: Automatically attach screenshots to Cursor chat
- [ ] **Chat hook**: Monitor Cursor chat in real-time
- [ ] **Smart context**: AI analyzes screenshot to understand error
- [ ] **Video capture**: Record video when complex errors occur
- [ ] **OCR extraction**: Extract text from screenshots for analysis
- [ ] **Error correlation**: Match screenshots with error logs

---

## Configuration

### Enable/Disable Auto-Capture

```python
# Disable auto-capture (only capture on explicit request)
integration = CursorChatScreenshotIntegration(auto_capture=False)
```

### Custom RDP IP

```python
# Use different RDP server
integration = CursorChatScreenshotIntegration(rdp_ip="10.17.17.11")
```

---

## Integration Code

### In Your Scripts

```python
from cursor_chat_screenshot_integration import process_chat_message

# Process a chat message
result = process_chat_message("I'm getting an error", auto_capture=True)

if result["screenshot_path"]:
    print(f"Screenshot ready: {result['screenshot_path']}")
    # Attach to chat or use as needed
```

### With MANUS

```python
from manus_unified_control import MANUSUnifiedControl, ControlArea, ControlOperation

control = MANUSUnifiedControl(project_root)

# Capture screenshot via MANUS
operation = ControlOperation(
    operation_id="capture_001",
    area=ControlArea.RDP_CAPTURE,
    action="capture_with_context",
    parameters={"description": "Cursor chat error"}
)

result = control.execute_operation(operation)
if result.success:
    screenshot_path = result.data.get("screenshot_path")
```

---

## Benefits

✅ **No Manual Screenshots**: Automatic capture on error  
✅ **Context-Aware**: Captures with descriptions  
✅ **Easy Sharing**: Paths ready for attachment  
✅ **Atlas-Like**: Similar to OpenAI Atlas features  
✅ **Integrated**: Works with MANUS and Cursor  

---

## Troubleshooting

### Issue: Screenshots Not Capturing

**Solutions**:
- Check RDP connection is active
- Verify MANUS RDP Screenshot Capture is working
- Check output directory permissions

### Issue: Too Many Screenshots

**Solutions**:
- Disable auto-capture: `auto_capture=False`
- Adjust error keywords list
- Use explicit requests only

---

**Last Updated**: 2026-01-02  
**Status**: Ready to use  
**Script**: `scripts/python/cursor_chat_screenshot_integration.py`
