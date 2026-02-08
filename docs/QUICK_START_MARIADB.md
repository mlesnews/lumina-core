# 🚀 Quick Start - MariaDB Holocron Conversion

## Prerequisites

**IMPORTANT:** Before starting, ensure you have a MariaDB user with remote access.

### Check Current Status

```bash
# Search for MariaDB credentials
python scripts/python/search_mariadb_secrets.py

# Test connection (auto-retrieves from Azure Vault)
python scripts/python/test_mariadb_connection.py --host 10.17.17.32 --database lumina_holocrons
```

### If Root Doesn't Have Remote Access

Root user typically doesn't have remote access (security best practice). Set up a dedicated user:

```bash
# Option 1: Automated setup (recommended)
python scripts/python/setup_mariadb_user.py

# Option 2: Manual setup via phpMyAdmin
# See: docs/MARIADB_USER_SETUP.md
```

## Fastest Way to Get Started

### Option 1: Interactive Guided Setup (Recommended)

```bash
python scripts/python/quick_start_mariadb.py
```

This will:
1. ✅ Automatically retrieve credentials from Azure Vault/ProtonPass
2. ✅ Prompt for any missing connection details
3. ✅ Test the connection
4. ✅ Find all large JSON files
5. ✅ Convert them to MariaDB tables
6. ✅ Show summary

### Option 2: Manual Step-by-Step

#### Step 1: Test Connection

```bash
python scripts/python/test_mariadb_connection.py \
  --host <NAS_IP> \
  --user <username> \
  --password <password> \
  --database lumina_holocrons
```

Or use config file:
```bash
# Create config first
python scripts/python/schedule_holocron_backups.py --create-config mariadb_config.json
# Edit mariadb_config.json with your details
python scripts/python/test_mariadb_connection.py --config mariadb_config.json
```

#### Step 2: Create Database (if needed)

```bash
mysql -h <NAS_IP> -u <username> -p
```

```sql
CREATE DATABASE lumina_holocrons CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lumina_holocrons;
```

#### Step 3: Convert Files

**Single file:**
```bash
python scripts/python/json_to_mariadb.py data/asks_timeline.json \
  --host <NAS_IP> \
  --user <username> \
  --password <password> \
  --database lumina_holocrons
```

**Batch convert:**
```bash
python scripts/python/batch_convert_to_mariadb.py
```

#### Step 4: Verify Conversion

```bash
mysql -h <NAS_IP> -u <username> -p lumina_holocrons

SHOW TABLES;
SELECT COUNT(*) FROM asks_timeline;
SELECT * FROM asks_timeline LIMIT 10;
```

#### Step 5: Setup Backups

```bash
# Create backup config
python scripts/python/schedule_holocron_backups.py --create-config backup_config.json

# Edit backup_config.json

# Generate cron schedule
python scripts/python/schedule_holocron_backups.py \
  --config backup_config.json --type cron

# Test backup
python scripts/python/backup_mariadb_holocrons.py \
  --host <NAS_IP> --user <username> --database lumina_holocrons \
  --backup-dir "\\NAS\share\backups\holocrons" \
  --action backup
```

## What You Need

1. **NAS MariaDB Details:**
   - Host/IP address
   - Port (usually 3306)
   - Username
   - Password
   - Database name

2. **Python Packages:**
   ```bash
   pip install pymysql
   ```

3. **MySQL Client Tools** (for backups):
   - `mysqldump` - For backups
   - `mysql` - For queries
   - Usually included with MariaDB installation

## Troubleshooting

### Connection Refused
- Check NAS firewall allows port 3306
- Verify MariaDB is running
- Check user has remote access

### Authentication Failed
- Verify username/password
- Check user permissions
- Try connecting from NAS directly first

### Database Doesn't Exist
```sql
CREATE DATABASE lumina_holocrons CHARACTER SET utf8mb4;
```

### Large File Timeout
- Convert files individually
- Increase MariaDB `max_allowed_packet`
- Monitor NAS resources

## Next Steps After Conversion

1. ✅ **Query your data** - Test SQL queries
2. ✅ **Setup backups** - Configure automated backups
3. ✅ **Monitor** - Check conversion success
4. ✅ **Cleanup** - Remove original JSON (after verification)

---

**Ready to start? Run: `python scripts/python/quick_start_mariadb.py`** 🚀
