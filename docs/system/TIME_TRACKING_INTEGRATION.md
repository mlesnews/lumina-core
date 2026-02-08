# Time Tracking Integration - All Frameworks

## Overview

The AI Agent Live Monitor integrates **ALL time tracking frameworks**, with **PRIMARY focus on Cursor and WakaTime**.

## Integrated Time Tracking Frameworks

### Primary Frameworks

1. **WakaTime** (PRIMARY)
   - Real-time coding time tracking
   - API integration for live stats
   - Project-specific tracking
   - Language and editor statistics

2. **Cursor** (PRIMARY)
   - Cursor IDE workflow tracking
   - Cursor IDE mode tracking
   - Agent session tracking
   - Model usage tracking

### Additional Frameworks

3. **Comprehensive Analytics Tracker**
   - Aggregates all timekeeping sources
   - System resource monitoring
   - Cross-platform tracking

4. **WakaTime + Cursor Stats**
   - Combined WakaTime and Cursor statistics
   - Unified analytics dashboard

## Integration Points

### AI Agent Live Monitor

The live monitor tracks:
- **Current Task Time**: Time spent on current task
- **WakaTime Hours**: Total hours tracked by WakaTime
- **Cursor Tracked**: Whether Cursor is tracking
- **Last Sync**: Last synchronization timestamp

### Time Tracking Data Structure

```json
{
  "time_tracking": {
    "task_start_time": "2026-01-15T12:00:00",
    "total_time_seconds": 3600.0,
    "total_time_formatted": "1h 0m 0s",
    "wakatime_tracked": true,
    "cursor_tracked": true,
    "wakatime_hours": 8.5,
    "cursor_hours": 8.2,
    "last_sync": "2026-01-15T12:00:00"
  }
}
```

## Usage

### Automatic Tracking

Time tracking is **automatic** when:
- AI agent is active
- Task is set via `set_current_task()`
- Monitoring is running

### Manual Tracking

```python
from ai_agent_live_monitor import get_live_monitor

monitor = get_live_monitor()

# Set task (starts time tracking)
monitor.set_current_task("code_generation: generate_function")

# Time tracking updates automatically every 2 seconds
# View in live status file: data/ai_agent_monitor/live_status.json
```

## WakaTime Integration

### Configuration

1. **API Key**: Set `WAKATIME_API_KEY` environment variable
   - Or store in Azure Key Vault as `wakatime-api-key`

2. **Project**: Tracks time for "LUMINA" project

3. **Sync Interval**: Syncs every monitoring cycle (2 seconds)

### Data Retrieved

- **Today's Summary**: Total coding time for today
- **Project Time**: Time spent on LUMINA project
- **Language Stats**: Time by programming language
- **Editor Stats**: Time by editor (Cursor, VS Code, etc.)

## Cursor Integration

### Tracking Sources

1. **Cursor IDE Mode Tracker**
   - Tracks time in different IDE modes
   - Agent mode vs Editor mode
   - Daily and weekly statistics

2. **Cursor Workflow Tracking**
   - Tracks workflow execution time
   - Agent session duration
   - Model selection time

3. **Cursor Active Model Tracker**
   - Tracks time per model
   - Model switch events
   - Usage patterns

## Display

### Full Display

```
Time Tracking:
  Current Task Time: 1h 23m 45s
  ✅ WakaTime: 8.50 hours
  ✅ Cursor: Tracked
  Last Sync: 2026-01-15T12:00:00
```

### Compact Display

```
✅ [OPTIMAL] ULTRON / qwen2.5:72b | Time: 1h 23m | Success: 95.0% | Response: 0.50s
```

## Status File

Time tracking data is included in:
- `data/ai_agent_monitor/live_status.json`

## Tags

`#TIME_TRACKING` `#WAKATIME` `#CURSOR` `#ANALYTICS` `#TRANSPARENCY` `@LUMINA` `@JARVIS`

---

**Status**: ✅ **OPERATIONAL**  
**Primary**: WakaTime + Cursor  
**Update Interval**: 2 seconds  
**Auto-Sync**: Enabled
