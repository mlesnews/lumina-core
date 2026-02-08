# NAS Service Monitoring with Heartbeat and Master Coordination

**Date**: 2025-01-24  
**Status**: ✅ **ACTIVE**  
**Enhanced By**: @JARVIS

## Overview

The NAS service monitoring system provides comprehensive heartbeat monitoring, API availability checks, and master service coordination for all NAS services. It implements a ping-pong communication pattern for bidirectional status reporting.

## Features

### ✅ Heartbeat Monitoring
- **Configurable heartbeat intervals** (default: 300 seconds = 5 minutes)
- Longer intervals reduce overhead while maintaining service visibility
- Automatic health status tracking and reporting

### ✅ API Availability Checks
- **NAS API connectivity** (Synology DSM API)
- **SSH connectivity** checks
- Response time monitoring
- Automatic status classification (healthy, degraded, unhealthy, offline)

### ✅ Ping-Pong Communication
- **Bidirectional status reporting** between services and master
- Sequence number tracking for message ordering
- Response acknowledgment (pong) from master service
- History tracking (last 100 ping-pong exchanges)

### ✅ Master Service Coordination
- **Centralized service registry** for all NAS services
- Aggregated status reporting across all services
- Health summary and statistics
- Service discovery and registration

## Architecture

### Components

1. **NASServiceMonitor**
   - Individual service monitor
   - Performs health checks at configured intervals
   - Sends heartbeat (ping) to master service
   - Receives and processes pong responses

2. **NASMasterCoordinator**
   - Central coordinator for all services
   - Aggregates status from multiple monitors
   - Provides unified status reporting
   - Tracks heartbeat history

3. **ServiceHealth**
   - Health metrics data structure
   - Tracks success/failure counts
   - Records response times
   - Stores API and SSH availability status

4. **HeartbeatMessage**
   - Ping-pong message format
   - Sequence number tracking
   - Status and health data payload

## Configuration

### Basic Configuration

```python
from nas_service_monitor import NASServiceMonitor

nas_config = {
    'host': '10.17.17.32',
    'port': 5001,
    'api_port': 5001,
    'ssh_port': 22,
    'username': 'backupadm',
    'password': '...'  # Or from Azure Key Vault
}

monitor = NASServiceMonitor(
    service_id='nas-cache-service',
    nas_config=nas_config,
    heartbeat_interval=300,  # 5 minutes
    master_endpoint='http://master-service:8080'
)
```

### Integration with NAS Cache

The monitoring system is automatically integrated into `TieredPhysicsCache`:

```python
cache_config = {
    'nas_config': {...},
    'monitor_config': {
        'heartbeat_interval': 300,  # 5 minutes
        'master_endpoint': 'http://master-service:8080',
        'service_id': 'nas-physics-cache'
    }
}

cache = TieredPhysicsCache(cache_config)
# Monitor starts automatically
```

## Usage

### Starting a Monitor

```python
monitor = NASServiceMonitor(
    service_id='my-nas-service',
    nas_config=nas_config,
    heartbeat_interval=300
)

# Register with master coordinator
from nas_service_monitor import get_master_coordinator
master = get_master_coordinator()
master.register_service(monitor)

# Start monitoring
monitor.start()
```

### Getting Status

```python
# Get service status
status = monitor.get_status()
print(json.dumps(status, indent=2))

# Get health summary
health = monitor.get_health_summary()
print(f"Status: {health['status']}")
print(f"Success Rate: {health['success_rate']}")
print(f"API Available: {health['api_available']}")
print(f"SSH Available: {health['ssh_available']}")
```

### Master Coordinator

```python
from nas_service_monitor import get_master_coordinator

master = get_master_coordinator()

# Get all service status
all_status = master.get_all_status()
print(f"Total Services: {all_status['total_services']}")
print(f"Healthy: {all_status['healthy_count']}")
print(f"Offline: {all_status['offline_count']}")

# Get specific service status
service_status = master.get_service_status('nas-cache-service')
```

## Health Status Levels

### ServiceStatus Enum

- **HEALTHY**: Service is fully operational
  - API or SSH available
  - Response time < 1 second
  
- **DEGRADED**: Service is operational but slow
  - API or SSH available
  - Response time 1-5 seconds
  
- **UNHEALTHY**: Service has issues
  - API or SSH available
  - Response time > 5 seconds
  
- **OFFLINE**: Service is unavailable
  - Neither API nor SSH available
  
- **UNKNOWN**: Status not yet determined
  - Initial state before first check

## Ping-Pong Communication

### Ping (Heartbeat)
Services send periodic heartbeat messages to the master:

```json
{
  "service_id": "nas-cache-service",
  "timestamp": "2025-01-24T10:30:00",
  "status": "healthy",
  "health": {
    "api_available": true,
    "ssh_available": true,
    "response_time_ms": 245.5
  },
  "sequence": 42,
  "response_required": true
}
```

### Pong (Acknowledgment)
Master responds with acknowledgment:

```json
{
  "acknowledged": true,
  "sequence": 42,
  "master_status": "operational",
  "timestamp": "2025-01-24T10:30:00.123"
}
```

## Monitoring Metrics

### Service Health Metrics

- `success_count`: Number of successful health checks
- `failure_count`: Number of failed health checks
- `response_time_ms`: Average response time in milliseconds
- `api_available`: NAS API connectivity status
- `ssh_available`: SSH connectivity status
- `last_success`: Timestamp of last successful check
- `last_failure`: Timestamp of last failed check

### Master Coordinator Metrics

- `total_services`: Total number of registered services
- `healthy_count`: Number of healthy services
- `degraded_count`: Number of degraded services
- `unhealthy_count`: Number of unhealthy services
- `offline_count`: Number of offline services

## Integration Points

### NAS Physics Cache

The monitoring system is automatically integrated into `TieredPhysicsCache`:

```python
cache = TieredPhysicsCache(config)
# Monitor is automatically started

# Get monitoring status
monitoring_status = cache.get_monitoring_status()

# Get health summary
health = cache.get_health_summary()
```

### Status Callbacks

You can provide a callback for status updates:

```python
def on_status_update(health):
    if health.status == ServiceStatus.OFFLINE:
        print("⚠️  NAS service is offline!")
    elif health.status == ServiceStatus.HEALTHY:
        print("✅ NAS service is healthy")

monitor = NASServiceMonitor(
    service_id='my-service',
    nas_config=nas_config,
    status_callback=on_status_update
)
```

## Command Line Usage

```bash
# Start a monitor
python scripts/python/nas_service_monitor.py \
    --service-id nas-cache-service \
    --heartbeat 300 \
    --master http://master-service:8080 \
    --nas-host 10.17.17.32 \
    --nas-port 5001
```

## Configuration Options

### Monitor Configuration

```python
monitor_config = {
    'heartbeat_interval': 300,  # Heartbeat interval in seconds (5 min default)
    'master_endpoint': 'http://master-service:8080',  # Master service URL
    'service_id': 'nas-physics-cache'  # Unique service identifier
}
```

### NAS Configuration

```python
nas_config = {
    'host': '10.17.17.32',  # NAS IP address
    'port': 5001,  # NAS port
    'api_port': 5001,  # NAS API port (Synology DSM)
    'ssh_port': 22,  # SSH port
    'username': 'backupadm',  # SSH username
    'password': '...',  # SSH password (or from Azure Key Vault)
    'timeout': 30  # Connection timeout
}
```

## Benefits

### Operational Excellence
- **Proactive monitoring**: Detect issues before they impact services
- **Centralized visibility**: Single point for all NAS service status
- **Historical tracking**: Ping-pong history for troubleshooting
- **Automatic classification**: Status levels based on performance

### Performance Optimization
- **Longer heartbeat intervals**: Reduced overhead (5 minutes default)
- **Efficient checks**: Quick API/SSH connectivity tests
- **Background operation**: Non-blocking monitoring threads

### Reliability
- **Graceful degradation**: System continues if monitoring fails
- **Automatic recovery**: Retry logic for transient failures
- **Status persistence**: Health metrics tracked over time

## Troubleshooting

### Monitor Not Starting

```python
# Check if monitor is available
from nas_service_monitor import NAS_MONITOR_AVAILABLE
print(f"Monitor available: {NAS_MONITOR_AVAILABLE}")

# Check monitor status
if monitor:
    status = monitor.get_status()
    print(f"Monitoring: {status['monitoring']}")
```

### Master Not Responding

- Check master endpoint URL
- Verify network connectivity
- Check master service logs
- Monitor will continue operating even if master is unavailable

### High Response Times

- Check NAS network connectivity
- Verify NAS is not overloaded
- Review NAS system logs
- Consider increasing heartbeat interval

## Future Enhancements

Potential improvements:

1. **Distributed Master**: Multiple master coordinators for redundancy
2. **Alerting**: Integration with alerting systems (email, Slack, etc.)
3. **Metrics Export**: Prometheus/Grafana integration
4. **Predictive Health**: ML-based health prediction
5. **Auto-scaling**: Automatic service scaling based on health

## References

- `scripts/python/nas_service_monitor.py`: Main monitoring implementation
- `scripts/python/nas_physics_cache.py`: Cache integration
- `config/nas_proxy_cache_config.yaml`: Configuration file

---

**Status**: ✅ **PRODUCTION READY**  
**Maintained By**: @JARVIS  
**Last Updated**: 2025-01-24

