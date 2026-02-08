# Workflow Auto Review & Fix Component

**Date**: 2025-12-28  
**Status**: ✅ **INTEGRATED INTO WORKFLOW_BASE**  
**Purpose**: Automatic review and fix cycle that maintains chat histories and feeds back into workflow loop

---

## Overview

The Auto Review & Fix component automatically:
1. ✅ **Maintains agent chat histories** - All chat interactions preserved
2. ✅ **Accepts all changes after running** - Automatic acceptance
3. ✅ **Reviews changes** - Analyzes for issues, errors, improvements
4. ✅ **Fixes all issues** - Automatically fixes where possible
5. ✅ **Feeds back into workflow loop** - Results feed back for next iteration

---

## Integration with WorkflowBase

### Automatic Integration

The component is **automatically initialized** in `WorkflowBase.__init__()`:

```python
# Auto Review & Fix component initialized automatically
self.auto_review_fix = WorkflowAutoReviewFix(
    project_root=project_root,
    workflow_id=self.execution_id
)
```

### Automatic Execution

After workflow execution, call `auto_review_and_fix()`:

```python
# After workflow execution
review_result = workflow.auto_review_and_fix()
```

---

## Workflow Steps

### Step 1: Maintain Chat Histories

**Automatic**: All chat interactions are tracked

```python
# Add chat history (automatic in workflows)
workflow.add_chat_history("JARVIS", "Starting workflow execution")
workflow.add_chat_history("MARVIN", "Reviewing workflow steps")
```

**Storage**: `data/agent_chat_history/{workflow_id}_chat_history.jsonl`

---

### Step 2: Track Changes

**Automatic**: File changes are tracked during workflow execution

```python
# Track changes (automatic in workflows)
workflow.track_change("file.py", "created", diff="+ def function(): pass")
workflow.track_change("workflow.py", "modified", diff="- old\n+ new")
```

**Storage**: `data/workflow_reviews/{workflow_id}_changes.json`

---

### Step 3: Auto-Accept All Changes

**Automatic**: After workflow runs, all changes are automatically accepted

```python
# Automatic acceptance
accept_result = workflow.auto_review_fix.auto_accept_all_changes()
# Result: {"accepted_count": 5, "total_changes": 5}
```

**What it does**:
- Marks all pending changes as ACCEPTED
- Prepares for review

---

### Step 4: Review Changes

**Automatic**: All accepted changes are reviewed for issues

```python
# Automatic review
review_result = workflow.auto_review_fix.review_changes()
```

**Review Checks**:
- ✅ File path validation
- ✅ Change type validation
- ✅ Syntax error detection
- ✅ TODO/FIXME detection
- ✅ Secret detection

**Result**: Changes marked as NEEDS_FIX or COMPLETE

---

### Step 5: Fix All Issues

**Automatic**: Issues are automatically fixed where possible

```python
# Automatic fixes
fix_result = workflow.auto_review_fix.fix_all_issues()
```

**Fixes Applied**:
- Basic syntax fixes
- Indentation corrections
- Secret flagging (manual review required)

**Result**: Changes marked as FIXED or NEEDS_MANUAL_REVIEW

---

### Step 6: Feed Back to Workflow

**Automatic**: Results feed back into workflow loop

```python
# Feedback to workflow
feedback = workflow.auto_review_fix.feed_back_to_workflow()
```

**Feedback Includes**:
- Changes summary
- Review results
- Fix results
- Next steps
- Workflow continuation decision

**Result**: Workflow can continue or needs manual intervention

---

## Full Cycle Execution

### Single Method Call

Execute the entire cycle with one call:

```python
# Execute full cycle
cycle_result = workflow.auto_review_and_fix()
```

**What it does**:
1. Auto-accepts all changes
2. Reviews all changes
3. Fixes all issues
4. Feeds back to workflow

**Returns**: Complete cycle result with all data

---

## Workflow Loop Integration

### Automatic Workflow Loop

The component integrates seamlessly with workflow execution:

```python
class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Step 1: Do work
        result = await self.do_work()
        
        # Step 2: Track changes
        self.track_change("output.py", "created", diff=result)
        
        # Step 3: Add chat history
        self.add_chat_history("JARVIS", "Work completed")
        
        # Step 4: Auto review and fix (automatic)
        review_result = self.auto_review_and_fix()
        
        # Step 5: Check if workflow should continue
        if review_result["workflow_feedback"]["workflow_should_continue"]:
            # Continue workflow
            pass
        else:
            # Needs manual review
            pass
        
        return result
```

---

## Data Storage

### Chat History
- **Location**: `data/agent_chat_history/{workflow_id}_chat_history.jsonl`
- **Format**: JSONL (one entry per line)
- **Content**: All agent interactions

### Changes
- **Location**: `data/workflow_reviews/{workflow_id}_changes.json`
- **Format**: JSON
- **Content**: All file changes with review status

### Review Results
- **Location**: `data/workflow_reviews/{workflow_id}_review.json`
- **Format**: JSON
- **Content**: Review results and workflow feedback

---

## Review Status Flow

```
PENDING → ACCEPTED → REVIEWING → NEEDS_FIX → FIXING → FIXED → COMPLETE
                                    ↓
                            (Manual Review)
```

---

## Usage Examples

### Basic Usage

```python
from workflow_base import WorkflowBase

class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Work happens here
        self.track_change("file.py", "created")
        self.add_chat_history("JARVIS", "File created")
        
        # Auto review and fix
        result = self.auto_review_and_fix()
        
        return result
```

### Advanced Usage

```python
# Manual control
workflow.auto_review_fix.auto_accept_all_changes()
review = workflow.auto_review_fix.review_changes()
fixes = workflow.auto_review_fix.fix_all_issues()
feedback = workflow.auto_review_fix.feed_back_to_workflow()
```

---

## Benefits

### For Workflows

1. **Automatic Quality Control**: Changes reviewed automatically
2. **Issue Detection**: Problems found before deployment
3. **Automatic Fixes**: Common issues fixed automatically
4. **Workflow Continuity**: Feedback enables workflow loops

### For Chat Histories

1. **Complete Record**: All interactions preserved
2. **Context Maintenance**: Full context for workflow decisions
3. **Audit Trail**: Complete history for debugging

### For Automation

1. **Reduced Manual Review**: Automatic acceptance and review
2. **Faster Iteration**: Automatic fixes speed up workflow
3. **Workflow Loops**: Feedback enables continuous improvement

---

## Configuration

### Enable/Disable

The component is automatically enabled if available. To disable:

```python
# In WorkflowBase.__init__
self.auto_review_fix = None  # Disable
```

### Custom Review Logic

Override `_review_change()` method to add custom review logic:

```python
class CustomReviewFix(WorkflowAutoReviewFix):
    def _review_change(self, change):
        issues = super()._review_change(change)
        # Add custom review logic
        if "custom_check" in change.diff:
            issues.append("Custom issue detected")
        return issues
```

---

## Integration Checklist

- ✅ Integrated into `WorkflowBase`
- ✅ Automatic initialization
- ✅ Chat history maintenance
- ✅ Change tracking
- ✅ Auto-acceptance
- ✅ Automatic review
- ✅ Automatic fixes
- ✅ Workflow feedback
- ✅ Full cycle execution

---

**Last Updated**: 2025-12-28  
**Status**: ✅ **FULLY INTEGRATED**  
**Next**: Test with actual workflows

