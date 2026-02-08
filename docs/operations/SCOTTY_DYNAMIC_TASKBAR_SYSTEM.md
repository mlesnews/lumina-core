# @SCOTTY's Dynamic Taskbar System

**Tags:** `#SCOTTY` `#TASKBAR` `#DYNAMIC` `#USAGE_TRACKING` `@SCOTTY` `@LUMINA`

## Overview

@SCOTTY has implemented a dynamic taskbar system that tracks application usage and automatically adjusts the taskbar based on popularity and frequency of use.

## Current Status

### ✅ Completed

1. **Desktop Shortcuts Restored:**
   - Cursor IDE ✅
   - Visual Studio Code ✅
   - Windows Terminal ✅
   - PowerShell ✅
   - Git ✅
   - Docker Desktop ✅
   - Neo Browser ⚠️ (not found - may need manual installation path)

2. **Taskbar Pinned Applications (8):**
   - Cursor IDE
   - Visual Studio Code
   - Windows Terminal
   - PowerShell
   - Git
   - Docker Desktop
   - Command Prompt
   - File Explorer

3. **Dynamic Tracking System:**
   - Usage tracking database created
   - Application launch monitoring ready
   - Top 10 recommendation system implemented

## How It Works

### Usage Tracking

The system tracks:
- Application launches (when apps are opened)
- Frequency of use (daily counts)
- Recent usage (last 7 days by default)
- Historical data (total launches)

### Scoring Algorithm

Applications are scored by:
```
Score = Recent Launches (last 7 days) + (Total Launches / 100)
```

This balances:
- **Recent usage** (what you're using now)
- **Historical usage** (what you've used over time)

### Dynamic Updates

The taskbar recommendations update based on:
- Top 10 applications by score
- Minimum usage threshold (7 days default)
- Maximum taskbar items (10 default)

## Usage

### Start Monitoring

```powershell
# Monitor application launches
python scripts\python\scotty_taskbar_monitor.py --daemon --interval 60
```

### View Top Applications

```powershell
# Show top 10 applications
python scripts\python\scotty_dynamic_taskbar.py --top 10

# Show recommendations for taskbar
python scripts\python\scotty_dynamic_taskbar.py --recommend
```

### Track Specific Application

```powershell
# Manually track an application launch
python scripts\python\scotty_dynamic_taskbar.py --track "Neo Browser:C:\Path\To\Neo Browser.exe"
```

### Update Taskbar

```powershell
# Get recommendations and update taskbar
.\scripts\powershell\scotty_update_taskbar_dynamic.ps1
```

## Configuration

Configuration file: `data/scotty_taskbar_config.json`

```json
{
  "max_taskbar_items": 10,
  "min_usage_days": 7,
  "update_frequency_hours": 24,
  "pinned_apps": []
}
```

## Files

- `scripts/python/scotty_dynamic_taskbar.py` - Main tracking and recommendation system
- `scripts/python/scotty_taskbar_monitor.py` - Background monitoring daemon
- `scripts/powershell/scotty_restore_dev_shortcuts.ps1` - Restore developer shortcuts
- `scripts/powershell/scotty_pin_top_dev_apps.ps1` - Pin applications to taskbar
- `scripts/powershell/scotty_update_taskbar_dynamic.ps1` - Update taskbar based on usage
- `data/scotty_taskbar_usage.json` - Usage tracking data
- `data/scotty_taskbar_config.json` - Configuration

## Next Steps

1. **Start Monitoring:**
   ```powershell
   python scripts\python\scotty_taskbar_monitor.py --daemon
   ```

2. **Find Neo Browser:**
   - Search for Neo Browser installation
   - Add to tracking if found
   - Create shortcut manually if needed

3. **Automatic Updates:**
   - Set up scheduled task to run recommendations daily
   - Or run monitor as background service

## Notes

- Neo Browser was not found in standard installation locations
- May need to manually locate and add to system
- Current taskbar has 8 pinned applications (room for 2 more)
- System will learn usage patterns over time

---

**USS Lumina - @scotty (Windows Systems Architect)**

*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
