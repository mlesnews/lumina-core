# Smart Lighting Day/Night Sync

## Overview

Smart lighting system that:
- ✅ **Keeps external lighting effects** (synced with day/night cycles)
- ✅ **Disables display and keyboard lighting**
- ✅ **Dims screen appropriately for night sessions**
- ✅ **Monitors and adjusts automatically**

## Configuration

### Day/Night Cycle Settings

**Default Configuration:**
- **Sunrise**: 6:00 AM
- **Sunset**: 8:00 PM
- **Night Start**: 10:00 PM
- **Night End**: 6:00 AM

**Brightness Levels:**
- **Day Screen**: 80%
- **Night Screen**: 30%
- **Day External Lighting**: 70%
- **Night External Lighting**: 30%

### Customization

Edit `scripts/python/jarvis_smart_lighting_day_night_sync.py` to adjust:
- Time periods (sunrise, sunset, night start/end)
- Brightness levels for day/night
- Check intervals for monitoring

## Usage

### Initial Setup

```bash
# Run initial setup (re-enables services, applies settings)
python scripts/python/jarvis_smart_lighting_day_night_sync.py
```

### Continuous Monitoring

```bash
# Run once (check and adjust)
python scripts/python/jarvis_continuous_day_night_monitor.py --once

# Run continuously (default: 60 second intervals)
python scripts/python/jarvis_continuous_day_night_monitor.py

# Custom interval (e.g., every 30 seconds)
python scripts/python/jarvis_continuous_day_night_monitor.py --interval 30

# Run for specific duration (e.g., 1 hour = 3600 seconds)
python scripts/python/jarvis_continuous_day_night_monitor.py --duration 3600
```

### Startup Script

```bash
# Create startup script (runs automatically on login)
python scripts/python/jarvis_setup_smart_lighting_startup.py
```

## How It Works

### 1. Service Management
- Re-enables `ArmouryCrateService` and `LightingService`
- Sets services to Manual startup (not Auto, not Disabled)
- Allows external lighting control while preventing auto-start issues

### 2. Lighting Control
- **External Lighting**: Enabled and synced with day/night cycles
- **Display Lighting**: Disabled
- **Keyboard Lighting**: Disabled

### 3. Screen Brightness
- Automatically adjusts based on time of day
- **Day**: 80% brightness
- **Night**: 30% brightness (for entire night session)

### 4. Automatic Monitoring
- Checks every 60 seconds (configurable)
- Adjusts lighting/brightness when period changes
- Runs automatically on login via startup script

## Files Created

1. **`scripts/python/jarvis_smart_lighting_day_night_sync.py`**
   - Core smart lighting system
   - Day/night cycle detection
   - Screen brightness control
   - External lighting control

2. **`scripts/python/jarvis_continuous_day_night_monitor.py`**
   - Continuous monitoring system
   - Automatic adjustment on period changes
   - Background monitoring

3. **`scripts/python/jarvis_setup_smart_lighting_startup.py`**
   - Startup script creation
   - Automatic launch on login

4. **`docs/smart_lighting_day_night_sync.md`**
   - This documentation

## Status

### Current Status
- ✅ Services: Enabled (Manual startup)
- ✅ Display/Keyboard Lighting: Disabled
- ✅ External Lighting: Enabled (synced)
- ✅ Screen Brightness: Auto-adjusted
- ✅ Startup Script: Active
- ✅ Continuous Monitor: Ready

### Verification

```bash
# Check current status
python scripts/python/jarvis_verify_external_lighting_fix.py
```

## Troubleshooting

### Services Not Starting
- Check if services are set to Manual (not Disabled)
- Run setup again: `python scripts/python/jarvis_smart_lighting_day_night_sync.py`

### Screen Brightness Not Changing
- May require admin privileges for WMI brightness control
- Check Windows display settings
- Try manual brightness adjustment to verify hardware support

### External Lighting Not Syncing
- Verify Armoury Crate is running
- Check service status: `Get-Service ArmouryCrateService,LightingService`
- May require Armoury Crate API integration (future enhancement)

### Monitor Not Running
- Check startup script exists: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\JARVIS_SmartLightingMonitor.bat`
- Run manually to test: `python scripts/python/jarvis_continuous_day_night_monitor.py --once`

## Future Enhancements

1. **Armoury Crate API Integration**
   - Direct API calls for external lighting control
   - More reliable lighting synchronization

2. **Sunrise/Sunset Detection**
   - Automatic sunrise/sunset detection based on location
   - Dynamic time adjustment

3. **Custom Profiles**
   - User-defined lighting profiles
   - Multiple time periods (morning, afternoon, evening, night)

4. **Screen Brightness Smooth Transitions**
   - Gradual brightness changes instead of instant
   - Configurable transition duration

## Notes

- **Display/Keyboard Lighting**: Permanently disabled (as requested)
- **External Lighting**: Always enabled and synced with day/night
- **Screen Dimming**: Automatic for entire night session (10 PM - 6 AM)
- **Monitoring**: Runs continuously in background (60 second intervals)
