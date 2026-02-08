# Docker Migration - Manual Instructions

**Date**: 2026-01-14  
**Status**: 📋 **MANUAL ACTION REQUIRED**  
**Tags**: `#DOIT` `#NAS` `#MIGRATION` `#DOCKER` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Objective

Free 133.8 GB by moving Docker data to NAS and deleting local source.

**Current Status**:
- Docker Desktop: RUNNING (PID: 3760)
- Local Docker: 133.8 GB (locked by running process)
- Docker on NAS: 0.2 GB (copy incomplete or failed)

---

## ⚠️ Important Note

**Docker copy to NAS appears incomplete** (0.2 GB on NAS vs 133.8 GB local).

**Options**:
1. **Re-copy Docker** to NAS (after stopping Docker Desktop)
2. **Or** configure Docker to use NAS directly (no copy needed)

---

## 📋 Manual Steps Required

### Step 1: Stop Docker Desktop

**Method 1: Via System Tray**
1. Right-click Docker Desktop icon in system tray
2. Click "Quit Docker Desktop"
3. Wait for Docker to fully stop

**Method 2: Via Task Manager**
1. Press `Ctrl+Shift+Esc`
2. Find "Docker Desktop" process
3. Right-click → End Task

**Method 3: Via PowerShell** (after user approval)
```powershell
Stop-Process -Id 3760 -Force
```

**Verify**: Check Docker Desktop is stopped
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*docker*"}
# Should return nothing
```

---

### Step 2: Copy Docker to NAS (If Needed)

**If Docker on NAS is incomplete** (0.2 GB vs 133.8 GB):

```powershell
$dockerLocal = "C:\Users\mlesn\AppData\Local\Docker"
$dockerNAS = "\\10.17.17.32\homes\mlesn\docker"

# Copy to NAS
robocopy $dockerLocal $dockerNAS /E /COPYALL /R:3 /W:5 /MT:4
```

**Verify copy completed**:
```powershell
$nasSize = (Get-ChildItem $dockerNAS -Recurse | Measure-Object -Property Length -Sum).Sum / 1GB
Write-Host "Docker on NAS: $([math]::Round($nasSize, 1)) GB"
# Should be ~133.8 GB
```

---

### Step 3: Delete Local Docker Directory

**After verifying NAS copy is complete**:

```powershell
$dockerLocal = "C:\Users\mlesn\AppData\Local\Docker"

# Verify Docker Desktop is stopped
$dockerProcess = Get-Process | Where-Object {$_.ProcessName -like "*docker*"}
if ($dockerProcess) {
    Write-Host "⚠️  Docker Desktop still running - stop it first!"
} else {
    # Delete local directory
    Remove-Item $dockerLocal -Recurse -Force
    Write-Host "✅ Local Docker directory deleted"
}
```

---

### Step 4: Configure Docker Desktop to Use NAS

**Option A: Docker Desktop Settings**

1. Open Docker Desktop
2. Go to Settings → Resources → Advanced
3. Set "Disk image location" to: `\\10.17.17.32\homes\mlesn\docker`
4. Click "Apply & Restart"

**Option B: Docker Configuration File**

Edit Docker Desktop configuration to use NAS path.

**Option C: Symbolic Link** (if Docker requires local path)

```powershell
# Create symlink from local to NAS
New-Item -ItemType SymbolicLink -Path "C:\Users\mlesn\AppData\Local\Docker" -Target "\\10.17.17.32\homes\mlesn\docker"
```

---

### Step 5: Restart Docker Desktop

1. Start Docker Desktop
2. Verify it's using NAS path
3. Test Docker functionality

---

## 📊 Expected Results

### Before

- **Local Docker**: 133.8 GB
- **Disk Usage**: 98.6%
- **Free Space**: 52.8 GB

### After

- **Local Docker**: 0 GB (or symlink)
- **Docker on NAS**: 133.8 GB
- **Disk Usage**: ~95% (after Docker freed)
- **Free Space**: ~186 GB

**Space Freed**: 133.8 GB

---

## 🔧 Alternative: Direct NAS Configuration

**If re-copying is not desired**:

1. Stop Docker Desktop
2. Delete local Docker directory
3. Configure Docker Desktop to use NAS directly
4. Docker will create new data on NAS
5. Re-pull images/containers as needed

**Pros**: Faster, no copy needed  
**Cons**: Need to re-download images/containers

---

## ⚠️ Warnings

1. **Backup**: Ensure Docker data is backed up before deletion
2. **Verify NAS Copy**: Check NAS copy is complete before deleting local
3. **Docker Must Be Stopped**: Cannot delete while Docker Desktop is running
4. **Test After Migration**: Verify Docker works with NAS path

---

## 📝 Verification Checklist

- [ ] Docker Desktop stopped
- [ ] Docker data copied to NAS (or configured to use NAS directly)
- [ ] NAS copy verified (if copied)
- [ ] Local Docker directory deleted
- [ ] Docker Desktop configured to use NAS
- [ ] Docker Desktop restarted
- [ ] Docker functionality tested
- [ ] Disk space freed verified

---

**Status**: 📋 **MANUAL ACTION REQUIRED**  
**Priority**: 🔴 **HIGH** - Will free 133.8 GB  
**Blocked By**: Docker Desktop running (must be stopped by user)  
**Tags**: `#DOIT` `#NAS` `#MIGRATION` `#DOCKER` `@LUMINA` `@JARVIS` `#PEAK`
