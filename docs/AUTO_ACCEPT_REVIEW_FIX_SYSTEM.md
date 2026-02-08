# Auto-Accept, Review, Fix System - @MANUS #EVOLUTION

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

---

## Overview

Complete system for automatically handling "ACCEPT ALL CHANGES" in sub-sessions:
1. **Auto-Accept** - Automatically accepts all changes after running
2. **Auto-Review** - Reviews all changes for issues
3. **Auto-Fix** - Fixes all issues found during review
4. **MARVIN Roasting** - Always roasts asks to identify gaps and bloat
5. **JARVIS Gap Closing** - Uses MARVIN roasts to close gaps and reduce bloat

---

## Problem Statement

**ISSUE**: Multiple sub-agent chats or single one-off sessions have "ACCEPT ALL CHANGES" pending, which require:
- Being saved
- Being reviewed
- Being fixed
- Input back into the workflow loop

**SOLUTION**: Automated system that handles all of this automatically.

---

## Architecture

### System Flow

```
User Ask
    ↓
Master Session (JARVIS)
    ├─→ MARVIN Roasts Ask
    │   ├─→ Identifies Gaps
    │   ├─→ Identifies Bloat
    │   ├─→ Identifies Missing Integrations
    │   ├─→ Identifies Incomplete Workflows
    │   └─→ Identifies Unused Code
    ↓
JARVIS Closes Gaps
    ├─→ Creates Actions from Roast
    ├─→ Executes Actions
    └─→ Closes Gaps & Reduces Bloat
    ↓
Match to Workflows
    ↓
Spawn Sub-Session
    ↓
Sub-Session Execution
    ↓
AUTO-ACCEPT ALL CHANGES
    ↓
AUTO-REVIEW CHANGES
    ↓
AUTO-FIX ISSUES
    ↓
Feed Back to Workflow Loop
```

---

## Components

### 1. MARVIN Roast System

**File**: `scripts/python/marvin_roast_system.py`

**Purpose**: Roast asks to identify gaps, bloat, and issues.

**Features**:
- ✅ **Gap Identification** - Finds missing implementations
- ✅ **Bloat Identification** - Finds duplicate/unused code
- ✅ **Missing Integration Identification** - Finds missing connections
- ✅ **Incomplete Workflow Identification** - Finds broken workflows
- ✅ **Unused Code Identification** - Finds dead code

**Output**: `MarvinRoast` with findings and recommendations.

### 2. JARVIS Gap Closer

**File**: `scripts/python/jarvis_gap_closer.py`

**Purpose**: Uses MARVIN roasts to close gaps and reduce bloat.

**Features**:
- ✅ **Action Creation** - Creates actions from roast findings
- ✅ **Gap Closure** - Implements missing functionality
- ✅ **Bloat Reduction** - Removes duplicate/unused code
- ✅ **Integration Completion** - Completes missing integrations
- ✅ **Workflow Completion** - Completes incomplete workflows
- ✅ **Code Consolidation** - Consolidates unused code

**Output**: `GapClosureResult` with actions and results.

### 3. Workflow Auto Review & Fix

**File**: `scripts/python/workflow_auto_review_fix.py`

**Purpose**: Automatically accepts, reviews, and fixes changes.

**Features**:
- ✅ **Auto-Accept** - Automatically accepts all changes
- ✅ **Auto-Review** - Reviews all changes for issues
- ✅ **Auto-Fix** - Fixes all issues found
- ✅ **Chat History** - Maintains agent chat histories
- ✅ **Workflow Feedback** - Feeds back into workflow loop

**Output**: `ReviewResult` with review and fix results.

### 4. Master Workflow Orchestrator Integration

**File**: `scripts/python/master_workflow_orchestrator.py`

**Purpose**: Coordinates all sub-sessions with auto-accept/review/fix.

**Features**:
- ✅ **MARVIN Integration** - Always roasts asks
- ✅ **JARVIS Integration** - Always closes gaps from roasts
- ✅ **Auto-Review/Fix Integration** - Automatically handles sub-sessions
- ✅ **Sub-Session Management** - Manages all sub-sessions

---

## Usage

### Automatic Operation

The system operates automatically:

1. **User makes ask** → Master session receives it
2. **MARVIN roasts ask** → Identifies gaps and bloat
3. **JARVIS closes gaps** → Creates and executes actions
4. **Workflow matching** → Matches to workflows
5. **Sub-session spawned** → Created for execution
6. **Sub-session executes** → Workflow runs
7. **Auto-accept** → All changes automatically accepted
8. **Auto-review** → All changes reviewed
9. **Auto-fix** → All issues fixed
10. **Feedback loop** → Results fed back to workflow

### Manual Operation

```python
from master_workflow_orchestrator import MasterWorkflowOrchestrator

# Initialize orchestrator
orchestrator = MasterWorkflowOrchestrator()

# Receive ask (MARVIN roasts automatically, JARVIS closes gaps automatically)
ask_id = orchestrator.receive_user_ask(
    "Complete the incomplete workflow",
    priority=8
)

# Get workflow matches
matches = orchestrator.get_workflow_matches_for_ask(ask_id)

# Spawn sub-session
if matches:
    sub_session_id = orchestrator.spawn_sub_session(ask_id, matches[0])
    
    # Start sub-session
    orchestrator.start_sub_session(sub_session_id)
    
    # Execute workflow (in sub-session)
    # ... workflow code ...
    
    # Complete sub-session (auto-accept/review/fix happens automatically)
    orchestrator.complete_sub_session(
        sub_session_id,
        success=True,
        result={"value": 100.0}
    )
```

---

## MARVIN Roasting

### Roast Categories

1. **Gaps** - Missing implementations
2. **Bloat** - Duplicate/unused code
3. **Missing Integrations** - Missing connections
4. **Incomplete Workflows** - Broken workflows
5. **Unused Code** - Dead code

### Severity Levels

- **Critical** - Blocks functionality
- **High** - Significant impact
- **Medium** - Moderate impact
- **Low** - Minor impact

### Example Roast

```python
from marvin_roast_system import MarvinRoastSystem

roaster = MarvinRoastSystem()
roast = roaster.roast_ask(
    "complete_the_lumina_extension",
    "Complete the Lumina extension we've been working on for a year"
)

print(roast.summary)
# Output: "🔥 MARVIN ROAST: 2 gap(s) identified, 1 incomplete workflow(s). Total severity: 15.0"
```

---

## JARVIS Gap Closing

### Action Types

1. **Implement** - Implement missing functionality
2. **Remove** - Remove bloat
3. **Integrate** - Complete missing integrations
4. **Complete** - Complete incomplete workflows
5. **Consolidate** - Consolidate unused code

### Example Gap Closure

```python
from jarvis_gap_closer import JarvisGapCloser

closer = JarvisGapCloser()
result = closer.close_gaps_from_roast("ask_id", roast)

print(f"Gaps Closed: {result.gaps_closed}")
print(f"Bloat Reduced: {result.bloat_reduced}")
print(f"Actions Completed: {result.actions_completed}")
```

---

## Auto-Review & Fix

### Review Process

1. **Auto-Accept** - All changes automatically accepted
2. **Review** - Changes reviewed for issues
3. **Fix** - Issues automatically fixed
4. **Feedback** - Results fed back to workflow

### Review Checks

- Syntax errors
- TODO/FIXME markers
- Hardcoded secrets
- Missing file paths
- Invalid change types

### Fix Capabilities

- Basic syntax fixes
- Indentation fixes
- Secret detection
- File validation

---

## Integration Points

### Master Workflow Orchestrator

- Receives user asks
- Triggers MARVIN roasting
- Triggers JARVIS gap closing
- Spawns sub-sessions
- Auto-accepts/reviews/fixes sub-sessions

### Workflow Base

- Integrates with `WorkflowAutoReviewFix`
- Tracks changes
- Maintains chat histories
- Feeds back to workflow

### Master Session Manager

- Consolidates all sessions
- Tracks all interactions
- Manages master session

---

## Configuration

### Auto-Accept Settings

- **Auto-accept enabled**: Yes (default)
- **Review enabled**: Yes (default)
- **Auto-fix enabled**: Yes (default)

### MARVIN Settings

- **Always roast**: Yes (default)
- **Severity threshold**: Medium (default)
- **Roast categories**: All (default)

### JARVIS Settings

- **Always close gaps**: Yes (default)
- **Action priority**: Based on severity (default)
- **Auto-execute**: Yes (default)

---

## Best Practices

1. **Always use master session** - All coordination through master
2. **Let MARVIN roast** - Always roast asks to identify issues
3. **Let JARVIS close gaps** - Always close gaps from roasts
4. **Auto-accept/review/fix** - Automatically handle all changes
5. **Feed back to workflow** - Always feed results back

---

## Status

✅ **MARVIN Roast System** - Operational  
✅ **JARVIS Gap Closer** - Operational  
✅ **Auto-Review & Fix** - Operational  
✅ **Master Orchestrator Integration** - Operational  

---

**Last Updated**: 2025-01-24  
**Status**: ✅ **OPERATIONAL**

