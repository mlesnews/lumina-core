# Lumina NAS Setup Prerequisites

## Overview

Before network drives can be mapped, the NAS (Network Attached Storage) must be properly configured with the required shares.

**NAS IP:** `10.17.17.32`

## Required NAS Shares

### Z: Drive - Backups Share
- **Share Name:** `backups`
- **Full Path:** `\\10.17.17.32\backups`
- **Purpose:** 
  - Backup storage
  - File downloads
  - Jupyter notebooks
  - Data storage

## NAS Setup Checklist

### 1. NAS Network Configuration
- [ ] NAS is powered on and connected to network
- [ ] NAS has static IP: `10.17.17.32`
- [ ] NAS is accessible from workstation (ping test)
- [ ] Firewall allows SMB/CIFS traffic (ports 445, 139)

### 2. Share Configuration
- [ ] Create `backups` share on NAS
- [ ] Set appropriate share permissions
- [ ] Configure user access permissions
- [ ] Enable SMB/CIFS protocol if needed

### 3. User Permissions
- [ ] NAS username: `backupadm` (already configured)
- [ ] NAS password stored in Azure Key Vault: `jarvis-lumina` → `nas-password`
- [ ] Grant read/write permissions to `backups` share for `backupadm`
- [ ] Test access from another machine if possible

**Note:** The password for `backupadm` must be stored in Azure Key Vault:
```powershell
az keyvault secret set --vault-name jarvis-lumina --name nas-password --value "PASSWORD"
```

### 4. Network Connectivity
- [ ] Workstation can ping NAS: `ping 10.17.17.32`
- [ ] Can browse to `\\10.17.17.32` in File Explorer
- [ ] Can see `backups` share listed

## Testing NAS Access

### Step 1: Ping Test
```powershell
Test-Connection 10.17.17.32
```

### Step 2: Browse NAS
```powershell
# Open File Explorer to NAS
explorer.exe "\\10.17.17.32"
```

### Step 3: Test Share Access
```powershell
# Try to access the share directly
Test-Path "\\10.17.17.32\backups"
```

### Step 4: Manual Mapping Test
```powershell
# Try manual mapping first
net use Z: \\10.17.17.32\backups /PERSISTENT:YES
```

## Common Issues

### NAS Not Reachable
**Symptoms:** Ping fails, cannot browse to NAS

**Solutions:**
1. Check NAS power and network cables
2. Verify NAS IP address in NAS settings
3. Check network switch/router configuration
4. Verify firewall settings

### Share Not Found
**Symptoms:** Can ping NAS but cannot see `backups` share

**Solutions:**
1. Log into NAS admin interface
2. Verify share exists and is enabled
3. Check share name spelling (case-sensitive on some NAS)
4. Ensure SMB/CIFS protocol is enabled

### Access Denied
**Symptoms:** Can see share but cannot access

**Solutions:**
1. Verify user credentials
2. Check share permissions in NAS settings
3. Verify user has read/write access
4. Try mapping with explicit credentials:
   ```powershell
   net use Z: \\10.17.17.32\backups /USER:username /PERSISTENT:YES
   ```

## After NAS Setup

Once the NAS shares are configured:

1. **Test manual mapping:**
   ```powershell
   net use Z: \\10.17.17.32\backups /PERSISTENT:YES
   ```

2. **Verify access:**
   ```powershell
   Test-Path Z:\
   dir Z:\
   ```

3. **Run Lumina mapping script:**
   ```powershell
   .\scripts\powershell\Map-LuminaNetworkDrives.ps1
   ```

4. **Add to startup (optional):**
   ```powershell
   .\scripts\powershell\Map-LuminaNetworkDrives.ps1 -AddToStartup
   ```

## NAS Configuration Reference

### Synology NAS (Common)
1. **Control Panel** → **Shared Folder** → Create `backups`
2. **Control Panel** → **User** → Set permissions
3. **Control Panel** → **File Services** → Enable SMB

### QNAP NAS
1. **Storage** → **Shared Folders** → Create `backups`
2. **Privilege Settings** → Configure access
3. **Network Services** → **Win/Mac/NFS** → Enable SMB

### Generic SMB/CIFS NAS
1. Create shared folder named `backups`
2. Configure user permissions
3. Enable SMB/CIFS protocol
4. Set static IP: `10.17.17.32`

## Related Documentation

- [Lumina Network Drives](./LUMINA_NETWORK_DRIVES.md) - Drive mapping configuration
- [Lumina Setup Complete](./LUMINA_SETUP_COMPLETE.md) - Overall setup guide

---

**Last Updated:** 2025-01-24  
**Status:** Prerequisites must be completed before network drive mapping

