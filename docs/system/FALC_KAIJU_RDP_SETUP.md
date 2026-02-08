# Enable Remote Desktop Between FALC and KAIJU

**Date**: 2026-01-01  
**Status**: ⚠️ **SETUP REQUIRED**  
**Tag**: #FALC #KAIJU #RDP #REMOTE-ACCESS

---

## 🎯 Goal

Enable Remote Desktop (RDP) access from **FALC** (laptop) to **KAIJU** (NAS) for easier configuration and management.

---

## 📋 Prerequisites

- **KAIJU IP**: `10.17.17.32`
- **KAIJU Computer Name**: `kaiju_no_8` (or similar)
- **Administrator access** on KAIJU
- **Network connectivity** between FALC and KAIJU

---

## 🚀 Setup Instructions

### Step 1: Enable RDP on KAIJU

**On KAIJU (10.17.17.32)**:

**Option A: Using Script (Recommended)**
```powershell
# Run as Administrator on KAIJU
.\scripts\powershell\enable_rdp_kaiju.ps1
```

**Option B: Manual Configuration**
```powershell
# Run as Administrator on KAIJU
# 1. Enable RDP
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 0

# 2. Configure firewall
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# 3. Allow RDP through firewall
New-NetFirewallRule -DisplayName "Remote Desktop" -Direction Inbound -LocalPort 3389 -Protocol TCP -Action Allow
```

**Option C: Via GUI**
1. Open **System Properties** (Win+R → `sysdm.cpl`)
2. Go to **Remote** tab
3. Select **"Enable Remote Desktop"**
4. Click **OK**

---

### Step 2: Verify RDP is Enabled

**From FALC (laptop)**, test RDP port:

```powershell
Test-NetConnection -ComputerName 10.17.17.32 -Port 3389
```

**Expected**: `TcpTestSucceeded: True`

---

### Step 3: Connect from FALC

**Option A: Remote Desktop Connection (mstsc)**
```powershell
# Open Remote Desktop
mstsc

# Or directly:
mstsc /v:10.17.17.32
```

**Option B: Command Line**
```powershell
# Start RDP session
mstsc /v:10.17.17.32 /admin
```

**Option C: Using Computer Name**
```powershell
mstsc /v:kaiju_no_8
```

---

## 🔐 Authentication

**Credentials**: Use your KAIJU user account credentials
- Username: (your KAIJU username)
- Password: (your KAIJU password)

**Note**: If you have sudoless root access, you may be able to use that account.

---

## 🔧 Advanced Configuration

### Enable RDP for Specific Users

```powershell
# Add user to Remote Desktop Users group
Add-LocalGroupMember -Group "Remote Desktop Users" -Member "username"
```

### Configure RDP Settings

```powershell
# Allow connections without Network Level Authentication (if needed)
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "UserAuthentication" -Value 0
```

### Change RDP Port (Optional)

```powershell
# Change RDP port from 3389 to custom port (e.g., 13389)
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" -Name "PortNumber" -Value 13389
```

---

## ✅ Verification Checklist

- [ ] RDP enabled on KAIJU
- [ ] Firewall allows RDP (port 3389)
- [ ] Can connect from FALC using `mstsc /v:10.17.17.32`
- [ ] Authentication works
- [ ] Can execute commands on KAIJU via RDP

---

## 🎯 Use Cases

Once RDP is enabled, you can:

1. **Configure Ollama models**:
   - RDP to KAIJU
   - Run `configure_kaiju_ollama_models.ps1`
   - Verify all 7 models appear

2. **Manage KAIJU**:
   - Access file system
   - Run scripts
   - Configure services
   - Monitor system

3. **Execute remote tasks**:
   - No need for SSH
   - Full GUI access
   - Easy file transfer

---

## 🔒 Security Notes

- **Use strong passwords** for RDP access
- **Consider VPN** if accessing over internet
- **Limit RDP access** to specific IPs if possible
- **Enable Network Level Authentication** (recommended)
- **Monitor RDP access** logs

---

## 📝 Scripts Created

- **Enable RDP**: `scripts/powershell/enable_rdp_kaiju.ps1`
- **Run on**: KAIJU (as Administrator)

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS @FALC @KAIJU
