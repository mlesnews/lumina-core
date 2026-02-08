# Terminology Clarification: Request ID, @ask, @job

**Date:** 2026-01-14  
**Status:** 🔄 **IN PROGRESS - CLARIFICATION NEEDED**  
**Issue:** Humans use terms interchangeably, causing confusion and loss of context

---

## 🎯 The Problem

**Humans tend to use terms interchangeably, to our detriment and at the expense of context.**

The terms **Request ID**, **@ask**, and **@job** are being used interchangeably, but they represent **different concepts** with **different contexts**.

---

## 📋 Three Distinct Concepts

### 1. Request ID
**Type:** Technical Identifier  
**Purpose:** Track individual API requests, operations, transactions  
**Context:** Low-level, technical, operational  
**Scope:** Single request/operation  
**Examples:**
- API request identifier
- HTTP request ID
- Transaction ID
- Operation tracking ID
- Error correlation ID

**Characteristics:**
- Ephemeral (short-lived)
- Technical/operational
- Used for debugging, logging, tracing
- Not a work item or task

### 2. @ask
**Type:** Implementation Plan Item  
**Purpose:** Track feature development, implementation work, project items  
**Context:** Project management, feature development  
**Scope:** Implementation plan, feature work  
**Format:** `PM` + 9 digits (e.g., `PM000000001`)  
**Examples:**
- `PM000000001` - Verify and Complete Feature Tracking
- `pm000000002` - Implement Automated Feature Tracking Sync
- `pm000000003` - Implement Real-Time Feature Updates

**Characteristics:**
- Long-lived (project work items)
- Strategic/planning
- Part of implementation plans
- Tracked in `data/ask_database/implementation_plan_tasks.json`

### 3. @job
**Type:** Background Job / Work Item  
**Purpose:** Track background jobs, scheduled tasks, work items  
**Context:** Job scheduling, background processing, work queues  
**Scope:** Background processing, scheduled work  
**Examples:**
- Background processing job
- Scheduled task
- Work queue item
- Job slot platform integration
- Channel transformation job

**Characteristics:**
- Can be ephemeral or persistent
- Operational/execution
- Background processing
- Job scheduling system

---

## 🔍 Key Distinctions

| Aspect | Request ID | @ask | @job |
|--------|-----------|------|------|
| **Purpose** | Track API/operation | Track implementation work | Track background jobs |
| **Context** | Technical/operational | Project management | Job scheduling |
| **Lifespan** | Ephemeral (short) | Long-lived | Variable |
| **Scope** | Single request | Feature/project | Background task |
| **Format** | UUID/hex/random | `pm` + 9 digits | Varies |
| **Tracking** | Request logs | Implementation plan | Job queue |

---

## ⚠️ Common Confusion Points

### Interchangeable Usage (WRONG) - Context Loss
- ❌ "The request ID for this ask is..." → **Loses context:** Request ID ≠ Ask ID
- ❌ "This job has request ID..." → **Loses context:** Job ≠ Request ID
- ❌ "The ask job request ID..." → **Loses context:** Mixing all three terms
- ❌ Using request ID as ask ID → **Wrong context:** Technical vs. Project
- ❌ Using ask ID as job ID → **Wrong context:** Project vs. Operational
- ❌ "Track this request ID as an ask" → **Confusion:** Different tracking systems

### Correct Usage - Preserving Context
- ✅ "Request ID: `4060f8dd-268b-4165-8889-4a25d89ace31` (for API call tracking)"
- ✅ "Ask ID: `pm000000001` (for implementation plan item)"
- ✅ "Job ID: `job_12345` (for background processing job)"
- ✅ "The request ID tracks the API call, the ask tracks the feature work, the job tracks the background task"
- ✅ "Request ID is for debugging, @ask is for project management, @job is for job scheduling"

---

## 📝 Proper Terminology

### When to Use Each Term

**Use "Request ID" when:**
- Tracking API requests
- Debugging errors
- Correlating logs
- Tracking individual operations
- Technical/operational context

**Use "@ask" when:**
- Referring to implementation plan items
- Feature development work
- Project management items
- Strategic planning
- Long-term work items

**Use "@job" when:**
- Referring to background jobs
- Scheduled tasks
- Work queue items
- Background processing
- Job scheduling context

---

## 🔧 Implementation Context

### Request ID System
- **Files:** `track_request_id.py`, `jarvis_request_tracking_system.py`
- **Purpose:** Track API requests, operations, transactions
- **Storage:** Request logs, diagnostics (`data/diagnostics/`)
- **Format:** UUID (e.g., `4060f8dd-268b-4165-8889-4a25d89ace31`), hex, or system-generated
- **Lifespan:** Ephemeral (short-lived, for debugging/tracing)
- **Example:** `4060f8dd-268b-4165-8889-4a25d89ace31` - API request identifier

### @ask System
- **Files:** `data/ask_database/implementation_plan_tasks.json`
- **Purpose:** Track implementation plan items, feature development
- **Storage:** Implementation plan database
- **Format:** `PM` + 9 digits (e.g., `PM000000001`)
- **Lifespan:** Long-lived (project work items)
- **Example:** `pm000000001` - "Verify and Complete Feature Tracking"

### @job System
- **Files:** `jarvis_job_slot_platform_integration.py`, `channel_transformation_job_processor.py`
- **Purpose:** Track background jobs, scheduled tasks, work queue items
- **Storage:** Job queue, job database
- **Format:** Varies by system (job IDs, slot IDs, etc.)
- **Lifespan:** Variable (can be ephemeral or persistent)
- **Example:** Job slot platform integration, background processing jobs

---

## ✅ Verification Checklist

**Before using terminology, verify:**
- [ ] Is this a technical API/operation identifier? → **Request ID**
- [ ] Is this an implementation plan item? → **@ask**
- [ ] Is this a background job/task? → **@job**
- [ ] Am I using the correct term for the context?
- [ ] Am I avoiding interchangeable usage?

---

## 🎯 Action Items

1. **Clarify in code:** Use proper terminology in code comments and documentation
2. **Update documentation:** Ensure all docs use correct terminology
3. **Code review:** Check for interchangeable usage
4. **Training:** Ensure team understands distinctions

---

## Tags

**Tags:** `#TERMINOLOGY` `#REQUEST_ID` `#ASK` `#JOB` `#CLARIFICATION` 
         `#CONTEXT` `@JARVIS` `@LUMINA`

---

**Status:** 🔄 **CLARIFICATION IN PROGRESS**

**"Request ID, @ask, and @job are NOT interchangeable. They represent different concepts with different contexts. Use the correct term for the correct context."** - @JARVIS
