# NAS Cron Daemons - Headless Terminal-less Execution

**Status**: ✅ OPERATIONAL  
**Purpose**: Run JARVIS God Feedback Loop and Lumina Feedback Loop as headless daemons on NAS via cron

---

## Overview

These daemons run JARVIS and Lumina feedback loops as headless, terminal-less processes suitable for NAS cron scheduling. All output is logged to files - no TTY/terminal required.

---

## Daemon Scripts

### 1. JARVIS God Feedback Loop Daemon
**Script**: `scripts/python/jarvis_god_feedback_loop_daemon.py`

**Features**:
- Headless execution (no TTY required)
- File-based logging with rotation
- PID file management
- Signal handling (SIGTERM, SIGINT, SIGHUP)
- Single-cycle mode (for cron) or continuous daemon mode

**Modes**:
- `--cycle`: Run single cycle (for cron one-shot execution)
- `--daemon`: Run as continuous daemon
- `--stop`: Stop running daemon

**Logs**: `data/logs/jarvis_god_loop/jarvis_god_loop_YYYYMMDD.log`

### 2. Lumina Feedback Loop Daemon
**Script**: `scripts/python/lumina_feedback_loop_daemon.py`

**Features**:
- Headless execution (no TTY required)
- File-based logging with rotation
- PID file management
- Signal handling (SIGTERM, SIGINT, SIGHUP)
- Single-cycle mode (for cron) or continuous daemon mode

**Modes**:
- `--cycle`: Run single cycle (for cron one-shot execution)
- `--daemon`: Run as continuous daemon
- `--stop`: Stop running daemon

**Logs**: `data/logs/lumina_feedback_loop/lumina_feedback_loop_YYYYMMDD.log`

---

## Logging

All daemons use Python's `logging` module with:
- **File handlers**: Rotating file handlers (10MB max, 10 backups)
- **Error handlers**: Separate error log files
- **Format**: `%(asctime)s [%(levelname)s] %(name)s: %(message)s`
- **No console output**: stdout/stderr redirected to `/dev/null` when not TTY

**Log Locations**:
- JARVIS God Loop: `data/logs/jarvis_god_loop/`
- Lumina Feedback Loop: `data/logs/lumina_feedback_loop/`

**Log Files**:
- `*_YYYYMMDD.log`: Daily log files
- `*_errors_YYYYMMDD.log`: Error-only log files

---

## NAS Cron Configuration

### Setup

Run the setup script to generate cron configurations:

```bash
python scripts/python/setup_nas_cron_daemons.py
```

This creates:
- `scripts/automation/nas_cron/jarvis_god_loop_cron.conf`
- `scripts/automation/nas_cron/lumina_feedback_loop_cron.conf`
- `scripts/automation/nas_cron/deploy_nas_cron.sh`

### Default Schedule

- **JARVIS God Loop**: Every hour at minute 0
- **Lumina Feedback Loop**: Every hour at minute 30 (offset to avoid overlap)

### Deploy to NAS

#### Option 1: Automated Deployment
```bash
python scripts/python/setup_nas_cron_daemons.py --deploy
```

Requires `nas_kron_daemon_manager.py` and NAS SSH configuration.

#### Option 2: Manual Deployment
```bash
# Copy deploy script to NAS
scp scripts/automation/nas_cron/deploy_nas_cron.sh user@nas:/path/to/project/

# SSH to NAS and run
ssh user@nas
cd /path/to/project
bash deploy_nas_cron.sh
```

#### Option 3: Manual Crontab Edit
```bash
# SSH to NAS
ssh user@nas

# Edit crontab
crontab -e

# Add lines from cron.conf files:
# 0 * * * * cd /path/to/project && /usr/bin/python3 scripts/python/jarvis_god_feedback_loop_daemon.py --cycle >> /dev/null 2>&1
# 30 * * * * cd /path/to/project && /usr/bin/python3 scripts/python/lumina_feedback_loop_daemon.py --cycle >> /dev/null 2>&1
```

---

## Usage Examples

### Run Single Cycle (Manual/Cron)
```bash
# JARVIS God Loop
python scripts/python/jarvis_god_feedback_loop_daemon.py --cycle

# Lumina Feedback Loop
python scripts/python/lumina_feedback_loop_daemon.py --cycle
```

### Run as Continuous Daemon
```bash
# JARVIS God Loop (1 hour interval)
python scripts/python/jarvis_god_feedback_loop_daemon.py --daemon --interval 3600

# Lumina Feedback Loop (1 hour interval)
python scripts/python/lumina_feedback_loop_daemon.py --daemon --interval 3600
```

### Stop Daemon
```bash
# JARVIS God Loop
python scripts/python/jarvis_god_feedback_loop_daemon.py --stop

# Lumina Feedback Loop
python scripts/python/lumina_feedback_loop_daemon.py --stop
```

### Check Logs
```bash
# JARVIS God Loop logs
tail -f data/logs/jarvis_god_loop/jarvis_god_loop_*.log

# Lumina Feedback Loop logs
tail -f data/logs/lumina_feedback_loop/lumina_feedback_loop_*.log

# Error logs
tail -f data/logs/jarvis_god_loop/jarvis_god_loop_errors_*.log
tail -f data/logs/lumina_feedback_loop/lumina_feedback_loop_errors_*.log
```

---

## Headless/TTY-less Design

### Why Headless?
- NAS systems often don't have TTY/terminal attached
- Cron jobs run without interactive shell
- Docker containers may not have TTY
- Background processes don't need console output

### Implementation Details

1. **TTY Detection**: Checks if stdout/stderr are TTYs
2. **Output Redirection**: Redirects to `/dev/null` if not TTY
3. **Logging Only**: All output goes through logging module
4. **No Print Statements**: Uses logger instead of print()
5. **Signal Handling**: Graceful shutdown via signals (no keyboard interrupt needed)

### Code Pattern
```python
# Disable stdout/stderr if not a TTY
if not sys.stdout.isatty():
    sys.stdout = open(os.devnull, 'w')
if not sys.stderr.isatty():
    sys.stderr = open(os.devnull, 'w')

# All output via logger
logger.info("Message")
logger.error("Error message", exc_info=True)
```

---

## PID File Management

Daemons create PID files for process management:

**Location**:
- Linux: `/tmp/{daemon_name}.pid`
- Windows: `%TEMP%\{daemon_name}.pid`

**Files**:
- `jarvis_god_loop_daemon.pid`
- `lumina_feedback_loop_daemon.pid`

**Usage**:
- Check if daemon is running
- Stop daemon via PID
- Prevent duplicate instances

---

## Signal Handling

Daemons handle signals for graceful shutdown:

- **SIGTERM**: Graceful shutdown (default kill signal)
- **SIGINT**: Graceful shutdown (Ctrl+C equivalent)
- **SIGHUP**: Graceful shutdown (if available)

On signal receipt:
1. Set `running = False`
2. Stop feedback loop
3. Remove PID file
4. Exit cleanly

---

## Verification

### Check Daemon Status
```bash
# Check if PID file exists and process is running
ls -la /tmp/jarvis_god_loop_daemon.pid
ps aux | grep jarvis_god_feedback_loop_daemon

# Check cron jobs
crontab -l | grep -E "(jarvis|lumina)"
```

### Test Single Cycle
```bash
# Run single cycle and check exit code
python scripts/python/jarvis_god_feedback_loop_daemon.py --cycle
echo $?  # Should be 0 if successful

# Check logs for cycle completion
tail -20 data/logs/jarvis_god_loop/jarvis_god_loop_*.log
```

### Monitor Execution
```bash
# Watch logs in real-time
tail -f data/logs/jarvis_god_loop/jarvis_god_loop_*.log

# Check for errors
grep -i error data/logs/jarvis_god_loop/jarvis_god_loop_*.log
```

---

## Troubleshooting

### Daemon Won't Start
1. Check if PID file exists (stale PID)
2. Remove PID file: `rm /tmp/{daemon_name}.pid`
3. Check logs for errors
4. Verify Python path in cron configuration

### No Logs Appearing
1. Check log directory permissions
2. Verify log directory exists
3. Check disk space
4. Verify daemon is actually running

### Cron Job Not Running
1. Check cron service: `systemctl status cron` (Linux)
2. Verify cron syntax: `crontab -l`
3. Check cron logs: `/var/log/cron` or `journalctl -u cron`
4. Test command manually outside cron

### Permission Errors
1. Ensure user has write access to log directories
2. Check file permissions on daemon scripts
3. Verify Python executable path in cron

---

## Integration with Existing Systems

### NAS Kron Daemon Manager
The `nas_kron_daemon_manager.py` can deploy these cron configurations automatically:

```python
from nas_kron_daemon_manager import NASKronDaemonManager

manager = NASKronDaemonManager()
manager.deploy_cron_to_nas(Path("scripts/automation/nas_cron/jarvis_god_loop_cron.conf"))
```

### Task Scheduler (Windows)
For Windows systems, use Task Scheduler instead of cron (see `setup_automated_feedback_cycles.py`).

---

## Security Considerations

1. **File Permissions**: Restrict log file permissions (600 or 640)
2. **User Context**: Run as non-root user when possible
3. **Path Security**: Use absolute paths in cron configurations
4. **Log Rotation**: Prevents disk space exhaustion
5. **PID File Security**: Restrict PID file directory permissions

---

## Status

✅ **JARVIS God Feedback Loop Daemon**: OPERATIONAL  
✅ **Lumina Feedback Loop Daemon**: OPERATIONAL  
✅ **Cron Configurations**: GENERATED  
✅ **Logging**: INTEGRATED  
✅ **Headless Mode**: TESTED  

---

## Related Documentation

- `docs/system/JARVIS_MCU_COMPARISON.md`: JARVIS features
- `docs/system/DATA_MINING_FEEDBACK_LOOP_IMPLEMENTATION.md`: Feedback loop details
- `scripts/python/setup_automated_feedback_cycles.py`: Windows Task Scheduler setup
