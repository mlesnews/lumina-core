# Workflow Scope & Mode Selection Gap Analysis

**Date**: 2025-01-24  
**Status**: 🔴 **CRITICAL GAP** - No Comprehensive Understanding  
**Issue**: We don't know when to work in what scope/mode

---

## Overview

We lack comprehensive understanding of **when to work in what scope**:

1. **Scope Types**:
   - **Local** - Local machine operations
   - **Worktree** - Git worktree operations
   - **Cloud** - Cloud-based operations
   - **Non-workspace** - Single file(s) operations
   - **Workspace** - Full workspace operations

2. **Mode Types**:
   - **@flow** - Flow mode (workflow orchestration)
   - **@auto[#automatic]** - Automatic mode (auto-execute)
   - **@auto[#autonomous]** - Autonomous mode (self-directed)
   - **@auto[#automation]** - Automation mode (automated workflows)

**Current State**: ❌ **NO COMPREHENSIVE SYSTEM** - Only partial implementations exist

---

## What Exists ✅

### 1. Workspace vs Non-Workspace Mode
- `scripts/python/cursor_workspace_mode_manager.py` - Basic workspace/non-workspace detection
- `scripts/python/jarvis_unified_interface.py` - Unified interface for both modes
- Can detect workspace vs non-workspace
- Can sync settings between modes

### 2. Basic Mode Detection
- Can detect if workspace is open
- Can detect if single file(s) are open
- Can switch between modes

### 3. Worktree References
- References to worktrees in various scripts
- No comprehensive worktree management system

---

## What's Missing ❌

### 1. Scope Selection Decision Tree
**Missing**: Intelligent decision-making for:
- **When to use local scope**
- **When to use worktree scope**
- **When to use cloud scope**
- **When to use workspace vs non-workspace**

**Current**: No decision tree, just basic detection

### 2. @flow Mode System
**Missing**:
- What @flow mode is
- When to use @flow mode
- How @flow mode differs from other modes
- @flow mode workflow orchestration

**Current**: No @flow mode implementation

### 3. @auto Mode Variants
**Missing**: Understanding of:
- **@auto[#automatic]** - When to auto-execute
- **@auto[#autonomous]** - When to be self-directed
- **@auto[#automation]** - When to automate workflows
- Differences between variants
- When to use each variant

**Current**: No @auto mode variant system

### 4. Scope + Mode Combination Logic
**Missing**:
- How scopes and modes combine
- When to use specific combinations
- Priority hierarchy
- Fallback logic

**Current**: No combination logic

### 5. Context-Aware Selection
**Missing**:
- Context analysis for scope/mode selection
- Task-based selection
- User intent detection
- Resource availability checking

**Current**: No context-aware selection

---

## Required Scope & Mode System

### Architecture

```
User Request
    ↓
Context Analyzer
    ├─ Analyze task type
    ├─ Analyze file structure
    ├─ Analyze git status
    ├─ Analyze resource availability
    └─ Analyze user intent
    ↓
Scope Selector
    ├─ Local Scope
    │  ├─ Local file operations
    │  ├─ Local git operations
    │  └─ Local execution
    ├─ Worktree Scope
    │  ├─ Worktree operations
    │  ├─ Worktree git operations
    │  └─ Worktree execution
    ├─ Cloud Scope
    │  ├─ Cloud storage operations
    │  ├─ Cloud git operations
    │  └─ Cloud execution
    ├─ Workspace Scope
    │  ├─ Full workspace operations
    │  ├─ Multi-file operations
    │  └─ Project-level operations
    └─ Non-Workspace Scope
       ├─ Single file operations
       ├─ File-level operations
       └─ Quick operations
    ↓
Mode Selector
    ├─ @flow Mode
    │  ├─ Workflow orchestration
    │  ├─ Multi-step processes
    │  └─ Complex workflows
    ├─ @auto[#automatic]
    │  ├─ Auto-execute simple tasks
    │  ├─ Auto-apply fixes
    │  └─ Auto-complete operations
    ├─ @auto[#autonomous]
    │  ├─ Self-directed execution
    │  ├─ Independent decision-making
    │  └─ Self-optimization
    └─ @auto[#automation]
       ├─ Automated workflows
       ├─ Scheduled operations
       └─ Background processes
    ↓
Execution
    ├─ Scope + Mode combination
    ├─ Resource allocation
    └─ Result handling
```

### Decision Tree Logic

#### 1. Scope Selection

```python
class ScopeSelector:
    """Select optimal scope for operation"""
    
    def select(self, context: OperationContext) -> Scope:
        """Select scope based on context"""
        
        # Check if workspace is open
        if context.has_workspace:
            # Check if operation requires workspace
            if context.requires_workspace:
                return Scope.WORKSPACE
            else:
                # Can use non-workspace for simple operations
                if context.is_simple_operation:
                    return Scope.NON_WORKSPACE
                else:
                    return Scope.WORKSPACE
        
        # Check if worktree is available
        if context.has_worktree and context.requires_git:
            return Scope.WORKTREE
        
        # Check if cloud is needed
        if context.requires_cloud or context.requires_collaboration:
            return Scope.CLOUD
        
        # Default to local
        return Scope.LOCAL
```

#### 2. Mode Selection

```python
class ModeSelector:
    """Select optimal mode for operation"""
    
    def select(self, context: OperationContext, scope: Scope) -> Mode:
        """Select mode based on context and scope"""
        
        # Check for explicit mode request
        if context.requested_mode:
            return context.requested_mode
        
        # @flow mode for complex workflows
        if context.is_complex_workflow or context.has_multiple_steps:
            return Mode.FLOW
        
        # @auto[#automatic] for simple auto-execute tasks
        if context.is_simple_task and context.can_auto_execute:
            return Mode.AUTO_AUTOMATIC
        
        # @auto[#autonomous] for self-directed tasks
        if context.requires_independence and context.has_clear_objectives:
            return Mode.AUTO_AUTONOMOUS
        
        # @auto[#automation] for automated workflows
        if context.is_recurring or context.is_scheduled:
            return Mode.AUTO_AUTOMATION
        
        # Default: Manual mode
        return Mode.MANUAL
```

### Scope Selection Rules

#### Local Scope
**When to Use**:
- ✅ Single file operations
- ✅ Quick edits
- ✅ Local testing
- ✅ No git operations needed
- ✅ No collaboration needed
- ✅ Privacy-sensitive operations

**When NOT to Use**:
- ❌ Multi-file operations
- ❌ Git operations (use worktree)
- ❌ Collaboration needed (use cloud)
- ❌ Workspace-level operations

#### Worktree Scope
**When to Use**:
- ✅ Git operations needed
- ✅ Branch management
- ✅ Multiple worktrees
- ✅ Isolated git environments
- ✅ Testing different branches

**When NOT to Use**:
- ❌ No git operations needed
- ❌ Single file operations (use local)
- ❌ Cloud collaboration (use cloud)

#### Cloud Scope
**When to Use**:
- ✅ Collaboration needed
- ✅ Cloud storage operations
- ✅ Remote git operations
- ✅ Cross-machine operations
- ✅ Backup/sync operations

**When NOT to Use**:
- ❌ Privacy-sensitive operations
- ❌ Offline operations
- ❌ Local-only operations

#### Workspace Scope
**When to Use**:
- ✅ Multi-file operations
- ✅ Project-level operations
- ✅ Full workspace context needed
- ✅ Complex refactoring
- ✅ Cross-file dependencies

**When NOT to Use**:
- ❌ Single file operations (use non-workspace)
- ❌ Quick edits (use non-workspace)
- ❌ Simple operations

#### Non-Workspace Scope
**When to Use**:
- ✅ Single file operations
- ✅ Quick edits
- ✅ File-level operations
- ✅ Simple operations
- ✅ No workspace context needed

**When NOT to Use**:
- ❌ Multi-file operations (use workspace)
- ❌ Project-level operations (use workspace)
- ❌ Complex operations

### Mode Selection Rules

#### @flow Mode
**When to Use**:
- ✅ Complex workflows
- ✅ Multi-step processes
- ✅ Workflow orchestration
- ✅ Sequential operations
- ✅ Dependent steps

**Characteristics**:
- Workflow-aware
- Step-by-step execution
- State management
- Progress tracking

#### @auto[#automatic]
**When to Use**:
- ✅ Simple auto-execute tasks
- ✅ Auto-apply fixes
- ✅ Auto-complete operations
- ✅ Quick operations
- ✅ Low-risk operations

**Characteristics**:
- Auto-execution
- No user confirmation needed
- Fast execution
- Simple operations

#### @auto[#autonomous]
**When to Use**:
- ✅ Self-directed tasks
- ✅ Independent decision-making
- ✅ Self-optimization
- ✅ Adaptive operations
- ✅ Learning tasks

**Characteristics**:
- Self-directed
- Independent
- Adaptive
- Learning

#### @auto[#automation]
**When to Use**:
- ✅ Automated workflows
- ✅ Scheduled operations
- ✅ Background processes
- ✅ Recurring tasks
- ✅ Batch operations

**Characteristics**:
- Automated
- Scheduled
- Background
- Recurring

### Scope + Mode Combinations

#### Valid Combinations

1. **Local + @flow**
   - Local workflow orchestration
   - Multi-step local operations

2. **Local + @auto[#automatic]**
   - Quick local auto-execute
   - Simple local operations

3. **Local + @auto[#autonomous]**
   - Self-directed local operations
   - Independent local tasks

4. **Worktree + @flow**
   - Git workflow orchestration
   - Multi-step git operations

5. **Worktree + @auto[#automatic]**
   - Quick git auto-execute
   - Simple git operations

6. **Cloud + @flow**
   - Cloud workflow orchestration
   - Multi-step cloud operations

7. **Workspace + @flow**
   - Workspace workflow orchestration
   - Multi-step workspace operations

8. **Non-Workspace + @auto[#automatic]**
   - Quick file auto-execute
   - Simple file operations

#### Invalid Combinations

1. **Cloud + @auto[#autonomous]** (privacy risk)
2. **Non-Workspace + @flow** (too complex for non-workspace)
3. **Local + @auto[#automation]** (should use workspace for automation)

---

## Implementation Plan

### Phase 1: Context Analyzer (4-5 days)
- [ ] Create `scripts/python/workflow_scope_context_analyzer.py`
- [ ] Implement task type analysis
- [ ] Implement file structure analysis
- [ ] Implement git status analysis
- [ ] Implement resource availability checking
- [ ] Implement user intent detection

### Phase 2: Scope Selector (3-4 days)
- [ ] Create `scripts/python/workflow_scope_selector.py`
- [ ] Implement scope selection logic
- [ ] Add scope validation
- [ ] Add scope fallback logic
- [ ] Test scope selection

### Phase 3: Mode Selector (4-5 days)
- [ ] Create `scripts/python/workflow_mode_selector.py`
- [ ] Implement @flow mode
- [ ] Implement @auto[#automatic]
- [ ] Implement @auto[#autonomous]
- [ ] Implement @auto[#automation]
- [ ] Test mode selection

### Phase 4: Integration (3-4 days)
- [ ] Integrate scope + mode selection
- [ ] Add combination validation
- [ ] Add execution routing
- [ ] Test end-to-end flow

### Phase 5: Documentation (2-3 days)
- [ ] Document scope selection rules
- [ ] Document mode selection rules
- [ ] Document combinations
- [ ] Create decision tree diagrams

**Total Estimated Time**: 16-21 days

---

## Detailed Components

### 1. Context Analyzer

```python
class WorkflowScopeContextAnalyzer:
    """Analyze context for scope/mode selection"""
    
    def analyze(self, request: str, current_state: Dict) -> OperationContext:
        """Analyze operation context"""
        
        return OperationContext(
            task_type=self._classify_task_type(request),
            file_structure=self._analyze_file_structure(),
            git_status=self._analyze_git_status(),
            resource_availability=self._check_resources(),
            user_intent=self._detect_intent(request),
            has_workspace=self._check_workspace(),
            has_worktree=self._check_worktree(),
            requires_workspace=self._requires_workspace(request),
            requires_git=self._requires_git(request),
            requires_cloud=self._requires_cloud(request),
            is_complex_workflow=self._is_complex_workflow(request),
            is_simple_task=self._is_simple_task(request),
            can_auto_execute=self._can_auto_execute(request),
            requires_independence=self._requires_independence(request),
            is_recurring=self._is_recurring(request)
        )
```

### 2. Scope Selector

```python
class WorkflowScopeSelector:
    """Select optimal scope"""
    
    def select(self, context: OperationContext) -> Scope:
        """Select scope based on context"""
        
        # Priority order
        if context.has_workspace and context.requires_workspace:
            return Scope.WORKSPACE
        
        if context.has_worktree and context.requires_git:
            return Scope.WORKTREE
        
        if context.requires_cloud:
            return Scope.CLOUD
        
        if context.has_workspace and not context.is_simple_operation:
            return Scope.WORKSPACE
        
        if not context.has_workspace or context.is_simple_operation:
            return Scope.NON_WORKSPACE
        
        return Scope.LOCAL
```

### 3. Mode Selector

```python
class WorkflowModeSelector:
    """Select optimal mode"""
    
    def select(self, context: OperationContext, scope: Scope) -> Mode:
        """Select mode based on context and scope"""
        
        # @flow for complex workflows
        if context.is_complex_workflow:
            return Mode.FLOW
        
        # @auto[#automatic] for simple auto-execute
        if context.is_simple_task and context.can_auto_execute:
            return Mode.AUTO_AUTOMATIC
        
        # @auto[#autonomous] for self-directed
        if context.requires_independence:
            return Mode.AUTO_AUTONOMOUS
        
        # @auto[#automation] for automated
        if context.is_recurring:
            return Mode.AUTO_AUTOMATION
        
        return Mode.MANUAL
```

---

## Configuration

### Scope & Mode Configuration

```json
{
  "workflow_scope_mode": {
    "enabled": true,
    "auto_detect": true,
    "scope_selection": {
      "priority": [
        "workspace",
        "worktree",
        "cloud",
        "non_workspace",
        "local"
      ],
      "rules": {
        "workspace": {
          "when": [
            "multi_file_operations",
            "project_level_operations",
            "full_workspace_context_needed",
            "complex_refactoring",
            "cross_file_dependencies"
          ],
          "when_not": [
            "single_file_operations",
            "quick_edits",
            "simple_operations"
          ]
        },
        "non_workspace": {
          "when": [
            "single_file_operations",
            "quick_edits",
            "file_level_operations",
            "simple_operations"
          ],
          "when_not": [
            "multi_file_operations",
            "project_level_operations",
            "complex_operations"
          ]
        },
        "worktree": {
          "when": [
            "git_operations_needed",
            "branch_management",
            "multiple_worktrees",
            "isolated_git_environments"
          ],
          "when_not": [
            "no_git_operations",
            "single_file_operations",
            "cloud_collaboration"
          ]
        },
        "cloud": {
          "when": [
            "collaboration_needed",
            "cloud_storage_operations",
            "remote_git_operations",
            "cross_machine_operations"
          ],
          "when_not": [
            "privacy_sensitive_operations",
            "offline_operations",
            "local_only_operations"
          ]
        },
        "local": {
          "when": [
            "single_file_operations",
            "quick_edits",
            "local_testing",
            "privacy_sensitive_operations"
          ],
          "when_not": [
            "multi_file_operations",
            "git_operations",
            "collaboration_needed"
          ]
        }
      }
    },
    "mode_selection": {
      "flow": {
        "when": [
          "complex_workflows",
          "multi_step_processes",
          "workflow_orchestration",
          "sequential_operations"
        ],
        "characteristics": [
          "workflow_aware",
          "step_by_step_execution",
          "state_management",
          "progress_tracking"
        ]
      },
      "auto_automatic": {
        "when": [
          "simple_auto_execute_tasks",
          "auto_apply_fixes",
          "auto_complete_operations",
          "quick_operations",
          "low_risk_operations"
        ],
        "characteristics": [
          "auto_execution",
          "no_user_confirmation",
          "fast_execution",
          "simple_operations"
        ]
      },
      "auto_autonomous": {
        "when": [
          "self_directed_tasks",
          "independent_decision_making",
          "self_optimization",
          "adaptive_operations"
        ],
        "characteristics": [
          "self_directed",
          "independent",
          "adaptive",
          "learning"
        ]
      },
      "auto_automation": {
        "when": [
          "automated_workflows",
          "scheduled_operations",
          "background_processes",
          "recurring_tasks"
        ],
        "characteristics": [
          "automated",
          "scheduled",
          "background",
          "recurring"
        ]
      }
    },
    "combinations": {
      "valid": [
        "local + flow",
        "local + auto_automatic",
        "local + auto_autonomous",
        "worktree + flow",
        "worktree + auto_automatic",
        "cloud + flow",
        "workspace + flow",
        "non_workspace + auto_automatic"
      ],
      "invalid": [
        "cloud + auto_autonomous",
        "non_workspace + flow",
        "local + auto_automation"
      ]
    }
  }
}
```

---

## Success Metrics

### Scope Selection
- ✅ Correct scope selected 95%+ of the time
- ✅ Scope validation passes 100% of the time
- ✅ Fallback works 100% of the time

### Mode Selection
- ✅ Correct mode selected 90%+ of the time
- ✅ Mode matches task requirements 95%+ of the time
- ✅ Mode execution succeeds 90%+ of the time

### Combination Logic
- ✅ Valid combinations used 100% of the time
- ✅ Invalid combinations rejected 100% of the time
- ✅ Combination execution succeeds 90%+ of the time

### Performance
- ✅ Context analysis time < 50ms
- ✅ Scope selection time < 20ms
- ✅ Mode selection time < 20ms
- ✅ Total selection time < 100ms

---

## Related Files

- `scripts/python/cursor_workspace_mode_manager.py` - Existing workspace mode manager
- `scripts/python/jarvis_unified_interface.py` - Unified interface
- `docs/system/AUTO_MODE_COMPREHENSIVE_GAP.md` - @auto mode gap analysis
- `docs/system/KNOWN_ISSUES.md` - Known issues tracking

---

## Next Steps

1. **Create Context Analyzer** - Analyze operation context
2. **Create Scope Selector** - Implement scope selection logic
3. **Create Mode Selector** - Implement mode selection logic
4. **Integrate Components** - Connect everything together
5. **Test and Document** - Ensure robust operation

---

**Status**: ❌ **NOT IMPLEMENTED** - Critical gap requiring comprehensive solution

**Last Updated**: 2025-01-24

