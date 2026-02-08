# How to See What AI Model Cursor is Using (Especially in Auto Mode)

## 🚨 Quick Answer

**When Cursor is set to "Auto", the model is displayed as `AUTO\MODEL_NAME` format.**

Example: `AUTO\ULTRON` or `AUTO\GROK`

This shows Auto mode is active AND which model is being used.

---

## 📍 Where to Look in Cursor UI

### Method 1: Chat Input Dropdown (Easiest)
1. **Look at the chat input box** (bottom of Cursor)
2. **Click the dropdown** next to the input field
3. The **currently selected model** is shown at the top
4. Even in "Auto" mode, it shows which model was selected

### Method 2: Model Selector Button
1. In the chat panel, look for a **model name button** or **dropdown**
2. Usually appears as: `[Model Name ▼]` or `[Auto ▼]`
3. Click it to see:
   - Current model (if explicitly set)
   - "Auto" indicator (if in auto mode)
   - List of available models

### Method 3: Status Bar (If Available)
1. Check the **bottom-right corner** of Cursor
2. Some versions show the active model there
3. May appear as: `🤖 Model: Claude` or similar

### Method 4: Command Palette
1. Press `Ctrl+Shift+P`
2. Type `model` or `select model`
3. See model-related commands and current selection

---

## 🔧 Using Scripts to Check

### Quick Check (One-Time)
```powershell
python scripts/python/check_active_model.py
```

**Output shows:**
- Current active model
- Model type (local/cloud/auto)
- Available models
- Endpoint information

### Continuous Monitoring
```powershell
python scripts/python/cursor_active_model_tracker.py --monitor
```

**Monitors and updates:**
- `data/cursor_active_model_status.json` (updated every second)
- Shows in console what model is active

### Check Status File Directly
```powershell
cat data/cursor_active_model_status.json
```

**Shows:**
```json
{
  "active_model": "AUTO\\ULTRON",
  "actual_model": "ULTRON",
  "is_auto_mode": true,
  "model_type": "auto",
  "provider": "ollama",
  "endpoint": "http://localhost:11434",
  "last_updated": "2026-01-13T18:56:08.123456"
}
```

**Format:**
- `AUTO\MODEL` = Auto mode with detected model
- `MODEL` = Explicitly set model

---

## 🤔 When "Auto" Mode is Active

**The Challenge:**
- Auto mode dynamically selects models based on context
- The model might change during a conversation
- There's no permanent UI indicator

**Solutions:**

1. **Check the chat input dropdown** - Shows what model will be used for the next message
2. **Look at the response** - Some models include their name in the response
3. **Check network requests** (F12 → Network tab) - See which API endpoint was called
4. **Use the status tracker** - Run the monitoring script to see changes in real-time

---

## 📊 Current Status (From Last Check)

Based on your configuration:

- **Active Model**: ULTRON (virtual_cluster)
- **Provider**: ollama
- **Endpoint**: http://localhost:11434
- **Type**: Local model

**Available Models:**
- IRON-LEGION (KAIJU: 10.17.17.11:3001)
- iron-legion (KAIJU: 10.17.17.11:3001)
- codellama-kaiju (KAIJU: 10.17.17.11:3001)

---

## 🎯 Quick Commands

| Command | What It Does |
|---------|-------------|
| `python scripts/python/check_active_model.py` | One-time check of active model |
| `python scripts/python/cursor_active_model_tracker.py --status` | Show current status |
| `python scripts/python/cursor_active_model_tracker.py --monitor` | Monitor continuously |
| `python scripts/python/cursor_active_model_tracker.py --update` | Update status file once |

---

## 💡 Pro Tips

1. **If you can't see the model in UI:**
   - Run the check script - it reads from Cursor's settings
   - The status file is always up-to-date if monitoring is running

2. **To see which model was ACTUALLY used:**
   - Check the network tab (F12) during a request
   - Look for API calls to model endpoints
   - The endpoint URL tells you which model

3. **To force a specific model:**
   - Click the model selector in chat
   - Choose a specific model instead of "Auto"
   - The script will then show that model as active

---

## 📁 Related Files

- **Status File**: `data/cursor_active_model_status.json`
- **Tracker Script**: `scripts/python/cursor_active_model_tracker.py`
- **Quick Check**: `scripts/python/check_active_model.py`
- **Cursor Settings**: `C:\Users\mlesn\AppData\Roaming\Cursor\User\settings.json`
