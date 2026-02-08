# Cursor IDE Todo Status Display System

## Overview

Real-time status tracking and display for:
- **@AGENT@MASTER.TODOLIST** - Master todo list status
- **@SUBAGENT@PADAWAN.LIST** - Subagent/Padawan todo list status

Quantified with **@PEAK** percentages and displayed in Cursor IDE UI/UX.

## Features

### Real-Time Status Tracking
- Automatic calculation of todo metrics
- Percentage tracking with @PEAK quantification
- Status file generation for Cursor IDE integration
- Live updates on todo changes

### @PEAK Quantification

**Weighted percentage calculation:**
- **Complete** = 100%
- **In Progress** = 50%
- **Pending** = 0%

**Formula:**
```
@PEAK = ((Complete × 100) + (In Progress × 50) + (Pending × 0)) / Total
```

### Status Metrics

**Per List:**
- Total todos
- Pending count
- In Progress count
- Complete count
- Cancelled count
- Priority breakdown (Critical, High, Medium, Low)
- @PEAK percentage

**Overall:**
- Combined @PEAK percentage (weighted by total todos)
- Active todos count
- Completed todos count

## Usage

### Command Line

```bash
python scripts/python/cursor_ide_todo_status_display.py
```

### Output

**Status File:**
- Location: `data/cursor_ide_status/todo_status.json`
- Format: JSON with complete status information
- Updates: Real-time on each execution

**Status Summary:**
```
@AGENT@MASTER: XX.X% @PEAK
  Total: XXX | Active: XXX | Complete: XXX
@SUBAGENT@PADAWAN: XX.X% @PEAK
  Total: XXX | Active: XXX | Complete: XXX
OVERALL: XX.X% @PEAK
```

**Status Bar Text:**
```
@MASTER: XX.X% | @PADAWAN: XX.X% | @PEAK: XX.X%
```

## Cursor IDE Integration

### Status File Monitoring

Cursor IDE can monitor the status file:
- **Path**: `data/cursor_ide_status/todo_status.json`
- **Update Frequency**: On-demand or scheduled
- **Format**: JSON for easy parsing

### Webview Panel

Create a Cursor IDE webview panel that:
- Reads `todo_status.json`
- Displays real-time status
- Shows @PEAK percentages
- Updates automatically

### Status Bar Integration

Display status in Cursor IDE status bar:
- **Text**: `@MASTER: XX.X% | @PADAWAN: XX.X% | @PEAK: XX.X%`
- **Click**: Opens detailed status view
- **Color**: Green (high %), Yellow (medium %), Red (low %)

### Extension Integration

Create a Cursor IDE extension that:
- Monitors status file changes
- Updates status bar automatically
- Provides command to refresh status
- Shows detailed view in webview panel

## Status File Structure

```json
{
  "master": {
    "metrics": {
      "total": 0,
      "pending": 0,
      "in_progress": 0,
      "complete": 0,
      "cancelled": 0,
      "percentage_complete": 0.0,
      "percentage_in_progress": 0.0,
      "high_priority": 0,
      "medium_priority": 0,
      "low_priority": 0,
      "critical_priority": 0
    },
    "last_updated": "2026-01-10T06:30:00.000000",
    "total_todos": 0,
    "active_todos": 0,
    "completed_todos": 0,
    "peak_percentage": 0.0
  },
  "padawan": {
    "metrics": { ... },
    "last_updated": "2026-01-10T06:30:00.000000",
    "total_todos": 0,
    "active_todos": 0,
    "completed_todos": 0,
    "peak_percentage": 0.0,
    "padawan_assignments": {}
  },
  "overall_percentage": 0.0,
  "timestamp": "2026-01-10T06:30:00.000000",
  "status_summary": "..."
}
```

## Implementation

### Python Script

**Location**: `scripts/python/cursor_ide_todo_status_display.py`

**Key Classes:**
- `CursorIDETodoStatusDisplay` - Main status display system
- `MasterTodoStatus` - Master todo list status
- `PadawanTodoStatus` - Padawan/Subagent todo list status
- `CursorIDEStatus` - Complete status for display
- `TodoStatusMetrics` - Metrics calculation

### Auto-Update

**Options:**
1. **File Watcher**: Monitor todo JSON files for changes
2. **Scheduled Task**: Run periodically (e.g., every 5 minutes)
3. **On-Demand**: Run via command or API call
4. **Git Hook**: Update on commit/push

## @PEAK Quantification

**Purpose**: Provide meaningful percentage that reflects actual progress.

**Why Weighted:**
- Complete tasks = 100% value
- In Progress tasks = 50% value (work started)
- Pending tasks = 0% value (not started)

**Example:**
- 10 total todos
- 5 complete (100% each) = 500
- 3 in progress (50% each) = 150
- 2 pending (0% each) = 0
- **@PEAK = (500 + 150 + 0) / 10 = 65%**

## Always Visible

**At All Times:**
- Status file always available
- Status bar text always visible
- Webview panel can stay open
- Command to refresh anytime

## Next Steps

1. **Create Cursor IDE Extension**
   - Monitor status file
   - Update status bar
   - Provide webview panel

2. **Auto-Refresh System**
   - File watcher for todo changes
   - Automatic status updates
   - Real-time display

3. **Enhanced Display**
   - Charts/graphs
   - Trend analysis
   - Priority breakdown
   - Padawan assignment view

---

**Tags**: #CURSOR_IDE #TODO_STATUS #MASTER_TODOLIST #PADAWAN_LIST #PEAK #QUANTIFICATION #UI_UX

**Created**: 2026-01-10
**Purpose**: Real-time todo status tracking and display in Cursor IDE UI/UX with @PEAK quantification
