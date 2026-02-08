# Synology Surveillance Station Setup & Reolink Doorbell Recommendations

**Date**: 2025-01-16  
**NAS IP**: `10.17.17.32`  
**Purpose**: Install Surveillance Station and configure Reolink doorbell cameras for front and back doors

> **Note**: For detailed installation and configuration steps, see: `SURVEILLANCE_STATION_INSTALL.md`

---

## Part 1: Install Surveillance Station on Synology NAS

### Prerequisites
- ✅ Synology NAS accessible at `10.17.17.32`
- ✅ DSM 7.0 or later (required for Surveillance Station 9.x)
- ✅ Admin access to DSM web interface
- ✅ Default 2 camera licenses included (can add more later)

### Installation Steps

#### Method 1: Package Center (Recommended)
1. **Access DSM Web Interface**
   - Open browser and navigate to: `http://10.17.17.32:5000` (or `https://10.17.17.32:5001`)
   - Log in with admin credentials

2. **Open Package Center**
   - Click **Main Menu** (top-left)
   - Select **Package Center**

3. **Install Surveillance Station**
   - Search for **"Surveillance Station"**
   - Click **Install** button
   - During installation:
     - Choose storage volume (use your main volume)
     - Set alias/URL segment (optional, default is fine)
     - Leave **"Run after installation"** enabled
   - Wait for installation to complete (~2-5 minutes)

4. **Access Surveillance Station**
   - After installation, find **Surveillance Station** in Main Menu
   - Or access directly at: `https://10.17.17.32:9901` (default HTTPS port)
   - First launch will prompt you to:
     - Create recording storage location (shared folder)
     - Set up initial admin account (if not using DSM admin)

#### Method 2: Manual Install (If Package Center is delayed)
1. **Download .spk file**
   - Visit: https://www.synology.com/en-us/support/download_center
   - Select your NAS model
   - Download **Surveillance Station** .spk file

2. **Manual Installation**
   - In Package Center, click **Manual Install**
   - Select the downloaded .spk file
   - Follow installation prompts
   - Launch after installation

### Post-Installation Configuration

1. **Verify Installation**
   - Check Main Menu for Surveillance Station icon
   - Access via `https://10.17.17.32:9901`
   - Should see default 2 camera licenses available

2. **Configure Storage Location**
   - Surveillance Station > **Settings** > **Storage**
   - Create or select shared folder for recordings
   - Recommended: `\\10.17.17.32\surveillance` or similar

3. **Network Configuration** (Optional)
   - Control Panel > **Login Portal** > **Applications**
   - Customize Surveillance Station port if needed
   - Configure reverse proxy if desired

---

## Part 2: Reolink Doorbell Recommendations

### Front Door Recommendation: **Reolink Video Doorbell PoE (D340P)**

**Model**: D340P - Smart 2K+ Wired PoE Video Doorbell with Chime

**Why This Model:**
- ✅ **PoE Power**: Single Ethernet cable for power + data (most reliable)
- ✅ **Local-Only**: Full RTSP/ONVIF support, no cloud required
- ✅ **Synology Compatible**: Native integration with Surveillance Station
- ✅ **5MP Resolution**: 2560×1920 (black) or 1920×2560 (white)
- ✅ **180° FOV**: Wide diagonal field of view
- ✅ **Smart Detection**: Person, vehicle, animal, visitor detection
- ✅ **Two-Way Audio**: Built-in speaker and microphone
- ✅ **Night Vision**: IR up to 23ft, Color Night Vision up to 10ft
- ✅ **Homelab-Friendly**: Works with Frigate, Home Assistant, etc.

**Specifications:**
- **Power**: IEEE 802.3af PoE (48V) or 12-24V AC / 24V DC
- **Network**: Wired Ethernet only (PoE)
- **Resolution**: 5MP (2K+)
- **FOV**: 180° diagonal (varies by color: Black H135°/V100°, White H100°/V135°)
- **Audio**: Two-way with 93 dBA speaker
- **Storage**: RTSP/ONVIF to NAS (no local SD card)
- **Chime**: Requires Reolink Chime (V2/V3, supports up to 5 chimes)

**Purchase Links:**
- Amazon: Search "Reolink D340P"
- Reolink Official: https://reolink.com/product/d340p/

**Installation Notes:**
- Requires PoE switch or PoE injector
- Can use existing doorbell wiring (12-24V AC) if PoE unavailable
- Does NOT ring existing mechanical chimes (needs Reolink Chime)

---

### Back Door Recommendation: **Reolink Video Doorbell PoE (D340P)** or **Reolink Video Doorbell WiFi (D340W)**

#### Option A: Second PoE Doorbell (D340P) - **RECOMMENDED**
**Best for**: Consistent setup, maximum reliability, homelab environments

**Advantages:**
- Same model as front door (easier management)
- PoE reliability (no WiFi issues)
- Identical features and integration
- Single management interface

#### Option B: WiFi Doorbell (D340W) - **Alternative**
**Model**: D340W - Smart Video Doorbell Camera (Plug-in WiFi)

**When to Choose:**
- Cannot run Ethernet to back door
- Prefer easier installation (uses existing doorbell wiring)
- WiFi coverage is strong at back door location

**Specifications:**
- **Power**: 12-24V AC / 24V DC (uses existing doorbell wiring)
- **Network**: Dual-band WiFi (2.4/5 GHz)
- **Resolution**: 5MP (same as PoE model)
- **FOV**: Same 180° diagonal
- **RTSP/ONVIF**: Supported (enable in settings)
- **Note**: Some users report RTSP stability issues on WiFi; PoE preferred for reliability

**Trade-offs:**
- ⚠️ WiFi dependency (less reliable than PoE)
- ⚠️ Potential RTSP stream stability issues (community reports)
- ✅ Easier installation (no Ethernet required)
- ✅ Uses existing doorbell wiring

#### Option C: Regular Reolink Camera (For Back Door)
**Alternative**: Use a standard Reolink PoE camera (e.g., RLC-810A, RLC-820A) instead of a doorbell

**When to Choose:**
- Don't need doorbell button/chime at back door
- Want more camera placement flexibility
- Lower cost option

**Recommended Models:**
- **RLC-810A**: 4K PoE bullet camera
- **RLC-820A**: 4K PoE dome camera
- Both support RTSP/ONVIF and work with Surveillance Station

---

## Part 3: Camera Setup in Surveillance Station

### Adding Reolink Doorbell to Surveillance Station

1. **Prepare Doorbell**
   - Install doorbell at front/back door location
   - Connect to network (PoE or WiFi)
   - Note the camera's IP address (check router DHCP or Reolink app)

2. **Enable RTSP/ONVIF on Doorbell**
   - Open Reolink app or web interface
   - Navigate to **Settings** > **Network** > **Advanced**
   - Enable **RTSP** and **ONVIF**
   - Note RTSP port (default: 554)
   - Set username/password for RTSP access

3. **Add Camera in Surveillance Station**
   - Open Surveillance Station
   - Go to **IP Camera** > **Add** > **Add Camera**
   - Choose **Quick Setup** or **Complete Setup**
   - Select **ONVIF** or **Generic RTSP**
   - Enter camera details:
     - **IP Address**: Doorbell's IP (e.g., `192.168.1.100`)
     - **Port**: RTSP port (default: 554)
     - **Username**: Camera username
     - **Password**: Camera password
   - Click **Test Connection** to verify
   - Complete setup wizard

4. **Configure Recording**
   - Set recording schedule (continuous or motion-triggered)
   - Configure retention policy
   - Set storage location (NAS shared folder)

5. **Repeat for Second Doorbell**
   - Follow same steps for back door camera
   - Note: You'll use 2 of your default 2 licenses

---

## Part 4: License Management

### Default Licenses
- **Included**: 2 camera licenses (free)
- **Usage**: Front door + Back door = 2 licenses ✅

### Adding More Cameras (If Needed)
- Purchase **Surveillance Device License Pack** from Synology
- In Surveillance Station: **License** > **Add** > Enter license key
- License packs available: 1, 4, 8, 16, 32 camera licenses

---

## Part 5: Recommended Purchase List

### Front Door Setup
- [ ] **Reolink Video Doorbell PoE (D340P)** - Black or White
- [ ] **Reolink Chime (V2 or V3)** - For doorbell notifications
- [ ] **PoE Switch** (if not already owned) - 802.3af compatible
- [ ] **Ethernet Cable** - Cat5e or better, appropriate length

### Back Door Setup
- [ ] **Reolink Video Doorbell PoE (D340P)** - Same as front (recommended)
  - OR **Reolink Video Doorbell WiFi (D340W)** - If PoE not feasible
- [ ] **Reolink Chime (V2 or V3)** - If using doorbell model
  - Note: V2/V3 chimes can pair with up to 5 doorbells

### Optional Accessories
- [ ] **Reolink Home Hub** - For advanced automations (optional)
- [ ] **PoE Injector** - If using single PoE port instead of switch

---

## Part 6: Integration Notes

### Synology Surveillance Station
- ✅ Native ONVIF/RTSP support
- ✅ Motion detection and recording
- ✅ Mobile app access (DS cam)
- ✅ Web interface access
- ✅ Timeline playback

### Home Assistant (Optional)
- Reolink doorbells work with Home Assistant
- Use Reolink integration or ONVIF integration
- Can create automations (doorbell press triggers actions)

### Frigate NVR (Alternative/Additional)
- Reolink doorbells work with Frigate
- AI-powered object detection
- Can run in Docker on your NAS
- More advanced than Surveillance Station for AI features

---

## Part 7: Security Considerations

### Best Practices
1. **Network Isolation**: Place cameras on VLAN or isolated network
2. **Firmware Updates**: Keep doorbell firmware updated
3. **Strong Passwords**: Use unique, strong passwords for cameras
4. **Disable Cloud Features**: If using local-only, disable P2P/cloud in Reolink settings
5. **HTTPS Only**: Access Surveillance Station via HTTPS (port 9901)

### Known Security Notes (2025)
- Some Reolink doorbell models had CVEs reported in 2025
- Keep firmware updated
- Use local-only access when possible
- Review security advisories before exposing to internet

---

## Troubleshooting

### Surveillance Station Issues
- **Package not appearing**: Check DSM version compatibility
- **Installation fails**: Try manual install via .spk file
- **Can't access**: Check firewall rules, verify port 9901 is open

### Camera Connection Issues
- **RTSP not working**: Verify RTSP/ONVIF enabled on doorbell
- **Connection timeout**: Check IP address, network connectivity
- **Poor video quality**: Adjust stream settings, check bandwidth
- **WiFi doorbell disconnects**: Consider switching to PoE model

### Recording Issues
- **No recordings**: Check recording schedule, storage location
- **Storage full**: Configure retention policy, check NAS disk space
- **Playback issues**: Install Advanced Media Extensions (AME) for H.265

---

## Next Steps

1. ✅ Install Surveillance Station on NAS (`10.17.17.32`)
2. ⏳ Order Reolink doorbell(s) (D340P recommended)
3. ⏳ Install doorbell(s) at front and back doors
4. ⏳ Configure RTSP/ONVIF on doorbells
5. ⏳ Add cameras to Surveillance Station
6. ⏳ Configure recording schedules and retention
7. ⏳ Test mobile app access (DS cam)
8. ⏳ Optional: Integrate with Home Assistant or Frigate

---

**Last Updated**: 2025-01-16  
**Status**: Ready for implementation
