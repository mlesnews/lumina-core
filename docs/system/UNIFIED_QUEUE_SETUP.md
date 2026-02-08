# Unified Queue System - Setup Guide

Quick setup guide to get the unified queue system working with the IDE footer extension.

## ✅ Setup Complete!

The system is now ready to use. Here's what's been set up:

### 1. VSCode Extension Compiled ✅
- Extension location: `vscode-extensions/lumina-unified-queue/`
- Compiled TypeScript: `out/extension.js`
- Ready to load in VSCode/Cursor

### 2. Queue State File ✅
- Location: `data/unified_queue/queue_state.json`
- Auto-saves every 5 seconds
- Contains all queue items (sources, problems, tasks)

### 3. Unified Queue Adapter ✅
- Auto-saves queue state
- Syncs with orchestrator
- Ready to use

## Quick Start

### Step 1: Start the Queue Daemon (Optional but Recommended)

```bash
# Keep adapter running in background
python scripts/python/unified_queue_daemon.py
```

This ensures:
- Queue state is always up-to-date
- Auto-save runs every 5 seconds
- IDE extension can read current state

### Step 2: Load the Extension in VSCode/Cursor

1. Open VSCode/Cursor
2. Press `F5` to open Extension Development Host
3. Or install the extension:
   ```bash
   cd vscode-extensions/lumina-unified-queue
   vsce package
   # Install the generated .vsix file
   ```

### Step 3: Add Items to Queue

```python
from scripts.python.unified_queue_adapter import UnifiedQueueAdapter

adapter = UnifiedQueueAdapter()

# Add source (same as problems)
adapter.add_source("https://www.youtube.com/@EWTN", "web", priority="high")

# Add problem
adapter.add_problem("Linter Error", "Unused import", priority="normal")

# Add task
adapter.add_task("Review PR", "Code review needed", priority="low")
```

### Step 4: View in IDE Footer

The footer will show:
```
📋 ⚙️ 3 ⏳1
```

Meaning:
- 3 total items
- Currently processing (spinner)
- 1 pending

Click the status bar item to see details!

## Testing

### Test the Extension

1. Add test items:
   ```bash
   python -c "from scripts.python.unified_queue_adapter import UnifiedQueueAdapter; a = UnifiedQueueAdapter(); a.add_source('https://ewtn.com', 'web'); a.add_problem('Test', 'Test problem')"
   ```

2. Check queue state:
   ```bash
   type data\unified_queue\queue_state.json
   ```

3. Load extension in VSCode - footer should update!

### View Queue

```bash
# Real-time viewer
python scripts/python/unified_queue_viewer.py

# Summary
python scripts/python/unified_queue_adapter.py --summary
```

## Extension Features

### Status Bar Display
- Shows total items
- Processing indicator (spinner)
- Pending count
- Failed count
- Updates every 2 seconds

### Click Actions
- **Click status bar**: Show queue details
- **Command**: `lumina.unifiedQueue.showDetails`
- **Command**: `lumina.unifiedQueue.openViewer`
- **Command**: `lumina.unifiedQueue.refresh`

## Configuration

Add to `.vscode/settings.json`:

```json
{
  "lumina.unifiedQueue.showInStatusBar": true,
  "lumina.unifiedQueue.updateInterval": 2000,
  "lumina.unifiedQueue.showDetails": true
}
```

## Troubleshooting

### Extension Not Showing
1. Check queue state file exists: `data/unified_queue/queue_state.json`
2. Verify extension is loaded (check Output panel)
3. Reload window: `Ctrl+Shift+P` → "Reload Window"

### Queue State Not Updating
1. Ensure daemon is running: `python scripts/python/unified_queue_daemon.py`
2. Check auto-save is active (should see logs every 5s)
3. Manually save: `adapter.save_queue_state()`

### No Items Showing
1. Add items to queue (see Quick Start Step 3)
2. Wait 5 seconds for auto-save
3. Check `queue_state.json` has items

## Files Created

- ✅ `vscode-extensions/lumina-unified-queue/` - Extension source
- ✅ `vscode-extensions/lumina-unified-queue/out/extension.js` - Compiled extension
- ✅ `data/unified_queue/queue_state.json` - Queue state file
- ✅ `scripts/python/unified_queue_daemon.py` - Daemon script

## Next Steps

1. **Start daemon** (keeps queue updated)
2. **Load extension** in VSCode/Cursor
3. **Add items** to queue
4. **View in footer** - see real-time updates!

## Tags

@SETUP @QUEUE @UNIFIED @EXTENSION @FOOTER
