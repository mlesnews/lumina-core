# RDP & Docker + SSH Status

**Date**: 2026-01-01  
**Tag**: #KAIJU #RDP #SSH #DOCKER

---

## 📊 Current Status

### ❌ RDP: NOT FIXED
- **Port 3389**: Not accessible from FALC
- **Status**: Needs fix script run on KAIJU
- **Fix Script**: `scripts/powershell/fix_rdp_kaiju.ps1` or `fix_rdp_docker.ps1`

### ⚠️ SSH: Port Open, Auth Required
- **Port 22**: Accessible
- **Authentication**: Permission denied (needs password/key)
- **Status**: Not configured for passwordless access

### ❌ Docker + SSH: NOT FIXED
- **Status**: Requires SSH authentication
- **Error**: `Permission denied (publickey,password)`
- **Fix**: Configure SSH authentication or use RDP

---

## 🔧 What's Been Created

### Scripts Created (Ready to Use)

1. **`fix_rdp_kaiju.ps1`** - Full RDP fix
   - Enables RDP registry
   - Starts RDP service
   - Configures firewall
   - Verifies configuration

2. **`fix_rdp_docker.ps1`** - RDP fix (Docker context)
   - Same as above, optimized for Docker environment

3. **`check_kaiju_docker.ps1`** - Status check via Docker
   - Checks Docker containers
   - Lists Ollama models
   - Checks environment variables
   - Verifies RDP status

4. **`check_kaiju_simple.ps1`** - Simple status check
   - Quick verification script

---

## ✅ What Needs to Be Done

### 1. Fix RDP (Run on KAIJU)

**Option A: Via Local Access**
```powershell
# On KAIJU (local access)
D:\Dropbox\my_projects\.lumina\scripts\powershell\fix_rdp_kaiju.ps1
```

**Option B: Via Existing RDP Connection**
```powershell
# If you already have RDP access
D:\Dropbox\my_projects\.lumina\scripts\powershell\fix_rdp_kaiju.ps1
```

**After running**, verify from FALC:
```powershell
Test-NetConnection -ComputerName 10.17.17.32 -Port 3389
mstsc /v:10.17.17.32
```

### 2. Fix SSH Authentication (Optional)

**Option A: SSH Key Authentication**
```powershell
# On FALC - Generate key pair
ssh-keygen -t rsa -b 4096

# Copy public key to KAIJU (requires password once)
ssh-copy-id mlesn@10.17.17.32
```

**Option B: Use SSH with Password**
```powershell
# Interactive (will prompt for password)
ssh mlesn@10.17.17.32 "docker ps"
```

**Option C: Configure SSH Config**
```powershell
# Create/edit ~/.ssh/config
Host kaiju
    HostName 10.17.17.32
    User mlesn
    IdentityFile ~/.ssh/id_rsa
```

### 3. Test Docker + SSH (After SSH Fix)

```powershell
# Once SSH auth is working
ssh 10.17.17.32 "docker ps"
ssh 10.17.17.32 "docker exec ollama ollama list"
```

---

## 🎯 Recommended Order

1. **Fix RDP first** (easiest, most reliable)
   - Run fix script on KAIJU
   - Verify connection from FALC
   - Use RDP for all KAIJU management

2. **Then fix SSH** (optional, for automation)
   - Set up SSH keys
   - Test Docker commands via SSH
   - Use for automated scripts

---

## 📝 Verification Checklist

### RDP
- [ ] Run `fix_rdp_kaiju.ps1` on KAIJU
- [ ] Test port 3389 from FALC: `Test-NetConnection -ComputerName 10.17.17.32 -Port 3389`
- [ ] Connect via RDP: `mstsc /v:10.17.17.32`
- [ ] Verify RDP service running on KAIJU

### SSH
- [ ] Port 22 accessible: `Test-NetConnection -ComputerName 10.17.17.32 -Port 22`
- [ ] SSH authentication configured (key or password)
- [ ] Test SSH connection: `ssh 10.17.17.32 "echo 'test'"`
- [ ] Test Docker via SSH: `ssh 10.17.17.32 "docker ps"`

### Docker + SSH
- [ ] SSH working
- [ ] Docker accessible via SSH: `ssh 10.17.17.32 "docker ps"`
- [ ] Ollama accessible via SSH: `ssh 10.17.17.32 "docker exec ollama ollama list"`

---

## 🚀 Quick Start

**To fix RDP right now:**

1. Access KAIJU (local or existing RDP)
2. Run: `D:\Dropbox\my_projects\.lumina\scripts\powershell\fix_rdp_kaiju.ps1`
3. Verify from FALC: `mstsc /v:10.17.17.32`

**To fix SSH (optional):**

1. Generate SSH key on FALC: `ssh-keygen -t rsa -b 4096`
2. Copy to KAIJU: `ssh-copy-id mlesn@10.17.17.32`
3. Test: `ssh 10.17.17.32 "docker ps"`

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: RDP and SSH need to be fixed on KAIJU
