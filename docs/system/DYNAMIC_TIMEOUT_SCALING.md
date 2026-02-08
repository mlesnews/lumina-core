# Dynamic Timeout Scaling - Account for LUMINA System Latency

**Status**: ✅ **IMPLEMENTED & INTEGRATED**

---

## The Problem

**"SO I'M NOTICING THAT IF I GIVE IT A 'MOMENT' THAT @ASK SENDS AND RETRIES**
**THAT ENCOUNTER THE COMMUNICATION TIMEOUTS, IS JUST US NOT ACCOUNTING FOR**
**THE LATENCY OF THE LUMINA PROJECT AND ITS SYSTEMS. AND NOT MITIGATING FOR IT.**
**/FIX PLEASE? @DYNAMIC-SCALING OF TIMEOUTS? NOT A NEW CONCEPT FOR US EH?"**

---

## The Solution

### Dynamic Timeout Scaling

**Dynamic timeout scaling based on:**
- Measured LUMINA system latency
- Historical latency patterns
- System load
- Adaptive retry with exponential backoff

---

## How It Works

### 1. Latency Measurement

**Measures latency for each system/operation:**
- Records successful and failed operations
- Maintains rolling window of last 100 measurements
- Calculates average latency

### 2. Dynamic Timeout Calculation

**Timeout = max(**
- **min_timeout,**
- **min(**
  - **max_timeout,**
  - **base_timeout * adaptive_factor * (1 + latency_seconds * latency_multiplier)**
- **)**
**)**

**Default Configuration:**
- Base timeout: 30 seconds
- Min timeout: 10 seconds
- Max timeout: 300 seconds (5 minutes)
- Latency multiplier: 3.0x
- Adaptive factor: 1.5x

### 3. Exponential Backoff Retry

**Retry logic:**
- Max retries: 3
- Exponential backoff: 2^attempt seconds
- Timeout increases with each retry
- Accounts for system latency

---

## Integration

### Requests Wrapper

**Convenience functions for HTTP requests:**

```python
from dynamic_timeout_scaling import (
    get_with_dynamic_timeout,
    post_with_dynamic_timeout,
    put_with_dynamic_timeout,
    delete_with_dynamic_timeout
)

# GET request with dynamic timeout
response = get_with_dynamic_timeout(
    system="symbiotic_cluster",
    operation="check_endpoint",
    url="http://example.com/api"
)

# POST request with dynamic timeout
response = post_with_dynamic_timeout(
    system="symbiotic_cluster",
    operation="route_request",
    url="http://example.com/api",
    json=data
)
```

### Integrated Systems

**✅ Symbiotic Cluster Coordinator**
- Uses dynamic timeout for route requests
- Uses dynamic timeout for endpoint checks
- Accounts for LUMINA system latency

**✅ LUMINA Ultimate Goal**
- Uses dynamic timeout for @WOPR explorations
- Measures latency and adapts timeouts

**More integrations coming...**

---

## Usage

### Configure System Timeout

```bash
python scripts/python/dynamic_timeout_scaling.py --configure "system_name" "base_timeout" "min_timeout" "max_timeout" "multiplier"
```

**Example:**
```bash
python scripts/python/dynamic_timeout_scaling.py --configure "symbiotic_cluster" "45" "15" "300" "3.0"
```

### Get Dynamic Timeout

```bash
python scripts/python/dynamic_timeout_scaling.py --get-timeout "system_name" "operation"
```

**Example:**
```bash
python scripts/python/dynamic_timeout_scaling.py --get-timeout "symbiotic_cluster" "route_request"
```

### Get Statistics

```bash
python scripts/python/dynamic_timeout_scaling.py --statistics [system_name]
```

**Example:**
```bash
python scripts/python/dynamic_timeout_scaling.py --statistics symbiotic_cluster
```

---

## Configuration

### Per-System Configuration

**Configure timeout settings for specific systems:**

```python
from dynamic_timeout_scaling import get_timeout_scaler, TimeoutConfig

scaler = get_timeout_scaler()

config = TimeoutConfig(
    base_timeout=45.0,  # 45 seconds base
    min_timeout=15.0,   # Minimum 15 seconds
    max_timeout=300.0,  # Maximum 5 minutes
    latency_multiplier=3.0,
    adaptive_factor=1.5,
    retry_backoff_base=2.0,
    max_retries=3
)

scaler.configure_system("symbiotic_cluster", config)
```

---

## Statistics

### Latency Metrics

**Tracks:**
- Total measurements
- Successful vs failed
- Average latency (ms)
- Median latency (ms)
- Min/Max latency (ms)
- Current dynamic timeout

### Timeout Metrics

**Tracks:**
- Current timeout (dynamically calculated)
- Base timeout (configured)
- Min/Max timeout (configured)

---

## The Fix

### Before

**Hardcoded timeouts:**
```python
response = requests.post(url, json=data, timeout=60)  # Fixed 60s timeout
```

**Problems:**
- Doesn't account for LUMINA system latency
- Timeouts too short for slow systems
- Timeouts too long for fast systems
- No adaptation to changing conditions

### After

**Dynamic timeouts:**
```python
response = post_with_dynamic_timeout(
    system="symbiotic_cluster",
    operation="route_request",
    url=url,
    json=data
)  # Dynamically calculated timeout based on measured latency
```

**Benefits:**
- Accounts for LUMINA system latency
- Adapts to system conditions
- Reduces timeout errors
- Improves reliability

---

## The Bottom Line

### The Problem

**"IF I GIVE IT A 'MOMENT' THAT @ASK SENDS AND RETRIES**
**THAT ENCOUNTER THE COMMUNICATION TIMEOUTS, IS JUST US NOT ACCOUNTING FOR**
**THE LATENCY OF THE LUMINA PROJECT AND ITS SYSTEMS."**

### The Solution

**Dynamic timeout scaling:**
- Measures LUMINA system latency
- Adapts timeouts based on measurements
- Retries with exponential backoff
- Accounts for system conditions

### The Result

**No more communication timeouts due to:**
- Unaccounted latency
- Fixed timeouts
- System load variations

**Instead:**
- Dynamic timeouts that adapt
- Retry logic that accounts for latency
- Reliable communication

---

**Status**: ✅ **IMPLEMENTED & INTEGRATED**  
**Problem**: Communication timeouts due to unaccounted LUMINA system latency  
**Solution**: Dynamic timeout scaling with latency measurement  
**Integration**: Symbiotic Cluster Coordinator, LUMINA Ultimate Goal  
**Result**: Reliable communication with adaptive timeouts
