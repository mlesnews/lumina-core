# KAIJU Infrastructure Architecture

**Date**: 2026-01-01  
**Tag**: #KAIJU #ARCHITECTURE #INFRASTRUCTURE

---

## 🏗️ Infrastructure Overview

### KAIJU (10.17.17.11 / kaiju_no_8)

**Role**: Main Docker services host - Heavy workloads

**Services**:
- ✅ **Iron Legion Cluster** - 7-model Docker cluster
- ✅ **Ollama Services** - Main Ollama installation (Docker or native)
- ✅ **MCP Server** - Model Control Protocol server
- ✅ **Load Balancer** - Iron Legion router
- ✅ **All heavy Docker workloads**

**Access**:
- SSH: `ssh kaiju_no_8` or `ssh 10.17.17.11`
- RDP: `mstsc /v:10.17.17.11`
- Docker: All main containers run here

---

### NAS (10.17.17.32)

**Role**: Lightweight shared services - Minimal Docker

**Services**:
- ✅ **Minimal DSM Docker Package** - Synology's lightweight Docker
- ✅ **Centralized Shared Docker Container** - Lightweight services only
- ❌ **NOT main Docker services** - No Iron Legion, no heavy workloads

**Purpose**: 
- Shared storage
- Lightweight centralized services
- NOT the primary Docker host

---

## ⚠️ Common Confusion

**Problem**: AI/scripts confused NAS (10.17.17.32) with KAIJU (10.17.17.11)

**Result**: 
- Scripts checking wrong IP for Ollama
- Ollama installation on KAIJU may have been "stepped on" (overwritten/damaged)
- Incorrect assumptions about where services run

**Solution**: 
- All main Docker services = KAIJU (10.17.17.11)
- NAS (10.17.17.32) = Lightweight shared services only

---

## 🔍 Verification

### Check Ollama on KAIJU

```powershell
# SSH to KAIJU
ssh kaiju_no_8

# Check Ollama service
Get-Service -Name "*ollama*"

# Check Ollama process
Get-Process -Name "*ollama*"

# Check Ollama Docker container
docker ps -a --filter "name=ollama"

# Test Ollama API
curl http://localhost:11434/api/tags
```

### Check NAS Docker

```powershell
# NAS has minimal Docker - should NOT have Ollama/Iron Legion
# Only lightweight shared containers
```

---

## 🛠️ Fixing Ollama on KAIJU

If Ollama installation was "stepped on":

1. **Check current state**:
   ```powershell
   ssh kaiju_no_8 "Get-Service -Name '*ollama*'; Get-Process -Name '*ollama*'; docker ps -a --filter 'name=ollama'"
   ```

2. **Restore Ollama**:
   - If Docker: Restart container or redeploy
   - If Native: Reinstall Ollama service
   - Check Iron Legion cluster status

3. **Verify**:
   ```powershell
   ssh kaiju_no_8 "curl http://localhost:11434/api/tags"
   ```

---

## 📋 Correct IP Usage

| Service | IP | Purpose |
|---------|-----|---------|
| **KAIJU SSH/RDP** | 10.17.17.11 | Main Docker host access |
| **KAIJU Ollama** | 10.17.17.11:11434 | Main Ollama API |
| **NAS Shared** | 10.17.17.32 | Lightweight services only |
| **NAS Docker** | 10.17.17.32 | Minimal DSM Docker |

---

## 🎯 Script Updates Needed

All scripts should use:
- **KAIJU operations**: `10.17.17.11` (kaiju_no_8)
- **Ollama API**: `http://10.17.17.11:11434` (NOT NAS)
- **NAS operations**: Only for lightweight shared services

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: Architecture clarified - Ollama should be on KAIJU
