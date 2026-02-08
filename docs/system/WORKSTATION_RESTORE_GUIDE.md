# Workstation Restoration Guide

**Date:** 2025-01-25  
**Backup Systems:** Backup for Business (B4B) + Synology HyperBackup  
**NAS Location:** `\\10.17.17.32\backups\MATT_Backups`

---

## Quick Start

### Option 1: Automatic Detection (Recommended)

Run the restore script without specifying a path - it will automatically search for backups:

```powershell
.\scripts\restore_from_backup.ps1
```

The script will:
1. Search for HyperBackup backups on NAS (`\\10.17.17.32`)
2. Search for B4B/File History backups
3. Let you select which backup to restore from

### Option 2: Specify Backup Path

If you know the exact backup location:

```powershell
# From HyperBackup (NAS)
.\scripts\restore_from_backup.ps1 -BackupPath "\\10.17.17.32\backups\MATT_Backups"

# From B4B/File History
.\scripts\restore_from_backup.ps1 -BackupPath "$env:USERPROFILE\AppData\Local\Microsoft\Windows\FileHistory\Data"

# From specific backup folder
.\scripts\restore_from_backup.ps1 -BackupPath "D:\Backups\2025-01-25"
```

### Option 3: Restore Specific Components

Restore only what you need:

```powershell
# Restore only project files
.\scripts\restore_from_backup.ps1 -BackupPath "\\10.17.17.32\backups\MATT_Backups" -RestoreMode "project"

# Restore only Cursor settings
.\scripts\restore_from_backup.ps1 -BackupPath "\\10.17.17.32\backups\MATT_Backups" -RestoreMode "cursor"

# Restore only configuration files
.\scripts\restore_from_backup.ps1 -BackupPath "\\10.17.17.32\backups\MATT_Backups" -RestoreMode "config"
```

---

## Backup System Details

### Synology HyperBackup

**Primary Location:** `\\10.17.17.32\backups\MATT_Backups`

**Characteristics:**
- May contain versioned backups (multiple folders with timestamps)
- Script automatically selects the latest version
- Accessible via network share or Synology Drive client

**Access Methods:**
1. **Network Share:** `\\10.17.17.32\backups\MATT_Backups`
2. **Synology File Station:** `http://10.17.17.32:5001`
3. **Synology Drive Client:** Syncs to local folder

### Backup for Business (B4B)

**Primary Location:** `$env:USERPROFILE\AppData\Local\Microsoft\Windows\FileHistory\`

**Characteristics:**
- Windows File History format
- Versioned by date/time
- May require administrator access

**Access Methods:**
1. **File History UI:** Windows Settings > Update & Security > Backup
2. **Direct Path:** `$env:USERPROFILE\AppData\Local\Microsoft\Windows\FileHistory\Data`

---

## What Gets Restored

### Project Files
- All project code and scripts
- Configuration files
- Documentation
- Data directories

**Location:** `D:\Dropbox\my_projects` (or specified `-ProjectRoot`)

### Python Environment
- Virtual environment (if portable)
- **Note:** Virtual environments are often not portable - script will offer to recreate

### Cursor IDE Settings
- User settings
- Workspace settings
- Extensions configuration
- Session history

**Location:** `$env:APPDATA\Cursor`

### PowerShell Profile
- Custom PowerShell profiles
- Module configurations

**Location:** `$env:USERPROFILE\Documents\PowerShell`

### Configuration Files
- Project configs in `config/`
- IDE settings
- Tool configurations

---

## Restoration Process

1. **Locate Backup** - Script searches common locations
2. **Detect Backup Type** - Identifies HyperBackup vs B4B
3. **Identify Restorable Items** - Scans for project files, settings, etc.
4. **Restore Files** - Copies files using robocopy (resumable)
5. **Complete Setup** - Runs workstation setup script
6. **Verify** - Checks that everything was restored correctly

---

## Post-Restoration Steps

After restoration completes:

1. **Recreate Python Virtual Environment** (if needed):
   ```powershell
   cd D:\Dropbox\my_projects
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r cfs-llc-env\requirements.txt
   ```

2. **Install Python Dependencies**:
   ```powershell
   pip install -r cfs-llc-env\requirements.txt
   ```

3. **Restart Cursor/VS Code** to load restored settings

4. **Verify Setup**:
   ```powershell
   python scripts\python\verify_coding_assistants_setup.py
   ```

5. **Check Ollama/Iron Legion** (if using):
   ```powershell
   # Verify Ollama is running
   curl http://localhost:11437/api/tags
   
   # Install missing models if needed
   ollama pull codellama:13b
   ollama pull llama3.2:11b
   ollama pull qwen2.5-coder:1.5b-base
   ```

---

## Troubleshooting

### Backup Not Found

**Problem:** Script can't find backup location

**Solutions:**
1. Manually specify path: `-BackupPath "\\10.17.17.32\backups\MATT_Backups"`
2. Map network drive first:
   ```powershell
   net use Z: \\10.17.17.32\backups
   .\scripts\restore_from_backup.ps1 -BackupPath "Z:\MATT_Backups"
   ```
3. Use Synology Drive client to sync backup locally

### Network Access Issues

**Problem:** Can't access NAS at `\\10.17.17.32`

**Solutions:**
1. Verify network connectivity: `ping 10.17.17.32`
2. Check credentials: May need to authenticate to NAS
3. Use Synology File Station web interface: `http://10.17.17.32:5001`
4. Download backup locally first, then restore from local path

### Python Virtual Environment Issues

**Problem:** Virtual environment doesn't work after restore

**Solution:** Recreate virtual environment (they're often not portable):
```powershell
# Remove old venv
Remove-Item -Recurse -Force venv

# Create new venv
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r cfs-llc-env\requirements.txt
```

### Cursor Settings Not Restored

**Problem:** Cursor settings don't appear after restore

**Solutions:**
1. Close Cursor completely before restoring
2. Manually restore from backup:
   ```powershell
   .\cfs-llc-env\restore-cursor-sessions.ps1
   ```
3. Check backup contains Cursor settings folder

---

## Manual Restoration

If automated restoration fails, you can manually restore:

### Project Files
```powershell
# From HyperBackup
robocopy "\\10.17.17.32\backups\MATT_Backups\my_projects" "D:\Dropbox\my_projects" /E /ZB
```

### Cursor Settings
```powershell
# Close Cursor first
Get-Process -Name "Cursor" -ErrorAction SilentlyContinue | Stop-Process -Force

# Restore settings
$backup = "\\10.17.17.32\backups\MATT_Backups\AppData\Roaming\Cursor"
$target = "$env:APPDATA\Cursor"
robocopy $backup $target /E /ZB
```

### PowerShell Profile
```powershell
$backup = "\\10.17.17.32\backups\MATT_Backups\Documents\PowerShell"
$target = "$env:USERPROFILE\Documents\PowerShell"
robocopy $backup $target /E /ZB
```

---

## Related Scripts

- **`scripts/restore_workstation_setup.ps1`** - Complete workstation setup (run after restore)
- **`scripts/restore_from_backup.ps1`** - This script (restore from backup)
- **`cfs-llc-env/restore-cursor-sessions.ps1`** - Restore Cursor sessions only
- **`scripts/python/verify_coding_assistants_setup.py`** - Verify setup after restore

---

## Backup Locations Reference

### HyperBackup (Primary)
- **NAS IP:** `10.17.17.32`
- **Share:** `\\10.17.17.32\backups\MATT_Backups`
- **Web Interface:** `http://10.17.17.32:5001`

### B4B/File History
- **Local:** `$env:USERPROFILE\AppData\Local\Microsoft\Windows\FileHistory\`
- **Data:** `$env:USERPROFILE\AppData\Local\Microsoft\Windows\FileHistory\Data`

### Synology Drive (if synced)
- **Local:** `$env:USERPROFILE\SynologyDrive\backups`

---

**Last Updated:** 2025-01-25  
**Maintained By:** Cedarbrook Financial Services LLC

