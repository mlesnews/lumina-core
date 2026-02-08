# ASUS Armory Crate & FN+F4 AURA Lighting Fix

## Problem Solved

**Lost FN+F4 AURA lighting effects functionality** - The keyboard shortcut for cycling through RGB lighting themes on ASUS ROG devices stopped working.

## Root Causes

This issue typically occurs due to:
- Corrupted Armory Crate installation
- ASUS services not running
- Outdated ROG drivers
- Windows updates breaking functionality
- Keyboard firmware issues

## Solution Overview

The comprehensive fix script (`Fix-ArmoryCrate-AURA.ps1`) addresses all common causes:

1. **Service Management**: Restarts all ASUS services
2. **Installation Repair**: Fixes corrupted Armory Crate installations
3. **Driver Updates**: Ensures latest ASUS drivers
4. **Functionality Testing**: Verifies FN+F4 works
5. **Troubleshooting Tools**: Provides diagnostic information

## Usage

### Method 1: VSCode Task (Recommended)
1. Open VSCode/Cursor
2. Press `Ctrl+Shift+P` (Command Palette)
3. Run: `Tasks: Run Task`
4. Select: `ASUS: Fix Armory Crate & FN+F4 AURA`

### Method 2: Direct PowerShell (Administrator)
```powershell
# Basic fix
.\scripts\powershell\Fix-ArmoryCrate-AURA.ps1

# Force reinstallation
.\scripts\powershell\Fix-ArmoryCrate-AURA.ps1 -ForceReinstall

# Skip driver updates
.\scripts\powershell\Fix-ArmoryCrate-AURA.ps1 -SkipDrivers

# Verbose output
.\scripts\powershell\Fix-ArmoryCrate-AURA.ps1 -Verbose
```

## What the Fix Does

### 🔧 Service Management
**Restarts critical ASUS services:**
- Armory Crate Service
- ASUS App Service
- ASUS Certificate Service
- ROG Live Service
- AURA Lighting Service
- ASUS Optimization Service

### 🔄 Installation Repair
**Automatically repairs Armory Crate:**
- Detects existing installation
- Runs repair utilities
- Provides manual installation guidance
- Handles corrupted installations

### 📡 Driver Updates
**Ensures latest drivers:**
- Checks ASUS Update utility
- Updates ROG components
- Refreshes keyboard drivers
- Maintains firmware compatibility

### 🧪 Functionality Testing
**Comprehensive validation:**
- Verifies AURA service status
- Checks Armory Crate processes
- Tests keyboard driver presence
- Provides step-by-step testing instructions

### 🛠️ Troubleshooting Tools
**Diagnostic capabilities:**
- Service status monitoring
- Process verification
- Driver enumeration
- Desktop shortcut creation

## Expected Results

### ✅ Successful Fix
```
🎉 ASUS Armory Crate & AURA Fix Complete!

✅ All services are running correctly
✅ FN+F4 should now work for AURA lighting effects
```

### 🔄 Manual Testing Required
After running the fix:
1. Close the PowerShell window
2. Press `FN+F4` on your keyboard
3. RGB lighting should cycle through effects
4. If it doesn't work, restart your computer

## Troubleshooting

### Issue: "Armory Crate is not installed"
**Solution:**
1. Download latest Armory Crate from ASUS website
2. Run installer as Administrator
3. Restart computer
4. Run fix script again

### Issue: "Services fail to start"
**Solution:**
1. Open Services.msc as Administrator
2. Manually start ASUS services
3. Check Windows Event Viewer for errors
4. Run fix script with `-ForceReinstall` flag

### Issue: "FN+F4 still doesn't work after fix"
**Solutions:**
1. Restart computer completely
2. Update BIOS/firmware through ASUS software
3. Check for Windows updates
4. Test with external keyboard (if available)
5. Contact ASUS support with device model

## ASUS Services Monitored

| Service Name | Display Name | Purpose |
|-------------|-------------|---------|
| ARMOURY CRATE Service | Armory Crate Service | Main control service |
| AsusAppService | ASUS App Service | Application integration |
| AsusCertService | ASUS Certificate Service | Security certificates |
| AsusROGLSLService | ROG Live Service | Live streaming features |
| AsusOptimization | ASUS Optimization Service | System optimization |
| LightingService | AURA Lighting Service | RGB lighting control |
| AsusArmouryCrateService | Armory Crate Core Service | Core functionality |

## FN+F4 Keyboard Shortcut

### What it does:
- Cycles through AURA lighting effects
- Changes RGB themes/patterns
- Controls keyboard backlighting modes

### Alternative access:
- Armory Crate system tray icon
- AURA software interface
- ASUS ROG software suite

## Prevention

### Regular Maintenance:
1. Keep Armory Crate updated
2. Don't disable ASUS services
3. Update Windows regularly
4. Avoid third-party RGB software conflicts

### Backup Settings:
- Export AURA profiles regularly
- Backup Armory Crate settings
- Document custom lighting configurations

## Advanced Options

### Force Reinstallation:
```powershell
.\Fix-ArmoryCrate-AURA.ps1 -ForceReinstall
```
Completely reinstalls Armory Crate components.

### Skip Driver Updates:
```powershell
.\Fix-ArmoryCrate-AURA.ps1 -SkipDrivers
```
Skips driver update step (faster execution).

### Verbose Logging:
```powershell
.\Fix-ArmoryCrate-AURA.ps1 -Verbose
```
Provides detailed execution information.

## Compatibility

### Supported Devices:
- ASUS ROG laptops
- ASUS ROG desktops
- ASUS ROG peripherals
- ASUS TUF Gaming series
- ASUS ZenBook Pro series

### Requirements:
- Windows 10/11
- Administrator privileges
- Internet connection (for updates)
- ASUS ROG hardware

## Error Codes

### Common Exit Codes:
- `0`: Success
- `1`: Administrator privileges required
- `2`: Armory Crate installation failed
- `3`: Service restart failed
- `4`: Driver update failed

## Logs and Diagnostics

### Log Locations:
- `%LOCALAPPDATA%\ASUS\ArmoryCrate\logs\`
- Windows Event Viewer → Windows Logs → Application
- PowerShell execution output

### Diagnostic Commands:
```powershell
# Check ASUS services status
Get-Service -Name "*asus*" | Format-Table

# List ASUS processes
Get-Process -Name "*armory*", "*asus*", "*aura*" | Format-Table

# Check ASUS drivers
Get-PnpDevice | Where-Object { $_.Name -like "*ASUS*" -or $_.Name -like "*ROG*" }
```

## Support Resources

### ASUS Official Support:
- **Website**: https://www.asus.com/support/
- **FAQ**: https://www.asus.com/support/FAQ/1042475
- **Downloads**: https://www.asus.com/support/download-center/

### Community Resources:
- ASUS ROG Forums
- Reddit r/ASUS
- ROG Community Discord

## Version History

- **v1.0**: Initial release with comprehensive ASUS service management
- **v1.1**: Added driver update functionality
- **v1.2**: Enhanced error handling and logging
- **v1.3**: Added VSCode integration and desktop shortcuts

---

**Note**: This fix script is designed for ASUS ROG devices with AURA RGB lighting. For non-ASUS devices, consult your manufacturer's lighting software documentation.



