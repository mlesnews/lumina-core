# Cursor Tasks to NAS Cron - Deployment Status

**Date**: 2026-01-02  
**Status**: ⚠️ **READY FOR MANUAL DEPLOYMENT**  
**Tag**: #CURSOR #NAS #CRON #DEPLOYMENT

---

## Status

✅ **Conversion**: Complete - 5 tasks converted  
⚠️ **Deployment**: Manual deployment required (Synology DSM uses different cron system)

---

## Converted Tasks

| Task | Schedule | Command |
|------|----------|---------|
| JARVIS: Auto Git Commit | `0 */6 * * *` | Every 6 hours |
| JARVIS: Health Check | `0 */2 * * *` | Every 2 hours |
| JARVIS: Cursor IDE Optimization | `0 0 * * 0` | Weekly (Sunday) |
| JARVIS: Monitor IDE Notifications | `*/15 * * * *` | Every 15 minutes |
| SSO: Verify Readiness | `0 8 * * *` | Daily at 8 AM |

---

## Generated Files

- ✅ `scripts/nas/cron/cursor_tasks_cron.json` - JSON config
- ✅ `scripts/nas/cron/cursor_tasks_crontab.txt` - Crontab format
- ✅ `scripts/nas/cron/dsm_scheduler_import.sh` - DSM script

---

## Manual Deployment Options

### Option 1: DSM Task Scheduler (Recommended)

1. **Open DSM**: https://10.17.17.32:5001
2. **Control Panel** → **Task Scheduler**
3. **Create** → **Scheduled Task** → **User-defined script**

For each task:

1. **Task Name**: `JARVIS: Auto Git Commit`
2. **User**: `root`
3. **Schedule**: 
   - **Run on the following days**: Select days
   - **Time**: Set time (e.g., Every 6 hours)
4. **Task Settings** → **User-defined script**:
   ```bash
   python /volume1/lumina/scripts/python/jarvis_auto_git_manager.py --auto-commit --message '[AUTO] Auto-commit changes'
   ```
5. **Save** and **Enable**

### Option 2: SSH Manual Crontab

1. **SSH to NAS**:
   ```bash
   ssh admin@10.17.17.32
   ```

2. **Switch to root**:
   ```bash
   sudo su -
   ```

3. **Check if crontab exists**:
   ```bash
   which crontab
   # Or try:
   /usr/bin/crontab -l
   ```

4. **If crontab works, add tasks**:
   ```bash
   crontab -e
   # Add lines from cursor_tasks_crontab.txt
   ```

5. **If crontab doesn't work**, use DSM Task Scheduler instead.

### Option 3: Review Generated Files

Review the generated files and manually create tasks in DSM:

```bash
# View crontab format
cat scripts/nas/cron/cursor_tasks_crontab.txt

# View JSON config
cat scripts/nas/cron/cursor_tasks_cron.json
```

---

## Cron Tasks Ready for Deployment

### 1. JARVIS: Auto Git Commit
```cron
0 */6 * * * python /volume1/lumina/scripts/python/jarvis_auto_git_manager.py --auto-commit --message [AUTO] Auto-commit changes
```

### 2. JARVIS: Health Check
```cron
0 */2 * * * python /volume1/lumina/scripts/python/jarvis_health_check.py
```

### 3. JARVIS: Cursor IDE Optimization
```cron
0 0 * * 0 python /volume1/lumina/scripts/python/jarvis_cursor_ide_engineer.py --optimize
```

### 4. JARVIS: Monitor IDE Notifications
```cron
*/15 * * * * python /volume1/lumina/scripts/python/jarvis_ide_notification_monitor.py --monitor
```

### 5. SSO: Verify Readiness
```cron
0 8 * * * python /volume1/lumina/scripts/python/verify_sso_readiness.py --nas-ip 10.17.17.32 --vault-name jarvis-lumina
```

---

## Next Steps

1. ✅ **Conversion Complete** - Tasks converted to NAS cron format
2. ⏳ **Manual Deployment** - Use DSM Task Scheduler to add tasks
3. ⏳ **Verification** - Test each task manually first
4. ⏳ **Monitoring** - Check logs after deployment

---

## Troubleshooting

### Issue: Crontab Command Not Found

**Solution**: Synology DSM may use DSM Task Scheduler instead of standard crontab. Use DSM Task Scheduler (Option 1) instead.

### Issue: Python Path Not Found

**Solution**: Verify Python path on NAS:
```bash
ssh admin@10.17.17.32
which python
# Or try:
which python3
```

Update commands in DSM Task Scheduler to use correct Python path.

### Issue: Script Path Not Found

**Solution**: Verify scripts exist on NAS:
```bash
ssh admin@10.17.17.32
ls -la /volume1/lumina/scripts/python/
```

If scripts don't exist, sync them to NAS first.

---

## Files Location

- **Conversion Script**: `scripts/python/convert_cursor_tasks_to_nas_cron.py`
- **Deployment Script**: `scripts/python/deploy_cursor_tasks_to_nas.py`
- **Generated Cron**: `scripts/nas/cron/cursor_tasks_crontab.txt`
- **JSON Config**: `scripts/nas/cron/cursor_tasks_cron.json`

---

**Last Updated**: 2026-01-02  
**Status**: Ready for manual deployment via DSM Task Scheduler
