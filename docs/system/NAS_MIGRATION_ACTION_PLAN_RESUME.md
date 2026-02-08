# NAS Migration - Action Plan (Resume)

**Date**: 2026-01-14  
**Status**: 🔄 **EXECUTING - CRITICAL DISK USAGE 98.6%**  
**Tags**: `#DOIT` `#NAS` `#MIGRATION` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🚨 Critical Status

- **Disk Usage**: 98.6% (3,642.2 GB used, 52.8 GB free)
- **Target**: < 80% (< 2,956 GB used)
- **Need to Free**: ~686 GB
- **Status**: 🔴 **CRITICAL** - Immediate action required

---

## 📊 Current Findings

### AppData Breakdown (222.8 GB total)

- **AppData\Local**: 198.4 GB 🔥 (largest)
- **AppData\Roaming**: 24.2 GB
- **AppData\LocalLow**: 0.2 GB

### Docker Status

- **Docker Desktop**: RUNNING (PID: 3760)
- **Local Docker**: EXISTS (locked by running process)
- **Docker on NAS**: EXISTS (copied, ready)
- **Action**: Stop Docker Desktop to free 133.8 GB

### Folder Redirection Status

- **Documents**: ⚠️ Regular folder (not redirected)
- **Downloads**: ⚠️ Regular folder (not redirected)
- **Videos**: ⚠️ Regular folder (not redirected)
- **Music**: ⚠️ Regular folder (not redirected)
- **Pictures**: ❌ Not found

**Status**: Files may be moved, but symlinks not created

### NAS Connectivity

- **NAS**: ✅ Accessible (`\\10.17.17.32\homes\mlesn`)

---

## 🎯 Immediate Action Plan

### Priority 1: Analyze AppData\Local (198.4 GB)

**Action**: Identify top 10 largest directories in AppData\Local

**Expected findings**:
- Docker (133.8 GB)
- Microsoft applications
- Caches
- Other application data

### Priority 2: Stop Docker Desktop & Free Space

**Action**: 
1. Stop Docker Desktop (PID: 3760)
2. Verify Docker data is on NAS
3. Delete local Docker directory
4. Configure Docker to use NAS path
5. Restart Docker Desktop

**Impact**: Will free 133.8 GB

### Priority 3: Complete Folder Redirection

**Action**:
1. Verify files are on NAS
2. Remove local folders (after verification)
3. Create symlinks to NAS
4. Test functionality

**Folders**: Documents, Downloads, Videos, Music

### Priority 4: Move Other Large Directories

**Action**: 
1. Identify remaining large directories in AppData\Local
2. Move to NAS
3. Create symlinks if needed

---

## 📋 Execution Steps

### Step 1: Analyze AppData\Local

```powershell
# Find top 10 largest directories
Get-ChildItem "C:\Users\mlesn\AppData\Local" -Directory | 
    ForEach-Object { 
        $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | 
            Measure-Object -Property Length -Sum).Sum / 1GB
        [PSCustomObject]@{Name=$_.Name; SizeGB=[math]::Round($size, 1)}
    } | Sort-Object SizeGB -Descending | Select-Object -First 10
```

### Step 2: Docker Migration

**Manual Action Required** (Docker Desktop must be stopped by user):
1. User stops Docker Desktop
2. Delete `C:\Users\mlesn\AppData\Local\Docker`
3. Configure Docker Desktop to use `\\10.17.17.32\homes\mlesn\docker`
4. Restart Docker Desktop

**Automated** (after Docker stopped):
```powershell
# Verify NAS copy exists
# Delete local source
Remove-Item "C:\Users\mlesn\AppData\Local\Docker" -Recurse -Force
```

### Step 3: Folder Redirection

```powershell
# For each folder (Documents, Downloads, Videos, Music)
# 1. Verify files on NAS
# 2. Remove local folder
# 3. Create symlink

$folders = @("Documents", "Downloads", "Videos", "Music")
foreach ($folder in $folders) {
    $local = "$env:USERPROFILE\$folder"
    $nas = "\\10.17.17.32\homes\mlesn\$folder"
    
    if (Test-Path $nas) {
        # Remove local (after verification)
        Remove-Item $local -Recurse -Force -ErrorAction SilentlyContinue
        # Create symlink
        New-Item -ItemType SymbolicLink -Path $local -Target $nas
    }
}
```

### Step 4: Move Other Large Directories

**After analysis**, move large directories from AppData\Local to NAS:
- Create NAS directories
- Move files
- Create symlinks if needed

---

## 📊 Progress Tracking

### Current State

- **Disk Usage**: 98.6% (CRITICAL)
- **AppData\Local**: 198.4 GB (analyzing)
- **Docker**: 133.8 GB (ready to free)
- **Folders**: Not redirected (need symlinks)

### Target State

- **Disk Usage**: < 80%
- **Space Freed**: ~686 GB
- **Folders**: All redirected with symlinks
- **Docker**: Using NAS path

---

## 🔄 Next Actions

1. ✅ Analyze AppData\Local breakdown
2. ⏳ Document Docker stop instructions
3. ⏳ Complete folder redirection symlinks
4. ⏳ Move other large AppData directories
5. ⏳ Continue finding remaining large directories

---

**Status**: 🔄 **EXECUTING - ANALYZING APPDATA**  
**Priority**: 🔴 **CRITICAL** - 98.6% disk usage  
**Next Action**: Complete AppData analysis, document Docker stop process  
**Tags**: `#DOIT` `#NAS` `#MIGRATION` `@LUMINA` `@JARVIS` `#PEAK`
