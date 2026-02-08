# Sub-Ask Todo System - Each Sub-Ask Gets Its Own Todo List & Chat Session

**Date**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

---

## Overview

**Each sub-ask gets:**
1. ✅ **Its own todo list** - Dedicated todos for that sub-ask
2. ✅ **Its own sub-agent chat session** - Separate chat for that sub-ask
3. ✅ **Workflow completion tracking** - Tracks when workflows are completed
4. ✅ **Revisit/Update/Follow-up tracking** - Tracks chats that need attention

---

## Key Principle

**Every sub-ask is a separate entity with:**
- Its own todo list (in Master Todo Tracker)
- Its own sub-agent chat session (new or existing)
- Workflow completion status
- Status tracking (pending, needs_revisit, needs_update, needs_followup)

---

## How It Works

### 1. Sub-Ask Creation

When a sub-session is spawned, a sub-ask is automatically created:

```python
from master_workflow_orchestrator import MasterWorkflowOrchestrator

orchestrator = MasterWorkflowOrchestrator()

# Receive user ask
ask_id = orchestrator.receive_user_ask("Process outstanding items")

# Get workflow matches
matches = orchestrator.get_workflow_matches_for_ask(ask_id)

# Spawn sub-session (automatically creates sub-ask with todo list + chat session)
sub_session_id = orchestrator.spawn_sub_session(ask_id, matches[0])
```

**What happens automatically:**
1. ✅ Sub-ask created with unique ID
2. ✅ Todo list created for sub-ask
3. ✅ Sub-agent chat session created (or existing one used)
4. ✅ Todos added to Master Todo Tracker
5. ✅ Workflow completion todo added (if workflow exists)

---

### 2. Sub-Agent Chat Sessions

**New Chat Session:**
- Created when sub-ask is new
- Status: `NEW`
- Gets its own session ID

**Existing Chat Session (Revisit/Update/Follow-up):**
- Used when chat needs to be revisited
- Status: `NEEDS_REVISIT`, `NEEDS_UPDATE`, or `NEEDS_FOLLOWUP`
- Re-activated when sub-ask is created with `use_existing_chat` parameter

---

### 3. Todo List Management

Each sub-ask has its own todo list:

```python
from sub_ask_todo_manager import SubAskTodoManager

manager = SubAskTodoManager()

# Add todo to sub-ask
manager.add_todo_to_sub_ask(
    sub_ask_id="sub_ask_123",
    todo_title="Complete workflow execution",
    todo_description="Execute the workflow for this sub-ask",
    priority=Priority.HIGH
)
```

**Todos are:**
- Added to Master Todo Tracker
- Categorized by sub-ask ID
- Tagged with sub-ask ID and parent ask ID
- Tracked for completion

---

### 4. Chat Session Status Tracking

**Status Types:**
- `NEW` - New chat session created
- `EXISTING` - Existing chat session being used
- `NEEDS_REVISIT` - Needs to be revisited
- `NEEDS_UPDATE` - Needs to be updated
- `NEEDS_FOLLOWUP` - Needs follow-up
- `ACTIVE` - Currently active
- `ARCHIVED` - Completed and archived

**Marking chats for attention:**

```python
# Mark chat as needs revisit
manager.mark_chat_needs_revisit(
    session_id="chat_123",
    reason="Workflow incomplete, needs review"
)

# Mark chat as needs update
manager.mark_chat_needs_update(
    session_id="chat_123",
    reason="Configuration changed, needs update"
)

# Mark chat as needs follow-up
manager.mark_chat_needs_followup(
    session_id="chat_123",
    reason="Waiting for user input"
)
```

---

### 5. Workflow Completion

Track when workflows are completed:

```python
# Mark workflow as completed
manager.complete_workflow_for_sub_ask(sub_ask_id="sub_ask_123")
```

**What happens:**
- Sub-ask workflow_completed = True
- Chat session workflow_completed = True
- Status updated

---

## Using Existing Chat Sessions

When a chat needs to be revisited/updated/followed-up:

```python
# Create sub-ask using existing chat session
sub_ask = manager.create_sub_ask(
    parent_ask_id="parent_123",
    sub_ask_text="Revisit workflow execution",
    agent_name="Sub-Agent",
    workflow_id="workflow_123",
    use_existing_chat="chat_123"  # Use existing chat session
)
```

**What happens:**
- Existing chat session is re-activated
- Status changes from `NEEDS_REVISIT`/`NEEDS_UPDATE`/`NEEDS_FOLLOWUP` to `ACTIVE`
- New sub-ask linked to existing chat
- New todo list created for this revisit

---

## Finding Chats That Need Attention

```python
# Get sub-asks needing attention
needing_attention = manager.get_sub_asks_needing_attention()

for sub_ask in needing_attention:
    print(f"Sub-ask {sub_ask.sub_ask_id}: {sub_ask.status.value}")
    if sub_ask.chat_session:
        print(f"  Chat: {sub_ask.chat_session.session_id}")
        print(f"  Reason: {sub_ask.chat_session.revisit_reason or sub_ask.chat_session.update_reason or sub_ask.chat_session.followup_reason}")

# Get chat sessions needing attention
chats_needing_attention = manager.get_chat_sessions_needing_attention()

for chat in chats_needing_attention:
    print(f"Chat {chat.session_id}: {chat.chat_status.value}")
    print(f"  Reason: {chat.revisit_reason or chat.update_reason or chat.followup_reason}")
```

---

## Integration with Master Workflow Orchestrator

The system is automatically integrated:

1. **When sub-session is spawned:**
   - Sub-ask automatically created
   - Todo list automatically created
   - Chat session automatically created
   - Todos automatically added to Master Todo Tracker

2. **When workflow completes:**
   - Call `complete_workflow_for_sub_ask()` to mark complete

3. **When chat needs attention:**
   - Use `mark_chat_needs_revisit()`, `mark_chat_needs_update()`, or `mark_chat_needs_followup()`
   - Create new sub-ask with `use_existing_chat` to revisit

---

## Data Storage

**Files:**
- `data/sub_ask_todos/sub_asks.json` - All sub-asks
- `data/sub_ask_todos/chat_sessions.json` - All chat sessions

**Structure:**
```json
{
  "sub_ask_123": {
    "sub_ask_id": "sub_ask_123",
    "parent_ask_id": "ask_456",
    "sub_ask_text": "Execute workflow: Test Workflow",
    "status": "in_progress",
    "todo_list": {
      "sub_ask_id": "sub_ask_123",
      "todo_list_id": "todo_sub_ask_123",
      "todos": [...],
      "total_count": 3,
      "completed_count": 1
    },
    "chat_session": {
      "session_id": "chat_sub_ask_123",
      "sub_ask_id": "sub_ask_123",
      "agent_name": "Sub-Agent",
      "chat_status": "active",
      "workflow_completed": false
    },
    "workflow_id": "workflow_789",
    "workflow_completed": false
  }
}
```

---

## Status Flow

```
Sub-Ask Created
    ↓
Status: PENDING
Chat Status: NEW
    ↓
Work Started
    ↓
Status: IN_PROGRESS
Chat Status: ACTIVE
    ↓
[If needs attention]
    ↓
Status: NEEDS_REVISIT/UPDATE/FOLLOWUP
Chat Status: NEEDS_REVISIT/UPDATE/FOLLOWUP
    ↓
[Revisit with use_existing_chat]
    ↓
Status: IN_PROGRESS
Chat Status: ACTIVE
    ↓
Workflow Completed
    ↓
Status: COMPLETED
Chat Status: ARCHIVED
```

---

## Best Practices

1. **Always create sub-ask for sub-sessions** - Automatic via orchestrator
2. **Track workflow completion** - Call `complete_workflow_for_sub_ask()` when done
3. **Mark chats needing attention** - Use revisit/update/followup methods
4. **Use existing chats for revisits** - Pass `use_existing_chat` parameter
5. **Check for chats needing attention** - Use `get_chat_sessions_needing_attention()`

---

## Examples

### Example 1: Create Sub-Ask (Automatic)

```python
# This happens automatically when spawning sub-session
orchestrator = MasterWorkflowOrchestrator()
ask_id = orchestrator.receive_user_ask("Process items")
matches = orchestrator.get_workflow_matches_for_ask(ask_id)
sub_session_id = orchestrator.spawn_sub_session(ask_id, matches[0])

# Sub-ask, todo list, and chat session automatically created
```

### Example 2: Revisit Existing Chat

```python
manager = SubAskTodoManager()

# Mark chat as needs revisit
manager.mark_chat_needs_revisit(
    session_id="chat_123",
    reason="Workflow incomplete"
)

# Later, create new sub-ask using existing chat
sub_ask = manager.create_sub_ask(
    parent_ask_id="parent_123",
    sub_ask_text="Revisit incomplete workflow",
    use_existing_chat="chat_123"  # Reuse existing chat
)
```

### Example 3: Complete Workflow

```python
manager = SubAskTodoManager()

# Mark workflow as completed
manager.complete_workflow_for_sub_ask(sub_ask_id="sub_ask_123")
```

---

## Files Created

- ✅ `scripts/python/sub_ask_todo_manager.py` - Sub-ask todo manager
- ✅ `docs/SUB_ASK_TODO_SYSTEM.md` - This documentation

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

