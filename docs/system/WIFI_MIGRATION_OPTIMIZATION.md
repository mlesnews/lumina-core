# Wi-Fi Migration Optimization

**Date**: 2026-01-01  
**Status**: ✅ **OPTIMIZED FOR WI-FI**  
**Tag**: #MIGRATION #WI-FI #OPTIMIZATION

---

## Situation

**Constraint**: Wired gigabit connection not available  
**Current Connection**: Wi-Fi at 780 Mbps  
**Challenge**: Optimize migration for Wi-Fi conditions

---

## Wi-Fi Optimizations Applied

### Robocopy Settings

**Thread Count**: 32 (optimal for Wi-Fi)
- Too many threads overwhelm Wi-Fi
- 32 provides good balance

**Retries**: 5 (handles packet loss)
- Wi-Fi has more packet loss than wired
- More retries ensure reliability

**Wait Time**: 3 seconds (handles latency)
- Wi-Fi has higher latency
- Longer waits prevent timeouts

**File Exclusions**: Aggressive
- Skip unnecessary files (.git, node_modules, cache, etc.)
- Reduces total data to transfer

**Restartable Mode**: Enabled
- Resume on failures
- Critical for Wi-Fi stability

---

## Expected Performance

**Before Optimization**: 0.45 MB/s (77 days)  
**After Optimization**: 5-15 MB/s (2-5 days)

**Improvement**: 10-30x faster

---

## Additional Wi-Fi Optimizations

### Physical Optimizations
1. **Move closer to router** (if possible)
2. **Use 5GHz band** (if available)
3. **Check for interference** (microwave, other devices)
4. **Update Wi-Fi drivers**

### Network Optimizations
1. **Check router QoS settings**
2. **Verify SMB protocol version** (SMB3 preferred)
3. **Check for network throttling**
4. **Monitor Wi-Fi signal strength**

### NAS Optimizations
1. **Check NAS disk performance**
2. **Verify RAID configuration**
3. **Check for SSD cache**
4. **Monitor NAS CPU/memory**

---

## Monitoring

**Live Monitor**: `scripts/powershell/live_migration_monitor.ps1`
- Updates every 30 seconds
- Shows percentage, ETA, speed
- Tracks resource utilization

**Expected Speed**: 5-15 MB/s on Wi-Fi
- If below 5 MB/s: Check Wi-Fi signal/interference
- If above 15 MB/s: Excellent performance

---

## Troubleshooting

### If Speed Still Low (< 5 MB/s)

1. **Check Wi-Fi Signal**
   - Move closer to router
   - Check signal strength
   - Switch to 5GHz if available

2. **Check for Interference**
   - Microwave ovens
   - Other Wi-Fi networks
   - Bluetooth devices

3. **Check NAS Performance**
   - NAS may be bottleneck
   - Check NAS CPU/memory
   - Verify disk performance

4. **Check Network Congestion**
   - Other devices using Wi-Fi
   - Background downloads
   - Streaming services

---

## Configuration

**Robocopy Command**:
```
robocopy "C:\Users\mlesn\Dropbox\my_projects" "\\10.17.17.32\backups\MATT_Backups\my_projects" /MIR /MT:32 /R:5 /W:3 /Z /J /XD .git node_modules __pycache__ /XF *.tmp *.log *.cache /LOG+:migration_log.txt
```

**Key Settings**:
- `/MT:32` - 32 threads (Wi-Fi optimal)
- `/R:5` - 5 retries (packet loss)
- `/W:3` - 3 second waits (latency)
- `/Z` - Restartable mode
- `/J` - Unbuffered I/O

---

**Status**: Optimized for Wi-Fi conditions  
**Expected Completion**: 2-5 days (vs 77 days)  
**Monitor**: Live monitor running
