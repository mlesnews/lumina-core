# Dropbox Space Crisis - Urgent Migration Plan

**Date**: 2026-01-01  
**Status**: 🔴 **CRITICAL - IMMEDIATE ACTION REQUIRED**  
**Tag**: #CRISIS #MIGRATION #DROPBOX #SPACE

---

## 🚨 Current Crisis

### Drive Space Status
- **C: Drive**: 10.3% free (380.8 GB free / 3.6 TB total)
- **Status**: CRITICAL - Dropbox not functioning
- **Root Cause**: `my_projects` taking up space on C: drive
- **Solution**: Migrate `my_projects` to NAS immediately

---

## 🎯 Immediate Action Plan

### Step 1: Map Network Drive (M:)

**Target**: `\\10.17.17.32\backups\MATT_Backups\my_projects`

```powershell
# Run network drive mapping script
.\scripts\powershell\map_my_projects_to_m_drive.ps1

# Or manually map
net use M: \\10.17.17.32\backups\MATT_Backups\my_projects /persistent:yes
```

### Step 2: Start Migration

**Option A: Using Migration Script (Recommended)**
```powershell
# Use enhanced migration script
.\scripts\fast_c_to_d_migration.ps1 `
  -SourcePath "C:\Users\mlesn\Dropbox\my_projects" `
  -DestPath "M:\my_projects" `
  -Threads 16
```

**Option B: Direct Robocopy (Fastest)**
```powershell
# High-speed robocopy migration
robocopy "C:\Users\mlesn\Dropbox\my_projects" "M:\my_projects" `
  /MIR /MT:16 /R:3 /W:5 /LOG:"M:\migration_log.txt" `
  /XD ".git" "node_modules" "__pycache__" `
  /XF "*.tmp" "*.log" "*.cache"
```

**Option C: NAS-Enhanced Migration**
```powershell
# If NAS API is available
.\scripts\nas_enhanced_migration.ps1 `
  -SourcePath "C:\Users\mlesn\Dropbox\my_projects" `
  -DestPath "M:\my_projects" `
  -UseNasApi `
  -Threads 16
```

---

## 📋 Migration Checklist

### Pre-Migration
- [ ] Verify NAS connectivity: `ping 10.17.17.32`
- [ ] Map M: drive to NAS
- [ ] Verify NAS has space (39TB free confirmed)
- [ ] Stop Dropbox sync temporarily (to prevent conflicts)
- [ ] Backup critical files (if needed)

### During Migration
- [ ] Monitor migration progress
- [ ] Check for errors in log file
- [ ] Verify files are copying correctly
- [ ] Don't interrupt migration

### Post-Migration
- [ ] Verify data integrity (spot check)
- [ ] Update path references in scripts
- [ ] Update environment variables
- [ ] Test critical applications
- [ ] Re-enable Dropbox sync (pointing to NAS)
- [ ] Delete original from C: drive (after verification)

---

## 🔧 Path Updates Needed

After migration, update these references:

### Environment Variables
```powershell
# Update project root
$env:CFS_PROJECT_DIR = "M:\my_projects"
$env:LUMINA_PROJECT_ROOT = "M:\my_projects\.lumina"
```

### Scripts
- Update hardcoded paths in scripts
- Update config files
- Update JARVIS path references

### Dropbox
- Point Dropbox to sync from NAS location
- Or disable Dropbox sync for `my_projects` (now on NAS)

---

## ⚡ Quick Start (Fastest Method)

```powershell
# 1. Map drive
net use M: \\10.17.17.32\backups\MATT_Backups\my_projects /persistent:yes

# 2. Start migration (robocopy - fastest)
robocopy "C:\Users\mlesn\Dropbox\my_projects" "M:\my_projects" /MIR /MT:16 /R:3 /W:5 /LOG:"M:\migration_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"

# 3. Monitor progress
Get-Content "M:\migration_*.log" -Tail 20 -Wait
```

---

## 📊 Expected Results

### Space Freed
- **my_projects size**: ~1TB+ (estimated)
- **C: Drive after**: ~15-20% free (estimated)
- **Dropbox**: Will function again

### Time Estimate
- **Robocopy**: ~2-4 hours (depending on data size and network speed)
- **With MT:16**: Maximum speed with 16 threads

---

## ⚠️ Important Notes

1. **Don't Delete Original Yet**: Keep original until migration verified
2. **Dropbox Sync**: Disable during migration to prevent conflicts
3. **Network Speed**: Migration speed depends on network (1Gbps = ~125 MB/s)
4. **Resume Capability**: Robocopy can resume if interrupted
5. **Verification**: Always verify data integrity before deleting original

---

## 🆘 Troubleshooting

### Network Drive Won't Map
```powershell
# Check NAS connectivity
ping 10.17.17.32

# Check credentials
# May need to use: net use M: \\10.17.17.32\backups\MATT_Backups /user:username
```

### Migration Slow
- Check network speed: `Test-NetConnection -ComputerName 10.17.17.32`
- Increase threads: `/MT:32` (if system can handle)
- Check NAS disk I/O

### Errors During Migration
- Check log file for specific errors
- Robocopy will retry automatically (/R:3)
- Common issues: permissions, file locks, network drops

---

## ✅ Success Criteria

- [ ] Migration completes without critical errors
- [ ] Data verified on NAS
- [ ] C: drive space increased significantly
- [ ] Dropbox functioning again
- [ ] All path references updated
- [ ] Applications working with new paths

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Priority**: 🔴 CRITICAL - Execute immediately
