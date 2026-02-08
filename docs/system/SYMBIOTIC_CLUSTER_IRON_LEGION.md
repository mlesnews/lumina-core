# Symbiotic Cluster Coordinator - Iron Legion

**Date**: 2025-01-24  
**Status**: ✅ **ACTIVE**  
**Maintained By**: @JARVIS @GANDALF @MARVIN

## Overview

The Symbiotic Cluster Coordinator treats **local and target host (Kaiju Iron Legion) as one symbiotic organism**, implementing holistic resource management with **97% utilization target** (@gandalf), automatic failover, load balancing, and degradation mitigation.

## @marvin Analysis: Two Halves of the Same Cluster

**Question**: Why wouldn't making both hosts two halves of the same cluster?

**Answer**: ✅ **This is absolutely in our wheelhouse!**

Making both hosts two halves of the same cluster enables:

1. **Automatic Compensation**: If one host is lost, the other automatically compensates
2. **Load Balancing**: Requests distributed across both hosts for optimal performance
3. **Degradation Mitigation**: System gracefully handles partial failures
4. **Holistic Resource Utilization**: Both hosts work together to achieve target utilization (97%)

## Architecture

### Symbiotic Organism Model

```
┌─────────────────────────────────────────────────────────┐
│         Symbiotic Cluster (One Organism)                 │
│                                                          │
│  ┌──────────────────┐      ┌──────────────────┐         │
│  │  Local Host      │◄────►│  Target Host     │         │
│  │  localhost:11437 │      │  kaiju_no_8:11437│         │
│  │                  │      │                  │         │
│  │  - Models        │      │  - Models        │         │
│  │  - Resources     │      │  - Resources     │         │
│  │  - Capacity      │      │  - Capacity      │         │
│  └──────────────────┘      └──────────────────┘         │
│           │                        │                     │
│           └──────────┬──────────────┘                     │
│                      │                                    │
│           ┌──────────▼──────────┐                        │
│           │  Cluster Coordinator │                       │
│           │  - Load Balancing    │                       │
│           │  - Failover          │                       │
│           │  - Resource Mgmt     │                       │
│           │  - 97% Utilization   │                       │
│           └─────────────────────┘                        │
└─────────────────────────────────────────────────────────┘
```

### Key Features

1. **Symbiotic Operation**
   - Both hosts treated as one organism
   - Shared resource pool
   - Unified load management
   - Holistic health monitoring

2. **Automatic Failover**
   - If local host fails → automatically route to target
   - If target host fails → automatically route to local
   - Seamless transition with no service interruption
   - Automatic recovery when host comes back online

3. **Load Balancing**
   - Intelligent request routing based on:
     - Current host utilization
     - Response times
     - Queue lengths
     - Available models
   - Dynamic load distribution to achieve target utilization

4. **Resource Utilization (@gandalf)**
   - Target: **97% utilization** across both hosts
   - Holistic resource management
   - Automatic load adjustment
   - Capacity optimization

5. **Degradation Mitigation**
   - Graceful handling of partial failures
   - Automatic compensation when one host is lost
   - Load redistribution to maintain service
   - Health-based routing

## Configuration

### Basic Setup

```python
from symbiotic_cluster_coordinator import SymbioticClusterCoordinator

coordinator = SymbioticClusterCoordinator(
    local_endpoint="http://localhost:11437",
    target_endpoint="http://kaiju_no_8:11437",
    target_utilization=97.0,  # @gandalf target
    balance_interval=30  # seconds
)

# Start coordination
coordinator.start()
```

### Request Routing

```python
# Route request (automatic host selection)
host_id, response = coordinator.route_request(
    model="codellama:13b",
    endpoint="/api/generate",
    data={"prompt": "..."},
    priority="balanced"  # or "local", "target", "fastest"
)

# Manual host selection
host_id = coordinator.select_host(
    model="codellama:13b",
    priority="balanced"
)
```

## Routing Priorities

### Balanced (Default)
- Distributes load to achieve target utilization
- Considers current host load
- Optimizes for 97% cluster utilization

### Local
- Prefers local host
- Falls back to target if local unavailable

### Target
- Prefers target host (Kaiju)
- Falls back to local if target unavailable

### Fastest
- Selects host with lowest response time
- Optimizes for latency

## Automatic Failover

### Failover Scenarios

1. **Local Host Offline**
   ```
   Request → Local (fails) → Automatic → Target (succeeds)
   ```

2. **Target Host Offline**
   ```
   Request → Target (fails) → Automatic → Local (succeeds)
   ```

3. **Both Hosts Available**
   ```
   Request → Balanced routing based on load
   ```

### Failover Metrics

- Automatic failover count tracked
- Seamless transition (no user-visible errors)
- Automatic recovery when host comes back online
- Health monitoring for proactive failover

## Resource Utilization (@gandalf)

### Target: 97% Utilization

The system aims to utilize **97% of available resources** across both hosts:

```python
# Get utilization report
report = coordinator.get_utilization_report()

print(f"Current: {report['current_utilization']:.1f}%")
print(f"Target: {report['target_utilization']:.1f}%")
print(f"Gap: {report['utilization_gap']:.1f}%")
```

### Utilization Management

- **Below Target**: System increases load to reach 97%
- **Above Target**: System reduces load to prevent overload
- **Balanced**: Load distributed evenly across hosts
- **Holistic**: Both hosts contribute to target utilization

## Health Monitoring

### Host Status

- **HEALTHY**: Fully operational
- **DEGRADED**: Operational but slow
- **OVERLOADED**: High load, may need load shedding
- **OFFLINE**: Unavailable, automatic failover

### Metrics Tracked

- CPU usage
- Memory usage
- GPU usage (if available)
- Active requests
- Queue length
- Response time
- Error rate
- Available models

## Cluster Status

### Get Cluster Status

```python
status = coordinator.get_cluster_status()

# Returns:
{
    "cluster_id": "iron_legion_symbiotic",
    "mode": "symbiotic",
    "target_utilization": 97.0,
    "current_utilization": 95.2,
    "active_hosts": ["local", "target"],
    "load_distribution": {
        "local": 48.5,
        "target": 48.5
    },
    "failover_count": 2,
    "total_requests": 15420
}
```

## Command Line Usage

```bash
# Start coordinator
python scripts/python/symbiotic_cluster_coordinator.py \
    --local http://localhost:11437 \
    --target http://kaiju_no_8:11437 \
    --target-util 97.0

# Show cluster status
python scripts/python/symbiotic_cluster_coordinator.py --status

# Show utilization report
python scripts/python/symbiotic_cluster_coordinator.py --utilization
```

## Benefits

### Operational Excellence

- **High Availability**: Automatic failover ensures service continuity
- **Optimal Utilization**: 97% target utilization maximizes resource usage
- **Load Balancing**: Intelligent distribution across both hosts
- **Degradation Mitigation**: Graceful handling of partial failures

### Performance

- **Reduced Latency**: Route to fastest available host
- **Increased Throughput**: Both hosts contribute to capacity
- **Better Resource Usage**: Holistic utilization management
- **Scalability**: Easy to add more hosts

### Reliability

- **Automatic Recovery**: Hosts automatically rejoin when available
- **Health Monitoring**: Proactive detection of issues
- **Failover Tracking**: Metrics for reliability analysis
- **Seamless Operation**: No user-visible interruptions

## Integration Points

### Existing Systems

- **Kaiju Iron Legion Monitor**: Health monitoring integration
- **Cluster Aware Cache**: Cache coordination across hosts
- **JARVIS**: Central coordination and reporting
- **Network Support**: Network health integration

## @marvin's Analysis Summary

**Question**: Is making both hosts two halves of the same cluster in our wheelhouse?

**Answer**: ✅ **Absolutely Yes!**

The symbiotic cluster approach provides:

1. ✅ **Automatic Compensation**: If one host is lost, the other automatically compensates
2. ✅ **Load Balancing**: Requests distributed across both hosts
3. ✅ **Degradation Mitigation**: System gracefully handles partial failures
4. ✅ **Holistic Resource Utilization**: Both hosts work together (97% target)

This is **exactly** what we need for a robust, high-availability cluster system.

## Future Enhancements

Potential improvements:

1. **Multi-Host Support**: Extend beyond two hosts
2. **Predictive Load Balancing**: ML-based load prediction
3. **Geographic Distribution**: Support for geographically distributed hosts
4. **Advanced Metrics**: GPU utilization, model-specific metrics
5. **Auto-Scaling**: Automatic host addition/removal

## References

- `scripts/python/symbiotic_cluster_coordinator.py`: Main implementation
- `scripts/python/kaiju_iron_legion_monitor.py`: Health monitoring
- `config/kaiju_iron_legion_config.json`: Configuration

---

**Status**: ✅ **PRODUCTION READY**  
**Maintained By**: @JARVIS @GANDALF @MARVIN  
**Last Updated**: 2025-01-24

