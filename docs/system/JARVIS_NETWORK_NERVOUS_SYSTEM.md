# JARVIS Network Nervous System

**Date**: 2025-01-24  
**Status**: ✅ **ACTIVE**  
**Maintained By**: @JARVIS

## Overview

The JARVIS Network Nervous System maps the **home lab as JARVIS's body**, with all network devices, domain devices, and hosts as the **nervous system**.

### Concept

```
Home Lab = JARVIS's Body
Network = Nervous System
Devices/Hosts = Neurons/Nodes
Domain = Central Nervous System
```

## Architecture

### Nervous System Roles

1. **CORE** - Critical systems (brain stem)
   - JARVIS core services
   - Master coordination
   - Critical infrastructure

2. **PROCESSOR** - Processing nodes (neurons)
   - Compute hosts (KAIJU, workstations)
   - LLM clusters
   - Processing services

3. **STORAGE** - Memory/storage (synapses)
   - NAS devices
   - Storage servers
   - Backup systems

4. **GATEWAY** - Network gateway (spinal cord)
   - Routers
   - Firewalls
   - Network switches

5. **SENSOR** - Monitoring/sensing (sensory neurons)
   - Monitoring devices
   - Health check systems
   - Metrics collectors

6. **ACTUATOR** - Action/control (motor neurons)
   - Control systems
   - Automation devices
   - Actuator services

7. **COORDINATOR** - Coordination (cerebellum)
   - Coordination services
   - Load balancers
   - Orchestration systems

## Device Types

- **HOST** - General purpose host
- **NAS** - Network attached storage
- **ROUTER** - Network router
- **SWITCH** - Network switch
- **FIREWALL** - Firewall device
- **SERVER** - Server system
- **WORKSTATION** - Workstation computer
- **LAPTOP** - Laptop computer
- **MOBILE** - Mobile device
- **IOT** - IoT device
- **PRINTER** - Network printer
- **STORAGE** - Storage device
- **HYPERVISOR** - Virtualization host
- **CONTAINER** - Container host
- **SERVICE** - Service endpoint
- **API** - API endpoint

## Usage

### Discover Devices

```bash
# Discover all devices on network
python scripts/python/jarvis_network_nervous_system.py --discover
```

### View Nervous System Map

```bash
# Show complete nervous system map
python scripts/python/jarvis_network_nervous_system.py --map
```

### List Devices

```bash
# List all devices
python scripts/python/jarvis_network_nervous_system.py --devices

# Filter by role
python scripts/python/jarvis_network_nervous_system.py --devices --role processor

# Filter by type
python scripts/python/jarvis_network_nervous_system.py --devices --type nas
```

### Python API

```python
from jarvis_network_nervous_system import JARVISNetworkNervousSystem

# Initialize
nervous_system = JARVISNetworkNervousSystem()

# Discover devices
devices = nervous_system.discover_devices()

# Get nervous system map
map_data = nervous_system.get_nervous_system_map()

# Get devices by role
processors = nervous_system.get_devices_by_role(NervousSystemRole.PROCESSOR)

# Get devices by type
nas_devices = nervous_system.get_devices_by_type(DeviceType.NAS)
```

## Device Discovery

### Automatic Discovery

The system automatically discovers devices by:
1. Scanning local network subnet
2. Probing known IP addresses
3. Checking configured devices
4. Detecting services on common ports

### Known Devices

Devices are loaded from:
- `config/homelab_ai_ecosystem.json`
- `config/lumina_nas_ssh_config.json`
- `config/kaiju_iron_legion_config.json`

### Service Detection

Automatically detects services on:
- Port 22: SSH
- Port 80: HTTP
- Port 443: HTTPS
- Port 8000: API
- Port 11437: Ollama
- Port 5001: Synology
- Port 8080: HTTP-alt

## Device Inventory

### Device Information

Each device tracks:
- Device ID and name
- IP address and MAC address
- Hostname and domain
- Device type and nervous role
- Operating system
- Running services
- Open ports
- Capabilities
- Status (online/offline/degraded)
- Discovery timestamps

### Network Interfaces

Each device can have multiple network interfaces:
- Interface name
- IP address
- MAC address
- Subnet mask
- Gateway
- DNS servers
- Status and speed

## Integration

### With Organizational Structure

Devices can be mapped to organizational members:
- Network engineers manage network devices
- System administrators manage servers
- Analysts monitor device health

### With Symbiotic Cluster

Devices are part of the symbiotic cluster:
- Local host = local device
- Target host (KAIJU) = target device
- Both treated as one organism

### With Network Support

Network support workflows use device inventory:
- Health checks use device list
- Diagnostics probe devices
- Remediation targets specific devices

## Continuous Discovery

### Start Continuous Discovery

```python
# Start continuous discovery (every hour)
nervous_system.start_continuous_discovery(interval=3600)
```

### Stop Discovery

```python
nervous_system.stop_continuous_discovery()
```

## Data Storage

### Inventory File

Device inventory saved to:
`data/network_nervous_system/device_inventory.json`

### Structure

```json
{
  "timestamp": "2025-01-24T...",
  "devices": {
    "device_id": {
      "device_id": "...",
      "name": "...",
      "device_type": "host",
      "nervous_role": "processor",
      "ip_address": "10.17.17.32",
      "status": "online",
      "services": ["ssh", "http"],
      ...
    }
  },
  "networks": {...},
  "domain_devices": [...]
}
```

## Statistics

The nervous system map includes:
- Total devices
- Online devices
- Domain devices
- Devices by role
- Devices by type

## Command Reference

```bash
# Discover devices
python scripts/python/jarvis_network_nervous_system.py --discover

# Show map
python scripts/python/jarvis_network_nervous_system.py --map

# List devices
python scripts/python/jarvis_network_nervous_system.py --devices

# Filter by role
python scripts/python/jarvis_network_nervous_system.py --devices --role processor

# Filter by type
python scripts/python/jarvis_network_nervous_system.py --devices --type nas

# JSON output
python scripts/python/jarvis_network_nervous_system.py --map --json
```

## Files

- `scripts/python/jarvis_network_nervous_system.py`: Main implementation
- `data/network_nervous_system/device_inventory.json`: Device inventory
- `config/homelab_ai_ecosystem.json`: Known devices

## References

- `docs/system/LUMINA_ORGANIZATIONAL_STRUCTURE.md`: Organizational mapping
- `docs/system/SYMBIOTIC_CLUSTER_IRON_LEGION.md`: Cluster integration
- `config/homelab_ai_ecosystem.json`: Ecosystem configuration

---

**Status**: ✅ **PRODUCTION READY**  
**Maintained By**: @JARVIS  
**Last Updated**: 2025-01-24

