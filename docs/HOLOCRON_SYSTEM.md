# 🎯 HOLOCRON SYSTEM - Queryable Knowledge Repositories

## What are Holocrons?

Holocrons are **SQLite databases** created from your large JSON files. Instead of deleting monster files, convert them to Holocrons for efficient querying and data preservation.

### Benefits

✅ **Preserve all data** - Nothing is lost
✅ **Fast SQL queries** - Much faster than parsing JSON
✅ **Indexed searches** - Automatic indexes on timestamp fields
✅ **Smaller size** - SQLite is more efficient than raw JSON
✅ **Standard SQL** - Use any SQLite tool to query

## Quick Start

### 1. Convert a JSON File to Holocron

```bash
python scripts/python/json_to_holocron.py data/syphon_lumina_hourly/execution_20260105_064706.json
```

This creates: `data/holocrons/execution_20260105_064706.holocron.db`

### 2. Query Your Holocron

```bash
# List all tables
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --list-tables

# Get table structure
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --info <table_name>

# Run SQL query
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db \
  --query "SELECT * FROM <table> WHERE <condition> LIMIT 10"

# Search across text columns
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db \
  --search "search_term" --table <table_name>
```

### 3. Batch Convert All Monster Files

```bash
python scripts/python/batch_convert_to_holocrons.py
```

## Conversion Process

The converter automatically:

1. **Analyzes JSON structure** - Detects if it's a list, dict, or nested structure
2. **Creates optimal schema** - Infers column types from data
3. **Flattens nested data** - Converts nested objects to flat columns
4. **Preserves arrays** - Stores arrays as JSON strings (can be queried with JSON functions)
5. **Adds metadata** - Tracks source file, conversion date, record count
6. **Creates indexes** - Automatically indexes timestamp/date fields

## Query Examples

### Basic Queries

```sql
-- Get all records
SELECT * FROM table_name LIMIT 100;

-- Count records
SELECT COUNT(*) FROM table_name;

-- Filter by date
SELECT * FROM table_name
WHERE timestamp > '2026-01-01'
ORDER BY timestamp DESC;

-- Search in JSON columns
SELECT * FROM table_name
WHERE json_extract(nested_data, '$.key') = 'value';
```

### Using the Query Tool

```bash
# Table format (default)
python scripts/python/query_holocron.py <holocron.db> --query "SELECT * FROM table LIMIT 10"

# JSON format
python scripts/python/query_holocron.py <holocron.db> --query "SELECT * FROM table" --format json

# CSV format (for export)
python scripts/python/query_holocron.py <holocron.db> --query "SELECT * FROM table" --format csv > output.csv
```

## Integration with Monster File Slayer

Convert monster files to Holocrons during cleanup:

```bash
# Dry run - see what would be converted
python scripts/python/slay_monster_files.py --to-holocron

# Actually convert
python scripts/python/slay_monster_files.py --execute --to-holocron
```

## Using Other SQLite Tools

Since Holocrons are standard SQLite databases, you can use any SQLite tool:

### Command Line (sqlite3)

```bash
sqlite3 data/holocrons/execution_20260105_064706.holocron.db

# Then in SQLite prompt:
.tables                    # List tables
.schema table_name         # Show table structure
SELECT * FROM table_name LIMIT 10;
```

### GUI Tools

- **DB Browser for SQLite** - https://sqlitebrowser.org/
- **DBeaver** - https://dbeaver.io/
- **VS Code SQLite Extension** - Search "SQLite" in VS Code extensions

### Python

```python
import sqlite3

conn = sqlite3.connect('data/holocrons/execution_20260105_064706.holocron.db')
cursor = conn.cursor()

# Query
cursor.execute("SELECT * FROM table_name LIMIT 10")
results = cursor.fetchall()

# Get column names
cursor.execute("PRAGMA table_info(table_name)")
columns = [row[1] for row in cursor.fetchall()]

conn.close()
```

## Holocron Metadata

Each Holocron includes a `holocron_metadata` table:

```sql
SELECT * FROM holocron_metadata;
```

Contains:
- `holocron_name` - Name of the holocron
- `source_file` - Original JSON file path
- `converted_at` - Conversion timestamp
- `record_count` - Number of records
- `file_size_mb` - Original file size

## Best Practices

1. **Keep originals initially** - Don't delete JSON files until you verify Holocrons work
2. **Test queries** - Run a few queries to ensure data integrity
3. **Backup Holocrons** - SQLite files are easy to backup
4. **Use indexes** - The converter creates indexes automatically, but you can add more
5. **Archive old Holocrons** - Move old Holocrons to archive storage

## Troubleshooting

### "Table doesn't exist"
- List tables first: `--list-tables`
- Check table name spelling (case-sensitive)

### "No results found"
- Try without WHERE clause first
- Check data types match (use CAST if needed)

### Large result sets
- Always use LIMIT in queries
- Use `--limit` flag to control output size

### Import errors
- Check JSON file is valid: `python -m json.tool file.json`
- Large files may take time - be patient
- Check disk space availability

## File Locations

- **Holocrons**: `data/holocrons/*.holocron.db`
- **Conversion scripts**: `scripts/python/json_to_holocron.py`
- **Query tool**: `scripts/python/query_holocron.py`
- **Batch converter**: `scripts/python/batch_convert_to_holocrons.py`

---

**"The knowledge of the ages, preserved and queryable!"** 🎯
