# Auto Cron Registration System - Complete

**Status:** ✅ Complete - Services automatically register with cron scheduler

---

## 🎯 Mission

**Problem:** Services that need regular cron schedules were being created but not automatically registered, leaving them unused.

**Solution:** Automatic cron registration system that:
- Detects services needing scheduling
- Automatically registers them with NASCronScheduler
- Ensures no scheduled service is left unused
- Applies dynamic/evolutionary principles (Adapt, Improvise, Overcome)

---

## 🏗️ Architecture

### Components

1. **AutoCronRegistry** - Central registry for all scheduled services
2. **CronScheduleConfig** - Configuration for cron schedules
3. **@cron_scheduled decorator** - Decorator for automatic registration
4. **Auto-registration on initialization** - Services register themselves when created

### Integration Points

- **NASCronScheduler** - Integrates with existing cron scheduler
- **Service initialization** - Services auto-register in `__init__`
- **Registry persistence** - Stores registered services in `data/auto_cron/registered_services.json`

---

## 📋 Usage

### Method 1: Auto-Registration on Service Creation

When creating a service that needs scheduling, add auto-registration in `__init__`:

```python
from auto_cron_registration import CronScheduleConfig, get_registry

class MyScheduledService:
    def __init__(self, project_root: Optional[Path] = None):
        # ... initialization code ...
        
        # Auto-register with cron scheduler
        try:
            from auto_cron_registration import CronScheduleConfig, get_registry
            registry = get_registry()
            
            registry.register_service(
                service_id="my-service-hourly",
                service_name="My Service - Hourly",
                script_path="scripts/python/my_service.py",
                schedule_config=CronScheduleConfig.hourly(
                    minute=0,
                    description="Hourly service execution",
                    tags=["my_service", "hourly"]
                ),
                command_template="python /volume1/docker/lumina/scripts/python/my_service.py --run-hourly",
                auto_deploy=True
            )
        except Exception as e:
            logger.debug(f"Could not auto-register: {e}")
```

### Method 2: Using Decorator (for functions)

```python
from auto_cron_registration import cron_scheduled, CronScheduleConfig

@cron_scheduled(
    CronScheduleConfig.daily(hour=2, description="Daily task"),
    service_id="my-daily-task",
    service_name="My Daily Task"
)
def my_daily_task():
    # Task implementation
    pass
```

### Method 3: Manual Registration

```python
from auto_cron_registration import CronScheduleConfig, get_registry

registry = get_registry()
registry.register_service(
    service_id="my-service",
    service_name="My Service",
    script_path="scripts/python/my_service.py",
    schedule_config=CronScheduleConfig.hourly(minute=30),
    auto_deploy=True
)
```

---

## ⚙️ Schedule Configuration

### Predefined Schedules

```python
# Hourly (at minute 0)
CronScheduleConfig.hourly(minute=0, description="Hourly task")

# Daily (at 2:00 AM)
CronScheduleConfig.daily(hour=2, minute=0, description="Daily task")

# Weekly (Monday at midnight)
CronScheduleConfig.weekly(day=1, hour=0, minute=0, description="Weekly task")

# Custom cron expression
CronScheduleConfig.custom("0 */6 * * *", description="Every 6 hours")
```

### Schedule Options

- `schedule`: Cron expression (e.g., "0 * * * *")
- `frequency`: ScheduleFrequency enum (HOURLY, DAILY, WEEKLY, MONTHLY, CUSTOM)
- `enabled`: Whether the schedule is enabled
- `description`: Human-readable description
- `tags`: List of tags for categorization
- `metadata`: Additional metadata

---

## 🔄 Auto-Registration Flow

1. **Service Created** → Service initializes
2. **Auto-Registration Triggered** → Service calls `get_registry().register_service()`
3. **Registry Check** → Checks if already registered
4. **Scheduler Integration** → Adds to NASCronScheduler if available
5. **Persistence** → Saves to registry file
6. **Deployment** → Optionally deploys to NAS cron

---

## 📊 Registered Services

### View Registered Services

```bash
python scripts/python/auto_cron_registration.py --list
```

### Auto-Register Existing Services

```bash
python scripts/python/register_all_cron_services.py
```

This will:
- Scan for services needing registration
- Register them automatically
- Show all registered services

---

## 🚀 Deployment

### Deploy All Registered Services to NAS

```bash
python scripts/python/auto_cron_registration.py --deploy
```

Or use the NAS scheduler directly:

```bash
python scripts/python/nas_cron_scheduler.py --deploy
```

---

## 📁 File Structure

```
data/
  auto_cron/
    registered_services.json    # Registry of all registered services

scripts/python/
  auto_cron_registration.py     # Core registration system
  register_all_cron_services.py # Registration script
  nas_cron_scheduler.py         # NAS cron scheduler (existing)
```

---

## ✅ Currently Registered Services

1. **LUMINA Intelligence Collection - Hourly**
   - Schedule: `0 * * * *` (Every hour at minute 0)
   - Command: `python .../lumina_intelligence_collection.py --collect-hourly`
   - Tags: intelligence, hourly, data_collection

2. **LUMINA Intelligence Collection - Daily**
   - Schedule: `0 2 * * *` (Daily at 2:00 AM)
   - Command: `python .../lumina_intelligence_collection.py --aggregate-daily`
   - Tags: intelligence, daily, aggregation

---

## 🔍 Verification

### Check Registry

```bash
python scripts/python/auto_cron_registration.py --list
```

### Check NAS Cron Jobs

```bash
python scripts/python/nas_cron_scheduler.py --list-jobs
```

### Verify Deployment

```bash
# SSH to NAS and check crontab
ssh mlesn@10.17.17.32 "crontab -l"
```

---

## 🎯 Best Practices

### When Creating New Scheduled Services

1. **Add auto-registration in `__init__`**
   - Use `get_registry().register_service()`
   - Provide clear service ID and name
   - Set appropriate schedule

2. **Use descriptive names**
   - Service ID: `service-name-frequency` (e.g., `lumina-intelligence-hourly`)
   - Service Name: Human-readable (e.g., "LUMINA Intelligence Collection - Hourly")

3. **Set appropriate tags**
   - Helps with categorization
   - Enables filtering and grouping

4. **Test registration**
   - Run `register_all_cron_services.py` after creating service
   - Verify it appears in the list

5. **Deploy after registration**
   - Run `--deploy` to deploy to NAS
   - Verify cron jobs are active

---

## 🔄 Dynamic/Evolutionary Principles

The system applies LUMINA's core values:

- **Adapt**: Automatically adapts to new services
- **Improvise**: Flexible schedule configuration
- **Overcome**: Ensures no service is left unused

### Evolution Features

- Services can update their schedules
- Registry tracks changes
- Scheduler can evolve based on effectiveness

---

## 📝 Example: Adding New Scheduled Service

```python
# In your service file
from auto_cron_registration import CronScheduleConfig, get_registry

class MyNewService:
    def __init__(self, project_root: Optional[Path] = None):
        # ... your initialization ...
        
        # Auto-register
        try:
            registry = get_registry()
            registry.register_service(
                service_id="my-new-service",
                service_name="My New Service",
                script_path="scripts/python/my_new_service.py",
                schedule_config=CronScheduleConfig.hourly(
                    minute=15,
                    description="My new service runs every hour at :15",
                    tags=["my_service", "hourly"]
                ),
                command_template="python /volume1/docker/lumina/scripts/python/my_new_service.py --run",
                auto_deploy=True
            )
        except Exception as e:
            logger.debug(f"Could not auto-register: {e}")
```

Then run:

```bash
python scripts/python/register_all_cron_services.py
```

---

## ✅ Summary

**Problem Solved:**
- ✅ Services automatically register with cron when created
- ✅ No scheduled service left unused
- ✅ Integrated with existing NASCronScheduler
- ✅ Persistent registry
- ✅ Easy deployment to NAS

**Current Status:**
- ✅ Auto-registration system created
- ✅ LUMINA Intelligence Collection registered
- ✅ Registry persistence working
- ✅ Integration with NASCronScheduler complete

**Next Steps:**
- Add more services as needed
- Deploy to NAS when ready
- Monitor registered services

---

**Tags:** #CRON #AUTOMATION #SCHEDULING #REGISTRATION @JARVIS @LUMINA @PEAK @DTN @EVO
