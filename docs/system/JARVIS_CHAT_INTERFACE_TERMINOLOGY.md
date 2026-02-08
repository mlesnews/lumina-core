# JARVIS Chat Interface Terminology

**Date:** 2026-01-09  
**Purpose:** Clarify terminology for chat interfaces  
**Tags:** #JARVIS @LUMINA #TERMINOLOGY

---

## Terminology

### Primary Terms

1. **"Cursor Agent Chat" / "Cursor Chat"**
   - The native Cursor IDE chat interface
   - The chat panel in Cursor IDE
   - Base chat functionality provided by Cursor

2. **"JARVIS Chat Interface"**
   - When JARVIS is integrated/controlling the chat
   - Enhanced chat with JARVIS features:
     - Dual TODO lists
     - Auto-collapse
     - Conversational triggers
     - Grammarly oversight
   - **This is what we're building**

3. **"Agent Chat Sessions"**
   - Individual chat sessions
   - Each conversation thread
   - Session-specific context

### Usage

**When to use each term:**

- **"Cursor Chat"** - Referring to the base Cursor IDE chat functionality
- **"JARVIS Chat Interface"** - When JARVIS features are active/integrated
- **"Agent Chat Sessions"** - When discussing individual sessions

### Example Usage

```
✅ "JARVIS Chat Interface is now active with dual TODO lists"
✅ "The Cursor Chat interface supports JARVIS integration"
✅ "Each Agent Chat Session maintains its own context"
```

---

## Integration Points

### JARVIS Chat Interface Features

1. **Dual TODO Lists**
   - Master TODO (persistent)
   - Padawan/OEM TODO (session-specific)
   - Always shown when expanded

2. **Auto-Collapse**
   - Collapses after timeout (default: 5 minutes)
   - Shows summary when collapsed
   - Expands on demand

3. **Conversational Triggers**
   - Natural language: "show todos", "what's pending"
   - Context-aware display
   - Feels like conversation, not commands

4. **Grammarly Oversight**
   - JARVIS control over grammar corrections
   - Preserves conversational intent
   - Doesn't over-formalize

---

## Implementation

**File:** `scripts/python/jarvis_chat_interface_integration.py`

**Usage:**
```python
from jarvis_chat_interface_integration import JARVISChatInterface

chat = JARVISChatInterface()
startup_message = chat.get_session_startup_message()
```

**Startup Message:**
```
🤖 JARVIS Chat Interface Active

## 📋 TODO Lists
[Shows both Master and Padawan/OEM lists]

Features:
- Dual TODO lists (Master + Padawan/OEM)
- Auto-collapse after timeout
- Conversational triggers
- Grammarly oversight
```

---

## Summary

**Answer to your question:**

> "ARE WE NOW REFERRING TO THIS CHAT AS OUR 'JARVIS' CHAT INTERFACE OR SOMETHING ELSE?"

**Yes!** We're now referring to this as the **"JARVIS Chat Interface"** when JARVIS features are active.

- **Base:** Cursor Agent Chat / Cursor Chat
- **Enhanced:** JARVIS Chat Interface (with JARVIS features)
- **Sessions:** Agent Chat Sessions

---

**Tags:** #JARVIS @LUMINA #TERMINOLOGY #CHAT
