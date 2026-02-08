# Migration Execution Checklist

**Date**: 2026-01-01  
**Status**: 🟢 **IN PROGRESS**  
**Tag**: #MIGRATION #CHECKLIST #EXECUTION

---

## 📋 Complete Migration Checklist

### Phase 1: my_projects Migration ✅ IN PROGRESS

- [x] **Started migration** (2026-01-01 19:08:27)
- [ ] **Monitor migration progress**
  ```powershell
  Get-Process -Name "robocopy"
  Get-Content migration_log_20260101_190827.txt -Tail 20 -Wait
  ```
- [ ] **Verify migration complete**
  - Check robocopy process finished
  - Verify file counts match
  - Spot check critical files
- [ ] **Verify data on NAS**
  ```powershell
  Test-Path "\\10.17.17.32\backups\MATT_Backups\my_projects"
  Get-ChildItem "\\10.17.17.32\backups\MATT_Backups\my_projects" | Measure-Object
  ```

---

### Phase 2: Network Drive Mapping

- [ ] **Map M: drive** (my_projects)
  ```powershell
  net use M: \\10.17.17.32\backups\MATT_Backups\my_projects /persistent:yes
  ```
- [ ] **Map L: drive** (LUMINA data)
  ```powershell
  net use L: \\10.17.17.32\backups\MATT_Backups\lumina_data /persistent:yes
  ```
- [ ] **Verify drives mapped**
  ```powershell
  Test-Path "M:\"
  Test-Path "L:\"
  ```

---

### Phase 3: Path Updates

- [ ] **Update environment variables**
  ```powershell
  .\scripts\powershell\update_paths_after_migration.ps1
  ```
- [ ] **Verify environment variables**
  ```powershell
  $env:CFS_PROJECT_DIR
  $env:LUMINA_PROJECT_ROOT
  ```
- [ ] **Update script paths**
  - Review and update hardcoded paths
  - Update config files
  - Update JARVIS references

---

### Phase 4: LUMINA Data Migration

- [ ] **Identify LUMINA data**
  ```powershell
  .\scripts\powershell\identify_lumina_data.ps1
  ```
- [ ] **Migrate high-priority data**
  - data/ (1.13 GB total)
  - data/holocron/ (0.25 GB)
  - data/backups/
- [ ] **Migrate to NAS**
  ```powershell
  robocopy "C:\Users\mlesn\Dropbox\my_projects\.lumina\data" "L:\data" /MIR /MT:16
  ```
- [ ] **Verify LUMINA data on NAS**
- [ ] **Update LUMINA configs** to point to NAS

---

### Phase 5: DSM Cloud Sync Setup (REQUIRED)

- [ ] **Access DSM web interface**
  ```
  http://10.17.17.32:5000
  ```
- [ ] **Install Cloud Sync package**
  - Package Center → Search "Cloud Sync" → Install
- [ ] **Configure cloud provider**
  - Open Cloud Sync
  - Add provider (Dropbox/OneDrive/Google Drive)
  - Authorize and grant permissions
- [ ] **Create sync task**
  - Task Name: `LUMINA_Projects_Backup`
  - Local Path: `/volume1/backups/MATT_Backups/my_projects`
  - Remote Path: `/LUMINA_Backups/my_projects`
  - Direction: One-way (Upload only)
- [ ] **Configure selective sync**
  - Include: `.lumina/**`, `config/**`, `scripts/**`, `docs/**`, `*.json`, `*.yaml`, `*.md`, `*.py`, `*.ps1`
  - Exclude: `data/**`, `node_modules/**`, `__pycache__/**`, `*.mp4`, `*.model`, `*.zip`, `*.log`
- [ ] **Set sync schedule**
  - Daily at 2:00 AM (or continuous)
- [ ] **Start initial sync**
- [ ] **Verify files in cloud**
- [ ] **Test restore** (verify can restore from cloud)

**Guide**: `docs/system/DSM_CLOUD_SYNC_SETUP.md`  
**Script**: `.\scripts\powershell\setup_dsm_cloud_sync.ps1`

---

### Phase 6: System Testing

- [ ] **Test LUMINA systems**
  - JARVIS
  - MANUS
  - R5 Matrix
  - All integrations
- [ ] **Test path references**
  - Verify all scripts work
  - Verify configs load correctly
  - Verify data access
- [ ] **Test network drives**
  - Verify auto-mapping on startup
  - Verify persistent connections
- [ ] **Test DSM Cloud Sync**
  - Verify sync is working
  - Verify files in cloud
  - Test restore capability

---

### Phase 7: Dropbox Cleanup

- [ ] **Verify all data migrated**
  - my_projects on NAS
  - LUMINA data on NAS
  - DSM Cloud Sync working
- [ ] **Disable Dropbox sync for my_projects**
  - Dropbox settings → Selective Sync
  - Uncheck `my_projects`
- [ ] **Delete original from C: drive** (after verification)
  - Keep backup for 30 days if possible
  - Or move to archive location
- [ ] **Update Dropbox settings**
  - Point to NAS location if needed
  - Or remove Dropbox dependency

---

### Phase 8: Documentation & Optimization

- [ ] **Update documentation**
  - Update path references in docs
  - Document new architecture
  - Update runbooks
- [ ] **Set up auto-mapping**
  - Network drives auto-map on startup
  - Persistent connections
- [ ] **Optimize NAS performance**
  - Check network speed
  - Optimize sync schedules
  - Monitor storage usage
- [ ] **Create backup verification script**
  - Verify DSM Cloud Sync status
  - Verify data integrity
  - Generate reports

---

## 📊 Progress Tracking

### Current Status

**Phase 1**: ✅ IN PROGRESS (my_projects migration running)  
**Phase 2**: ⏳ PENDING (wait for Phase 1)  
**Phase 3**: ⏳ PENDING (wait for Phase 1)  
**Phase 4**: ⏳ PENDING (wait for Phase 1)  
**Phase 5**: ⏳ PENDING (REQUIRED - can start after Phase 1)  
**Phase 6**: ⏳ PENDING (wait for all phases)  
**Phase 7**: ⏳ PENDING (wait for verification)  
**Phase 8**: ⏳ PENDING (final step)

---

## 🚀 Quick Commands Reference

### Check Migration Status
```powershell
Get-Process -Name "robocopy"
Get-Content migration_log_20260101_190827.txt -Tail 20
```

### Map Network Drives
```powershell
net use M: \\10.17.17.32\backups\MATT_Backups\my_projects /persistent:yes
net use L: \\10.17.17.32\backups\MATT_Backups\lumina_data /persistent:yes
```

### Update Paths
```powershell
.\scripts\powershell\update_paths_after_migration.ps1
```

### Identify LUMINA Data
```powershell
.\scripts\powershell\identify_lumina_data.ps1
```

### DSM Cloud Sync Setup
```powershell
.\scripts\powershell\setup_dsm_cloud_sync.ps1
```

### Run Full Execution
```powershell
.\scripts\powershell\execute_full_migration.ps1
```

---

## ⚠️ Important Notes

1. **Don't delete original** until migration verified
2. **DSM Cloud Sync is REQUIRED** - not optional
3. **Test everything** before disabling Dropbox
4. **Monitor migration** - 2.98 TB will take hours
5. **Keep backups** - maintain redundancy

---

## ✅ Success Criteria

- [ ] my_projects fully migrated to NAS
- [ ] LUMINA data migrated to NAS
- [ ] All path references updated
- [ ] Network drives auto-mapping
- [ ] DSM Cloud Sync working (REQUIRED)
- [ ] All systems tested and working
- [ ] Dropbox sync disabled
- [ ] C: drive space freed (2.98 TB)
- [ ] Documentation updated

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: Migration in progress - Follow checklist sequentially
