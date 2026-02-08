# DNS Cluster with Caching and Failover

**Date**: 2025-01-24  
**Status**: ✅ **IMPLEMENTED**

---

## Overview

Two-node DNS cluster with:
- **Primary DNS**: NAS (Synology DSM) - `10.17.17.32:53`
- **Secondary DNS**: pfSense firewall - `10.17.17.1:53`
- **DNS Caching**: Response caching with TTL
- **Automatic Failover**: Primary → Secondary on failure
- **Health Monitoring**: Continuous health checks
- **Automatic Failback**: Secondary → Primary on recovery

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│         DNS Cluster Manager                     │
│  (Two-Node Cluster with Caching)               │
└─────────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
┌─────────────┐ ┌──────────┐ ┌──────────────┐
│ Primary DNS │ │Secondary │ │ DNS Cache    │
│ NAS (DSM)   │ │pfSense   │ │ (TTL-based)  │
│ 10.17.17.32 │ │10.17.17.1│ │              │
└─────────────┘ └──────────┘ └──────────────┘
        │           │           │
        └───────────┴───────────┘
                    │
            Automatic Failover
```

---

## Features

### 1. DNS Caching

**Purpose**: Reduce DNS queries and improve performance

**How it works**:
- Caches DNS responses with TTL (Time To Live)
- Default TTL: 300 seconds (5 minutes)
- Cache hit: Returns cached result immediately
- Cache miss: Queries DNS server, then caches result

**Benefits**:
- ✅ Faster DNS resolution
- ✅ Reduced network traffic
- ✅ Lower DNS server load
- ✅ Better performance

**Example**:
```python
from dns_cluster_manager import DNSClusterManager

cluster = DNSClusterManager(enable_cache=True, cache_ttl=300)

# First query: Hits DNS server, caches result
ip1 = cluster.resolve("example.com")  # ~30ms

# Second query: Cache hit, instant response
ip2 = cluster.resolve("example.com")  # ~0.1ms (cached)
```

### 2. Two-Node Cluster

**Primary DNS**: NAS (Synology DSM)
- Host: `10.17.17.32`
- Port: `53`
- Type: Primary DNS server
- Source: Synology DSM DNS Server package

**Secondary DNS**: pfSense Firewall
- Host: `10.17.17.1` (typical gateway IP)
- Port: `53`
- Type: Secondary DNS (failover)
- Source: pfSense DNS Resolver/Forwarder

### 3. Automatic Failover

**How it works**:
1. **Health Check**: Monitors primary DNS every 30 seconds
2. **Failure Detection**: If primary fails, switch to secondary
3. **Automatic Switch**: Seamless failover to pfSense
4. **Recovery**: When primary recovers, failback automatically

**Failover Process**:
```
Primary DNS (NAS) → Health Check Fails
    ↓
Switch to Secondary (pfSense)
    ↓
Continue DNS resolution via pfSense
    ↓
Monitor Primary for recovery
    ↓
Primary Recovers → Failback to Primary
```

### 4. Health Monitoring

**Continuous Monitoring**:
- Health checks every 30 seconds
- Response time tracking
- Failure count tracking
- Last check timestamp

**Metrics Tracked**:
- `is_healthy`: Boolean health status
- `response_time_ms`: DNS query response time
- `failure_count`: Consecutive failures
- `last_health_check`: Timestamp of last check

---

## Usage

### Basic Usage

```python
from dns_cluster_manager import DNSClusterManager, DNSServer

# Create cluster
cluster = DNSClusterManager(
    primary_dns=DNSServer(
        name="NAS Primary DNS",
        host="10.17.17.32",
        port=53,
        type="primary"
    ),
    secondary_dns=DNSServer(
        name="pfSense Secondary DNS",
        host="10.17.17.1",
        port=53,
        type="secondary"
    ),
    enable_cache=True,
    cache_ttl=300
)

# Resolve hostname (with caching and failover)
ip = cluster.resolve("example.com")
print(f"Resolved: {ip}")

# Reverse DNS lookup
hostname = cluster.reverse_resolve("93.184.216.34")
print(f"Reverse: {hostname}")

# Get cluster status
status = cluster.get_cluster_status()
print(f"Primary Healthy: {status['primary_dns']['healthy']}")
print(f"Secondary Healthy: {status['secondary_dns']['healthy']}")
print(f"Failover Active: {status['failover_active']}")
```

### CLI Usage

#### Check Cluster Status

```bash
python scripts/python/dns_cluster_manager.py --status
```

**Output**:
```
🏛️  DNS Cluster Status:

Primary DNS:
  Name: NAS Primary DNS
  Host: 10.17.17.32
  Healthy: ✅
  Response Time: 33.21ms

Secondary DNS:
  Name: pfSense Secondary DNS
  Host: 10.17.17.1
  Healthy: ✅
  Response Time: 1.05ms

Current DNS: NAS Primary DNS
Failover Active: ✅ No

Cache:
  Valid Entries: 0
  Total Entries: 0
```

#### Resolve Hostname

```bash
python scripts/python/dns_cluster_manager.py --resolve example.com
```

**Output**:
```
✅ example.com → 93.184.216.34
```

#### Reverse DNS Lookup

```bash
python scripts/python/dns_cluster_manager.py --reverse 93.184.216.34
```

**Output**:
```
✅ 93.184.216.34 → example.com
```

#### Clear Cache

```bash
# Clear specific hostname
python scripts/python/dns_cluster_manager.py --clear-cache example.com

# Clear all cache
python scripts/python/dns_cluster_manager.py --clear-cache all
```

---

## Integration with Network Security Orchestrator

### Automatic Integration

The Network Security Orchestrator automatically uses the DNS cluster:

```python
from network_security_orchestrator import NetworkSecurityOrchestrator

orchestrator = NetworkSecurityOrchestrator()

# Automatically uses DNS cluster with caching and failover
result = orchestrator.secure_network_endpoint(
    "http://nas.local:5001",
    verify_dns=True,
    verify_reverse_dns=True
)

# DNS resolution uses:
# 1. DNS cache (if available)
# 2. Primary DNS (NAS)
# 3. Secondary DNS (pfSense) if primary fails
```

---

## DNS Caching Details

### Cache Structure

```python
@dataclass
class DNSCacheEntry:
    hostname: str
    ip_address: str
    record_type: str = "A"  # A, AAAA, PTR
    ttl: int = 300  # seconds
    cached_at: datetime
    expires_at: datetime
    source: str = "unknown"  # primary, secondary, cache
```

### Cache Operations

**Get from Cache**:
```python
entry = cache.get("example.com", "A")
if entry and datetime.now() < entry.expires_at:
    return entry.ip_address  # Cache hit
```

**Set in Cache**:
```python
cache.set(
    hostname="example.com",
    ip_address="93.184.216.34",
    record_type="A",
    ttl=300,
    source="primary"
)
```

**Cache Expiration**:
- Entries expire based on TTL
- Expired entries are automatically removed
- Cache size is tracked

---

## Failover Scenarios

### Scenario 1: Primary DNS Failure

```
1. Primary DNS (NAS) becomes unavailable
2. Health check fails
3. Automatic failover to Secondary (pfSense)
4. DNS resolution continues via pfSense
5. Primary monitored for recovery
6. Primary recovers → Automatic failback
```

### Scenario 2: Network Partition

```
1. Primary DNS unreachable
2. Secondary DNS (pfSense) still accessible
3. Failover to Secondary
4. DNS resolution continues
5. When network recovers, failback to Primary
```

### Scenario 3: Both DNS Servers Down

```
1. Primary fails → Failover to Secondary
2. Secondary also fails
3. DNS resolution fails
4. Error logged
5. Retry when servers recover
```

---

## pfSense Integration

### pfSense DNS Configuration

**pfSense DNS Resolver/Forwarder**:
- Service: DNS Resolver (Unbound) or DNS Forwarder
- Port: 53
- IP: `10.17.17.1` (gateway)
- Role: Secondary DNS server

**Configuration**:
1. Enable DNS Resolver in pfSense
2. Configure as secondary DNS
3. Set up zone transfers (if needed)
4. Configure caching

### Benefits of pfSense as Secondary

- ✅ **High Availability**: Router is always on
- ✅ **Network Gateway**: Central network device
- ✅ **Caching**: Built-in DNS caching
- ✅ **Reliability**: Separate from NAS
- ✅ **Performance**: Fast response times

---

## Performance Metrics

### With Caching

- **First Query**: ~30-50ms (DNS server query)
- **Cached Query**: ~0.1-1ms (cache lookup)
- **Cache Hit Rate**: 70-90% (typical)
- **Performance Improvement**: 30-500x faster

### Without Caching

- **Every Query**: ~30-50ms
- **No Performance Benefit**: All queries hit DNS server
- **Higher Load**: More DNS server requests

---

## Recommendations

### ✅ DO

- Enable DNS caching (default: 300s TTL)
- Use two-node cluster (primary + secondary)
- Monitor health continuously
- Configure automatic failover
- Use pfSense as secondary DNS

### ❌ DON'T

- Disable caching (unless debugging)
- Use single DNS server (no redundancy)
- Ignore health checks
- Manual failover (use automatic)
- Skip secondary DNS configuration

---

## Configuration

### Default Configuration

```python
DNSClusterManager(
    primary_dns=DNSServer(
        name="NAS Primary DNS",
        host="10.17.17.32",
        port=53,
        type="primary"
    ),
    secondary_dns=DNSServer(
        name="pfSense Secondary DNS",
        host="10.17.17.1",
        port=53,
        type="secondary"
    ),
    enable_cache=True,
    cache_ttl=300  # 5 minutes
)
```

### Custom Configuration

```python
# Custom primary DNS
primary = DNSServer(
    name="Custom Primary",
    host="192.168.1.10",
    port=53,
    type="primary",
    health_check_interval=60  # Check every 60 seconds
)

# Custom secondary DNS
secondary = DNSServer(
    name="Custom Secondary",
    host="192.168.1.1",
    port=53,
    type="secondary"
)

cluster = DNSClusterManager(
    primary_dns=primary,
    secondary_dns=secondary,
    enable_cache=True,
    cache_ttl=600  # 10 minutes
)
```

---

## Status

✅ **DNS Cluster Manager**: Implemented  
✅ **DNS Caching**: Working  
✅ **Two-Node Cluster**: Configured  
✅ **Automatic Failover**: Working  
✅ **Health Monitoring**: Active  
✅ **pfSense Integration**: Ready  
✅ **Network Security Integration**: Complete  

---

## Related Files

- `scripts/python/dns_cluster_manager.py` - DNS Cluster Manager
- `scripts/python/network_security_orchestrator.py` - Security Orchestrator
- `scripts/python/nas_dns_manager.py` - NAS DNS Manager
- `docs/NAS_DNS_ACTIVE_DIRECTORY_INTEGRATION.md` - DNS integration docs

---

**Last Updated**: 2025-01-24

