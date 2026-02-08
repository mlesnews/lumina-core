# WOPR Core: Workflow/Worktree Identification & Pattern Mapping

**Date**: 2025-12-28  
**Status**: ✅ **CORE @WOPR FUNCTIONALITY**  
**Principle**: #pattern = @wopr workflows

---

## Overview

**THIS IS CORE @WOPR**

The identification and mapping of workflows/worktrees to #patterns is **core functionality** for WOPR (War Operation Plan Response). This system enables:

1. ✅ **Identification** of new or updating existing workflows/worktrees
2. ✅ **Mapping** workflows to #patterns
3. ✅ **Linking** patterns to WOPR workflows
4. ✅ **Processing** workflow mapping for specific or new workflows

**Principle**: #pattern = @wopr workflows

---

## Core Functionality

### 1. Workflow/Worktree Identification

**Automatic Identification**:
- Scans codebase for `WorkflowBase` subclasses
- Identifies workflow files (`*workflow*.py`)
- Detects Git worktrees
- Classifies workflows (new, existing, pattern, WOPR)

**Workflow Types**:
- `NEW_WORKFLOW` - Newly detected workflow
- `EXISTING_WORKFLOW` - Previously identified workflow
- `WORKTREE` - Git worktree structure
- `PATTERN_WORKFLOW` - Workflow with #pattern tags
- `WOPR_WORKFLOW` - Workflow linked to WOPR

---

### 2. Pattern Mapping

**Automatic Pattern Extraction**:
- Extracts `#pattern` hashtags from workflows
- Identifies workflow patterns (step patterns, method patterns)
- Maps patterns to workflow functionality
- Calculates pattern frequency and confidence

**Pattern Link Types**:
- `DIRECT_MATCH` - Exact pattern match in pattern system
- `SIMILAR_PATTERN` - Similar pattern found
- `WORKFLOW_PATTERN` - Workflow-specific pattern
- `WOPR_STRATAGEM` - WOPR strategic pattern

---

### 3. WOPR Linking

**Automatic WOPR Integration**:
- Links workflows to WOPR workflows
- Creates WOPR workflow entries
- Tracks pattern mappings
- Generates WOPR stratagems for frequent patterns

**Principle**: #pattern = @wopr workflows

**When Linked**:
- Workflow has pattern mappings
- Pattern frequency >= 2 (creates stratagem)
- Pattern confidence >= 0.7

---

### 4. Workflow Processing

**Processing Function**:
- Identifies all workflows/worktrees
- Maps workflows to patterns
- Links to WOPR workflows
- Creates stratagems for frequent patterns
- Generates processing reports

**Processing Modes**:
- **All Workflows**: Process entire codebase
- **Specific Workflow**: Process single workflow by ID

---

## Integration with WorkflowBase

### Automatic Integration

The WOPR Pattern Mapper is **automatically initialized** in `WorkflowBase.__init__()`:

```python
# WOPR Pattern Mapper initialized automatically (CORE @WOPR)
self.wopr_pattern_mapper = WOPRWorkflowPatternMapper(project_root=project_root)
```

### Automatic Registration

Workflows are **automatically registered** with WOPR patterns:

```python
# In workflow execution
class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Work happens here
        
        # Register with WOPR patterns (automatic)
        wopr_result = self.register_with_wopr_patterns()
        
        return result
```

---

## Data Storage

### Workflow Identification
- **Location**: `data/wopr_workflows/identified_workflows.json`
- **Content**: All identified workflows with metadata

### Pattern Mappings
- **Location**: `data/wopr_workflows/pattern_mappings.json`
- **Content**: All workflow-pattern mappings

### WOPR Workflows
- **Location**: `data/wopr_plans/WOPR_WORKFLOWS.json`
- **Content**: WOPR workflow entries linked to patterns

### WOPR Stratagems
- **Location**: `data/wopr_plans/stratagems/{stratagem_id}.json`
- **Content**: Strategic plans for frequent patterns

---

## Usage

### Automatic Processing

**All workflows are automatically processed**:

```python
from wopr_workflow_pattern_mapper import WOPRWorkflowPatternMapper

mapper = WOPRWorkflowPatternMapper()

# Process all workflows
result = mapper.process_workflow_mapping()

# Process specific workflow
result = mapper.process_workflow_mapping(workflow_id="abc123")
```

### In Workflows

**Automatic registration in workflows**:

```python
class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Workflow execution
        result = await self.do_work()
        
        # Register with WOPR (automatic)
        wopr_result = self.register_with_wopr_patterns()
        
        return result
```

---

## Pattern Hashtag Detection

### Supported Hashtags

- `#pattern` - General pattern
- `#pattern_workflow` - Workflow pattern
- `#pattern_wopr` - WOPR pattern
- `#wopr_pattern` - WOPR-specific pattern
- `#workflow_pattern` - Workflow-specific pattern

### Pattern Extraction

Patterns are extracted from:
- Workflow file content
- Class definitions
- Method names
- Step patterns
- Documentation comments

---

## WOPR Stratagem Creation

### When Created

Stratagems are created when:
- Pattern frequency >= 2
- Pattern is mapped to workflow
- Pattern confidence >= 0.7

### What's Created

1. **Strategic Plan** - How to apply pattern
2. **Tactics** - Specific actions
3. **Checkpoints** - Success criteria
4. **Frequency Tracking** - Pattern occurrence tracking

---

## Workflow Loop Integration

### Complete Workflow Loop

```
Workflow Execution
    ↓
Pattern Detection (#pattern tags)
    ↓
Pattern Mapping (workflow → pattern)
    ↓
WOPR Linking (#pattern = @wopr workflows)
    ↓
Stratagem Creation (if frequent)
    ↓
Workflow Feedback (continue/optimize)
    ↓
Next Iteration
```

---

## Benefits

### For WOPR Operations

1. **Complete Workflow Visibility**: All workflows identified and tracked
2. **Pattern Recognition**: Patterns automatically mapped to workflows
3. **Strategic Planning**: Stratagems created for frequent patterns
4. **Operational Intelligence**: Full workflow-pattern intelligence

### For Workflows

1. **Automatic Pattern Recognition**: Patterns detected automatically
2. **WOPR Integration**: Workflows linked to WOPR operations
3. **Strategic Optimization**: Stratagems optimize workflow execution
4. **Pattern Reuse**: Patterns can be reused across workflows

---

## Core @WOPR Principles

### Principle 1: #pattern = @wopr workflows
**All patterns are mapped to WOPR workflows for operational processing.**

### Principle 2: Always Identify
**All workflows/worktrees are identified and tracked.**

### Principle 3: Always Map
**All workflows are mapped to patterns for WOPR processing.**

### Principle 4: Always Link
**All pattern workflows are linked to WOPR for strategic planning.**

---

## Status

✅ **CORE @WOPR FUNCTIONALITY ACTIVE**

- ✅ Workflow identification working
- ✅ Pattern mapping working
- ✅ WOPR linking working
- ✅ Stratagem creation working
- ✅ Integrated with WorkflowBase

---

**Last Updated**: 2025-12-28  
**Status**: ✅ **CORE @WOPR - OPERATIONAL**  
**Next**: Continuous workflow/pattern mapping and WOPR integration

