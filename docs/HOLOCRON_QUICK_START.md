# 🎯 Holocron Quick Start Guide

## Choose Your Database

### Option 1: MariaDB (Recommended for NAS) 🗄️

**Best for:**
- Large datasets (millions of records)
- Network access from multiple devices
- Better performance on NAS
- Concurrent queries

**Setup:**
```bash
pip install pymysql
python scripts/python/json_to_mariadb.py <file.json> \
  --host <NAS_IP> --user <user> --database <db>
```

See: [MARIADB_HOLOCRON_SETUP.md](MARIADB_HOLOCRON_SETUP.md)

### Option 2: SQLite (Local/Portable) 💾

**Best for:**
- Single-user access
- Portable databases
- No server setup needed
- Smaller datasets

**Setup:**
```bash
python scripts/python/json_to_holocron.py <file.json>
```

See: [HOLOCRON_SYSTEM.md](HOLOCRON_SYSTEM.md)

## Quick Conversion

### Single File

**MariaDB:**
```bash
python scripts/python/json_to_mariadb.py data/asks_timeline.json \
  --host 192.168.1.100 \
  --user lumina_user \
  --password your_password \
  --database lumina_holocrons
```

**SQLite:**
```bash
python scripts/python/json_to_holocron.py data/asks_timeline.json
```

### Batch Conversion

**MariaDB:**
```bash
python scripts/python/batch_convert_to_mariadb.py
```

**SQLite:**
```bash
python scripts/python/batch_convert_to_holocrons.py
```

## Query Examples

### MariaDB
```bash
mysql -h <NAS_IP> -u <user> -p <database>

SELECT COUNT(*) FROM asks_timeline;
SELECT category, COUNT(*) FROM asks_timeline GROUP BY category;
```

### SQLite
```bash
python scripts/python/query_holocron.py data/holocrons/asks_timeline.holocron.db \
  --query "SELECT COUNT(*) FROM asks_timeline"
```

## Which Should You Use?

| Scenario | Recommendation |
|----------|---------------|
| Have NAS with MariaDB | **MariaDB** - Better performance, network access |
| Large files (500MB+) | **MariaDB** - Handles millions of records better |
| Need portable DB | **SQLite** - Single file, easy to move |
| Single user | **SQLite** - Simpler setup |
| Multiple users | **MariaDB** - Concurrent access |

## Next Steps

1. **Choose your database** (MariaDB recommended for NAS)
2. **Convert one file** to test
3. **Query and verify** data integrity
4. **Batch convert** remaining files
5. **Delete original JSON** (after verification)

---

**For detailed guides:**
- MariaDB: [MARIADB_HOLOCRON_SETUP.md](MARIADB_HOLOCRON_SETUP.md)
- SQLite: [HOLOCRON_SYSTEM.md](HOLOCRON_SYSTEM.md)
- Queries: [HOLOCRON_QUERY_EXAMPLES.md](HOLOCRON_QUERY_EXAMPLES.md)
