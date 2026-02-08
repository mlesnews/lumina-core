# RDP Setup Instructions for KAIJU

**Purpose**: Enable Remote Desktop Protocol (RDP) on KAIJU for remote access from FALC  
**Tag**: #KAIJU #RDP #REMOTE-ACCESS

**Preferred**: For MANUS remote desktop, prefer **TightVNC** over RDP when possible. See [REMOTE_DESKTOP_TIGHTVNC.md](REMOTE_DESKTOP_TIGHTVNC.md). This doc remains for RDP fallback/setup.

---

## 🎯 Quick Fix

**Run this script directly on KAIJU** (via local access or existing RDP):

```powershell
D:\Dropbox\my_projects\.lumina\scripts\powershell\fix_rdp_kaiju.ps1
```

This script will:
1. ✅ Enable RDP in registry
2. ✅ Start RDP service
3. ✅ Configure firewall rules
4. ✅ Verify configuration

---

## 📋 Manual Steps (if script doesn't work)

### On KAIJU:

1. **Enable RDP in Registry**:
   ```powershell
   Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections" -Value 0
   ```

2. **Start RDP Service**:
   ```powershell
   Start-Service -Name "TermService"
   Set-Service -Name "TermService" -StartupType Automatic
   ```

3. **Enable Firewall Rules**:
   ```powershell
   Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
   ```

4. **Verify**:
   ```powershell
   Get-Service -Name "TermService"
   Get-NetFirewallRule -DisplayGroup "Remote Desktop" | Where-Object { $_.Enabled -eq $true }
   ```

---

## 🔌 Connect from FALC

Once RDP is enabled on KAIJU:

```powershell
# Via command line
mstsc /v:10.17.17.32

# Or use Remote Desktop Connection app
# Computer: 10.17.17.32
# Username: [your KAIJU username]
```

---

## 🔍 Troubleshooting

### RDP Port Not Accessible

**From FALC**, test connection:
```powershell
Test-NetConnection -ComputerName 10.17.17.32 -Port 3389
```

**Possible issues**:
1. **Firewall on FALC**: Windows Firewall may be blocking outbound RDP
2. **Firewall on KAIJU**: RDP firewall rules not enabled
3. **Network**: Router/firewall blocking port 3389
4. **Service not running**: TermService not started on KAIJU

### Check RDP Service

**On KAIJU**:
```powershell
# Check service
Get-Service -Name "TermService"

# Check registry
(Get-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" -Name "fDenyTSConnections").fDenyTSConnections
# Should be 0 (enabled)

# Check firewall
Get-NetFirewallRule -DisplayGroup "Remote Desktop" | Where-Object { $_.Enabled -eq $true }
```

---

## ✅ Verification Checklist

- [ ] RDP registry setting: `fDenyTSConnections = 0`
- [ ] TermService status: `Running`
- [ ] TermService startup: `Automatic`
- [ ] Firewall rules: At least 1 rule enabled
- [ ] Port 3389: Accessible from FALC
- [ ] Can connect: `mstsc /v:10.17.17.32`

---

## 🚀 Quick Start

**If you have local access to KAIJU:**
```powershell
D:\Dropbox\my_projects\.lumina\scripts\powershell\fix_rdp_kaiju.ps1
```

**Then from FALC:**
```powershell
mstsc /v:10.17.17.32
```

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS
