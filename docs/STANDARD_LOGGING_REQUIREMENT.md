# Standard Logging Module Requirement

## CRITICAL: 5/5 Importance (+++++)

**ALL scripts in the .lumina project MUST use the standard logging module: `lumina_logger`**

## Standard Pattern

```python
# ALWAYS use the standard logging module: lumina_logger
# This is a critical requirement - all scripts must use lumina_logger.get_logger()
from lumina_logger import get_logger

logger = get_logger("ModuleName")
```

## NEVER Use

❌ **DO NOT** use fallback patterns:
```python
# WRONG - Do not use this pattern
try:
    from lumina_logger import get_logger
except ImportError:
    import logging
    logging.basicConfig(level=logging.INFO)
    get_logger = lambda name: logging.getLogger(name)
```

❌ **DO NOT** use direct logging:
```python
# WRONG - Do not use this
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ModuleName")
```

## Why This Matters

1. **Consistency**: All components use the same logging format
2. **Colorization**: Standard module provides colorized output when available
3. **Centralized Configuration**: All logging behavior is controlled in one place
4. **File Logging**: Standard module supports file logging out of the box
5. **Proper Naming**: Ensures consistent logger naming across the ecosystem

## Enforcement

This requirement is stored as a **CRITICAL (5/5)** memory in JARVIS Persistent Memory:
- Memory Type: LONG_TERM
- Priority: CRITICAL
- Tags: `logging`, `standard`, `lumina_logger`, `coding_standards`, `critical`, `mandatory`, `5/5`, `+++++`

## Verification

To verify all scripts use standard logging:
```bash
python scripts/python/update_all_to_standard_logging.py
```

To verify the memory is stored:
```bash
python scripts/python/verify_logging_standard_memory.py
```

## Updated Files

The following files have been updated to use standard logging:
- `tool_resource_utilization_historian.py`
- `standardized_timestamp_logging.py`
- `va_compound_log_monitor.py`

## If lumina_logger is Not Available

If `lumina_logger` is not available, the script should:
1. **Fail gracefully** with a clear error message
2. **NOT** fall back to basic logging
3. **Indicate** that the standard module is required

Example:
```python
try:
    from lumina_logger import get_logger
except ImportError as e:
    raise ImportError(
        "lumina_logger is required but not available. "
        "This is a critical dependency. Please ensure lumina_logger.py is in the path."
    ) from e
```

## Memory Reference

This requirement is permanently stored in JARVIS memory with ID:
`mem_20260103_130312_aa668dbb1e570e5a`

To retrieve:
```python
from jarvis_persistent_memory import JARVISPersistentMemory
memory = JARVISPersistentMemory(project_root)
results = memory.search_memories(query="lumina_logger", tags=["critical", "5/5"])
```
