# Homelab Comprehensive Inventory Audit

## Overview

Complete inventory audit system for the entire homelab environment (lesnewski.local) including all hardware devices, operating systems, applications, licenses, and network services.

## Features

- **Hardware Inventory**: Model, serial number, manufacturer, date acquired
- **OS Inventory**: Version, build, edition, license keys, product IDs
- **Application Inventory**: Installed software, versions, product keys, serial numbers
- **Network Discovery**: Device discovery, service scanning, endpoint mapping
- **License Tracking**: Product keys, serial numbers, license types
- **Historical Tracking**: Timestamped audits with master inventory

## Usage

### Full Audit (All Devices)

```bash
python scripts/python/homelab_comprehensive_inventory_audit.py --full
```

### Local Device Only

```bash
python scripts/python/homelab_comprehensive_inventory_audit.py --local-only
```

## What Gets Audited

### Hardware Information
- Manufacturer and model
- Serial number and asset tag
- Date acquired (if available)
- CPU (model, cores, threads)
- Memory (total GB)
- Storage devices (model, serial, size)
- Network interfaces (MAC addresses)
- GPU devices
- BIOS version and date
- Chassis type

### Operating System
- OS family (Windows/Linux/macOS)
- Name and version
- Build number
- Edition
- Architecture
- Install date
- Last boot time
- License key (Windows)
- Product ID
- License status

### Applications
- Application name
- Version
- Publisher
- Install date
- Install location
- Product key (if available)
- Serial number (if available)
- License type
- Service endpoints (if applicable)

### Network Services
- Service name
- Protocol (TCP/UDP)
- Port number
- Status (open/closed)
- Service type (SSH/HTTP/RDP/etc)
- Version information

## Output

### Files Generated

1. **Timestamped Inventory**: `data/homelab_inventory/inventory_YYYYMMDD_HHMMSS.json`
   - Complete snapshot of current state
   - Historical record

2. **Master Inventory**: `data/homelab_inventory/master_inventory.json`
   - Latest complete inventory
   - Updated with each audit

### Report Structure

```json
{
  "audit_date": "2026-01-03T13:00:00",
  "auditor": "hostname",
  "network_domain": "lesnewski.local",
  "summary": {
    "total_devices": 10,
    "by_type": {
      "server": 2,
      "workstation": 3,
      "nas": 1
    },
    "by_os_family": {
      "windows": 5,
      "linux": 3
    },
    "total_applications": 150,
    "total_services": 45
  },
  "devices": [...]
}
```

## Device Types

- **SERVER**: Server systems
- **WORKSTATION**: Desktop/laptop computers
- **NAS**: Network attached storage
- **ROUTER**: Network routers
- **SWITCH**: Network switches
- **FIREWALL**: Firewall appliances
- **PRINTER**: Printers
- **IOT**: IoT devices
- **MOBILE**: Mobile devices
- **VIRTUAL**: Virtual machines
- **UNKNOWN**: Unidentified devices

## Network Discovery

The system discovers devices by:
1. Local network scanning (nmap if available)
2. DNS resolution (lesnewski.local)
3. Common subnet ranges (192.168.x.x, 10.0.x.x)
4. Manual IP addresses

## Requirements

### Windows
- `wmi` package for hardware/OS info: `pip install wmi`
- `pywin32` for Windows registry access: `pip install pywin32`

### Linux
- Standard system commands: `lscpu`, `free`, `/sys/class/dmi/`
- `nmap` (optional) for network scanning: `apt install nmap` or `yum install nmap`

### All Platforms
- `psutil` (if not already installed): `pip install psutil`

## Security Notes

- **Product Keys**: Windows product keys are retrieved from registry (may require admin)
- **Serial Numbers**: Hardware serial numbers are read from system (no network access)
- **Network Scanning**: Port scanning is passive and only checks common ports
- **Credentials**: No credentials are stored or transmitted

## Integration

The inventory can be integrated with:
- Asset management systems
- License tracking systems
- Network monitoring
- Security auditing
- Compliance reporting

## Example Output

```
🏠 HOMELAB COMPREHENSIVE INVENTORY AUDIT
================================================================================
🔍 Discovering network devices...
   Local IP: 192.168.1.100
   Hostname: DESKTOP-ABC123
   Found 8 devices via nmap
✅ Discovered 8 devices to audit

📋 AUDITING LOCAL DEVICE
   Gathering hardware information...
   Gathering OS information...
   Gathering application information...
   Discovering network services...
✅ Local device audit complete: DESKTOP-ABC123
   Hardware: Dell Inc. OptiPlex 7090
   OS: Windows Windows 10 Pro
   Applications: 125
   Services: 5

📊 INVENTORY AUDIT SUMMARY
================================================================================
Total Devices: 8
By Type:
  workstation: 3
  server: 2
  nas: 1
  router: 1
By OS Family:
  windows: 5
  linux: 3
Total Applications: 150
Total Services: 45
```

## Future Enhancements

- SNMP support for network devices
- SSH-based remote auditing
- WMI remote queries for Windows devices
- Docker container inventory
- VM inventory (VMware, Hyper-V)
- Cloud resource inventory
- Automated license expiration tracking
- Warranty tracking
- Asset depreciation calculations
