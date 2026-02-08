# Automatic Workflow Archiving System

**Status:** ✅ **ACTIVE**  
**Date:** 2026-01-08  
**Tags:** #AUTOMATIC_ARCHIVING #CERTIFICATION #DOCUMENTATION #WORKFLOW #HELPDESK #FINTECH #EOL #ROI

---

## Overview

The Automatic Workflow Archiving System automatically archives workflows, helpdesk tickets, and business/technical areas when they meet all criteria:

1. **Certification Passed** - Workflow has passed certification
2. **Documentation Complete** - All documentation is complete and successful
3. **No Issues** - No documented issues remain

This applies to:
- **Cursor IDE workflows** (and any IDE framework)
- **Agent workflows** and frameworks
- **@N8N integrations** and maintenance
- **Helpdesk tickets** (PM, CM, notification tickets)
- **Company business and technical areas**
- **FINTECH** business and technical domains

All archived items are tracked until **@EOL** (End of Life) and **@ROI** (Return on Investment).

---

## Architecture

### Components

1. **Automatic Workflow Archiver** (`jarvis_automatic_workflow_archiver.py`)
   - Main archiving engine
   - Scans and archives eligible items
   - Manages archive locations

2. **Workflow Certification Manager** (`jarvis_workflow_certification_manager.py`)
   - Manages certification status
   - Certifies/revokes certifications
   - Tracks certification details

3. **Documentation Status Manager** (`jarvis_documentation_status_manager.py`)
   - Tracks documentation completion
   - Manages documentation status
   - Tracks issues

### Archive Locations

- **Helpdesk Tickets:** `data/archives/helpdesk/`
- **Workflows:** `data/archives/workflows/`
- **N8N Integrations:** `data/archives/n8n/`
- **Business Areas:** `data/archives/business/`
- **Technical Areas:** `data/archives/technical/`

---

## Certification Process

### Certifying a Workflow/Ticket/Area

```bash
# Certify a helpdesk ticket
python scripts/python/jarvis_workflow_certification_manager.py --certify PM000000001:helpdesk_pm

# Certify an agent workflow
python scripts/python/jarvis_workflow_certification_manager.py --certify workflow_123:cursor_agent --notes "All tests passed"

# Certify an N8N integration
python scripts/python/jarvis_workflow_certification_manager.py --certify n8n_integration_456:n8n
```

### Certification Criteria

For certification to pass, the following must be verified:
- ✅ Functionality verified
- ✅ Integration tested
- ✅ Performance acceptable
- ✅ Security validated

---

## Documentation Status

### Marking Documentation Complete

```bash
# Mark documentation complete
python scripts/python/jarvis_documentation_status_manager.py --complete workflow_123:cursor_agent --docs README.md API.md INTEGRATION.md

# Check documentation status
python scripts/python/jarvis_documentation_status_manager.py --status workflow_123:cursor_agent
```

### Documentation Requirements

Documentation must be:
- ✅ Complete (all required docs present)
- ✅ Successful (no failed documentation)
- ✅ No issues documented

---

## Automatic Archiving

### Scanning and Archiving

The system automatically scans all items and archives those meeting criteria:

```bash
# Scan and archive all eligible items
python scripts/python/jarvis_automatic_workflow_archiver.py --scan-all
```

### Manual Archiving

```bash
# Archive a specific helpdesk ticket
python scripts/python/jarvis_automatic_workflow_archiver.py --archive-ticket PM000000001:PM

# Archive a specific workflow
python scripts/python/jarvis_automatic_workflow_archiver.py --archive-workflow workflow_123:agent:cursor

# Archive an N8N integration
python scripts/python/jarvis_automatic_workflow_archiver.py --archive-n8n n8n_integration_456

# Archive a business/technical area
python scripts/python/jarvis_automatic_workflow_archiver.py --archive-area area_789:business
```

---

## Archive Metadata

Each archived item includes:

```json
{
  "status": "archived",
  "archived_at": "2026-01-08T05:00:00",
  "archived_by": "JARVIS_Automatic_Archiver",
  "archiving_reason": "Certification passed, documentation complete, no issues",
  "archive_metadata": {
    "certified": true,
    "documentation_complete": true,
    "no_issues": true,
    "certification_details": {...}
  },
  "eol_tracking": {
    "end_of_life_date": null,
    "roi_metrics": {
      "return_on_investment": null,
      "tracking_enabled": true
    }
  }
}
```

---

## EOL and ROI Tracking

### End of Life (EOL)

Archived items are tracked until End of Life:
- EOL date is set when item reaches end of life
- Maintenance continues until EOL
- Post-EOL items remain in archive for historical reference

### Return on Investment (ROI)

ROI metrics are tracked for archived items:
- ROI calculation and tracking enabled
- Metrics updated as data becomes available
- Used for business decision-making

---

## Integration with Post-Startup Checklist

The automatic archiving system is integrated into the AI post-startup checklist:

- **ID:** `automatic_workflow_archiving`
- **Priority:** High
- **Runs:** Automatically on system startup
- **Frequency:** Once per startup (can be run manually)

---

## Workflow Types Supported

### Cursor IDE Workflows
- Agent workflows
- Framework integrations
- IDE-specific workflows

### Any IDE Framework
- Generic IDE workflows
- Framework-agnostic agent workflows
- Cross-platform integrations

### N8N Integrations
- N8N workflow automations
- N8N node integrations
- N8N maintenance workflows

### Helpdesk Tickets
- **PM (Problem Management)** tickets
- **CM (Change Management)** tickets
- **Notification tickets** (Cursor IDE request IDs, etc.)

### Business Areas
- FINTECH business domains
- Company business processes
- Business workflow automations

### Technical Areas
- Technical implementations
- System integrations
- Technical workflows

---

## Usage Examples

### Complete Workflow: Certify → Document → Archive

```bash
# Step 1: Certify the workflow
python scripts/python/jarvis_workflow_certification_manager.py --certify my_workflow:cursor_agent --notes "All tests passed, integration verified"

# Step 2: Mark documentation complete
python scripts/python/jarvis_documentation_status_manager.py --complete my_workflow:cursor_agent --docs README.md API.md

# Step 3: Archive (automatic on next scan, or manual)
python scripts/python/jarvis_automatic_workflow_archiver.py --archive-workflow my_workflow:agent:cursor
```

### Automatic Scanning

The system automatically scans on startup (via post-startup checklist) and archives all eligible items.

---

## Status Tracking

### Certification Status Files
Location: `data/workflow_certifications/`
Format: `{item_type}_{item_id}_certification.json`

### Documentation Status Files
Location: `data/documentation_status/`
Format: `{item_type}_{item_id}_docs.json`

### Archive Files
Location: `data/archives/{category}/`
Format: `{item_id}_{details}_archived_{timestamp}.json`

---

## Criteria Summary

For an item to be automatically archived, it must meet **ALL** of these criteria:

1. ✅ **Certified** - Certification status is "certified" and passed = true
2. ✅ **Documentation Complete** - Documentation status is "complete" and all_successful = true
3. ✅ **No Issues** - has_issues = false and no issues in issues array

---

## Maintenance Until EOL

All archived items:
- Continue to be maintained until End of Life
- ROI tracking enabled
- Historical reference maintained
- Can be reactivated if needed (revoke archive status)

---

## FINTECH Context

The system is designed with FINTECH business and technical areas in mind:
- Financial workflow tracking
- Compliance documentation
- Audit trail maintenance
- ROI measurement for financial systems

---

## Tags

#AUTOMATIC_ARCHIVING #CERTIFICATION #DOCUMENTATION #WORKFLOW #HELPDESK #FINTECH #EOL #ROI #CURSOR_IDE #N8N #AGENT #FRAMEWORK

---

**Created:** 2026-01-08T05:00:00  
**Status:** ✅ **ACTIVE - AUTOMATIC ARCHIVING ENABLED**
