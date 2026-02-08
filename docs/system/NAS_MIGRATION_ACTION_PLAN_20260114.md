# NAS Migration PXE Boot - Action Plan

**Date**: 2026-01-14
**Status**: 🔄 **IN PROGRESS - CRITICAL ACTIONS REQUIRED**
**Tags**: `#NAS` `#MIGRATION` `#PXE` `#DISK_CLEANUP` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Current State Summary

### Disk Usage Status

- **Current**: 97.1% used (3,589 GB used, 106 GB free)
- **Target**: < 80% used (< 2,956 GB used)
- **Gap**: ~630 GB to free
- **Status**: 🔴 **CRITICAL - IMMEDIATE ACTION REQUIRED**

### Migration Status

| Component | Status | Details |
|-----------|--------|---------|
| **NAS Connectivity** | ✅ Working | `\\10.17.17.32\homes\mlesn` accessible |
| **Ollama Models** | ✅ Migrated | `OLLAMA_MODELS` points to `\\10.17.17.32\data\models\ollama` |
| **Documents Folder** | ❌ Not Redirected | Local path, not symlink |
| **Downloads Folder** | ❌ Not Redirected | Local path, not symlink |
| **Pictures Folder** | ❌ Not Redirected | Local path, not symlink |
| **Videos Folder** | ❌ Not Redirected | Local path, not symlink |
| **Music Folder** | ❌ Not Redirected | Local path, not symlink |
| **Docker Volumes** | ⚠️ Unknown | Needs verification |
| **VS Code/Cursor Cache** | ⚠️ Unknown | Needs verification |
| **Symlinks** | ⚠️ Unknown | Needs verification |

---

## 🚨 Critical Action Items

### Priority 1: Disk Cleanup (CRITICAL) 🔴

**Target**: Free ~630 GB to get below 80% usage

**Immediate Actions**:

1. **Identify Large Files/Directories**
   ```powershell
   # Check common large directories
   - C:\Users\mlesn\Downloads (likely large)
   - C:\Users\mlesn\Documents (if not redirected)
   - C:\Users\mlesn\Videos (if not redirected)
   - C:\Users\mlesn\Pictures (if not redirected)
   - C:\Users\mlesn\AppData\Local (caches, temp files)
   - C:\Users\mlesn\AppData\Roaming (app data)
   - C:\ProgramData (system caches)
   - C:\Windows\Temp (system temp)
   ```

2. **Move Large Files to NAS**
   - Move Downloads folder contents to `\\10.17.17.32\homes\mlesn\Downloads`
   - Move Videos to `\\10.17.17.32\homes\mlesn\Videos`
   - Move Pictures to `\\10.17.17.32\homes\mlesn\Pictures`
   - Move Music to `\\10.17.17.32\homes\mlesn\Music`

3. **Clean Temporary Files**
   ```powershell
   # Clean temp files
   Remove-Item $env:TEMP\* -Recurse -Force -ErrorAction SilentlyContinue
   Remove-Item C:\Windows\Temp\* -Recurse -Force -ErrorAction SilentlyContinue

   # Clean browser caches (if applicable)
   # Clean npm/pip caches
   # Clean Docker unused images/volumes
   ```

4. **Remove Old Backups/Logs**
   - Check for old backup files
   - Remove old log files
   - Clean up old project files

**Priority**: 🔴 **CRITICAL - DO FIRST**

---

### Priority 2: Implement Folder Redirection (HIGH) 🟠

**Target**: Redirect all Windows standard folders to NAS

**Actions**:

1. **Prepare NAS Folders**
   ```powershell
   # Ensure NAS folders exist
   New-Item -Path "\\10.17.17.32\homes\mlesn\Documents" -ItemType Directory -Force
   New-Item -Path "\\10.17.17.32\homes\mlesn\Downloads" -ItemType Directory -Force
   New-Item -Path "\\10.17.17.32\homes\mlesn\Pictures" -ItemType Directory -Force
   New-Item -Path "\\10.17.17.32\homes\mlesn\Videos" -ItemType Directory -Force
   New-Item -Path "\\10.17.17.32\homes\mlesn\Music" -ItemType Directory -Force
   ```

2. **Move Existing Files to NAS**
   ```powershell
   # Move Documents (if not empty)
   Move-Item "$env:USERPROFILE\Documents\*" "\\10.17.17.32\homes\mlesn\Documents\" -Force

   # Move Downloads
   Move-Item "$env:USERPROFILE\Downloads\*" "\\10.17.17.32\homes\mlesn\Downloads\" -Force

   # Move Pictures
   Move-Item "$env:USERPROFILE\Pictures\*" "\\10.17.17.32\homes\mlesn\Pictures\" -Force

   # Move Videos
   Move-Item "$env:USERPROFILE\Videos\*" "\\10.17.17.32\homes\mlesn\Videos\" -Force

   # Move Music
   Move-Item "$env:USERPROFILE\Music\*" "\\10.17.17.32\homes\mlesn\Music\" -Force
   ```

3. **Create Symlinks or Registry Redirects**

   **Option A: Symlinks (Simple)**
   ```powershell
   # Remove local folders
   Remove-Item "$env:USERPROFILE\Documents" -Force
   Remove-Item "$env:USERPROFILE\Downloads" -Force
   Remove-Item "$env:USERPROFILE\Pictures" -Force
   Remove-Item "$env:USERPROFILE\Videos" -Force
   Remove-Item "$env:USERPROFILE\Music" -Force

   # Create symlinks
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\Documents" -Target "\\10.17.17.32\homes\mlesn\Documents"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\Downloads" -Target "\\10.17.17.32\homes\mlesn\Downloads"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\Pictures" -Target "\\10.17.17.32\homes\mlesn\Pictures"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\Videos" -Target "\\10.17.17.32\homes\mlesn\Videos"
   New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\Music" -Target "\\10.17.17.32\homes\mlesn\Music"
   ```

   **Option B: Registry Redirects (Windows Native)**
   ```powershell
   # Use Windows folder redirection via registry
   # More complex but Windows-native
   ```

**Priority**: 🟠 **HIGH - DO AFTER DISK CLEANUP**

---

### Priority 3: Verify App Data Migration (MEDIUM) 🟡

**Target**: Verify all app data is on NAS or properly configured

**Actions**:

1. **Verify Ollama** ✅ (Already done)
   - `OLLAMA_MODELS` = `\\10.17.17.32\data\models\ollama`

2. **Verify Docker**
   ```powershell
   # Check Docker Desktop settings
   # Verify volumes are on NAS
   # Check Docker data directory
   ```

3. **Verify VS Code/Cursor**
   ```powershell
   # Check extensions cache location
   # Check workspace storage location
   # Move to NAS if needed
   ```

4. **Verify npm/pip Caches**
   ```powershell
   # Check npm cache location
   # Check pip cache location
   # Redirect to NAS if needed
   ```

**Priority**: 🟡 **MEDIUM - DO AFTER FOLDER REDIRECTION**

---

### Priority 4: Verify Symlinks (MEDIUM) 🟡

**Target**: Verify all symlinks are working correctly

**Actions**:

1. **List All Symlinks**
   ```powershell
   Get-ChildItem $env:USERPROFILE -Recurse -ErrorAction SilentlyContinue | Where-Object {$_.LinkType -eq 'SymbolicLink'} | Select-Object FullName, Target
   ```

2. **Verify Symlink Targets**
   - Check each symlink points to correct NAS path
   - Verify NAS paths are accessible
   - Test file access through symlinks

3. **Fix Broken Symlinks**
   - Recreate any broken symlinks
   - Update any incorrect targets

**Priority**: 🟡 **MEDIUM - DO AFTER APP DATA VERIFICATION**

---

## 📋 Execution Plan

### Phase 1: Immediate Disk Cleanup (Today)

1. ✅ **Check Current Disk Usage** - DONE (97.1%)
2. 🔄 **Identify Large Files** - IN PROGRESS
3. 🔄 **Move Large Files to NAS** - TO DO
4. 🔄 **Clean Temporary Files** - TO DO
5. 🔄 **Verify Disk Usage < 80%** - TO DO

**Target**: Free ~630 GB

---

### Phase 2: Folder Redirection (This Week)

1. 🔄 **Prepare NAS Folders** - TO DO
2. 🔄 **Move Existing Files** - TO DO
3. 🔄 **Create Symlinks** - TO DO
4. 🔄 **Verify Redirection** - TO DO

**Target**: All Windows folders redirected to NAS

---

### Phase 3: App Data Verification (This Week)

1. ✅ **Ollama** - VERIFIED
2. 🔄 **Docker** - TO DO
3. 🔄 **VS Code/Cursor** - TO DO
4. 🔄 **npm/pip** - TO DO

**Target**: All app data verified or migrated

---

### Phase 4: Symlink Verification (This Week)

1. 🔄 **List Symlinks** - TO DO
2. 🔄 **Verify Targets** - TO DO
3. 🔄 **Fix Issues** - TO DO

**Target**: All symlinks working correctly

---

## 🎯 Success Criteria

### Immediate (Today)

- [ ] Disk usage < 80% (currently 97.1%)
- [ ] ~630 GB freed

### Short-Term (This Week)

- [ ] All Windows folders redirected to NAS
- [ ] All app data verified/migrated
- [ ] All symlinks verified/working

### Long-Term (Future)

- [ ] PXE boot production deployment (if needed)
- [ ] Performance optimization
- [ ] Monitoring and maintenance

---

## 📊 Progress Tracking

### Current Metrics

- **Disk Usage**: 97.1% (🔴 CRITICAL)
- **NAS Connectivity**: ✅ Working
- **Ollama Migration**: ✅ Complete
- **Folder Redirection**: ❌ 0/5 folders
- **App Data Migration**: ⚠️ Partial (1/4 verified)
- **Symlinks**: ⚠️ Unknown

### Target Metrics

- **Disk Usage**: < 80%
- **NAS Connectivity**: ✅ Working
- **Ollama Migration**: ✅ Complete
- **Folder Redirection**: ✅ 5/5 folders
- **App Data Migration**: ✅ All verified
- **Symlinks**: ✅ All verified

---

## 🚀 Next Steps

### Immediate (Today)

1. **Start Disk Cleanup**
   - Identify largest directories
   - Move files to NAS
   - Clean temp files
   - Target: < 80% disk usage

### Short-Term (This Week)

2. **Implement Folder Redirection**
   - Move files to NAS
   - Create symlinks
   - Verify functionality

3. **Verify App Data**
   - Check Docker
   - Check VS Code/Cursor
   - Check npm/pip

4. **Verify Symlinks**
   - List all symlinks
   - Verify targets
   - Fix issues

---

## 📝 Notes

- **Plan Status**: All phases marked "completed" but reality shows critical gaps
- **Disk Usage**: Still critical at 97.1% - immediate action required
- **Folder Redirection**: None implemented - needs immediate attention
- **App Data**: Only Ollama verified - others need checking
- **Symlinks**: Unknown status - needs verification

---

**Status**: 🔄 **ACTION PLAN CREATED - READY FOR EXECUTION**
**Next Action**: Start disk cleanup (Priority 1 - CRITICAL)
**Tags**: `#NAS` `#MIGRATION` `#PXE` `#DISK_CLEANUP` `@LUMINA` `@JARVIS` `#PEAK`
