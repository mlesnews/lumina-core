# LUMINA Visual Progress Tracking Guide

LUMINA provides a comprehensive system for visual progress tracking, featuring real-time terminal meters, ETA calculations, and IDE status bar integration.

## 🚀 Visual Progressive Meter (CLI)

Use the `lumina_visual_meter.py` utility to track long-running tasks. This script integrates with the JARVIS Progress Tracker and updates the Cursor IDE status bar.

### Basic Usage

```bash
# Update progress for a task
python scripts/python/lumina_visual_meter.py --process "Data Move" --total 1000 --current 250 --show-bar
```

### Options

| Flag | Description |
|------|-------------|
| `--process` | Name of the process (e.g., "NAS Migration") |
| `--total` | Total number of items/files to process |
| `--current` | Current number of items completed |
| `--show-bar` | Show a visual progress bar in the terminal |
| `--complete` | Mark the process as 100% complete |
| `--fail "msg"` | Mark the process as failed with an error message |
| `--source` | Source of the task (defaults to LUMINA-CLI) |

### Integration with @DOIT / @BDA

You can use the meter within your automated scripts:

```python
from jarvis_progress_tracker import get_progress_tracker

tracker = get_progress_tracker()
tracker.register_process("task_id", "Task Name", "Source", total_items)

# ... inside loop ...
tracker.update_progress("task_id", current_count)

# ... on completion ...
tracker.complete_process("task_id")
```

## 📊 IDE Integration

The **Lumina Progress Status** extension automatically reads progress from the system and displays it in your Cursor footer.

### Features:
- **Scrolling Signboard**: Shows active tasks and percentages in the status bar.
- **Dynamic Tooltips**: Hover over the progress item to see detailed ETA and source counts.
- **Status Colors**: Changes color based on progress (Orange for < 50%, Green for > 90%).

## ⏱️ Real-time Migration Monitoring

For the NAS migration specifically, you can use the dedicated monitor:

```bash
python scripts/python/monitor_migration_progress.py
```

This provides a full-screen dashboard showing:
- Maximum files and current progress
- Percentage complete
- Projected ETA based on transfer speed
- Space freed (GB)

## 🧬 Under the Hood

The system uses `data/progress_tracking/cursor_status.json` as the central exchange for progress data. This file is updated by the `JARVISProgressTracker` class, which handles thread-safe aggregation and ETA projection using linear regression based on elapsed time.

### Key Files:
- `scripts/python/jarvis_progress_tracker.py`: Core tracking logic.
- `scripts/python/lumina_visual_meter.py`: CLI wrapper.
- `.vscode/extensions/lumina-progress-status/`: IDE status bar extension.
- `data/progress_tracking/cursor_status.json`: Live state data.

---
**Tags**: #PROGRESS #TRACKING #ETA #VISUAL #JARVIS #LUMINA @JARVIS @LUMINA
