# Workflow Memory Persistence System
Core Persistent Memories for All Workflows

## Overview

All workflows are stored as **core persistent memories** in the AI's memory system, broken down into basic building blocks. This ensures workflows are remembered across sessions and can be retrieved, reused, and learned from.

## Memory Tiers

Workflows are stored in different memory tiers based on importance and usage:

### Short-Term Memory (48 hours)
- Recent workflow executions
- Active workflows
- Current session workflows
- Default tier for new workflows

### Long-Term Memory (365 days)
- Core workflow patterns
- Frequently used workflows
- Important workflows
- Promoted from short-term based on usage

### Context Memory (24 hours)
- Current workflow context
- Active workflow state
- Session-specific workflows

### Episodic Memory
- Specific workflow executions
- Historical workflow runs
- Execution details and outcomes

### Semantic Memory
- Workflow knowledge and patterns
- Reusable workflow components
- Workflow relationships

### Procedural Memory
- How to execute workflows
- Workflow procedures
- Step-by-step instructions

## Building Blocks

Workflows are decomposed into basic building blocks:

### Step Blocks
- Individual workflow steps
- Step execution details
- Step status and outcomes

### Pattern Blocks
- Reusable workflow patterns
- Common workflow structures
- Pattern recognition

### Decision Blocks
- Decision points in workflows
- Decision logic
- Decision outcomes

### Action Blocks
- Actions to execute
- Action parameters
- Action results

### Condition Blocks
- Condition checks
- Conditional logic
- Condition outcomes

### Transition Blocks
- State transitions
- Workflow flow
- Transition conditions

### Integration Blocks
- External integrations
- API calls
- System interactions

### Validation Blocks
- Validation checks
- Verification logic
- Validation results

## Automatic Storage

Workflows are automatically stored when they execute:

```python
from workflow_base import WorkflowBase

class MyWorkflow(WorkflowBase):
    def __init__(self):
        super().__init__("MyWorkflow", total_steps=5)
    
    async def execute(self):
        # ... workflow execution ...
        
        # Automatically stored in memory after execution
        # Can also manually store:
        workflow_id = self.store_in_memory(
            memory_tier=MemoryTier.LONG_TERM,
            importance=0.9,
            tags=["critical", "automation"],
            success=True
        )
        return {"success": True, "workflow_id": workflow_id}
```

## API Endpoints

### Store Workflow
```
POST /lumina/workflows/memory/store
```

**Request Body:**
```json
{
  "workflow_data": {
    "workflow_name": "LogParsingWorkflow",
    "execution_id": "...",
    "total_steps": 5,
    "step_tracker": {...},
    "progress": {...}
  },
  "workflow_type": "log_parsing",
  "memory_tier": "short_term",
  "importance": 0.8,
  "tags": ["logging", "parsing"],
  "success": true
}
```

**Response:**
```json
{
  "success": true,
  "workflow_id": "abc123...",
  "memory_tier": "short_term",
  "message": "Workflow stored in persistent memory"
}
```

### Retrieve Workflow
```
GET /lumina/workflows/memory/<workflow_id>
```

**Response:**
```json
{
  "success": true,
  "workflow": {
    "workflow_id": "abc123...",
    "workflow_name": "LogParsingWorkflow",
    "workflow_type": "log_parsing",
    "building_blocks": [...],
    "execution_history": [...],
    "memory_tier": "short_term",
    "execution_count": 5,
    "success_rate": 1.0
  }
}
```

### Search Workflows
```
GET /lumina/workflows/memory/search?query=parsing&workflow_type=log_parsing&memory_tier=long_term&limit=10
```

**Response:**
```json
{
  "success": true,
  "workflows": [...],
  "count": 3
}
```

### Promote to Long-Term
```
POST /lumina/workflows/memory/promote/<workflow_id>
```

Promotes a workflow from short-term to long-term memory.

### Get Building Blocks
```
GET /lumina/workflows/memory/blocks?block_type=step&workflow_type=log_parsing
```

**Response:**
```json
{
  "success": true,
  "blocks": [
    {
      "block_id": "...",
      "block_type": "step",
      "name": "LogParsingWorkflow - Step 1",
      "description": "Parse log file",
      "content": {...},
      "dependencies": [],
      "outputs": ["parsed_logs"]
    }
  ],
  "count": 15
}
```

### Get Statistics
```
GET /lumina/workflows/memory/stats
```

**Response:**
```json
{
  "success": true,
  "statistics": {
    "total_workflows": 42,
    "by_tier": {
      "short_term": 20,
      "long_term": 15,
      "context": 7
    },
    "by_type": {
      "log_parsing": 10,
      "wopr_experiment": 5,
      "general": 27
    },
    "total_building_blocks": 210,
    "total_executions": 150,
    "average_success_rate": 0.95
  }
}
```

## Integration Points

### Memory Manager
- Workflows stored in memory manager
- Automatic tier management
- Access tracking and promotion

### R5 Living Context Matrix
- Workflow knowledge aggregated in R5
- Workflow patterns extracted
- Cross-workflow learning

### Workflow Base Class
- Automatic storage on execution
- Memory persistence built-in
- Easy access to memory system

## Memory Lifecycle

1. **Creation**: Workflow executed → Stored in short-term memory
2. **Usage**: Workflow accessed → Access count incremented
3. **Promotion**: Frequent access → Promoted to long-term memory
4. **Retention**: Long-term workflows retained for 365 days
5. **Cleanup**: Old short-term workflows cleaned after 48 hours

## Building Block Extraction

When a workflow is stored, it's automatically decomposed:

1. **Steps**: Each workflow step becomes a step block
2. **Patterns**: Progress patterns extracted as pattern blocks
3. **Validations**: Verification logic becomes validation blocks
4. **Dependencies**: Block dependencies identified
5. **Outputs**: Block outputs cataloged

## Usage Examples

### Store Workflow After Execution
```python
# In workflow execute() method
result = await self.execute()
success = result.get("success", False)

# Store in memory
workflow_id = self.store_in_memory(
    memory_tier=MemoryTier.LONG_TERM if success else MemoryTier.SHORT_TERM,
    importance=0.9 if success else 0.5,
    tags=["automation", "critical"],
    success=success
)
```

### Retrieve and Reuse Workflow
```python
from workflow_memory_persistence import WorkflowMemoryPersistence

persistence = WorkflowMemoryPersistence()
workflow = persistence.retrieve_workflow("workflow_id")

# Access building blocks
for block in workflow.building_blocks:
    if block.block_type == BuildingBlockType.STEP:
        print(f"Step: {block.name}")
```

### Search for Similar Workflows
```python
workflows = persistence.search_workflows(
    query="log parsing",
    workflow_type="log_parsing",
    memory_tier=MemoryTier.LONG_TERM
)
```

### Promote Important Workflow
```python
persistence.promote_to_long_term("workflow_id")
```

## Benefits

1. **Persistence**: Workflows remembered across sessions
2. **Reusability**: Building blocks can be reused
3. **Learning**: System learns from workflow patterns
4. **Efficiency**: Avoid recreating similar workflows
5. **Knowledge**: Workflow knowledge aggregated in R5
6. **Tiered Storage**: Important workflows in long-term, recent in short-term

## Storage Locations

- **Workflow Data**: `data/memory/workflows/workflows.json`
- **Memory Manager**: `data/memory/short_term_memories.json`, `data/memory/long_term_memories.json`
- **R5 Integration**: `data/r5_living_matrix/`

## Notes

- **Automatic Storage**: Workflows stored automatically when using WorkflowBase
- **Building Blocks**: All workflows decomposed into reusable blocks
- **Memory Tiers**: Flexible tier system (short-term, long-term, context, etc.)
- **Integration**: Fully integrated with memory manager and R5
- **Core Memories**: All workflows are part of AI's core persistent memories

