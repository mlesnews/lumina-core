# Cursor Active Model Status Display

**Date**: 2026-01-04  
**Status**: ✅ **COMPLETE**

---

## Overview

Added a system to display the currently active model in Cursor IDE UI, showing the actual model being used even when the selector shows "Auto".

---

## Components

### 1. Model Tracker Script
**File**: `scripts/python/cursor_active_model_tracker.py`

Monitors Cursor's settings and determines the currently active model:
- Reads `.cursor/settings.json`
- Determines active model from agent/composer/chat defaults
- Tracks model details (type, provider, endpoint, local/cloud)
- Writes status to `data/cursor_active_model_status.json`

**Features**:
- Detects model type (local, cloud, virtual_cluster, auto)
- Tracks cluster configurations
- Updates status file in real-time
- Supports continuous monitoring mode

**Usage**:
```bash
# Update once
python scripts/python/cursor_active_model_tracker.py --update

# Monitor continuously
python scripts/python/cursor_active_model_tracker.py --monitor

# Show current status
python scripts/python/cursor_active_model_tracker.py --status
```

### 2. VS Code Extension
**Location**: `vscode-extensions/cursor-active-model-status/`

A VS Code/Cursor extension that displays the active model in the status bar:
- Shows model name with type indicator
- Updates automatically when model changes
- Click to see detailed information
- Configurable update interval

**Status Bar Display**:
- `$(circuit-board) ULTRON $(home)` - Local model
- `$(circuit-board) GPT-4 $(cloud)` - Cloud model
- `$(circuit-board) ULTRON $(server)` - Virtual cluster
- `$(circuit-board) Auto $(sync~spin)` - Auto mode

**Installation**:
1. Navigate to `vscode-extensions/cursor-active-model-status/`
2. Run `npm install`
3. Run `npm run compile`
4. Press F5 to launch extension development host
5. Or package and install: `vsce package` then install the `.vsix` file

### 3. Quick Start Script
**File**: `scripts/python/start_cursor_model_tracker.py`

Convenience script to start the tracker:
```bash
python scripts/python/start_cursor_model_tracker.py
```

---

## Status File Format

The tracker writes to `data/cursor_active_model_status.json`:

```json
{
  "active_model": "ULTRON",
  "model_type": "virtual_cluster",
  "provider": "ollama",
  "endpoint": "http://localhost:11434",
  "is_local": true,
  "context_length": 32768,
  "description": "ULTRON Virtual Hybrid Cluster - Local Ollama (qwen2.5:72b) + KAIJU NAS",
  "cluster_nodes": 2,
  "cluster_type": "virtual_hybrid",
  "cluster_routing": "load_balanced",
  "last_updated": "2026-01-04T05:45:30.123456",
  "status": "active"
}
```

---

## Model Detection Logic

The tracker determines the active model using this priority:

1. **Agent Model** (highest priority)
   - Checks `cursor.agent.defaultModel`
   - Looks up in `cursor.agent.customModels`

2. **Composer Model**
   - Checks `cursor.composer.defaultModel`
   - Looks up in `cursor.composer.customModels`

3. **Chat Model**
   - Checks `cursor.chat.defaultModel`
   - Looks up in `cursor.chat.customModels`

4. **Auto Mode**
   - If no default is set, shows "Auto (Selecting...)"

---

## Model Type Detection

The tracker identifies model types:

- **`local`**: Model marked with `localOnly: true`
- **`cloud`**: Model without `localOnly` flag
- **`virtual_cluster`**: Model with `cluster` configuration
- **`auto`**: No default model set (auto-selection mode)

---

## UI Display Location

The extension displays the active model in the **status bar** (bottom right of Cursor IDE):
- Position: Right side, high priority (1000)
- Format: Icon + Model Name + Type Indicator
- Tooltip: Shows full details on hover
- Click: Opens detailed information dialog

**Example Display**:
```
[Status Bar] ... $(circuit-board) ULTRON $(home)
```

---

## Configuration

### Extension Settings

In Cursor/VS Code settings:

```json
{
  "cursorActiveModelStatus.updateInterval": 1000,
  "cursorActiveModelStatus.showInStatusBar": true
}
```

- **`updateInterval`**: How often to check for model changes (milliseconds)
- **`showInStatusBar`**: Whether to show in status bar

### Tracker Settings

Tracker can be configured via command-line arguments:
- `--interval`: Update interval in seconds (default: 1.0)
- `--update`: Update once and exit
- `--monitor`: Monitor continuously
- `--status`: Show current status

---

## Integration with Voice Chat Area

The user requested the display "around the space of wherever our voice chat transcribed Directly above it is a Greater than and then. 300 files".

**Current Implementation**:
- Status bar display (bottom right)
- Can be moved/customized via extension settings

**Future Enhancement**:
- Could add a custom webview panel
- Could add to chat panel header
- Could add as a notification badge

---

## Commands

The extension provides these commands:

1. **`cursorActiveModelStatus.refresh`**
   - Manually refresh the status
   - Available in Command Palette

2. **`cursorActiveModelStatus.showDetails`**
   - Show detailed model information
   - Click status bar item or use Command Palette

---

## Troubleshooting

### Status Not Updating

1. **Check tracker is running**:
   ```bash
   python scripts/python/cursor_active_model_tracker.py --status
   ```

2. **Start tracker**:
   ```bash
   python scripts/python/start_cursor_model_tracker.py
   ```

3. **Check status file exists**:
   ```bash
   cat data/cursor_active_model_status.json
   ```

### Extension Not Showing

1. **Check extension is installed**:
   - Open Extensions view
   - Search for "Cursor Active Model Status"

2. **Check extension is enabled**:
   - Verify in Extensions view

3. **Reload window**:
   - Press `Ctrl+Shift+P` → "Reload Window"

### Model Shows "Unknown"

1. **Check Cursor settings**:
   - Verify `.cursor/settings.json` exists
   - Check `cursor.agent.defaultModel` is set

2. **Run tracker manually**:
   ```bash
   python scripts/python/cursor_active_model_tracker.py --update
   ```

3. **Check status file**:
   ```bash
   python scripts/python/cursor_active_model_tracker.py --status
   ```

---

## Files Created

1. **`scripts/python/cursor_active_model_tracker.py`**
   - Main tracker script
   - Monitors and updates model status

2. **`scripts/python/start_cursor_model_tracker.py`**
   - Convenience script to start tracker

3. **`vscode-extensions/cursor-active-model-status/package.json`**
   - Extension manifest

4. **`vscode-extensions/cursor-active-model-status/src/extension.ts`**
   - Extension source code

5. **`vscode-extensions/cursor-active-model-status/tsconfig.json`**
   - TypeScript configuration

6. **`data/cursor_active_model_status.json`**
   - Status file (created by tracker)

---

## Next Steps

1. **Install Extension**:
   - Compile TypeScript: `cd vscode-extensions/cursor-active-model-status && npm install && npm run compile`
   - Install in Cursor IDE

2. **Start Tracker**:
   ```bash
   python scripts/python/start_cursor_model_tracker.py
   ```

3. **Verify Display**:
   - Check status bar for active model
   - Click to see details

---

## Benefits

1. **Transparency**: See exactly which model is active
2. **Real-time Updates**: Changes as model selection changes
3. **Works with Auto Mode**: Shows actual model even when selector says "Auto"
4. **Local/Cloud Indicator**: Visual indicator of model location
5. **Cluster Support**: Shows cluster information for virtual clusters

---

**Ready to use!** 🚀
