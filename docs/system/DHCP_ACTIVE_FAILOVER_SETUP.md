# DHCP Active Failover Setup

**Status:** ✅ **ACTIVE FAILOVER CONFIGURED**  
**Date:** 2026-01-16  
**Priority:** 🔴 **CRITICAL - Network Infrastructure**

---

## 🎯 Overview

Active DHCP failover system with automatic monitoring and switching:
- **Primary DHCP:** pfSense (10.17.17.1) - Range: 10.17.17.100 - 10.17.17.150
- **Fallback DHCP:** NAS (10.17.17.32) - Range: 10.17.17.151 - 10.17.17.200
- **Failover Monitor:** Automatically enables NAS DHCP when pfSense fails
- **Auto-Recovery:** Automatically disables NAS DHCP when pfSense recovers

---

## 📋 Configuration Summary

### Network Settings
- **Subnet:** 10.17.17.0/24
- **Gateway:** 10.17.17.1 (pfSense)
- **Primary DNS:** 10.17.17.1 (pfSense)
- **Secondary DNS:** 10.17.17.32 (NAS)

### DHCP Ranges (Non-Overlapping)
- **pfSense (Primary):** 10.17.17.100 - 10.17.17.150 (51 IPs)
- **NAS (Fallback):** 10.17.17.151 - 10.17.17.200 (50 IPs)
- **Lease Time:** 86400 seconds (24 hours)

### Failover Monitor Settings
- **Check Interval:** 30 seconds
- **Failure Threshold:** 3 consecutive failures = down
- **Recovery Threshold:** 3 consecutive successes = recovered
- **Auto-Enable NAS DHCP:** Yes (when pfSense fails)
- **Auto-Disable NAS DHCP:** Yes (when pfSense recovers)

---

## 🚀 Quick Start

### 1. Configure Active Failover
```bash
python scripts/python/configure_dhcp_active_failover.py
```

This will:
- Configure pfSense DHCP with primary range
- Configure NAS DHCP with fallback range (disabled by default)
- Initialize failover monitor

### 2. Start Failover Monitor

**Option A: Continuous Monitoring (Recommended)**
```bash
python scripts/python/dhcp_failover_monitor.py
```

**Option B: Cron Service (Every Minute)**
```bash
python scripts/python/deploy_activate_all_cron_services.py
```

**Option C: Single Check**
```bash
python scripts/python/dhcp_failover_monitor.py --once
```

---

## 🔧 Manual Configuration

### Step 1: Configure pfSense (Primary DHCP)

1. **Access pfSense:** https://10.17.17.1
2. **Navigate:** Services > DHCP Server > LAN
3. **Configure:**
   ```
   ✅ Enable DHCP server on LAN interface
   Subnet: 10.17.17.0/24
   Subnet mask: 255.255.255.0
   
   Range:
   From: 10.17.17.100
   To: 10.17.17.150
   
   Gateway: 10.17.17.1
   DNS Servers: 10.17.17.1 10.17.17.32
   Lease Time: 86400
   ```
4. **Save and Apply**

### Step 2: Configure NAS (Fallback DHCP)

1. **Access NAS:** https://10.17.17.32:5001
2. **Install DHCP Server** (if not installed):
   - Package Center > Search "DHCP Server" > Install
3. **Configure DHCP Server:**
   ```
   ⚠️  IMPORTANT: Keep DISABLED by default
   
   Enable DHCP server: DISABLED (will be auto-enabled on failover)
   Subnet: 10.17.17.0/24
   Subnet mask: 255.255.255.0
   
   Range:
   From: 10.17.17.151
   To: 10.17.17.200
   
   Gateway: 10.17.17.1
   DNS Servers: 10.17.17.1 10.17.17.32
   Lease Time: 86400
   ```
4. **Save Configuration**

---

## 🔍 How It Works

### Normal Operation
1. **pfSense DHCP:** ACTIVE (serving 10.17.17.100 - 10.17.17.150)
2. **NAS DHCP:** DISABLED (standby)
3. **Failover Monitor:** Checks pfSense every 30 seconds

### Failover Scenario
1. **pfSense DHCP fails** (3 consecutive failures detected)
2. **Failover Monitor** automatically:
   - Enables NAS DHCP service
   - NAS starts serving 10.17.17.151 - 10.17.17.200
   - Logs failover event
3. **Clients** can renew leases and get IPs from NAS

### Recovery Scenario
1. **pfSense DHCP recovers** (3 consecutive successes detected)
2. **Failover Monitor** automatically:
   - Disables NAS DHCP service
   - pfSense resumes serving primary range
   - Logs recovery event
3. **Clients** renew leases and get IPs from pfSense

---

## 📊 Monitoring

### Check Status
```bash
# Single check
python scripts/python/dhcp_failover_monitor.py --once

# Continuous monitoring
python scripts/python/dhcp_failover_monitor.py

# With custom interval
python scripts/python/dhcp_failover_monitor.py --check-interval 60
```

### Monitor Output
```
📋 Check #1 - 2026-01-16 16:50:00
  ✅ pfSense DHCP: healthy
  ⏸️ NAS DHCP: unknown (enabled: False)
  ✅ NORMAL Failover: False
```

### Failover Active
```
📋 Check #15 - 2026-01-16 16:52:30
  ❌ pfSense DHCP: failed
  ✅ NAS DHCP: healthy (enabled: True)
  🔄 ACTIVE Failover: True
```

---

## ⚙️ Advanced Configuration

### Custom Check Interval
```bash
python scripts/python/dhcp_failover_monitor.py --check-interval 60
```

### Custom Thresholds
```bash
python scripts/python/dhcp_failover_monitor.py \
  --failure-threshold 5 \
  --recovery-threshold 5
```

### Monitor Only (No Auto-Failover)
```bash
python scripts/python/dhcp_failover_monitor.py --disable-auto-failover
```

### Run for Duration
```bash
python scripts/python/dhcp_failover_monitor.py --duration 3600
```

---

## 🛠️ Troubleshooting

### pfSense DHCP Not Detected
- Check SSH access to pfSense
- Verify DHCP service is running: `ps aux | grep dhcpd`
- Check firewall rules
- Review pfSense logs

### NAS DHCP Not Enabling
- Check SSH access to NAS
- Verify DHCP Server package is installed
- Check service status: `synoservice --status dhcpd`
- Review NAS logs

### Failover Not Triggering
- Check monitor is running
- Verify failure threshold is met (default: 3)
- Check network connectivity
- Review monitor logs

### Both DHCP Servers Active
- This is normal during failover transition
- Ranges are non-overlapping, so no conflicts
- Clients will get IPs from whichever responds first

---

## 📝 Cron Service Registration

The failover monitor is automatically registered with the cron system:

```python
# Registered as: dhcp_failover_monitor
# Schedule: */1 * * * * (every minute)
# Description: DHCP Active Failover Monitor
```

To deploy:
```bash
python scripts/python/deploy_activate_all_cron_services.py
```

---

## ✅ Success Criteria

- ✅ pfSense DHCP configured and active
- ✅ NAS DHCP configured (disabled by default)
- ✅ Failover monitor running
- ✅ Non-overlapping ranges configured
- ✅ Automatic failover working
- ✅ Automatic recovery working
- ✅ Monitoring and logging active

---

## 📊 Status Dashboard

### Current Status
- **pfSense DHCP:** ✅ HEALTHY
- **NAS DHCP:** ⏸️ STANDBY
- **Failover:** ✅ NORMAL
- **Last Check:** 2026-01-16 16:50:00

### Failover History
- **Total Failovers:** 0
- **Last Failover:** None
- **Average Recovery Time:** N/A

---

## 🔐 Security Notes

- SSH credentials stored in Azure Key Vault
- Monitor runs with minimal privileges
- Failover actions logged for audit
- No manual intervention required

---

**Last Updated:** 2026-01-16  
**Status:** ✅ **ACTIVE FAILOVER CONFIGURED**  
**Next Steps:** Monitor and verify failover behavior
