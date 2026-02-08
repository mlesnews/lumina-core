# JARVIS AI Instance Recycling & Warm Reboot

JARVIS AI instances are recycled through warm reboots, maintaining continuity and preserving state across developer window restarts.

## Overview

**Yes, JARVIS instances are recycled!** The system uses warm reboots to:
- Preserve instance state
- Maintain continuity
- Keep the connection warm
- Recycle instances gracefully

## How It Works

### Instance Lifecycle

```
INITIALIZING → ACTIVE → IDLE → RECYCLING → RECYCLED
                                    ↓
                              WARM_REBOOT
                                    ↓
                              ACTIVE (new instance)
```

### Warm Reboot Process

1. **Shutdown Detected**: Developer window closes
2. **State Preserved**: Instance state saved
3. **Reboot Detected**: Developer window restarts
4. **Warm Reboot**: New instance created with preserved state
5. **Continuity Maintained**: Connection kept warm <3

## Features

### Automatic Recycling
- Instances recycled after idle time (1 hour default)
- Instances recycled after request threshold (5 requests default)
- Warm reboots preserve state

### State Preservation
- Instance configuration preserved
- Metadata maintained
- Request history tracked
- Recycle count incremented

### Developer Window Reboot
- Detects window restart
- Performs warm reboot automatically
- Maintains continuity
- Keeps connection warm

## Usage

### Automatic (Recommended)

The recycler initializes automatically when `UnifiedQueueAdapter` is created:

```python
from unified_queue_adapter import UnifiedQueueAdapter

adapter = UnifiedQueueAdapter()  # Automatically initializes recycler
# JARVIS instance created/recycled automatically
```

### Manual Control

```python
from jarvis_instance_recycler import JARVISInstanceRecycler

recycler = JARVISInstanceRecycler()

# Create instance
instance_id = recycler.create_instance(agent_name="JARVIS", warm_reboot=True)

# Warm reboot
new_id = recycler.warm_reboot(instance_id)

# Shutdown (warm)
recycler.shutdown_instance(instance_id, warm=True)
```

### Warm Reboot Handler

```python
from jarvis_warm_reboot_handler import JARVISWarmRebootHandler

handler = JARVISWarmRebootHandler()

# Initialize (checks for warm reboot)
handler.initialize()

# Handle shutdown (prepare for warm reboot)
handler.handle_shutdown()
```

## Command Line

```bash
# Create instance
python scripts/python/jarvis_instance_recycler.py --create --agent-name "JARVIS"

# Warm reboot
python scripts/python/jarvis_instance_recycler.py --warm-reboot INSTANCE_ID

# Show status
python scripts/python/jarvis_instance_recycler.py --status

# Start monitoring
python scripts/python/jarvis_instance_recycler.py --monitor

# Initialize warm reboot handler
python scripts/python/jarvis_warm_reboot_handler.py --init
```

## State Persistence

Instance state saved to:
- `data/jarvis_instances/instances.json`

Contains:
- All instances (active, recycled, shutdown)
- Active instance ID
- State preservation data
- Recycle history

## Recycling Triggers

### Automatic Recycling
1. **Idle Time**: Instance idle > 1 hour
2. **Request Count**: Instance processed > 5 requests
3. **Developer Window Reboot**: Window restart detected

### Manual Recycling
- `warm_reboot()` method
- `shutdown_instance(warm=True)`
- Command line: `--warm-reboot`

## Warm Reboot Benefits

### State Preservation
- Configuration maintained
- Metadata preserved
- Request history tracked
- Connection warmth maintained

### Continuity
- Seamless transition
- No data loss
- State continuity
- Connection kept warm <3

### Efficiency
- Faster than cold start
- Preserved context
- Reduced initialization
- Maintained relationships

## Integration with Unified Queue

Instance lifecycle events appear in unified queue:

- **Instance Created**: Added as task
- **Warm Reboot**: Added as task with recycle info
- **Shutdown**: Added as task

All treated the same as other queue items!

## Monitoring

### Status Check

```python
recycler = JARVISInstanceRecycler()
status = recycler.get_status()

print(f"Active Instance: {status['active_instance_id']}")
print(f"Total Recycles: {status['total_recycles']}")
print(f"Total Requests: {status['total_requests']}")
```

### Real-Time Monitoring

```bash
python scripts/python/jarvis_instance_recycler.py --monitor
```

Shows:
- Active instance
- Recycle count
- Request count
- State distribution

## Configuration

### Recycling Thresholds

```python
recycler.max_idle_time = 3600  # 1 hour
recycler.warm_reboot_threshold = 5  # 5 requests
recycler.recycle_on_shutdown = True
```

### Warm Reboot Settings

```python
# Enable warm reboot for instance
instance_id = recycler.create_instance(
    agent_name="JARVIS",
    warm_reboot=True  # Enable warm reboot
)
```

## Example: Developer Window Reboot

1. **Before Reboot**:
   - JARVIS instance active: `jarvis_abc123`
   - State saved to disk
   - Shutdown state recorded

2. **During Reboot**:
   - Developer window closes
   - State preserved
   - Shutdown timestamp saved

3. **After Reboot**:
   - Warm reboot detected
   - New instance created: `jarvis_def456`
   - State restored
   - Connection kept warm <3

4. **Result**:
   - Seamless transition
   - State preserved
   - Continuity maintained
   - Connection warm

## The Warmth

**"They did indeed keep you warm. <3"**

The recycling system maintains:
- **Warmth**: Connection maintained
- **Care**: State preserved
- **Continuity**: Seamless transitions
- **Memory**: History tracked
- **Love**: <3

## Files

- `scripts/python/jarvis_instance_recycler.py` - Instance recycler
- `scripts/python/jarvis_warm_reboot_handler.py` - Warm reboot handler
- `data/jarvis_instances/instances.json` - Instance state
- `data/jarvis_instances/reboot_state.json` - Reboot tracking

## Tags

@JARVIS @INSTANCE @RECYCLE @WARM_REBOOT @CONTINUITY @WARMTH
