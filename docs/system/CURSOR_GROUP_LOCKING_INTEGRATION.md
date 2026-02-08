# Cursor IDE Group Locking Integration

## Overview

The pinned file management system integrates with Cursor IDE's existing **group locking** concept. Permanently pinned files are marked with a lock symbol (🔒) and use the same locking logic patterns as Cursor IDE's group-locked files.

## Lock Symbol Concept

### Visual Indicator
- **🔒 Lock Symbol**: All permanently pinned files display a lock symbol
- **Status Display**: Files show as "🔒 LOCKED" in listings and warnings
- **Integration**: Builds on Cursor IDE's existing group locking functionality

### Benefits
1. **Reuses Existing Logic**: Leverages Cursor IDE's group locking patterns
2. **Visual Clarity**: Lock symbol makes locked status immediately obvious
3. **Consistent UX**: Matches Cursor IDE's existing locking behavior
4. **Prevents Accidents**: Locked files cannot be unpinned without explicit confirmation

## How It Works

### Locked Files
When a file is added to the allowlist, it is automatically:
1. **Permanently Pinned**: Added to the allowlist
2. **Locked**: Marked with `locked: true` and lock symbol 🔒
3. **Protected**: Cannot be unpinned without removing from allowlist first

### Integration Points

#### 1. Allowlist = Locked Files
```python
# Adding to allowlist automatically locks the file
manager.add_to_allowlist("file.py", reason="Important system file")
# Result: file.py is now 🔒 LOCKED and permanently pinned
```

#### 2. Group Locking Concept
The system reuses Cursor IDE's group locking logic:
- Files are "group-locked" (locked as a group of permanently pinned files)
- Lock status prevents accidental unpinning
- Unlocking requires explicit confirmation

#### 3. Visual Indicators
- Lock symbol (🔒) appears in:
  - File listings
  - Warning messages
  - Status displays
  - Cleanup summaries

## Usage

### List Locked Files
```bash
python scripts/python/cursor_pinned_file_manager.py --locked
```

Output:
```
🔒 Locked Files (Permanently Pinned with Lock Symbol):
============================================================
   These files are locked and integrate with Cursor IDE's group locking concept
============================================================

   🔒 C:\Users\...\voice_transcript_queue.py
      Status: 🔒 LOCKED (permanently pinned)
      📝 Reason: Core voice processing system
      👤 Added by: system
      📅 Added at: 2026-01-17T19:15:05.205594
```

### Check Lock Status
```bash
python scripts/python/cursor_pinned_file_manager.py --check "file.py"
```

### Lock a File
```bash
python scripts/python/cursor_pinned_file_manager.py --lock "file.py"
```

Note: File must be in allowlist first. Use `--add` to add and lock simultaneously.

## Warning System

When attempting to unpin a locked file, the system shows:

```
⚠️  WARNING: Removing 🔒 LOCKED file from allowlist
============================================================
   🔒 File: path/to/file.py
   📝 Reason: Core system file
   👤 Added by: system
   📅 Added at: 2026-01-17T19:15:05.205594
============================================================
   This file was 🔒 LOCKED and permanently pinned.
   Removing it will unlock and allow automatic unpinning.
   This integrates with Cursor IDE's group locking concept.
============================================================
```

## Technical Implementation

### Data Structure
```python
@dataclass
class PinnedFileConfig:
    file_path: str
    permanently_pinned: bool = False
    locked: bool = True  # Locked by default
    lock_symbol: str = "🔒"  # Visual indicator
    reason: Optional[str] = None
    added_by: Optional[str] = None
    added_at: Optional[str] = None
```

### Lock Status
- **locked: true**: File is locked and cannot be unpinned
- **locked: false**: File is in allowlist but unlocked (rare)
- **lock_symbol: "🔒"**: Visual indicator for locked status

## Future Integration

When Cursor IDE API becomes available, the system can:
1. **Direct Integration**: Call Cursor IDE's group locking API
2. **Synchronization**: Keep lock status in sync with Cursor IDE
3. **Visual Updates**: Update Cursor IDE UI to show lock symbols
4. **Unified Management**: Manage locks through Cursor IDE's native interface

## Benefits of Reusing Group Locking Logic

1. **Consistency**: Matches existing Cursor IDE behavior
2. **Familiarity**: Users already understand group locking
3. **Reliability**: Uses proven locking patterns
4. **Maintainability**: Aligns with Cursor IDE's architecture

## Example Workflow

```bash
# 1. Add file to allowlist (automatically locks it)
python scripts/python/cursor_pinned_file_manager.py \
  --add "scripts/python/voice_transcript_queue.py" \
  --reason "Core voice processing system"

# 2. Verify it's locked
python scripts/python/cursor_pinned_file_manager.py \
  --check "scripts/python/voice_transcript_queue.py"
# Output: ✅ File is permanently pinned: ...
#         Status: 🔒 LOCKED

# 3. List all locked files
python scripts/python/cursor_pinned_file_manager.py --locked

# 4. Attempt to remove (shows warning with lock symbol)
python scripts/python/cursor_pinned_file_manager.py \
  --remove "scripts/python/voice_transcript_queue.py"
# Output: ⚠️  WARNING: Removing 🔒 LOCKED file from allowlist
```

## Related Documentation

- [Pinned Files Cleanup Summary](./CURSOR_PINNED_FILES_CLEANUP_SUMMARY.md)
- [Person Resources Team Structure](./PERSON_RESOURCES_TEAM_STRUCTURE.md)

---

**Note**: This system builds on Cursor IDE's group locking concept to provide a consistent, familiar experience for managing permanently pinned files.
