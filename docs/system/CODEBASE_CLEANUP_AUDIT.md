# Codebase Cleanup - Obsolete Code Archive

**Date**: 2025-12-28  
**Status**: ✅ **IMPLEMENTED**  
**Phase**: Phase 2 - Codebase Cleanup

---

## Overview

Automated system to audit and archive obsolete code (demos, tests, examples) as identified in MANUS gap analysis. Files are moved to archive directory instead of being deleted, preserving history.

---

## Implementation

**Deliverable**: `scripts/python/codebase_cleanup_archive_obsolete.py`

### Features

- **Audit System**: Identifies obsolete files by category:
  - Demo scripts (`*demo*.py`, `*_demo.py`)
  - Test scripts (`test_*.py`, `*_test.py`)
  - Example scripts (`example_*.py`, `*_example.py`)
  - Files with TODO/FIXME markers

- **Archive System**: 
  - Moves files to archive directory (doesn't delete)
  - Organized by category
  - Maintains manifest of archived files
  - Handles filename conflicts

- **Safety Features**:
  - Dry-run mode
  - Archive manifest tracking
  - Preserves file structure in archive

---

## Usage

### List Obsolete Files
```bash
python scripts/python/codebase_cleanup_archive_obsolete.py --list
```

### Dry Run (Preview)
```bash
python scripts/python/codebase_cleanup_archive_obsolete.py --archive --dry-run
```

### Archive Obsolete Files
```bash
python scripts/python/codebase_cleanup_archive_obsolete.py --archive
```

### View Archive Manifest
```bash
python scripts/python/codebase_cleanup_archive_obsolete.py --manifest
```

---

## Archive Structure

```
archive/
  obsolete_code/
    20251228/
      archive_manifest.json
      demo/
        demo_hr_team_routing.py
        demo_autonomous_execution.py
        ...
      test/
        test_babelfish_anime.py
        test_file_auto_close.py
        ...
      example/
        example_workflow_with_droids.py
        example_bitcoin_workflow.py
        ...
      todo_fixme/
        [files with TODO/FIXME markers]
        ...
```

---

## Identified Files (from analysis)

### Demo Scripts
- `demo_autonomous_execution.py`
- `demo_hr_team_routing.py`
- `syphon_jarvis_integration_demo.py`
- `manus_youtube_automation_demo.py`

### Example Scripts
- `example_workflow_with_droids.py`
- `example_bitcoin_workflow.py`

### Test Scripts
- `test_babelfish_anime.py`
- `find_and_test_anime.py`
- `test_file_auto_close.py`
- `test_jarvis_escalation.py`
- `test_droid_imports.py`
- `generate_bitcoin_test_data.py`

---

## Archive Manifest Format

```json
{
  "created_at": "2025-12-28T...",
  "total_entries": 10,
  "entries": [
    {
      "original_path": "scripts/python/demo_hr_team_routing.py",
      "archived_path": "archive/obsolete_code/20251228/demo/demo_hr_team_routing.py",
      "category": "demo",
      "reason": "Demo script - moved to archive",
      "archived_at": "2025-12-28T...",
      "metadata": {
        "file_size": 1234,
        "parent_dir": "scripts/python"
      }
    }
  ]
}
```

---

## Integration with MANUS

This cleanup system is part of MANUS Phase 2:
- Addresses bloat identified in gap analysis
- Reduces codebase clutter
- Preserves history (archive, not delete)
- Can be automated via unified control interface

---

**Status**: ✅ **READY FOR USE**  
**Next Step**: Run audit and archive obsolete files

