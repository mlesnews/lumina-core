# Unified Queue System

The unified queue system treats all queue items the same way - whether they're sources (SYPHON + IDM), VSCode problems, tasks, or notifications. This provides a consistent interface for managing all types of work items.

## Overview

The unified queue system integrates:
- **Sources Queue** (AI SYPHON + IDM Orchestrator)
- **VSCode Problems** (linter errors, build issues)
- **Tasks** (general work items)
- **Notifications** (system alerts)
- **Alerts** (critical issues)

All items flow through the same queue interface with:
- Unified status tracking
- Consistent priority system
- Same filtering and sorting
- Unified display/viewer

## Key Concept

> **Sources are treated exactly like VSCode problems and other queue items**

This means:
- Same API for adding items
- Same status workflow
- Same priority system
- Same viewing interface
- Same management tools

## Queue Item Types

| Type | Description | Example |
|------|-------------|---------|
| `SOURCE` | Sources queue items (SYPHON + IDM) | YouTube channel, website URL |
| `PROBLEM` | VSCode problems | Linter errors, build failures |
| `TASK` | General tasks | Code review, documentation |
| `NOTIFICATION` | System notifications | Updates, reminders |
| `ALERT` | Critical alerts | System errors, failures |

## Unified Status

All items use the same status workflow:

```
PENDING → QUEUED → PROCESSING → COMPLETED
                              ↓
                            FAILED
```

- **PENDING**: Item created, waiting to start
- **QUEUED**: Item queued for processing
- **PROCESSING**: Item actively being processed
- **COMPLETED**: Item successfully completed
- **FAILED**: Item failed with error
- **CANCELLED**: Item cancelled by user
- **SKIPPED**: Item skipped (not processed)

## Priority System

Unified priority system (1-10, lower = higher priority):

- **1-3**: High priority (🔴)
- **4-6**: Normal priority (🟡)
- **7-10**: Low priority (🟢)

Or use string values:
- `"high"` = 3
- `"normal"` = 5
- `"low"` = 7

## Usage

### Adding Sources (Same as Problems)

```python
from unified_queue_adapter import UnifiedQueueAdapter

adapter = UnifiedQueueAdapter()

# Add source (same interface as problems)
source_id = adapter.add_source(
    url="https://www.youtube.com/@EWTN",
    source_type="web",
    priority="high"  # Same priority system
)

# Add problem (same interface)
problem_id = adapter.add_problem(
    title="Linter error in main.py",
    description="Unused import detected",
    category="linting",
    priority="high"  # Same priority system
)

# Add task (same interface)
task_id = adapter.add_task(
    title="Review PR #123",
    description="Code review needed",
    priority="normal"  # Same priority system
)
```

### Viewing All Items Together

```python
# Get all items (sources, problems, tasks together)
all_items = adapter.get_all_items()

# Filter by type
sources = adapter.get_all_items(item_type=QueueItemType.SOURCE)
problems = adapter.get_all_items(item_type=QueueItemType.PROBLEM)

# Filter by status
pending = adapter.get_all_items(status=QueueItemStatus.PENDING)
processing = adapter.get_all_items(status=QueueItemStatus.PROCESSING)

# Filter by priority
high_priority = adapter.get_all_items(priority_min=3)
```

### Unified Viewer

```bash
# View all queue items together
python scripts/python/unified_queue_viewer.py

# Filter by type
python scripts/python/unified_queue_viewer.py --filter-type source
python scripts/python/unified_queue_viewer.py --filter-type problem

# Filter by status
python scripts/python/unified_queue_viewer.py --filter-status processing

# Filter by priority
python scripts/python/unified_queue_viewer.py --filter-priority 3

# Sort options
python scripts/python/unified_queue_viewer.py --sort priority
python scripts/python/unified_queue_viewer.py --sort created_at
python scripts/python/unified_queue_viewer.py --sort updated_at
```

## Integration with Orchestrator

The unified queue adapter automatically syncs with the AI SYPHON + IDM Orchestrator:

- Sources added to orchestrator automatically appear in unified queue
- Status updates from orchestrator sync to unified queue
- Workflow stages map to unified status
- Progress tracking unified

## Display Format

The unified viewer shows all items in the same format:

```
Type        Status      Priority  Title                          Progress
─────────────────────────────────────────────────────────────────────────
🔗 source   ⚙️ processing  🔴 3  Source: https://youtube.com...  ████████░░ 80.0%
⚠️ problem  ⏳ pending      🟡 5  Linter error in main.py         ░░░░░░░░░░  0.0%
📝 task     ✅ completed   🟢 7  Review PR #123                  ██████████ 100.0%
```

## Status Mapping

Sources workflow stages map to unified status:

| Workflow Stage | Unified Status |
|----------------|----------------|
| DISCOVERY | PENDING |
| QUEUED | QUEUED |
| DOWNLOADING | PROCESSING |
| DOWNLOADED | PROCESSING |
| EXTRACTING | PROCESSING |
| EXTRACTED | PROCESSING |
| PROCESSING | PROCESSING |
| COMPLETED | COMPLETED |
| FAILED | FAILED |
| SKIPPED | SKIPPED |

## Benefits

### Consistency
- Same interface for all queue types
- Same status workflow
- Same priority system
- Same viewing experience

### Unified Management
- View all items together
- Filter and sort consistently
- Manage priorities uniformly
- Track progress the same way

### Integration
- Sources integrate seamlessly
- Problems integrate seamlessly
- Tasks integrate seamlessly
- All work items in one place

## Examples

### Example: Adding Multiple Item Types

```python
adapter = UnifiedQueueAdapter()

# Add source
adapter.add_source("https://www.ewtn.com", priority="high")

# Add problem
adapter.add_problem("Build failed", "TypeScript compilation error", priority="high")

# Add task
adapter.add_task("Update docs", "Document new API", priority="normal")

# View all together
all_items = adapter.get_all_items()
# Returns sources, problems, and tasks together, sorted by priority
```

### Example: Unified Summary

```python
summary = adapter.get_queue_summary()

print(f"Total: {summary['total_items']}")
print(f"Sources: {summary['by_type']['source']}")
print(f"Problems: {summary['by_type']['problem']}")
print(f"Tasks: {summary['by_type']['task']}")
print(f"Processing: {summary['processing_count']}")
```

## Command Line Usage

```bash
# Add source
python scripts/python/unified_queue_adapter.py \
    --add-source "https://youtube.com/@EWTN" "web"

# Add problem
python scripts/python/unified_queue_adapter.py \
    --add-problem "Build Error" "TypeScript compilation failed"

# View summary
python scripts/python/unified_queue_adapter.py --summary

# List all items
python scripts/python/unified_queue_adapter.py --list

# View in real-time
python scripts/python/unified_queue_viewer.py
```

## Storage

Queue state is saved to:
- `data/unified_queue/queue_state.json`

Contains:
- All queue items
- Current status
- Metadata
- Timestamps

## Future Enhancements

- [ ] VSCode extension integration
- [ ] Web dashboard
- [ ] Notification system
- [ ] Auto-assignment rules
- [ ] SLA tracking
- [ ] Analytics and reporting

## Related Systems

- **AI SYPHON + IDM Orchestrator**: Sources queue backend
- **VSCode Problems**: Problem queue source
- **Task Queue**: General task management
- **Unified Queue Adapter**: Integration layer
- **Unified Queue Viewer**: Display interface

## Tags

@UNIFIED @QUEUE @SOURCES @PROBLEMS @TASKS @INTEGRATION
