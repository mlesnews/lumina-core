# Chat History Queue Operations

## Function Mapping & Workflow

This document maps out all operations available for managing chat history sessions in the unified queue system.

---

## Core Operations

### 1. **Pin / Unpin** 📌
**Purpose**: Keep important chat sessions at the top of the queue

- **`pin(item_id)`**: Mark a chat history session as pinned
  - Sets `metadata.pinned = True`
  - Pinned items appear first in sorted views
  - Visual indicator: 📌 icon
  
- **`unpin(item_id)`**: Remove pin from a chat history session
  - Sets `metadata.pinned = False` or removes flag
  - Item returns to normal sorting

**Use Case**: Pin important conversations you want to reference frequently

---

### 2. **Read / Unread** 👁️
**Purpose**: Track which chat sessions have been reviewed

- **`mark_read(item_id)`**: Mark a chat history session as read
  - Sets `metadata.read = True`
  - Sets `metadata.read_at = timestamp`
  - Visual indicator: ✓ or muted appearance
  
- **`mark_unread(item_id)`**: Mark a chat history session as unread
  - Sets `metadata.read = False`
  - Removes `read_at` timestamp
  - Visual indicator: 🔴 or bold appearance

**Use Case**: Track which conversations you've reviewed vs. new ones

---

### 3. **Rename** ✏️
**Purpose**: Give chat sessions custom, meaningful names

- **`rename(item_id, new_title)`**: Change the title of a chat history session
  - Updates `title` field
  - Preserves original title in `metadata.original_title` (first rename only)
  - Updates `updated_at` timestamp
  - Returns success/failure

**Use Case**: Organize sessions with descriptive names like "API Integration Discussion" instead of auto-generated IDs

---

### 4. **Duplicate** 📋
**Purpose**: Create a copy of a chat session for experimentation

- **`duplicate(item_id, new_title=None)`**: Create a copy of a chat history session
  - Creates new item with:
    - New `item_id` (with `_copy` suffix)
    - Same `chat_session_id` (or new one if specified)
    - Copy of all metadata
    - `metadata.duplicated_from = original_item_id`
    - `metadata.is_duplicate = True`
    - `status = PENDING` (fresh start)
    - `read = False` (new item, unread)
    - `pinned = False` (duplicate not pinned by default)
  - Returns new `item_id`

**Use Case**: 
- Experiment with variations of a conversation
- Create backup before major changes
- Branch a conversation into different directions

---

### 5. **Delete** 🗑️
**Purpose**: Remove chat sessions (with safety checks)

- **`delete(item_id, force=False)`**: Delete a chat history session
  - **Safety Checks**:
    - If `force=False`: Only deletes if `metadata.is_duplicate = True`
    - If `force=True`: Deletes any item (use with caution)
    - Prevents deletion of pinned items unless `force=True`
  - Moves to `CANCELLED` status first (soft delete)
  - After confirmation period, removes from queue
  - Logs deletion with timestamp

**Use Case**: 
- Clean up duplicate copies after evolving them
- Remove old backup sessions
- **Workflow**: `duplicate()` → evolve duplicate → `delete()` original

---

## Workflow Patterns

### Pattern 1: Safe Evolution Workflow
```
1. duplicate(item_id) → new_item_id
2. [Work on new_item_id, evolve it]
3. rename(new_item_id, "Evolved Version")
4. pin(new_item_id)  # Keep the good one
5. delete(item_id)  # Remove old backup (safe, it's not a duplicate)
```

### Pattern 2: Organization Workflow
```
1. mark_read(item_id)  # Mark as reviewed
2. rename(item_id, "Descriptive Name")
3. pin(item_id)  # Keep important ones at top
```

### Pattern 3: Cleanup Workflow
```
1. Filter: get_all_items(item_type=CHAT_HISTORY, filter_duplicates=True)
2. Review duplicates
3. For each duplicate:
   - If evolved version is better: delete(original_id)
   - If original is better: delete(duplicate_id)
```

---

## Filtering & Sorting

### Filter Options
- **By Pinned**: `filter_pinned=True/False`
- **By Read Status**: `filter_read=True/False/None` (None = all)
- **By Duplicate Status**: `filter_duplicates=True/False`
- **By Agent**: `filter_agent="agent_name"`

### Sort Options
- **Default**: Pinned first, then priority, then created_at
- **By Read Status**: Unread first, then read
- **By Updated**: Most recently updated first
- **By Title**: Alphabetical

---

## Metadata Structure

Each chat history item stores flags in `metadata`:

```json
{
  "pinned": false,
  "read": false,
  "read_at": "2026-01-10T12:00:00",
  "is_duplicate": false,
  "duplicated_from": null,
  "original_title": "Chat History: Auto Session (abc12345...)",
  "tags": [],
  "notes": ""
}
```

---

## Implementation Status

- [x] Pin/Unpin
- [x] Read/Unread
- [x] Rename
- [x] Duplicate
- [x] Delete (with safety)
- [x] Filtering by flags
- [x] Sorting with pinned priority
- [x] CLI commands for all operations

---

## CLI Usage Examples

```bash
# Pin a chat session
python unified_queue_adapter.py --pin chat_history_session_123

# Mark as read
python unified_queue_adapter.py --mark-read chat_history_session_123

# Rename
python unified_queue_adapter.py --rename chat_history_session_123 "API Discussion"

# Duplicate
python unified_queue_adapter.py --duplicate chat_history_session_123

# Delete (only duplicates by default)
python unified_queue_adapter.py --delete chat_history_session_123_copy

# Force delete (any item)
python unified_queue_adapter.py --delete chat_history_session_123 --force

# List pinned items
python unified_queue_viewer.py --filter-type chat_history --filter-pinned

# List unread items
python unified_queue_viewer.py --filter-type chat_history --filter-unread
```
