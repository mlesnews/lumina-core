# APICLI Endpoint @BAU Daemon

**Status**: ✅ **ACTIVE**  
**Date**: 2026-01-12  
**Tags**: `#APICLI` `#BAU` `#V3` `#HEALTH_CHECK` `#DAEMON` `#NAS` `#CRON` `@JARVIS` `@LUMINA`

---

## Overview

The APICLI Endpoint @BAU Daemon is an automated, scheduled, recurring NAS cron scheduler task/daemon that runs APICLI endpoint updates at configured intervals as part of **@bau (Business As Usual)** workflows.

### Multiple Intervals (x1+)

The system supports **multiple intervals** for different check types:

1. **@v3 Verification**: Every 15-30 minutes (configurable)
   - Less frequent, more comprehensive
   - First pass verification
   - Validates endpoint accessibility and health

2. **Health Checks**: Every 5-10 minutes (configurable)
   - More frequent, lighter checks
   - Second pass health and welfare checks
   - Monitors datapoints and painpoints

3. **Full Update**: Every hour (configurable)
   - Comprehensive endpoint update
   - Includes both @v3 verification and health checks
   - Complete reporting

---

## Architecture

### Daemon Components

1. **APICLIEndpointBAUDaemon** (`apicli_endpoint_bau_daemon.py`)
   - Headless daemon for automated execution
   - Supports multiple check modes
   - Full logging to files
   - Signal handling for graceful shutdown

2. **Cron Scheduler Setup** (`setup_apicli_bau_cron.py`)
   - Generates cron configurations
   - Creates deployment scripts
   - Configurable intervals
   - NAS integration

### Check Modes

- **`v3_only`**: Run only @v3 verification (first pass)
- **`health_only`**: Run only health and welfare checks (second pass)
- **`full`**: Run comprehensive update (both passes)

---

## Default Intervals

### Recommended Configuration

```json
{
  "v3_verification": 15,  // Every 15 minutes
  "health_check": 5,      // Every 5 minutes
  "full_update": 60       // Every hour
}
```

### Rationale

- **@v3 Verification (15 min)**: Comprehensive verification takes longer, so less frequent
- **Health Checks (5 min)**: Lightweight checks can run more frequently for continuous monitoring
- **Full Update (60 min)**: Complete update includes all checks, runs hourly for comprehensive reporting

### Customization

Intervals can be customized based on:
- Endpoint criticality
- System load
- Network conditions
- Business requirements

---

## Installation & Setup

### Step 1: Generate Cron Configurations

```bash
python scripts/python/setup_apicli_bau_cron.py \
  --v3-interval 15 \
  --health-interval 5 \
  --full-interval 60
```

### Step 2: Review Generated Files

Generated files in `data/nas_cron/apicli_bau/`:
- `apicli_bau_v3.cron` - @v3 verification cron config
- `apicli_bau_health.cron` - Health checks cron config
- `apicli_bau_full.cron` - Full update cron config
- `deploy_apicli_bau_cron.sh` - Deployment script
- `apicli_bau_cron_config.json` - Configuration file

### Step 3: Deploy to NAS

```bash
# Copy deployment script to NAS
scp data/nas_cron/apicli_bau/deploy_apicli_bau_cron.sh user@nas:/path/to/

# SSH to NAS and run deployment
ssh user@nas 'bash /path/to/deploy_apicli_bau_cron.sh'
```

### Step 4: Verify Cron Entries

```bash
# On NAS, verify cron entries
crontab -l | grep apicli_endpoint_bau_daemon
```

Expected output:
```
*/15 * * * * cd /path/to/project && /usr/bin/python3 scripts/python/apicli_endpoint_bau_daemon.py --mode v3_only --cycle >> /dev/null 2>&1
*/5 * * * * cd /path/to/project && /usr/bin/python3 scripts/python/apicli_endpoint_bau_daemon.py --mode health_only --cycle >> /dev/null 2>&1
*/60 * * * * cd /path/to/project && /usr/bin/python3 scripts/python/apicli_endpoint_bau_daemon.py --mode full --cycle >> /dev/null 2>&1
```

---

## Usage

### Manual Execution

```bash
# Run one cycle of @v3 verification
python scripts/python/apicli_endpoint_bau_daemon.py --mode v3_only --cycle

# Run one cycle of health checks
python scripts/python/apicli_endpoint_bau_daemon.py --mode health_only --cycle

# Run one cycle of full update
python scripts/python/apicli_endpoint_bau_daemon.py --mode full --cycle
```

### Daemon Mode

```bash
# Run as daemon (for testing)
python scripts/python/apicli_endpoint_bau_daemon.py --mode full --interval 3600
```

---

## Logging

### Log Locations

Logs are written to separate directories based on check mode:

- **@v3 Verification**: `data/logs/apicli_bau_v3_only/`
- **Health Checks**: `data/logs/apicli_bau_health_only/`
- **Full Update**: `data/logs/apicli_bau_full/`

### Log Files

- Daily log files: `apicli_bau_{mode}_{YYYYMMDD}.log`
- Error log files: `apicli_bau_{mode}_errors_{YYYYMMDD}.log`
- Log rotation: 10MB max, 10 backups

### Log Format

```
2026-01-12 16:00:00 [INFO] [APICLIEndpointBAU-full] Starting @BAU endpoint check cycle (full)
2026-01-12 16:00:01 [INFO] [APICLIEndpointBAU-full] Running full @BAU endpoint update...
2026-01-12 16:00:15 [INFO] [APICLIEndpointBAU-full] ✅ @v3 verification complete: 6/6 verified
2026-01-12 16:00:30 [INFO] [APICLIEndpointBAU-full] ✅ Health checks complete: 6 endpoints checked
```

---

## Monitoring

### Check Daemon Status

```bash
# Check if cron jobs are running
ps aux | grep apicli_endpoint_bau_daemon

# Check recent log entries
tail -f data/logs/apicli_bau_full/apicli_bau_full_$(date +%Y%m%d).log
```

### Verify Results

```bash
# Check latest verification results
ls -lt data/apicli_endpoints/v3_verification_*.json | head -1

# Check latest health check results
ls -lt data/apicli_endpoints/health_welfare_*.json | head -1
```

---

## Configuration

### Interval Configuration

Edit `data/nas_cron/apicli_bau/apicli_bau_cron_config.json`:

```json
{
  "intervals": {
    "v3_verification": 15,
    "health_check": 5,
    "full_update": 60
  }
}
```

### Custom Intervals

```bash
# More frequent health checks
python scripts/python/setup_apicli_bau_cron.py \
  --v3-interval 30 \
  --health-interval 3 \
  --full-interval 120
```

---

## Integration Points

### @BAU Workflow Integration
- Part of Business As Usual workflows
- Automated endpoint maintenance
- Continuous health monitoring

### @V3 Integration
- Uses @v3 verification logic
- Pre-execution validation
- Quality assurance

### NAS Cron Integration
- Integrates with NAS cron scheduler
- Automated scheduling
- Log management

### Health Check Integration
- Integrates with health check systems
- Comprehensive monitoring
- Alerting capabilities

---

## Troubleshooting

### Cron Jobs Not Running

1. Check cron service: `systemctl status cron`
2. Check cron logs: `grep CRON /var/log/syslog`
3. Verify cron entries: `crontab -l`
4. Check file permissions: Ensure scripts are executable

### Daemon Errors

1. Check log files for errors
2. Verify Python path in cron config
3. Check project root path
4. Verify dependencies installed

### Missing Results

1. Check if daemon is running
2. Verify log files are being created
3. Check data directory permissions
4. Verify endpoint configurations

---

## Best Practices

### Interval Selection

- **High Criticality**: More frequent checks (3-5 min health, 10-15 min v3)
- **Medium Criticality**: Standard intervals (5 min health, 15 min v3)
- **Low Criticality**: Less frequent checks (10 min health, 30 min v3)

### Resource Management

- Monitor system load
- Adjust intervals based on performance
- Use appropriate check modes
- Balance frequency vs. resource usage

### Monitoring

- Review logs regularly
- Set up alerts for critical issues
- Track endpoint health trends
- Monitor daemon performance

---

## Status

✅ **ACTIVE** - Daemon system is operational

**Components**:
1. ✅ Daemon implementation
2. ✅ Cron scheduler setup
3. ✅ Multiple interval support
4. ✅ Logging system
5. ✅ Configuration management
6. ✅ Deployment scripts

**Next Steps**:
1. Deploy to NAS
2. Monitor initial runs
3. Adjust intervals as needed
4. Set up alerting

---

**Tags**: `#APICLI` `#BAU` `#V3` `#HEALTH_CHECK` `#DAEMON` `#NAS` `#CRON` `@JARVIS` `@LUMINA` `#PEAK`
