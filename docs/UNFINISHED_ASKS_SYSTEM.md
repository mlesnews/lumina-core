# Unfinished Asks Collation & Organization System

**Last Updated**: 2025-12-28  
**Status**: ✅ Active System  
**Purpose**: Comprehensive tracking of all unfinished asks/tasks across all environments

---

## Overview

This system collates and organizes **all unfinished asks** from:
- Master Todo List
- Verified Todo List  
- Workflow steps
- Code comments (TODO/FIXME)
- Environment-specific TODO files
- Workflow patterns

**Result**: A unified, ongoing list that integrates with existing todo systems.

---

## System Components

### 1. Collation System (`collate_unfinished_asks.py`)

**Purpose**: Scans ALL environments to find unfinished tasks

**Sources Scanned**:
- ✅ Master Todo List (pending/in-progress)
- ✅ Verified Todo List (incomplete verified tasks)
- ✅ Workflow step tracking (incomplete steps)
- ✅ Code comments (TODO/FIXME/XXX/HACK/NOTE)
- ✅ Environment TODO.md files
- ✅ Workflow pattern analysis

**Output**:
- `data/todo/unfinished_asks_collation.json` - Complete data
- `UNFINISHED_ASKS_REPORT.md` - Human-readable report

**Usage**:
```bash
python scripts/python/collate_unfinished_asks.py
```

---

### 2. Organization System (`organize_unfinished_asks.py`)

**Purpose**: Organizes collated tasks into appropriate tracking systems

**Organization Strategy**:

#### A. Master Todo List
- **For**: Generic tasks, high-priority items, general development pipeline
- **Location**: `data/todo/master_todos.json`
- **Integration**: Integrated with Master Todo Tracker
- **Categories**: Added to appropriate categories

#### B. Workflow-Specific Todo Lists (Pattern-Based)
- **For**: Tasks that are steps in specific workflows
- **Location**: `data/todo/workflows/*_todos.md`
- **Purpose**: Pattern-based todo lists for workflow execution
- **Usage**: These are workflow steps that need to be part of the pattern todo list

#### C. Code Cleanup Tracking
- **For**: TODO/FIXME comments, code quality improvements
- **Location**: `data/todo/code_cleanup_tracking.json`
- **Purpose**: Separate tracking for technical debt

#### D. Environment-Specific
- **For**: Tasks specific to each environment
- **Location**: Respective environment TODO.md files
- **Purpose**: Keep environment-specific tasks in their environments

**Usage**:
```bash
python scripts/python/organize_unfinished_asks.py
```

---

## Decision Guide

### When to Add to Master Todo List

✅ **Add to Master Todo** when:
- Generic tasks that apply across the project
- High-priority items that need tracking
- Tasks that don't fit into workflow-specific patterns
- Items that should be part of the general development pipeline
- Tasks that need to be part of the ongoing master list

**Example**:
- "Enhance video quality" → Master Todo (video_production category)
- "System Integration Layer" → Master Todo (system_integration category)

---

### When to Use Workflow-Specific Todo Lists

✅ **Use Workflow-Specific** when:
- Tasks are steps in a specific workflow
- Pattern-based tasks (e.g., workflow execution steps)
- Tasks that are part of a workflow's todo list pattern
- Items that need to be tracked as part of workflow execution

**Example**:
- "WorkflowBase - Step 3" → Workflow-specific (WorkflowBase_todos.md)
- "DemoWorkflow - Step 5" → Workflow-specific (DemoWorkflow_todos.md)

**Pattern Todo List**: These are the "patiwan todo list" - workflow-specific steps that are part of the workflow pattern.

---

### When to Use Code Cleanup Tracking

✅ **Use Code Cleanup** when:
- TODO/FIXME comments in code
- Code quality improvements
- Technical debt items
- Refactoring tasks

**Example**:
- "TODO: Fix error handling" → Code cleanup tracking
- "FIXME: Update deprecated API" → Code cleanup tracking

---

### When to Keep Environment-Specific

✅ **Keep Environment-Specific** when:
- Tasks specific to a particular environment
- Environment configuration tasks
- Environment-specific features

**Example**:
- "Create task queue data structure" → cedarbrook-financial-services_llc-env TODO.md
- "Update lodash dependency" → cfs-llc-env TODO.md

---

## Workflow Integration

### Workflow Base Class Integration

The `WorkflowBase` class already tracks steps. Unfinished workflow steps are:
1. **Detected** during collation
2. **Organized** into workflow-specific todo lists
3. **Tracked** as part of the workflow pattern

**Pattern Todo List**: When a workflow has unfinished steps, they are added to a workflow-specific todo list (e.g., `WorkflowBase_todos.md`). This is the "patiwan todo list" - steps that need to be part of the workflow pattern.

---

## Ongoing Maintenance

### Regular Collation

Run collation periodically to catch new unfinished asks:

```bash
# Collate all unfinished asks
python scripts/python/collate_unfinished_asks.py

# Organize into appropriate systems
python scripts/python/organize_unfinished_asks.py
```

### Review Process

1. **Review Collation Report**: Check `UNFINISHED_ASKS_REPORT.md`
2. **Review Organization**: Check `UNFINISHED_ASKS_ORGANIZATION.md`
3. **Update Master Todo**: Add high-priority items manually if needed
4. **Workflow Integration**: Review workflow-specific todo lists
5. **Code Cleanup**: Schedule code cleanup tasks regularly

---

## Integration with Existing Systems

### Master Todo Tracker

✅ **Integrated**: Unfinished asks can be added to Master Todo List
- Uses existing `MasterTodoTracker` class
- Maintains categories and priorities
- Tracks in `data/todo/master_todos.json`

### Dual Todo System

✅ **Integrated**: Verified todos are included in collation
- Scans verified todo list for incomplete items
- Maintains verification status

### Workflow Base

✅ **Integrated**: Workflow steps are tracked
- Detects incomplete workflow steps
- Creates workflow-specific todo lists
- Integrates with workflow step tracking

---

## File Structure

```
.lumina/
├── scripts/python/
│   ├── collate_unfinished_asks.py      # Collation system
│   ├── organize_unfinished_asks.py      # Organization system
│   ├── master_todo_tracker.py           # Master Todo Tracker
│   └── dual_todo_system.py              # Dual Todo System
├── data/todo/
│   ├── master_todos.json                # Master Todo List
│   ├── verified_todos.json              # Verified Todo List
│   ├── unfinished_asks_collation.json   # Collation data
│   ├── code_cleanup_tracking.json       # Code cleanup tasks
│   └── workflows/                       # Workflow-specific todo lists
│       ├── WorkflowBase_todos.md
│       ├── DemoWorkflow_todos.md
│       └── ...
├── UNFINISHED_ASKS_REPORT.md            # Collation report
└── UNFINISHED_ASKS_ORGANIZATION.md      # Organization summary
```

---

## Statistics (Current)

From last collation (2025-12-28):
- **Total Unfinished Asks**: 450
- **By Source**:
  - Code comments: 370
  - Environment TODO files: 73
  - Workflow patterns: 5
  - Master Todo: 2
- **By Recommendation**:
  - Code cleanup: 370
  - Environment-specific: 73
  - Workflow-specific: 5
  - Generic category: 2

---

## Best Practices

### 1. Regular Collation
- Run collation weekly or after major changes
- Review reports before organizing

### 2. Organization Decisions
- Use Master Todo for general tasks
- Use Workflow-Specific for pattern-based tasks
- Use Code Cleanup for technical debt
- Keep Environment-Specific in their environments

### 3. Workflow Integration
- Review workflow-specific todo lists regularly
- Integrate workflow steps into workflow patterns
- Track workflow completion

### 4. Code Cleanup
- Schedule code cleanup tasks regularly
- Prioritize high-impact cleanup items
- Track progress in code cleanup tracking

---

## Future Enhancements

### Planned Improvements

1. **Automated Collation**: Schedule regular collation runs
2. **Smart Recommendations**: AI-powered organization recommendations
3. **Workflow Pattern Detection**: Automatic workflow pattern detection
4. **Integration Dashboard**: Unified dashboard for all todo systems
5. **Progress Tracking**: Track progress across all systems

---

## Related Documentation

- `MASTER_TODO.md` - Master Todo List
- `DUAL_TODO_REPORT.md` - Dual Todo System Report
- `docs/MASTER_TODO_SYSTEM.md` - Master Todo System Documentation
- `docs/DUAL_TODO_SYSTEM.md` - Dual Todo System Documentation
- `WORKFLOW_STEP_TRACKING_MANDATORY.md` - Workflow Step Tracking

---

**Last Updated**: 2025-12-28  
**Maintained By**: JARVIS, MARVIN, Human Operator  
**Status**: ✅ Active System

