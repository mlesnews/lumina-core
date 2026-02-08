# Tool Resource Utilization Historian

## Overview

The Tool Resource Utilization Historian tracks and measures resource utilization percentage scores for major/minor tools/apps with historical data tracking.

**Tags:** #measure #historian #resource #utilization #monitoring

## Features

- **Real-time Resource Monitoring**: CPU, Memory, Disk I/O, Network I/O
- **Historical Tracking**: Timestamped snapshots stored daily
- **Percentage Scores**: Weighted utilization scores (0-100%) for each tool
- **Tool Categorization**: Major (IDEs, browsers) vs Minor (utilities) vs System
- **Historical Analysis**: Average, peak, and time-period utilization reports

## Quick Start

### Capture Current Snapshot

```bash
python scripts/python/tool_resource_utilization_historian.py --capture
```

Shows top 10 tools by current utilization with:
- Overall utilization percentage score
- CPU usage
- Memory usage
- Tool category (major/minor/system)

### Generate Utilization Report

```bash
# Full historical report
python scripts/python/tool_resource_utilization_historian.py --report

# Report for specific time period
python scripts/python/tool_resource_utilization_historian.py --report --hours 24

# Load specific date and generate report
python scripts/python/tool_resource_utilization_historian.py --load 20260103 --report
```

### Continuous Monitoring

```bash
# Monitor every 60 seconds
python scripts/python/tool_resource_utilization_historian.py --monitor 60

# Monitor and save periodically
python scripts/python/tool_resource_utilization_historian.py --monitor 60 --save
```

### Save/Load History

```bash
# Capture and save
python scripts/python/tool_resource_utilization_historian.py --capture --save

# Load specific date
python scripts/python/tool_resource_utilization_historian.py --load 20260103
```

## Utilization Score Calculation

The overall utilization percentage score is a weighted combination:

- **CPU**: 40% weight
- **Memory**: 40% weight  
- **Disk I/O**: 10% weight
- **Network I/O**: 10% weight

Score range: 0-100%

## Tool Categories

### Major Tools
Primary applications that are actively used:
- IDEs: Cursor, VS Code
- Browsers: Chrome, Edge, Firefox
- Communication: Slack, Teams, Discord
- Development: Python, Node.js, Docker, Git

### Minor Tools
Supporting utilities and background processes:
- Shells: PowerShell, CMD
- System: Explorer, DWM

### System
Windows system processes (typically filtered out unless significant)

## Data Storage

- **Daily History**: `data/resource_utilization/tool_history_YYYYMMDD.json`
- **Reports**: `data/resource_utilization/utilization_report_YYYYMMDD_HHMMSS.json`

## Report Output

Reports include:
- **Summary**: Total tools, major/minor counts, average/peak utilization
- **Sorted Tools**: Top tools by average utilization with:
  - Average utilization percentage
  - Peak utilization percentage
  - Recent 1-hour average
  - Recent 24-hour average
  - Tool category

## Example Output

```
📊 TOOL RESOURCE UTILIZATION REPORT
================================================================================
Summary:
  Total Tools: 63
  Major Tools: 3
  Minor Tools: 4
  Average Utilization: 5.34%
  Peak Utilization: 33.76%

🔝 Top Tools by Average Utilization:
  Python                         [major ] Avg:  15.36% | Peak:  57.10%
  Cursor IDE                     [major ] Avg:   8.51% | Peak:  36.73%
  Node.js                        [major ] Avg:   7.13% | Peak:   8.69%
```

## Integration

The historian can be imported and used programmatically:

```python
from scripts.python.tool_resource_utilization_historian import ToolResourceUtilizationHistorian

historian = ToolResourceUtilizationHistorian()

# Capture snapshot
snapshots = historian.capture_snapshot()

# Get report
report = historian.get_tool_utilization_report(hours=24)

# Save history
historian.save_history()
```

## Requirements

- `psutil`: Install with `pip install psutil`

## Notes

- Only tracks processes with utilization > 0.1% (or major tools regardless)
- System processes are filtered unless explicitly tracked
- Historical data is stored daily and can be loaded for analysis
- Utilization scores are normalized to system resources (CPU count, total memory)
