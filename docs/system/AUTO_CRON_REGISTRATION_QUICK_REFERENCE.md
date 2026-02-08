# Auto Cron Registration - Quick Reference

**Quick guide for automatically registering services with cron scheduler**

---

## 🚀 Quick Start

### Register All Services

```bash
python scripts/python/register_all_cron_services.py
```

### View Registered Services

```bash
python scripts/python/auto_cron_registration.py --list
```

### Deploy to NAS

```bash
python scripts/python/auto_cron_registration.py --deploy
```

---

## 📋 Adding New Scheduled Service

### In Service `__init__`:

```python
from auto_cron_registration import CronScheduleConfig, get_registry

# In __init__ method:
try:
    registry = get_registry()
    registry.register_service(
        service_id="my-service-id",
        service_name="My Service Name",
        script_path="scripts/python/my_service.py",
        schedule_config=CronScheduleConfig.hourly(minute=0),
        command_template="python /volume1/docker/lumina/scripts/python/my_service.py --run",
        auto_deploy=True
    )
except Exception as e:
    logger.debug(f"Could not auto-register: {e}")
```

---

## ⚙️ Schedule Types

```python
# Hourly
CronScheduleConfig.hourly(minute=0)

# Daily
CronScheduleConfig.daily(hour=2, minute=0)

# Weekly
CronScheduleConfig.weekly(day=1, hour=0, minute=0)

# Custom
CronScheduleConfig.custom("0 */6 * * *")
```

---

## ✅ Verification

```bash
# List registered
python scripts/python/auto_cron_registration.py --list

# Check NAS cron
python scripts/python/nas_cron_scheduler.py --list-jobs
```

---

**Tags:** #CRON #QUICK_REFERENCE @JARVIS @LUMINA
