# IDE Session Load Balancing

**Date**: 2025-01-24  
**Status**: ✅ **ACTIVE**  
**Maintained By**: @JARVIS

## Problem Solved

**Issue**: Multiple IDE sessions (Cursor, VS Code, etc.) running on the same host can cause:
- Resource contention
- Stalled processes
- Uneven load distribution
- Performance degradation

**Solution**: IDE Session Load Balancer tracks all IDE sessions and ensures fair resource distribution.

## How It Works

### Session Discovery

Automatically discovers all IDE sessions on the host:
- Cursor sessions
- VS Code sessions
- Abacus sessions
- Other IDE processes

### Load Tracking

Tracks per-session metrics:
- CPU usage
- Memory usage
- Active requests
- Queue length
- Session status (active, idle, stalled, overloaded)

### Load Balancing

1. **Per-Session Limits**:
   - Max CPU: 50% per session
   - Max Memory: 2GB per session
   - Max Requests: 10 concurrent per session

2. **Stall Detection**:
   - Detects stalled sessions (30s timeout)
   - Automatically routes away from stalled sessions
   - Prevents resource hogging

3. **Fair Distribution**:
   - Routes to least loaded session
   - Balances load across all sessions
   - Prevents any single session from stalling

## Integration with Symbiotic Cluster

The IDE Session Load Balancer is integrated with the Symbiotic Cluster Coordinator:

1. **Host Selection**: Considers IDE session load when selecting hosts
2. **Request Routing**: Routes requests away from overloaded sessions
3. **Failover**: Automatically fails over if local host is overloaded
4. **Load Adjustment**: Adjusts host utilization based on IDE session load

## Usage

### Discover Sessions

```bash
python scripts/python/ide_session_load_balancer.py --discover
```

### Check Status

```bash
python scripts/python/ide_session_load_balancer.py --status
```

### Python API

```python
from ide_session_load_balancer import IDESessionLoadBalancer

# Initialize
balancer = IDESessionLoadBalancer()

# Check if can accept request
if balancer.can_accept_request():
    # Make request
    balancer.record_request()
    # ... do work ...
    balancer.complete_request()

# Get least loaded session
least_loaded = balancer.get_least_loaded_session()
```

## Session Status

- **ACTIVE**: Session is processing requests
- **IDLE**: Session is idle, ready for requests
- **STALLED**: Session has been inactive for >30s with active requests
- **OVERLOADED**: Session exceeds resource limits
- **UNKNOWN**: Session status unknown

## Monitoring

The load balancer continuously monitors:
- Session discovery (every 5 seconds)
- Resource usage tracking
- Stall detection
- Load distribution

## Configuration

Default settings (configurable):
- `max_cpu_per_session`: 50.0%
- `max_memory_per_session_mb`: 2048.0 MB
- `max_requests_per_session`: 10
- `stall_timeout_seconds`: 30

## Benefits

1. **Prevents Stalling**: Detects and routes away from stalled sessions
2. **Fair Distribution**: Ensures all sessions get fair resource allocation
3. **Automatic Failover**: Routes to target host if local is overloaded
4. **Resource Protection**: Prevents any session from hogging resources
5. **Performance**: Maintains optimal performance across all sessions

## Current Status

**Discovered**: 39 IDE sessions on host "Millennium-Falcon"
- Most sessions are active and healthy
- Load balancing is working correctly
- No stalled sessions detected

## Files

- `scripts/python/ide_session_load_balancer.py`: Main implementation
- `data/ide_sessions/session_state.json`: Session state storage
- `scripts/python/symbiotic_cluster_coordinator.py`: Integration

---

**Status**: ✅ **OPERATIONAL**  
**Sessions Tracked**: 39  
**Stalled Sessions**: 0  
**Maintained By**: @JARVIS  
**Last Updated**: 2025-01-24

