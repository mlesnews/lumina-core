# 🎯 Holocron Query Examples

## Quick Reference

### Basic Queries

```bash
# List all tables
python scripts/python/query_holocron.py <holocron.db> --list-tables

# Get table structure
python scripts/python/query_holocron.py <holocron.db> --info <table_name>

# Simple SELECT
python scripts/python/query_holocron.py <holocron.db> --query "SELECT * FROM <table> LIMIT 10"

# Count records
python scripts/python/query_holocron.py <holocron.db> --query "SELECT COUNT(*) FROM <table>"
```

## asks_timeline.holocron.db

### Table Structure
- **921,113 records** with 12 columns
- Columns: id, imported_at, category, context, index, metadata_extracted_at, metadata_file, metadata_line, priority, source, text, timestamp

### Useful Queries

#### 1. Category Distribution
```sql
SELECT category, COUNT(*) as count
FROM asks_timeline
GROUP BY category
ORDER BY count DESC
LIMIT 20;
```

#### 2. Source Analysis
```sql
SELECT source, COUNT(*) as count
FROM asks_timeline
GROUP BY source
ORDER BY count DESC;
```

#### 3. Time Range Analysis
```sql
SELECT
    MIN(timestamp) as earliest,
    MAX(timestamp) as latest,
    COUNT(*) as total
FROM asks_timeline
WHERE timestamp IS NOT NULL;
```

#### 4. Search by Text
```bash
python scripts/python/query_holocron.py data/holocrons/asks_timeline.holocron.db \
  --search "interaction" --table asks_timeline --limit 10
```

#### 5. Filter by Category
```sql
SELECT text, context, timestamp
FROM asks_timeline
WHERE category = 'code_comment'
ORDER BY timestamp DESC
LIMIT 20;
```

#### 6. Priority Distribution
```sql
SELECT priority, COUNT(*) as count
FROM asks_timeline
GROUP BY priority;
```

#### 7. Recent Entries
```sql
SELECT text, category, timestamp
FROM asks_timeline
WHERE timestamp IS NOT NULL
ORDER BY timestamp DESC
LIMIT 50;
```

#### 8. Find Specific Patterns
```sql
SELECT text, context, category
FROM asks_timeline
WHERE text LIKE '%@ask%'
   OR context LIKE '%@ask%'
LIMIT 20;
```

## discovered_asks.holocron.db

### Table Structure
- **1 record** with 5 columns
- Columns: id, cached_at, asks, count, imported_at

### Useful Queries

#### 1. View All Data
```sql
SELECT * FROM discovered_asks;
```

#### 2. Extract JSON Data (if asks is stored as JSON)
```sql
SELECT
    cached_at,
    count,
    json_extract(asks, '$') as asks_data
FROM discovered_asks;
```

## LUMINA_ALL_ASKS_ORDERED.holocron.db

### Table Structure
- **1 record** (dictionary converted to single row)

### Useful Queries

#### 1. View Structure
```sql
SELECT * FROM LUMINA_ALL_ASKS_ORDERED LIMIT 1;
```

## Advanced Queries

### Date Range Filtering
```sql
SELECT *
FROM asks_timeline
WHERE timestamp >= '2026-01-01'
  AND timestamp < '2026-01-10'
ORDER BY timestamp;
```

### Aggregations
```sql
SELECT
    DATE(timestamp) as date,
    COUNT(*) as daily_count,
    COUNT(DISTINCT category) as unique_categories
FROM asks_timeline
WHERE timestamp IS NOT NULL
GROUP BY DATE(timestamp)
ORDER BY date DESC
LIMIT 30;
```

### Text Search with Context
```sql
SELECT
    text,
    context,
    category,
    timestamp
FROM asks_timeline
WHERE text LIKE '%error%'
   OR context LIKE '%error%'
ORDER BY timestamp DESC
LIMIT 20;
```

### Export to CSV
```bash
python scripts/python/query_holocron.py data/holocrons/asks_timeline.holocron.db \
  --query "SELECT * FROM asks_timeline WHERE category = 'code_comment' LIMIT 1000" \
  --format csv > exported_data.csv
```

### Export to JSON
```bash
python scripts/python/query_holocron.py data/holocrons/asks_timeline.holocron.db \
  --query "SELECT * FROM asks_timeline LIMIT 100" \
  --format json > exported_data.json
```

## Performance Tips

1. **Always use LIMIT** for large result sets
2. **Use WHERE clauses** to filter before processing
3. **Index on timestamp fields** - already created automatically
4. **Use COUNT(*) first** to check result size
5. **Export large results** to CSV/JSON instead of displaying

## Using SQLite Directly

You can also use any SQLite tool:

```bash
# Command line
sqlite3 data/holocrons/asks_timeline.holocron.db

# Then in SQLite prompt:
.tables
.schema asks_timeline
SELECT COUNT(*) FROM asks_timeline;
```

## Verification Queries

### Data Integrity Checks

```sql
-- Check for NULLs in critical fields
SELECT
    COUNT(*) as total,
    COUNT(timestamp) as has_timestamp,
    COUNT(text) as has_text,
    COUNT(category) as has_category
FROM asks_timeline;

-- Check for duplicates (if applicable)
SELECT text, COUNT(*) as count
FROM asks_timeline
GROUP BY text
HAVING count > 1
LIMIT 10;
```

---

**Remember**: Always test queries with LIMIT first, then remove it once you're confident!
