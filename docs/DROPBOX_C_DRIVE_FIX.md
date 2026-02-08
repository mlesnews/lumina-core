# Dropbox C Drive Issue - Root Cause & Solution

## Problem Identified

**Dropbox folder on C drive is 4.5 TB!**

- **Location**: `C:\Users\<username>\Dropbox`
- **Size**: ~4.5 TB
- **Impact**: This is the primary cause of C drive filling up

## Solutions

### Option 1: Move Dropbox to D Drive (Recommended)

1. **Pause Dropbox Sync**
   - Right-click Dropbox icon in system tray
   - Select "Pause syncing" → "2 hours" (or until finished)

2. **Move Dropbox Folder**
   - Open Dropbox settings
   - Go to "Preferences" → "Sync"
   - Click "Move" next to Dropbox folder location
   - Change from: `C:\Users\<username>\Dropbox`
   - Change to: `D:\Dropbox` (or `D:\Users\<username>\Dropbox`)
   - Let Dropbox move the files (this may take hours for 4.5 TB)

3. **Verify Move**
   - Ensure all files synced correctly
   - Check that projects still work

### Option 2: Use Selective Sync

If you need Dropbox on C drive but want to reduce size:

1. **Open Dropbox Settings**
   - Right-click Dropbox icon → Settings
   - Go to "Sync" tab

2. **Selective Sync**
   - Click "Choose folders to sync"
   - Uncheck large folders/projects you don't actively need on this machine
   - Keep only essential folders synced
   - Files still accessible via web if needed

### Option 3: Clean Up Dropbox Contents

1. **Identify Large Folders**
   ```powershell
   Get-ChildItem "C:\Users\$env:USERNAME\Dropbox" -Directory -Recurse | 
   ForEach-Object { 
       $size = [math]::Round((Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | 
       Measure-Object -Property Length -Sum -ErrorAction SilentlyContinue).Sum / 1GB, 2)
       if ($size -gt 10) { 
           [PSCustomObject]@{Path=$_.FullName; SizeGB=$size} 
       } 
   } | Sort-Object SizeGB -Descending
   ```

2. **Archive or Delete**
   - Move old/unused projects to archive
   - Delete duplicates
   - Remove large files no longer needed

### Option 4: Use Smart Sync (Dropbox Plus/Business)

If you have Dropbox Plus or Business:
- Use Smart Sync to keep files online-only
- Files appear in Explorer but don't take local disk space
- Download on-demand when accessed

## Immediate Actions

### Quick Win: Clean Up Your Projects Folder

Since your projects are in `C:\Users\<username>\Dropbox\my_projects\.lumina`:

1. **Check if projects can move to D:**
   - Identify projects that don't need to be in Dropbox
   - Move them directly to D: drive
   - Remove from Dropbox sync

2. **Clean up project artifacts:**
   ```powershell
   # Find large files in projects
   Get-ChildItem "C:\Users\$env:USERNAME\Dropbox\my_projects" -Recurse -File | 
   Where-Object { $_.Length -gt 100MB } | 
   Sort-Object Length -Descending | 
   Select-Object -First 20 FullName, @{Name="SizeGB";Expression={[math]::Round($_.Length/1GB,2)}}
   ```

## Recommended Solution

**Move Dropbox to D: drive** - This solves the root cause:

1. Most effective - removes 4.5 TB from C drive
2. Better performance - D drive may be faster/less used
3. Safer - C drive is for OS, D drive for data
4. Prevents future issues

## Steps to Move Dropbox

1. **Create target location**:
   ```powershell
   New-Item -ItemType Directory -Path "D:\Dropbox" -Force
   ```

2. **Use Dropbox built-in move** (safest):
   - Dropbox Settings → Sync → Move
   - This ensures all sync links are updated

3. **Or manually move** (if needed):
   ```powershell
   # Stop Dropbox
   Stop-Process -Name Dropbox -Force -ErrorAction SilentlyContinue
   
   # Move folder
   Move-Item -Path "C:\Users\$env:USERNAME\Dropbox" -Destination "D:\Dropbox" -Force
   
   # Update Dropbox settings manually (advanced)
   ```

## After Moving

1. Verify all files synced
2. Test that projects still work
3. Check Dropbox shows correct location
4. Monitor C drive space

## Prevention

- Keep large data/projects on D: drive, not in Dropbox on C:
- Use Dropbox for small files, code, documents
- Store large datasets, media, VMs on D: drive
- Use Selective Sync for large folders

---

**Created**: 2025-12-31  
**Priority**: CRITICAL - This is the root cause of C drive filling up
