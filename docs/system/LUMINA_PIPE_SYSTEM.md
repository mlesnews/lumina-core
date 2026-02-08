# LUMINA Pipe System

**Architecture**: Siphon → Pipe → Destination  
**Concept**: Like running a city - lots of pipes for different purposes.

#JARVIS #LUMINA #PIPES #ARCHITECTURE #SYPHON

---

## Overview

The LUMINA Pipe System provides a flexible, reusable architecture for data flow:

1. **SYPHON**: First, siphon the source (extract data)
2. **PIPE**: Then pipe it through stages (transform, analyze, etc.)
3. **DESTINATION**: Finally, deliver to destination (store, notify, etc.)

---

## Architecture

### Pipe Stages

Each pipe consists of multiple stages:

1. **SYPHON Stage** (`PipeStageType.SYPHON`)
   - Extract data from source
   - First stage in most pipes
   - Supports: email, filesystem, database, API

2. **TRANSFORM Stage** (`PipeStageType.TRANSFORM`)
   - Transform/process data
   - Extract structured data from unstructured

3. **VALIDATE Stage** (`PipeStageType.VALIDATE`)
   - Validate data quality
   - Check for errors

4. **ENRICH Stage** (`PipeStageType.ENRICH`)
   - Add additional data
   - Enhance with context

5. **ANALYZE Stage** (`PipeStageType.ANALYZE`)
   - Analyze data
   - Generate insights

6. **STORE Stage** (`PipeStageType.STORE`)
   - Store data
   - Save to filesystem/database

7. **NOTIFY Stage** (`PipeStageType.NOTIFY`)
   - Send notifications
   - Alert users

8. **ROUTE Stage** (`PipeStageType.ROUTE`)
   - Route to different destinations
   - Conditional routing

---

## HVAC Email Pipe

### Complete Flow

```
SYPHON → EXTRACT → ANALYZE → COMPARE → STORE
```

1. **SYPHON**: Siphon emails from Gmail/ProtonMail
2. **EXTRACT**: Extract bid data from attachments
3. **ANALYZE**: HVAC SME analysis
4. **COMPARE**: Compare all bids
5. **STORE**: Store results

### Usage

```bash
# Run HVAC Email Pipe
python scripts/python/run_hvac_email_pipe.py

# With custom query
python scripts/python/run_hvac_email_pipe.py --query "from:fletcher" --days 30

# With custom budget
python scripts/python/run_hvac_email_pipe.py --budget 15000
```

---

## Creating Custom Pipes

### Example: Financial Data Pipe

```python
from scripts.python.pipes.core import Pipe, PipeStage, PipeStageType
from scripts.python.pipes.syphon_stage import SyphonStage

# Create pipe
pipe = Pipe(
    name="financial_data_pipe",
    project_root=project_root,
    description="Process financial data from banking accounts"
)

# Stage 1: SYPHON - Siphon from banking API
syphon_stage = SyphonStage(
    name="siphon_banking",
    source_type="api",
    source_config={
        "api_url": "https://api.bank.com/transactions",
        "account_id": "12345"
    }
)

# Stage 2: Transform - Parse transactions
class TransactionTransformStage(PipeStage):
    def process(self, context):
        # Transform banking data
        return context

# Stage 3: Analyze - Financial analysis
class FinancialAnalysisStage(PipeStage):
    def process(self, context):
        # Analyze transactions
        return context

# Add stages
pipe.add_stages([
    syphon_stage,
    TransactionTransformStage("transform", PipeStageType.TRANSFORM),
    FinancialAnalysisStage("analyze", PipeStageType.ANALYZE)
])

# Execute
result = pipe.execute()
```

---

## Pipe Context

Data flows through stages via `PipeContext`:

```python
@dataclass
class PipeContext:
    pipe_name: str
    stage_name: str
    data: Dict[str, Any]  # Main data
    metadata: Dict[str, Any]  # Metadata
    errors: List[str]  # Errors
    warnings: List[str]  # Warnings
    timestamp: str
```

### Context Methods

- `add_data(key, value)` - Add data
- `get_data(key, default)` - Get data
- `add_error(error)` - Add error
- `add_warning(warning)` - Add warning

---

## Pipe Result

Each pipe execution returns a `PipeResult`:

```python
@dataclass
class PipeResult:
    success: bool
    pipe_name: str
    stages_executed: List[str]
    final_data: Dict[str, Any]
    errors: List[str]
    warnings: List[str]
    execution_time_seconds: float
    timestamp: str
```

---

## Hook & Trace Integration

All pipe operations are automatically tracked via Hook & Trace:

- Pipe start/complete
- Stage execution
- Errors and warnings
- Performance metrics

---

## File Structure

```
scripts/python/pipes/
├── __init__.py          # Pipe system exports
├── core.py              # Core pipe architecture
├── syphon_stage.py      # SYPHON stage implementation
└── hvac_email_pipe.py   # HVAC email pipe example

data/pipes/
└── <pipe_name>/
    ├── pipe_config.json
    └── result_*.json
```

---

## Best Practices

### 1. Always Start with SYPHON
```python
# First stage should always be SYPHON
syphon_stage = SyphonStage(...)
pipe.add_stage(syphon_stage)
```

### 2. Handle Errors Gracefully
```python
def process(self, context):
    try:
        # Process data
        pass
    except Exception as e:
        context.add_error(f"Processing failed: {e}")
        # Don't raise - let pipe decide whether to continue
```

### 3. Add Metadata
```python
context.metadata["custom_info"] = "value"
```

### 4. Log Progress
```python
logger.info(f"[{context.pipe_name}] Processing stage: {self.name}")
```

---

## Future Pipes

Potential pipes to create:

1. **Financial Data Pipe** - Banking, credit cards, investments
2. **Document Processing Pipe** - PDFs, contracts, invoices
3. **Calendar Pipe** - Events, appointments, reminders
4. **Task Management Pipe** - Todos, projects, workflows
5. **Communication Pipe** - SMS, calls, messages
6. **Health Data Pipe** - Medical records, fitness data
7. **Home Automation Pipe** - Smart home devices, sensors

---

## Summary

The LUMINA Pipe System provides:

- ✅ **Flexible Architecture**: Easy to create new pipes
- ✅ **Reusable Stages**: Common stages can be shared
- ✅ **Error Handling**: Built-in error tracking
- ✅ **Hook & Trace**: Automatic metrics and tracking
- ✅ **Extensible**: Easy to add new stage types
- ✅ **City-Scale**: Designed for many pipes running simultaneously

**Like running a city - lots of pipes for different purposes.**

---

**Status**: ✅ **READY - HVAC Email Pipe operational**
