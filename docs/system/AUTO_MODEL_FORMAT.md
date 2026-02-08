# AUTO\MODEL Format Display

## 🎯 Format: `AUTO\MODEL_NAME`

When Cursor is in **Auto mode**, the active model is displayed as:

```
AUTO\ULTRON
AUTO\GROK
AUTO\CLAUDE
```

This format clearly shows:
- **AUTO** = Auto mode is active (Cursor selects models dynamically)
- **MODEL_NAME** = The detected/selected model being used

---

## 📊 Examples

### Explicit Model (Not Auto)
```
Active Model: ULTRON
Model Type: virtual_cluster
```

### Auto Mode with Detected Model
```
Active Model: AUTO\ULTRON
Model Type: auto
```

### Auto Mode (Selecting)
```
Active Model: AUTO\SELECTING...
Model Type: auto
```

---

## 🔍 How It Works

1. **Detection**: The tracker checks if `defaultModel` is set to "auto" or empty
2. **Model Identification**: 
   - Checks last-known model from status file
   - Falls back to first available model
   - Uses "SELECTING..." if no model detected
3. **Formatting**: Displays as `AUTO\MODEL_NAME`

---

## 📁 Status File Format

The status file (`data/cursor_active_model_status.json`) stores:

```json
{
  "active_model": "AUTO\\ULTRON",
  "actual_model": "ULTRON",
  "is_auto_mode": true,
  "model_type": "auto",
  "provider": "ollama",
  "endpoint": "http://localhost:11434",
  "last_updated": "2026-01-13T18:58:08.123456"
}
```

**Fields:**
- `active_model`: Formatted display name (`AUTO\ULTRON`)
- `actual_model`: Just the model name (`ULTRON`)
- `is_auto_mode`: Boolean flag for auto mode

---

## 🚀 Usage

### Check Current Model
```powershell
python scripts/python/check_active_model.py
```

**Output:**
```
📊 CURRENT STATUS:
   Active Model: AUTO\ULTRON
   Model Type: auto
```

### Monitor Continuously
```powershell
python scripts/python/cursor_active_model_tracker.py --monitor
```

**Updates status file every second with:**
- `AUTO\MODEL` format when in auto mode
- `MODEL` format when explicitly set

---

## 💡 Benefits

1. **Clear Indication**: Immediately see if Auto mode is active
2. **Model Visibility**: Know which model is being used even in Auto
3. **Consistent Format**: Same format across all tools and displays
4. **Easy Parsing**: Simple to parse `AUTO\MODEL` format programmatically

---

## 🔧 Implementation

The format is implemented in:
- `cursor_active_model_tracker.py` - Detects and formats
- `check_active_model.py` - Displays formatted name
- Status file - Stores both formatted and actual model name
