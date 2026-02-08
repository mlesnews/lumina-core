# TradingView Desktop Explorer & Controller

## Overview

Comprehensive exploration, keyboard shortcut mapping, and control system for TradingView Desktop with MANUS mouse fallback and SMS/Email notifications for important events.

## Features

### 1. Application Exploration
- **Desktop Detection**: Automatically detects TradingView Desktop application
- **Process Monitoring**: Tracks application process ID and window state
- **UI Element Mapping**: Maps toolbar, chart area, side panels, and status bar
- **Application Structure**: Documents panels, features, data sources, and integrations

### 2. Keyboard Shortcut Mapping
- **33 Keyboard Shortcuts** mapped across categories:
  - Navigation (5 shortcuts)
  - Chart Operations (16 shortcuts)
  - Indicators (2 shortcuts)
  - Alerts (2 shortcuts)
  - Trading (2 shortcuts)
  - Analysis (3 shortcuts)
  - View (2 shortcuts)
  - Settings (1 shortcut)

### 3. MANUS Mouse Control Fallback
- **Automatic Fallback**: If keyboard shortcuts fail, uses MANUS mouse cursor control
- **Seamless Integration**: Works with existing MANUS Unified Control system
- **Reliable Execution**: Ensures actions complete even if keyboard fails

### 4. SMS & Email Notifications
- **SMS Notifications**: Sends SMS to both phone numbers for important events
- **Email Notifications**: Sends detailed email with event information
- **Event Severity Levels**: INFO, WARNING, ERROR, CRITICAL
- **Automatic Routing**: Notifications sent based on event severity

## Usage

### Basic Exploration

```python
from scripts.python.jarvis_tradingview_desktop_explorer import TradingViewDesktopExplorer

explorer = TradingViewDesktopExplorer()

# Explore application
exploration = await explorer.explore_application()
print(exploration)
```

### Execute Keyboard Shortcut

```python
# Execute keyboard shortcut
result = explorer.execute_keyboard_shortcut("Open Symbol Search")
# or
result = explorer.execute_keyboard_shortcut("Ctrl+K")

# With MANUS fallback (default)
result = explorer.execute_keyboard_shortcut("Add Indicator", fallback_to_mouse=True)
```

### Record Event with Notifications

```python
# Record event that requires notifications
event = explorer.record_event(
    event_type="ALERT_TRIGGERED",
    severity="CRITICAL",
    message="Price alert triggered for BTCUSDT",
    details={
        "symbol": "BTCUSDT",
        "price": 45000.0,
        "alert_type": "price_above"
    },
    requires_notification=True  # This will trigger SMS and Email
)
```

## Keyboard Shortcuts

### Navigation
- `Ctrl+K` - Open Symbol Search
- `Ctrl+G` - Go to Symbol
- `Ctrl+Tab` - Switch Chart
- `Ctrl+N` - New Chart
- `Ctrl+W` - Close Chart

### Chart Operations
- `Ctrl++` - Zoom In
- `Ctrl+-` - Zoom Out
- `Ctrl+0` - Reset Zoom
- `Ctrl+F` - Fit to Screen
- `Left Arrow` - Scroll Left
- `Right Arrow` - Scroll Right
- `D` - Drawing Tools
- `C` - Toggle Crosshair

### Timeframes
- `1` - 1 Minute
- `5` - 5 Minutes
- `15` - 15 Minutes
- `H` - 1 Hour
- `4` - 4 Hours
- `D` - 1 Day
- `W` - 1 Week
- `M` - 1 Month

### Indicators & Tools
- `Ctrl+I` - Add Indicator
- `Delete` - Remove Indicator

### Alerts
- `Ctrl+Alt+A` - Create Alert
- `Ctrl+Alt+L` - Alert List

### Trading
- `Ctrl+T` - Trading Panel
- `Ctrl+E` - Order Entry

### Analysis
- `Ctrl+S` - Screener
- `Ctrl+W` - Watchlist
- `Ctrl+I` - Symbol Info

### View & Settings
- `F11` - Full Screen
- `Ctrl+L` - Layouts
- `Ctrl+,` - Settings

## Event Monitoring

### Event Types
- `ALERT_TRIGGERED` - Trading alert triggered
- `PRICE_ALERT` - Price level reached
- `INDICATOR_SIGNAL` - Indicator generated signal
- `ERROR` - Application error
- `WARNING` - Warning condition
- `INFO` - Informational event

### Event Severity
- `INFO` - Informational, no notification
- `WARNING` - Warning condition, optional notification
- `ERROR` - Error condition, notification recommended
- `CRITICAL` - Critical event, notification required

### Notification Configuration

SMS notifications require:
- Twilio credentials in Azure Vault:
  - `twilio-account-sid`
  - `twilio-auth-token`
  - `twilio-phone-number`
- Phone numbers in Azure Vault:
  - `matthew-phone-number` (or similar)
  - `phone-number-1`, `phone-number-2`
  - `primary-phone`, `secondary-phone`

Email notifications require:
- SMTP configuration in Azure Vault:
  - `smtp-server` (default: 10.17.17.32)
  - `smtp-port` (default: 587)
  - `email-username`
  - `email-password`
  - `email-from`
- Email recipients:
  - `email-to`, `email-recipient`
  - `matthew-email`, `primary-email`, `secondary-email`

## MANUS Integration

The explorer integrates with MANUS Unified Control for mouse cursor fallback:

```python
# MANUS automatically used if keyboard fails
result = explorer.execute_keyboard_shortcut("Add Indicator")
# If keyboard fails, MANUS mouse control takes over
```

## Data Storage

### Exploration Data
- Location: `data/tradingview_desktop_exploration/`
- Files:
  - `keyboard_shortcuts.json` - Keyboard shortcut mappings
  - `events.json` - Event history
  - `exploration_YYYYMMDD_HHMMSS.json` - Exploration results

### Event History
All events are stored with:
- Event ID
- Event type and severity
- Message and details
- Timestamp
- Notification status

## Status

### Current Status
- ✅ TradingView Desktop detected (PID: 3348)
- ✅ 33 keyboard shortcuts mapped
- ✅ UI elements mapped
- ✅ Application structure documented
- ✅ MANUS mouse control integrated
- ✅ SMS notification service ready
- ✅ Email notification service ready
- ⚠️ Phone numbers need to be added to Azure Vault
- ⚠️ Email credentials need to be configured

## Next Steps

1. **Add Phone Numbers to Azure Vault**:
   ```bash
   # Add your phone numbers
   az keyvault secret set --vault-name jarvis-lumina --name matthew-phone-number --value "+1234567890"
   az keyvault secret set --vault-name jarvis-lumina --name phone-number-2 --value "+0987654321"
   ```

2. **Configure Email Settings**:
   ```bash
   # Add email configuration
   az keyvault secret set --vault-name jarvis-lumina --name email-username --value "your-email@domain.com"
   az keyvault secret set --vault-name jarvis-lumina --name email-password --value "your-password"
   az keyvault secret set --vault-name jarvis-lumina --name email-to --value "recipient@domain.com"
   ```

3. **Test Notifications**:
   ```python
   # Test with a critical event
   event = explorer.record_event(
       event_type="TEST",
       severity="CRITICAL",
       message="Test notification",
       requires_notification=True
   )
   ```

## Tags

@JARVIS @TRADINGVIEW @DESKTOP @EXPLORATION @KEYBOARD_SHORTCUTS @MANUS @SMS @EMAIL @NOTIFICATIONS
