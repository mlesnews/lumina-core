# Module-First Principle

## Core Question

**Before implementing ANY functionality, ask:**

1. **Does this already have a module?**
2. **Should it have a module?**
3. **If it already has a module, we MUST use that module and stay within its scope**

## Principle

> "Does what we're trying to do already have a module? Should it have a module? Yes or no? Does it already have a module? If it already has a module, then we must always stay in the scope of module and not simply just design one-off systems around it. And it defeats the purpose of modules in the first place."

## Workflow

### Before Implementation Checklist

1. **Check for existing module**
   ```python
   from module_audit_checker import check_before_implementing
   
   result = check_before_implementing("retry logic")
   if result["has_module"]:
       # USE EXISTING MODULE
       from result["recommended_module"] import ...
   else:
       # CREATE NEW MODULE (if appropriate)
       ...
   ```

2. **Use module audit checker**
   ```bash
   python scripts/python/module_audit_checker.py
   ```

3. **Stay within module scope**
   - Don't create one-off implementations
   - Don't duplicate module functionality
   - Extend modules, don't replace them

## Examples

### ✅ CORRECT: Using Existing Module

```python
# GOOD: Using lumina_logger module for voice filter logging
from lumina_logger import log_voice_filter_accept, log_voice_filter_reject

log_voice_filter_accept(logger, similarity=0.95, threshold=0.90)
log_voice_filter_reject(logger, similarity=0.75, threshold=0.90)
```

### ❌ WRONG: One-Off Implementation

```python
# BAD: Creating one-off logging instead of using module
logger.info(f"✅ Voice match: {similarity:.2f} (user's voice) - ACCEPTING")
logger.warning(f"🚫 Voice REJECTED: {similarity:.2f} (TV/background) - FILTERING OUT")
```

### ✅ CORRECT: Using Retry Module

```python
# GOOD: Using cursor_chat_retry_manager module
from cursor_chat_retry_manager import retry_chat_operation

result = retry_chat_operation(send_message, max_retries=3)
```

### ❌ WRONG: One-Off Retry Logic

```python
# BAD: Creating one-off retry instead of using module
for attempt in range(3):
    try:
        send_message()
        break
    except Exception as e:
        if attempt >= 2:
            raise
        time.sleep(1)
```

## Module Categories

### Logging Modules
- `lumina_logger.py` - **USE THIS** for all logging
- Global patterns: `log_voice_filter_*`, `log()`, `get_logger()`

### Retry Modules
- `cursor_chat_retry_manager.py` - **USE THIS** for retry logic
- `CursorChatRetryManager` class
- `retry_chat_operation()` function

### Error Handling Modules
- `lumina_error_handler.py` - **USE THIS** for error handling
- Don't create one-off error handlers

### Voice Modules
- `voice_filter_system.py` - Voice filtering
- `cursor_transcription_sender.py` - Transcription sending
- Use these modules, don't duplicate their functionality

## Enforcement

### Module Audit Checker

Run before implementing:
```bash
python scripts/python/module_audit_checker.py
```

### Code Review Checklist

- [ ] Checked for existing module?
- [ ] Using existing module (not one-off)?
- [ ] Staying within module scope?
- [ ] Not duplicating module functionality?

## Benefits

1. **Consistency**: Same patterns across codebase
2. **Maintainability**: Update once, applies everywhere
3. **Reusability**: Modules can be used by multiple components
4. **Clarity**: Clear separation of concerns
5. **Efficiency**: Don't reinvent the wheel

## Status

✅ **Module Audit Checker**: Created (`module_audit_checker.py`)
✅ **Global Logging Module**: Using `lumina_logger.py` for all logging patterns
✅ **Retry Module**: Using `cursor_chat_retry_manager.py` for all retry logic
✅ **Documentation**: This document

---

**Last Updated**: 2025-01-05
**Purpose**: Enforce module-first principle - use existing modules, don't create one-offs
