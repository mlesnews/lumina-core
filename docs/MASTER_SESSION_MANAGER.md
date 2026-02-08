# Master Session Manager - JARVIS Lead Session System

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

---

## Overview

The Master Session Manager is the **penned/pinned master session** that JARVIS uses as the lead session to work with all other agents. It provides:

1. **Master Session Designation** - Penned/pinned master session
2. **Session Consolidation** - Roll all sessions into master
3. **Workflow Pattern Matching** - Identify correct workflow(s) using WOPR
4. **Session Duplication** - Branch into new sessions
5. **Archive System** - Archive completed sessions after verification
6. **BAU Detection** - Automatic Business As Usual detection
7. **Master Feedback Loop** - Apply learned patterns to new workflows

---

## Core Principles

### 1. Master Session = JARVIS Lead Session

- **One master session** that JARVIS uses to coordinate with all agents
- All agent interactions flow through master session
- Master session is **penned/pinned** and persistent

### 2. Workflow Pattern Matching

- Uses **WOPR pattern mapper** to identify correct workflows
- Automatically matches messages to workflow patterns
- Links workflows to #patterns for WOPR processing

### 3. Session Consolidation

- **Roll all sessions into master** after processing
- Consolidates chat history, workflows, and patterns
- Maintains full context across all sessions

### 4. BAU (Business As Usual) Processing

- **Automatic BAU detection** using decision tree and pattern matching
- BAU tasks are processed automatically (verification, archiving, etc.)
- Non-BAU tasks require special handling

### 5. Master Feedback Loop

- **Applies learned patterns** from master session to new workflows
- Enhances workflow processing with historical context
- Continuous improvement through feedback

---

## Architecture

### Components

```
MasterSessionManager
├── Master Session (penned/pinned)
├── Session Consolidation
├── Workflow Pattern Matching (WOPR)
├── BAU Detection
├── Archive System
└── Master Feedback Loop
```

### Data Structure

```
data/master_sessions/
├── MASTER_SESSION.json          # Master session data
├── sessions_index.json           # All sessions index
├── sessions/                      # Individual session files
└── archive/                      # Archived sessions
```

---

## Usage

### 1. Create/Set Master Session

```python
from master_session_manager import MasterSessionManager

manager = MasterSessionManager()
master_id = manager.create_or_set_master_session("JARVIS Master Lead Session")
```

### 2. Add to Master Session

```python
# Automatically:
# - Detects BAU vs non-BAU
# - Matches workflow patterns
# - Processes workflow identification

entry_id = manager.add_to_master_session(
    agent="JARVIS",
    message="Starting workflow processing",
    workflow_id="workflow_123",
    context={"priority": "high"}
)
```

### 3. Consolidate Sessions

```python
# Roll all active sessions into master
result = manager.consolidate_sessions()

# Or consolidate specific sessions
result = manager.consolidate_sessions(session_ids=["session_1", "session_2"])
```

### 4. Duplicate Session for Branching

```python
# Duplicate master session for new work
new_session_id = manager.duplicate_session(
    session_id=None,  # Uses master if None
    new_session_name="New Feature Branch"
)
```

### 5. Archive Completed Session

```python
# Archive after verification (BAU processing)
success = manager.archive_completed_session(
    session_id="session_123",
    verify_success=True  # Automatic verification (BAU)
)
```

### 6. Process Workflows from Master

```python
# Process workflows identified in master session
result = manager.process_workflows_from_master()
```

### 7. Apply Master Feedback Loop

```python
# Apply learned patterns to new workflows
result = manager.apply_master_feedback_loop()
```

---

## Integration with WorkflowBase

The Master Session Manager is **automatically integrated** into `WorkflowBase`:

```python
class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Master session is automatically initialized
        # All chat history is added to master session
        
        # Add chat entry (automatically goes to master)
        self.add_chat_history("JARVIS", "Starting workflow")
        
        # Process with master session
        result = self.process_with_master_session()
        
        return result
```

---

## BAU Detection

### BAU Indicators

- Keywords: `verify`, `check`, `validate`, `confirm`, `archive`, `complete`
- Standard, routine, normal, usual, regular, typical
- Automated, automatic, BAU, business as usual

### Non-BAU Indicators

- Keywords: `new`, `create`, `build`, `implement`, `develop`, `design`
- Critical, urgent, emergency, unusual, special
- First time, never done, experimental

### Decision Tree Integration

If available, uses `universal_decision_tree` for BAU detection:

```python
from universal_decision_tree import decide, DecisionContext

context = DecisionContext(
    action="detect_bau",
    inputs={"message": message, "context": context},
    metadata={"has_bau_keywords": True}
)

result = decide('bau_detection', context)
```

---

## Workflow Pattern Matching

### Pattern Matching Process

1. **Process WOPR mapping** - Get all identified workflows
2. **Search for matches** - Check message against workflow names and patterns
3. **Calculate confidence** - Exact (0.9), Similar (0.6), Pattern (0.8)
4. **Return best match** - If confidence >= 0.6

### Match Types

- **Exact**: Workflow name found in message
- **Similar**: Key words from workflow name found
- **Pattern**: Pattern hashtags found in message

---

## Session Lifecycle

```
1. Create Master Session (penned/pinned)
   ↓
2. Add Entries (auto BAU detection, workflow matching)
   ↓
3. Process Workflows (WOPR pattern matching)
   ↓
4. Consolidate Sessions (roll into master)
   ↓
5. Duplicate for Branching (new work)
   ↓
6. Archive Completed (after verification - BAU)
```

---

## Master Feedback Loop

### Process

1. **Extract Learned Patterns** - From master session chat history
2. **Identify Workflow Patterns** - From workflows and patterns matched
3. **Apply to New Workflows** - Enhance workflow processing
4. **Continuous Improvement** - Learn from all interactions

### Pattern Sources

- Chat history entries with pattern matches
- Workflows with pattern hashtags
- WOPR pattern mappings
- Historical workflow processing

---

## Archive System

### Verification (BAU)

Automatic verification checks:
- Success indicators present
- No critical errors
- Workflows completed
- Patterns processed

### Archive Process

1. **Verify Success** - Automatic (BAU)
2. **Mark as Archived** - Update status
3. **Move to Archive** - Save to archive directory
4. **Update Index** - Remove from active sessions

---

## API Reference

### MasterSessionManager

#### Methods

- `create_or_set_master_session(session_name: str) -> str`
- `add_to_master_session(agent: str, message: str, workflow_id: Optional[str], context: Optional[Dict]) -> str`
- `consolidate_sessions(session_ids: Optional[List[str]]) -> Dict[str, Any]`
- `duplicate_session(session_id: Optional[str], new_session_name: str) -> str`
- `archive_completed_session(session_id: str, verify_success: bool) -> bool`
- `process_workflows_from_master() -> Dict[str, Any]`
- `apply_master_feedback_loop() -> Dict[str, Any]`
- `get_master_session_summary() -> Dict[str, Any]`

### WorkflowBase Integration

#### Methods

- `process_with_master_session() -> Dict[str, Any]`
  - Process workflow with master session
  - Uses workflow pattern matching
  - Applies master feedback loop

---

## Examples

### Example 1: Basic Usage

```python
from master_session_manager import MasterSessionManager

manager = MasterSessionManager()

# Create master session
master_id = manager.create_or_set_master_session()

# Add entries
manager.add_to_master_session("JARVIS", "Starting task")
manager.add_to_master_session("MARVIN", "Reviewing patterns")

# Process workflows
result = manager.process_workflows_from_master()

# Get summary
summary = manager.get_master_session_summary()
print(f"Chat Entries: {summary['chat_entries']}")
print(f"Workflows: {summary['workflows_identified']}")
```

### Example 2: Session Consolidation

```python
# Consolidate all active sessions into master
result = manager.consolidate_sessions()

print(f"Consolidated {result['consolidated_sessions']} sessions")
print(f"Entries consolidated: {result['entries_consolidated']}")
```

### Example 3: Workflow Integration

```python
class MyWorkflow(WorkflowBase):
    async def execute(self):
        # Master session automatically initialized
        
        # Add to master session
        self.add_chat_history("JARVIS", "Executing workflow")
        
        # Process with master session
        result = self.process_with_master_session()
        
        return result
```

---

## Best Practices

1. **Always use master session** - All agent interactions should go through master
2. **Consolidate regularly** - Roll sessions into master after processing
3. **Archive completed** - Archive after verification (BAU)
4. **Use feedback loop** - Apply learned patterns to new workflows
5. **BAU detection** - Let system detect BAU automatically
6. **Workflow matching** - Use pattern matching to identify correct workflows

---

## Troubleshooting

### Master Session Not Found

```python
# Create master session if it doesn't exist
if not manager.master_session:
    manager.create_or_set_master_session()
```

### Workflow Pattern Matching Not Working

```python
# Check WOPR mapper availability
if not manager.wopr_mapper:
    print("WOPR mapper not available")
```

### BAU Detection Issues

```python
# Check decision tree availability
from universal_decision_tree import decide
if decide:
    print("Decision tree available")
```

---

## Future Enhancements

1. **Real-time session sync** - Sync sessions across agents
2. **Advanced pattern matching** - ML-based workflow matching
3. **Session analytics** - Analyze session patterns and trends
4. **Multi-master support** - Support for multiple master sessions
5. **Session templates** - Pre-configured session templates

---

## Related Documentation

- [WOPR Core Workflow Pattern Mapping](./WOPR_CORE_WORKFLOW_PATTERN_MAPPING.md)
- [Workflow Auto Review & Fix](./WORKFLOW_AUTO_REVIEW_FIX.md)
- [Workflow Base Class](./WORKFLOW_BASE.md)
- [Master Feedback Loop System](./MASTER_FEEDBACK_LOOP.md)

---

**Status**: ✅ **OPERATIONAL**  
**Last Updated**: 2025-01-24

