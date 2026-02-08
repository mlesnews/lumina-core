# Ciao Session Resumer

Automatically resumes interrupted Ciao sessions on IDE startup with intelligent resource balancing and triage-based prioritization.

## Features

### 🔄 Auto-Retry on IDE Startup
- Automatically runs when IDE starts
- Configurable startup delay (default: 10 seconds)
- Checks system resources before starting
- Deferred execution if system is overloaded

### 🏥 Triage-Based Prioritization
- Uses AIQ Triage system to prioritize sessions
- Priority levels: Immediate, Urgent, Elevated, Routine
- Higher priority sessions processed first

### ⏱️ Staggered Processing
- Stagger delays based on triage priority:
  - **Immediate**: 0.5 seconds
  - **Urgent**: 1.0 second
  - **Elevated**: 2.0 seconds
  - **Routine**: 5.0 seconds
- Delays automatically adjust based on system load

### 📊 Resource Balancing
- Monitors CPU and memory usage in real-time
- Throttles processing when resources are high
- Default limits:
  - CPU: 75% max
  - Memory: 80% max
- Adaptive adjustment based on statistics

### 📈 Statistics & Adaptive Adjustment
- Tracks processing statistics:
  - Total processed
  - Success/failure rates
  - CPU/memory usage history
  - Average processing times
- Automatically adjusts stagger delays every 30 seconds
- Increases delays when system is under load
- Decreases delays when system has capacity

### 🔀 Session Merging
- Groups related sessions by category
- Merges sessions within each group
- Preserves all messages and metadata
- Creates merged session files

## Usage

### Manual Execution
```bash
python scripts/python/ciao_session_resumer.py
```

### Auto-Startup on IDE
```bash
python scripts/python/ciao_startup_integration.py
```

### With Custom Settings
```bash
python scripts/python/ciao_session_resumer.py \
  --auto-startup \
  --startup-delay 15 \
  --max-cpu 70 \
  --max-memory 75
```

## Configuration

### Resource Limits
- `--max-cpu`: Maximum CPU percent before throttling (default: 75.0)
- `--max-memory`: Maximum memory percent before throttling (default: 80.0)

### Startup Settings
- `--auto-startup`: Enable auto-startup on IDE initialization
- `--startup-delay`: Delay after IDE startup in seconds (default: 10.0)

## Workflow

1. **Find Interrupted Sessions**
   - Scans all session files
   - Identifies incomplete/interrupted sessions
   - Checks for Ciao references

2. **Triage Sessions**
   - Uses AIQ Triage system
   - Assigns priority and category
   - Falls back to "Routine" if triage unavailable

3. **Group Related Sessions**
   - Groups by category and topic
   - Determines group priority (highest in group)

4. **Staggered Merging**
   - Sorts groups by priority
   - Processes with stagger delays
   - Monitors resources continuously
   - Throttles if needed

5. **Save Resumed Sessions**
   - Creates merged session files
   - Saves to `data/ciao_resumed/`
   - Generates summary report

## Resource Monitoring

The system continuously monitors:
- CPU usage (per core and overall)
- Memory usage (percent and available)
- Processing history (last 100 readings)

Adaptive adjustments:
- **High load** (CPU > 70% or Memory > 75%): Increase delays by 1.5x
- **Low load** (CPU < 40% and Memory < 50%): Decrease delays by 0.8x
- **Normal load**: Use base delays

## Output

### Session Files
- Location: `data/ciao_resumed/`
- Format: `merged_{group_id}_{timestamp}.json`
- Contains: All messages, metadata, merge information

### Summary Report
- Location: `data/ciao_resumed/resume_summary_{timestamp}.json`
- Contains:
  - Total sessions found
  - Groups created
  - Sessions resumed
  - Priority breakdown
  - Resource usage statistics

## Integration

### IDE Startup
Add to IDE startup scripts or configuration:
```python
# In IDE startup script
from scripts.python.ciao_startup_integration import main
main()
```

### Scheduled Execution
Can be run on a schedule or triggered by events:
```bash
# Run every hour
0 * * * * python /path/to/ciao_session_resumer.py
```

## Statistics Tracking

The system maintains statistics for:
- Processing performance
- Resource utilization
- Success/failure rates
- Adaptive delay adjustments

These statistics are used to:
- Adjust processing parameters
- Optimize resource usage
- Improve future performance

## Troubleshooting

### No Sessions Found
- Check session directory: `data/r5_living_matrix/sessions/`
- Verify session files are JSON format
- Check for interruption indicators in content

### High Resource Usage
- Increase stagger delays
- Lower max CPU/memory thresholds
- Process fewer sessions at once

### Triage Unavailable
- System falls back to "Routine" priority
- All sessions processed with routine delays
- Check MCP server connection

## Future Enhancements

- Multi-workstation coordination
- Distributed processing
- Advanced resource prediction
- Machine learning for delay optimization
- Integration with load balancers

