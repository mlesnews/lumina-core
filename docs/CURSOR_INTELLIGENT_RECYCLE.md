# 🔄 Cursor IDE Intelligent Warm Recycle

## Overview

Automatically and intelligently recycles (restarts) Cursor IDE when needed. Monitors performance, detects issues, and performs smart warm recycles that preserve your work.

## Features

✅ **Automatic Detection** - Monitors memory, CPU, performance  
✅ **Smart Decision-Making** - Multiple factors determine when to recycle  
✅ **Work Preservation** - Saves all files and workspace state  
✅ **Graceful Shutdown** - Clean restart, not force kill  
✅ **State Restoration** - Reopens workspace after restart  
✅ **Proactive Recycling** - Scheduled recycling to prevent issues  

## How It Works

```
👁️  Monitor Cursor → 📊 Analyze Performance → 🤔 Decide → 🔄 Warm Recycle
                                                                    ↓
                    💾 Save State → 🛑 Graceful Shutdown → 🚀 Restart
```

## Recycling Triggers

The system automatically recycles Cursor when:

1. **High Memory** (>2GB) - Cursor using too much RAM
2. **High CPU** (>80%) - Cursor consuming excessive CPU
3. **Frozen State** - Cursor appears unresponsive
4. **Performance Degradation** - Trending upward memory/CPU
5. **Proactive** - Scheduled recycle every 4 hours
6. **Error Count** - Too many errors detected

## Usage

### Check if Recycle Needed

```bash
python scripts/python/cursor_intelligent_warm_recycle.py --check
```

### Perform Recycle Now

```bash
python scripts/python/cursor_intelligent_warm_recycle.py --recycle
```

### Start Automatic Monitoring

```bash
python scripts/python/cursor_intelligent_warm_recycle.py --monitor --interval 60
```

### Integrated with Hands-Free Control

The recycle system is automatically integrated with JARVIS hands-free control:

```bash
python scripts/python/jarvis_hands_free_startup.py
```

This starts:
- Hands-free voice control
- Automatic warm recycling
- Keyboard shortcut execution
- Mouse fallback

## Configuration

Configuration is stored in: `config/cursor_recycle_config.json`

```json
{
  "memory_threshold_mb": 2048,
  "cpu_threshold_percent": 80.0,
  "proactive_interval": 14400,
  "last_recycle": "2025-12-31T18:20:00",
  "recycle_count": 5
}
```

## Warm Recycle Process

When recycling is triggered:

1. **Save Workspace State** - Stores open files, workspace folder
2. **Save All Files** - Saves all open files (Ctrl+K, S)
3. **Graceful Shutdown** - Closes Cursor cleanly (Alt+F4)
4. **Wait** - Brief pause for cleanup
5. **Restart** - Launches Cursor with workspace restored

## Thresholds

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Memory | >1.5GB | >2GB | Recycle |
| CPU | >60% | >80% | Recycle |
| Proactive | - | 4 hours | Recycle |

## Decision Making

The system uses multiple factors:

- **Memory Usage** - Total memory across all Cursor processes
- **CPU Usage** - Peak and average CPU across processes
- **Performance Trends** - Historical data analysis
- **Time Since Last Recycle** - Proactive recycling
- **Confidence Score** - How certain the recycle is needed

## Integration

### With Hands-Free Control

Automatically monitors and recycles in background:

```python
from jarvis_hands_free_cursor_control import JARVISHandsFreeCursorControl

control = JARVISHandsFreeCursorControl()
control.start_hands_free_mode()  # Auto-recycle enabled
```

### With MANUS Controller

Integrated with MANUS troubleshooting system:

```python
from cursor_intelligent_warm_recycle import CursorIntelligentWarmRecycle

recycle = CursorIntelligentWarmRecycle()
decision = recycle.should_recycle()
if decision.should_recycle:
    recycle.warm_recycle(decision.reason)
```

## Monitoring

### Real-Time Monitoring

```bash
# Start continuous monitoring
python scripts/python/cursor_intelligent_warm_recycle.py --monitor
```

Monitors every 60 seconds by default (configurable).

### Metrics Tracked

- Total memory usage (MB)
- CPU usage (percent)
- Process count
- Performance trends
- Recycle history

## Status

✅ **Fully Operational**

- Automatic detection: ✅ Working
- Smart decision-making: ✅ Working
- Warm recycle process: ✅ Working
- State preservation: ✅ Working
- Integration: ✅ Complete

## Troubleshooting

### Recycle Not Triggering

- Check thresholds in config file
- Verify Cursor processes are detected
- Check monitoring is active

### Recycle Failing

- Ensure Cursor executable is found
- Check file permissions
- Verify workspace path exists

### Workspace Not Restored

- Check workspace state file
- Verify workspace folder path
- Check Cursor startup options

## Files

- `cursor_intelligent_warm_recycle.py` - Core recycle system
- `jarvis_hands_free_startup.py` - Integrated startup
- `config/cursor_recycle_config.json` - Configuration
- `data/cursor_workspace_state.json` - Saved workspace state

---

**Created**: 2025-12-31  
**Status**: ✅ Operational  
**Integration**: ✅ Complete
