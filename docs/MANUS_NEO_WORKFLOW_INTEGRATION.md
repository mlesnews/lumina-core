# 🔄 MANUS-NEO Browser Workflow Integration

## Status: ✅ INTEGRATED

Neo AI browser is now integrated into MANUS workflow control system!

---

## Overview

MANUS can now orchestrate Neo browser automation as part of workflows. This enables:
- ✅ **Workflow-controlled browser automation**
- ✅ **Step-by-step task execution**
- ✅ **Error handling and recovery**
- ✅ **Workflow state tracking**
- ✅ **Integration with JARVIS and other MANUS systems**

---

## Quick Start

### Run ElevenLabs Setup Workflow

```bash
python scripts/python/manus_neo_workflow_integration.py --elevenlabs
```

This will:
1. Launch Neo browser
2. Navigate to ElevenLabs
3. Extract API key
4. Return result

### Run Custom Workflow

```bash
# Create workflow JSON file
python scripts/python/manus_neo_workflow_integration.py --workflow my_workflow.json
```

---

## Workflow Structure

### Example Workflow

```json
{
  "id": "my_workflow",
  "name": "My Automation Workflow",
  "description": "Automate a task",
  "stop_on_error": true,
  "steps": [
    {
      "action": "launch",
      "parameters": {
        "url": "https://example.com"
      }
    },
    {
      "action": "wait",
      "parameters": {
        "seconds": 3
      }
    },
    {
      "action": "fill_form",
      "parameters": {
        "url": "https://example.com/signup",
        "form_data": {
          "email": "user@example.com",
          "name": "John Doe"
        }
      }
    },
    {
      "action": "click",
      "parameters": {
        "selector": "button[type='submit']"
      }
    }
  ]
}
```

---

## Available Actions

### Browser Control
- `launch` / `open` - Launch browser with URL
- `navigate` / `goto` - Navigate to URL
- `close` - Close browser

### Page Interaction
- `execute_script` / `script` - Execute JavaScript
- `fill_form` - Fill form fields
- `click` - Click element by selector
- `get_page_info` - Get current page info

### Data Extraction
- `get_cookies` - Get cookies for domain
- `get_page_info` - Get page title, URL, etc.

### Utilities
- `wait` - Wait for specified seconds

---

## Integration with JARVIS

### From JARVIS Chat

```python
from manus_neo_workflow_integration import MANUSNEOWorkflowController

controller = MANUSNEOWorkflowController()

# Create workflow
workflow = {
    "id": "jarvis_task",
    "name": "JARVIS Browser Task",
    "steps": [
        {"action": "launch", "parameters": {"url": "https://example.com"}},
        {"action": "get_page_info", "parameters": {}}
    ]
}

# Execute
result = controller.execute_workflow(workflow)
```

### From MANUS Workflow System

MANUS can now include browser automation steps in any workflow:

```python
# MANUS workflow with browser step
workflow = {
    "steps": [
        {"type": "browser", "action": "launch", "url": "https://example.com"},
        {"type": "browser", "action": "navigate", "url": "https://example.com/page"},
        {"type": "other", "action": "process_data", "data": "..."}
    ]
}
```

---

## Pre-built Workflows

### ElevenLabs Setup

```bash
python scripts/python/manus_neo_workflow_integration.py --elevenlabs
```

Automates:
1. Opening ElevenLabs website
2. Navigating to API keys page
3. Extracting API key
4. Returning result

---

## Workflow Management

### Check Status

```bash
python scripts/python/manus_neo_workflow_integration.py --status WORKFLOW_ID
```

### List Active Workflows

```bash
python scripts/python/manus_neo_workflow_integration.py --list
```

---

## Error Handling

Workflows support:
- ✅ **Stop on error** - Halt workflow if step fails
- ✅ **Continue on error** - Skip failed steps and continue
- ✅ **Error logging** - All errors recorded in workflow history
- ✅ **State tracking** - Track which steps completed

---

## Files Created

1. ✅ `scripts/python/manus_neo_workflow_integration.py` - **Main integration** (USE THIS)
2. ✅ `docs/MANUS_NEO_WORKFLOW_INTEGRATION.md` - This guide

## Files Used

1. ✅ `manus_neo_browser_control.py` - Browser control system
2. ✅ `manus_neo_integration.py` - High-level integration layer

---

## Example: Complete Workflow

```python
from manus_neo_workflow_integration import MANUSNEOWorkflowController

controller = MANUSNEOWorkflowController()

# Create workflow
workflow = {
    "id": "website_signup",
    "name": "Website Signup Automation",
    "steps": [
        {
            "action": "launch",
            "parameters": {"url": "https://example.com/signup"}
        },
        {
            "action": "wait",
            "parameters": {"seconds": 3}
        },
        {
            "action": "fill_form",
            "parameters": {
                "form_data": {
                    "email": "user@example.com",
                    "password": "securepassword123",
                    "name": "John Doe"
                }
            }
        },
        {
            "action": "click",
            "parameters": {"selector": "button[type='submit']"}
        },
        {
            "action": "wait",
            "parameters": {"seconds": 2}
        },
        {
            "action": "get_page_info",
            "parameters": {}
        }
    ]
}

# Execute
result = controller.execute_workflow(workflow)

print(f"Success: {result['success']}")
print(f"Steps completed: {result['steps_completed']}/{result['steps_total']}")
```

---

## Integration Points

### With JARVIS
- JARVIS can trigger browser workflows
- Workflow results feed back to JARVIS
- JARVIS can monitor workflow progress

### With MANUS
- MANUS orchestrates browser workflows
- Browser steps integrated into larger workflows
- State management across all workflow types

### With Other Systems
- R5 knowledge aggregation from browser data
- Cookie extraction for authentication
- API key retrieval and storage

---

## Next Steps

1. **Test it**: Run the ElevenLabs setup workflow
2. **Create workflows**: Build custom automation workflows
3. **Integrate**: Use in JARVIS and MANUS systems

---

**Status**: ✅ Integrated and Ready  
**Feature**: Neo browser controlled by MANUS workflows  
**Created**: 2025-12-31
