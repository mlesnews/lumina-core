# @ASKChain SYPHON Troubleshooting Integration - Recommendations

## Overview

Integration recommendations for enhancing the @askchain system with SYPHON-enhanced troubleshooting capabilities.

## Current State

### @ASKChain System
- **File**: `scripts/python/jarvis_execute_ask_chains.py`
- **Features**:
  - Discovers and creates chains from @asks
  - Executes tasks in dependency order
  - Basic error handling (try/except)
  - Task status tracking (pending, running, completed, failed)
  - Operator idleness restriction integration

### Current Error Handling
- Basic exception catching
- Task marking as failed
- Error message logging
- No proactive troubleshooting
- No pattern recognition
- No simulation before execution
- No intelligence extraction

## Recommended Enhancements

### 1. Pre-Execution Troubleshooting

**Location**: `_execute_task()` method in `jarvis_execute_ask_chains.py`

**Enhancement**: Add SYPHON-enhanced troubleshooting before task execution

```python
def _execute_task(self, task) -> Dict[str, Any]:
    """Execute a single chained task with SYPHON troubleshooting"""
    
    # Pre-execution troubleshooting
    if self.syphon_troubleshooter:
        error_data = {
            "error_id": f"pre_check_{task.task_id}",
            "error_type": "pre_execution_check",
            "message": f"Pre-execution check for task: {task.task_id}",
            "task_id": task.task_id,
            "ask_text": task.ask_text,
            "dependencies": task.dependencies
        }
        
        troubleshooting_result = self.syphon_troubleshooter.troubleshoot_with_syphon(
            error_data,
            mode="pre",
            level="standard"
        )
        
        # Check if we should proceed
        if not troubleshooting_result.simulation_success_rate > 0.75:
            logger.warning(f"⚠️  Low confidence for task {task.task_id}, skipping")
            return {"success": False, "reason": "low_confidence", "troubleshooting": troubleshooting_result.to_dict()}
```

### 2. Pattern Recognition for Common Failures

**Enhancement**: Detect common @askchain failure patterns

**Patterns to Detect**:
- Dependency failures
- Timeout issues
- Resource constraints
- Operator idleness
- Workflow execution errors
- JARVIS verification failures

**Implementation**:
```python
def _detect_askchain_patterns(self, error: Exception, task) -> List[Dict[str, Any]]:
    """Detect patterns in askchain failures"""
    error_msg = str(error).lower()
    patterns = []
    
    # Dependency pattern
    if "dependency" in error_msg or "not found" in error_msg:
        patterns.append({
            "pattern_id": "dependency_failure",
            "intent": "Resolve dependency before execution",
            "building_blocks": ["check_dependencies", "wait_for_dependency", "retry"]
        })
    
    # Timeout pattern
    if "timeout" in error_msg or "timed out" in error_msg:
        patterns.append({
            "pattern_id": "timeout",
            "intent": "Increase timeout or optimize task",
            "building_blocks": ["increase_timeout", "optimize_task", "retry"]
        })
    
    return patterns
```

### 3. Simulation Before Execution

**Enhancement**: Simulate task execution before actual execution

**Benefits**:
- Predict failures before they happen
- Calculate success rates
- Only execute high-confidence tasks
- Learn from simulations

**Implementation**:
```python
def _simulate_task_execution(self, task) -> Dict[str, Any]:
    """Simulate task execution"""
    simulation = {
        "task_id": task.task_id,
        "simulated": True,
        "success_rate": 0.0,
        "potential_issues": [],
        "recommendations": []
    }
    
    # Check dependencies
    missing_deps = self._check_dependencies(task)
    if missing_deps:
        simulation["potential_issues"].append(f"Missing dependencies: {missing_deps}")
        simulation["success_rate"] -= 0.3
    
    # Check operator status
    if self.idleness_restriction and not self.idleness_restriction.is_action_allowed("ask_chain_execution"):
        simulation["potential_issues"].append("Operator idle - execution will be blocked")
        simulation["success_rate"] = 0.0
    
    # Check resource availability
    # ... resource checks ...
    
    return simulation
```

### 4. Intelligence Extraction from Failures

**Enhancement**: Extract intelligence from failed tasks using SYPHON

**Implementation**:
```python
def _extract_failure_intelligence(self, task, error: Exception) -> Dict[str, Any]:
    """Extract intelligence from task failure"""
    if not self.troubleshooting_extractor:
        return {}
    
    error_data = {
        "error_id": f"failure_{task.task_id}",
        "error_type": "task_execution_failure",
        "message": str(error),
        "task_id": task.task_id,
        "ask_text": task.ask_text,
        "task_status": task.status.value if hasattr(task.status, 'value') else str(task.status),
        "error_message": task.error_message if hasattr(task, 'error_message') else None
    }
    
    syphon_result = self.troubleshooting_extractor.extract(
        content=error_data,
        metadata={
            "chain_id": task.chain_id if hasattr(task, 'chain_id') else None,
            "task_id": task.task_id,
            "source": "askchain_execution"
        }
    )
    
    if syphon_result.success and syphon_result.data:
        return {
            "actionable_items": syphon_result.data.actionable_items,
            "tasks": syphon_result.data.tasks,
            "decisions": syphon_result.data.decisions,
            "intelligence": syphon_result.data.intelligence,
            "proven_patterns": [
                p for p in syphon_result.data.intelligence 
                if p.get("type") == "proven_pattern"
            ]
        }
    
    return {}
```

### 5. Automatic Retry with Pattern-Based Fixes

**Enhancement**: Automatically retry failed tasks using proven patterns

**Implementation**:
```python
def _retry_task_with_fix(self, task, error: Exception, intelligence: Dict[str, Any]) -> Dict[str, Any]:
    """Retry task with pattern-based fixes"""
    proven_patterns = intelligence.get("proven_patterns", [])
    
    # Apply proven fixes
    for pattern in proven_patterns:
        if pattern.get("success_rate", 0) > 0.75:
            fix_strategy = pattern.get("fix_strategy")
            
            if fix_strategy == "retry_with_delay":
                time.sleep(5)  # Delay before retry
                return self._execute_task(task)
            
            elif fix_strategy == "skip_dependency_check":
                # Bypass dependency check (if safe)
                task.dependencies = []
                return self._execute_task(task)
            
            # ... more fix strategies ...
    
    return {"success": False, "reason": "no_proven_fix_available"}
```

### 6. Building Blocks Breakdown

**Enhancement**: Break down askchain tasks into building blocks

**Implementation**:
```python
def _break_down_task(self, task) -> List[str]:
    """Break down task into building blocks"""
    building_blocks = []
    
    # Parse ask text for building blocks
    ask_lower = task.ask_text.lower()
    
    if "create" in ask_lower or "generate" in ask_lower:
        building_blocks.append("create")
    if "update" in ask_lower or "modify" in ask_lower:
        building_blocks.append("update")
    if "delete" in ask_lower or "remove" in ask_lower:
        building_blocks.append("delete")
    if "execute" in ask_lower or "run" in ask_lower:
        building_blocks.append("execute")
    if "verify" in ask_lower or "check" in ask_lower:
        building_blocks.append("verify")
    
    return building_blocks
```

### 7. @FF Keyboard Shortcuts for AskChain Operations

**Enhancement**: Use @FF shortcuts for askchain management

**Shortcuts**:
- `F5`: Retry failed task
- `F9`: Skip task
- `Ctrl+Shift+R`: Retry all failed tasks
- `Ctrl+Shift+S`: Show chain status
- `Ctrl+Shift+D`: Discover new chains

## Integration Points

### 1. Initialize SYPHON Troubleshooter in Executor

```python
def __init__(self, project_root: Optional[Path] = None):
    # ... existing initialization ...
    
    # Initialize SYPHON-enhanced troubleshooting
    try:
        from jarvis_syphon_enhanced_troubleshooting import JARVISSyphonEnhancedTroubleshooting
        self.syphon_troubleshooter = JARVISSyphonEnhancedTroubleshooting(project_root)
        logger.info("✅ SYPHON-enhanced troubleshooting initialized")
    except Exception as e:
        logger.warning(f"⚠️  SYPHON troubleshooting not available: {e}")
        self.syphon_troubleshooter = None
```

### 2. Enhance Error Handling

```python
except Exception as e:
    # Extract intelligence from failure
    intelligence = self._extract_failure_intelligence(task, e)
    
    # Try pattern-based retry
    if intelligence.get("proven_patterns"):
        retry_result = self._retry_task_with_fix(task, e, intelligence)
        if retry_result.get("success"):
            return retry_result
    
    # Mark as failed with intelligence
    self.chain_manager.mark_task_failed(task.task_id, str(e))
    task.metadata["failure_intelligence"] = intelligence
    
    return {"success": False, "error": str(e), "intelligence": intelligence}
```

### 3. Pre-Execution Checks

```python
def _execute_task(self, task) -> Dict[str, Any]:
    # Pre-execution troubleshooting
    if self.syphon_troubleshooter:
        pre_check = self.syphon_troubleshooter.troubleshoot_with_syphon(
            {"task_id": task.task_id, "ask_text": task.ask_text},
            mode="pre",
            level="standard"
        )
        
        if pre_check.simulation_success_rate < 0.75:
            return {"success": False, "reason": "low_confidence_pre_check"}
    
    # ... rest of execution ...
```

## Benefits

1. **Proactive Troubleshooting**: Detect issues before execution
2. **Pattern Recognition**: Learn from common failure patterns
3. **Intelligence Extraction**: Build knowledge base from failures
4. **Automatic Recovery**: Retry with proven fixes
5. **Building Blocks**: Better understanding of task composition
6. **@FF Automation**: Quick actions for common operations

## Implementation Priority

1. **High Priority**:
   - Initialize SYPHON troubleshooter in executor
   - Add intelligence extraction from failures
   - Enhance error handling with SYPHON

2. **Medium Priority**:
   - Add pre-execution troubleshooting
   - Implement pattern recognition
   - Add simulation before execution

3. **Low Priority**:
   - Automatic retry with fixes
   - @FF keyboard shortcuts
   - Building blocks breakdown

## Tags

@ASKCHAIN @SYPHON #TROUBLESHOOTING #PATTERNS #INTELLIGENCE #PROACTIVE #SIMULATION
