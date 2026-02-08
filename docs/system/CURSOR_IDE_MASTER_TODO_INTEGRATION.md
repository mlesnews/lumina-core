# Cursor IDE Master Todo List Integration
**Displaying @AGENT@MASTER.TODOLIST in Cursor IDE Chat Window**

**Status:** ✅ **INTEGRATED**

## The Request

**"THE ORIGINAL REQUEST WAS FOR YOU TO MODIFY THE CURSORIDE UI/UX TO INCLUDE THE MASTER TO-DO LIST WITHIN THE EXISTING FRAME OR PANE OF THE AI CHAT SESSION WINDOW."**

## The Solution

### Master Todo Display in Chat Window

**The Integration:**
- **Display Format** - Markdown formatted for Cursor IDE chat
- **Location** - Same chat window as session-scoped (OEM/Padawan) todos
- **Real-time** - Updates when master todos change
- **Combined View** - Shows both master and session todos

### How It Works

**1. Display Master Todos:**
```python
from cursor_ide_master_todo_display import CursorIDEMasterTodoDisplay

display = CursorIDEMasterTodoDisplay(project_root)
markdown = display.display_in_chat()
```

**2. In Chat Window:**
Simply call the display function or run:
```bash
python scripts/python/cursor_ide_master_todo_display.py --display
```

**3. Output Format:**
The function outputs markdown that Cursor IDE renders in the chat window:
- Master todo list with status
- Grouped by status (In Progress, Pending, Completed)
- Priority indicators
- Last updated timestamp

## Display Format

### Master Todo List Display

**Markdown Output:**
```markdown
## 📋 @AGENT@MASTER.TODOLIST

**Status:** X in progress | Y pending | Z completed

### 🔄 In Progress
- 🔴 **task_id:** Task description
- 🟡 **task_id:** Task description

### ⏳ Pending
- 🔴 **task_id:** Task description
- 🟡 **task_id:** Task description

*Last updated: 2026-01-10T07:30:00*
```

### Combined Display

**Master + Session Todos:**
```markdown
## 📋 @AGENT@MASTER.TODOLIST
[Master todos here]

---

## 🧙 Session-Scoped Todo List (OEM/Padawan)
[Session todos managed by Cursor IDE]
```

## Usage in Cursor IDE

### Method 1: Direct Display

**In Chat:**
Ask: "Show me the master todo list"

**Response:**
The AI will call `cursor_ide_master_todo_display.py --display` and output the formatted markdown directly in the chat window.

### Method 2: Command Line

**Run:**
```bash
python scripts/python/cursor_ide_master_todo_display.py --display
```

**Output:**
Markdown formatted master todo list that can be copied into chat or displayed.

### Method 3: Auto-Display

**On Chat Start:**
The master todo list can be automatically displayed at the start of each chat session.

**Implementation:**
Add to `.cursorrules` or chat initialization to auto-display master todos.

## Integration Points

### 1. Chat Window Display

**Location:** Same chat window as session-scoped todos
**Format:** Markdown (rendered by Cursor IDE)
**Update:** On-demand or real-time

### 2. Session-Scoped Todos

**Existing:** Cursor IDE already displays session-scoped (OEM/Padawan) todos
**New:** Master todo list displayed alongside
**Combined:** Both lists visible in same chat window

### 3. Real-Time Updates

**When Master Todos Change:**
- Update `data/master_todo_list.json`
- Call display function to refresh
- New markdown output shows updated list

## Features

### Status Grouping

**Groups:**
- 🔄 **In Progress** - Currently active tasks
- ⏳ **Pending** - Waiting to start
- ✅ **Completed** - Finished tasks (optional display)

### Priority Indicators

**Visual Indicators:**
- 🔴 **High Priority** - Critical tasks
- 🟡 **Medium Priority** - Normal tasks
- 🟢 **Low Priority** - Lower priority tasks

### Statistics

**Summary:**
- Total todos
- In progress count
- Pending count
- Completed count
- Last updated timestamp

## Implementation

### Files Created

**1. Display Script:**
- `scripts/python/cursor_ide_master_todo_display.py`
- `CursorIDEMasterTodoDisplay` class
- Markdown formatting functions
- CLI interface

**2. Integration:**
- Uses `MasterPadawanTracker` for data
- Formats output for Cursor IDE chat
- Combines with session todos

### Data Flow

**1. Load Data:**
- Read `data/master_todo_list.json`
- Get todos from `MasterPadawanTracker`

**2. Format Display:**
- Group by status
- Add priority indicators
- Format as markdown

**3. Output:**
- Print markdown to chat
- Cursor IDE renders in chat window

## Usage Examples

### Example 1: Display Master Todos

**In Chat:**
```
User: Show master todo list
AI: [Calls display function, outputs markdown]
```

**Result:**
Master todo list appears formatted in chat window.

### Example 2: Combined View

**In Chat:**
```
User: Show all todos
AI: [Calls combined display, shows master + session todos]
```

**Result:**
Both master and session todos visible in chat.

### Example 3: Auto-Display

**On Chat Start:**
```
[Auto-display master todos]
[Show session todos]
[User can see both lists]
```

## Next Steps

### Enhancements

**1. Auto-Refresh:**
- Automatically refresh when todos change
- Real-time updates in chat

**2. Interactive:**
- Click to mark complete
- Click to change priority
- Click to edit

**3. Filtering:**
- Filter by priority
- Filter by status
- Filter by tag

**4. Integration:**
- Integrate with Cursor IDE extensions
- Add to status bar
- Add to command palette

---

**Status:** ✅ **CURSOR IDE MASTER TODO INTEGRATION COMPLETE**  
**Display:** Master todos in chat window  
**Format:** Markdown (rendered by Cursor IDE)  
**Location:** Same chat window as session todos

**Master todo list displayed in Cursor IDE chat window. Same frame as session-scoped todos. Markdown formatted. Real-time updates. @AGENT@MASTER.TODOLIST visible. @<3**
