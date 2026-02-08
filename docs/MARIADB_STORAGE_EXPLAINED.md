# 🗄️ MariaDB Storage on NAS - How It Works

## Quick Answer

**MariaDB databases are stored on your NAS filesystem**, but they're **NOT directly accessible as network drive files**. They're managed by the MariaDB server process.

## How MariaDB Storage Works

### Where Databases Live

MariaDB databases are stored in MariaDB's **data directory** on your NAS, typically:
- **Synology**: `/volume1/@database/mariadb/` or `/var/lib/mysql/`
- **QNAP**: `/share/CACHEDEV1_DATA/.qpkg/MariaDB/var/lib/mysql/`
- **Generic Linux**: `/var/lib/mysql/`

### Important Distinctions

| What | Location | Access Method |
|------|----------|---------------|
| **Database files** | NAS filesystem (MariaDB data dir) | Via MariaDB server (port 3306) |
| **Network drive files** | NAS shared folders | Direct file access (SMB/NFS) |
| **Your JSON files** | Network drive (e.g., `\\NAS\share\data\`) | Direct file access |

### You CANNOT:

❌ Browse database files in Windows Explorer
❌ Copy database files directly from network drive
❌ Access `.frm`, `.ibd` files directly
❌ See database as files on your mapped network drive

### You CAN:

✅ Connect via MariaDB client (port 3306)
✅ Query data using SQL
✅ Use GUI tools (phpMyAdmin, DBeaver)
✅ Access from any device on network
✅ Backup/restore via SQL dumps

## Access Methods

### Method 1: MariaDB Client (Recommended)

```bash
# Connect to MariaDB server on NAS
mysql -h <NAS_IP> -u <user> -p <database>

# Your data is on the NAS, accessed through the server
SELECT * FROM asks_timeline;
```

### Method 2: Python Scripts

```python
# Connect to MariaDB server
import pymysql
conn = pymysql.connect(
    host='<NAS_IP>',  # NAS IP address
    user='<user>',
    password='<password>',
    database='lumina_holocrons'
)
# Data is on NAS, accessed via network connection
```

### Method 3: GUI Tools

- **phpMyAdmin** (if on NAS) - `http://NAS_IP/phpMyAdmin`
- **DBeaver** - Connect to `NAS_IP:3306`
- **MySQL Workbench** - Connect to `NAS_IP:3306`

## File Locations Comparison

### Your Current Setup (Network Drive)

```
\\NAS\share\data\
  ├── asks_timeline.json          ← Direct file access
  ├── discovered_asks.json        ← Direct file access
  └── syphon_lumina_hourly\       ← Direct file access
```

### After MariaDB Conversion (NAS Filesystem)

```
NAS Filesystem (MariaDB data directory):
  /var/lib/mysql/lumina_holocrons/
    ├── asks_timeline.frm          ← Managed by MariaDB
    ├── asks_timeline.ibd          ← Managed by MariaDB
    └── ...
```

**You access via:**
```
mysql -h NAS_IP -u user -p lumina_holocrons
```

## Why This Is Better

### Network Drive Files (Current)
- ❌ Large files cause performance issues
- ❌ No indexing
- ❌ Slow queries
- ❌ Limited concurrent access

### MariaDB on NAS (After Conversion)
- ✅ Optimized storage format
- ✅ Automatic indexing
- ✅ Fast SQL queries
- ✅ Concurrent access
- ✅ Network accessible (via MariaDB protocol)

## Workflow

### 1. Your JSON Files (Network Drive)
```
Location: \\NAS\share\my_projects\.lumina\data\
Access: Direct file access (Windows Explorer)
```

### 2. Conversion Process
```bash
# Script reads from network drive
python json_to_mariadb.py \\NAS\share\...\data\asks_timeline.json \
  --host NAS_IP --database lumina_holocrons

# Data gets stored in MariaDB on NAS
```

### 3. Querying (MariaDB Server)
```bash
# Connect to MariaDB server on NAS
mysql -h NAS_IP -u user -p lumina_holocrons

# Query data (stored on NAS, accessed via server)
SELECT * FROM asks_timeline;
```

## Backup Strategy

### Option 1: SQL Dump (Recommended)
```bash
# Export from MariaDB
mysqldump -h NAS_IP -u user -p lumina_holocrons > backup.sql

# This creates a file you CAN store on network drive
# Copy backup.sql to \\NAS\share\backups\
```

### Option 2: MariaDB Native Backup
```bash
# MariaDB backup tools (if available on NAS)
# Backs up to NAS filesystem
```

## Summary

| Aspect | Network Drive Files | MariaDB on NAS |
|--------|---------------------|----------------|
| **Storage** | Network share folder | NAS filesystem (MariaDB dir) |
| **Access** | Direct file access | Via MariaDB server (port 3306) |
| **Visibility** | See in Explorer | Hidden (managed by MariaDB) |
| **Performance** | Slow for large files | Optimized, indexed |
| **Query** | Parse JSON manually | Fast SQL queries |
| **Backup** | Copy files | SQL dumps |

## Bottom Line

✅ **Databases ARE on your NAS** - stored in MariaDB's data directory
✅ **You access them via MariaDB server** - not as direct files
✅ **Much better performance** - optimized for queries
✅ **Network accessible** - from any device via MariaDB protocol

Think of it like this:
- **Network drive files** = Books on a shelf (you can see and touch them)
- **MariaDB databases** = Books in a library system (you access via the librarian/server)

Both are on the NAS, but accessed differently! 🗄️
