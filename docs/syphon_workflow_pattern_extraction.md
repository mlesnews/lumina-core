# SYPHON Workflow Pattern Extraction

## Overview

**SYPHON Workflow Pattern Extraction** uses SYPHON intelligence extraction to automatically extract workflow patterns and register them with the @PEAK Pattern System.

## Features

✅ **SYPHON Intelligence Extraction**
- Extracts actionable items from workflows
- Identifies tasks and actions
- Captures decisions and conditions
- Gathers intelligence metadata

✅ **Pattern Classification**
- Automatically classifies workflow types (automation, data_processing, api_integration, etc.)
- Identifies step types (validation, extraction, processing, storage, notification)
- Extracts triggers and conditions

✅ **@PEAK Integration**
- Automatically registers extracted patterns to @PEAK Pattern System
- Stores patterns for reuse
- Enables pattern matching for future workflows

✅ **Direct Pattern Extraction**
- Extracts patterns directly from workflow structure
- Identifies step-by-step patterns
- Captures triggers and conditions

## Usage

### Basic Usage

```python
from scripts.python.syphon_workflow_patterns import SYPHONWorkflowPatternExtractor

# Initialize extractor
extractor = SYPHONWorkflowPatternExtractor()

# Extract patterns from workflow content
patterns = extractor.extract_patterns_from_workflow(
    workflow_content="Your workflow content here...",
    workflow_name="My Workflow",
    workflow_source="example.py"
)

# Patterns are automatically:
# 1. Saved to data/workflow_patterns/
# 2. Registered to @PEAK Pattern System
```

### Extract from File

```python
from pathlib import Path

# Extract patterns from a workflow file
patterns = extractor.extract_from_file(
    Path("scripts/python/jarvis_disable_all_lighting.py")
)
```

### Manual Registration

```python
# Register a pattern to @PEAK
for pattern in patterns:
    extractor.save_pattern(pattern)
    extractor.register_pattern_to_peak(pattern)
```

## Workflow Pattern Structure

```python
@dataclass
class WorkflowPattern:
    pattern_id: str              # Unique pattern ID
    name: str                    # Pattern name
    description: str             # Pattern description
    workflow_type: str          # Type (automation, data_processing, etc.)
    steps: List[Dict]           # Workflow steps
    triggers: List[str]         # Trigger conditions
    conditions: List[str]       # Conditional logic
    actions: List[str]          # Actions to execute
    metadata: Dict              # Additional metadata
    source_workflow: str        # Source workflow name
    extracted_at: str           # Extraction timestamp
```

## Workflow Types

- **automation**: Automated workflows with triggers
- **data_processing**: Data transformation workflows
- **api_integration**: API integration workflows
- **testing**: Testing and validation workflows
- **deployment**: Build and deployment workflows
- **general**: General purpose workflows

## Step Types

- **validation**: Check, verify, validate steps
- **extraction**: Get, fetch, retrieve steps
- **processing**: Process, transform, convert steps
- **storage**: Save, store, write steps
- **notification**: Send, post, notify steps
- **action**: General action steps

## Integration Points

### SYPHON System
- Uses SYPHON's intelligence extraction
- Leverages actionable item extraction
- Utilizes task and decision extraction

### @PEAK Pattern System
- Registers patterns automatically
- Stores patterns for reuse
- Enables pattern matching

### Workflow Files
- Can extract from Python scripts
- Supports JSON/YAML workflows
- Handles any text-based workflow format

## Example Output

```
🔍 Extracting patterns from workflow: Disable All Lighting
  📊 SYPHON extracted: 4 actionable items, 2 tasks, 1 decisions
✅ Extracted 1 pattern(s) from workflow: Disable All Lighting

📊 Pattern: Disable All Lighting Pattern
   Type: automation
   Steps: 4
   Triggers: 2
   Conditions: 1
   Actions: 2

✅ Saved pattern: data/workflow_patterns/workflow_pattern_20260102_044127.json
✅ Registered to @PEAK Pattern System
```

## Storage

Patterns are stored in:
- **JSON Files**: `data/workflow_patterns/{pattern_id}.json`
- **@PEAK Registry**: `data/peak_patterns/peak_pattern_registry.json`

## Tags

`@SYPHON` `@PEAK` `#PATTERNS` `#WORKFLOWS` `@JARVIS` `#AUTOMATION`
