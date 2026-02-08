# JARVIS Vacuum Integration Guide

## Overview

JARVIS Vacuum Integration enables intelligent remote control of smart vacuum cleaners through the JARVIS ecosystem. The system supports multiple vacuum brands and protocols, providing a unified interface for automation and intelligent scheduling.

## Supported Brands & Protocols

### miIO Protocol (Xiaomi/Roborock/Dreame)
- **Protocol**: UDP on port 54321
- **Authentication**: 32-byte hex token
- **Discovery**: Automatic via UDP broadcast
- **Token Retrieval**:
  - From rooted device filesystem
  - Via older Xiaomi app versions
  - Using Home Assistant integration methods

### MQTT Protocol (iRobot Roomba)
- **Protocol**: Local MQTT broker on robot
- **Authentication**: BLID + robot password
- **Discovery**: Manual (requires connecting to robot's WiFi)
- **Credentials**:
  - Connect to Roomba's WiFi network
  - Use Roomba app or Home Assistant integration

### Tuya Protocol (Eufy and other Tuya-based)
- **Protocol**: LAN UDP/TCP
- **Authentication**: devId + localKey
- **Discovery**: Manual
- **Credentials**:
  - Via Tuya app logcat (Android)
  - Using Tuya developer tools
  - Home Assistant custom integrations

### Ecovacs Protocol
- **Protocol**: HTTP + MQTT over TLS
- **Authentication**: Ecovacs account + device binding
- **Discovery**: Via Ecovacs API
- **Libraries**: deebot-client, deebotozmo

## Quick Start

### 1. Discovery

Discover vacuum cleaners on your network:

```bash
python scripts/python/jarvis_vacuum_control.py --discover
```

This will:
- Scan network for miIO devices (Xiaomi/Roborock/Dreame)
- Attempt to identify device brand and model
- Save discovered devices to `data/jarvis_vacuum/discovered_devices.json`

### 2. Manual Configuration

For devices that require manual configuration (iRobot, Tuya, Ecovacs), you'll need to:

1. **Obtain credentials** (see brand-specific sections above)
2. **Edit configuration** in `data/jarvis_vacuum/controllers.json`
3. **Add device manually**:

```python
from jarvis_vacuum_control import JARVISVacuumControl
from jarvis_vacuum_discovery import VacuumDevice, VacuumBrand, VacuumProtocol

control = JARVISVacuumControl()

# Create device manually
device = VacuumDevice(
    device_id="roomba_001",
    brand=VacuumBrand.IROBOT,
    protocol=VacuumProtocol.MQTT,
    ip_address="192.168.1.100",
    blid="your_blid_here",
    password="your_password_here"
)

# Register controller
controller = VacuumController(
    device_id="roomba_001",
    device=device
)
control.controllers["roomba_001"] = controller
control._save_controllers()
```

### 3. Control

#### Start Cleaning

```bash
python scripts/python/jarvis_vacuum_control.py --start DEVICE_ID
```

#### Stop Cleaning

```bash
python scripts/python/jarvis_vacuum_control.py --stop DEVICE_ID
```

#### Return to Dock

```bash
python scripts/python/jarvis_vacuum_control.py --dock DEVICE_ID
```

#### Get Status

```bash
python scripts/python/jarvis_vacuum_control.py --status DEVICE_ID
# or for all devices:
python scripts/python/jarvis_vacuum_control.py --status all
```

### 4. Monitoring

Start continuous monitoring:

```bash
python scripts/python/jarvis_vacuum_control.py --monitor
```

This will:
- Update device status every 30 seconds
- Check and execute scheduled cleaning tasks
- Log status changes and events

## Intelligent Scheduling

### Creating Cleaning Tasks

Tasks can be created programmatically or via configuration:

```python
from jarvis_vacuum_control import JARVISVacuumControl, CleaningTask, CleaningMode, CleaningSchedule

control = JARVISVacuumControl()

task = CleaningTask(
    task_id="daily_cleaning",
    device_id="vacuum_001",
    mode=CleaningMode.STANDARD,
    schedule=CleaningSchedule.DAILY,
    scheduled_time="09:00",  # 9 AM daily
    priority=7,
    enabled=True
)

control.tasks[task.task_id] = task
control._save_tasks()
```

### Schedule Types

- **MANUAL**: On-demand only (no automatic execution)
- **DAILY**: Once per day at specified time
- **MULTIPLE**: Multiple times per day (configure via metadata)
- **SMART**: AI-driven based on patterns (future feature)

### Cleaning Modes

- **QUICK**: Fast pass cleaning
- **STANDARD**: Normal cleaning cycle
- **DEEP**: Thorough cleaning
- **SPOT**: Clean specific area
- **ROOM**: Clean specific room(s)

## API Integration

### JARVIS Unified API

The vacuum system integrates with JARVIS unified API for remote control:

```python
from jarvis_unified_api import JARVISUnifiedAPI, RequestType, APIRequest

api = JARVISUnifiedAPI()

# Discover vacuums
request = APIRequest(
    request_id="req_001",
    request_type=RequestType.COMMAND,
    source="user",
    target="vacuum",
    payload={"action": "discover"}
)
response = api.process_request(request)

# Start cleaning
request = APIRequest(
    request_id="req_002",
    request_type=RequestType.COMMAND,
    source="user",
    target="vacuum",
    payload={
        "action": "start",
        "device_id": "vacuum_001",
        "mode": "standard"
    }
)
response = api.process_request(request)
```

## Configuration

### Main Configuration

Edit `config/jarvis_vacuum_config.json`:

```json
{
  "monitoring_enabled": true,
  "status_update_interval": 30,
  "auto_connect": true,
  "intelligent_scheduling": true,
  "default_cleaning_mode": "standard"
}
```

### Device Configuration

Devices are stored in `data/jarvis_vacuum/controllers.json`. Example:

```json
{
  "controllers": [
    {
      "device_id": "roborock_s7",
      "device": {
        "device_id": "roborock_s7",
        "brand": "roborock",
        "model": "S7",
        "protocol": "miio",
        "ip_address": "192.168.1.50",
        "port": 54321,
        "token": "your_32_byte_hex_token_here"
      },
      "is_connected": false
    }
  ]
}
```

## Token/Key Retrieval

### miIO Token (Xiaomi/Roborock/Dreame)

1. **From Rooted Device**:
   - SSH into device
   - Token stored in `/mnt/data/miio/device.token` or similar

2. **Via App**:
   - Use older Xiaomi app versions
   - Check app backup files
   - Use Home Assistant integration methods

3. **Via Network Sniffing**:
   - Capture traffic during app pairing
   - Extract token from packets

### iRobot BLID + Password

1. **Via Roomba WiFi**:
   - Connect to Roomba's WiFi network
   - Use Roomba app to obtain credentials
   - Or use Home Assistant Roomba integration

2. **Via Local MQTT**:
   - Connect to robot's MQTT broker
   - Credentials visible in connection process

### Tuya devId + localKey

1. **Via Android Logcat**:
   - Use specific Eufy app versions
   - Monitor logcat during device pairing
   - Extract devId and localKey

2. **Via Tuya Developer Tools**:
   - Requires Tuya developer account
   - Use Tuya IoT platform

## Troubleshooting

### Device Not Discovered

- Ensure vacuum is powered on and connected to WiFi
- Check firewall settings (UDP port 54321 for miIO)
- Try manual configuration if automatic discovery fails
- Verify device is on same network segment

### Connection Failed

- Verify IP address is correct
- Check token/credentials are valid
- Ensure device firmware is compatible
- Try re-pairing device with official app

### Commands Not Working

- Verify device is connected (`--status` command)
- Check device supports the command
- Review device logs/status for errors
- Some commands may require specific firmware versions

## Advanced Features

### Custom Protocol Handlers

Extend `VacuumProtocolHandler` to add support for new brands:

```python
from jarvis_vacuum_protocols import VacuumProtocolHandler, VacuumStatus, VacuumState

class CustomProtocolHandler(VacuumProtocolHandler):
    def connect(self) -> bool:
        # Implement connection logic
        pass

    def get_status(self) -> Optional[VacuumStatus]:
        # Implement status retrieval
        pass

    # ... implement other methods
```

### Event Handlers

Register event handlers for automation:

```python
def on_cleaning_complete(device_id: str, status: VacuumStatus):
    print(f"Cleaning complete on {device_id}")

control.event_handlers["cleaning_complete"] = [on_cleaning_complete]
```

## Security Notes

- **Never commit tokens/credentials** to version control
- **Use secure storage** for sensitive credentials
- **Consider local-only operation** to avoid cloud dependencies
- **Keep firmware updated** for security patches
- **Review network access** - devices may phone home

## Future Enhancements

- [ ] Full miIO encryption implementation
- [ ] Room mapping and navigation
- [ ] AI-driven scheduling based on occupancy
- [ ] Integration with home automation systems
- [ ] Multi-zone cleaning strategies
- [ ] Obstacle detection and avoidance
- [ ] Voice control integration
- [ ] Mobile app interface

## Resources

- [python-miio Documentation](https://python-miio.readthedocs.io/)
- [Valetudo Project](https://valetudo.cloud/)
- [Home Assistant Integrations](https://www.home-assistant.io/integrations/)
- [Roomba Python Libraries](https://github.com/pschmitt/roombapy)

## Support

For issues or questions:
- Check device-specific documentation
- Review protocol handler implementations
- Consult community resources (Home Assistant, Valetudo)
- Check JARVIS logs in `data/jarvis_vacuum/`

---

**Tags**: #JARVIS #VACUUM #IoT #HOME_AUTOMATION #INTEGRATION @JARVIS @LUMINA
