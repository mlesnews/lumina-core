# V3 & R5 Systems Startup Guide

**Last Updated:** 2025-01-27  
**Startup Script:** `scripts/python/start_v3_r5_systems.py`

## Quick Start

### PowerShell (Recommended)
```powershell
.\scripts\powershell\Start-V3R5Systems.ps1
```

### Python
```bash
python scripts/python/start_v3_r5_systems.py
```

## What the Startup Script Does

1. ✅ **Checks Python Version** - Ensures Python 3.8+ is installed
2. ✅ **Checks Dependencies** - Verifies all required packages are installed
3. ✅ **Installs Missing Dependencies** - Automatically installs missing packages
4. ✅ **Verifies V3 System** - Tests V3 verification system
5. ✅ **Verifies R5 System** - Tests R5 living context matrix system
6. ✅ **Starts R5 API Server** - Starts API server on port 8000 (optional)

## Required Dependencies

The startup script automatically installs these if missing:

- **flask** - Web framework for R5 API server
- **flask-cors** - CORS support for API
- **requests** - HTTP library for API calls

## Optional Dependencies

These are optional but recommended for full functionality:

- **azure-keyvault-secrets** - Azure Key Vault integration
- **azure-identity** - Azure authentication
- **paramiko** - SSH client support

## Usage Options

### Check Dependencies Only
```powershell
.\scripts\powershell\Start-V3R5Systems.ps1 -CheckOnly
```

Or:
```bash
python scripts/python/start_v3_r5_systems.py --check-only
```

### Start Without API Server
```powershell
.\scripts\powershell\Start-V3R5Systems.ps1 -NoAPI
```

Or:
```bash
python scripts/python/start_v3_r5_systems.py --no-api
```

### Run API Server in Foreground
```powershell
.\scripts\powershell\Start-V3R5Systems.ps1 -Foreground
```

Or:
```bash
python scripts/python/start_v3_r5_systems.py --foreground
```

## Startup Sequence

```
[Step 1] Checking Python version...
  ✓ Python 3.11.9

[Step 2] Checking dependencies...
  ✓ flask: Installed
  ✓ flask-cors: Installed
  ✓ requests: Installed

[Step 3] Verifying V3 system...
  ✓ V3 system verified

[Step 4] Verifying R5 system...
  ✓ R5 system verified

[Step 5] Starting R5 API server...
  ✓ R5 API server started on http://localhost:8000

============================================================
STARTUP COMPLETE - All systems operational
============================================================
```

## Verification

After startup, verify systems are running:

### Check R5 API Server
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/r5/health"
```

Or:
```bash
curl http://localhost:8000/r5/health
```

### Run Full Verification
```bash
python scripts/python/verify_v3_r5_systems.py
```

## Troubleshooting

### Dependencies Not Installing

If dependencies fail to install:

1. **Check pip is up to date:**
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Install manually:**
   ```bash
   pip install flask flask-cors requests
   ```

3. **Check Python environment:**
   ```bash
   python --version
   ```

### R5 API Server Won't Start

1. **Check if port 8000 is in use:**
   ```powershell
   Test-NetConnection -ComputerName localhost -Port 8000
   ```

2. **Check for errors:**
   ```bash
   python scripts/python/r5_api_server.py
   ```

3. **Verify dependencies:**
   ```bash
   python scripts/python/start_v3_r5_systems.py --check-only
   ```

### V3/R5 Import Errors

1. **Verify scripts are in correct location:**
   - `scripts/python/v3_verification.py`
   - `scripts/python/r5_living_context_matrix.py`

2. **Check Python path:**
   ```python
   import sys
   print(sys.path)
   ```

## Manual Startup

If you prefer to start services manually:

### Start R5 API Server
```bash
python scripts/python/r5_api_server.py
```

### Verify V3 System
```python
from scripts.python.v3_verification import V3Verification
verifier = V3Verification()
```

### Verify R5 System
```python
from scripts.python.r5_living_context_matrix import R5LivingContextMatrix
from pathlib import Path
r5 = R5LivingContextMatrix(Path("."))
```

## Integration with Other Systems

The startup script integrates with:

- **Lumina Deployment** - `scripts/python/deploy_activate_lumina.py`
- **System Verification** - `scripts/python/verify_v3_r5_systems.py`
- **Service Orchestration** - Can be added to service orchestrator configs

## Next Steps

After successful startup:

1. ✅ Verify all systems are operational
2. ✅ Test R5 API endpoints
3. ✅ Ingest test session to R5
4. ✅ Run V3 verification on test workflow

---

**For more information:**
- `docs/system/V3_R5_VERIFICATION_REPORT.md` - Verification details
- `docs/system/V3_R5_QUICK_REFERENCE.md` - Quick reference guide
- `scripts/python/start_v3_r5_systems.py` - Startup script source

