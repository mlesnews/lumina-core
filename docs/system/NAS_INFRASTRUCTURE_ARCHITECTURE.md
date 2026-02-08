# NAS Infrastructure Architecture

**Generated:** 2026-01-09  
**Status:** Infrastructure Examination & Documentation

---

## 🏗️ Infrastructure Overview

Centralized infrastructure on NAS (DS1821PLUS) shared by LAPTOP and DESKTOP PCs:

- **N8N**: Workflow automation on NAS
- **DSM Container Manager**: Synology's Docker-compatible container system
- **Centralized Containers**: Shared containers accessible by both LAPTOP and DESKTOP
- **MCP Container**: Manages all centralized containers
- **Centralized Storage**: Shared storage volumes
- **DNS**: Primary/secondary with pfSense failover

---

## 📊 N8N Setup on NAS

### Configuration
- **Host**: `10.17.17.32` (NAS IP)
- **Port**: `5678` (default N8N port)
- **Endpoint**: `http://10.17.17.32:5678`
- **Status**: Configured (may be running in container)

### Integration Points
- **Email Hub**: `http://10.17.17.32:5678/webhook/email/hub/receive`
- **SYPHON Integration**: `scripts/python/n8n_syphon_integration.py`
- **Workflows**: Email processing, SMS processing, automation

### MARVIN Intelligence
- **Source**: `n8n_nas` (internal)
- **Task**: `marvin_n8n_intelligence`
- **Schedule**: Every 6 hours
- **Script**: `scripts/python/n8n_syphon_integration.py`

### N8N as Internal Source
N8N on NAS is classified as **internal** because:
- Anything coming through N8N on NAS is internal
- N8N workflows process internal communications (email, SMS)
- N8N is part of the internal automation infrastructure

---

## 🐳 DSM Container Manager (Lightweight Docker)

### Overview
Synology's Container Manager is Synology's version of Docker for NAS:
- Docker-compatible API
- Lightweight container runtime
- Web-based management UI
- Accessible via: `http://10.17.17.32:5000` (DSM) → Container Manager

### Container Architecture

#### Centralized Containers (Shared by LAPTOP & DESKTOP)
Containers deployed on NAS that are accessible by both LAPTOP and DESKTOP:

1. **MCP Container** (Management Container)
   - **Purpose**: Manages all centralized containers
   - **Container Name**: `mcp-server` or `mcp-container`
   - **Services**:
     - `manus-mcp-server` (port 8085)
     - `elevenlabs-mcp-server` (port 8086)
   - **Configuration**: `config/lumina_mcp_integration.json`
   - **Docker Compose**: `containerization/services/mcp-servers/docker-compose.yml`

2. **Shared Service Containers**
   - Containers that provide services to both LAPTOP and DESKTOP
   - Stored in: `/volume1/docker/` or `/volume1/@docker/`
   - Accessible via network from both machines

#### Container Storage
- **Docker Volumes**: `/volume1/docker/`
- **Container Data**: `/volume1/@docker/`
- **Shared Volumes**: `/volume1/shared/`
- **Mounted on Windows**: `M:\` and `N:\`

---

## 🔧 MCP Container Management

### MCP Container Purpose
The MCP (Model Context Protocol) container manages all centralized containers:

- **Container Name**: `mcp-server` or `mcp-container`
- **Location**: NAS (DS1821PLUS)
- **Management**: Orchestrates all centralized containers
- **Access**: Both LAPTOP and DESKTOP connect to MCP container on NAS

### MCP Services

#### 1. MANUS MCP Server
- **Container**: `manus-mcp-server`
- **Port**: 8085
- **Purpose**: MANUS Unified Control Interface via MCP
- **Capabilities**:
  - IDE Control
  - Workstation Control
  - Home Lab Infrastructure
  - Project Lumina Management
  - Automation Control
  - Data Management
  - Security Control

#### 2. ElevenLabs MCP Server
- **Container**: `elevenlabs-mcp-server`
- **Port**: 8086
- **Purpose**: ElevenLabs Text-to-Speech and Audio Processing
- **Capabilities**:
  - Text-to-Speech
  - Voice Cloning
  - Audio Processing
  - Transcription
  - Soundscape Generation

### MCP Configuration
- **Config File**: `config/lumina_mcp_integration.json`
- **Docker Compose**: `containerization/services/mcp-servers/docker-compose.yml`
- **Network**: `mcp-network`
- **Volumes**:
  - `manus-data`
  - `manus-logs`
  - `elevenlabs-output`
  - `elevenlabs-data`

---

## 💾 Centralized Storage

### NAS Storage Volumes
- **Primary Volume**: `/volume1/`
- **Docker Volume**: `/volume1/docker/`
- **Container Data**: `/volume1/@docker/`
- **Shared Volume**: `/volume1/shared/`

### Windows Mounts
- **M:\\**: NAS mount (LAPTOP & DESKTOP)
- **N:\\**: NAS mount (LAPTOP & DESKTOP)

### Container Shared Storage
Containers use shared volumes accessible by both LAPTOP and DESKTOP:
- Container data persists on NAS
- Both machines can access same container data
- Centralized configuration and state

---

## 🌐 DNS Architecture (Primary/Secondary with pfSense)

### DNS Cluster Configuration

#### Primary Cluster (NAS)
- **Node 1**: NAS Primary DNS (`10.17.17.32:53`)
- **Node 2**: NAS Primary DNS Backup (`10.17.17.33:53`)
- **Type**: Primary DNS server
- **Location**: NAS (DS1821PLUS)

#### Secondary Cluster (pfSense)
- **Node 1**: pfSense Secondary DNS (`10.17.17.1:53`)
- **Node 2**: pfSense Secondary DNS Backup (`10.17.17.2:53`)
- **Type**: Secondary DNS server (failover)
- **Location**: pfSense firewall device

### Failover Hierarchy
1. **Primary Cluster Node 1** (NAS) - Primary
2. **Primary Cluster Node 2** (NAS Backup) - Node-level failover
3. **Secondary Cluster Node 1** (pfSense) - Cluster-level failover
4. **Secondary Cluster Node 2** (pfSense Backup) - Cluster + node-level failover

### DNS Management
- **Manager**: `scripts/python/dns_cluster_manager.py`
- **Status Check**: `scripts/python/check_nas_dns_status.py`
- **pfSense Integration**: `scripts/python/check_pfsense_dns_overrides.py`

---

## 🔄 Container Sharing Architecture

### How Containers are Shared

1. **Deployment**: Containers deployed on NAS via Container Manager
2. **Storage**: Container data stored in `/volume1/docker/` (centralized)
3. **Network**: Containers accessible via NAS IP (`10.17.17.32`)
4. **Access**: Both LAPTOP and DESKTOP connect to containers on NAS
5. **Management**: MCP container orchestrates all centralized containers

### Centralized Container Benefits
- **Single Source of Truth**: One container instance shared by both machines
- **Consistent State**: Both machines see same container state
- **Resource Efficiency**: Containers run once on NAS, not duplicated
- **Centralized Management**: MCP container manages all containers

---

## 📋 Infrastructure Components Summary

| Component | Location | Purpose | Access |
|-----------|----------|---------|--------|
| **N8N** | NAS Container | Workflow automation | `http://10.17.17.32:5678` |
| **Container Manager** | NAS (DSM) | Docker management | DSM Web UI |
| **MCP Container** | NAS Container | Container orchestration | Port 8085/8086 |
| **Centralized Containers** | NAS Containers | Shared services | Network access |
| **Storage** | NAS Volumes | Centralized data | M:\ N:\ |
| **DNS Primary** | NAS | Primary DNS | `10.17.17.32:53` |
| **DNS Secondary** | pfSense | Failover DNS | `10.17.17.1:53` |

---

## 🔍 Examination Scripts

### Infrastructure Examination
```bash
python scripts/python/examine_nas_infrastructure.py
```

### Component-Specific Checks
```bash
# N8N only
python scripts/python/examine_nas_infrastructure.py --n8n-only

# Containers only
python scripts/python/examine_nas_infrastructure.py --containers-only

# DNS only
python scripts/python/examine_nas_infrastructure.py --dns-only

# Storage only
python scripts/python/examine_nas_infrastructure.py --storage-only
```

### N8N Discovery
```bash
python scripts/python/discover_nas_n8n.py
```

### Container Deployment
```bash
python scripts/python/deploy_lightweight_containers_to_nas.py check
python scripts/python/deploy_lightweight_containers_to_nas.py deploy-all
```

### DNS Status
```bash
python scripts/python/dns_cluster_manager.py --status
```

---

## 🎯 MARVIN Intelligence Integration

### N8N as Internal Source
MARVIN monitors N8N on NAS as an internal source:
- **Source ID**: `n8n_nas`
- **Type**: Internal
- **Category**: Automation
- **Task**: `marvin_n8n_intelligence`
- **Schedule**: Every 6 hours
- **Why Internal**: Anything coming through N8N on NAS is internal communication

### Intelligence Gathering
MARVIN extracts intelligence from:
- N8N workflow executions
- N8N webhook data
- N8N automation results
- N8N error logs

---

## 📝 Configuration Files

### N8N
- `scripts/python/n8n_syphon_integration.py` - N8N SYPHON integration
- `config/syphon_scheduled_sources.json` - N8N source configuration

### Containers
- `config/lumina_mcp_integration.json` - MCP container configuration
- `containerization/services/mcp-servers/docker-compose.yml` - MCP docker-compose
- `scripts/python/deploy_lightweight_containers_to_nas.py` - Container deployment

### DNS
- `scripts/python/dns_cluster_manager.py` - DNS cluster management
- `scripts/python/check_nas_dns_status.py` - DNS status check

### Storage
- `config/drive_mappings.json` - Drive mappings
- NAS mounts: `M:\` and `N:\`

---

## 🚀 Next Steps

1. **Verify N8N**: Check if N8N is running in a container
2. **List Containers**: Get full list of containers on NAS
3. **MCP Container**: Verify MCP container is running and managing containers
4. **DNS Failover**: Test DNS failover between NAS and pfSense
5. **Storage Access**: Verify both LAPTOP and DESKTOP can access shared storage

---

**Tags:** #NAS #N8N #CONTAINER #DSM #MCP #DNS #INFRASTRUCTURE #CENTRALIZED @JARVIS @LUMINA @MARVIN
