# Chat History Queue - Quick Reference

## All Operations

### Pin/Unpin
```bash
# Pin an item (keeps at top)
python scripts/python/unified_queue_adapter.py --pin <item_id>

# Unpin an item
python scripts/python/unified_queue_adapter.py --unpin <item_id>
```

### Read/Unread
```bash
# Mark as read
python scripts/python/unified_queue_adapter.py --mark-read <item_id>

# Mark as unread
python scripts/python/unified_queue_adapter.py --mark-unread <item_id>
```

### Rename
```bash
# Rename an item
python scripts/python/unified_queue_adapter.py --rename <item_id> "New Title"
```

### Duplicate
```bash
# Create a copy of an item
python scripts/python/unified_queue_adapter.py --duplicate <item_id>
```

### Delete
```bash
# Delete a duplicate (safe, default)
python scripts/python/unified_queue_adapter.py --delete <item_id>

# Force delete any item (use with caution)
python scripts/python/unified_queue_adapter.py --delete <item_id> --force
```

## Viewing

### List All Items
```bash
# List all items
python scripts/python/unified_queue_adapter.py --list

# List only pinned items
python scripts/python/unified_queue_adapter.py --list --filter-pinned

# List only unread items
python scripts/python/unified_queue_adapter.py --list --filter-unread

# List only duplicates
python scripts/python/unified_queue_adapter.py --list --filter-duplicates
```

### Real-time Viewer
```bash
# View all chat history items
python scripts/python/unified_queue_viewer.py --filter-type chat_history

# View with filters
python scripts/python/unified_queue_viewer.py --filter-type chat_history --filter-status pending
```

## Common Workflows

### 1. Safe Evolution (Duplicate → Evolve → Delete)
```bash
# Step 1: Duplicate
python scripts/python/unified_queue_adapter.py --duplicate chat_history_abc123
# Returns: chat_history_abc123_copy_1234567890

# Step 2: Work on the duplicate, evolve it
# [Your work here]

# Step 3: Rename the evolved version
python scripts/python/unified_queue_adapter.py --rename chat_history_abc123_copy_1234567890 "Evolved Version"

# Step 4: Pin the good one
python scripts/python/unified_queue_adapter.py --pin chat_history_abc123_copy_1234567890

# Step 5: Delete the old original (safe, it's not a duplicate)
python scripts/python/unified_queue_adapter.py --delete chat_history_abc123 --force
```

### 2. Organization
```bash
# Mark as reviewed
python scripts/python/unified_queue_adapter.py --mark-read chat_history_abc123

# Give it a meaningful name
python scripts/python/unified_queue_adapter.py --rename chat_history_abc123 "API Integration Discussion"

# Pin important ones
python scripts/python/unified_queue_adapter.py --pin chat_history_abc123
```

### 3. Cleanup Duplicates
```bash
# List all duplicates
python scripts/python/unified_queue_adapter.py --list --filter-duplicates

# Review and delete unwanted duplicates
python scripts/python/unified_queue_adapter.py --delete <duplicate_item_id>
```

## Visual Indicators

In the viewer, items show:
- **📌** = Pinned (appears first)
- **✓** = Read
- **🔴** = Unread
- **📋** = Duplicate

## Safety Features

- **Delete Protection**: By default, only duplicates can be deleted
- **Pin Protection**: Pinned items cannot be deleted (unless `--force`)
- **Force Override**: Use `--force` flag to bypass safety checks (use with caution)

## Metadata Stored

Each item tracks:
- `pinned`: Boolean
- `read`: Boolean
- `read_at`: Timestamp
- `is_duplicate`: Boolean
- `duplicated_from`: Original item ID
- `original_title`: First title before rename
- `deleted_at`: Timestamp when deleted
