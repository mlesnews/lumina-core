# JARVIS Vacuum Integration - Quick Start

## 🚀 Getting Started in 5 Minutes

### Step 1: Discover Your Vacuum

```bash
cd c:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/jarvis_vacuum_control.py --discover
```

This will scan your network for smart vacuums. If your vacuum uses miIO protocol (Xiaomi/Roborock/Dreame), it should be discovered automatically.

### Step 2: Get Device Token (if needed)

For miIO devices, you'll need a 32-byte hex token. Here are quick methods:

**Method 1: From Home Assistant** (if you use it)
- Check your Home Assistant configuration
- Token is usually in `.storage/core.config_entries`

**Method 2: From Rooted Device**
- SSH into your vacuum (if rooted)
- Token is in `/mnt/data/miio/device.token`

**Method 3: Network Capture**
- Use Wireshark during app pairing
- Extract token from network packets

### Step 3: Configure Device

Edit `data/jarvis_vacuum/controllers.json` and add your device:

```json
{
  "controllers": [
    {
      "device_id": "my_vacuum",
      "device": {
        "device_id": "my_vacuum",
        "brand": "roborock",
        "protocol": "miio",
        "ip_address": "192.168.1.50",
        "port": 54321,
        "token": "your_32_byte_hex_token_here"
      }
    }
  ]
}
```

### Step 4: Test Connection

```bash
python scripts/python/jarvis_vacuum_control.py --status my_vacuum
```

### Step 5: Start Cleaning!

```bash
python scripts/python/jarvis_vacuum_control.py --start my_vacuum
```

## 📋 Common Commands

```bash
# List all registered devices
python scripts/python/jarvis_vacuum_control.py --list

# Get status
python scripts/python/jarvis_vacuum_control.py --status DEVICE_ID

# Start cleaning
python scripts/python/jarvis_vacuum_control.py --start DEVICE_ID

# Stop cleaning
python scripts/python/jarvis_vacuum_control.py --stop DEVICE_ID

# Return to dock
python scripts/python/jarvis_vacuum_control.py --dock DEVICE_ID

# Start monitoring (continuous status updates)
python scripts/python/jarvis_vacuum_control.py --monitor
```

## 🔧 For iRobot Roomba Users

iRobot devices require BLID and password:

1. **Connect to Roomba's WiFi** (usually starts with "Roomba-")
2. **Use Roomba app** to get credentials
3. **Or use Home Assistant** Roomba integration to extract BLID/password

Then configure in `controllers.json`:

```json
{
  "device_id": "roomba_001",
  "device": {
    "brand": "irobot",
    "protocol": "mqtt",
    "ip_address": "192.168.1.100",
    "blid": "your_blid_here",
    "password": "your_password_here"
  }
}
```

## 🤖 Integration with JARVIS

Once configured, JARVIS can control your vacuum remotely:

```python
from jarvis_vacuum_control import JARVISVacuumControl

control = JARVISVacuumControl()

# Start cleaning
result = control.start_cleaning("my_vacuum")
print(result)

# Get status
status = control.get_status("my_vacuum")
print(f"Battery: {status['status']['battery_level']}%")
```

## 📅 Scheduling

Create automated cleaning schedules:

```python
from jarvis_vacuum_control import JARVISVacuumControl, CleaningTask, CleaningMode, CleaningSchedule

control = JARVISVacuumControl()

# Daily cleaning at 9 AM
task = CleaningTask(
    task_id="daily_morning",
    device_id="my_vacuum",
    mode=CleaningMode.STANDARD,
    schedule=CleaningSchedule.DAILY,
    scheduled_time="09:00",
    enabled=True
)

control.tasks[task.task_id] = task
control._save_tasks()

# Start monitoring to execute scheduled tasks
control.start_monitoring()
```

## 🆘 Troubleshooting

**Device not discovered?**
- Ensure vacuum is on and connected to WiFi
- Check firewall (UDP port 54321 for miIO)
- Try manual configuration

**Connection failed?**
- Verify IP address is correct
- Check token/credentials are valid
- Ensure device is on same network

**Commands not working?**
- Check device status first
- Verify device supports the command
- Review device firmware version

## 📚 Next Steps

- Read full documentation: `docs/jarvis_vacuum_integration.md`
- Explore API integration: `scripts/python/jarvis_vacuum_integration.py`
- Check protocol details: `scripts/python/jarvis_vacuum_protocols.py`

---

**Need help?** Check the logs in `data/jarvis_vacuum/` or review the full integration guide.
