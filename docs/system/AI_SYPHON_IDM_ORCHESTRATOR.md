# AI SYPHON + IDM Orchestrator

Intelligent system that coordinates SYPHON (intelligence extraction) and Internet Download Manager (IDM) for comprehensive content processing with real-time monitoring and debug capabilities.

## Overview

The AI Orchestrator intelligently routes content through a multi-stage workflow:
1. **Discovery** - Analyze content and determine processing strategy
2. **Download** (optional) - Use IDM to download content when needed
3. **Extraction** - Use SYPHON to extract intelligence
4. **Processing** - Final processing and storage
5. **Completion** - Item marked complete

## Features

### 🤖 AI-Driven Routing
- Automatically determines whether to download first or extract directly
- Optimizes resource allocation based on content type
- Adapts strategy based on file size, source type, and metadata

### 📊 Real-Time Monitoring
- Live status updates every 2-5 seconds
- Visual workflow representation
- Stage-by-stage progress tracking
- Performance metrics

### 🐛 Debug Workflow
- Complete stage transition history
- Detailed error logging
- Timeline tracking for each item
- Debug logs saved to `data/ai_orchestrator/debug/`

### ⚡ Multi-Stage Processing
- Parallel processing across stages
- Queue management for each stage
- Automatic stage transitions
- Error recovery and retry logic

## Workflow Stages

| Stage | Description | Next Stage |
|-------|-------------|------------|
| `DISCOVERY` | Initial analysis and routing decision | `QUEUED` |
| `QUEUED` | Item queued for processing | `DOWNLOADING` or `EXTRACTING` |
| `DOWNLOADING` | Downloading via IDM | `DOWNLOADED` |
| `DOWNLOADED` | Download complete | `EXTRACTING` |
| `EXTRACTING` | SYPHON intelligence extraction | `EXTRACTED` |
| `EXTRACTED` | Extraction complete | `PROCESSING` |
| `PROCESSING` | Final processing | `COMPLETED` |
| `COMPLETED` | Item fully processed | - |
| `FAILED` | Processing failed | - |
| `SKIPPED` | Item skipped | - |

## Usage

### Basic Usage

```python
from ai_syphon_idm_orchestrator import AIOrchestrator

# Initialize orchestrator
orchestrator = AIOrchestrator(enable_ai_routing=True)
orchestrator.start_monitoring()

# Add items
item_id = orchestrator.add_item(
    url="https://www.youtube.com/@EWTN",
    source_type="web",
    metadata={"priority": "high"}
)

# Get status
status = orchestrator.get_status()
orchestrator.print_status()

# Stop when done
orchestrator.stop_monitoring()
```

### Command Line

```bash
# Basic processing
python scripts/python/ai_syphon_idm_orchestrator.py \
    --urls "https://example.com" "https://youtube.com/watch?v=..."

# From file
python scripts/python/ai_syphon_idm_orchestrator.py \
    --file urls.txt \
    --console

# With real-time monitor
python scripts/python/workflow_realtime_monitor.py
```

### Real-Time Monitor

```bash
# Start monitor (requires orchestrator running)
python scripts/python/workflow_realtime_monitor.py \
    --update-interval 2.0 \
    --no-debug
```

## AI Routing Decisions

The AI orchestrator makes intelligent decisions based on:

### Content Type Analysis
- **YouTube videos**: Download first for transcript extraction
- **Large files (>100MB)**: Download first
- **Web pages**: Extract directly (no download needed)
- **Social media**: Extract directly via API

### Priority Levels
- **High**: YouTube videos, large files
- **Normal**: Standard web content
- **Low**: Background processing

### Processing Strategies
- **video_extraction**: Download → Extract transcript → Process
- **direct_extraction**: Extract directly → Process
- **standard**: Download → Extract → Process

## Real-Time Status Updates

The system provides real-time status updates via callbacks:

```python
def status_callback(status):
    if status["type"] == "stage_update":
        print(f"Item {status['item_id']} moved to {status['new_stage']}")
    elif status["type"] == "status_update":
        print(f"Active: {len(status['active_items'])} items")

orchestrator.add_status_callback(status_callback)
```

## Debug Information

### Debug Logs
- Location: `data/ai_orchestrator/debug/workflow_YYYYMMDD.log`
- Format: JSON lines with timestamps
- Contains: Stage transitions, errors, metadata

### Status Snapshots
- Location: `data/ai_orchestrator/debug/status_YYYYMMDD_HHMMSS.json`
- Updated: Every 5 seconds
- Contains: Complete workflow state

### Item Data
- Location: `data/ai_orchestrator/items/{item_id}.json`
- Contains: Complete item history and metadata

## Integration Points

### SYPHON Integration
- Extracts intelligence from content
- Supports: Web, Social, Video sources
- Returns: Structured data with actionable items

### IDM Integration
- Downloads content when needed
- Supports: Resume capability, batch downloads
- Monitors: Download progress (future enhancement)

### R5 Integration
- Ingest processed content to R5 Living Context Matrix
- Enables: Long-term intelligence storage

## Performance Metrics

The monitor tracks:
- **Stage Duration**: Average, min, max time per stage
- **Throughput**: Items processed per minute
- **Success Rate**: Completed vs failed items
- **Queue Sizes**: Items waiting in each stage

## Error Handling

- **Automatic Retry**: Failed items can be retried
- **Error Logging**: All errors logged with context
- **Graceful Degradation**: Falls back when components unavailable
- **State Recovery**: Can resume from saved state

## Configuration

### Environment Variables
- `AI_ORCHESTRATOR_DEBUG`: Enable debug logging
- `AI_ORCHESTRATOR_UPDATE_INTERVAL`: Status update interval
- `AI_ORCHESTRATOR_MAX_WORKERS`: Maximum parallel workers per stage

### Configuration File
Location: `config/ai_orchestrator_config.json`

```json
{
  "enable_ai_routing": true,
  "update_interval": 5.0,
  "max_workers_per_stage": 4,
  "retry_failed_items": true,
  "save_state_interval": 60
}
```

## Examples

### EWTN YouTube Channel Processing

```python
orchestrator = AIOrchestrator()
orchestrator.start_monitoring()

# Add EWTN channel
orchestrator.add_item(
    "https://www.youtube.com/@EWTN",
    source_type="web",
    metadata={"channel": "EWTN", "priority": "high"}
)

# Monitor progress
while True:
    status = orchestrator.get_status()
    if status["stats"]["completed"] > 0:
        break
    time.sleep(5)
```

### Batch Processing with Monitor

```python
from workflow_realtime_monitor import WorkflowMonitor

orchestrator = AIOrchestrator()
orchestrator.start_monitoring()

# Add multiple items
for url in urls:
    orchestrator.add_item(url)

# Start visual monitor
monitor = WorkflowMonitor(orchestrator)
monitor.start()  # Blocks until Ctrl+C
```

## Troubleshooting

### IDM Not Available
- Check IDM installation path
- Verify IDM CLI access
- System will fall back to direct extraction

### SYPHON Not Available
- Check SYPHON configuration
- Verify SYPHON module import
- System will skip extraction stage

### Items Stuck in Queue
- Check stage worker threads
- Review error logs
- Manually retry failed items

## Future Enhancements

- [ ] IDM download progress monitoring
- [ ] Web-based dashboard
- [ ] Machine learning for routing optimization
- [ ] Distributed processing support
- [ ] Advanced retry strategies
- [ ] Cost optimization (API usage)

## Related Systems

- **SYPHON**: Intelligence extraction system
- **IDM-CLI**: Internet Download Manager integration
- **R5 Living Context Matrix**: Long-term storage
- **Workflow Monitor**: Real-time visualization

## Tags

@AI @SYPHON @IDM @ORCHESTRATOR @REALTIME @DEBUG @WORKFLOW @MONITORING
