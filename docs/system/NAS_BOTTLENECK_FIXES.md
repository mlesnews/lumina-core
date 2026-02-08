# NAS Bottleneck Fixes - STORAGE TEAM

**Date**: 2026-01-01  
**Priority**: 🔴 **HIGH**  
**Tag**: #MIGRATION #NAS #STORAGE-TEAM

---

## Problem

**Migration Speed**: 0.45 MB/s (EXTREMELY SLOW)  
**WiFi Speed**: 780 Mbps (NOT the bottleneck)  
**Actual Issue**: Likely NAS performance bottleneck

---

## NAS-Side Checks Required

### 1. Disk Performance

**Check:**
- RAID configuration (RAID 0, 1, 5, 6, 10?)
- Disk type (HDD, SSD, hybrid?)
- Disk health status
- Disk fragmentation

**Actions:**
- Verify RAID is optimal for write performance
- Check if disks are healthy
- Consider SSD cache if available
- Defragment if needed

### 2. SSD Cache

**Check:**
- Is SSD cache enabled?
- Cache size and utilization
- Cache hit rate

**Actions:**
- Enable SSD cache if available
- Increase cache size if possible
- Monitor cache performance

### 3. NAS CPU/Memory

**Check:**
- CPU utilization during migration
- Memory utilization
- Other processes consuming resources

**Actions:**
- Monitor during migration
- Disable unnecessary services
- Free up resources if needed

### 4. SMB Protocol

**Check:**
- SMB version (SMB3 preferred)
- SMB multichannel enabled?
- SMB encryption (may slow down)

**Actions:**
- Enable SMB3 if available
- Enable SMB multichannel
- Disable encryption if not needed (for speed)

### 5. Network Settings

**Check:**
- Jumbo frames enabled?
- MTU size
- Network interface speed

**Actions:**
- Enable jumbo frames if supported
- Optimize MTU size
- Verify network interface speed

---

## Quick Fixes to Try

### On NAS (via DSM or SSH):

1. **Disable unnecessary services during migration:**
   ```
   - Media indexing
   - Cloud sync (temporarily)
   - Antivirus scanning
   - Other background tasks
   ```

2. **Enable SMB3 and multichannel:**
   ```
   Control Panel > File Services > SMB
   - Enable SMB3
   - Enable SMB multichannel
   ```

3. **Check disk performance:**
   ```
   Storage Manager > Check disk health
   Storage Manager > Check RAID status
   ```

4. **Enable SSD cache:**
   ```
   Storage Manager > SSD Cache
   - Enable if available
   - Allocate maximum cache
   ```

5. **Optimize network:**
   ```
   Control Panel > Network > Network Interface
   - Check link speed
   - Enable jumbo frames if supported
   ```

---

## Expected Impact

**If NAS is the bottleneck:**
- Fixing NAS performance could improve speed 10-50x
- Expected speed: 10-50 MB/s (vs 0.45 MB/s)
- Completion: 1-3 days (vs 77 days)

---

## Testing

**Test NAS write speed:**
```powershell
# From Windows client
$testFile = "\\10.17.17.32\backups\MATT_Backups\speed_test.tmp"
$testSize = 100MB
$testData = New-Object byte[] $testSize
$start = Get-Date
[System.IO.File]::WriteAllBytes($testFile, $testData)
$end = Get-Date
$speed = ($testSize / 1MB) / ($end - $start).TotalSeconds
Write-Host "NAS Write Speed: $speed MB/s"
```

**Expected**: 50+ MB/s for good NAS performance  
**Current**: Likely < 5 MB/s (bottleneck)

---

## Priority Actions

1. **IMMEDIATE**: Check NAS disk performance
2. **IMMEDIATE**: Verify SSD cache enabled
3. **HIGH**: Enable SMB3 multichannel
4. **MEDIUM**: Disable unnecessary services
5. **LOW**: Optimize network settings

---

**Contact**: STORAGE TEAM  
**NAS IP**: 10.17.17.32  
**Share**: \\10.17.17.32\backups\MATT_Backups
