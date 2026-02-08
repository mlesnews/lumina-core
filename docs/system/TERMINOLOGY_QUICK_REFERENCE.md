# Terminology Quick Reference - Request ID, @ask, @job

**Date:** 2026-01-14  
**Status:** ✅ **QUICK REFERENCE**  
**Purpose:** Prevent interchangeable usage that causes context loss

---

## 🎯 Three Distinct Terms - DO NOT INTERCHANGE

### Request ID
**What:** Technical identifier for API requests/operations  
**When:** Debugging, logging, tracing, error correlation  
**Format:** UUID/hex (e.g., `4060f8dd-268b-4165-8889-4a25d89ace31`)  
**Context:** Technical/operational  
**Lifespan:** Ephemeral (short-lived)

### @ask
**What:** Implementation plan item  
**When:** Feature development, project management, strategic work  
**Format:** `PM` + 9 digits (e.g., `PM000000001`)  
**Context:** Project management  
**Lifespan:** Long-lived (project work)

### @job
**What:** Background job / scheduled task  
**When:** Job scheduling, background processing, work queues  
**Format:** Varies (job IDs, slot IDs, etc.)  
**Context:** Job scheduling / operational  
**Lifespan:** Variable

---

## ❌ WRONG - Interchangeable Usage

- ❌ "Request ID for this ask"
- ❌ "Job request ID"
- ❌ "Ask job ID"
- ❌ Using any term for another's purpose

---

## ✅ CORRECT - Context-Specific Usage

- ✅ "Request ID: `4060f8dd-...` (API call)"
- ✅ "Ask: `pm000000001` (implementation work)"
- ✅ "Job: `job_12345` (background task)"

---

## 📋 Decision Tree

**Need to track an API call/operation?** → **Request ID**  
**Need to track implementation work?** → **@ask**  
**Need to track background job?** → **@job**

---

**"Request ID ≠ @ask ≠ @job. Use the correct term for the correct context."** - @JARVIS
