# Centralized Log Parsing and Aggregation

## Overview

The centralized log parsing system automatically parses and aggregates logs from IDE startup, service startup, and runtime operations. It detects patterns over time and provides insights for debugging and analysis.

## Features

### 1. Log Parsing
- **IDE Startup Logs**: Automatically detects and parses IDE (Cursor/VSCode) startup logs
- **Service Startup Logs**: Parses service startup logs
- **Centralized Storage**: Reads from both local logs and NAS centralized logs (`\\10.17.17.32\backups\MATT_Backups\logs`)

### 2. Pattern Detection
- **Automatic Pattern Matching**: Detects common patterns like:
  - IDE startup events
  - Service startup events
  - Error exit codes
  - Connection failures
  - Service crashes
  - Resource exhaustion
  - Performance issues

### 3. Aggregation
- **Time-based Aggregation**: Aggregates logs by hour, day, or week
- **Pattern Aggregation**: Groups logs by detected patterns
- **Trend Analysis**: Tracks pattern occurrences over time

### 4. Debugging Support
- **Recent Errors**: Identifies recent errors for quick debugging
- **Pattern Trends**: Shows which patterns are trending (increasing occurrences)
- **Recommendations**: Provides actionable recommendations based on log analysis

## Usage

### Automatic Parsing on Startup

The log parser is automatically integrated into the IDE startup process (`ciao_startup_integration.py`). When the IDE starts:

1. Log parser initializes
2. Startup logs are parsed in the background (non-blocking)
3. Patterns are detected and aggregated
4. Results are saved to `data/log_aggregation/`

### Manual Parsing

```bash
# Parse all logs once
python scripts/python/centralized_log_parser.py

# Run aggregation service once
python scripts/python/log_aggregation_service.py --once

# Get debugging insights
python scripts/python/log_aggregation_service.py --insights

# Get pattern trends
python scripts/python/log_aggregation_service.py --trends all --hours 24

# Start continuous aggregation service
python scripts/python/log_aggregation_service.py --start
```

## Output Files

### Aggregation Results
- Location: `data/log_aggregation/aggregation_YYYYMMDD_HHMMSS.json`
- Contains: Full aggregation results with patterns and time-based aggregations

### Pattern Registry
- Location: `data/log_aggregation/patterns.json`
- Contains: All detected patterns with statistics

### Pattern Trends
- Location: `data/log_aggregation/history/pattern_trends.json`
- Contains: Historical pattern occurrences over time

## Pattern Detection

The system automatically detects patterns in logs. Common patterns include:

### Startup Patterns
- **IDE Startup**: Detects IDE initialization events
- **Service Startup**: Detects service startup events

### Error Patterns
- **Error Exit Code**: Detects process exit codes (especially non-zero)
- **Connection Failed**: Detects connection failures
- **Service Crash**: Detects service crashes or fatal errors

### Warning Patterns
- **Resource Exhaustion**: Detects memory/disk/resource warnings
- **Performance Issue**: Detects performance-related warnings

## Custom Patterns

You can add custom patterns by editing `data/log_aggregation/patterns.json` or by extending the `_initialize_common_patterns()` method in `centralized_log_parser.py`.

## Integration Points

### IDE Startup
- Integrated in `ciao_startup_integration.py`
- Runs automatically on IDE startup
- Non-blocking background parsing

### Service Startup
- Can be integrated into service startup scripts
- Monitors service startup logs

### Continuous Monitoring
- Use `log_aggregation_service.py` for continuous monitoring
- Runs aggregation cycles at configurable intervals (default: 5 minutes)

## Debugging Workflow

1. **Check Recent Errors**:
   ```bash
   python scripts/python/log_aggregation_service.py --insights
   ```

2. **Review Pattern Trends**:
   ```bash
   python scripts/python/log_aggregation_service.py --trends all --hours 24
   ```

3. **Analyze Specific Pattern**:
   ```bash
   python scripts/python/log_aggregation_service.py --trends error_exit_code --hours 48
   ```

4. **Review Aggregation Results**:
   - Check `data/log_aggregation/aggregation_*.json` files
   - Look for patterns with high occurrences
   - Review pattern examples

## Example Output

### Aggregation Summary
```
CENTRALIZED LOG PARSING SUMMARY
============================================================
Total log files: 15
Total entries: 1,234

By Level:
  INFO: 856
  WARNING: 234
  ERROR: 123
  CRITICAL: 21

By Source:
  ide_startup: 456
  service_startup: 234
  application: 344
  system: 200

Patterns Matched: 5
  IDE Startup: 456 occurrences (info)
  Service Startup: 234 occurrences (info)
  Error Exit Code: 45 occurrences (warning)
  Connection Failed: 12 occurrences (error)
  Service Crash: 3 occurrences (critical)
```

### Debugging Insights
```json
{
  "timestamp": "2025-01-28T10:30:00",
  "recent_errors": [
    {
      "timestamp": "2025-01-28T10:25:00",
      "source": "service_startup",
      "component": "mcp_server",
      "message": "Service failed to start: exit code 64"
    }
  ],
  "pattern_summary": {
    "total_patterns": 7,
    "patterns_by_severity": {
      "info": 2,
      "warning": 2,
      "error": 2,
      "critical": 1
    }
  },
  "trending_patterns": [
    {
      "pattern_id": "error_exit_code",
      "current": 45,
      "previous": 42,
      "increase": 3
    }
  ],
  "recommendations": [
    "Review 1 recent errors for patterns",
    "Monitor 1 trending patterns"
  ]
}
```

## Configuration

### Aggregation Interval
Default: 5 minutes (300 seconds)

To change:
```python
service = LogAggregationService(interval=600)  # 10 minutes
```

### Log Sources
The parser automatically discovers logs from:
- Local: `logs/` directory
- NAS: `\\10.17.17.32\backups\MATT_Backups\logs`

## Future Enhancements

- Real-time log streaming
- Machine learning pattern detection
- Automated alerting for critical patterns
- Integration with monitoring dashboards
- Log correlation across services

