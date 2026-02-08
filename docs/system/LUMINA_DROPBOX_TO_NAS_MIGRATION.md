# LUMINA Project: Dropbox to NAS Migration Strategy

**Date**: 2026-01-01  
**Status**: 🟢 **IN PROGRESS** - my_projects migration started  
**Tag**: #MIGRATION #DROPBOX #NAS #LUMINA

---

## 🎯 Strategic Goal

**Move Project LUMINA off Dropbox** and transition to **local cloud storage / NAS** for:
- ✅ Better performance (local network vs cloud sync)
- ✅ More control over data location
- ✅ Reduced cloud dependency
- ✅ Lower costs (no cloud storage fees)
- ✅ Better privacy (data stays local)
- ✅ Faster access (local network speeds)

---

## 📋 Migration Status

### Phase 1: my_projects Migration ✅ IN PROGRESS

**Status**: Migration started (2026-01-01 19:08:27)

**Details**:
- **Source**: `C:\Users\mlesn\Dropbox\my_projects` (2.98 TB)
- **Destination**: `\\10.17.17.32\backups\MATT_Backups\my_projects`
- **Method**: Robocopy with /MIR (mirror)
- **Threads**: 16 (maximum speed)
- **Estimated Time**: Several hours (2.98 TB)

**Benefits**:
- Frees up 2.98 TB from C: drive
- Centralizes project data on NAS
- Enables local cloud storage strategy

---

## 🏗️ Target Architecture

### Current (Dropbox-Based)
```
C:\Users\mlesn\Dropbox\my_projects\
├── .lumina\          (LUMINA project)
├── [other projects]  (various projects)
└── [synced to cloud]  (Dropbox cloud sync)
```

### Target (NAS-Based)
```
\\10.17.17.32\backups\MATT_Backups\
├── my_projects\      (all projects - centralized)
│   ├── .lumina\      (LUMINA project)
│   └── [other projects]
├── lumina_data\      (LUMINA-specific data)
├── docker_volumes\   (Docker storage)
└── backups\          (system backups)
```

**Access Methods**:
- **Network Drive**: M: drive mapped to NAS
- **UNC Path**: `\\10.17.17.32\backups\MATT_Backups`
- **Local Cloud**: NAS with DSM Cloud Sync (optional)

---

## 🔄 Migration Phases

### Phase 1: my_projects Migration ✅ IN PROGRESS
- [x] Start migration to NAS
- [ ] Verify migration complete
- [ ] Update path references
- [ ] Test applications
- [ ] Disable Dropbox sync for my_projects

### Phase 2: LUMINA-Specific Data Migration
- [ ] Identify LUMINA-specific data directories
- [ ] Migrate to `\\10.17.17.32\backups\MATT_Backups\lumina_data`
- [ ] Update LUMINA configs
- [ ] Test LUMINA systems

### Phase 3: DSM Cloud Sync Setup (REQUIRED)
- [ ] Set up DSM Cloud Sync on NAS (REQUIRED - for cloud backup)
- [ ] Configure cloud provider (Dropbox, OneDrive, Google Drive, etc.)
- [ ] Configure selective sync (only critical data)
- [ ] Set up one-way backup (NAS → Cloud)
- [ ] Test cloud sync functionality

### Phase 4: Dropbox Removal
- [ ] Remove Dropbox dependency
- [ ] Update all scripts/configs
- [ ] Verify DSM Cloud Sync is working
- [ ] Document new backup strategy

### Phase 5: Optimization
- [ ] Set up automated backups
- [ ] Configure network drive auto-mapping
- [ ] Optimize NAS performance
- [ ] Document new architecture

---

## 🎯 Benefits of NAS-Based Storage

### Performance
- ✅ **Faster Access**: Local network (1Gbps+) vs cloud sync
- ✅ **No Sync Delays**: Instant file access
- ✅ **Better for Large Files**: No cloud upload/download limits

### Control
- ✅ **Data Location**: Data stays on your network
- ✅ **No Cloud Vendor Lock-in**: Independent of Dropbox/OneDrive/etc
- ✅ **Custom Backup Strategy**: Full control over backups

### Cost
- ✅ **No Cloud Storage Fees**: Use existing NAS capacity
- ✅ **One-Time Investment**: NAS hardware vs recurring cloud fees
- ✅ **Scalable**: Add storage as needed

### Privacy
- ✅ **Local Data**: Data never leaves your network (unless you choose)
- ✅ **No Cloud Scanning**: No cloud provider scanning your files
- ✅ **Compliance**: Easier to meet data residency requirements

---

## 🔧 Implementation Details

### Network Drive Mapping

**Persistent M: Drive**:
```powershell
net use M: \\10.17.17.32\backups\MATT_Backups /persistent:yes
```

**Auto-Mapping Script**:
```powershell
.\scripts\powershell\map_my_projects_to_m_drive.ps1 -Persistent
```

### Path Updates Needed

**Environment Variables**:
```powershell
$env:CFS_PROJECT_DIR = "M:\my_projects"
$env:LUMINA_PROJECT_ROOT = "M:\my_projects\.lumina"
```

**Script Updates**:
- Update hardcoded `C:\Users\mlesn\Dropbox\my_projects` references
- Update config files
- Update JARVIS path references

### DSM Cloud Sync (REQUIRED)

**Cloud backup is REQUIRED** for redundancy:
1. **Set up DSM Cloud Sync** on NAS (REQUIRED)
2. **Selective Sync**: Only sync critical/config files
3. **Large Files**: Keep on NAS only (no cloud sync)
4. **Backup Strategy**: NAS → Cloud (one-way backup)
5. **Provider Options**: Dropbox, OneDrive, Google Drive, etc.

---

## 📊 Current Migration Progress

### my_projects Migration
- **Status**: ✅ Running
- **Size**: 2.98 TB
- **Started**: 2026-01-01 19:08:27
- **Destination**: `\\10.17.17.32\backups\MATT_Backups\my_projects`
- **Log**: `migration_log_20260101_190827.txt`

### Next Steps
1. Monitor migration progress
2. Verify data integrity after completion
3. Update path references
4. Test all LUMINA systems
5. **Set up DSM Cloud Sync (REQUIRED)**
6. Configure cloud backup
7. Disable Dropbox sync (after DSM Cloud Sync verified)

---

## ✅ Success Criteria

- [ ] my_projects fully migrated to NAS
- [ ] All path references updated
- [ ] LUMINA systems working with NAS paths
- [ ] DSM Cloud Sync set up and working (REQUIRED)
- [ ] Cloud backup configured and tested
- [ ] Dropbox sync disabled for my_projects
- [ ] C: drive space freed (2.98 TB)
- [ ] Network drives auto-mapping on startup
- [ ] Backup strategy documented
- [ ] Documentation updated

---

## 🚀 Quick Reference

### Check Migration Status
```powershell
Get-Process -Name "robocopy" -ErrorAction SilentlyContinue
Get-Content migration_log_20260101_190827.txt -Tail 20
```

### Map Network Drive
```powershell
net use M: \\10.17.17.32\backups\MATT_Backups /persistent:yes
```

### Verify NAS Access
```powershell
Test-Path "\\10.17.17.32\backups\MATT_Backups\my_projects"
```

### Update Environment Variables
```powershell
[System.Environment]::SetEnvironmentVariable("CFS_PROJECT_DIR", "M:\my_projects", "User")
[System.Environment]::SetEnvironmentVariable("LUMINA_PROJECT_ROOT", "M:\my_projects\.lumina", "User")
```

---

## 📝 Notes

- **Migration Time**: 2.98 TB will take several hours
- **Network Speed**: Depends on 1Gbps network connection
- **Resume Capability**: Robocopy can resume if interrupted
- **Verification**: Always verify data before deleting original
- **Backup**: Keep original until migration verified

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: Migration in progress - Strategic move to NAS-based storage
