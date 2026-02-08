# Lumina Network Drives Configuration

## Overview

Network drives are configured to be permanently mapped and automatically reconnect on login.

**Source of Truth:** `config/lumina_network_drives.json`

**⚠️ IMPORTANT:** Before mapping network drives, ensure the NAS shares are configured. See [LUMINA_NAS_SETUP_PREREQUISITES.md](./LUMINA_NAS_SETUP_PREREQUISITES.md) for setup instructions.

## Current Network Drives (intended letters)

| Letter | UNC | Purpose |
|--------|-----|---------|
| **H:** | `\\10.17.17.32\homes` | NAS **homes** (all user home dirs). Use H for **homes**; Synology "home" is the per-user view into homes. |
| **P:** | `\\10.17.17.32\photos` | NAS **Pictures** (edit UNC to `photo` or `pictures` if your share name differs). |
| **V:** | `\\10.17.17.32\video` | NAS **Video**. |
| **G:** | `\\10.17.17.32\git` | NAS Git (DSM Git Server – local Git cloud). |
| **B:** | `\\10.17.17.32\backups` | NAS Backups. |
| **L:** | `\\10.17.17.32\backups\logs` | NAS **Logs** (L for Logs); logs subfolder on backups share; DSM **Log Center**. |

### L: Drive - NAS Logs (DSM Log Center)
- **UNC Path:** `\\10.17.17.32\backups\logs` (subfolder on backups share; created by automation if missing).
- **Description:** Logs (L: for Logs). Use with **Synology Log Center** (DSM Package Center: "Log Center") for centralized log collection and storage.
- **Persistent:** Yes
- **Auto-reconnect:** Yes
- **Usage:**
  - Centralized log storage and retrieval
  - DSM Log Center: gather and display log messages from network devices; flexible search

### B: Drive - NAS Backups
- **UNC Path:** `\\10.17.17.32\backups`
- **Description:** NAS Backups (B: for Backups)
- **Persistent:** Yes
- **Auto-reconnect:** Yes
- **Usage:**
  - Backup storage
  - File downloads
  - Jupyter notebooks
  - Data storage

## Mapping Script

**Script:** `scripts/powershell/Map-LuminaNetworkDrives.ps1`

This script:
- Maps all network drives from SSoT configuration
- Makes mappings persistent (survive reboots)
- Verifies connections
- Handles credentials automatically
- Can be added to Windows Startup

### Usage

**Map all drives:**
```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1
```

**Add to Windows Startup (auto-map on login):**
```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -AddToStartup
```

**Remove from startup:**
```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -RemoveFromStartup
```

**Verify existing mappings:**
```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -VerifyOnly
```

**If you see error 1219 (multiple user names):** Windows allows only one username per client to the same server. Another process (e.g. Explorer, or a previous session) may already be connected to the NAS under a different account. Try:
1. Close any Explorer windows showing NAS paths (`\\10.17.17.32\...`).
2. Run the script from a **new** PowerShell window (no other NAS use in that session).
3. Or use **-DisconnectAllFirst** to remove all of your network drives first, then map only NAS: `.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -Force -DisconnectAllFirst`.
4. If it still fails, reboot and run the script before opening any NAS shares in Explorer.

## Configuration

### Adding New Network Drives

Edit `config/lumina_network_drives.json`:

```json
{
  "network_drives": [
    {
      "drive_letter": "Z",
      "unc_path": "\\\\10.17.17.32\\backups",
      "description": "NAS Backups",
      "persistent": true,
      "reconnect_on_startup": true,
      "verify_on_mapping": true,
      "credentials": {
        "required": true,
        "source": "user_prompt"
      }
    },
    {
      "drive_letter": "Y",
      "unc_path": "\\\\server\\share",
      "description": "New Share",
      "persistent": true,
      "reconnect_on_startup": true,
      "verify_on_mapping": true,
      "credentials": {
        "required": false,
        "source": "cached"
      }
    }
  ]
}
```

### Drive Letter Availability

Common available drive letters (in order of preference):
- Z, Y, X, W, V, U, T, S, R, Q, P, O, N, M

Avoid: A, B (floppy), C (system), D (data drive in this setup)

## Persistent Mappings

### How It Works

1. **Persistent Flag:** Uses `/PERSISTENT:YES` with `net use`
2. **Windows Credential Manager:** Stores credentials securely
3. **Startup Integration:** Script can be added to Windows Startup folder
4. **Auto-reconnect:** Windows automatically reconnects persistent mappings on login

### Verification

**Check current mappings:**
```powershell
net use
```

**Check specific drive:**
```powershell
Get-PSDrive -Name Z
```

**Test accessibility:**
```powershell
Test-Path Z:\
```

## Troubleshooting

### NAS Not Set Up

**If you see "Server not reachable" or mapping hangs:**

1. **First, set up NAS shares:**
   - See [LUMINA_NAS_SETUP_PREREQUISITES.md](./LUMINA_NAS_SETUP_PREREQUISITES.md)
   - Configure `backups` share on NAS at `10.17.17.32`
   - Ensure share is accessible before running mapping script

2. **Verify NAS is reachable:**
   ```powershell
   Test-Connection 10.17.17.32
   ```

3. **Test share exists:**
   ```powershell
   # Browse to NAS
   explorer.exe "\\10.17.17.32"
   # Verify backups share is visible
   ```

### Drive Not Mapping

1. **Check network connectivity:**
   ```powershell
   Test-Connection 10.17.17.32
   ```

2. **Check credentials:**
   - Credentials may need to be re-entered
   - Check Windows Credential Manager

3. **Check permissions:**
   - Ensure user has access to the network share
   - Verify share permissions on server

### Drive Shows as "Unavailable"

1. **Remap the drive:**
   ```powershell
   net use Z: /DELETE
   .\scripts\powershell\Map-LuminaNetworkDrives.ps1
   ```

2. **Check server availability:**
   - Verify NAS/server is online
   - Check network connection

### Credentials Not Saved

1. **Map with credentials explicitly:**
   ```powershell
   net use Z: \\10.17.17.32\backups /PERSISTENT:YES /USER:username
   ```

2. **Check Windows Credential Manager:**
   - Open "Credential Manager" in Control Panel
   - Check for stored network credentials

## Startup Integration

### Adding to Startup

The script can be added to Windows Startup folder to automatically map drives on login:

```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -AddToStartup
```

This creates a shortcut in:
- `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`

### Removing from Startup

```powershell
.\scripts\powershell\Map-LuminaNetworkDrives.ps1 -RemoveFromStartup
```

## Logging

All mapping operations are logged to:
- `%TEMP%\lumina_network_drives_YYYYMMDD.log`

Log includes:
- Timestamp
- Operation (mapping, verification, etc.)
- Success/failure status
- Error messages

## Related Files

- `config/lumina_network_drives.json` - SSoT configuration
- `scripts/powershell/Map-LuminaNetworkDrives.ps1` - Mapping script
- `docs/system/LUMINA_NETWORK_DRIVES.md` - This documentation

## Best Practices

1. **Use persistent mappings:** Always set `persistent: true`
2. **Verify connections:** Enable `verify_on_mapping: true`
3. **Add to startup:** Use `-AddToStartup` for automatic mapping
4. **Monitor logs:** Check log files for mapping issues
5. **Test connectivity:** Use `-VerifyOnly` to check drive status

---

**Last Updated:** 2025-01-24
**Maintained By:** Lumina Project Team

