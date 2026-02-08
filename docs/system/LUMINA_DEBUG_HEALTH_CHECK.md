# LUMINA Debug Mode Health Check - V3 Validation

**Status**: ✅ **SYSTEM CREATED**

---

## Purpose

Comprehensive granular health check for all LUMINA systems in debug mode. Verifies all systems are GREEN before:
- NAS migration
- SpaceHog epic-battle
- V3 validation of local AI configurations
- Other critical operations

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
- `--debug`: Enable debug mode (default: enabled)
- `--no-debug`: Disable debug mode
- `--save`: Save report to file (default: enabled)
- `--project-root PATH`: Specify project root directory

---

## What It Checks

### 1. Core LUMINA Systems ✅
- **@JARVIS**: Files, dynamic scaling integration
- **@R5**: Living Context Matrix, unified engine integration
- **@SYPHON**: Pattern extraction, unified engine integration
- **@WOPR**: Simulator, unified engine integration
- **@UATU**: The Watcher, observation files
- **@BONES**: System diagnostics, reboot scripts
- **Pattern Unified Engine**: Core engine, V3 test

### 2. Docker & Kubernetes ✅
- **Docker**: Installation, daemon status, authentication
- **Kubernetes**: kubectl, cluster status
- **Docker Images**: dyno-lumina-jarvis, access issues
- **Access Issues**: Push/pull denied, authentication

### 3. Local AI Configurations ✅
- **Ollama**: Installation, service status, models
- **Local LLM Configs**: Config files, JSON validation
- **MCP Configs**: Localhost, homelab hybrid

### 4. System Resources ✅
- **CPU**: Usage, cores, thresholds
- **Memory**: Usage, total, available, thresholds
- **Disk**: Usage, free space, thresholds

---

## Status Levels

| Status | Icon | Meaning |
|--------|------|---------|
| **GREEN** | ✅ | All systems operational |
| **YELLOW** | ⚠️  | Warnings, non-critical |
| **RED** | ❌ | Errors detected |
| **CRITICAL** | 🚨 | Critical issues requiring immediate action |

---

## Report Output

### Console Output
- Real-time check results
- Status icons and details
- Summary with counts
- Actionable recommendations

### JSON Report
Saved to: `data/health_checks/debug_health_check_YYYYMMDD_HHMMSS.json`

**Report Structure**:
```json
{
  "timestamp": "2026-01-12T...",
  "overall_status": "GREEN|YELLOW|RED|CRITICAL",
  "project_root": "...",
  "debug_mode": true,
  "summary": {
    "total_checks": 15,
    "green": 12,
    "yellow": 2,
    "red": 1,
    "critical": 0
  },
  "checks": [
    {
      "name": "@JARVIS",
      "status": "GREEN",
      "details": {...},
      "timestamp": "..."
    },
    ...
  ]
}
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All systems GREEN |
| 1 | Warnings detected (YELLOW) |
| 2 | Errors detected (RED) |
| 3 | Critical issues (CRITICAL) |

---

## Integration with Operations

### Pre-NAS Migration
Run health check to ensure:
- All core systems operational
- Docker/Kubernetes ready
- System resources adequate
- No critical issues

### Pre-SpaceHog Epic-Battle
Verify:
- All systems GREEN
- Disk space adequate
- No blocking issues

### V3 Local AI Validation
Check:
- Ollama operational
- Local LLM configs valid
- All AI systems integrated

---

## Debug Mode Features

When `--debug` is enabled:
- Detailed check results
- File paths and status
- Integration status
- Error details
- Configuration validation

---

## Example Output

```
================================================================================
🔍 LUMINA DEBUG MODE HEALTH CHECK - V3 VALIDATION
================================================================================
   Project Root: C:\Users\mlesn\Dropbox\my_projects\.lumina
   Debug Mode: True

================================================================================
CHECK 1: CORE LUMINA SYSTEMS
================================================================================

✅ @JARVIS: GREEN
      files_found: 3
      files_missing: 0
      dynamic_scaling: available
      dynamic_scaling_enabled: True

✅ @R5: GREEN
      files_found: 3
      unified_engine_integrated: True

...

================================================================================
📊 HEALTH CHECK SUMMARY
================================================================================

✅ Overall Status: GREEN

   Total Checks: 15
   ✅ GREEN: 12
   ⚠️  YELLOW: 2
   ❌ RED: 1
   🚨 CRITICAL: 0
```

---

## Next Steps After Health Check

### If GREEN ✅
- Proceed with NAS migration
- Proceed with SpaceHog epic-battle
- Proceed with V3 validation

### If YELLOW ⚠️
- Review warnings
- Address non-critical issues
- Re-run health check

### If RED ❌
- Fix errors immediately
- Review detailed report
- Do not proceed with operations

### If CRITICAL 🚨
- Stop all operations
- Address critical issues immediately
- System may be unstable

---

## Related Systems

- `@BONES`: System diagnostics
- `@UATU`: Ecosystem-wide observation
- `@JARVIS`: Command & Control
- `@R5`: Living Context Matrix

---

**Tags:** `#HEALTH_CHECK` `#DEBUG_MODE` `#V3` `#VALIDATION` `@JARVIS` `@BONES` `@UATU` `@DOIT` `@LUMINA`

**Status:** ✅ **SYSTEM OPERATIONAL - READY FOR USE**
