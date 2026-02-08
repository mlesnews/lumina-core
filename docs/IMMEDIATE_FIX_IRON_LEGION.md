# 🚨 IMMEDIATE FIX: "Iron Legion" Model Error

## Current Error
```
Invalid Model: "The model Iron Legion does not work with your current plan or api key."
```

## Immediate Fix (No Reboot Needed)

### Step 1: Change Model in Chat Interface

1. **Open Cursor Chat**
   - Press `Ctrl+L` (or `Cmd+L` on Mac)
   - Or click the chat icon in sidebar

2. **Check Current Model Selection**
   - Look at the top of the chat panel
   - You'll see a model selector/dropdown
   - **If it says "Iron Legion"** - that's the problem!

3. **Change the Model**
   - Click on the model dropdown/selector
   - Select a valid Ollama model:
     - `qwen2.5:72b` (recommended)
     - `llama3`
     - `codellama:13b`
   - **DO NOT select "Iron Legion" or "ULTRON"** - these are not models!

4. **Start New Chat**
   - If the error persists, start a **new chat session**
   - Click the "+" button or "New Chat"
   - Select a valid model from the dropdown

### Step 2: Check Cursor Settings (Quick Check)

1. **Open Settings**
   - Press `Ctrl+,` (or `Cmd+,` on Mac)

2. **Search for "model"**
   - Type "model" in search box
   - Look for any setting that shows "Iron Legion" as a model

3. **Search for "Iron Legion"**
   - Type "Iron Legion" in search box
   - If you find any entries, check if they're using it as a model name
   - If so, change to an actual model like `qwen2.5:72b`

### Step 3: Clear Chat History (If Needed)

If the error persists:

1. **Close Current Chat**
   - Close the chat panel
   - Or start a completely new chat

2. **Clear Chat History** (Optional)
   - In Chat panel, look for history/clear options
   - Or manually delete chat sessions that used "Iron Legion"

## Why This Happens

Cursor is trying to use "Iron Legion" as a **model name**, but:
- ❌ "Iron Legion" is a **cluster/system name**, NOT a model
- ❌ "ULTRON" is a **virtual cluster name**, NOT a model
- ✅ `qwen2.5:72b` is an **actual Ollama model** - use this!

## Quick Model Reference

| What You See | What It Is | Action |
|--------------|------------|--------|
| "Iron Legion" | Cluster name | ❌ Don't select as model |
| "ULTRON" | Virtual cluster | ❌ Don't select as model |
| `qwen2.5:72b` | Actual model | ✅ Select this! |
| `llama3` | Actual model | ✅ Select this! |
| `codellama:13b` | Actual model | ✅ Select this! |

## If Still Not Working

1. **Check Ollama is Running**
   ```bash
   ollama list
   ```

2. **Verify Ollama Endpoint**
   - Settings → Search "ollama"
   - Endpoint should be: `http://localhost:11434`

3. **Restart Cursor** (if above doesn't work)
   - Close Cursor completely
   - Reopen Cursor
   - Try chat again with valid model

4. **Full Reboot** (last resort)
   - See `docs/CURSOR_REBOOT_FIX_GUIDE.md`

## Most Likely Solution

**The issue is in the Chat interface model selector:**
1. Open Chat (`Ctrl+L`)
2. Look at the model dropdown at the top
3. Change from "Iron Legion" to `qwen2.5:72b` or another Ollama model
4. Start a new chat if needed

---

**Created**: 2025-12-31  
**Priority**: High - Immediate fix
