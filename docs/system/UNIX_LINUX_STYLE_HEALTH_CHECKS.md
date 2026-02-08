# Unix/Linux Style Health Checks

**Status**: ✅ **IMPLEMENTED**

---

## Purpose

LUMINA health checks now use traditional Unix/Linux server startup/shutdown style status indicators, familiar to system administrators who work with Unix/Linux servers (both physical and virtual).

---

## Status Format

### Unix/Linux Style Indicators

| Status | Display | Meaning |
|--------|---------|---------|
| **OK** | `[  OK  ]` | Service/system operational |
| **WARN** | `[WARN ]` | Warnings detected, non-critical |
| **FAILED** | `[FAILED]` | Errors detected, requires attention |
| **CRITICAL** | `[CRIT ]` | Critical issues, immediate action required |

---

## Example Output

### Startup Sequence

```
================================================================================
LUMINA System Health Check - V3 Validation
================================================================================
Project Root: C:\Users\mlesn\Dropbox\my_projects\.lumina
Debug Mode: True

Starting system checks...

================================================================================
Starting core LUMINA systems...
================================================================================

[  OK  ] @JARVIS
[  OK  ] @R5
[  OK  ] @SYPHON
[  OK  ] @WOPR
[  OK  ] @UATU
[  OK  ] @BONES
[  OK  ] Pattern Unified Engine

================================================================================
Starting Docker & Kubernetes services...
================================================================================

[  OK  ] Docker
[  OK  ] Kubernetes
[WARN ] Docker Images

================================================================================
Starting local AI configurations...
================================================================================

[  OK  ] Cursor IDE Connection
[  OK  ] Ollama
[WARN ] Ultron Model (qwen2.5:72b)
[  OK  ] Local LLM Configs

================================================================================
Checking system resources...
================================================================================

[  OK  ] CPU
[  OK  ] Memory
[WARN ] Disk

================================================================================
System Health Check Summary
================================================================================

[WARN ] Warnings detected

Total Checks: 17
  [  OK  ]: 14
  [WARN ]: 3
  [FAILED]: 0
  [CRIT ]: 0

================================================================================
ISSUES DETECTED - REVIEW DETAILS ABOVE
================================================================================

[WARN ] checks need attention but are non-critical
[FAILED] checks indicate errors that should be fixed
[CRIT ] checks require immediate action
```

---

## Comparison to Traditional Unix/Linux

### Traditional Unix/Linux Startup

```
Starting system services...
[  OK  ] sshd.service
[  OK  ] nginx.service
[WARN ] postgresql.service
[FAILED] apache2.service
```

### LUMINA Health Check

```
Starting system checks...
[  OK  ] @JARVIS
[  OK  ] @R5
[WARN ] Docker Images
[FAILED] (if errors detected)
```

**Format**: ✅ **IDENTICAL TO TRADITIONAL UNIX/LINUX STYLE**

---

## Benefits

### 1. Familiar Format
- System administrators immediately understand status
- Consistent with Unix/Linux conventions
- Clear, unambiguous status indicators

### 2. Quick Scanning
- Easy to scan for issues
- Status clearly visible at start of line
- Consistent formatting

### 3. Automation-Friendly
- Easy to parse programmatically
- Consistent format for scripts
- Exit codes match status

---

## Exit Codes

| Code | Status | Meaning |
|------|--------|---------|
| 0 | `[  OK  ]` | All systems GREEN |
| 1 | `[WARN ]` | Warnings detected |
| 2 | `[FAILED]` | Errors detected |
| 3 | `[CRIT ]` | Critical issues |

---

## Integration with Operations

### Pre-Operation Checks

**Before NAS Migration**:
```bash
./scripts/lumina-debug-health-check.ps1
# Check for [  OK  ] on all critical systems
# Proceed if [WARN ] only on non-critical systems
```

**Before SpaceHog Epic-Battle**:
```bash
./scripts/lumina-debug-health-check.ps1
# Verify [  OK  ] on all systems
# Address [WARN ] before proceeding
```

**Before V3 Validation**:
```bash
./scripts/lumina-debug-health-check.ps1
# All systems should show [  OK  ]
# [WARN ] acceptable for non-critical
```

---

## Status Interpretation

### [  OK  ] - Operational
- System/service is working correctly
- No issues detected
- Ready for operations

### [WARN ] - Non-Critical Warning
- System/service is operational
- Minor issues detected
- Non-blocking for operations
- Should be addressed when convenient

### [FAILED] - Error Detected
- System/service has errors
- May impact operations
- Should be fixed before proceeding
- Review details for specific issues

### [CRIT ] - Critical Issue
- Critical system failure
- Operations may be impacted
- Immediate action required
- Do not proceed with operations

---

## Debug Mode

When `--debug` is enabled, additional details are shown:

```
[  OK  ] @JARVIS
         files_found: 3
         files_missing: 0
         dynamic_scaling: available
         dynamic_scaling_enabled: True
```

**Format**: Indented details below status line

---

## Customization

### Status Display

The status display format can be customized in `lumina_debug_health_check.py`:

```python
def _log_check(self, check: SystemCheck) -> None:
    """Log check result - Unix/Linux style OK/FAIL"""
    if check.status == HealthStatus.GREEN:
        status_display = "[  OK  ]"
    elif check.status == HealthStatus.YELLOW:
        status_display = "[WARN ]"
    elif check.status == HealthStatus.RED:
        status_display = "[FAILED]"
    else:  # CRITICAL
        status_display = "[CRIT ]"
```

---

## Related Systems

- `@BONES`: System diagnostics (uses health check results)
- `@UATU`: Ecosystem-wide observation (observes health check)
- `@JARVIS`: Command & Control (orchestrates health checks)

---

## Usage

### PowerShell
```powershell
.\scripts\lumina-debug-health-check.ps1
```

### Python Direct
```bash
python scripts/python/lumina_debug_health_check.py --debug --save
```

### Options
- `--debug`: Enable debug mode (shows detailed information)
- `--no-debug`: Disable debug mode
- `--save`: Save report to file
- `--project-root PATH`: Specify project root

---

## Report Location

**JSON Report**: `data/health_checks/debug_health_check_YYYYMMDD_HHMMSS.json`

**Contains**:
- Overall status
- Individual check results
- Detailed information for each check
- Timestamp and metadata

---

## Status

**Format**: ✅ **UNIX/LINUX STYLE IMPLEMENTED**

**Compatibility**: ✅ **FAMILIAR TO SYSTEM ADMINISTRATORS**

**Automation**: ✅ **SCRIPT-FRIENDLY FORMAT**

**Documentation**: ✅ **COMPLETE**

---

**Tags:** `#HEALTH_CHECK` `#UNIX` `#LINUX` `#SERVER_STYLE` `#SYSTEM_ADMIN` `@JARVIS` `@BONES` `@UATU` `@DOIT` `@LUMINA`

**Status:** ✅ **UNIX/LINUX STYLE HEALTH CHECKS OPERATIONAL**
