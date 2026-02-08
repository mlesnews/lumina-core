# IDM Firewall Configuration - Error 10061 Fix

**Date**: 2026-01-10  
**Issue**: Error 10061 - Connection Refused  
**Reference**: https://www.internetdownloadmanager.com/register/new_faq/How_to_configure_Firewalls_for_IDM.html

## Problem

Error 10061 indicates "Connection Refused" - IDM cannot connect to download sources because:
1. Windows Firewall is blocking IDM
2. Third-party firewall/antivirus is blocking IDM
3. HTTP server port (8888) is blocked

## Solution

### Quick Fix

Run the firewall configuration script **as Administrator**:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/startup/CONFIGURE_IDM_FIREWALL.ps1
```

This script will:
- ✅ Create inbound firewall rule for IDM
- ✅ Create outbound firewall rule for IDM
- ✅ Allow HTTP server port 8888
- ✅ Verify all rules are active

### Manual Configuration

#### Windows Firewall

1. Open Windows Defender Firewall
2. Click "Allow an app or feature through Windows Firewall"
3. Click "Change Settings" > "Allow another app"
4. Browse to `C:\Program Files (x86)\Internet Download Manager\IDMan.exe`
5. Check both "Private" and "Public" networks
6. Click "OK"

#### HTTP Server Port (8888)

1. Open Windows Defender Firewall
2. Click "Advanced Settings"
3. Click "Inbound Rules" > "New Rule"
4. Select "Port" > Next
5. Select "TCP" > "Specific local ports" > Enter "8888"
6. Select "Allow the connection"
7. Check all profiles (Domain, Private, Public)
8. Name: "IDM HTTP Server - Port 8888"
9. Click "Finish"

### Third-Party Firewall/Antivirus

If you have third-party security software:

1. **Avast/AVG**: Settings > Protection > Firewall > Application Rules > Add IDMan.exe
2. **Kaspersky**: Settings > Protection > Firewall > Applications > Add IDMan.exe
3. **Norton**: Settings > Firewall > Program Control > Add IDMan.exe
4. **McAfee**: Firewall > Program Permissions > Add IDMan.exe
5. **Windows Defender**: Add IDMan.exe to exclusions

### IDM Settings

1. Open IDM
2. Options > Connection
3. Check "Use proxy server" if behind proxy
4. Test connection
5. Options > Proxy/Firewall
6. Configure if needed

## Verification

After configuration, test:

```powershell
# Test HTTP server
Invoke-WebRequest -Uri "http://10.17.17.191:8888/" -Method Head -UseBasicParsing

# Test IDM download
& "C:\Program Files (x86)\Internet Download Manager\IDMan.exe" /n /d "http://example.com/test.zip" /p "C:\Downloads"
```

## Common Issues

### Error 10061
- **Cause**: Firewall blocking connection
- **Fix**: Configure firewall rules (see above)

### IDM Cannot Start Downloads
- **Cause**: Outbound rule missing
- **Fix**: Create outbound firewall rule

### HTTP Server Not Accessible
- **Cause**: Port 8888 blocked
- **Fix**: Allow port 8888 in firewall

### Downloads Start Then Stop
- **Cause**: Firewall blocking mid-download
- **Fix**: Ensure both inbound and outbound rules exist

## Additional Resources

- IDM Firewall FAQ: https://www.internetdownloadmanager.com/register/new_faq/How_to_configure_Firewalls_for_IDM.html
- Windows Firewall Documentation: https://support.microsoft.com/windows

---

**Status**: ✅ **FIREWALL CONFIGURATION SCRIPT CREATED**  
**Script**: `scripts/startup/CONFIGURE_IDM_FIREWALL.ps1`
