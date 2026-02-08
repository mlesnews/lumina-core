# Surveillance Station Installation Status

**Date**: 2025-01-16  
**NAS IP**: `10.17.17.32`  
**Status**: ⚠️ **Manual Installation Required**

---

## Current Status

### ✅ Completed
- ✅ **NAS Connection**: Successfully connected to Synology NAS
- ✅ **Package Detection**: Found Surveillance Station in package list
  - **Package ID**: `SurveillanceStation`
  - **Version Available**: `9.2.4-11880`
- ✅ **Installation Script**: Created automated installation script
- ✅ **Configuration Script**: Ready for post-installation configuration

### ⚠️ Installation Method
- **Automated API Installation**: ❌ Not available (API returns error codes 102/103)
- **Manual Installation Required**: ✅ Via DSM Package Center UI

---

## Manual Installation Steps

### Step 1: Access DSM
1. Open browser and navigate to: `https://10.17.17.32:5001`
2. Log in with your admin credentials

### Step 2: Install Surveillance Station
1. Click **Main Menu** (top-left, 9-dot icon)
2. Open **Package Center**
3. Use the search bar and search for: **"Surveillance Station"**
4. Click **Install** button
5. During installation:
   - Select storage volume (use main volume, typically `volume1`)
   - Leave default settings
   - Enable **"Run after installation"**
6. Wait for installation to complete (~2-5 minutes)

### Step 3: Verify Installation
1. Check **Main Menu** for **Surveillance Station** icon
2. Access directly at: `https://10.17.17.32:9901`
3. First launch will prompt for initial setup

---

## Post-Installation Configuration

After manual installation, run the configuration script:

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts\python\install_surveillance_station.py --configure-only
```

**Note**: The `--configure-only` flag will be added to configure storage and settings after installation.

### Configuration Tasks
1. ✅ Create `surveillance` shared folder (if it doesn't exist)
2. ✅ Configure storage location in Surveillance Station
3. ✅ Verify license status (should show 2 free licenses)
4. ✅ Set up recording storage path

---

## Automated Installation Attempt Results

### API Response
- **Package Found**: ✅ Yes (`SurveillanceStation` ID confirmed)
- **Download API**: ❌ Error 103 (Invalid parameter or method)
- **Installation API**: ❌ Error 102 (Method not available)

### Conclusion
Surveillance Station appears to require installation through the Package Center UI rather than the programmatic API. This is common for certain Synology packages that have special installation requirements.

---

## Next Steps

1. **Manual Installation** (Required)
   - Follow steps above to install via DSM Package Center
   - Estimated time: 5-10 minutes

2. **Post-Installation Configuration** (Automated)
   - Run configuration script after installation
   - Will set up storage and verify setup

3. **Camera Setup** (After hardware arrives)
   - Add Reolink doorbell cameras
   - Configure RTSP/ONVIF streams
   - Set up recording schedules

---

## Access Information

- **DSM Web Interface**: `https://10.17.17.32:5001`
- **Surveillance Station**: `https://10.17.17.32:9901` (after installation)
- **Default Licenses**: 2 cameras (free)

---

## Troubleshooting

### If Installation Fails
- Check DSM version (must be 7.0+)
- Verify disk space available
- Check Package Center for error messages
- Try manual .spk file installation if needed

### If Configuration Script Fails
- Verify Surveillance Station is installed and running
- Check that you can access `https://10.17.17.32:9901`
- Verify NAS credentials are correct
- Check firewall allows port 9901

---

**Last Updated**: 2025-01-16  
**Next Action**: Manual installation via DSM Package Center
