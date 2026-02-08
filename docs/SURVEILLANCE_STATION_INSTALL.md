# Synology Surveillance Station Installation & Configuration

**Date**: 2025-01-16  
**NAS IP**: `10.17.17.32`  
**Purpose**: Install and configure Surveillance Station DSM package

---

## Prerequisites

- ✅ Synology NAS accessible at `10.17.17.32`
- ✅ DSM 7.0 or later (required for Surveillance Station 9.x)
- ✅ Admin access to DSM web interface
- ✅ Default 2 camera licenses included (free with NAS)

---

## Part 1: Installation

### Method 1: Package Center (Recommended)

1. **Access DSM Web Interface**
   ```
   URL: http://10.17.17.32:5000
   OR:  https://10.17.17.32:5001
   ```
   - Log in with your admin credentials

2. **Open Package Center**
   - Click **Main Menu** (top-left corner, 9-dot icon)
   - Select **Package Center**

3. **Install Surveillance Station**
   - In Package Center, use the search bar
   - Search for: **"Surveillance Station"**
   - Click the **Install** button
   - During installation wizard:
     - **Storage Volume**: Select your main volume (where you want recordings stored)
     - **Alias/URL**: Leave default or customize (optional)
     - **Run after installation**: ✅ Keep this checked
   - Wait for installation to complete (~2-5 minutes)
   - You'll see a notification when installation is complete

4. **Verify Installation**
   - Check **Main Menu** for **Surveillance Station** icon
   - Should appear in the application list
   - Status should show as "Running"

### Method 2: Manual Install (If Package Center is delayed/unavailable)

1. **Download .spk File**
   - Visit: https://www.synology.com/en-us/support/download_center
   - Select your NAS model (check DSM > Control Panel > Info Center for model)
   - Navigate to: **Surveillance Station**
   - Download the latest .spk file for your NAS model

2. **Manual Installation**
   - In Package Center, click **Manual Install** button (top-right)
   - Click **Browse** and select the downloaded .spk file
   - Click **Next** and follow installation prompts
   - Same options as Method 1 (storage volume, alias, etc.)
   - Launch after installation completes

---

## Part 2: Initial Configuration

### Step 1: First Launch & Storage Setup

1. **Launch Surveillance Station**
   - Click **Surveillance Station** in Main Menu
   - OR access directly: `https://10.17.17.32:9901`
   - First launch will open setup wizard

2. **Create Recording Storage Location**
   - Wizard will prompt for storage location
   - **Option A**: Use existing shared folder
     - Select from dropdown (e.g., `surveillance`, `video`, or create new)
   - **Option B**: Create new shared folder
     - Name: `surveillance` (recommended)
     - Location: Main volume
     - Enable encryption: Optional (recommended for sensitive footage)
   - Click **Next** to continue

3. **Complete Setup Wizard**
   - Review settings
   - Click **Finish** to complete initial setup

### Step 2: Verify Installation

1. **Check License Status**
   - In Surveillance Station, go to **License** (left sidebar)
   - Should show: **2 licenses available** (default free licenses)
   - Status: **Activated**

2. **Access Surveillance Station**
   - **Web Interface**: `https://10.17.17.32:9901`
   - **Main Menu**: Click Surveillance Station icon in DSM
   - Should see main dashboard with no cameras yet

---

## Part 3: Storage Configuration

### Configure Recording Storage

1. **Navigate to Storage Settings**
   - Surveillance Station > **Settings** (gear icon, top-right)
   - Select **Storage** from left menu

2. **Set Recording Storage Location**
   - **Recording Folder**: Select the folder created during setup
     - Default: `surveillance` or `surveillance/recording`
   - **Path**: Should show something like `/volume1/surveillance`
   - **Available Space**: Check available disk space
   - Click **Apply** to save

3. **Configure Storage Limits** (Optional but Recommended)
   - **Storage Allocation**: Set max storage for recordings
   - **Retention Policy**: Configure automatic deletion of old recordings
   - **Low Space Alert**: Set threshold (e.g., 10% remaining)

### Verify Storage Access

- Check that the shared folder is accessible:
  - Windows: `\\10.17.17.32\surveillance`
  - Should be able to browse and see folder structure

---

## Part 4: Network Configuration

### Configure Access Ports

1. **Check Default Port**
   - Surveillance Station default HTTPS port: **9901**
   - Access via: `https://10.17.17.32:9901`

2. **Customize Port** (Optional)
   - DSM > **Control Panel** > **Login Portal** > **Applications**
   - Find **Surveillance Station** in the list
   - Click **Edit** to change port if needed
   - **Note**: Changing port requires updating firewall rules

### Firewall Configuration

1. **Check Firewall Rules**
   - DSM > **Control Panel** > **Security** > **Firewall**
   - Ensure port **9901** (or custom port) is allowed
   - Allow from: Your local network (e.g., `10.17.17.0/24`)

2. **HTTPS Certificate** (Recommended)
   - Use DSM's built-in certificate or import your own
   - Control Panel > **Security** > **Certificate**
   - Ensure Surveillance Station uses HTTPS certificate

---

## Part 5: Advanced Configuration

### Enable Advanced Features

1. **Advanced Media Extensions (AME)** - For H.265 Support
   - **Why**: Some cameras use H.265 codec; AME enables proper playback
   - **Install**: Package Center > Search "Advanced Media Extensions" > Install
   - **Note**: May require additional setup after installation

2. **Mobile App Access**
   - **DS cam** app available for iOS/Android
   - Enable mobile access in Surveillance Station settings
   - **Settings** > **Network** > **Mobile** > Enable mobile access

### User Permissions

1. **Create Surveillance Station Users** (Optional)
   - **Settings** > **Users** > **Add**
   - Create users with specific permissions:
     - **View Only**: Can view live feeds and recordings
     - **Operator**: Can control cameras and view
     - **Administrator**: Full access
   - Or use existing DSM users

---

## Part 6: Verification Checklist

After installation and configuration, verify:

- [ ] Surveillance Station appears in Main Menu
- [ ] Can access via `https://10.17.17.32:9901`
- [ ] License shows 2 available cameras
- [ ] Storage location is configured and accessible
- [ ] Can browse to `\\10.17.17.32\surveillance` (if using Windows)
- [ ] Firewall allows access on port 9901
- [ ] HTTPS certificate is valid
- [ ] No error messages in Surveillance Station dashboard

---

## Part 7: Troubleshooting

### Installation Issues

**Problem**: Package not appearing in Package Center
- **Solution**: 
  - Check DSM version (must be 7.0+)
  - Try refreshing Package Center
  - Check internet connectivity (for package list updates)
  - Use Manual Install method instead

**Problem**: Installation fails
- **Solution**:
  - Check available disk space
  - Verify DSM is up to date
  - Try manual install via .spk file
  - Check system logs: **Main Menu** > **Log Center**

**Problem**: "Repair" option appears after DSM update
- **Solution**:
  - Click **Repair** in Package Center
  - Or uninstall and reinstall Surveillance Station
  - Your camera configurations are preserved

### Access Issues

**Problem**: Can't access Surveillance Station (port 9901)
- **Solution**:
  - Check firewall rules (allow port 9901)
  - Verify service is running: **Main Menu** > **Resource Monitor** > **Services**
  - Try accessing via Main Menu instead of direct URL
  - Check if port was changed in Login Portal settings

**Problem**: HTTPS certificate errors
- **Solution**:
  - Control Panel > **Security** > **Certificate**
  - Generate or import valid certificate
  - Assign certificate to Surveillance Station

### Storage Issues

**Problem**: Can't create storage folder
- **Solution**:
  - Check user permissions (need admin or storage manager)
  - Verify disk space available
  - Check shared folder creation permissions in Control Panel

**Problem**: Recordings not saving
- **Solution**:
  - Verify storage location is set correctly
  - Check disk space (may be full)
  - Verify folder permissions
  - Check recording schedule is configured

---

## Part 8: Next Steps (After Hardware Arrives)

Once your doorbell cameras arrive, you'll need to:

1. **Enable RTSP/ONVIF on Cameras**
   - Configure cameras via their app/web interface
   - Enable RTSP and ONVIF protocols
   - Note camera IP addresses and credentials

2. **Add Cameras to Surveillance Station**
   - Surveillance Station > **IP Camera** > **Add** > **Add Camera**
   - Use **ONVIF** or **Generic RTSP** connection method
   - Enter camera IP, port, username, password
   - Test connection before completing setup

3. **Configure Recording**
   - Set recording schedules (continuous or motion-triggered)
   - Configure retention policies
   - Set up motion detection zones

4. **Test Mobile Access**
   - Install DS cam app on mobile device
   - Connect to your NAS
   - Test live view and playback

---

## Quick Reference

### Access URLs
- **DSM**: `http://10.17.17.32:5000` or `https://10.17.17.32:5001`
- **Surveillance Station**: `https://10.17.17.32:9901`

### Default Ports
- **DSM HTTP**: 5000
- **DSM HTTPS**: 5001
- **Surveillance Station HTTPS**: 9901

### Storage Paths
- **Windows Network**: `\\10.17.17.32\surveillance`
- **Linux/Mac**: `/volume1/surveillance` (via SMB/NFS)

### License Information
- **Default Licenses**: 2 cameras (free)
- **Additional Licenses**: Purchase from Synology
- **Check Status**: Surveillance Station > **License**

---

**Last Updated**: 2025-01-16  
**Status**: Ready for installation  
**Next**: Install Surveillance Station, then configure cameras when hardware arrives
