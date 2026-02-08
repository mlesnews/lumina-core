# Resource-Aware System Integration

**Date**: 2025-01-24
**Status**: ACTIVE
**Purpose**: Unified integration of all resource-aware systems

## Overview

The Resource-Aware System Integration provides a unified interface connecting:

1. **Memory Manager** - Short/long-term persistent memory
2. **Resource-Aware Context Checker** - Pre-flight resource checking before AI queries
3. **Holocron Query Engine** - Query Holocron Archive knowledge base
4. **R5 Living Context Matrix** - IDE chat session aggregation
5. **Jupyter Notebook Integration** - Data export and analysis

## Architecture

```
┌─────────────────────────────────────────┐
│   Resource-Aware Integration (Unified)  │
└───────────────┬─────────────────────────┘
                │
    ┌───────────┼───────────┐
    │           │           │
    ▼           ▼           ▼
┌────────┐ ┌─────────┐ ┌──────────┐
│ Memory │ │Holocron │ │    R5    │
│Manager │ │ Engine  │ │  System  │
└────┬───┘ └────┬────┘ └─────┬────┘
     │          │            │
     └──────────┴────────────┘
                │
                ▼
     ┌─────────────────────┐
     │ Context Checker     │
     │ (Pre-flight checks) │
     └─────────────────────┘
                │
                ▼
     ┌─────────────────────┐
     │   Jupyter Export    │
     │   (Analysis & Viz)  │
     └─────────────────────┘
```

## Components

### 1. Memory Manager
**Location**: `scripts/python/memory_manager.py`

**Features**:
- Short-term memory (recent context, session state)
- Long-term memory (archived knowledge, patterns)
- Working memory (active context)
- Memory consolidation and archiving

**Integration**:
- Stores R5 session summaries
- Exports for Jupyter analysis
- Provides context to resource checker

### 2. Resource-Aware Context Checker
**Location**: `scripts/python/resource_aware_context.py`

**Features**:
- Pre-flight checks before AI queries
- Checks memory, holocron, R5, documentation, config
- Confidence scoring
- Token savings estimation

**Integration**:
- Uses Memory Manager for context
- Queries Holocron Engine
- Checks R5 Living Context Matrix
- Returns unified results

### 3. Holocron Query Engine
**Location**: `scripts/python/holocron_query.py`

**Features**:
- Query Holocron Archive knowledge base
- Content-based and metadata search
- Relevance scoring
- Multiple holocron types

**Integration**:
- Provides intelligence reports to context checker
- Can be queried directly or through unified interface

### 4. R5 Living Context Matrix
**Location**: `scripts/python/r5_living_context_matrix.py`

**Features**:
- IDE chat session aggregation
- @PEAK pattern extraction
- @WHATIF thought experiments
- Knowledge condensation

**Integration**:
- Session summaries stored in memory
- Exports for Jupyter analysis
- Provides context to resource checker

### 5. Unified Integration Interface
**Location**: `scripts/python/resource_aware_integration.py`

**Features**:
- Single entry point for all systems
- Unified query interface
- System status monitoring
- Jupyter export coordination

## Usage

### Basic Usage

```python
from scripts.python.resource_aware_integration import get_resource_aware_integration
from pathlib import Path

project_root = Path(r"D:\Dropbox\my_projects")
integration = get_resource_aware_integration(project_root)

# Unified query
result = integration.query("Tesla autonomous vehicles")
if result.found and not result.should_use_ai:
    print(f"Found in {result.source}: {result.content}")
    print(f"Tokens saved: {result.tokens_saved}")
else:
    # Proceed with AI query only if needed
    pass
```

### Store Memory

```python
# Store important information
memory_id = integration.store_memory(
    content={"type": "session", "action": "code_review", "file": "test.py"},
    memory_type=MemoryType.SHORT_TERM,
    importance=MemoryImportance.MEDIUM,
    tags=["code", "review"]
)
```

### Ingest R5 Session

```python
session_data = {
    "session_id": "session_001",
    "timestamp": datetime.now().isoformat(),
    "messages": [
        {"role": "user", "content": "How do I use @PEAK patterns?"},
        {"role": "assistant", "content": "@PEAK patterns are..."}
    ]
}

session_id = integration.ingest_r5_session(session_data)
```

### Export for Jupyter

```python
# Export all data for Jupyter notebooks
export_data = integration.export_for_jupyter()

# Use in Jupyter
import pandas as pd

memory_df = pd.DataFrame(export_data["memory"]["short_term_summary"]["recent"])
r5_sessions_df = pd.DataFrame(export_data["r5"]["sessions_df"])
```

### Consolidate Systems

```python
# Consolidate memory and aggregate R5
stats = integration.consolidate_all()
print(f"Memory consolidated: {stats['memory']}")
print(f"R5 aggregated: {stats['r5']}")
```

### System Status

```python
# Check system status
status = integration.get_system_status()
print(json.dumps(status, indent=2))
```

## Integration Flow

### Query Flow

1. **User Query**: Agent receives query
2. **Unified Query**: `integration.query(query)`
3. **Parallel Checks**:
   - Memory Manager: Check short/long-term memory
   - Holocron Engine: Query knowledge base
   - R5 System: Check aggregated context
   - Context Checker: Check all resources
4. **Best Result**: Return highest confidence result
5. **Decision**: Should use AI? (based on confidence)
6. **Response**: Return local result or proceed with AI

### Memory Flow

1. **Session Ends**: Store session summary in memory
2. **R5 Ingestion**: Ingest into R5 Living Context Matrix
3. **Memory Storage**: Store important info in memory
4. **Consolidation**: Periodically consolidate memory
5. **Export**: Export for Jupyter analysis

### Jupyter Flow

1. **Data Collection**: Collect from all systems
2. **Format**: Format for pandas/analysis
3. **Export**: Export to Jupyter notebook
4. **Analysis**: Analyze in Jupyter
5. **Visualization**: Create visualizations
6. **Insights**: Generate insights

## Configuration

### Project Root
Default: `D:\Dropbox\my_projects`

### Directories
- Memory: `data/memory/`
- R5: `data/r5_living_matrix/`
- Holocron: `data/holocron/`
- Jupyter: `data/jupyter/`

### Configuration Files
- Memory: Auto-configured
- R5: `config/r5/r5_config.json` (if exists)
- Holocron: Auto-indexed from `data/holocron/`
- Jupyter: `config/jupyter/nas_config.json`

## Best Practices

1. **Always use unified query** for checking resources
2. **Store important sessions** in memory and R5
3. **Consolidate regularly** to maintain efficiency
4. **Export for analysis** periodically to Jupyter
5. **Monitor system status** for health checks
6. **Use confidence scores** to decide on AI usage

## Troubleshooting

### System Not Initialized
- Check project root path
- Verify all modules are importable
- Check logs for errors

### No Results Found
- Normal for new queries
- System learns over time
- Use AI query as fallback

### Integration Errors
- Check individual system status
- Review logs for specific errors
- Verify directory structure

## Next Steps

1. **Continuous Learning**: System improves with more sessions
2. **Pattern Recognition**: R5 extracts patterns over time
3. **Memory Consolidation**: Regular consolidation maintains efficiency
4. **Jupyter Analysis**: Periodic analysis provides insights

---

**Status**: ✅ OPERATIONAL
**Maintenance**: Automatic
**Support**: See individual component docs

