# @ask Ticket Auto-Execution System - Code Cowork-Style

## Overview

Enhanced @ask ticket system with Code Cowork-style automatic task execution. Automatically executes validated tickets, completing tasks with file access, command execution, and result reporting.

## Architecture

### Enhanced Workflow

```
@ask → Validation (Holocron) → Auto-Execution → Results → Database → Holocron
```

### Components

1. **`ask_ticket_auto_executor.py`** - Code Cowork-style task execution engine
   - Task type detection (file ops, commands, workflows, etc.)
   - Execution with @v3 verification
   - Result reporting to holocron system

2. **Enhanced `ask_ticket_holocron_middleware.py`**
   - Optional auto-execution after validation
   - Seamless integration with existing validation flow

## Features

### Task Type Detection

Automatically detects task types from @ask text:
- **File Operations**: create, read, write, modify, delete files
- **Command Execution**: run scripts, CLI commands
- **Code Generation**: generate code, create functions/classes
- **Data Processing**: process, analyze, transform data
- **API Calls**: HTTP requests, API endpoints
- **Workflow Execution**: @DOIT workflows, pipelines

### @v3 Verification Integration

- Pre-execution verification
- Data integrity checks
- Workflow precondition validation
- Execution skipped if verification fails

### Execution Tracking

- Files accessed/modified
- Commands executed
- Execution time and status
- Error reporting and logging

### Holocron Integration

- Execution results saved to holocron format
- Queryable execution history
- Metadata preservation
- Cross-reference with tickets

## Usage

### Enable Auto-Execution in Middleware

```python
from ask_ticket_holocron_middleware import AskTicketHolocronMiddleware

middleware = AskTicketHolocronMiddleware(
    enable_auto_execution=True  # Enable Code Cowork-style execution
)

# Process @ask - will auto-execute after validation
_, validation_result = middleware.process_through_middleware(
    ask_id="...",
    ask_text="@ask create file 'test.py' with hello world",
    helpdesk_ticket="TICKET-20260113-0001"
)
```

### Direct Execution

```python
from ask_ticket_auto_executor import AskTicketAutoExecutor

executor = AskTicketAutoExecutor(
    enable_v3_verification=True,
    auto_execute=True
)

# Process and execute in one call
ticket, result = executor.process_and_execute(
    ask_id="...",
    ask_text="@ask run command 'python --version'",
    helpdesk_ticket="TICKET-20260113-0001"
)

print(f"Status: {result.status.value}")
print(f"Execution time: {result.execution_time_seconds:.2f}s")
print(f"Output: {result.output}")
```

### Execute Existing Ticket

```python
# Get validated ticket and execute
tickets = executor.collation_system.query(ask_id="...")
if tickets:
    result = executor.execute_ticket(tickets[0])
    print(f"Execution result: {result.to_dict()}")
```

### CLI Usage

```bash
# Process and execute @ask
python ask_ticket_auto_executor.py --execute ASK_ID "ASK_TEXT" HELPDESK GITLENS_TICKET GITLENS_PR

# Execute existing validated ticket
python ask_ticket_auto_executor.py --execute-ticket ASK_ID

# Skip @v3 verification (not recommended)
python ask_ticket_auto_executor.py --execute ASK_ID "ASK_TEXT" ... --no-v3

# Disable auto-execution
python ask_ticket_auto_executor.py --execute ASK_ID "ASK_TEXT" ... --no-auto
```

## Execution Results

### ExecutionResult Structure

```python
{
    "ask_id": "...",
    "status": "success|failed|skipped|partial",
    "executed_at": "2026-01-13T...",
    "execution_time_seconds": 1.23,
    "output": "Execution output...",
    "error": null,
    "files_accessed": ["file1.py", "file2.json"],
    "files_modified": ["file1.py"],
    "commands_executed": ["python --version"],
    "verification_passed": true,
    "verification_results": [...],
    "metadata": {...}
}
```

### Result Storage

- **Execution Logs**: `data/ask_ticket_executions/execution_{ask_id}_{timestamp}.json`
- **Holocron Format**: `data/holocron/ask_executions/execution_{ask_id}_{timestamp}.json`
- **Database**: Updated via collation system

## Integration Points

✅ **AskTicketCollationSystem** - Ticket storage and querying
✅ **AskTicketHolocronMiddleware** - Validation and shaping
✅ **@v3 Verification** - Pre-execution validation
✅ **@DOIT Workflows** - Workflow execution integration
✅ **Holocron System** - Result storage and querying

## Safety Features

- **@v3 Verification** - Validates before execution
- **Dangerous Command Filtering** - Blocks unsafe commands (rm -rf, format, etc.)
- **Timeout Protection** - 30-second timeout for commands
- **Error Handling** - Comprehensive error reporting
- **Execution Logging** - Full audit trail

## Examples

### File Operation

```python
# @ask: "create file 'test.py' with print('hello')"
# Detected: FILE_OPERATION
# Result: File created, execution logged
```

### Command Execution

```python
# @ask: "run command 'python --version'"
# Detected: COMMAND_EXECUTION
# Result: Command executed, output captured
```

### Workflow Execution

```python
# @ask: "@doit optimize workflow"
# Detected: WORKFLOW_EXECUTION
# Result: Connected to JARVIS @DOIT executor
```

## Future Enhancements

1. **AI-Powered Intent Understanding** - Use NLP/AI to better parse task intent
2. **File Access Permissions** - Implement permission system similar to Code Cowork
3. **Execution Sandboxing** - Add safety sandboxing for command execution
4. **Real-Time Progress Reporting** - Stream execution progress
5. **Rollback Capabilities** - Add undo/rollback for failed executions

## Tags

`#ASK` `#EXECUTION` `#AUTOMATION` `#CODE_COWORK` `@JARVIS` `@LUMINA` `@DOIT` `@V3`

## Related Systems

- `ask_ticket_collation_system.py` - Ticket collation
- `ask_ticket_holocron_middleware.py` - Validation middleware
- `v3_verification.py` - Verification system
- `jarvis_execute_ask_chains.py` - JARVIS execution
