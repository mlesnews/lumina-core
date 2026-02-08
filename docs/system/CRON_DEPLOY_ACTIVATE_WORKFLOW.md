# Cron Deploy & Activate - Standard Workflow

**CRITICAL: This step MUST be included in ALL workflows that create scheduled services.**

---

## 🚨 MANDATORY WORKFLOW STEP

**After creating ANY service that needs cron scheduling:**

```bash
python scripts/python/deploy_activate_all_cron_services.py
```

**This step is NON-NEGOTIABLE and must ALWAYS be executed.**

---

## ✅ What This Does

1. **Auto-registers** all services with cron scheduler
2. **Initializes** services (triggers auto-registration)
3. **Lists** all registered services
4. **Deploys** to NAS cron scheduler
5. **Verifies** deployment

---

## 📋 Standard Workflow

### When Creating New Scheduled Service:

1. **Create service** with auto-registration in `__init__`
2. **Test service** works correctly
3. **EXECUTE DEPLOY & ACTIVATE:**
   ```bash
   python scripts/python/deploy_activate_all_cron_services.py
   ```
4. **Verify** services are registered and deployed

---

## 🔄 Integration Points

### After Service Creation

**ALWAYS run:**
```bash
python scripts/python/deploy_activate_all_cron_services.py
```

### After Multiple Service Updates

**ALWAYS run:**
```bash
python scripts/python/deploy_activate_all_cron_services.py
```

### Before Deployment

**ALWAYS run:**
```bash
python scripts/python/deploy_activate_all_cron_services.py
```

---

## ✅ Verification Checklist

After running deploy & activate, verify:

- [ ] Services are registered (check output)
- [ ] Services appear in cron scheduler
- [ ] All services are enabled
- [ ] Schedules are correct
- [ ] Commands are correct

---

## 📊 Current Status

**Registered Services:**
- ✅ LUMINA Intelligence Collection - Hourly (`0 * * * *`)
- ✅ LUMINA Intelligence Collection - Daily (`0 2 * * *`)

**Total Cron Jobs:** 7 (all enabled)

---

## 🚨 REMINDER

**DO NOT SKIP THIS STEP.**

Every time you create or modify a scheduled service:
1. Run `deploy_activate_all_cron_services.py`
2. Verify output
3. Confirm services are registered

---

**Tags:** #CRON #WORKFLOW #MANDATORY #DEPLOY #ACTIVATE @JARVIS @LUMINA
