# Lumina VS Code Extensions - Single Source of Truth (SSoT)

## Overview

This document defines the **Single Source of Truth (SSoT)** for all VS Code/Cursor marketplace extensions required for the Lumina project.

## Source of Truth Location

**File:** `config/lumina_vscode_extensions.json`

**Path:** `D:\Dropbox\my_projects\config\lumina_vscode_extensions.json`

## Purpose

This file is the **ONLY** authoritative source for:
- Required VS Code/Cursor extensions
- Extension categories and organization
- Excluded extensions and reasons
- Extension metadata

## Files That Reference SSoT

### Primary Consumers

1. **`.vscode/extensions.json`**
   - VS Code/Cursor workspace recommendations
   - Auto-generated from SSoT
   - Used by IDE to prompt users to install extensions

2. **`scripts/powershell/Install-LuminaExtensions.ps1`**
   - Automated extension installation script
   - Reads directly from SSoT
   - Falls back to hardcoded list if SSoT unavailable

### Deprecated Sources (DO NOT USE)

The following files contain **OLD** extension lists and should **NOT** be used:

- `cfs-llc-env/scripts/python/standardize_vscode_extensions.py`
- `cedarbrook-financial-services_llc-env/scripts/python/standardize_vscode_extensions.py`
- `cfs-llc-env/scripts/python/list_extensions.py`
- `cedarbrook-financial-services_llc-env/scripts/python/list_extensions.py`

These are legacy files from older project versions and are maintained for historical reference only.

## Extension Categories

The SSoT organizes extensions into the following categories:

1. **Python Development** (7 extensions)
2. **JavaScript/TypeScript Support** (3 extensions)
3. **Data Analysis Tools** (3 extensions)
4. **Docker Support** (2 extensions)
5. **Git Integration** (3 extensions)
6. **Productivity Tools** (5 extensions)
7. **Remote Development** (1 extension)

**Total: 24 extensions**

## Excluded Extensions

The following extensions are explicitly excluded with documented reasons:

1. `visualstudioexptteam.vscodeintellicode`
   - **Reason:** Not available in Cursor marketplace
   - **Alternatives:** None

2. `ms-vscode-remote.remote-ssh-edit`
   - **Reason:** Extension does not exist as separate package
   - **Alternatives:** `ms-vscode-remote.remote-ssh`

## Usage

### Reading from SSoT

**PowerShell:**
```powershell
$config = Get-Content "config/lumina_vscode_extensions.json" | ConvertFrom-Json
$extensions = $config.all_extensions
```

**Python:**
```python
import json
from pathlib import Path

ssot_path = Path("config/lumina_vscode_extensions.json")
with open(ssot_path) as f:
    config = json.load(f)
    extensions = config["all_extensions"]
```

### Updating SSoT

1. **Edit** `config/lumina_vscode_extensions.json`
2. **Update** `last_updated` field in `_metadata`
3. **Regenerate** dependent files if needed:
   - `.vscode/extensions.json` (if using auto-generation)
   - Run `Install-LuminaExtensions.ps1` to verify

### Adding New Extensions

1. Add extension ID to appropriate category in `extensions` section
2. Add extension ID to `all_extensions` array
3. Update `last_updated` timestamp
4. Test installation with `Install-LuminaExtensions.ps1`

### Removing Extensions

1. Remove from category in `extensions` section
2. Remove from `all_extensions` array
3. If excluded for a reason, add to `notes.excluded_extensions`
4. Update `last_updated` timestamp

## Validation

To validate the SSoT:

```powershell
# Validate JSON structure
Get-Content config/lumina_vscode_extensions.json | ConvertFrom-Json | Out-Null
if ($?) { Write-Host "✓ Valid JSON" } else { Write-Host "✗ Invalid JSON" }

# Count extensions
$config = Get-Content config/lumina_vscode_extensions.json | ConvertFrom-Json
Write-Host "Total extensions: $($config.all_extensions.Count)"
```

## Maintenance

- **Owner:** Lumina Project Team
- **Review Frequency:** Quarterly or when new extensions are needed
- **Version Control:** Tracked in Git
- **Backup:** Included in project backups

## Related Documentation

- [VS Code Extension Management Guide](../cedarbrook-financial-services_llc-env/documents/markdown/vscode_extension_management_guide.md) - General extension management
- [Lumina IDE Integration](../config/lumina_ide_integration.json) - IDE integration configuration

## Change Log

- **2025-01-24:** Initial SSoT creation
  - Migrated from legacy `cfs-llc-env` scripts
  - Established `config/lumina_vscode_extensions.json` as SSoT
  - Removed 2 non-existent extensions
  - Documented excluded extensions

---

**Remember:** This is the SINGLE SOURCE OF TRUTH. All extension lists must reference this file.

