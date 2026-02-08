# NAS Migration Integration Plan
## Complete Integration of DSM Cloud Storage & Cloud.local System

**Date:** January 9, 2025  
**Request ID:** 7eed9d32-9d75-4fb0-aefd-4a86fb0eff85  
**Status:** 🚀 Ready for Integration

---

## Executive Summary

The NAS migration initiative needs to be completed with full integration of:
1. **DSM Cloud Storage Package** - Like n8n@NAS, installed but not fully integrated
2. **Cloud.local System** - Multiple cloud storage provider integration
3. **Data Migration** - Move large files from KAIJU_NO_8 and MILLENNIUM_FALC to NAS
4. **Homelab Sharing** - Share storage to all homelab systems

**Current State:**
- ✅ NAS is reachable (10.17.17.32)
- ✅ DSM package setup scripts exist
- ⚠️ DSM package installed but not fully integrated
- ⚠️ Cloud.local system not configured
- ⚠️ Large files consuming local disk space on both systems

---

## Systems Overview

### KAIJU_NO_8 (Desktop)
- **IP:** 10.17.17.11
- **Primary Drive:** D: (not C:)
- **Dropbox Path:** `D:\Dropbox`
- **Status:** Large files consuming disk space

### MILLENNIUM_FALC (Laptop)
- **Primary Drive:** C:
- **Dropbox Path:** `C:\Users\mlesn\Dropbox`
- **Status:** Large files consuming disk space

### NAS
- **IP:** 10.17.17.32
- **Backup Path:** `\\10.17.17.32\backups\MATT_Backups`
- **Status:** Ready for migration

---

## Phase 1: DSM Cloud Storage Package Integration

### Current Status
- ✅ Package installed on NAS (similar to n8n@NAS)
- ⚠️ Not fully integrated
- ⚠️ Not configured for cloud providers

### Integration Steps

1. **Access DSM Package Center**
   ```
   http://10.17.17.32:5000
   → Package Center
   → Cloud Storage Packages
   ```

2. **Configure Cloud Sync Package**
   - Install/Update Cloud Sync
   - Add cloud providers:
     - Google Drive
     - Dropbox
     - OneDrive
     - Amazon S3 (optional)
     - Backblaze B2 (optional)
     - Wasabi (optional)

3. **Set Up Sync Tasks**
   - Configure sync from cloud providers → NAS
   - Set up bidirectional sync if needed
   - Configure sync schedules

4. **Integration Script**
   ```bash
   python scripts/python/nas_dsm_cloud_storage_setup.py
   python scripts/python/configure_all_dsm_packages_full_auto.py
   ```

---

## Phase 2: Cloud.local System Setup

### Architecture
```
Cloud Providers (Google Drive, Dropbox, OneDrive)
         ↓
    DSM Cloud Sync
         ↓
    NAS Storage (10.17.17.32)
         ↓
    cloud.local (DNS/Reverse Proxy)
         ↓
    All Homelab Systems
```

### Setup Steps

1. **DNS Configuration**
   - Add `cloud.local` DNS entry pointing to NAS (10.17.17.32)
   - Configure on pfSense or local DNS server
   - Add to hosts file on all systems if needed

2. **Reverse Proxy Setup**
   - Configure DSM Reverse Proxy
   - Map cloud.local → Cloud Station/Drive service
   - Set up SSL certificate for cloud.local

3. **SMB/NFS Shares**
   - Create shared folders for cloud storage
   - Configure permissions for homelab systems
   - Set up automatic mounting on KAIJU_NO_8 and MILLENNIUM_FALC

4. **Unified Authentication**
   - Set up LDAP/Active Directory integration (if available)
   - Or configure shared credentials
   - Enable SSO if possible

---

## Phase 3: Data Migration from Local Disks

### Migration Strategy

#### KAIJU_NO_8 (Desktop)
**Target:** `\\10.17.17.32\backups\MATT_Backups\migration\kaiju_no_8`

**Priority Items:**
1. **Large Media Files** (Videos, Downloads)
   - Scan: `D:\Videos`, `D:\Downloads`
   - Migrate files > 1GB
   - Keep local symlinks for access

2. **Project Backups**
   - Old project archives
   - Completed project backups
   - Large datasets

3. **Cache and Temp Files**
   - Application caches
   - Temporary files
   - Old logs

#### MILLENNIUM_FALC (Laptop)
**Target:** `\\10.17.17.32\backups\MATT_Backups\migration\millennium_falc`

**Priority Items:**
1. **Large Media Files**
   - Videos, large downloads
   - Media archives

2. **Dropbox Large Files**
   - Large files in Dropbox that can be archived
   - Old project files

3. **Application Data**
   - Large application caches
   - Old backups

### Migration Tools

1. **Robocopy** (Recommended for Windows)
   ```powershell
   robocopy "D:\Source" "\\10.17.17.32\backups\MATT_Backups\migration\kaiju_no_8\Source" /MIR /R:3 /W:5 /LOG:migration.log
   ```

2. **Migration Scripts**
   ```bash
   python scripts/python/execute_nas_migration.py
   python scripts/python/resume_nas_migration_initiative.py
   ```

3. **Verification**
   - Verify file integrity after migration
   - Check file counts and sizes
   - Test access from NAS

---

## Phase 4: Homelab Integration

### Systems to Integrate
- KAIJU_NO_8 (10.17.17.11)
- MILLENNIUM_FALC (Laptop)
- NAS (10.17.17.32)
- pfSense (if applicable)
- Other homelab systems

### Integration Steps

1. **Network Drive Mapping**
   - Map NAS drives on all systems
   - Set up automatic reconnection
   - Configure credentials

2. **Cloud.local Access**
   - Configure cloud.local access on all systems
   - Set up bookmarks/shortcuts
   - Test access from all systems

3. **Synchronization**
   - Set up automated sync from cloud providers
   - Configure sync schedules
   - Monitor sync status

---

## Implementation Plan

### Week 1: DSM Package Integration
- [ ] Access DSM Package Center
- [ ] Configure Cloud Sync package
- [ ] Add cloud storage providers
- [ ] Test cloud provider connections
- [ ] Set up initial sync tasks

### Week 2: Cloud.local Setup
- [ ] Configure DNS for cloud.local
- [ ] Set up reverse proxy
- [ ] Configure SSL certificate
- [ ] Test cloud.local access
- [ ] Set up SMB/NFS shares

### Week 3: Data Migration - KAIJU_NO_8
- [ ] Identify large files on KAIJU_NO_8
- [ ] Create migration plan
- [ ] Begin Phase 1 migration (large media)
- [ ] Verify migrated data
- [ ] Update application paths

### Week 4: Data Migration - MILLENNIUM_FALC
- [ ] Identify large files on MILLENNIUM_FALC
- [ ] Create migration plan
- [ ] Begin Phase 1 migration
- [ ] Verify migrated data
- [ ] Update application paths

### Week 5: Homelab Integration
- [ ] Map NAS drives on all systems
- [ ] Configure cloud.local access
- [ ] Test from all systems
- [ ] Set up automated sync
- [ ] Document configuration

---

## Scripts and Tools

### Available Scripts
1. **DSM Integration**
   - `nas_dsm_cloud_storage_setup.py` - DSM cloud storage setup
   - `migrate_cloud_storage_to_dsm_nas.py` - Cloud to NAS migration
   - `configure_all_dsm_packages_full_auto.py` - Auto-configure DSM packages

2. **Migration Management**
   - `complete_nas_migration_integration.py` - Comprehensive migration plan
   - `resume_nas_migration_initiative.py` - Resume interrupted migrations
   - `jarvis_nas_migration_manager.py` - JARVIS migration manager
   - `execute_nas_migration.py` - Execute migration tasks

3. **Monitoring**
   - `automated_nas_migration_monitor.py` - Monitor migration progress
   - `watch_nas_migration_live.py` - Live migration monitoring
   - `nas_migration_status.py` - Check migration status

### Usage Examples

```bash
# Generate comprehensive migration plan
python scripts/python/complete_nas_migration_integration.py --full-plan

# Check DSM package status
python scripts/python/nas_dsm_cloud_storage_setup.py --check-packages

# Resume migration initiative
python scripts/python/resume_nas_migration_initiative.py

# Monitor migration progress
python scripts/python/automated_nas_migration_monitor.py
```

---

## Cursor IDE Integration Note

**Important:** While completing NAS migration, ensure Cursor IDE chat history is handled properly:

1. **Option A:** Keep Cursor IDE data local (recommended for performance)
   - Exclude from Dropbox sync
   - Use local cache
   - Better performance

2. **Option B:** Move to NAS with optimization
   - Use local cache for active sessions
   - Archive old sessions to NAS
   - Set up symlinks for seamless access

3. **Option C:** Hybrid approach
   - Active chat history: Local
   - Archived chat history: NAS
   - Automatic archiving after 30 days

---

## Success Criteria

- ✅ DSM cloud storage package fully integrated
- ✅ Cloud.local system accessible from all homelab systems
- ✅ Multiple cloud providers syncing to NAS
- ✅ Large files migrated from KAIJU_NO_8 and MILLENNIUM_FALC
- ✅ Local disk space freed up significantly
- ✅ All homelab systems can access cloud.local
- ✅ Automated sync configured and working
- ✅ Data integrity verified after migration

---

## Next Steps

1. **Immediate:** Access DSM Package Center and configure Cloud Sync
2. **Short-term:** Set up cloud.local DNS and reverse proxy
3. **Medium-term:** Begin data migration from KAIJU_NO_8
4. **Long-term:** Complete migration and homelab integration

---

## Related Documentation

- [NAS Storage Bottleneck Action Plan](./NAS_STORAGE_BOTTLENECK_ACTION_PLAN.md)
- [Cursor Chat History Troubleshooting](./CURSOR_CHAT_HISTORY_TROUBLESHOOTING.md)
- NAS Infrastructure Architecture (if available)
- DSM Package Configuration Guides

---

**Last Updated:** January 9, 2025  
**Request ID:** 7eed9d32-9d75-4fb0-aefd-4a86fb0eff85  
**Status:** Ready for Implementation
