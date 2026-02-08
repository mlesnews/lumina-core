# Idle Timeout and Command Chaining System

## Overview

This document describes the idle timeout configuration and command chaining system implemented for the LUMINA project.

## Idle Timeout Configuration

### Changes Made

**File**: `scripts/python/ide_session_load_balancer.py`

- **Previous**: `stall_timeout_seconds = 60` (60 seconds / 1 minute)
- **Updated**: `stall_timeout_seconds = 600` (600 seconds / 10 minutes)

### Purpose

The idle timeout determines how long a session can remain inactive before being considered "stalled". Increasing this timeout to 10 minutes allows the system to retain control longer, reducing premature session termination when the user is still actively working.

### Impact

- Sessions will remain active for up to 10 minutes of inactivity
- Better control retention during longer thinking/planning periods
- Reduced false positives for stalled sessions
- More tolerant of natural workflow pauses

## Command Chaining System

### New Component

**File**: `scripts/python/command_chain_executor.py`

A comprehensive command chaining system that supports multiple operators for advanced command execution.

### Supported Operators

1. **`&&` (AND)**: Execute next command only if previous succeeded
   ```bash
   cmd1 && cmd2  # Run cmd2 only if cmd1 succeeds
   ```

2. **`||` (OR)**: Execute next command only if previous failed
   ```bash
   cmd1 || cmd2  # Run cmd2 only if cmd1 fails
   ```

3. **`&` (Background)**: Execute command in background
   ```bash
   cmd1 & cmd2  # Run cmd1 in background, then cmd2
   ```

4. **`|` (Pipe)**: Pipe output from one command to next
   ```bash
   cmd1 | cmd2  # Pipe cmd1 output to cmd2
   ```

### Features

- **Cross-platform**: Works on Windows (PowerShell) and Unix (bash)
- **Conditional Execution**: Smart handling of && and || operators
- **Background Processing**: Support for parallel command execution
- **Piping**: Standard Unix-style command piping
- **Error Handling**: Comprehensive error reporting and timeout support
- **Result Tracking**: Detailed execution results for each command

### Usage Examples

#### Basic Chaining
```bash
python scripts/python/command_chain_executor.py "echo 'Step 1' && echo 'Step 2'"
```

#### Error Handling
```bash
python scripts/python/command_chain_executor.py "false || echo 'Fallback command'"
```

#### Background Execution
```bash
python scripts/python/command_chain_executor.py "long_task & echo 'Task started'"
```

#### Piping
```bash
python scripts/python/command_chain_executor.py "echo 'test' | grep 'test'"
```

#### Complex Chains
```bash
python scripts/python/command_chain_executor.py "cmd1 && cmd2 || cmd3 & cmd4"
```

### CLI Options

```bash
python scripts/python/command_chain_executor.py --help
```

Options:
- `--cwd PATH`: Set working directory
- `--timeout SECONDS`: Set timeout per command
- `--wait-background`: Wait for background commands to complete

### Programmatic Usage

```python
from scripts.python.command_chain_executor import CommandChainExecutor
from pathlib import Path

executor = CommandChainExecutor(project_root=Path.cwd())
results = executor.execute_chain("cmd1 && cmd2 || cmd3", timeout=30)

for result in results:
    print(f"{result.command}: {result.success} (code: {result.return_code})")
```

### Integration Points

The command chain executor can be integrated with:

- **@JARVIS**: For coordinated command execution
- **@DOIT**: For autonomous workflow execution
- **@RR**: For read & run operations
- **@MARVIN**: For reality checking before execution

## Configuration Files

### Session Timeout

**File**: `config/service_orchestration.yaml`

```yaml
security:
  session_timeout: 3600  # seconds (1 hour)
```

Note: This is different from the idle timeout. Session timeout is for authentication sessions, while idle timeout is for IDE session activity.

## Benefits

1. **Better Control Retention**: 10-minute idle timeout prevents premature session termination
2. **Advanced Command Execution**: Support for complex command chains with logical operators
3. **Parallel Processing**: Background execution enables concurrent operations
4. **Error Recovery**: OR operator (||) enables fallback command execution
5. **Workflow Integration**: Seamless integration with existing LUMINA systems

## Future Enhancements

- [ ] Support for command grouping with parentheses
- [ ] Advanced piping with multiple commands
- [ ] Command result caching
- [ ] Integration with @SYPHON telemetry
- [ ] Performance metrics and optimization

## Related Systems

- **IDE Session Load Balancer**: Manages session timeouts and load balancing
- **JARVIS Command Control**: High-level command execution system
- **@DOIT Executor**: Autonomous execution system
- **SYPHON Telemetry**: Workflow tracking and metrics

## Tags

#JARVIS @lumina #TOYSAAC #peak
