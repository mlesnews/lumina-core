# IDE Idle Countdown Timer

## Overview

The IDE Idle Countdown Timer displays a real-time countdown in the IDE footer showing:
- Time remaining until restrictions (10-minute breather)
- Current idle duration
- Status (ACTIVE, IDLE, RESTRICTED)
- Proper scrolling and word-wrapping support

## Features

### Real-Time Updates
- Updates every second
- Background thread keeps status current
- Status file updated for IDE integration

### Display Formats

#### Compact Display (Default)
```
🟢 @OP ACTIVE | Breather: 09:45
🟡 @OP IDLE | Breather: 05:23
🔴 @OP RESTRICTED | Idle: 12:34
```

#### Short Display (Minimal)
```
🟢 09:45
🟡 05:23
🔴 RESTRICTED
```

#### Full Display (Word-Wrapping)
```
🟢 @OP ACTIVE | Breather Remaining: 09:45 (of 10min) | Restrictions: INACTIVE
🟡 @OP IDLE | Breather Remaining: 05:23 (of 10min) | Restrictions: PENDING
🔴 @OP RESTRICTED | Idle: 12:34 (12.6min) | Restrictions: ACTIVE | Actions: BLOCKED
```

### Scrolling and Word-Wrapping

The countdown timer supports:
- **Horizontal Scrolling**: Long text scrolls horizontally
- **Word-Wrapping**: Text wraps to multiple lines when needed
- **Ellipsis**: Long text truncated with "..." when space is limited
- **Responsive**: Adapts to available footer space

## Usage

### CLI Interface

```bash
# Show current status
python scripts/python/jarvis_ide_idle_countdown.py --status

# Get footer text (compact)
python scripts/python/jarvis_ide_idle_countdown.py --footer

# Get short footer text (minimal)
python scripts/python/jarvis_ide_idle_countdown.py --footer-short

# Get full footer text (word-wrapping)
python scripts/python/jarvis_ide_idle_countdown.py --footer-full

# Watch countdown in real-time
python scripts/python/jarvis_ide_idle_countdown.py --watch

# Get HTML footer (if IDE supports HTML)
python scripts/python/jarvis_ide_idle_countdown.py --html
```

### Cursor IDE Integration

```bash
# Get status bar text for Cursor IDE
python scripts/python/cursor_ide_countdown_extension.py --text

# Get full status bar text (word-wrapping)
python scripts/python/cursor_ide_countdown_extension.py --full

# Watch countdown file for changes
python scripts/python/cursor_ide_countdown_extension.py --watch
```

## Status File

The countdown status is written to:
- **File**: `data/ide_countdown/countdown_status.json`
- **Update Frequency**: Every 1 second
- **Format**: JSON with all status information

### Status File Structure

```json
{
  "status": "active",
  "status_message": "🟢 ACTIVE - Breather: 09:45",
  "countdown_seconds": 585,
  "countdown_display": "09:45",
  "idle_duration_seconds": 15,
  "idle_display": "00:15",
  "timeout_seconds": 600,
  "timeout_minutes": 10.0,
  "footer_display": "🟢 @OP ACTIVE | Breather: 09:45",
  "footer_display_short": "🟢 09:45",
  "footer_display_full": "🟢 @OP ACTIVE | Breather Remaining: 09:45 (of 10min) | Restrictions: INACTIVE",
  "timestamp": "2026-01-02T07:20:00.000000"
}
```

## Integration with Cursor IDE

### Option 1: Status Bar Integration

Add to Cursor IDE settings or extension:
```json
{
  "statusBar": {
    "items": [
      {
        "id": "jarvis-idle-countdown",
        "text": "${countdown}",
        "command": "python scripts/python/cursor_ide_countdown_extension.py --text"
      }
    ]
  }
}
```

### Option 2: File Watcher

Watch the status file and update IDE footer:
```bash
python scripts/python/cursor_ide_countdown_extension.py --watch
```

### Option 3: Custom Extension

Create a Cursor IDE extension that:
1. Watches `data/ide_countdown/countdown_status.json`
2. Updates status bar with countdown text
3. Handles scrolling and word-wrapping

## Display States

### 🟢 ACTIVE
- Operator is active
- Countdown shows time remaining in breather
- Restrictions: INACTIVE

### 🟡 IDLE
- Operator is idle but within breather period
- Countdown shows time remaining until restrictions
- Restrictions: PENDING

### 🔴 RESTRICTED
- Operator idle for >10 minutes
- Shows total idle duration
- Restrictions: ACTIVE
- Actions: BLOCKED

## Word-Wrapping Support

The countdown timer provides multiple display formats:

1. **Compact**: Single line, scrolls horizontally
2. **Short**: Minimal text, fits in small space
3. **Full**: Detailed text, word-wraps to multiple lines

All formats support:
- Proper text wrapping
- Horizontal scrolling when needed
- Ellipsis truncation for long text
- Responsive sizing

## Real-Time Updates

The countdown updates:
- **Every 1 second** in background thread
- **Status file** updated continuously
- **IDE integration** can watch file for changes
- **No performance impact** (lightweight updates)

## Troubleshooting

### Countdown Not Updating
- Check if idleness restriction is available
- Verify status file is being written
- Check logs for errors

### Footer Not Scrolling
- Ensure IDE supports status bar updates
- Check file watcher is running
- Verify status file path is correct

### Word-Wrapping Not Working
- Use `--footer-full` for word-wrapping format
- Check IDE supports multi-line status bar
- Verify text length isn't exceeding limits

## Tags

@JARVIS #IDLE_COUNTDOWN #IDE_FOOTER #STATUS_BAR #REALTIME #SCROLLING #WORD_WRAPPING #CURSOR
