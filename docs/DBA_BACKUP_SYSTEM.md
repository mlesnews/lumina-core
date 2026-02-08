# 🗄️ DBA/DBE Team - Holocron Backup System

## Overview

Comprehensive backup and restore system for MariaDB Holocrons on NAS.

## Features

✅ **Automated SQL dumps** - Full database backups
✅ **Table-level backups** - Backup individual tables
✅ **Compression** - Automatic gzip compression
✅ **Retention policies** - Automatic cleanup of old backups
✅ **Backup verification** - Verify backup integrity
✅ **Restore capabilities** - Full database restore
✅ **Metadata tracking** - Track all backups
✅ **Scheduling** - Integration with NAS cron/systemd

## Quick Start

### 1. Install Dependencies

```bash
pip install pymysql
```

### 2. Create Backup Configuration

```bash
python scripts/python/schedule_holocron_backups.py --create-config backup_config.json
```

Edit `backup_config.json` with your MariaDB details.

### 3. Manual Backup

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <username> \
  --password <password> \
  --database lumina_holocrons \
  --backup-dir /path/to/backups \
  --action backup
```

### 4. Setup Automated Backups

```bash
# Generate cron config
python scripts/python/schedule_holocron_backups.py \
  --config backup_config.json \
  --type cron \
  --output holocron_backup.cron

# Install on NAS
crontab -e
# Paste contents of holocron_backup.cron
```

## Backup Operations

### Full Database Backup

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action backup
```

**Output:**
- `{database}_backup_{timestamp}.sql.gz` - Compressed SQL dump
- Backup metadata stored in `backup_metadata.json`

### Table-Level Backup

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action backup-table \
  --table asks_timeline
```

### List Backups

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action list
```

### Verify Backup

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action verify \
  --backup-file /backups/holocrons/lumina_holocrons_backup_20260109_020000.sql.gz
```

### Restore Database

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action restore \
  --backup-file /backups/holocrons/lumina_holocrons_backup_20260109_020000.sql.gz
```

⚠️ **Warning**: Restore will overwrite existing database!

### Cleanup Old Backups

```bash
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> \
  --user <user> \
  --database <database> \
  --backup-dir /backups/holocrons \
  --action cleanup \
  --retention-days 30
```

Keeps minimum 5 most recent backups, removes older than retention period.

## Backup Schedule

### Daily Backups

Recommended schedule:
- **Daily**: 2:00 AM (low usage time)
- **Weekly cleanup**: Sunday 3:00 AM

### Cron Schedule

```cron
# Daily backup at 2 AM
0 2 * * * /usr/bin/python3 /path/to/backup_mariadb_holocrons.py --host <NAS_IP> --user <user> --database <database> --backup-dir /backups --action backup

# Weekly cleanup - Sunday at 3 AM
0 3 * * 0 /usr/bin/python3 /path/to/backup_mariadb_holocrons.py --host <NAS_IP> --user <user> --database <database> --backup-dir /backups --action cleanup --retention-days 30
```

### Systemd Timer (Linux NAS)

```bash
# Generate systemd files
python scripts/python/schedule_holocron_backups.py \
  --config backup_config.json \
  --type systemd \
  --output /tmp

# Install
sudo cp holocron-backup.service /etc/systemd/system/
sudo cp holocron-backup.timer /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable holocron-backup.timer
sudo systemctl start holocron-backup.timer
```

## Backup Storage

### Recommended Structure

```
/backups/holocrons/
├── backup_metadata.json          # Backup tracking
├── lumina_holocrons_backup_20260109_020000.sql.gz
├── lumina_holocrons_backup_20260110_020000.sql.gz
├── lumina_holocrons_backup_20260111_020000.sql.gz
└── ...
```

### Backup to Network Drive

You can store backups on your network drive:

```bash
# Backup to network drive
--backup-dir "\\NAS\share\backups\holocrons"

# Or mount network drive first
net use Z: \\NAS\share
--backup-dir "Z:\backups\holocrons"
```

### Backup Rotation

- **Daily backups**: Keep 7 days
- **Weekly backups**: Keep 4 weeks
- **Monthly backups**: Keep 12 months

Configure with `--retention-days` parameter.

## Backup Verification

### Automatic Verification

Backups are automatically verified during creation:
- ✅ File integrity check
- ✅ Compression validation
- ✅ SQL format validation

### Manual Verification

```bash
# Verify specific backup
python scripts/python/backup_mariadb_holocrons.py \
  --action verify \
  --backup-file /path/to/backup.sql.gz
```

## Restore Procedures

### Full Database Restore

1. **Verify backup**:
   ```bash
   --action verify --backup-file <backup_file>
   ```

2. **Restore**:
   ```bash
   --action restore --backup-file <backup_file>
   ```

3. **Verify restore**:
   ```bash
   mysql -h <NAS_IP> -u <user> -p <database>
   SELECT COUNT(*) FROM asks_timeline;
   ```

### Table-Level Restore

```bash
# Extract table from full backup
gunzip -c backup.sql.gz | grep -A 10000 "CREATE TABLE.*asks_timeline" > table_restore.sql

# Restore table
mysql -h <NAS_IP> -u <user> -p <database> < table_restore.sql
```

## Backup Monitoring

### Check Backup Status

```bash
# List recent backups
python scripts/python/backup_mariadb_holocrons.py \
  --action list
```

### Backup Metadata

Metadata stored in `backup_metadata.json`:
```json
{
  "backups": [
    {
      "timestamp": "20260109_020000",
      "datetime": "2026-01-09T02:00:00",
      "file": "lumina_holocrons_backup_20260109_020000.sql.gz",
      "size_mb": 1250.5,
      "compressed_size_mb": 312.3,
      "tables": 5,
      "table_counts": {
        "asks_timeline": 921113,
        "discovered_asks": 1
      }
    }
  ],
  "last_backup": {...}
}
```

## Integration with NAS Backup Systems

### Synology Hyper Backup

1. Add backup directory to Hyper Backup
2. Schedule NAS-level backups
3. Backup files synced to cloud/external drive

### QNAP Backup Station

1. Configure backup job for backup directory
2. Schedule automated backups
3. Multi-destination support

### Generic NAS Backup

```bash
# Add to NAS backup script
/path/to/backup_mariadb_holocrons.py --action backup
rsync -av /backups/holocrons/ /external/backup/holocrons/
```

## Best Practices

### 1. Backup Frequency
- **Production**: Daily backups
- **Development**: Weekly backups
- **Critical data**: Multiple daily backups

### 2. Retention Policy
- Keep daily backups for 7-30 days
- Keep weekly backups for 3-6 months
- Keep monthly backups for 1-2 years

### 3. Backup Verification
- Verify immediately after backup
- Test restore monthly
- Document restore procedures

### 4. Storage
- Store backups on separate drive/network location
- Use compression to save space
- Encrypt sensitive backups

### 5. Monitoring
- Monitor backup success/failure
- Alert on backup failures
- Track backup sizes (detect anomalies)

## Troubleshooting

### Backup Fails

**Check:**
- MariaDB connection
- Disk space
- Permissions on backup directory
- mysqldump availability

### Restore Fails

**Check:**
- Backup file integrity
- Database permissions
- Disk space
- Database not in use

### Large Backup Files

**Solutions:**
- Use compression (automatic)
- Backup individual tables
- Exclude large non-critical tables
- Use incremental backups (future feature)

## Security

### Password Management

```bash
# Use environment variable
export MARIADB_PASSWORD="your_password"
python scripts/python/backup_mariadb_holocrons.py --host ... --user ... --database ...

# Or use config file (restrict permissions)
chmod 600 backup_config.json
```

### Backup Encryption

```bash
# Encrypt backup after creation
gpg --encrypt --recipient your@email.com backup.sql.gz
```

### Access Control

- Restrict backup directory permissions
- Use dedicated backup user with limited privileges
- Store backups in secure location

---

**DBA/DBE Team - Keeping your Holocrons safe!** 🛡️🗄️
