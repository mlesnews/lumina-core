# Persistent Memory Rule - Auto-Process Workflows

**Rule**: No constant explanations - auto-digest workflows to Holocrons/DB/YouTube

## Core Principle

**"I DON'T NEED TO GET IN THE WEEDS"**

Workflows are automatically processed and digested into:
- **Holocrons** (persistent knowledge storage)
- **Database** (structured storage)
- **YouTube Content** (content generation)

No constant explanations needed - system handles it automatically.

## Importance Scoring System

**5+ Star System** (+, ++, +++, ++++, +++++)

- **+** (1 star): 0-20% importance
- **++** (2 stars): 21-40% importance
- **+++** (3 stars): 41-60% importance
- **++++** (4 stars): 61-80% importance
- **+++++** (5+ stars): 81-100% importance

## Auto-Processing Flow

1. **Workflow Executed** → Silent execution
2. **Importance Calculated** → 5+ star system
3. **Stored to Holocron** → If importance ≥ 3 stars
4. **Stored to DB** → Always
5. **YouTube Content** → If importance ≥ 4 stars
6. **No Explanation** → Unless importance = 5+ (+++++)

## Configuration

**`config/persistent_memory_config.json`**:
- `auto_digest`: true
- `explanation_threshold`: 0 (only explain 5+ star items)
- `workflow_auto_process`: true
- `auto_store_holocron`: true
- `auto_store_db`: true
- `auto_generate_content`: true

## Implementation

All workflows use `silent_workflow_executor.py` which:
- Executes without explanations
- Auto-calculates importance
- Stores to Holocrons/DB/YouTube
- Only outputs minimal result

---

**Status**: ✅ **RULE IMPLEMENTED**  
**Behavior**: Silent execution with auto-digestion
