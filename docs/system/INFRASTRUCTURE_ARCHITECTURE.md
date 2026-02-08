# Infrastructure Architecture

**Date**: 2026-01-01  
**Tag**: #ARCHITECTURE #KAIJU #NAS #DOCKER

---

## 🏗️ System Architecture

### KAIJU (10.17.17.11 / kaiju_no_8)

**Role**: Main compute node for heavy workloads

**Services**:
- ✅ **Main Docker services** - Iron Legion cluster
- ✅ **Ollama services** - LLM inference
- ✅ **Heavy workloads** - All primary compute tasks
- ✅ **Iron Legion cluster** - 7-model Docker cluster
- ✅ **MCP Server** - Docker container

**Access**:
- SSH: `ssh kaiju_no_8` or `ssh 10.17.17.11`
- RDP: `mstsc /v:10.17.17.11`
- Docker: All main containers run here

---

### NAS (10.17.17.32)

**Role**: Lightweight shared services and storage

**Services**:
- ✅ **Minimal DSM Docker package** - Synology's Docker
- ✅ **Lightweight centralized shared Docker container** - For shared services
- ❌ **NOT main Docker services** - No heavy workloads here

**Purpose**:
- Storage and file sharing
- Lightweight shared services
- Minimal Docker for basic containers

---

## 🔄 Service Distribution

### What Runs Where

| Service | Location | IP | Notes |
|---------|----------|----|----|
| Iron Legion Cluster | KAIJU | 10.17.17.11 | Main Docker services |
| Ollama (main) | KAIJU | 10.17.17.11 | Native processes or Docker |
| MCP Server | KAIJU | 10.17.17.11 | Docker container |
| Heavy workloads | KAIJU | 10.17.17.11 | All primary compute |
| Lightweight Docker | NAS | 10.17.17.32 | Minimal shared services |
| Storage/File Share | NAS | 10.17.17.32 | Primary storage |

---

## 📡 Network Access

### KAIJU (10.17.17.11)
- **SSH**: `ssh kaiju_no_8` or `ssh 10.17.17.11`
- **RDP**: `mstsc /v:10.17.17.11`
- **Docker**: `ssh kaiju_no_8 "docker ps"`
- **Ollama API**: `http://10.17.17.11:11434` (if running on KAIJU)

### NAS (10.17.17.32)
- **Ollama API**: `http://10.17.17.32:11434` (if running on NAS)
- **File Share**: SMB/NFS protocols
- **DSM Web**: `http://10.17.17.32:5000` (typical)

---

## ⚠️ Common Confusion

### What NOT to Do

❌ **Don't assume NAS has main Docker services**
- NAS only has minimal Docker package
- Main services are on KAIJU

❌ **Don't confuse IPs**
- KAIJU = 10.17.17.11 (kaiju_no_8)
- NAS = 10.17.17.32

❌ **Don't run heavy workloads on NAS**
- NAS is for storage and lightweight services
- Heavy compute goes to KAIJU

---

## ✅ Best Practices

1. **Heavy workloads** → KAIJU (10.17.17.11)
2. **Docker services** → KAIJU (10.17.17.11)
3. **Storage/File share** → NAS (10.17.17.32)
4. **Lightweight shared services** → NAS (10.17.17.32)

---

## 🔧 Configuration

### Cursor Settings

Currently configured:
- **KAIJU endpoint**: `http://10.17.17.32:11434` (points to NAS)
- **Should be**: `http://10.17.17.11:11434` (if Ollama on KAIJU)

**Note**: Verify where Ollama API is actually accessible and update accordingly.

---

## 📝 Verification

### Check KAIJU Services
```powershell
# SSH to KAIJU
ssh kaiju_no_8 "docker ps"

# Check Ollama on KAIJU
ssh kaiju_no_8 "curl http://localhost:11434/api/tags"
```

### Check NAS Services
```powershell
# Check NAS Ollama (if exists)
Invoke-WebRequest -Uri "http://10.17.17.32:11434/api/tags"
```

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS @ARCHITECT
