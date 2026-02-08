# DSM Cloud Sync Setup Guide (REQUIRED)

**Date**: 2026-01-01  
**Status**: 🔴 **REQUIRED** - Must be set up after migration  
**Tag**: #NAS #CLOUD-SYNC #BACKUP #REQUIRED

---

## 🎯 Purpose

**DSM Cloud Sync is REQUIRED** to provide cloud backup redundancy for NAS data. This ensures:
- ✅ Off-site backup protection
- ✅ Data redundancy (NAS + Cloud)
- ✅ Disaster recovery capability
- ✅ Selective sync (only critical data)

---

## 📋 Prerequisites

- ✅ NAS accessible at `10.17.17.32`
- ✅ DSM (Synology DiskStation Manager) access
- ✅ Cloud provider account (Dropbox, OneDrive, Google Drive, etc.)
- ✅ my_projects migration completed (or in progress)

---

## 🔧 Setup Steps

### Step 1: Access DSM

1. **Open DSM Web Interface**:
   ```
   http://10.17.17.32:5000
   ```

2. **Login** with administrator credentials

### Step 2: Install Cloud Sync Package

1. **Open Package Center**
2. **Search for**: "Cloud Sync"
3. **Install**: Cloud Sync package
4. **Wait** for installation to complete

### Step 3: Configure Cloud Provider

#### Option A: Dropbox (Recommended - Familiar)

1. **Open Cloud Sync**
2. **Click**: "Add" or "+"
3. **Select**: "Dropbox"
4. **Authorize**: Sign in to Dropbox account
5. **Grant permissions**: Allow Cloud Sync access

#### Option B: OneDrive

1. **Select**: "OneDrive"
2. **Authorize**: Sign in to Microsoft account
3. **Grant permissions**: Allow Cloud Sync access

#### Option C: Google Drive

1. **Select**: "Google Drive"
2. **Authorize**: Sign in to Google account
3. **Grant permissions**: Allow Cloud Sync access

### Step 4: Configure Sync Task

**Task Name**: `LUMINA_Projects_Backup`

**Local Path** (on NAS):
```
/volume1/backups/MATT_Backups/my_projects
```

**Remote Path** (in cloud):
```
/LUMINA_Backups/my_projects
```

**Sync Direction**: 
- ✅ **One-way (Upload only)** - Recommended
- NAS → Cloud (backup only, no cloud → NAS sync)

**Sync Mode**:
- ✅ **Selective Sync** - Only sync critical files
- Exclude large files (videos, models, etc.)

### Step 5: Configure Selective Sync

**Include** (sync these):
- ✅ `.lumina/` - LUMINA project files
- ✅ `config/` - Configuration files
- ✅ `scripts/` - Script files
- ✅ `docs/` - Documentation
- ✅ `*.json`, `*.yaml`, `*.yml` - Config files
- ✅ `*.md` - Documentation files
- ✅ `*.py`, `*.ps1`, `*.sh` - Script files

**Exclude** (don't sync):
- ❌ `data/` - Large data directories
- ❌ `node_modules/` - Dependencies
- ❌ `__pycache__/` - Python cache
- ❌ `*.mp4`, `*.avi`, `*.mov` - Video files
- ❌ `*.model`, `*.bin` - Model files
- ❌ `*.zip`, `*.tar`, `*.gz` - Archives
- ❌ `*.log` - Log files

### Step 6: Schedule Sync

**Sync Schedule**:
- **Frequency**: Daily
- **Time**: 2:00 AM (low usage time)
- **Or**: Continuous (real-time sync)

**Bandwidth Limit** (optional):
- Set upload limit if needed
- Prevents network saturation

### Step 7: Verify Sync

1. **Check Sync Status**: Cloud Sync dashboard
2. **Verify Files**: Check cloud provider
3. **Test Restore**: Verify can restore from cloud
4. **Monitor**: Check sync logs

---

## 📊 Configuration Summary

### Sync Task Configuration

```yaml
Task Name: LUMINA_Projects_Backup
Provider: Dropbox (or OneDrive/Google Drive)
Local Path: /volume1/backups/MATT_Backups/my_projects
Remote Path: /LUMINA_Backups/my_projects
Direction: One-way (Upload only)
Mode: Selective Sync
Schedule: Daily at 2:00 AM
```

### Include Patterns

```
.lumina/**
config/**
scripts/**
docs/**
*.json
*.yaml
*.yml
*.md
*.py
*.ps1
*.sh
```

### Exclude Patterns

```
data/**
node_modules/**
__pycache__/**
*.mp4
*.avi
*.mov
*.model
*.bin
*.zip
*.tar
*.gz
*.log
```

---

## 🔍 Verification Checklist

- [ ] Cloud Sync package installed
- [ ] Cloud provider connected
- [ ] Sync task created
- [ ] Selective sync configured
- [ ] Include/exclude patterns set
- [ ] Sync schedule configured
- [ ] Initial sync completed
- [ ] Files verified in cloud
- [ ] Sync logs checked
- [ ] Restore test successful

---

## 🛠️ Troubleshooting

### Sync Not Starting

**Issue**: Sync task not running

**Solutions**:
1. Check Cloud Sync service is running
2. Verify cloud provider connection
3. Check NAS storage space
4. Review sync logs for errors

### Slow Sync Speed

**Issue**: Sync taking too long

**Solutions**:
1. Check network bandwidth
2. Reduce file count (more exclusions)
3. Schedule sync during off-hours
4. Increase bandwidth limit

### Files Not Syncing

**Issue**: Expected files not in cloud

**Solutions**:
1. Check include/exclude patterns
2. Verify file paths are correct
3. Check file permissions
4. Review sync logs

### Cloud Storage Full

**Issue**: Cloud provider storage limit reached

**Solutions**:
1. Add more exclusions (large files)
2. Upgrade cloud storage plan
3. Archive old files
4. Use multiple cloud providers

---

## 📝 Post-Setup Tasks

### 1. Monitor Initial Sync

```powershell
# Check sync status via DSM API or web interface
# Monitor until initial sync completes
```

### 2. Verify Critical Files

```powershell
# Verify key files are in cloud:
# - .lumina/config files
# - scripts
# - documentation
```

### 3. Test Restore

```powershell
# Test restoring a file from cloud
# Verify restore process works
```

### 4. Document Configuration

- Document cloud provider used
- Document sync schedule
- Document include/exclude patterns
- Document restore procedures

---

## 🚀 Quick Setup Commands

### Via DSM Web Interface

1. **Access**: `http://10.17.17.32:5000`
2. **Package Center** → Install "Cloud Sync"
3. **Cloud Sync** → Add → Select provider
4. **Configure** sync task
5. **Start** sync

### Via SSH (if available)

```bash
# Check if Cloud Sync is installed
synopkg list | grep CloudSync

# Check Cloud Sync status
synopkg status CloudSync
```

---

## ✅ Success Criteria

- [ ] Cloud Sync installed and running
- [ ] Cloud provider connected
- [ ] Sync task created and active
- [ ] Selective sync configured correctly
- [ ] Initial sync completed
- [ ] Critical files verified in cloud
- [ ] Sync schedule working
- [ ] Restore test successful

---

## 📚 Related Documentation

- [NAS Data Centralization Guide](../NAS_DATA_CENTRALIZATION_GUIDE.md)
- [LUMINA Dropbox to NAS Migration](./LUMINA_DROPBOX_TO_NAS_MIGRATION.md)
- [NAS Migration Plan](../NAS_MIGRATION_PLAN_PM000003051.md)

---

**Last Updated**: 2026-01-01  
**Maintained By**: @JARVIS  
**Status**: 🔴 REQUIRED - Must be completed after migration
