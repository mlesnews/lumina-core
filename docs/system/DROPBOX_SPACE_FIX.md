# Dropbox Space Fix - Recursive Snapshot Cleanup

**Date**: 2025-12-28  
**Status**: Cleanup script ready, awaiting confirmation to delete

## Problem Summary

The `data/time_travel/snapshots` directory contains a recursive snapshot consuming **1.22 TB** of Dropbox space. The snapshot includes nested snapshot directories, creating infinite recursion (12 levels deep).

## Root Cause

File system snapshots were being created by copying the entire `my_projects` directory, but the snapshot output directory (`data/time_travel/snapshots`) was not excluded, causing it to include itself recursively.

## Solution: Use Git/GitLens for Snapshots

**Paradigm Shift**: Instead of creating file system snapshots, use Git/GitLens for version control and snapshots. Git already provides:
- Commit history (snapshots)
- Tags for milestones
- Branch-based state preservation
- Time travel capabilities

**Action Required**: 
1. Clean up the recursive file system snapshot
2. Stop creating file system snapshots
3. Use Git commits and tags for snapshot functionality

## Cleanup Script

Created: `scripts/python/cleanup_recursive_snapshots.py`

### Usage

**Dry Run (default)** - See what would be deleted:
```bash
python scripts/python/cleanup_recursive_snapshots.py \
    --snapshots-dir "c:\Users\mlesn\Dropbox\my_projects\data\time_travel\snapshots" \
    --report data/cleanup_recursive_snapshots_report.json
```

**Actual Deletion** - Remove recursive snapshots:
```bash
python scripts/python/cleanup_recursive_snapshots.py \
    --snapshots-dir "c:\Users\mlesn\Dropbox\my_projects\data\time_travel\snapshots" \
    --confirm \
    --report data/cleanup_recursive_snapshots_report.json
```

### Current Status

- **Found**: 1 recursive snapshot
- **Size**: 1.22 TB
- **Nesting Depth**: 12 levels
- **Snapshot Name**: `snapshot_main_20251228_005758_292043`

### Expected Results

Deleting the recursive snapshot will free **~1.22 TB** of Dropbox space, reducing:
- `data` directory from 1,262 GB to ~17 GB
- `my_projects` from 1,381 GB to ~161 GB
- Dropbox total from ~2.7 TB to ~1.5 TB

## Prevention

### Stop File System Snapshots

If any scripts are creating file system snapshots in `data/time_travel/snapshots`, they should be:
1. **Disabled** - Stop running automatically
2. **Updated** - Add exclusion for `data/time_travel/snapshots` directory
3. **Replaced** - Use Git/GitLens instead

### Backup Script Exclusions

Any backup scripts that copy `my_projects` or `data` directory should exclude:
- `data/time_travel/snapshots/**` (all snapshots)

Example PowerShell exclusion:
```powershell
$excludeDirs = @(
    "time_travel\snapshots"
)
# Use robocopy with /XD parameter or Copy-Item with exclusion
```

Example Python exclusion:
```python
exclude_patterns = ['time_travel/snapshots']
# Use shutil.copytree with ignore parameter
```

### Use Git for Snapshots

For snapshot functionality, use Git:
- **Commits**: Create commits for state preservation
- **Tags**: Create milestone tags (e.g., `v1.0.0`)
- **Branches**: Create branches for experimental states
- **Git Time Travel**: Use `git_time_travel.py` for navigation

See: `scripts/python/git_time_travel.py`

## Files Created

1. **Cleanup Script**: `scripts/python/cleanup_recursive_snapshots.py`
2. **Analysis Report**: `data/dropbox_space_analysis_report.json`
3. **Cleanup Report**: `data/cleanup_recursive_snapshots_report.json`
4. **Documentation**: 
   - `docs/system/DROPBOX_SPACE_ANALYSIS.md`
   - `docs/system/DROPBOX_SPACE_FIX.md` (this file)

## Next Steps

1. ✅ Analysis complete
2. ✅ Cleanup script created
3. ⏳ **Awaiting confirmation** to delete recursive snapshot
4. ⏳ Update backup scripts to exclude snapshot directory
5. ⏳ Disable/update any file system snapshot creation scripts
6. ⏳ Document Git/GitLens as the snapshot system

## Risk Assessment

**Low Risk**: The recursive snapshot is clearly identified and contains only redundant nested data. Deleting it will free space without losing any unique content (since it's a recursive copy of existing data).

**Recommendation**: Proceed with deletion using `--confirm` flag.

