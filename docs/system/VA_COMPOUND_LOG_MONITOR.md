# Virtual Assistant Compound Log Monitor

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24  
**ORDER 66: @DOIT**

---

## Overview

The Virtual Assistant Compound Log Monitor provides **LIVE-MONITORING** of all virtual assistant logs with:
- **Real-time tailing** of log files
- **Compound log parsing** (combines multiple log sources)
- **Event detection** from log patterns
- **Live monitoring** with callbacks and handlers
- **Statistics and analytics**

---

## Features

### 1. Compound Log Parsing

Monitors logs from all Virtual Assistants:
- **IMVA** (Iron Man Virtual Assistant)
- **ACVA** (Anakin/Vader Combat Virtual Assistant)
- **ULTRON**
- **JARVIS VA**
- All other VAs

### 2. Real-Time Tailing

- **Live monitoring** with 100ms polling interval
- **Tails from end of file** (new entries only)
- **Tracks file positions** to avoid re-reading
- **Multi-file monitoring** (all VAs simultaneously)

### 3. Log Parsing

Parses multiple log formats:
- ISO timestamp format: `2025-01-24T18:00:00 [LEVEL] message`
- Standard format: `2025-01-24 18:00:00,123 [LEVEL] message`
- Simple format: `LEVEL: message`

Extracts:
- Timestamps
- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Messages
- Source file information

### 4. Event Detection

Automatically detects events from log patterns:

- **STARTED**: VA started/initialized/online
- **STOPPED**: VA stopped/closed/exited
- **ERROR**: Errors/exceptions/failures
- **COMBAT_STARTED**: Combat/fight started
- **COMBAT_ENDED**: Combat/fight ended
- **VOICE_COMMAND**: Voice commands detected
- **INTERACTION**: User interactions (clicks, etc.)
- **SYSTEM_ALERT**: Alerts/warnings/notifications
- **POSITION_CHANGED**: Position changes
- **HEALTH_CHANGED**: Health/damage changes
- **STATE_CHANGED**: State/mode changes

### 5. Statistics

Tracks:
- Total log entries
- Entries by VA
- Entries by log level
- Events detected (by type)
- Monitoring duration

---

## Usage

### Command Line

```bash
# Show statistics
python scripts/python/va_compound_log_monitor.py --stats

# Tail logs in real-time (live monitoring)
python scripts/python/va_compound_log_monitor.py --tail

# Show recent logs (last 50)
python scripts/python/va_compound_log_monitor.py --recent 50

# Show recent logs for specific VA
python scripts/python/va_compound_log_monitor.py --recent 50 --va-id imva

# Show recent events
python scripts/python/va_compound_log_monitor.py --events --recent 100
```

### Python API

```python
from va_compound_log_monitor import (
    VACompoundLogMonitor,
    VAEventType,
    LogEntry,
    VAEvent
)

# Initialize monitor
monitor = VACompoundLogMonitor()

# Start live monitoring with callback
def on_log(log_entry: LogEntry):
    print(f"[{log_entry.timestamp}] [{log_entry.va_id}] {log_entry.message}")

monitor.start_monitoring(callback=on_log)

# Add event handler
def on_combat_started(event: VAEvent):
    print(f"⚔️  Combat started: {event.va_id}")

monitor.add_event_handler(VAEventType.COMBAT_STARTED, on_combat_started)

# Get recent logs
recent_logs = monitor.get_recent_logs(count=100, va_id="imva")

# Get recent events
recent_events = monitor.get_recent_events(count=50, event_type=VAEventType.ERROR)

# Get statistics
stats = monitor.get_statistics()
print(f"Total entries: {stats['stats']['total_entries']}")

# Stop monitoring
monitor.stop_monitoring()
```

---

## Event Types

### VAEventType Enum

- `STARTED` - VA started
- `STOPPED` - VA stopped
- `ERROR` - Error occurred
- `COMBAT_STARTED` - Combat started
- `COMBAT_ENDED` - Combat ended
- `VOICE_COMMAND` - Voice command detected
- `INTERACTION` - User interaction
- `SYSTEM_ALERT` - System alert
- `POSITION_CHANGED` - Position changed
- `HEALTH_CHANGED` - Health changed
- `STATE_CHANGED` - State changed

---

## Log File Discovery

The monitor automatically discovers log files from:
- `data/logs/`
- `data/vas/`
- `logs/`

Log files are identified by filename patterns:
- `imva`, `ironman`, `iron_man` → IMVA
- `acva`, `anakin` → ACVA
- `ultron` → ULTRON
- `jarvis.*va` → JARVIS VA

---

## Architecture

### Components

1. **VACompoundLogMonitor**: Main monitor class
2. **LogEntry**: Structured log entry
3. **VAEvent**: Detected event from logs
4. **Event Handlers**: Callback system for events
5. **Statistics**: Real-time statistics tracking

### Monitoring Loop

1. **Initialize**: Discover log files, set file positions
2. **Poll**: Check each log file for new entries (100ms interval)
3. **Parse**: Parse new log lines into LogEntry objects
4. **Detect**: Detect events from log patterns
5. **Notify**: Call event handlers and callbacks
6. **Buffer**: Store in circular buffers (logs and events)
7. **Stats**: Update statistics

---

## Performance

- **Polling Interval**: 100ms (10 checks/second)
- **Log Buffer**: 1000 entries (circular buffer)
- **Event Buffer**: 500 events (circular buffer)
- **Multi-file**: Monitors all log files simultaneously
- **Efficient**: Only reads new log entries (tailing)

---

## Integration

The monitor integrates with:
- **LUMINA Logger**: Standard logging system
- **Virtual Assistants**: All VA log files
- **Event Systems**: Event handlers for notifications
- **Statistics Systems**: Real-time analytics

---

## Tags

#VAS #LOGS #MONITORING #TAILING #PARSING #LIVE #ORDER66 #DOIT @JARVIS @TEAM

---

**ORDER 66: @DOIT EXECUTED** ✅
