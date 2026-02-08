# Prevention of Recursive Snapshot Creation

## Problem
Snapshots that include the snapshot directory itself create infinite recursion, consuming massive amounts of space (1.22 TB in our case).

## Solution: Exclusion Patterns

### PowerShell Scripts
When using `Copy-Item` or `robocopy`, always exclude the snapshot directory:

```powershell
# Using Copy-Item
$excludeDirs = @("time_travel\snapshots")
Copy-Item -Path $source -Destination $dest -Recurse -Force -Exclude $excludeDirs

# Using robocopy
robocopy $source $dest /MIR /XD "time_travel\snapshots"
```

### Python Scripts
When using `shutil.copytree`, use ignore parameter:

```python
import shutil

def ignore_snapshots(dirname, filenames):
    if 'snapshots' in dirname and 'time_travel' in dirname:
        return filenames
    return []

shutil.copytree(src, dst, ignore=ignore_snapshots)
```

### Always Verify
Before creating any backup/snapshot:
1. Check if snapshot directory exists in source
2. Verify exclusion patterns are in place
3. Test on small dataset first
4. Monitor output directory size

## Files to Update
- Any script that copies `data` directory
- Any script that creates backups
- Any script that creates snapshots
- Scheduled tasks that perform backups

## Git-Based Snapshots
Use Git/GitLens for snapshots instead of file system copies:
- Commits are snapshots
- Tags are milestones
- No file system space overhead
- No recursion risk

See: `scripts/python/git_time_travel.py`
