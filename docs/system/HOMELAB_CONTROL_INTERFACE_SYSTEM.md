# Homelab Control Interface System

**Date**: 2026-01-28
**Status**: ✅ **COMPLETE**
**Purpose**: Complete control map of all commands, APIs, and CLIs for homelab control

---

## Executive Summary

A comprehensive control interface discovery and mapping system that discovers, catalogs, and provides unified access to **every command, API endpoint, and CLI tool** available for controlling your homelab infrastructure.

**Discovery Results**:
- **10 Devices** mapped
- **33 Commands** discovered
- **85 API Endpoints** discovered
- **32 CLI Tools** discovered

---

## System Components

### 1. ✅ Control Interface Discovery
**File**: `scripts/python/homelab_control_interface_discovery.py`

**Discovers**:
- **Commands**: PowerShell, CMD, Linux commands, DSM commands
- **APIs**: Ollama API, ULTRON Router API, Synology DSM API
- **CLIs**: curl, git, docker, kubectl, terraform, ansible, etc.

**Platforms Supported**:
- Windows (PowerShell, CMD)
- Linux (systemctl, journalctl, etc.)
- Synology DSM (synoservice, synopkg, etc.)

---

### 2. ✅ Control Interface Explorer
**File**: `scripts/python/homelab_control_explorer.py`

**Capabilities**:
- List all devices and their control interfaces
- Explore device control capabilities
- Search control interfaces
- Execute commands
- Test API endpoints

---

### 3. ✅ Unified Control Interface
**File**: `scripts/python/homelab_unified_control.py`

**Features**:
- Single entry point for all control operations
- Automatic method selection (API → Command → CLI)
- Command execution
- API testing
- Control guide generation

---

### 4. ✅ Integrated Audit System
**File**: `scripts/python/homelab_audit_with_control.py`

**Combines**:
- Standard audit (features, services, etc.)
- Control interface discovery
- Unified output format

---

### 5. ✅ MariaDB Schema Extension
**File**: `scripts/python/extend_audit_mariadb_schema.py`

**New Tables**:
- `device_commands` - All commands per device
- `device_api_endpoints` - All API endpoints
- `device_cli_tools` - All CLI tools
- `command_execution_log` - Command execution history
- `api_test_log` - API test history
- `control_interface_registry` - Control interface registry

---

## Usage Guide

### Discover Control Interfaces

```bash
# Discover control interfaces from audit
python scripts/python/homelab_control_interface_discovery.py

# Run integrated audit (audit + control discovery)
python scripts/python/homelab_audit_with_control.py
```

### Explore Control Interfaces

```bash
# List all devices
python scripts/python/homelab_control_explorer.py --list-devices

# Explore specific device
python scripts/python/homelab_control_explorer.py --explore local_Millennium-Falcon

# Search control interfaces
python scripts/python/homelab_control_explorer.py --search "ollama"

# Generate report
python scripts/python/homelab_control_explorer.py --report
```

### Execute Commands

```bash
# Execute command
python scripts/python/homelab_unified_control.py \
  --execute "local_Millennium-Falcon:Get-Process"

# Call API
python scripts/python/homelab_unified_control.py \
  --api "local_Millennium-Falcon:List Models"

# Unified control (auto-selects best method)
python scripts/python/homelab_unified_control.py \
  --control "local_Millennium-Falcon:Get-Process"
```

### Generate Control Guide

```bash
# Generate comprehensive control guide
python scripts/python/homelab_unified_control.py --guide
```

---

## Control Interface Categories

### Commands

**Windows**:
- PowerShell: Get-Process, Get-Service, Get-NetAdapter, Get-Disk, etc.
- CMD: ipconfig, systeminfo, tasklist, netstat, sc, wmic

**Linux**:
- System: ps, systemctl, ip, df, lsblk, ss, netstat, journalctl
- Containers: docker, kubectl

**Synology DSM**:
- synoservice, synopkg, synoshare, synouser, synogroup, synovfs

### API Endpoints

**Ollama API** (`/api/*`):
- `/api/tags` - List models
- `/api/chat` - Chat completion
- `/api/generate` - Generate text
- `/api/pull` - Pull model
- `/api/show` - Show model info

**ULTRON Router API** (`:8080`):
- `/health` - Health check
- `/v1/chat/completions` - Chat via router
- `/api/status` - Cluster status

**Synology DSM API** (`:5000/webapi/*`):
- `/auth.cgi` - Authentication
- `/query.cgi` - Package/service/system queries

### CLI Tools

**Common**:
- curl, wget, ssh, scp, rsync, git

**Containers**:
- docker, kubectl

**Infrastructure**:
- terraform, ansible

**Platform-Specific**:
- Windows: powershell, cmd, wsl
- Linux: systemctl, journalctl
- DSM: synoservice, synopkg

---

## Control Map Structure

```json
{
  "map_id": "control_map_20260128_211754",
  "total_interfaces": 10,
  "total_commands": 33,
  "total_api_endpoints": 85,
  "total_cli_tools": 32,
  "interfaces": [
    {
      "interface_id": "device_control",
      "device_id": "device_id",
      "name": "Device Control Interface",
      "control_type": "mixed",
      "commands": [...],
      "api_endpoints": [...],
      "cli_tools": [...]
    }
  ]
}
```

---

## MariaDB Integration

### Schema Tables

**device_commands**:
- command_id, device_id, name, command, parameters, examples, platform, category

**device_api_endpoints**:
- endpoint_id, device_id, name, url, method, parameters, authentication, examples

**device_cli_tools**:
- cli_id, device_id, name, executable, version, available

**command_execution_log**:
- execution_id, command_id, executed_at, success, stdout, stderr, execution_time_ms

**api_test_log**:
- test_id, endpoint_id, tested_at, success, status_code, response_time_ms

---

## Example Usage

### List All Control Interfaces

```bash
python scripts/python/homelab_unified_control.py --list
```

### Execute PowerShell Command

```bash
python scripts/python/homelab_unified_control.py \
  --execute "local_Millennium-Falcon:Get-Process" \
  --json
```

### Test Ollama API

```bash
python scripts/python/homelab_unified_control.py \
  --api "local_Millennium-Falcon:List Models"
```

### Generate Complete Control Guide

```bash
python scripts/python/homelab_unified_control.py --guide > control_guide.txt
```

---

## Integration with Audit System

The control interface discovery is integrated with the audit system:

1. **Run Audit**: Discovers devices and features
2. **Discover Control**: Maps commands, APIs, CLIs for each device
3. **Combine**: Creates unified audit with control interfaces
4. **Import**: Imports to MariaDB@NAS-DSM
5. **Export**: Exports to Holocron format

---

## Files Created

### Control Maps
- `data/homelab_control/control_map_20260128_211754.json` - Control interface map

### Combined Audits
- `data/homelab_audit/audit_with_control_audit_20260128_211845.json` - Audit + control

### Scripts
- `scripts/python/homelab_control_interface_discovery.py` - Discovery system
- `scripts/python/homelab_control_explorer.py` - Explorer interface
- `scripts/python/homelab_unified_control.py` - Unified control
- `scripts/python/homelab_audit_with_control.py` - Integrated audit
- `scripts/python/extend_audit_mariadb_schema.py` - Schema extension
- `scripts/python/import_control_interfaces_mariadb.py` - MariaDB import

---

## Next Steps

### Immediate
1. ✅ Control interfaces discovered
2. ✅ Control map created
3. ✅ Explorer system built
4. ✅ Unified control interface created

### Short-term (Requires MariaDB Credentials)
1. ⏳ Extend database schema
2. ⏳ Import control interfaces
3. ⏳ Generate reports from database

### Long-term
1. ⏳ Web dashboard for control interface
2. ⏳ Command scheduling system
3. ⏳ API monitoring and alerting
4. ⏳ Automated testing of APIs

---

## Summary

**Complete control map** of your homelab:
- ✅ **33 Commands** - PowerShell, CMD, Linux, DSM
- ✅ **85 API Endpoints** - Ollama, ULTRON Router, DSM
- ✅ **32 CLI Tools** - curl, git, docker, kubectl, etc.

**Unified control interface** for:
- ✅ Command execution
- ✅ API testing
- ✅ CLI tool access
- ✅ Complete control guide

**Ready for**:
- ✅ MariaDB import (schema ready)
- ✅ Holocron export
- ✅ Continuous discovery and mapping

---

**You now have complete control over your entire homelab infrastructure!**

---

**Tags**: `#HOMELAB` `#CONTROL` `#COMMANDS` `#API` `#CLI` `#MAP` `@JARVIS` `@LUMINA`
