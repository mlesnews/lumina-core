# JARVIS Live Monitor & Maintenance System

## Overview

The JARVIS Live Monitor & Maintenance System provides **progressive percentage tracking** and **ongoing live monitoring & maintenance** for all JARVIS, AI, agents, and subagents processes.

## Features

### Progressive Percentage Tracking

- **Overall Progress**: Real-time percentage tracking across all active processes
- **Per-Process Breakdown**: Individual progress percentages for each process
- **Source Tracking**: Total sources, current sources being processed
- **ETA Calculation**: Estimated time to completion for all processes
- **System Health**: Overall system health percentage based on success/failure rates

### Ongoing Live Monitoring

- **Update Interval**: 0.5 seconds (configurable)
- **Continuous Monitoring**: Background thread monitors all processes
- **Real-Time Updates**: Status files updated every 0.5 seconds
- **Cursor IDE Integration**: Live updates displayed in Cursor IDE footer

### Maintenance Tasks

The system runs 4 maintenance tasks continuously:

1. **System Health Check** (every 5 seconds)
   - Monitors process states (running, completed, failed)
   - Calculates overall system health percentage
   - Tracks process counts

2. **Progress Update** (every 0.5 seconds)
   - Updates progressive percentage calculations
   - Recalculates ETA for all processes
   - Updates source counts

3. **Status File Write** (every 1 second)
   - Writes status to `live_monitor_status.json` (internal)
   - Writes enhanced status to `cursor_status.json` (Cursor IDE extension)
   - Ensures Cursor IDE footer displays live updates

4. **Cleanup Old Data** (every 5 minutes)
   - Removes status files older than 24 hours
   - Maintains clean data directory

## Usage

### Starting Live Monitoring

```python
from jarvis_live_monitor_maintenance import get_live_monitor

# Get or create live monitor instance
live_monitor = get_live_monitor(project_root=project_root, update_interval=0.5)

# Start monitoring (if not already active)
if not live_monitor.monitoring_active:
    live_monitor.start_monitoring()
```

### Getting Live Status

```python
status = live_monitor.get_live_status()

# Progressive percentage
pp = status["progressive_percentage"]
print(f"Overall Progress: {pp['overall']:.1f}%")
print(f"Active Processes: {pp['active_processes']}")
print(f"Total Sources: {pp['total_sources']}")
print(f"ETA: {pp['eta']}")

# System health
sh = status["system_health"]
print(f"System Health: {sh['overall_health_percent']:.1f}%")
print(f"Processes Running: {sh['processes_running']}")
```

### CLI Interface

```bash
# Start monitoring
python scripts/python/jarvis_live_monitor_maintenance.py --start

# Stop monitoring
python scripts/python/jarvis_live_monitor_maintenance.py --stop

# Show status
python scripts/python/jarvis_live_monitor_maintenance.py --status

# Custom update interval
python scripts/python/jarvis_live_monitor_maintenance.py --start --interval 0.3
```

## Integration

### With @ASK Chain Execution

The live monitor is automatically integrated with `execute_ask_chains_doit.py`:

```python
# Automatically starts live monitoring
python scripts/python/execute_ask_chains_doit.py
```

### With Progress Tracker

The live monitor integrates with `jarvis_progress_tracker.py`:

- Reads process status from progress tracker
- Calculates progressive percentages from process data
- Updates Cursor IDE extension status file
- Provides enhanced status with system health metrics

### With Cursor IDE Extension

The Cursor IDE extension (`.vscode/extensions/lumina-progress-status/`) reads from:
- `data/progress_tracking/cursor_status.json`

The live monitor writes enhanced status to this file with:
- Progressive percentage data
- System health metrics
- Signboard text for scrolling display
- Process breakdown

## Status Files

### `live_monitor_status.json` (Internal)

Internal status file for monitoring system:

```json
{
  "timestamp": "2026-01-02T18:00:00",
  "monitoring_active": true,
  "progressive_percentage": {
    "overall": 45.5,
    "active_processes": 3,
    "total_sources": 100,
    "current_sources": 45,
    "eta": "2h 15m",
    "breakdown": {
      "process_1": 50.0,
      "process_2": 40.0,
      "process_3": 46.5
    }
  },
  "system_health": {
    "overall_health_percent": 95.0,
    "processes_running": 3,
    "processes_completed": 10,
    "processes_failed": 0
  }
}
```

### `cursor_status.json` (Cursor IDE Extension)

Enhanced status file for Cursor IDE footer display:

```json
{
  "timestamp": "2026-01-02T18:00:00",
  "monitoring_active": true,
  "aggregate": {
    "overall_percentage": 45.5,
    "max_sources_processing": 45,
    "total_sources": 100,
    "active_processes": 3,
    "eta": "2h 15m",
    "progressive_percentage": 45.5
  },
  "progressive": {
    "overall": 45.5,
    "active_processes": 3,
    "total_sources": 100,
    "current_sources": 45,
    "eta": "2h 15m",
    "system_health": 95.0
  },
  "signboard_text": "JARVIS: 45.5% | 3 active | 45/100 sources | ETA: 2h 15m",
  "processes": [...]
}
```

## Display Format

### Cursor IDE Footer

The extension displays:
- **Scrolling Text**: Airport signboard effect with compact status
- **Tooltip**: Full details on hover/click
- **Color Coding**:
  - Green (≥90%): Near completion
  - Default (50-89%): Normal progress
  - Yellow (<50%): Early stage

### Example Display

```
🔄 JARVIS: 45.5% | 3 active | 45/100 sources | ETA: 2h 15m
```

## Architecture

### Components

1. **JARVISLiveMonitor**: Main monitoring class
   - Manages monitoring thread
   - Runs maintenance tasks
   - Calculates progressive percentages
   - Updates status files

2. **SystemHealth**: Health metrics dataclass
   - Overall health percentage
   - Process counts (running, completed, failed)
   - Issues and warnings

3. **ProgressivePercentage**: Progress tracking dataclass
   - Overall percentage
   - Per-process breakdown
   - Source counts
   - ETA calculation

### Threading

- **Main Thread**: User code execution
- **Monitor Thread**: Background monitoring (daemon thread)
  - Updates every 0.5 seconds
  - Runs maintenance tasks
  - Writes status files

## Configuration

### Update Interval

Default: `0.5` seconds (500ms)

Can be configured:
```python
live_monitor = get_live_monitor(update_interval=0.3)  # 300ms updates
```

### Maintenance Task Intervals

- Health Check: 5 seconds
- Progress Update: 0.5 seconds
- Status File Write: 1 second
- Cleanup: 5 minutes

## Mode: @LUMINA @CORE as @BAU

The system operates in **Business As Usual (BAU)** mode:
- Default mode for all operations
- Continuous monitoring and maintenance
- Progressive percentage tracking enabled
- Live updates to Cursor IDE

## Tags

- `@JARVIS` - JARVIS system integration
- `@LIVE` - Live monitoring
- `@MONITORING` - Continuous monitoring
- `@MAINTENANCE` - Maintenance tasks
- `#PROGRESSIVE` - Progressive percentage tracking
- `#PERCENTAGE` - Percentage calculations
- `#TRACKING` - Progress tracking

## Related Systems

- **JARVIS Progress Tracker**: Core progress tracking
- **Cursor IDE Extension**: Footer display
- **@ASK Chain Executor**: Automatic integration
- **Complete Workflow Chain**: Full system integration
