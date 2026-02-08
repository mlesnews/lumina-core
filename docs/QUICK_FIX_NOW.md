# ⚡ QUICK FIX - Do This Now (No Reboot Needed)

## The Problem
You're seeing: `Invalid Model: "The model Iron Legion does not work with your current plan or api key."`

## The Solution (Takes 30 seconds)

### Step 1: Open Chat
- Press `Ctrl+L` (or click chat icon)

### Step 2: Check Model Selector
- Look at the **top of the chat panel**
- You'll see a **model dropdown/selector**
- **If it shows "Iron Legion" or "KAIJU Iron Legion"** - that's the problem!

### Step 3: Change the Model
1. **Click on the model dropdown** (where it says "Iron Legion")
2. **Select one of these instead:**
   - `qwen2.5:72b` ← **RECOMMENDED**
   - `llama3`
   - `ULTRON Cluster (Qwen2.5 72B)` ← This is OK (it uses qwen2.5:72b internally)

### Step 4: Start New Chat (If Error Persists)
- Click the **"+" button** or **"New Chat"**
- Make sure the new chat uses a valid model (not "Iron Legion")

## Why This Happens

Your settings file is **correct** - it has proper model names. But:
- Cursor's chat interface might be showing **"KAIJU Iron Legion"** as a selectable option
- When you select it, Cursor might be using the **title** instead of the **model name**
- The title "KAIJU Iron Legion" is fine, but Cursor needs to use the actual model (`llama3`)

## Visual Guide

**❌ WRONG - Don't select this:**
```
Model: [KAIJU Iron Legion ▼]
```

**✅ CORRECT - Select this instead:**
```
Model: [qwen2.5:72b ▼]
```
or
```
Model: [ULTRON Cluster (Qwen2.5 72B) ▼]
```

## If You Don't See the Model Dropdown

1. **Look at the top of the chat panel** - it should be there
2. **Try clicking in the chat input area** - the dropdown might appear
3. **Check if there's a settings icon** in the chat panel
4. **Try starting a completely new chat** - the model selector should appear

## Still Not Working?

1. **Close the chat panel** (`Ctrl+L` again)
2. **Reopen it** (`Ctrl+L`)
3. **Start a new chat** (click "+" or "New Chat")
4. **Select a model BEFORE typing anything**

---

**This should fix it immediately - no reboot needed!**
