# DHCP Configuration: pfSense Primary, NAS Fallback

**Status:** ⚠️ **REQUIRES MANUAL CONFIGURATION**  
**Date:** 2026-01-16  
**Priority:** 🔴 **CRITICAL - Network Infrastructure**

---

## 🎯 Overview

Configure DHCP with:
- **Primary DHCP:** pfSense (10.17.17.1)
- **Fallback DHCP:** NAS (10.17.17.32)

This ensures network availability even if pfSense DHCP fails.

---

## 📋 Configuration Summary

### Network Settings
- **Subnet:** 10.17.17.0/24
- **Gateway:** 10.17.17.1 (pfSense)
- **Primary DNS:** 10.17.17.1 (pfSense)
- **Secondary DNS:** 10.17.17.32 (NAS)
- **DHCP Range:** 10.17.17.100 - 10.17.17.200
- **Lease Time:** 86400 seconds (24 hours)

---

## 🔧 Step 1: Configure pfSense as PRIMARY DHCP

### Access pfSense Web Portal
1. Open browser: **https://10.17.17.1**
2. Login with credentials from Azure Key Vault: `pfsense-password`

### Navigate to DHCP Server
1. Go to: **Services > DHCP Server**
2. Select the interface (typically **LAN**)

### Configure DHCP Settings
Enable and configure the following:

```
✅ Enable DHCP server on LAN interface
   Subnet: 10.17.17.0/24
   Subnet mask: 255.255.255.0
   
   Range:
   From: 10.17.17.100
   To: 10.17.17.200
   
   Gateway: 10.17.17.1
   
   DNS Servers:
   Primary: 10.17.17.1
   Secondary: 10.17.17.32
   
   Lease Time: 86400 (24 hours)
```

### Additional Settings
- **Domain:** (optional) `local`
- **Domain Search List:** (optional)
- **MAC Address Control:** (optional) Configure static IPs if needed

### Save and Apply
1. Click **Save**
2. Click **Apply Changes**
3. Verify DHCP service is running

### Verify pfSense DHCP
```bash
# SSH to pfSense (if SSH is enabled)
ssh admin@10.17.17.1

# Check DHCP service
ps aux | grep dhcpd | grep -v grep

# Check DHCP leases
cat /var/dhcpd/var/db/dhcpd.leases
```

---

## 🔧 Step 2: Configure NAS as FALLBACK DHCP

### Access NAS Web Portal
1. Open browser: **https://10.17.17.32:5001**
2. Login with credentials from Azure Key Vault: `nas-password`

### Install DHCP Server Package (if not installed)
1. Go to: **Package Center**
2. Search for: **DHCP Server**
3. Click **Install**
4. Wait for installation to complete

### Configure DHCP Server
1. Open **DHCP Server** application
2. Go to **Settings** or **Network Interface**

### Configure DHCP Settings
**IMPORTANT:** Configure NAS DHCP as **FALLBACK ONLY**

```
⚠️  CRITICAL: Only enable NAS DHCP if pfSense DHCP fails
   This is a FALLBACK configuration, not primary

✅ Enable DHCP server (FALLBACK MODE)
   Subnet: 10.17.17.0/24
   Subnet mask: 255.255.255.0
   
   Range:
   From: 10.17.17.100
   To: 10.17.17.200
   
   Gateway: 10.17.17.1
   
   DNS Servers:
   Primary: 10.17.17.1
   Secondary: 10.17.17.32
   
   Lease Time: 86400 (24 hours)
```

### Configure Failover Behavior
**Option A: Disable NAS DHCP (Recommended)**
- Keep NAS DHCP **DISABLED** by default
- Only enable manually if pfSense DHCP fails
- This prevents DHCP conflicts

**Option B: Configure Different Range (Alternative)**
- If both must run simultaneously, use different ranges:
  - pfSense: 10.17.17.100 - 10.17.17.150
  - NAS: 10.17.17.151 - 10.17.17.200
- **NOT RECOMMENDED** - Can cause conflicts

### Save Configuration
1. Click **Apply** or **Save**
2. Verify DHCP service status

### Verify NAS DHCP
```bash
# SSH to NAS
ssh backupadm@10.17.17.32

# Check DHCP service status
synoservice --status dhcpd

# Check DHCP Server package
synopkg list | grep -i dhcp
```

---

## 🔍 Step 3: Verify DHCP Configuration

### Test DHCP from Client
1. Connect a test device to the network
2. Release and renew IP:
   ```bash
   # Windows
   ipconfig /release
   ipconfig /renew
   
   # Linux/Mac
   sudo dhclient -r
   sudo dhclient
   ```
3. Verify IP assignment:
   ```bash
   # Windows
   ipconfig /all
   
   # Linux/Mac
   ip addr show
   ```
4. Check DNS resolution:
   ```bash
   nslookup google.com
   ```

### Verify DHCP Leases
**pfSense:**
- Web UI: **Status > DHCP Leases**
- SSH: `cat /var/dhcpd/var/db/dhcpd.leases`

**NAS:**
- Web UI: **DHCP Server > Leases**
- SSH: Check DHCP Server logs

### Test Failover (Optional)
1. Temporarily disable pfSense DHCP
2. Verify NAS DHCP takes over
3. Re-enable pfSense DHCP
4. Verify clients switch back

---

## ⚠️ Important Notes

### DHCP Conflict Prevention
- **DO NOT** run both DHCP servers simultaneously with overlapping ranges
- **RECOMMENDED:** Keep NAS DHCP disabled, enable only if pfSense fails
- If both must run, use **non-overlapping ranges**

### Best Practice
1. **pfSense DHCP:** PRIMARY (always enabled)
2. **NAS DHCP:** FALLBACK (disabled by default, enable manually if needed)

### Monitoring
- Monitor DHCP lease counts
- Check for DHCP conflicts in logs
- Verify DNS resolution from clients
- Monitor network connectivity

---

## 🛠️ Troubleshooting

### pfSense DHCP Not Working
1. Check DHCP service status
2. Verify interface configuration
3. Check firewall rules
4. Review DHCP logs: **Status > System Logs > DHCP**

### NAS DHCP Not Working
1. Verify DHCP Server package is installed
2. Check service status: `synoservice --status dhcpd`
3. Review package logs
4. Verify network interface configuration

### DHCP Conflicts
- Only one DHCP server should be active per subnet
- Disable NAS DHCP if pfSense is working
- Use different ranges if both must run

### Clients Not Getting IPs
1. Check DHCP service is running
2. Verify DHCP range is correct
3. Check for IP conflicts
4. Verify network connectivity
5. Check firewall rules

---

## 📊 Configuration Script

The automated configuration script is available:
```bash
python scripts/python/configure_dhcp_pfsense_primary_nas_fallback.py
```

**Note:** Script requires SSH access to both systems. If SSH is not available, use manual configuration above.

---

## ✅ Success Criteria

- ✅ pfSense DHCP is enabled and running
- ✅ NAS DHCP is configured as fallback (disabled by default)
- ✅ Clients receive IPs from pfSense DHCP
- ✅ DNS resolution works correctly
- ✅ Network connectivity is stable
- ✅ Failover can be tested manually if needed

---

## 📝 Configuration Checklist

- [ ] pfSense DHCP enabled and configured
- [ ] NAS DHCP Server package installed
- [ ] NAS DHCP configured as fallback (disabled)
- [ ] DHCP range configured correctly
- [ ] DNS servers configured correctly
- [ ] Gateway configured correctly
- [ ] DHCP leases verified
- [ ] Client connectivity tested
- [ ] DNS resolution tested
- [ ] Failover procedure documented

---

**Last Updated:** 2026-01-16  
**Status:** ⚠️ **REQUIRES MANUAL CONFIGURATION**  
**Next Steps:** Complete manual configuration via web UIs
