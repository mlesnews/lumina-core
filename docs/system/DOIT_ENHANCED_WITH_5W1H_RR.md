# @DOIT Enhanced - With Automatic @5W1H and @RR

**Status:** ✅ **ACTIVE**  
**Date:** 2026-01-08

---

## Overview

Enhanced @DOIT command that **automatically** applies:
- **@5W1H** (Who, What, When, Where, Why, How) questioning framework
- **@RR** (Root Cause Analysis) for all issues
- Systematic problem detection and resolution

---

## Core Concept

> **"@5W1H and @RR should already be part of the @doit or /doit command."**

### The Enhancement

- **Automatic 5W1H:** Every @DOIT automatically applies 5W1H questioning
- **Automatic Root Cause:** Every @DOIT automatically analyzes root causes
- **No Manual Steps:** Everything happens automatically
- **Systematic Execution:** ORDER 66 - Execute immediately

---

## Implementation

### Script

**File:** `scripts/python/doit_enhanced.py`

**Features:**
- Automatic @5W1H analysis
- Automatic @RR (Root Cause Analysis)
- Solution generation
- Systematic execution
- Integration with existing DOIT workflow

### Integration

**Components:**
- `doit_5w1h_workflow.py` - 5W1H questioning framework
- `root_cause_analysis.py` - Root cause analysis
- `jarvis_5w1h_troubleshooter.py` - Troubleshooting system

---

## Usage

### Basic Usage

```bash
python scripts/python/doit_enhanced.py "Fix IMVA not working"
```

**Automatically:**
1. Applies @5W1H analysis
2. Applies @RR (Root Cause Analysis)
3. Generates solutions
4. Executes (ORDER 66)

### Options

```bash
# Skip 5W1H
python scripts/python/doit_enhanced.py "Task" --no-5w1h

# Skip Root Cause Analysis
python scripts/python/doit_enhanced.py "Task" --no-rr

# Plan only (don't execute)
python scripts/python/doit_enhanced.py "Task" --no-execute
```

---

## Workflow

```
@DOIT Command
    ↓
Automatic @5W1H Analysis
    ↓
Automatic @RR (Root Cause Analysis)
    ↓
Generate Solutions
    ↓
Execute (ORDER 66)
    ↓
Save Results
```

---

## 5W1H Analysis

### Automatic Questions

1. **WHO:** Who is involved/affected?
2. **WHAT:** What needs to be done?
3. **WHEN:** When should this be done? (ORDER 66 - immediately)
4. **WHERE:** Where does this apply?
5. **WHY:** Why is this important?
6. **HOW:** How should this be accomplished? (ORDER 66 - systematically)

### Integration

- Uses `DOIT5W1HWorkflow` for structured analysis
- Falls back to `JARVIS_5W1H_Troubleshooter` if needed
- Provides basic fallback if components unavailable

---

## Root Cause Analysis

### Automatic Analysis

- Identifies root causes of problems
- Analyzes why issues occur
- Provides solutions
- Tracks resolved/unresolved causes

### Integration

- Uses `RootCauseAnalysis` system
- Checks for problem keywords
- Identifies relevant root causes
- Provides actionable insights

---

## Solution Generation

### Automatic Solutions

- Generates 3 viable actionable solutions
- Evaluates feasibility
- Selects best solution
- Creates execution plan

### Integration

- Uses `DOIT5W1HWorkflow` solution generation
- Considers 5W1H analysis
- Applies root cause insights
- Executes systematically

---

## VA Health Detection Integration

### Automatic Detection

The autonomous AI agent now:
- Checks VA health before working on TODOs
- Detects failed VAs (like IMVA)
- Automatically fixes failed VAs
- Ensures all required VAs are running

### VA Health Detector

**File:** `scripts/python/va_health_detector.py`

**Features:**
- Checks all VAs (JARVIS, IMVA, ACVA, etc.)
- Detects crashed/failed VAs
- Automatically launches failed VAs
- Reports health status

---

## Example: Fixing IMVA

### Problem

- IMVA not working
- Autonomous agent didn't detect it
- No automatic fix

### Solution (Using @DOIT Enhanced)

```bash
python scripts/python/doit_enhanced.py "Fix IMVA not working and ensure autonomous agent detects VA failures"
```

**Result:**
- ✅ 5W1H Analysis applied
- ✅ Root Cause Analysis applied
- ✅ Solutions generated
- ✅ VA Health Detector integrated
- ✅ Autonomous agent now checks VA health

---

## Status

✅ **@DOIT Enhanced:** ACTIVE  
✅ **Automatic @5W1H:** ACTIVE  
✅ **Automatic @RR:** ACTIVE  
✅ **VA Health Detection:** ACTIVE  
✅ **Autonomous Agent Integration:** ACTIVE

---

## Tags

#DOIT #ORDER66 #5W1H #ROOT_CAUSE #AUTOMATIC #VA_HEALTH #LUMINA @JARVIS @TEAM @POPPA @PALPATINE

---

**Created:** 2026-01-08T04:39:00  
**Status:** ✅ **ACTIVE - AUTOMATIC @5W1H AND @RR INTEGRATED**
