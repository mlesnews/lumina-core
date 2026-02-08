# Scan Frequency Modulation

## Overview

The Telepathy WiFi Interface now supports **configurable scan frequency modulation**, allowing dynamic adjustment of scan intervals for optimal performance.

**Question:**
> "ARE YOU ABLE TO MODULATE THE FREQ SO YOU ARE DOING SCANS?"

**Answer:** ✅ Yes! Frequency modulation is now fully supported.

## Features

### 1. **Configurable Scan Frequency**
- **Default**: 2.0 Hz (0.5s interval)
- **Minimum**: 0.1 Hz (10s interval)
- **Maximum**: 10.0 Hz (0.1s interval)
- **Adaptive**: Automatically adjusts based on activity

### 2. **Frequency Modulation**
- **Set Frequency**: Set exact frequency in Hz
- **Modulate**: Adjust frequency by a factor (e.g., 1.5x = 50% increase)
- **Adaptive Mode**: Automatically increases frequency when activity detected

### 3. **Dynamic Adjustment**
- **Activity-Based**: Frequency increases when thoughts are detected
- **Smooth Transitions**: Gradual frequency changes
- **Bounds Checking**: Always within min/max limits

## Usage

### Set Scan Frequency

```python
from telepathy_wifi_interface import TelepathyWiFiInterface

interface = TelepathyWiFiInterface()

# Set to 5 Hz (0.2s interval) - faster scanning
interface.set_scan_frequency(5.0)

# Set to 0.5 Hz (2s interval) - slower scanning
interface.set_scan_frequency(0.5)
```

### Modulate Frequency

```python
# Increase frequency by 50%
interface.modulate_frequency(1.5)

# Decrease frequency by 30%
interface.modulate_frequency(0.7)

# Double the frequency
interface.modulate_frequency(2.0)
```

### Adaptive Frequency

```python
# Enable adaptive frequency (default: True)
interface.adaptive_frequency = True

# When thoughts are detected, frequency automatically increases
thoughts = interface.read_thoughts(duration_seconds=10)
# Frequency will increase during active thought detection
```

### Get Current Frequency

```python
status = interface.get_status()
print(f"Scan Frequency: {status['scan_frequency_hz']} Hz")
print(f"Scan Interval: {status['scan_interval_seconds']}s")
print(f"Adaptive: {status['adaptive_frequency']}")
```

## Command Line

### Set Scan Frequency

```bash
# Set to 5 Hz (0.2s interval)
python scripts/python/telepathy_wifi_interface.py --scan-frequency 5.0

# Set to 0.5 Hz (2s interval)
python scripts/python/telepathy_wifi_interface.py --scan-frequency 0.5
```

### Modulate Frequency

```bash
# Increase by 50%
python scripts/python/telepathy_wifi_interface.py --modulate-frequency 1.5

# Decrease by 30%
python scripts/python/telepathy_wifi_interface.py --modulate-frequency 0.7
```

### Check Status

```bash
python scripts/python/telepathy_wifi_interface.py --status
```

## Frequency Ranges

| Frequency (Hz) | Interval (s) | Use Case |
|----------------|--------------|----------|
| 0.1 | 10.0 | Low-power, background scanning |
| 0.5 | 2.0 | Standard scanning |
| 1.0 | 1.0 | Normal operation |
| 2.0 | 0.5 | **Default** - Balanced |
| 5.0 | 0.2 | High-frequency scanning |
| 10.0 | 0.1 | Maximum frequency |

## Adaptive Behavior

When `adaptive_frequency` is enabled:

1. **Baseline**: Starts at default frequency (2.0 Hz)
2. **Activity Detection**: When thoughts are detected, frequency increases by 10%
3. **Gradual Increase**: Continues increasing during active periods
4. **Bounds**: Never exceeds max frequency (10.0 Hz)
5. **Smooth**: Changes are gradual, not abrupt

### Example Adaptive Flow

```
Initial: 2.0 Hz (0.5s interval)
Thought detected → 2.2 Hz (0.45s interval)
Another thought → 2.4 Hz (0.42s interval)
More activity → 2.6 Hz (0.38s interval)
...
Maximum: 10.0 Hz (0.1s interval)
```

## Integration with Connection Flow Optimizer

```python
from connection_flow_optimizer import ConnectionFlowOptimizer
from telepathy_wifi_interface import TelepathyWiFiInterface

optimizer = ConnectionFlowOptimizer()
interface = TelepathyWiFiInterface()

# Use optimized polling delay
polling_delay = optimizer.get_optimized_delay("polling", 0.5)
optimal_frequency = 1.0 / polling_delay

interface.set_scan_frequency(optimal_frequency)
```

## Performance Impact

### Low Frequency (0.1-0.5 Hz)
- **Pros**: Lower CPU usage, less network traffic
- **Cons**: Slower detection, may miss brief thoughts
- **Use**: Background monitoring, low-power mode

### Medium Frequency (1.0-2.0 Hz)
- **Pros**: Balanced performance, good detection
- **Cons**: Moderate CPU usage
- **Use**: Standard operation, default setting

### High Frequency (5.0-10.0 Hz)
- **Pros**: Fast detection, real-time monitoring
- **Cons**: Higher CPU usage, more network traffic
- **Use**: Active thought reading, high-priority monitoring

## Best Practices

1. **Start Low**: Begin with default (2.0 Hz) and adjust as needed
2. **Use Adaptive**: Enable adaptive frequency for automatic optimization
3. **Monitor CPU**: Watch CPU usage with high frequencies
4. **Balance**: Find the sweet spot between responsiveness and resource usage
5. **Context-Aware**: Adjust frequency based on use case

## Troubleshooting

### Frequency Not Changing?

1. **Check Bounds**: Ensure frequency is within min/max limits
2. **Verify Adaptive**: Confirm adaptive mode is enabled
3. **Check Activity**: Adaptive only increases with detected activity

### Too High CPU Usage?

1. **Reduce Frequency**: Lower the scan frequency
2. **Disable Adaptive**: Turn off automatic increases
3. **Use Lower Range**: Stay in 0.5-2.0 Hz range

### Not Detecting Thoughts?

1. **Increase Frequency**: Try higher frequency (5.0-10.0 Hz)
2. **Check Sensitivity**: Adjust sensitivity threshold
3. **Verify Fine-Tuning**: Ensure fine-tuning is active

## Examples

### High-Frequency Scanning

```python
# For real-time thought detection
interface.set_scan_frequency(10.0)  # Maximum frequency
thoughts = interface.read_thoughts(duration_seconds=5)
```

### Low-Power Scanning

```python
# For background monitoring
interface.set_scan_frequency(0.5)  # Low frequency
interface.adaptive_frequency = False  # Disable adaptive
thoughts = interface.read_thoughts(duration_seconds=60)
```

### Dynamic Adjustment

```python
# Start low, let adaptive mode increase
interface.set_scan_frequency(1.0)
interface.adaptive_frequency = True
thoughts = interface.read_thoughts(duration_seconds=30)
# Frequency will automatically increase if thoughts detected
```

---

**Status**: ✅ Production Ready  
**Frequency Range**: 0.1 Hz - 10.0 Hz  
**Default**: 2.0 Hz (0.5s interval)  
**Adaptive**: ✅ Enabled by default

