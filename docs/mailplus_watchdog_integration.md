# MailPlus Service Monitoring - Watchdog Integration

## Overview

MailPlus IMAP and SMTP services are now integrated into the LUMINA Watchdog & Guarddog System for continuous monitoring and automatic protection.

---

## Integration Details

### Watchdog Task: `mailplus_service_monitor`

**Configuration:**
- **ID**: `mailplus_service_monitor`
- **Name**: Monitor MailPlus Services
- **Description**: Monitor MailPlus IMAP (993) and SMTP (587) services on NAS
- **Trigger**: Time interval (every 5 minutes)
- **Priority**: Critical
- **Action**: `check_mailplus_services`

**Settings:**
```json
{
  "nas_host": "10.17.17.32",
  "imap_port": 993,
  "smtp_port": 587,
  "auto_restart": true,
  "alert_on_failure": true
}
```

### Guarddog Rules

#### Rule 1: Protect MailPlus IMAP Service
- **ID**: `protect_mailplus_imap`
- **System**: `mailplus`
- **Condition**: `if_service_down`
- **Service**: IMAP (port 993)
- **Action**: `restart` (ensures auto-start configuration)
- **Severity**: Critical

#### Rule 2: Protect MailPlus SMTP Service
- **ID**: `protect_mailplus_smtp`
- **System**: `mailplus`
- **Condition**: `if_service_down`
- **Service**: SMTP (port 587)
- **Action**: `restart` (ensures auto-start configuration)
- **Severity**: Critical

---

## How It Works

### Monitoring Cycle

1. **Every 5 Minutes**: Watchdog checks MailPlus services
   - Tests IMAP port 993 connectivity
   - Tests SMTP port 587 connectivity
   - Logs status (accessible or not)

2. **On Service Failure**:
   - Guarddog rules detect service is down
   - Automatically attempts to ensure auto-start configuration
   - Alerts if services remain down

3. **Auto-Restart**:
   - If `auto_restart` is enabled, watchdog attempts to configure services
   - Ensures MailPlus services are set to start automatically
   - Provides manual configuration instructions if needed

---

## Usage

### Check Status

```bash
python scripts/python/lumina_watchdog_guarddog_system.py --status
```

### Run Monitoring Once

```bash
python scripts/python/lumina_watchdog_guarddog_system.py --run-once
```

### Start Continuous Monitoring

```bash
python scripts/python/lumina_watchdog_guarddog_system.py --start
```

### Check Guarddog Rules

```bash
python scripts/python/lumina_watchdog_guarddog_system.py --check-rules
```

---

## Configuration Files

- **Tasks**: `data/watchdog_guarddog/watchdog_tasks.json`
- **Rules**: `data/watchdog_guarddog/guarddog_rules.json`

---

## Monitoring Output

When MailPlus services are checked, you'll see:

```
📧 Checking MailPlus services...
   ✅ MailPlus services: Both IMAP and SMTP are accessible
```

Or if services are down:

```
📧 Checking MailPlus services...
   ⚠️  MailPlus services: Some services are not accessible
      ❌ IMAP (port 993) is NOT accessible
      ❌ SMTP (port 587) is NOT accessible
   🔄 Attempting to ensure services are configured for auto-start...
   ✅ Auto-start configuration checked
```

---

## Integration with Other Systems

The MailPlus monitoring integrates with:
- **NAS Service Monitor**: Uses existing NAS monitoring infrastructure
- **Auto-Start Configurator**: Calls `ensure_mailplus_autostart.py` for configuration
- **Status Check Scripts**: Uses `check_nas_mail_hub_status.ps1` for verification

---

## Benefits

✅ **Continuous Monitoring**: Services checked every 5 minutes  
✅ **Automatic Protection**: Guarddog rules ensure services stay up  
✅ **Auto-Start Configuration**: Automatically ensures services start on boot  
✅ **Critical Priority**: Treated as critical system service  
✅ **Integrated Logging**: All checks logged in watchdog system  

---

## Troubleshooting

### Services Not Being Monitored

1. Check task is enabled:
   ```bash
   python scripts/python/lumina_watchdog_guarddog_system.py --status
   ```
2. Verify task exists in `watchdog_tasks.json`
3. Check logs for errors

### Services Down But Not Restarting

1. Check guarddog rules are enabled
2. Verify NAS is accessible (10.17.17.32)
3. Check MailPlus services are configured in DSM
4. Review watchdog logs for details

---

*Last Updated: 2026-01-16*  
*Integrated into LUMINA Watchdog & Guarddog System*
