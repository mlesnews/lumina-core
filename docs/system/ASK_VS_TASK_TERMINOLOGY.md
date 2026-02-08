# Ask vs Task Terminology - Help Desk Ticket Format

**Date:** 2026-01-14  
**Status:** ✅ **CLARIFIED**  
**Purpose:** Distinguish between "asks" (implementation plan items) and "tasks" (help desk tickets)

**⚠️ IMPORTANT:** Do NOT confuse with "Request ID" (technical/operational) or "@job" (background jobs). See `TERMINOLOGY_CLARIFICATION_REQUEST_ID_ASK_JOB.md` for full context.

---

## 🎯 Terminology Clarification

### "Ask" vs "Task"

**"Ask"** = Implementation plan items, feature requests, work items
- Format: `PM` + 9 digits (e.g., `PM000000001`)
- Used for: Implementation plans, feature development, project work
- Examples: `PM000000001`, `PM000000002`, `PM000000003`

**"Task"** = Help desk tickets (T + 9 digits)
- Format: `T` + 9 digits starting at `T300000001` (3,000,000+)
- Used for: Help desk issues, support tickets, bug reports
- Examples: `T300000001`, `T300000002`, `T300000003`

---

## 📋 Help Desk Ticket Format

### Syntax: T + 9 Digits

**Format:** `T` + 9 digits (zero-padded)

**Starting Number:** `T300000001` (3,000,000)

**Examples:**
- `T300000001` - First help desk ticket
- `T300000002` - Second help desk ticket
- `T300000003` - Third help desk ticket
- `T300000004` - Fourth help desk ticket
- `T300000005` - Fifth help desk ticket

### Progressive, Spiritual, and Unique

**Progressive:** Tickets increment sequentially  
**Spiritual:** Each ticket has meaning and purpose  
**Unique:** No duplicate ticket numbers

### Cross-Reference and Consolidation

**Cross-Reference:** Check previous tickets before creating new ones  
**Consolidate:** Merge related tickets when appropriate  
**No Duplicates:** Ensure tickets are unique and progressive

---

## 🔍 Existing Help Desk Tickets

**Location:** `data/helpdesk/tickets/`

**Existing T-Format Tickets:**
- `T000003001.json`
- `T000003002.json`
- `T000003003.json`
- `T000003004.json`
- `T000003005.json`

**Note:** These appear to be using 6-digit format. Should be updated to 9-digit format starting at T300000001.

---

## 📊 Implementation Plan Format

### Ask Format: pm + 9 Digits

**Format:** `pm` + 9 digits (zero-padded)

**Examples:**
- `pm000000001` - First ask (Verify and Complete Feature Tracking)
- `pm000000002` - Second ask (Implement Automated Feature Tracking Sync)
- `pm000000003` - Third ask (Implement Real-Time Feature Updates)
- `pm000000004` - Fourth ask (Implement Pattern Recognition Across Systems)
- `pm000000005` - Fifth ask (Implement Integration Analysis System)
- `pm000000006` - Sixth ask (Implement Dependency Mapping System)

---

## 🔄 Migration Notes

### From "Task" to "Ask"

**Updated Fields:**
- `task_id` → `ask_id`
- `total_tasks` → `total_asks`
- `tasks` → `asks` (in phases)
- All references updated to use "ask" terminology

**Reason:** Avoid confusion with help desk tickets (T + 9 digits)

---

## 📝 Help Desk Ticket System

### Ticket Creation

**Format:** `T` + 9 digits starting at `T300000001`

**Counter:** `data/helpdesk/ticket_counter.json`

**Syntax:**
```python
ticket_id = f"T{3000000 + counter:09d}"
# Example: T300000001, T300000002, etc.
```

### Ticket Properties

**Required Fields:**
- `ticket_id`: T + 9 digits
- `title`: Ticket title
- `description`: Ticket description
- `priority`: critical, high, medium, low
- `status`: open, in_progress, resolved, closed
- `component`: Affected component
- `issue_type`: bug, feature, task, etc.

**Optional Fields:**
- `github_pr_number`: Linked GitHub PR
- `gitlens_ref`: GitLens reference
- `linked_tickets`: Related ticket IDs
- `tags`: Ticket tags
- `metadata`: Additional metadata

---

## 🎯 Usage Examples

### Creating an Ask (Implementation Plan)

```python
ask = {
    "ask_id": "pm000000001",
    "ticket_number": "pm000000001",
    "title": "Verify and Complete Feature Tracking",
    "description": "...",
    "status": "completed"
}
```

### Creating a Help Desk Ticket

```python
ticket = {
    "ticket_id": "T300000001",
    "title": "Connection Error - Retry Manager Failed",
    "description": "...",
    "priority": "critical",
    "status": "open"
}
```

---

## ✅ Verification

**Terminology:**
- ✅ "Ask" used for implementation plan items
- ✅ "Task" reserved for help desk tickets
- ✅ Help desk tickets use T + 9 digits starting at T300000001
- ✅ Implementation asks use PM + 9 digits
- ✅ No confusion between asks and tasks

---

## Tags

**Tags:** `#ASK` `#TASK` `#HELPDESK` `#TICKET_FORMAT` `#TERMINOLOGY` 
         `@JARVIS` `@LUMINA` `#T300000001`

---

**Status:** ✅ **TERMINOLOGY CLARIFIED - ASK VS TASK**

**"Use 'ask' for implementation work, 'task' for help desk tickets. Help desk tickets use T + 9 digits starting at T300000001."** - @JARVIS
