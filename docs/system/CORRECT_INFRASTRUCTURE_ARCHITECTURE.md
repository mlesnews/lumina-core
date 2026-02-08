# Correct Infrastructure Architecture

**Date**: 2026-01-01  
**Tag**: #ARCHITECTURE #KAIJU #NAS #OLLAMA

---

## 🏗️ Correct Architecture (From Documentation Review)

### KAIJU (10.17.17.11 / kaiju_no_8)

**Role**: Main compute node - Desktop PC

**Services**:
- ✅ **Iron Legion Cluster** - 7-model Docker cluster
- ✅ **Ollama Services** - Main Ollama installation
- ✅ **MCP Server** - Docker container
- ✅ **All heavy Docker workloads**

**Ollama Endpoints** (from documentation):
- `http://kaiju_no_8:11437` - Primary endpoint (port 11437)
- `http://lesnewski.local:11437` - Domain name
- `http://localhost:11437` - Direct local access
- `http://10.17.17.11:11437` - IP address

**Note**: Documentation says port **11437** for KAIJU Ollama, NOT 11434

---

### NAS (10.17.17.32)

**Role**: Storage and lightweight shared services

**Services**:
- ✅ **Minimal DSM Docker Package** - Synology's lightweight Docker
- ✅ **Lightweight centralized shared Docker container** - For shared services only
- ❌ **NOT main Docker services** - No Iron Legion, no heavy workloads

**Purpose**: 
- Storage and file sharing
- Lightweight centralized services
- NOT the primary Docker host

---

## ⚠️ Current Configuration Issues

### Cursor Settings (`.cursor/settings.json`)

**Current (WRONG)**:
```json
{
  "name": "KAIJU",
  "apiBase": "http://10.17.17.32:11434"  // ❌ Wrong IP (NAS) and wrong port
}
```

**Should Be**:
```json
{
  "name": "KAIJU",
  "apiBase": "http://10.17.17.11:11437"  // ✅ Correct IP (KAIJU) and port
}
```

---

## 📋 Key Findings from Documentation

1. **KAIJU IRON LEGION** is a **LOCAL cluster** on KAIJU machine (10.17.17.11)
2. **Port 11437** is the Ollama API port on KAIJU (NOT 11434)
3. **Port 3000** may be a router/orchestrator (if configured)
4. **NAS (10.17.17.32)** should NOT have main Docker services
5. **Ollama installation on KAIJU** may have been "stepped on" (overwritten/damaged)

---

## 🔧 What Needs to Be Fixed

### 1. Cursor Configuration
- Update KAIJU endpoint from `10.17.17.32:11434` to `10.17.17.11:11437`
- Verify Ollama is accessible on KAIJU at port 11437

### 2. Scripts
- All scripts should use KAIJU IP: `10.17.17.11`
- Ollama API port: `11437` (not 11434)
- NAS IP: `10.17.17.32` (for storage/lightweight services only)

### 3. Ollama Installation on KAIJU
- Check if Ollama is running on KAIJU (port 11437)
- If not, restore/reinstall Ollama on KAIJU
- Verify Iron Legion cluster is running

---

## ✅ Correct IP and Port Usage

| Service | IP | Port | Purpose |
|---------|-----|------|---------|
| **KAIJU SSH/RDP** | 10.17.17.11 | 22/3389 | Main Docker host access |
| **KAIJU Ollama** | 10.17.17.11 | 11437 | Main Ollama API |
| **KAIJU Router** | 10.17.17.11 | 3000 | Load balancer (if configured) |
| **NAS Storage** | 10.17.17.32 | Various | Storage/lightweight services |
| **NAS Docker** | 10.17.17.32 | Various | Minimal DSM Docker only |

---

## 🎯 Next Steps

1. **Verify Ollama on KAIJU**:
   ```powershell
   ssh kaiju_no_8 "curl http://localhost:11437/api/tags"
   ```

2. **Update Cursor Config**:
   - Change KAIJU endpoint to `http://10.17.17.11:11437`

3. **Check Iron Legion Cluster**:
   ```powershell
   ssh kaiju_no_8 "docker ps | Select-String 'iron-legion'"
   ```

4. **Restore Ollama if needed**:
   - If Ollama installation was "stepped on", restore it on KAIJU

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS @ARCHITECT  
**Status**: Architecture clarified from documentation review
