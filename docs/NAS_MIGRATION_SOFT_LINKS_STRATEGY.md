# NAS Migration - Soft Links Strategy

**Date**: 2025-01-14  
**Status**: ✅ **SOFT LINKS STRATEGY IMPLEMENTED**

---

## 🎯 Strategy Overview

### Why Soft Links?

**Benefits**:
1. **Files appear in original location** - Dropbox, Cursor, and all apps see files where they expect them
2. **Data actually on NAS** - Frees local disk space
3. **Reconfigurable** - Can remove/repoint links after move completes
4. **Safer** - Can verify data on NAS before removing local copies
5. **Transparent** - Applications don't need path changes

### How It Works

```
Before:
C:\Users\mlesn\Dropbox\my_projects\data\time_travel\ (2847 GB on C:)

After Move:
C:\Users\mlesn\Dropbox\my_projects\data\time_travel\ → (symlink)
  → \\10.17.17.32\homes\mlesn\my_projects\data\time_travel\ (actual data)
```

**Result**: Files appear at original path, but data is on NAS.

---

## 📋 Implementation Steps

### Phase 1: Move Data to NAS
1. **Rename local folder** to `.moving` (prevents conflicts)
2. **Copy to NAS** via robocopy (safe, resumable)
3. **Verify** sizes match
4. **Delete local** `.moving` folder
5. **Create soft link** from original path to NAS

### Phase 2: Reconfigure Pathing (After Moves Complete)
1. **Check all soft links** in my_projects
2. **Options**:
   - Keep soft links (default - files appear in original location)
   - Convert to junction points (more compatible)
   - Remove links and update paths directly (if needed)

---

## 🔧 Scripts

### 1. `move_time_travel_softlink.ps1`
- Moves time_travel folder using soft link strategy
- Renames to `.moving`, copies to NAS, verifies, creates symlink
- **Status**: Running in background

### 2. `move_with_softlinks.ps1`
- Moves all my_projects subdirectories using soft links
- Handles large directories with robocopy
- Creates symlinks automatically

### 3. `reconfigure_pathing_after_move.ps1`
- Reconfigures pathing after all moves complete
- Can convert symlinks to junctions
- Can remove links and update paths directly

---

## 📊 Current Status

### time_travel Folder (2847 GB)
- **Status**: Moving to NAS (robocopy in progress)
- **Strategy**: Soft link
- **Local Path**: `C:\Users\mlesn\Dropbox\my_projects\data\time_travel`
- **NAS Path**: `\\10.17.17.32\homes\mlesn\my_projects\data\time_travel`
- **After Move**: Local path will be symlink → NAS

### Remaining my_projects Subdirectories
- Will use same soft link strategy
- Script: `move_with_softlinks.ps1`

---

## ✅ Advantages of Soft Links

1. **Dropbox Compatibility**
   - Files appear in original Dropbox location
   - Dropbox can sync metadata/structure
   - No path changes needed in Dropbox settings

2. **Application Compatibility**
   - Cursor, VS Code see files at expected paths
   - No configuration changes needed
   - Git repositories work normally

3. **Reconfigurable**
   - Can remove links later if needed
   - Can convert to junctions
   - Can update paths directly after verification

4. **Safety**
   - Data verified on NAS before deleting local
   - Can restore if needed
   - Gradual migration possible

---

## 🔄 After Move Completion

### Reconfiguration Options

1. **Keep Soft Links** (Recommended)
   - Files appear in original location
   - No application changes needed
   - Dropbox sync works

2. **Convert to Junctions**
   - More compatible with some apps
   - Better performance in some cases
   - Run: `reconfigure_pathing_after_move.ps1` option 3

3. **Direct NAS Paths**
   - Remove links, update all paths to NAS directly
   - Requires application reconfiguration
   - Run: `reconfigure_pathing_after_move.ps1` option 2

---

## 📝 Next Steps

1. ⏳ **Wait for time_travel move** to complete
2. 🔄 **Move remaining subdirectories** using soft links
3. 🐳 **Move Docker AppData** (when Docker stopped)
4. 📊 **Compare with Kaiju** (after moves complete)
5. 🔧 **Reconfigure pathing** (optional - after verification)

---

## 🎯 Success Criteria

- ✅ All large directories moved to NAS
- ✅ Soft links created from original paths
- ✅ Files accessible at original locations
- ✅ Disk usage < 80%
- ✅ Dropbox sync resumes
- ✅ All applications work normally

---

**Last Updated**: 2025-01-14  
**Strategy**: Soft Links (Symlinks)  
**Status**: time_travel move in progress with soft link strategy
