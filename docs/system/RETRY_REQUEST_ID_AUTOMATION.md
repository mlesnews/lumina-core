# Retry Request ID Automation System

**Status:** ✅ **ACTIVE**  
**Purpose:** Automatically include Request ID in next @OP @SEND after @RETRY

---

## Overview

The last step of the stock OEM mechanic Cursor-IDE @RETRY automatically includes the "Request ID" in the next @OP @SEND of @REQUEST.

### Workflow

```
1. User clicks @RETRY in Cursor IDE
   ↓
2. System captures Request ID
   ↓
3. Cross-references with Helpdesk/GitHub/CursorID tickets
   ↓
4. Sends to Jupyter Problem Management notebook
   ↓
5. Generates next @OP @SEND template with Request ID included
   ↓
6. Updates cross-reference database
```

---

## Components

### 1. Cursor Retry with Request ID
**File:** `scripts/python/cursor_retry_with_request_id.py`

- Captures Request ID from retry action
- Cross-references with tickets
- Generates next request template
- Sends to Jupyter notebooks

### 2. Cross-Reference Database
**File:** `scripts/python/cross_reference_database.py`

- Cross-references all LUMINA databases
- Links Request IDs, Helpdesk tickets, GitHub PRs, CursorID tickets
- Provides unified search across all systems

### 3. Jupyter Notebooks

#### Problem Management
**File:** `notebooks/problem_management/problem_management.ipynb`
- Receives retry actions with Request IDs
- Tracks problems and root cause analysis
- Team: Problem Management Team

#### Change Management
**File:** `notebooks/change_management/change_management.ipynb`
- Receives change requests with Request IDs
- Tracks changes and deployments
- Team: Change Management Team

---

## Cross-Referencing

### Supported Ticket Types

1. **Request IDs** (Cursor IDE)
   - Format: UUID (e.g., `7a9f31d7-62ff-479b-ae17-3546c5eafeb3`)
   - Source: Cursor IDE errors

2. **Helpdesk Tickets**
   - Format: Team-specific (e.g., `PM000000001`, `CR000000001`)
   - Source: Helpdesk system

3. **GitHub PRs**
   - Format: PR number (e.g., `#123`)
   - Source: GitHub

4. **CursorID Tickets**
   - Format: Ticket ID (e.g., `22f50c1b8c589929`)
   - Source: Notification ticket system

### Cross-Reference Flow

```
Request ID
    ↓
Cross-Reference Database
    ↓
├─→ Helpdesk Ticket
├─→ GitHub PR
├─→ CursorID Ticket
└─→ All LUMINA Databases
```

---

## Team Integration

### Problem Management Team
- **Manager:** @marvin
- **Technical Lead:** @r2d2
- **Notebook:** `notebooks/problem_management/problem_management.ipynb`
- **Tags:** #PROBLEMMANAGEMENT #HELPDESK

### Change Management Team
- **Manager:** @c3po
- **Technical Lead:** @r2d2
- **Notebook:** `notebooks/change_management/change_management.ipynb`
- **Tags:** #CHANGEMANAGEMENT #HELPDESK

---

## Usage

### Automatic (Recommended)

When @RETRY is clicked in Cursor IDE:
1. Request ID is automatically captured
2. Cross-referenced with tickets
3. Sent to appropriate Jupyter notebook
4. Next @SEND template generated with Request ID

### Manual

```bash
# Handle retry with Request ID
python scripts/python/cursor_retry_with_request_id.py \
    --request-id "7a9f31d7-62ff-479b-ae17-3546c5eafeb3" \
    --error "Connection error" \
    --operator "@OP"
```

### Cross-Reference Database

```bash
# Add cross-reference
python scripts/python/cross_reference_database.py \
    --add \
    --request-id "7a9f31d7-62ff-479b-ae17-3546c5eafeb3" \
    --helpdesk-ticket "PM000000001" \
    --github-pr "#123"

# Find references
python scripts/python/cross_reference_database.py \
    --find "7a9f31d7-62ff-479b-ae17-3546c5eafeb3"

# Scan all LUMINA databases
python scripts/python/cross_reference_database.py --scan-all
```

---

## Next @OP @SEND Template

After retry, the system generates a template like:

```
@OP @SEND @REQUEST

Request ID: 7a9f31d7-62ff-479b-ae17-3546c5eafeb3

Cross-References:
  Helpdesk Ticket: PM000000001
  GitHub PR: #123
  Ticket ID: 22f50c1b8c589929

Original Error: Connection error

[Your request here - Request ID automatically included]
```

---

## Database Cross-Referencing

### All LUMINA Databases

The cross-reference database scans and indexes:
- All JSON files in `data/` directory
- Request IDs found in any database
- Ticket numbers
- GitHub PR references
- CursorID tickets

### Unified Search

Search for any identifier and find:
- Related Request IDs
- Related tickets
- Related PRs
- Related database entries

---

## Integration with Helpdesk

### Support Teams

Both teams have their own notebooks and workflows:

1. **Problem Management Team**
   - Receives problems and retries
   - Root cause analysis
   - Resolution tracking

2. **Change Management Team**
   - Receives changes and deployments
   - Impact analysis
   - Deployment coordination

### Cross-Reference

All tickets are cross-referenced:
- Request ID ↔ Helpdesk Ticket
- Request ID ↔ GitHub PR
- Request ID ↔ CursorID Ticket
- All ↔ All LUMINA Databases

---

## Status

✅ **Retry Request ID Automation:** ACTIVE  
✅ **Cross-Reference Database:** ACTIVE  
✅ **Jupyter Notebooks:** CREATED  
✅ **Team Integration:** CONFIGURED  
✅ **Database Scanning:** ENABLED

---

## Tags

#RETRY #REQUEST_ID #AUTOMATION #HELPDESK #CROSS_REFERENCE #PROBLEMMANAGEMENT #CHANGEMANAGEMENT #JUPYTER #DATABASE @JARVIS @LUMINA

---

**Created:** 2026-01-08T02:50:00  
**Status:** ✅ **ACTIVE - READY FOR USE**
