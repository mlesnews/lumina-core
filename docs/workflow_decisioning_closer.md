# Workflow Decisioning Closer

**Date:** 2026-01-15
**Status:** ✅ Active
**Purpose:** Use #DECISIONING to update/close tickets, PM tasks, change requests, and archive chat sessions

---

## 🎯 **WORKFLOW**

### **Complete Workflow Process:**

1. **#DECISIONING** - Assess workflow completion
   - Uses `LuminaDecisioningEngine` to determine if workflow is complete
   - Checks tasks, tickets, documentation, verification status
   - Returns decision with confidence level

2. **Update and Close Items**
   - **Tickets**: Update status to "resolved", add resolution notes
   - **PM Tasks**: Update status to "completed", add completion notes
   - **Change Requests**: Update status to "closed", add closure notes
   - All items linked to session ID

3. **Archive Chat Session**
   - Archive agent chat session using `WalkAgentSessionsToArchive`
   - Session moved to archive with all metadata

---

## 🚀 **USAGE**

### **Command Line**

```bash
python scripts/python/jarvis_workflow_decisioning_closer.py \
  --session-id "session_123" \
  --ticket-ids "TICKET-001" "TICKET-002" \
  --pm-task-ids "PM-001" "PM-002" \
  --change-request-ids "CR-001" \
  --workflow-data workflow_data.json
```

### **From Workflow**

```python
from jarvis_workflow_decisioning_closer import WorkflowDecisioningCloser

closer = WorkflowDecisioningCloser(project_root=PROJECT_ROOT)

workflow_data = {
    "ticket_ids": ["TICKET-001", "TICKET-002"],
    "pm_task_ids": ["PM-001"],
    "change_request_ids": ["CR-001"],
    "tasks_completed": ["task1", "task2"],
    "documentation_complete": True,
    "verification_passed": True
}

results = closer.close_workflow("session_123", workflow_data)
```

---

## 📊 **DECISIONING LOGIC**

### **Decision Factors:**

- `tasks_completed`: List of completed tasks
- `tickets_resolved`: List of resolved tickets
- `pm_tasks_completed`: List of completed PM tasks
- `change_requests_closed`: List of closed change requests
- `documentation_complete`: Boolean - documentation complete
- `verification_passed`: Boolean - verification passed

### **Decision Actions:**

- `keep_all`: Workflow complete, proceed with closure
- `save`: Workflow mostly complete, save and continue
- `review`: Workflow needs review before closure
- `continue`: Workflow not ready, continue working

---

## 🎫 **TICKET UPDATES**

### **Ticket Update Fields:**

- `status`: Set to "resolved"
- `resolution_date`: Current timestamp
- `resolved_by`: "JARVIS Workflow Decisioning Closer"
- `resolution_notes`: "Workflow completed via session {session_id}"
- `session_id`: Link to chat session

---

## 📋 **PM TASK UPDATES**

### **PM Task Update Fields:**

- `status`: Set to "completed"
- `completion_date`: Current timestamp
- `completed_by`: "JARVIS Workflow Decisioning Closer"
- `completion_notes`: "Workflow completed via session {session_id}"
- `session_id`: Link to chat session

---

## 🔄 **CHANGE REQUEST UPDATES**

### **Change Request Update Fields:**

- `status`: Set to "closed"
- `closure_date`: Current timestamp
- `closed_by`: "JARVIS Workflow Decisioning Closer"
- `closure_notes`: "Workflow completed via session {session_id}"
- `session_id`: Link to chat session

---

## 📦 **SESSION ARCHIVING**

### **Archive Process:**

1. Session analyzed for completeness
2. V3 verification (if applicable)
3. Archive preparation
4. Move to archive directory
5. Update session metadata

### **Archive Location:**

```
data/agent_sessions/archive/{session_id}/
```

---

## 📊 **RESULTS**

### **Result Structure:**

```json
{
  "session_id": "session_123",
  "timestamp": "2026-01-15T14:30:00",
  "decision": {
    "action": "keep_all",
    "confidence": 0.95,
    "reasoning": "...",
    "complete": true
  },
  "tickets": {
    "updated": 2,
    "closed": 2,
    "errors": []
  },
  "pm_tasks": {
    "updated": 1,
    "closed": 1,
    "errors": []
  },
  "change_requests": {
    "updated": 1,
    "closed": 1,
    "errors": []
  },
  "archive": {
    "archived": true,
    "archive_path": "..."
  },
  "success": true
}
```

---

## 🔧 **INTEGRATION**

### **With Workflow Analyzer:**

After workflow analysis completes, automatically close workflow:

```python
# After workflow analysis
workflow_data = {
    "ticket_ids": extract_ticket_ids_from_analysis(),
    "pm_task_ids": extract_pm_task_ids_from_analysis(),
    "change_request_ids": extract_cr_ids_from_analysis(),
    "tasks_completed": analysis.get("tasks_completed", []),
    "documentation_complete": True,
    "verification_passed": True
}

closer.close_workflow(session_id, workflow_data)
```

### **With Continuous Analyzer:**

Add to `jarvis_workflow_continuous_analyzer.py`:

```python
# After opportunity execution
if execution_result.get("total_executed", 0) > 0:
    # Close workflow
    closer = WorkflowDecisioningCloser(project_root)
    closer.close_workflow(session_id, workflow_data)
```

---

## ✅ **STATUS**

**System:** ✅ Active
**Decisioning:** ✅ Integrated
**Ticket Updates:** ✅ Working
**PM Task Updates:** ✅ Working
**Change Request Updates:** ✅ Working
**Session Archiving:** ✅ Working

---

**Tags:** `#DECISIONING` `#WORKFLOW` `#TICKETS` `#ARCHIVE` `@JARVIS` `@LUMINA`
