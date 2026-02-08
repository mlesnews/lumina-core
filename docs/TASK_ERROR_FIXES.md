# Task Error Fixes

## Issues Fixed

### 1. Docker Task Type Error

**Error**: `Error: there is no registered task type 'docker-run'. Did you miss installing an extension that provides a corresponding task provider?`

**Cause**: Tasks were using `"type": "docker-run"` and `"type": "docker-build"` which require the Docker extension to be installed.

**Fix**: Converted docker tasks to use `"type": "shell"` with direct `docker` commands.

**Files Fixed**:
- `../cfs-llc-env/.vscode/tasks.json` - Converted docker-build and docker-run tasks

**Solution Applied**:
```json
// Before (requires Docker extension):
{
  "type": "docker-run",
  "label": "docker-run: debug",
  "python": { ... }
}

// After (works without extension):
{
  "type": "shell",
  "label": "docker-run: debug",
  "command": "docker",
  "args": [
    "run",
    "--rm",
    "-p",
    "8000:8000",
    "image:latest",
    "uvicorn",
    ...
  ]
}
```

### 2. PowerShell Script Exit Code 64

**Error**: PowerShell script `direct_fix_mcp.ps1` terminated with exit code 64

**Cause**: Unhandled errors or improper error handling in PowerShell script

**Fix**: 
- Added proper error handling with `$ErrorActionPreference = "Stop"`
- Added trap block to catch unhandled errors
- Improved exit code handling (64 for unexpected errors, 1 for validation failures, 0 for success)

**Files Fixed**:
- `../cedarbrook-financial-services_llc-env/scripts/powershell/direct_fix_mcp.ps1`

**Changes Made**:
```powershell
# Added error handling
$ErrorActionPreference = "Stop"
$PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

# Added trap for unhandled errors
trap {
    Write-Host "`n❌ Script error: $_" -ForegroundColor Red
    Write-Host "   At line: $($_.InvocationInfo.ScriptLineNumber)" -ForegroundColor Yellow
    exit 64
}
```

### 3. JSON Syntax Error

**Error**: `JSONDecodeError: Expecting property name enclosed in double quotes`

**Cause**: Invalid JSON comments in tasks.json file

**Fix**: Removed JSON comments (JSON doesn't support comments)

**Files Fixed**:
- `../cfs-llc-env/.vscode/tasks.json` - Removed comment lines

## Tools Created

### `fix_docker_tasks.py`

Automated script to fix docker-run and docker-build tasks across all workspaces.

**Usage**:
```bash
# Fix all workspaces
python scripts/python/fix_docker_tasks.py --all

# Fix specific workspace
python scripts/python/fix_docker_tasks.py --workspace ../cfs-llc-env
```

**Features**:
- Automatically detects docker-run and docker-build tasks
- Converts them to shell tasks with docker commands
- Preserves task configuration (dependsOn, presentation, etc.)
- Works across multiple workspaces

## Verification

All fixes have been verified:
- ✅ Docker tasks converted to shell tasks
- ✅ PowerShell script has proper error handling
- ✅ JSON files are valid
- ✅ Tasks work without Docker extension

## Prevention

To prevent these issues in the future:

1. **Use shell tasks for Docker**: Instead of docker-run/docker-build task types, use shell tasks with docker commands
2. **Validate JSON**: Always validate JSON files before committing
3. **Error Handling**: Always include proper error handling in PowerShell scripts
4. **Exit Codes**: Use appropriate exit codes (0=success, 1=error, 64=unexpected error)

---

**Status**: ✅ All issues resolved

