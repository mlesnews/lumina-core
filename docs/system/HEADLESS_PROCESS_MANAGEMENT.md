# Headless Process Management System

**Status**: ✅ **OPERATIONAL**

**Date**: 2026-01-06

## Overview

All processes now run as background daemons with:
- ✅ **No visible terminals** (headless/daemon mode)
- ✅ **Full logging module integration** (all output to log files)
- ✅ **JARVIS workflow tracking, tracing, and hooking**
- ✅ **Comprehensive workflow/subworkflow monitoring**

## Problem Solved

**Before**: Processes were spawning with `CREATE_NEW_CONSOLE` flag, causing visible terminal windows to open and close.

**After**: All processes run headless using:
- `DETACHED_PROCESS` (0x00000008) + `CREATE_NO_WINDOW` (0x08000000) on Windows
- Daemon mode on Unix/Linux
- All output redirected to log files in `logs/` directory

## Components

### 1. Headless Process Manager (`headless_process_manager.py`)

Manages all process spawning in headless mode:

**Features:**
- ✅ Headless/daemon process execution
- ✅ Full logging to `logs/{process_name}_{date}.log`
- ✅ JARVIS workflow tracking integration
- ✅ Environment variable injection for workflow IDs
- ✅ Process lifecycle management

**Usage:**
```bash
python scripts/python/headless_process_manager.py --start ironman --script scripts/python/ironman_virtual_assistant.py --workflow-id workflow_001
```

### 2. JARVIS Workflow Tracker (`jarvis_workflow_tracker.py`)

Comprehensive workflow tracking system:

**Features:**
- ✅ Workflow and subworkflow tracking
- ✅ Process tracking within workflows
- ✅ Trace logging for all events
- ✅ Hook system for workflow interception
- ✅ JARVIS memory integration
- ✅ Persistent trace storage

**Event Types:**
- `workflow_start` / `workflow_end`
- `subworkflow_start` / `subworkflow_end`
- `process_start` / `process_end`
- `process_error`
- `hook_triggered`

**Usage:**
```bash
# List all workflows
python scripts/python/jarvis_workflow_tracker.py --list

# Get trace for workflow
python scripts/python/jarvis_workflow_tracker.py --trace workflow_001

# Show workflow status
python scripts/python/jarvis_workflow_tracker.py --status
```

### 3. Updated Process Managers

All process managers updated to use headless mode:

- ✅ `ai_managed_va_orchestrator.py` - Uses headless process manager
- ✅ `ai_managed_live_operations.py` - Headless process spawning
- ✅ `intelligent_process_recycler.py` - Headless recycling
- ✅ `restart_all_vas.py` - Headless VA restarts

## Logging Integration

### Log File Structure

All processes log to: `logs/{process_name}_{YYYYMMDD}.log`

**Example:**
- `logs/ironman_20260106.log`
- `logs/kenny_20260106.log`
- `logs/ai_managed_va_orchestrator_20260106.log`

### Logging Features

- ✅ All stdout/stderr captured
- ✅ Timestamped entries
- ✅ Workflow ID tracking
- ✅ Process ID tracking
- ✅ Error logging with stack traces

## JARVIS Integration

### Workflow Tracking

All workflows are automatically tracked:
- Workflow start/end events
- Subworkflow tracking
- Process tracking
- Error tracking
- Hook execution

### JARVIS Memory Storage

Workflow traces stored in:
- JARVIS episodic memory
- `data/jarvis_workflow_traces.json`
- JARVIS intelligence directory

### Hook System

Hooks can be registered for:
- Pre-workflow execution
- Post-workflow execution
- Pre-subworkflow execution
- Post-subworkflow execution
- Error handling
- Completion handling

## Workflow Trace Structure

```json
{
  "workflow_id": "va_ironman_1234567890",
  "name": "VA Start: ironman",
  "status": "completed",
  "start_time": "2026-01-06T01:08:00",
  "end_time": "2026-01-06T01:08:05",
  "subworkflows": ["subworkflow_001"],
  "processes": [49372],
  "traces": [
    {
      "timestamp": "2026-01-06T01:08:00",
      "event_type": "workflow_start",
      "message": "Workflow 'VA Start: ironman' started"
    },
    {
      "timestamp": "2026-01-06T01:08:01",
      "event_type": "process_start",
      "process_id": 49372,
      "message": "Process 'ironman' (PID: 49372) started"
    }
  ]
}
```

## Integration Points

### AI-Managed VA Orchestrator

- Uses `HeadlessProcessManager` for all VA starts
- Integrates `JARVISWorkflowTracker` for tracking
- Logs all actions to JARVIS
- Tracks workflow lifecycle

### AI-Managed Live Operations

- Headless process spawning
- Workflow tracking for all operations
- JARVIS integration for orchestration

### Intelligent Process Recycler

- Headless recycling
- Workflow tracking for recycling actions
- JARVIS logging

## Benefits

1. **No Visible Terminals**: All processes run silently in background
2. **Full Logging**: All output captured to log files
3. **Workflow Tracking**: Complete visibility into all workflows
4. **JARVIS Integration**: All workflows tracked in JARVIS memory
5. **Hooking System**: Intercept and modify workflow execution
6. **Traceability**: Complete audit trail of all operations

## Configuration

### Environment Variables

Processes receive:
- `LUMINA_LOG_DIR`: Log directory path
- `LUMINA_WORKFLOW_ID`: Current workflow ID
- `LUMINA_SUBWORKFLOW_ID`: Current subworkflow ID (if applicable)

### Log Directory

Default: `logs/` in project root

Can be configured via `LUMINA_LOG_DIR` environment variable.

## Usage Examples

### Start Process Headless

```python
from headless_process_manager import HeadlessProcessManager

manager = HeadlessProcessManager(project_root)
manager.start_headless_process(
    name="ironman",
    script_path=project_root / "scripts" / "python" / "ironman_virtual_assistant.py",
    workflow_id="workflow_001"
)
```

### Track Workflow

```python
from jarvis_workflow_tracker import JARVISWorkflowTracker

tracker = JARVISWorkflowTracker(project_root)
workflow = tracker.start_workflow("workflow_001", "My Workflow")
tracker.add_process("workflow_001", 12345, "my_process")
tracker.add_trace("workflow_001", "custom_event", "Custom message")
tracker.end_workflow("workflow_001")
```

### Register Hook

```python
def my_hook(workflow_id, subworkflow_id):
    print(f"Hook triggered for {workflow_id}")

tracker.register_hook(
    hook_id="my_hook",
    hook_type=HookType.PRE_WORKFLOW,
    callback=my_hook
)
```

## Tags

#HEADLESS #DAEMON #LOGGING #JARVIS #WORKFLOW_TRACKING #TRACING #HOOKING @JARVIS @LUMINA
