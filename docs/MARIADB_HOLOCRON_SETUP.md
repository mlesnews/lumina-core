# 🗄️ MariaDB Holocron Setup Guide

## Why MariaDB Instead of SQLite?

MariaDB is **much better** for your NAS setup:

✅ **Handles millions of records** efficiently
✅ **Concurrent access** - multiple users/queries
✅ **Better indexing** and query optimization
✅ **JSON support** - native JSON columns
✅ **Network accessible** - query from anywhere
✅ **Better for large datasets** - your 900MB+ files

## Prerequisites

```bash
# Install Python MariaDB connector
pip install pymysql
```

## NAS MariaDB Connection

### 1. Get Your NAS MariaDB Details

You'll need:
- **Host**: Your NAS IP address or hostname
- **Port**: Usually 3306 (default)
- **Username**: Your MariaDB user
- **Password**: Your MariaDB password
- **Database**: Database name (create one if needed)

### 2. Create Database (if needed)

Connect to your NAS MariaDB:

```bash
mysql -h <NAS_IP> -u <username> -p
```

Then create database:

```sql
CREATE DATABASE lumina_holocrons CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lumina_holocrons;
```

## Converting JSON to MariaDB

### Single File Conversion

```bash
python scripts/python/json_to_mariadb.py data/asks_timeline.json \
  --host <NAS_IP> \
  --user <username> \
  --password <password> \
  --database lumina_holocrons \
  --table asks_timeline
```

### Using Environment Variable (Safer)

```bash
# Set password as environment variable
export MARIADB_PASSWORD="your_password"

# Then convert without --password flag
python scripts/python/json_to_mariadb.py data/asks_timeline.json \
  --host <NAS_IP> \
  --user <username> \
  --database lumina_holocrons
```

### Batch Conversion Script

Create a batch script:

```bash
#!/bin/bash
# convert_all_to_mariadb.sh

HOST="your_nas_ip"
USER="your_username"
DB="lumina_holocrons"

FILES=(
  "data/asks_timeline.json"
  "data/discovered_asks.json"
  "data/syphon_lumina_hourly/execution_20260105_064706.json"
)

for file in "${FILES[@]}"; do
  echo "Converting $file..."
  python scripts/python/json_to_mariadb.py "$file" \
    --host "$HOST" \
    --user "$USER" \
    --database "$DB"
done
```

## Querying MariaDB Holocrons

### Using MySQL/MariaDB Client

```bash
mysql -h <NAS_IP> -u <username> -p lumina_holocrons
```

```sql
-- List all tables
SHOW TABLES;

-- Get table structure
DESCRIBE asks_timeline;

-- Query data
SELECT COUNT(*) FROM asks_timeline;
SELECT * FROM asks_timeline LIMIT 10;

-- Category distribution
SELECT category, COUNT(*) as count
FROM asks_timeline
GROUP BY category
ORDER BY count DESC;
```

### Using Python

```python
import pymysql

conn = pymysql.connect(
    host='<NAS_IP>',
    user='<username>',
    password='<password>',
    database='lumina_holocrons',
    charset='utf8mb4'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM asks_timeline LIMIT 10")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
```

### Using GUI Tools

- **phpMyAdmin** (if installed on NAS)
- **DBeaver** - https://dbeaver.io/
- **MySQL Workbench** - https://www.mysql.com/products/workbench/
- **TablePlus** - https://tableplus.com/

## Performance Tips

1. **Use indexes** - Automatically created on timestamp fields
2. **Batch inserts** - Converter uses 1000-record batches
3. **JSON columns** - Complex nested data stored as JSON
4. **InnoDB engine** - Better for large datasets
5. **UTF8MB4 charset** - Full Unicode support

## Advantages Over SQLite

| Feature | SQLite | MariaDB |
|--------|--------|---------|
| Max file size | ~140TB | Unlimited |
| Concurrent writes | Limited | Full support |
| Network access | No | Yes |
| JSON support | Basic | Native |
| Indexing | Good | Excellent |
| Large datasets | Slower | Much faster |

## Migration from SQLite

If you already have SQLite Holocrons:

```bash
# Export from SQLite
sqlite3 data/holocrons/asks_timeline.holocron.db .dump > dump.sql

# Convert to MariaDB format and import
# (You may need to adjust the SQL syntax)
mysql -h <NAS_IP> -u <username> -p lumina_holocrons < dump.sql
```

Or just reconvert from original JSON files - it's faster!

## Security Notes

1. **Use strong passwords** for MariaDB users
2. **Limit network access** - Only allow connections from trusted IPs
3. **Use SSL** if accessing over internet
4. **Create dedicated user** with limited permissions:

```sql
CREATE USER 'lumina_holocron'@'%' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE ON lumina_holocrons.* TO 'lumina_holocron'@'%';
FLUSH PRIVILEGES;
```

## Troubleshooting

### Connection Refused
- Check NAS firewall allows port 3306
- Verify MariaDB is running on NAS
- Check user has remote access permissions

### Authentication Failed
- Verify username/password
- Check user has access from your IP
- Try connecting from NAS directly first

### Large File Timeout
- Increase `max_allowed_packet` in MariaDB config
- Use batch conversion for very large files
- Monitor NAS resources during conversion

---

**Your NAS MariaDB is the perfect home for your Holocrons!** 🗄️✨
