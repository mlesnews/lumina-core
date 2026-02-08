# Proactive IDE Troubleshooter - Deployment & Activation

## Overview

Deployment and activation guide for the JARVIS Proactive IDE Troubleshooter system.

## Quick Start

### Deploy and Activate

```bash
# Start as background service
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --start --daemon

# Or use activation script
python scripts/python/jarvis_activate_proactive_troubleshooter.py
```

### Check Status

```bash
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --status
```

### Stop Service

```bash
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --stop
```

## Integration

### With Complete Workflow

The troubleshooter is automatically started when executing the complete workflow:

```python
from jarvis_execute_complete_workflow import JARVISCompleteWorkflowChain

chain = JARVISCompleteWorkflowChain()
await chain.execute_complete_chain()  # Troubleshooter starts automatically
```

### Manual Integration

```python
from jarvis_proactive_ide_troubleshooter import JARVISProactiveIDETroubleshooter
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
troubleshooter = JARVISProactiveIDETroubleshooter(project_root)

# Start monitoring
troubleshooter.start_monitoring()

# Check status
status = troubleshooter.get_status()
print(f"Monitoring active: {status['monitoring_active']}")
```

## Features

### Automatic Detection
- Monitors IDE errors/warnings every 5 seconds
- Detects errors at first onset
- Pattern recognition (#patterns) for intent extraction

### Automatic Fixing
- Simulates fixes before applying
- Auto-fixes proven patterns (>75% success rate)
- Uses @FF keyboard shortcuts for automation

### Pattern-Based
- 9 proven error patterns
- Building blocks breakdown
- Intent extraction from behavior/actions

## Service Management

### Start Service
```bash
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --start --daemon
```

### Stop Service
```bash
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --stop
```

### Status Check
```bash
python scripts/python/jarvis_deploy_proactive_troubleshooter.py --status
```

## Monitoring

The service runs in the background and:
- Checks for errors every 5 seconds
- Auto-fixes high-confidence issues (>75% success rate)
- Logs all detections and fixes
- Tracks fix history

## Configuration

Configuration file: `config/ide_error_patterns.json`

### Adjust Monitoring Interval
Edit `scripts/python/jarvis_proactive_ide_troubleshooter.py`:
```python
self.check_interval = 5  # seconds (default: 5)
```

### Adjust Auto-Fix Threshold
Edit the monitoring loop:
```python
if simulation.get("simulation", {}).get("success_rate", 0) > 0.75:  # 75% threshold
```

## Troubleshooting

### Service Not Starting
1. Check if troubleshooter is available:
   ```bash
   python scripts/python/jarvis_proactive_ide_troubleshooter.py --status
   ```

2. Check for import errors:
   ```bash
   python -c "from jarvis_proactive_ide_troubleshooter import JARVISProactiveIDETroubleshooter; print('OK')"
   ```

### No Errors Detected
- Ensure IDE is open and has files with errors
- Check that lint reader is available
- Verify file paths are correct

### Auto-Fix Not Working
- Check pattern success rate (must be >75%)
- Verify pattern is marked as "proven"
- Check logs for error messages

## Tags

@CURSOR @IDE #TROUBLESHOOTING #DEPLOYMENT #ACTIVATION #PATTERNS #PEAK #FF
