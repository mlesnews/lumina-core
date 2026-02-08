# 🔥 MONSTER FILE SLAYER - RAID BOSS CLEANUP GUIDE

**"BY FIRE BE PURGED!"** - Ragnaros, probably

## Overview

This system identifies and cleans up large files that cause performance issues in Cursor/VS Code, including:
- Files larger than 100MB (monster files)
- Deeply nested backup directories
- Old backup files (>30 days)
- Duplicate files in backup structures

**NEW: Holocron Conversion!** 🎯
Instead of just deleting monster files, convert them to **Holocrons** - queryable SQLite databases that preserve your data while making it searchable and efficient!

## Quick Start

### Python Script (Cross-platform)

```bash
# Generate a report (safe, no changes)
python scripts/python/slay_monster_files.py --report-only

# Dry run (see what would be cleaned)
python scripts/python/slay_monster_files.py

# Actually execute cleanup
python scripts/python/slay_monster_files.py --execute

# Convert monster files to Holocrons (queryable databases) instead of deleting
python scripts/python/slay_monster_files.py --execute --to-holocron

# Batch convert all large JSON files to Holocrons
python scripts/python/batch_convert_to_holocrons.py

# Save report to file
python scripts/python/slay_monster_files.py --report-only --output monster_report.json
```

### PowerShell Script (Windows)

```powershell
# Generate a report (safe, no changes)
.\scripts\powershell\Slay-MonsterFiles.ps1 -ReportOnly

# Dry run (see what would be cleaned)
.\scripts\powershell\Slay-MonsterFiles.ps1

# Actually execute cleanup
.\scripts\powershell\Slay-MonsterFiles.ps1 -Execute
```

## What Gets Cleaned

### 1. Nested Backup Directories
- Removes backup directories nested deeper than 2 levels
- Example: `data/local_backup/data/local_backup/data/...` (too deep)

### 2. Old Backup Files
- Deletes backup files older than 30 days
- Patterns: `*backup*.json`, `execution_*.json`, `*_syphon_*.json`

### 3. Large File Options

#### Option A: Convert to Holocrons (Recommended) 🎯
- Converts JSON files larger than 50MB to SQLite databases
- **Preserves all data** in queryable format
- Much faster to query than JSON
- Use `--to-holocron` flag

#### Option B: Compression
- Compresses JSON files larger than 50MB to `.json.gz`
- Reduces file size by 60-80% typically
- Original files are removed after compression

### 4. Git Ignore Updates
- Large data files are now in `.gitignore`
- Prevents version control issues

## Holocron System 🎯

### What are Holocrons?

Holocrons are SQLite databases created from your large JSON files. They:
- **Preserve all data** from the original JSON
- **Enable SQL queries** for fast searching
- **Reduce file size** while maintaining accessibility
- **Support indexing** for even faster queries

### Converting Files to Holocrons

```bash
# Convert a single file
python scripts/python/json_to_holocron.py data/syphon_lumina_hourly/execution_20260105_064706.json

# Batch convert all large files
python scripts/python/batch_convert_to_holocrons.py

# Convert during monster slaying
python scripts/python/slay_monster_files.py --execute --to-holocron
```

### Querying Holocrons

```bash
# List all tables in a holocron
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --list-tables

# Get table information
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --info <table_name>

# Execute SQL query
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --query "SELECT * FROM <table> LIMIT 10"

# Search across text columns
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --search "search_term" --table <table_name>

# Export as JSON
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --query "SELECT * FROM <table>" --format json

# Export as CSV
python scripts/python/query_holocron.py data/holocrons/execution_20260105_064706.holocron.db --query "SELECT * FROM <table>" --format csv
```

### Holocron Location

All Holocrons are stored in: `data/holocrons/`

Each Holocron includes:
- All data from the original JSON file
- Metadata table with conversion info
- Automatic indexes on timestamp fields
- Queryable via standard SQL

## Current Monster Files Status

**Last Scan Results:**
- **59 monster files** found (>100MB)
- **1,389 nested backup directories** identified
- **~25.59 GB** of nested backup data
- Largest file: **1.18 GB** (execution_20260105_064706.json)

## Configuration

Edit the scripts to customize:

```python
# Python script
LARGE_FILE_THRESHOLD_MB = 100  # Files larger than this are "monsters"
COMPRESSION_THRESHOLD_MB = 50  # Files larger than this get compressed
BACKUP_RETENTION_DAYS = 30     # Keep backups for this many days
MAX_NESTED_BACKUP_DEPTH = 2    # Maximum allowed nesting depth
```

```powershell
# PowerShell script parameters
-RetentionDays 30
-LargeFileThresholdMB 100
-MaxNestedDepth 2
```

## Safety Features

1. **Dry Run by Default**: Scripts show what would be done without making changes
2. **Backup Verification**: Only removes files that match backup patterns
3. **Date-Based Cleanup**: Only removes files older than retention period
4. **Compression Before Deletion**: Large files are compressed, not deleted

## Prevention

To prevent future monster files:

1. **Monitor File Sizes**: Run the report script regularly
2. **Fix Backup Logic**: Ensure backup scripts don't create nested backups
3. **Archive Old Data**: Move old data to archive storage
4. **Use Compression**: Enable compression for large JSON files

## Recovery

If you need to recover compressed files:

```bash
# Decompress a .json.gz file
gunzip file.json.gz
# or
python -c "import gzip, shutil; shutil.copyfileobj(gzip.open('file.json.gz'), open('file.json', 'wb'))"
```

## Integration

Add to cron/scheduled tasks:

```bash
# Weekly cleanup (dry run)
0 2 * * 0 python /path/to/slay_monster_files.py --report-only --output /path/to/reports/weekly_$(date +\%Y\%m\%d).json

# Monthly cleanup (execute)
0 3 1 * * python /path/to/slay_monster_files.py --execute
```

## Support

If you encounter issues:
1. Always run with `--report-only` first
2. Check the report output
3. Verify file paths before executing
4. Keep backups of important data before cleanup

---

**Remember**: "The monsters must be purged, but wisdom guides the flame!" 🔥
