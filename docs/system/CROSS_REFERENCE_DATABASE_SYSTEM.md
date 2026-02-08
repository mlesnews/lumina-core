# Cross-Reference Database System for All LUMINA Databases

**Status:** ✅ **ACTIVE**  
**Purpose:** Cross-reference all Helpdesk/GitHub/CursorID tickets and all LUMINA databases

---

## Overview

The cross-reference database provides unified cross-referencing across **ALL** of LUMINA's databases, linking:
- Request IDs
- Helpdesk Tickets
- GitHub PRs
- CursorID Tickets
- All LUMINA database entries

---

## Architecture

### Central Database
**File:** `data/cross_reference/cross_reference_database.json`

Stores:
- Request IDs → Related tickets/PRs
- Helpdesk Tickets → Related Request IDs/PRs
- GitHub PRs → Related Request IDs/tickets
- CursorID Tickets → Related Request IDs/PRs
- All LUMINA database references

### Cross-Reference Index

```
Request ID: 7a9f31d7-62ff-479b-ae17-3546c5eafeb3
    ├─→ Helpdesk Ticket: PM000000001
    ├─→ GitHub PR: #123
    ├─→ CursorID Ticket: 22f50c1b8c589929
    └─→ Database: data/diagnostics/request_id_tracking_*.json
```

---

## Supported Identifiers

### 1. Request IDs
- **Format:** UUID (e.g., `7a9f31d7-62ff-479b-ae17-3546c5eafeb3`)
- **Sources:** Cursor IDE, retry actions, diagnostics

### 2. Helpdesk Tickets
- **Format:** Team-specific
  - Problem Management: `PM000000001`
  - Change Management: `CR000000001`
  - Task: `T000000001`
- **Sources:** Helpdesk system

### 3. GitHub PRs
- **Format:** PR number (e.g., `#123`)
- **Sources:** GitHub repository

### 4. CursorID Tickets
- **Format:** Ticket ID (e.g., `22f50c1b8c589929`)
- **Sources:** Notification ticket system

---

## Database Scanning

### Automatic Scanning

The system scans **ALL** LUMINA databases:
- `data/` directory (all JSON files)
- Request IDs found in any file
- Ticket numbers
- PR references
- Cross-references

### Manual Scanning

```bash
python scripts/python/cross_reference_database.py --scan-all
```

This will:
1. Scan all JSON files in `data/` directory
2. Extract Request IDs (UUID format)
3. Extract ticket numbers
4. Extract PR references
5. Build cross-reference index

---

## Usage Examples

### Add Cross-Reference

```bash
python scripts/python/cross_reference_database.py \
    --add \
    --request-id "7a9f31d7-62ff-479b-ae17-3546c5eafeb3" \
    --helpdesk-ticket "PM000000001" \
    --github-pr "#123" \
    --cursor-id-ticket "22f50c1b8c589929"
```

### Find References

```bash
# Find by Request ID
python scripts/python/cross_reference_database.py \
    --find "7a9f31d7-62ff-479b-ae17-3546c5eafeb3"

# Find by Helpdesk Ticket
python scripts/python/cross_reference_database.py \
    --find "PM000000001"

# Find by GitHub PR
python scripts/python/cross_reference_database.py \
    --find "#123"
```

### Scan All Databases

```bash
python scripts/python/cross_reference_database.py --scan-all
```

---

## Integration Points

### 1. Retry Manager
- Automatically adds cross-references when retry occurs
- Links Request ID to tickets/PRs

### 2. Ticket Tracker
- Creates cross-references when tickets are created
- Links tickets to Request IDs

### 3. Jupyter Notebooks
- Receives cross-reference data
- Problem Management and Change Management teams

### 4. All LUMINA Databases
- Scanned for identifiers
- Indexed in cross-reference database

---

## Database Structure

```json
{
  "request_ids": {
    "7a9f31d7-...": {
      "helpdesk_ticket": "PM000000001",
      "github_pr": "#123",
      "cursor_id_ticket": "22f50c1b8c589929",
      "metadata": {}
    }
  },
  "helpdesk_tickets": {
    "PM000000001": {
      "request_id": "7a9f31d7-...",
      "github_pr": "#123",
      "cursor_id_ticket": "22f50c1b8c589929"
    }
  },
  "github_prs": {
    "#123": {
      "request_id": "7a9f31d7-...",
      "helpdesk_ticket": "PM000000001",
      "cursor_id_ticket": "22f50c1b8c589929"
    }
  },
  "lumina_databases": {
    "scanned_at": "2026-01-08T...",
    "databases": [...],
    "total_databases": 150
  }
}
```

---

## Benefits

### 1. Unified Search
- Find any identifier and get all related references
- Search across all systems from one place

### 2. Complete Traceability
- Track Request ID through entire lifecycle
- See all related tickets, PRs, and database entries

### 3. Team Coordination
- Problem Management sees all related data
- Change Management sees all related data
- All teams have complete context

### 4. Database Integration
- All LUMINA databases cross-referenced
- No data silos
- Complete system visibility

---

## Status

✅ **Cross-Reference Database:** ACTIVE  
✅ **Database Scanning:** ENABLED  
✅ **Team Integration:** CONFIGURED  
✅ **All LUMINA Databases:** INDEXED

---

## Tags

#CROSS_REFERENCE #DATABASE #HELPDESK #GITHUB #CURSOR_ID #LUMINA #UNIFIED_SEARCH @JARVIS @LUMINA

---

**Created:** 2026-01-08T02:50:00  
**Status:** ✅ **ACTIVE - CROSS-REFERENCES ALL LUMINA DATABASES**
