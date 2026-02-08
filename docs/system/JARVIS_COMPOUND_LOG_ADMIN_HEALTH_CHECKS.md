# JARVIS Compound Log Admin - Comprehensive Health Checks

## Overview

JARVIS Compound Log Administrator now includes comprehensive health check monitoring and administration for all associated systems.

## Health Check Registry

The system includes a `HealthCheckRegistry` that manages all health checks:

- **Registration**: Register custom health checks
- **Execution**: Run individual or all health checks
- **History**: Track last 1000 health check results
- **Status Tracking**: Monitor run counts, error counts, and last status

## Registered Health Checks

### Default Health Checks

1. **compound_log** - Compound log health status
   - Checks compound log metrics (lines, errors, warnings, successes)
   - Status: HEALTHY, WARNING, DEGRADED, UNHEALTHY

2. **tail_processes** - Tail processes status
   - Monitors running vs stopped tail processes
   - Status: HEALTHY (all running), DEGRADED (some stopped), WARNING (more stopped than running)

3. **system_resources** - System resources (CPU, Memory)
   - Monitors CPU and memory usage
   - Status: HEALTHY (<70%), WARNING (70-90%), DEGRADED (>90%)

4. **unified_health** - Unified health system status
   - Integrates with UnifiedHealthSystem
   - Status: Overall health from unified system

5. **disk_space** - Disk space availability
   - Monitors disk usage percentage
   - Status: HEALTHY (<75%), WARNING (75-90%), DEGRADED (>90%)

6. **processes** - Running processes count
   - Tracks number of running processes
   - Status: Always HEALTHY (informational)

## Health Check Status Levels

- **HEALTHY** - System operating normally
- **WARNING** - Minor issues detected, monitoring required
- **DEGRADED** - Performance issues, action may be needed
- **UNHEALTHY** - Critical issues, immediate action required
- **ERROR** - Health check failed to execute

## CLI Commands

### Health Check Operations

```bash
# Run all health checks
python scripts/python/jarvis_compound_log_admin.py --health-checks

# Run a specific health check
python scripts/python/jarvis_compound_log_admin.py --health-check <check_name>

# Get health check registry status
python scripts/python/jarvis_compound_log_admin.py --health-status

# Start monitoring with health checks (60s interval)
python scripts/python/jarvis_compound_log_admin.py --start --interval 60
```

### Available Health Checks

- `compound_log` - Compound log health
- `tail_processes` - Tail processes status
- `system_resources` - CPU and memory
- `unified_health` - Unified health system
- `disk_space` - Disk space
- `processes` - Process count

## Integration with Unified Health System

The admin system automatically integrates with `UnifiedHealthSystem`:

- Registers all unified health system checks with `unified_` prefix
- Monitors unified health system status
- Combines results for comprehensive health overview

## Health Check Monitoring Loop

When monitoring is active:

1. **Health Check Loop** (runs every 60s by default):
   - Executes all registered health checks
   - Saves results to JSON files
   - Logs summary to console
   - Writes results to compound log

2. **Administration Monitoring Loop** (runs every 10s):
   - Monitors tail processes
   - Monitors compound log health
   - Processes delegated tasks
   - Triggers health recovery if needed

## Health Check Results

Results are saved to:
```
data/compound_log_admin/health_checks_YYYYMMDD_HHMMSS.json
```

Each result includes:
- Timestamp
- Individual check results
- Overall health status
- Summary statistics (healthy, warning, degraded, unhealthy, error counts)

## Delegation and Recovery

When health issues are detected:

- **UNHEALTHY** status triggers automatic health recovery delegation
- **DEGRADED** status logs warnings
- Health recovery tasks are processed in the administration loop

## Example Output

```json
{
  "timestamp": "2026-01-07T01:34:07.235664",
  "checks": {
    "compound_log": {
      "status": "HEALTHY",
      "metrics": {...},
      "details": "Compound log health status"
    },
    "system_resources": {
      "status": "HEALTHY",
      "cpu_percent": 7.2,
      "memory_percent": 31.3,
      "details": "CPU: 7.2%, Memory: 31.3%"
    },
    "disk_space": {
      "status": "DEGRADED",
      "used_percent": 93.75,
      "details": "Disk: 93.8% used (230.8GB free)"
    }
  },
  "overall_health": "DEGRADED",
  "summary": {
    "total": 6,
    "healthy": 4,
    "warning": 0,
    "degraded": 1,
    "unhealthy": 0,
    "error": 0
  }
}
```

## Custom Health Checks

Register custom health checks:

```python
def my_custom_check():
    return {
        "status": "HEALTHY",
        "details": "Custom check result"
    }

admin.register_health_check("my_check", my_custom_check, "My custom health check")
```

## Status API

Get comprehensive status:

```python
status = admin.get_admin_status()
# Includes:
# - Monitoring status
# - Health check registry
# - Current health check results
# - Tail processes
# - Delegated tasks
# - Compound log health
```

## Tags

#COMPOUND_LOG #ADMINISTRATION #MONITORING #HEALTH_CHECKS #DELEGATION @JARVIS @LUMINA
