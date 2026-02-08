# 🧹 LUMINA Spring Cleaning Plan

**Date**: 2026-01-08
**Status**: URGENT - Resource limits reached
**Reason**: 21,841+ files causing memory/timeout issues

## 🚨 Why Spring Cleaning is Critical

### Current Issues
- **21,841+ tracked files** - Too many for efficient operations
- **Memory exhaustion** - Stack/heap crashes during enumeration
- **Operation timeouts** - Git operations failing
- **Process freezes** - Directory traversal locking up
- **Incomplete statistics** - Can't get accurate counts

### Impact
- ❌ Can't get accurate file counts
- ❌ Tracking systems timing out
- ❌ Memory errors preventing operations
- ❌ Development workflow slowed
- ❌ Resource waste on unnecessary files

---

## 🎯 Spring Cleaning Goals

### Primary Objectives
1. **Reduce file count** - Target: <10,000 tracked files
2. **Remove obsolete data** - Clean up old/unused files
3. **Organize structure** - Better file organization
4. **Archive old data** - Move to archive instead of delete
5. **Improve performance** - Faster operations after cleanup

### Success Metrics
- ✅ File count reduced by 50%+
- ✅ No more memory errors
- ✅ Operations complete without timeouts
- ✅ Accurate statistics available
- ✅ Faster development workflow

---

## 📋 Cleanup Categories

### 1. Data Directory Cleanup

**Location**: `data/`

**Candidates for Cleanup**:
- Old session files (keep last 30 days)
- Duplicate analytics reports (keep latest)
- Old extension data (clean up unused extensions)
- Temporary files
- Old backups (archive instead of delete)

**Estimated Impact**: ~5,000-10,000 files

### 2. Extension Data Cleanup

**Location**: `data/extensions/`

**Candidates**:
- Unused extension data
- Old extension versions
- Cached extension files
- Extension backups

**Estimated Impact**: ~2,000-5,000 files

### 3. Config Backup Cleanup

**Location**: `config/`

**Candidates**:
- Old backup files (one_ring_blueprint_backup_*.json)
- Duplicate configs
- Old encrypted backups

**Estimated Impact**: ~100-500 files

### 4. Log File Cleanup

**Location**: `.lumina/logs/`

**Candidates**:
- Old log files
- Rotated logs
- Debug logs

**Estimated Impact**: ~500-1,000 files

### 5. Temporary Files

**Location**: Various

**Candidates**:
- `.tmp` files
- `.cache` files
- `.swp` files
- `.bak` files

**Estimated Impact**: ~1,000-2,000 files

---

## 🛠️ Cleanup Tools

### 1. Analysis Script
**Purpose**: Identify cleanup candidates without deleting

**Script**: `scripts/python/spring_cleaning_analyzer.py`

**Features**:
- Scans repository for cleanup candidates
- Estimates space savings
- Categorizes files by type
- Safe analysis (no deletions)

### 2. Cleanup Script
**Purpose**: Execute cleanup with safety checks

**Script**: `scripts/python/spring_cleaning_executor.py`

**Features**:
- Dry-run mode (preview only)
- Safety checks before deletion
- Archive option (move instead of delete)
- Logging of all operations

### 3. Archive Script
**Purpose**: Archive instead of delete

**Script**: `scripts/python/spring_cleaning_archiver.py`

**Features**:
- Move files to archive directory
- Compress archives
- Maintain structure
- Easy restoration

---

## 📊 Cleanup Strategy

### Phase 1: Analysis (Week 1)
1. ✅ Run analysis script
2. ✅ Review cleanup candidates
3. ✅ Identify high-impact areas
4. ✅ Plan cleanup order

### Phase 2: Safe Cleanup (Week 2)
1. ✅ Archive old backups
2. ✅ Remove temporary files
3. ✅ Clean up old logs
4. ✅ Remove duplicate configs

### Phase 3: Data Cleanup (Week 3)
1. ✅ Archive old session files
2. ✅ Clean extension data
3. ✅ Organize data directories
4. ✅ Remove obsolete analytics

### Phase 4: Verification (Week 4)
1. ✅ Verify file count reduction
2. ✅ Test tracking systems
3. ✅ Confirm no regressions
4. ✅ Document results

---

## 🎯 Priority Areas

### High Priority (Immediate Impact)
1. **Config backups** - Many duplicate backup files
2. **Old session files** - Large number of session files
3. **Extension data** - Unused extension files
4. **Temporary files** - Easy wins

### Medium Priority (Good Impact)
1. **Old analytics** - Keep only recent reports
2. **Log files** - Rotate and archive
3. **Cache files** - Can be regenerated

### Low Priority (Nice to Have)
1. **Documentation duplicates** - Consolidate
2. **Test data** - Archive old tests
3. **Example files** - Organize examples

---

## ⚠️ Safety Guidelines

### Never Delete
- ✅ Active configuration files
- ✅ Current session data
- ✅ Recent analytics
- ✅ Source code files
- ✅ Documentation

### Always Archive First
- ✅ Old backups
- ✅ Historical data
- ✅ Old session files
- ✅ Extension data

### Test Before Delete
- ✅ Run in dry-run mode first
- ✅ Verify backups exist
- ✅ Test after cleanup
- ✅ Keep logs of operations

---

## 📈 Expected Results

### Before Cleanup
- **Files**: 21,841+
- **Memory Errors**: Frequent
- **Timeouts**: Common
- **Statistics**: Incomplete

### After Cleanup (Target)
- **Files**: <10,000
- **Memory Errors**: None
- **Timeouts**: Rare
- **Statistics**: Complete

### Performance Improvements
- ✅ 50%+ faster operations
- ✅ Accurate file counts
- ✅ No memory issues
- ✅ Complete statistics
- ✅ Better development experience

---

## 🚀 Getting Started

### Step 1: Run Analysis
```bash
python scripts/python/spring_cleaning_analyzer.py
```

### Step 2: Review Report
- Check cleanup candidates
- Review estimated savings
- Identify priorities

### Step 3: Start with Safe Items
```bash
# Dry run first (default - preview only)
python scripts/python/spring_cleaning_executor.py

# Execute with archiving (safe - moves to archive)
python scripts/python/spring_cleaning_executor.py --execute --archive

# Execute with deletion (dangerous - permanent!)
python scripts/python/spring_cleaning_executor.py --execute --delete
```

### Step 4: Verify
```bash
# Check file count
git ls-files | wc -l

# Test tracking systems
python scripts/python/time_tracking_comparison.py last_7_days
```

---

## 📝 Cleanup Log

Track cleanup progress:

- [ ] Phase 1: Analysis complete
- [ ] Phase 2: Safe cleanup complete
- [ ] Phase 3: Data cleanup complete
- [ ] Phase 4: Verification complete

**Current Status**: Analysis complete - 2,593 files identified for cleanup

### Analysis Results (2026-01-08)
- **Config Backups**: 2,268 files (68 MB) - Archive all but latest 3
- **Extension Data**: 429 files (77 MB) - Review and remove unused
- **Temporary Files**: 114 files (0.77 MB) - Safe to delete
- **Total Identified**: 2,593 files
- **Estimated Savings**: 87 MB

**Note**: This is just the first pass. More cleanup needed to reach <10,000 files target.

---

## 🔗 Related Documentation

- [Tracking Limitations](TRACKING_LIMITATIONS.md) - Why cleanup is needed
- [All Tracking Systems](ALL_TRACKING_SYSTEMS.md) - Current state
- [Time Tracking Comparison](TIME_TRACKING_COMPARISON.md) - Performance impact

---

**URGENT**: Spring cleaning is critical for maintaining development efficiency and accurate tracking.

---

**Last Updated**: 2026-01-08
**Priority**: HIGH
**Status**: Planning
