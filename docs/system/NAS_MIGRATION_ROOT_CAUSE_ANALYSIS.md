# NAS Migration Root Cause Analysis & Solutions

**Date**: 2026-01-02  
**Status**: 🔴 BLOCKED - Multiple root causes identified

## Root Causes Identified

### 1. **Permission Issue: CIFS Mount Requires Root** ❌
**Problem**: The migration script runs as `backupadm` user, but `mount -t cifs` requires root privileges on Synology NAS.

**Evidence**:
```bash
mount: only root can use "--options" option
```

**Impact**: SMB mounting fails silently, migration cannot proceed.

### 2. **Ping Permission Denied** ❌
**Problem**: User `backupadm` cannot run ping without root/sudo.

**Evidence**:
```bash
ping: socket: Operation not permitted
sudo: a password is required
```

**Impact**: Connectivity checks fail, script thinks laptop is offline.

### 3. **Sudo Requires Password** ❌
**Problem**: Even if we add `sudo` to commands, it requires a password (not passwordless).

**Evidence**:
```bash
sudo: a password is required
```

**Impact**: Cannot elevate privileges to mount CIFS or ping.

### 4. **Wrong Migration Direction** ⚠️
**Current**: NAS pulls from laptop (requires NAS to mount Windows share)  
**Better**: Laptop pushes to NAS (uses Windows capabilities, NAS just receives)

---

## @PEAK Solutions (Ranked by Viability)

### Solution 1: Reverse Migration Direction (PUSH FROM WINDOWS) ⭐⭐⭐⭐⭐
**Viability**: HIGHEST  
**Complexity**: LOW  
**Reliability**: HIGH

**Approach**: Run migration script on Windows laptop that pushes files to NAS.

**Advantages**:
- ✅ Windows has native SMB/NAS access
- ✅ No root privileges needed
- ✅ Can use robocopy (native Windows tool)
- ✅ Works with Windows firewall
- ✅ Can schedule with Windows Task Scheduler
- ✅ Survives laptop reboots if scheduled

**Implementation**:
1. Create PowerShell script on laptop
2. Use `robocopy` or `rsync` to push to NAS SMB share
3. Schedule with Windows Task Scheduler
4. NAS just receives files (no mounting needed)

**Status**: ✅ RECOMMENDED PRIMARY SOLUTION

---

### Solution 2: Enable SSH/rsync on Windows ⭐⭐⭐⭐
**Viability**: HIGH  
**Complexity**: MEDIUM  
**Reliability**: HIGH

**Approach**: Enable OpenSSH Server on Windows, use rsync over SSH.

**Advantages**:
- ✅ No root/sudo needed
- ✅ Works across networks
- ✅ Native rsync support
- ✅ Secure (SSH encryption)

**Requirements**:
- Windows OpenSSH Server enabled
- SSH key authentication configured
- rsync installed on Windows (or use robocopy via SSH)

**Implementation**:
1. Enable OpenSSH Server on Windows
2. Configure key-based authentication
3. Install rsync on Windows (or use robocopy)
4. Update NAS script to use SSH rsync method

**Status**: ✅ VIABLE ALTERNATIVE

---

### Solution 3: Configure Passwordless Sudo for CIFS ⭐⭐⭐
**Viability**: MEDIUM  
**Complexity**: MEDIUM  
**Reliability**: MEDIUM

**Approach**: Configure `/etc/sudoers` to allow passwordless sudo for specific mount commands.

**Advantages**:
- ✅ Keeps current pull-based architecture
- ✅ Minimal script changes

**Requirements**:
- Root/sudo access to NAS to edit sudoers
- Security considerations (limited sudo access)

**Implementation**:
```bash
# On NAS as root:
echo "backupadm ALL=(ALL) NOPASSWD: /bin/mount, /bin/umount, /bin/ping" >> /etc/sudoers
```

**Status**: ⚠️ REQUIRES ROOT ACCESS TO NAS

---

### Solution 4: Use NAS User with Appropriate Permissions ⭐⭐
**Viability**: LOW  
**Complexity**: HIGH  
**Reliability**: LOW

**Approach**: Create/use a NAS user that can mount shares (may require NAS admin panel configuration).

**Status**: ❌ UNLIKELY - Synology typically requires root for mounts

---

### Solution 5: Use Synology Built-in Backup Tools ⭐⭐⭐
**Viability**: MEDIUM  
**Complexity**: LOW  
**Reliability**: HIGH

**Approach**: Use Synology Hyper Backup or Active Backup to pull from Windows.

**Advantages**:
- ✅ Native Synology tool
- ✅ Handles permissions automatically
- ✅ Built-in scheduling
- ✅ Reliable and tested

**Disadvantages**:
- ❌ Less customizable
- ❌ May not support custom paths easily

**Status**: ✅ VIABLE IF NEEDED

---

## Recommended Action Plan

### Immediate (Solution 1 - Reverse Direction):

1. **Create Windows PowerShell Push Script**:
   - Use `robocopy` to push from `C:\Users\mlesn\Dropbox\my_projects`
   - To NAS share: `\\10.17.17.32\backups\MATT_Backups\my_projects`
   - Include retry logic
   - Log to file

2. **Windows Task Scheduler**:
   - Schedule script to run periodically
   - Run whether user is logged in or not
   - High priority, retry on failure

3. **Status Monitoring**:
   - Create status file on NAS
   - Monitor from Python script
   - Integration with existing VA system

### Alternative (Solution 2 - SSH/rsync):

1. Enable Windows OpenSSH Server
2. Configure SSH keys
3. Update NAS script to use SSH rsync method
4. Test connectivity

---

## Implementation Priority

1. **PRIORITY 1**: Implement Solution 1 (Reverse - Push from Windows)
2. **PRIORITY 2**: Keep Solution 2 (SSH/rsync) as backup
3. **PRIORITY 3**: Document Solution 3 (Passwordless sudo) for future reference

---

## Notes

- User mentioned "sudoless root on nas" - need to verify if passwordless sudo is already configured
- Current NAS user: `backupadm`
- Current laptop IP: `10.17.17.191`
- NAS IP: `10.17.17.32`
- Destination: `/volume1/backups/MATT_Backups/my_projects`

---

**Next Steps**: Implement Solution 1 (Reverse Push Script) immediately.
