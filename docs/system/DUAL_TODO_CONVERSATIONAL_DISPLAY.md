# Dual TODO List with Conversational Display

**Date:** 2026-01-09  
**System:** JARVIS Conversational TODO Display  
**Tags:** #JARVIS @LUMINA #TODO #CONVERSATIONAL

---

## Overview

The Dual TODO List system provides:
1. **Master TODO List** - Persistent across all sessions
2. **Padawan/OEM TODO List** - Session-specific tasks
3. **Auto-collapse after timeout** - Streamlines developer experience
4. **Conversational integration** - Natural language triggers
5. **Grammarly oversight** - JARVIS control over grammar corrections

---

## Features

### 1. Dual List Management

**Master TODO List:**
- Stored in: `data/todo/master_todos.json`
- Persistent across all sessions
- Long-term project tasks
- Strategic items

**Padawan/OEM TODO List:**
- Stored in: `data/ask_database/master_padawan_todos.json`
- Session-specific tasks
- Current workflow items
- Temporary/contextual tasks

### 2. Auto-Collapse After Timeout

**Default Timeout:** 5 minutes (300 seconds)

**Behavior:**
- Lists expand when interacted with
- Auto-collapse after timeout period
- Shows summary when collapsed
- Expand on demand with conversational triggers

**Configuration:**
```python
from jarvis_dual_todo_manager import JARVISDualTODOManager

manager = JARVISDualTODOManager()
manager.set_timeout(300.0)  # 5 minutes
```

### 3. Conversational Integration

**Natural Language Triggers:**
- "show todos"
- "show todo"
- "todos"
- "todo list"
- "what's pending"
- "what's next"
- "tasks"
- "show master"
- "show padawan"
- "show oem"

**Usage:**
```python
from jarvis_conversational_todo_display import JARVISConversationalTODODisplay

display = JARVISConversationalTODODisplay()
result = display.handle_conversational_trigger("show todos")
if result:
    print(result)  # Displays both lists
```

### 4. Grammarly Oversight

**JARVIS Control:**
- Monitors Grammarly corrections
- Applies conversational flow rules
- Preserves natural language intent
- Overrides when needed for natural conversation

**Rules:**
- `conversational_mode`: Preserve natural flow
- `allow_informal`: Allow casual language ("gonna", "wanna")
- `preserve_voice_tone`: Don't over-formalize
- `ignore_casual_errors`: Ignore minor errors in conversation
- `min_confidence`: Only apply high-confidence corrections

**Configuration:** `config/grammarly_oversight_rules.json`

---

## Usage Examples

### Display Both Lists

```python
from jarvis_conversational_todo_display import get_conversational_todo_display

# Get formatted display
display_text = get_conversational_todo_display()
print(display_text)
```

**Output:**
```
## 📋 TODO Lists

### 🎯 Master TODO List (3 pending, 5 completed)
1. ⏳ Implement voice-to-action automation improvements
2. 🔄 Verify N8N is running in container and accessible
3. ⏳ Test DNS failover between NAS and pfSense

### 📝 Padawan/OEM TODO List (2 pending, 9 completed)
1. ⏳ List all containers on NAS and identify centralized containers
2. ⏳ Verify MCP container is managing centralized containers
```

### When Collapsed (After Timeout)

```
## 📋 TODO Lists

*Lists collapsed (timeout: 300s)*
**Master:** 3 pending, 5 completed
**Padawan/OEM:** 2 pending, 9 completed

*Say 'show todos' or interact to expand*
```

### Add TODO Items

```python
from jarvis_dual_todo_manager import JARVISDualTODOManager

manager = JARVISDualTODOManager()

# Add to master list
master_id = manager.add_master_todo(
    "Implement new feature X",
    priority=1,
    tags=["feature", "high-priority"]
)

# Add to Padawan/OEM list
padawan_id = manager.add_padawan_todo(
    "Fix bug in session Y",
    priority=2,
    tags=["bug", "session"]
)
```

### Update TODO Status

```python
from jarvis_dual_todo_manager import JARVISDualTODOManager, TODOStatus

manager = JARVISDualTODOManager()

# Mark as in-progress
manager.update_todo_status("master_1234567890", TODOStatus.IN_PROGRESS)

# Mark as completed
manager.update_todo_status("padawan_1234567890", TODOStatus.COMPLETED)
```

### Grammarly Oversight

```python
from jarvis_grammarly_oversight import JARVISGrammarlyOversight

oversight = JARVISGrammarlyOversight()

# Review a Grammarly contribution
contribution = oversight.review_contribution(
    original_text="I'm gonna do that",
    corrected_text="I am going to do that",
    suggestions=["Use 'going to' instead of 'gonna'"],
    confidence=0.8,
    context="conversational chat"
)

# In conversational mode, this will likely be IGNORED
# to preserve natural flow
print(contribution.action)  # GrammarlyAction.IGNORE
```

---

## Integration with JARVIS Chat

### Automatic Display

The system can be integrated to automatically show TODO lists:
- At the start of each session
- After completing tasks
- When user asks about tasks
- Periodically (if configured)

### Conversational Flow

**Example Conversation:**
```
User: "What do we have pending?"
JARVIS: [Shows expanded TODO lists]

[5 minutes pass, no interaction]

User: "Show todos"
JARVIS: [Shows expanded TODO lists again]
```

### Grammarly Integration

When Grammarly-CLI suggests corrections:
1. JARVIS oversight reviews the suggestion
2. Applies conversational flow rules
3. Decides: CORRECT, SUGGEST, or IGNORE
4. Preserves natural language intent

---

## Configuration

### Auto-Collapse Timeout

```python
manager = JARVISDualTODOManager()
manager.set_timeout(600.0)  # 10 minutes
```

### Grammarly Rules

Edit `config/grammarly_oversight_rules.json`:

```json
{
  "conversational_mode": true,
  "allow_informal": true,
  "preserve_voice_tone": true,
  "min_confidence": 0.7,
  "auto_apply": false
}
```

---

## File Structure

```
data/
├── todo/
│   ├── master_todos.json          # Master TODO list
│   └── display_state.json         # Display state (collapse/expand)
├── ask_database/
│   └── master_padawan_todos.json  # Padawan/OEM TODO list
└── grammarly/
    └── contributions.json         # Grammarly contribution history

config/
└── grammarly_oversight_rules.json # Grammarly oversight rules

scripts/python/
├── jarvis_dual_todo_manager.py           # Core TODO management
├── jarvis_conversational_todo_display.py # Conversational display
└── jarvis_grammarly_oversight.py        # Grammarly oversight
```

---

## CLI Usage

### Show TODO Lists

```bash
python scripts/python/jarvis_dual_todo_manager.py --show
```

### Add TODO

```bash
# Master list
python scripts/python/jarvis_dual_todo_manager.py --add-master "New task"

# Padawan list
python scripts/python/jarvis_dual_todo_manager.py --add-padawan "Session task"
```

### Expand Lists

```bash
python scripts/python/jarvis_dual_todo_manager.py --expand
```

### Set Timeout

```bash
python scripts/python/jarvis_dual_todo_manager.py --timeout 600
```

### Grammarly Oversight

```bash
# Show summary
python scripts/python/jarvis_grammarly_oversight.py --summary

# Enable conversational mode
python scripts/python/jarvis_grammarly_oversight.py --conversational-mode true
```

---

## Benefits

1. **Streamlined Experience**: Auto-collapse reduces visual clutter
2. **Natural Conversation**: Conversational triggers feel natural
3. **Dual Context**: Master (strategic) + Padawan (tactical)
4. **Grammar Control**: JARVIS preserves conversational intent
5. **Always Visible**: Both lists shown at all times (when expanded)

---

## Future Enhancements

- Voice integration for hands-free TODO management
- Smart prioritization based on context
- Integration with JARVIS intelligence system
- Cross-session TODO migration (Padawan → Master)
- Real-time collaboration on TODO items

---

**Tags:** #JARVIS @LUMINA #TODO #CONVERSATIONAL #GRAMMARLY
