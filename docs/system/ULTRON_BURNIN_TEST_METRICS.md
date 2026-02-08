# ULTRON Virtual Cluster - Burn-In Test with Tokens/Sec Gauge & Metrics/Analytics

**Status**: ✅ **IMPLEMENTED**

---

## Overview

Comprehensive burn-in testing system for ULTRON Virtual Cluster with:
- **Real-time tokens/sec gauges** (visual ASCII bars)
- **Performance metrics** (response times, throughput)
- **Comprehensive analytics** (cluster-wide and per-node)
- **Load testing** across all nodes
- **Time-series data collection**

---

## Features

### 1. Real-Time Tokens/Sec Gauges

**Visual ASCII Gauges** displaying tokens per second for each node:

```
📊 REAL-TIME TOKENS/SEC GAUGES:

ULTRON Standalone         [████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░]  45.23 tokens/sec ( 75.4%)
KAIJU/Iron Legion         [████████████████████████████████████████████████]  89.67 tokens/sec (100.0%)
FALC/Millennium Falcon    [████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░]  38.12 tokens/sec ( 63.5%)
```

**Features**:
- Real-time updates (every 1 second)
- Visual percentage bars
- Per-node tokens/sec display
- Auto-scaling max value (120% of peak)

### 2. Performance Metrics

**Per-Node Metrics**:
- Requests sent/succeeded/failed
- Total tokens generated
- Tokens per second
- Average/min/max response times
- Success rate percentage
- Error tracking

**Cluster-Wide Metrics**:
- Total requests across all nodes
- Total tokens generated
- Cluster tokens per second
- Average response time
- Overall success rate

### 3. Comprehensive Analytics

**Analytics Include**:
- Test duration
- Request distribution
- Token generation rates
- Response time statistics
- Error analysis
- Performance trends

---

## Usage

### Basic Usage

```bash
# Run 60-second burn-in test with default settings
python scripts/python/ultron_cluster_burnin_test.py

# Run with custom duration and rate
python scripts/python/ultron_cluster_burnin_test.py --duration 120 --rate 2.0

# Test specific nodes only
python scripts/python/ultron_cluster_burnin_test.py --nodes ultron kaiju

# Save analytics report
python scripts/python/ultron_cluster_burnin_test.py --save-report
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--duration` | Test duration in seconds | 60 |
| `--rate` | Requests per second | 1.0 |
| `--max-tokens` | Max tokens per request | 100 |
| `--nodes` | Nodes to test (ultron, kaiju, falc) | All nodes |
| `--save-report` | Save analytics report | False |
| `--output` | Custom output path | Auto-generated |

---

## Real-Time Display

### Gauge Display Format

The real-time display updates every second and shows:

1. **Header**: Test name and elapsed time
2. **Tokens/Sec Gauges**: Visual bars for each node
3. **Metrics Summary**: Per-node performance metrics
4. **Controls**: Instructions to stop early

### Example Output

```
================================================================================
🔥 ULTRON Virtual Cluster - BURN-IN TEST (Elapsed: 15.3s)
================================================================================

📊 REAL-TIME TOKENS/SEC GAUGES:

ULTRON Standalone         [████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░]  45.23 tokens/sec ( 75.4%)
KAIJU/Iron Legion         [████████████████████████████████████████████████]  89.67 tokens/sec (100.0%)
FALC/Millennium Falcon    [████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░]  38.12 tokens/sec ( 63.5%)

================================================================================
METRICS SUMMARY:
================================================================================

ULTRON Standalone:
  Requests: 15/15 (100.0% success)
  Tokens: 678 total, 45.23 tokens/sec
  Response Time: avg=234.56ms, min=189.23ms, max=312.45ms

KAIJU/Iron Legion:
  Requests: 15/15 (100.0% success)
  Tokens: 1,345 total, 89.67 tokens/sec
  Response Time: avg=156.78ms, min=123.45ms, max=198.90ms

FALC/Millennium Falcon:
  Requests: 15/15 (100.0% success)
  Tokens: 572 total, 38.12 tokens/sec
  Response Time: avg=267.89ms, min=234.56ms, max=345.67ms

================================================================================
Press Ctrl+C to stop early
================================================================================
```

---

## Metrics Collected

### Per-Node Metrics

```python
{
    "node_name": "ULTRON Standalone",
    "endpoint": "http://localhost:11434",
    "requests_sent": 60,
    "requests_succeeded": 58,
    "requests_failed": 2,
    "total_tokens": 2,710,
    "tokens_per_second": 45.17,
    "average_response_time_ms": 234.56,
    "min_response_time_ms": 189.23,
    "max_response_time_ms": 312.45,
    "success_rate": 96.67,
    "errors": ["Connection timeout", "Model not found"]
}
```

### Cluster-Wide Analytics

```python
{
    "test_duration_seconds": 60.0,
    "total_requests": 180,
    "total_tokens": 8,130,
    "cluster_tokens_per_second": 135.50,
    "cluster_average_response_time_ms": 219.41,
    "cluster_success_rate": 97.22
}
```

---

## Analytics Report

### Report Location

Reports are saved to:
```
data/burnin_tests/ultron_cluster_burnin_YYYYMMDD_HHMMSS.json
```

### Report Structure

```json
{
  "test_date": "2026-01-13T04:33:37",
  "analytics": {
    "test_duration_seconds": 60.0,
    "total_requests": 180,
    "total_tokens": 8130,
    "cluster_tokens_per_second": 135.50,
    "cluster_average_response_time_ms": 219.41,
    "cluster_success_rate": 97.22
  },
  "node_metrics": {
    "ultron": { ... },
    "kaiju": { ... },
    "falc": { ... }
  }
}
```

---

## Performance Benchmarks

### Expected Performance

| Node | Expected Tokens/Sec | Expected Response Time |
|------|---------------------|------------------------|
| ULTRON Standalone | 30-60 | 200-400ms |
| KAIJU/Iron Legion | 60-120 | 100-300ms |
| FALC/Millennium Falcon | 25-50 | 250-450ms |

### Performance Targets

- **Cluster Tokens/Sec**: > 100 tokens/sec
- **Success Rate**: > 95%
- **Average Response Time**: < 300ms
- **Max Response Time**: < 500ms

---

## Troubleshooting

### Zero Tokens/Sec

**Symptoms**: Gauges show 0.00 tokens/sec

**Possible Causes**:
1. Models not loaded on nodes
2. API endpoints unreachable
3. Network connectivity issues
4. Authentication failures

**Solutions**:
1. Verify models are loaded: `ollama list`
2. Check node connectivity: `curl http://localhost:11434/api/tags`
3. Verify network connectivity to KAIJU (10.17.17.11)
4. Check firewall rules

### Low Success Rate

**Symptoms**: Success rate < 90%

**Possible Causes**:
1. Model not available
2. Request timeout too short
3. Node overloaded
4. API errors

**Solutions**:
1. Verify model names match configuration
2. Increase timeout in test script
3. Reduce request rate
4. Check node logs for errors

### High Response Times

**Symptoms**: Response times > 500ms

**Possible Causes**:
1. Node overloaded
2. Network latency
3. Model size too large
4. System resource constraints

**Solutions**:
1. Reduce concurrent requests
2. Check network latency
3. Use smaller models
4. Monitor system resources (CPU, memory)

---

## Integration

### With Health Check System

The burn-in test integrates with the health check system:
- Uses same node endpoints
- Shares cluster configuration
- Compatible with health check metrics

### With V3 Battle Test

The burn-in test complements the V3 battle test:
- Battle test: Connectivity and failover
- Burn-in test: Performance under load
- Together: Complete cluster validation

---

## Advanced Usage

### Custom Load Patterns

Modify the `_generate_load` method to implement:
- Ramp-up patterns
- Spike testing
- Sustained load
- Stress testing

### Extended Analytics

Add custom analytics by:
- Extending `BurnInAnalytics` dataclass
- Adding time-series collection
- Implementing custom metrics
- Exporting to external systems

---

## Status

**Burn-In Test System**: ✅ **OPERATIONAL**

**Real-Time Gauges**: ✅ **WORKING**

**Metrics Collection**: ✅ **ACTIVE**

**Analytics Reporting**: ✅ **COMPLETE**

---

**Tags:** `#BURN_IN` `#PERFORMANCE` `#METRICS` `#ANALYTICS` `#TOKENS_PER_SEC` `#GAUGE` `#ULTRON` `#VIRTUAL_CLUSTER` `@JARVIS` `@BONES` `@LUMINA`

**Status:** ✅ **ULTRON BURN-IN TEST WITH TOKENS/SEC GAUGE & METRICS/ANALYTICS OPERATIONAL**
