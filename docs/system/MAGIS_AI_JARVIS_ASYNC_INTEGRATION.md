# MAGIS AI + JARVIS Async Integration

Asynchronous processing of chat history items from the unified queue using MAGIS AI for intelligence extraction, coordinated by JARVIS.

## Overview

The MAGIS AI + JARVIS async processor automatically:
- Monitors unified queue for `CHAT_HISTORY` items
- Processes them asynchronously using MAGIS AI
- Coordinates with JARVIS for orchestration
- Updates queue status in real-time
- Shows progress in IDE footer

## Architecture

```
Unified Queue (CHAT_HISTORY items)
    ↓
MAGIS AI + JARVIS Async Processor
    ↓
MAGIS AI Processor (Intelligence Extraction)
    ↓
JARVIS Coordinator (Orchestration)
    ↓
JARVIS SYPHON (Chat Session Extraction)
    ↓
Queue Status Updated → IDE Footer
```

## Components

### 1. MAGIS AI Processor (`MAGISAIProcessor`)
- Extracts intelligence from chat sessions
- Uses JARVIS SYPHON for extraction
- Returns structured intelligence data

### 2. JARVIS Coordinator (`JARVISCoordinator`)
- Coordinates async processing
- Loads chat data
- Manages workflow
- Updates queue status

### 3. Async Processor (`MAGISAIJARVISAsyncProcessor`)
- Monitors unified queue
- Processes items asynchronously
- Manages concurrent processing (max 3 at once)
- Updates queue status automatically

## Integration

### Automatic Processing

When chat history items are added to the unified queue:

```python
from unified_queue_adapter import UnifiedQueueAdapter

adapter = UnifiedQueueAdapter()  # Starts MAGIS AI + JARVIS processor

# Add chat history - automatically processed!
item_id = adapter.add_chat_history(
    session_id="session_123",
    agent_name="Cursor Agent",
    message_count=15,
    priority="high"
)
```

The async processor automatically:
1. Detects new `CHAT_HISTORY` items
2. Processes them asynchronously
3. Updates queue status (PENDING → PROCESSING → COMPLETED)
4. Shows progress in IDE footer

### Manual Processing

```python
from magis_ai_jarvis_async_processor import MAGISAIJARVISAsyncProcessor

processor = MAGISAIJARVISAsyncProcessor()
processor.start_processing()  # Start async loop
```

## Usage

### Add Chat History Items

```python
adapter = UnifiedQueueAdapter()

# Add chat history
adapter.add_chat_history(
    session_id="cursor_session_001",
    agent_name="Cursor Agent",
    title="Code Review Session",
    description="Reviewing Python code",
    message_count=15,
    priority="high"
)
```

### Run Async Processor

```bash
# Daemon mode (continuous processing)
python scripts/python/magis_ai_jarvis_async_processor.py --daemon

# Process single item
python scripts/python/magis_ai_jarvis_async_processor.py --process-item ITEM_ID

# Show statistics
python scripts/python/magis_ai_jarvis_async_processor.py --stats
```

### View in IDE Footer

The IDE footer shows:
```
📋 ⚙️ 5 ⏳2 💬3
```

- 5 total items
- Currently processing (spinner)
- 2 pending
- 3 chat history items

## Processing Flow

1. **Item Added**: Chat history added to unified queue
2. **Detected**: Async processor detects pending `CHAT_HISTORY` items
3. **Processing**: Status updated to `PROCESSING`, progress starts
4. **MAGIS AI**: Intelligence extraction using MAGIS AI
5. **JARVIS**: Coordination and orchestration
6. **Complete**: Status updated to `COMPLETED`, results saved
7. **Footer Update**: IDE footer reflects new status

## Status Updates

Queue status updates automatically:
- `PENDING` → Item queued
- `PROCESSING` → MAGIS AI + JARVIS processing
- `COMPLETED` → Processing successful
- `FAILED` → Processing failed (error logged)

## Results Storage

Processing results saved to:
- `data/magis_ai_jarvis/{item_id}_results.json`

Contains:
- Intelligence extraction results
- Topics, decisions, actions, patterns
- Processing metadata
- Success/failure status

## Configuration

### Concurrent Processing
- Default: Max 3 concurrent items
- Configurable in code: `max_concurrent = 3`

### Processing Interval
- Checks queue every 2 seconds
- Configurable: `await asyncio.sleep(2)`

## Integration with Unified Queue

The async processor integrates seamlessly:
- Automatically started when `UnifiedQueueAdapter` is initialized
- Monitors queue for `CHAT_HISTORY` items
- Updates queue status automatically
- Syncs with IDE extension via queue state file

## Example

```python
from unified_queue_adapter import UnifiedQueueAdapter

# Initialize (starts MAGIS AI + JARVIS processor)
adapter = UnifiedQueueAdapter()

# Add chat history items
adapter.add_chat_history("session_001", agent_name="JARVIS", priority="high")
adapter.add_chat_history("session_002", agent_name="MAGIS AI", priority="normal")

# Items automatically processed asynchronously!
# Check IDE footer for status updates
```

## Statistics

Get processing statistics:

```python
processor = MAGISAIJARVISAsyncProcessor()
stats = processor.get_stats()

print(f"Processed: {stats['processed']}")
print(f"Failed: {stats['failed']}")
print(f"Active: {stats['active_tasks']}")
```

## Troubleshooting

### Items Not Processing
1. Check processor is running: `processor.processing_active`
2. Verify items are `PENDING` status
3. Check logs for errors

### Processing Stuck
1. Check active tasks: `len(processor.processing_tasks)`
2. Restart processor: `processor.stop_processing()` then `start_processing()`

### No Results
1. Check `data/magis_ai_jarvis/` for result files
2. Verify JARVIS SYPHON is available
3. Check queue item status

## Related Systems

- **Unified Queue Adapter**: Queue management
- **JARVIS SYPHON**: Chat session extraction
- **IDE Extension**: Footer display
- **Queue Viewer**: Real-time monitoring

## Tags

@MAGISAI @JARVIS @ASYNC @CHAT_HISTORY @UNIFIED_QUEUE @INTELLIGENCE
