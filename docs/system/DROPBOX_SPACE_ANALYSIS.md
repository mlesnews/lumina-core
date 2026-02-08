# Dropbox Space Analysis Report

**Date**: 2025-12-28  
**Critical Issue**: Recursive Snapshot Bug Consuming 1.24 TB of Space

## Executive Summary

Dropbox is running out of space due to a **critical recursive snapshot bug** in the `time_travel` system. The `data/time_travel/snapshots` directory is consuming **1,245 GB (1.24 TB)**, which represents:

- **99%** of the `data` directory (1,262 GB)
- **90%** of `my_projects` directory (1,381 GB)
- **68%** of total Dropbox space (~2.7 TB)

## Space Breakdown

### Dropbox Root Level
| Directory | Size | Percentage |
|-----------|------|------------|
| **my_projects** | 1,381 GB | 51% |
| Shared | 909 GB | 34% |
| Dropbox_Flattened_20251222_000717 | 403 GB | 15% |
| Photos | 146 GB | 5% |
| Repository | 86 GB | 3% |

### my_projects Breakdown
| Directory | Size | Percentage |
|-----------|------|------------|
| **data** | 1,262 GB | 91% |
| cedarbrook-financial-services_llc-env | 45 GB | 3% |
| fvh | 12 GB | 1% |
| cfs-llc-env | 8 GB | 1% |
| .lumina | 2 GB | <1% |

### data Directory Breakdown
| Directory | Size | Percentage |
|-----------|------|------------|
| **time_travel** | **1,245 GB** | **99%** |
| cursor_chat_archive | 16 GB | 1% |
| moondev_extraction | 0.25 GB | <1% |
| holocron | 0.05 GB | <1% |
| Other directories | <0.1 GB each | <1% |

## Root Cause Analysis

### The Recursive Snapshot Bug

**Problem**: The snapshot creation process is including the `time_travel/snapshots` directory itself in snapshots, creating infinite recursive nesting.

**Evidence**: Log files show nested paths like:
```
data/time_travel/snapshots/snapshot_main_20251228_005758_292043/
  data/time_travel/snapshots/snapshot_main_20251228_005758_292043/
    data/time_travel/snapshots/snapshot_main_20251228_005758_292043/
      ... (infinite nesting)
```

**Impact**: This single bug is consuming over **1.2 TB** of Dropbox space.

## Recommendations

### Priority 1: CRITICAL - Fix Snapshot Creation

**Action**: Fix snapshot creation to exclude the `time_travel/snapshots` directory

**Location**: Need to identify the snapshot creation code (likely in a backup/snapshot script)

**Fix Required**:
- Add exclusion pattern for `time_travel/snapshots` directory in snapshot creation
- Ensure snapshot process ignores its own output directory

### Priority 2: HIGH - Clean Up Recursive Snapshots

**Action**: Delete all recursive snapshots

**Risk**: Only delete snapshots that contain nested snapshot directories (recursive ones)
- Keep the first-level snapshot if it contains valid data
- Verify which snapshots are recursive vs. legitimate

**Cleanup Script Needed**: Create a script that:
1. Identifies recursive snapshots (those containing `data/time_travel/snapshots` within them)
2. Calculates space that would be freed
3. Provides dry-run mode for verification
4. Safely deletes recursive snapshots

### Priority 3: MEDIUM - Implement Safeguards

**Action**: Implement snapshot size limits and retention policies

**Requirements**:
- Maximum snapshot size limits
- Snapshot age limits (auto-delete after X days)
- Snapshot count limits (keep only last N snapshots)
- Exclusion list for snapshot creation (prevent recursive inclusion)

### Priority 4: LOW - Audit Other Large Directories

**Action**: Review other large directories for cleanup opportunities

**Candidates**:
- `cursor_chat_archive` (16.4 GB) - Consider archiving or cleaning
- `Dropbox_Flattened_20251222_000717` (403 GB) - Verify if still needed
- `Shared` (909 GB) - Verify if all content is necessary

## Immediate Actions Required

1. **STOP**: Identify and disable any automated snapshot creation processes immediately
2. **ANALYZE**: Locate the snapshot creation code
3. **FIX**: Patch the code to exclude `time_travel/snapshots` directory
4. **CLEAN**: Delete recursive snapshots (this will free ~1.2 TB)
5. **VALIDATE**: Verify fix prevents future recursive snapshots
6. **MONITOR**: Add monitoring for snapshot directory size

## Estimated Space Recovery

If recursive snapshots are cleaned up:
- **Immediate**: ~1.2 TB freed (90% of my_projects space)
- **Data directory**: Reduced from 1,262 GB to ~17 GB
- **my_projects**: Reduced from 1,381 GB to ~136 GB
- **Dropbox total**: Reduced from ~2.7 TB to ~1.5 TB

## Related Files

- Analysis Report: `data/dropbox_space_analysis_report.json`
- Analysis Script: `scripts/python/dropbox_space_analysis_report.py`
- This Document: `docs/system/DROPBOX_SPACE_ANALYSIS.md`

## Status

- [x] Space analysis complete
- [x] Root cause identified
- [ ] Snapshot creation code located
- [ ] Snapshot creation fixed
- [ ] Recursive snapshots cleaned up
- [ ] Safeguards implemented
- [ ] Monitoring added

