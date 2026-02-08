# Lumina Single Source of Truth (SSoT) Registry

## Overview

This document provides a central registry of all Single Source of Truth (SSoT) configuration files for the Lumina project. All SSoT files are located in the `config/` directory and follow a consistent structure.

## SSoT Files

### 1. VS Code Extensions
**File:** `config/lumina_vscode_extensions.json`  
**Type:** Extensions  
**Status:** Active  
**Documentation:** [LUMINA_VSCODE_EXTENSIONS_SSOT.md](./LUMINA_VSCODE_EXTENSIONS_SSOT.md)

**Purpose:** Defines all required VS Code/Cursor marketplace extensions for the Lumina project.

**Consumers:**
- `.vscode/extensions.json` - Workspace recommendations
- `scripts/powershell/Install-LuminaExtensions.ps1` - Installation script

**Key Information:**
- 24 required extensions
- Organized by category (Python, JavaScript, Data, Docker, Git, Productivity, Remote)
- Excludes 2 non-existent extensions

---

### 2. Python Configuration
**File:** `config/lumina_python_config.json`  
**Type:** Runtime  
**Status:** Active  
**Documentation:** `docs/system/LUMINA_PYTHON_CONFIG.md` (to be created)

**Purpose:** Defines Python version requirements and virtual environment configuration.

**Consumers:**
- `.python-version` - Python version specification
- `pyproject.toml` - Project Python requirements
- `scripts/powershell/Setup-LuminaVenv.ps1` - Venv setup script

**Key Information:**
- Recommended: Python 3.11.9
- Minimum: Python 3.11.6
- Version spec: `>=3.11.6,<3.12.0`
- Venv location: `venv/`

---

### 3. Browser Configuration
**File:** `config/lumina_browser_config.json`  
**Type:** Tooling  
**Status:** Active  
**Documentation:** [LUMINA_BROWSER_CONFIG.md](./LUMINA_BROWSER_CONFIG.md)

**Purpose:** Defines browser preferences and configuration for Lumina project operations.

**Consumers:**
- `cedarbrook-financial-services_llc-env/demonstrate_llm_training.py`
- `cedarbrook-financial-services_llc-env/llm_trainer_with_process_lasso.py`
- `cedarbrook-financial-services_llc-env/roo-code-extension/roo-code-settings.json`

**Key Information:**
- Preferred Browser: Neo (`neo.exe`)
- Excluded Browsers: Chrome, chrome.exe, Google Chrome, Brave
- Protected Processes: `neo.exe`
- User Agent: Neo-specific user agent string

---

## Related Configuration Files

These files are not SSoT but are related to Lumina configuration:

1. **`config/lumina_ide_integration.json`** - IDE integration settings
2. **`config/lumina_extensions_integration.json`** - Lumina extensions integration
3. **`config/lumina_jarvis_content_index.json`** - JARVIS content indexing

## Standards

- **Python Version:** 3.11.9 (minimum 3.11.6)
- **Preferred Browser:** Neo
- **Excluded Browser:** Chrome
- **Virtual Environment:** `venv/` directory
- **Configuration Location:** `config/` directory

## SSoT File Structure

All SSoT files follow this structure:

```json
{
  "version": "1.0.0",
  "name": "...",
  "description": "...",
  "last_updated": "YYYY-MM-DD",
  "ssot": true,
  "ssot_location": "config/...",
  "_metadata": {
    "documentation": "docs/system/...",
    "references": [...],
    "deprecated_sources": [...]
  }
}
```

## Adding New SSoT Files

When creating a new SSoT file:

1. Create the file in `config/` directory
2. Follow the standard SSoT structure
3. Set `"ssot": true`
4. Add documentation in `docs/system/`
5. Update this registry
6. Update any consumers to reference the SSoT

## Validation

To validate SSoT files:

```powershell
# Check all SSoT files have ssot flag
Get-ChildItem config/lumina_*.json | ForEach-Object {
    $content = Get-Content $_.FullName | ConvertFrom-Json
    if ($content.ssot -ne $true) {
        Write-Host "WARNING: $($_.Name) missing ssot flag" -ForegroundColor Yellow
    }
}
```

## Maintenance

- **Review Frequency:** Quarterly
- **Owner:** Lumina Project Team
- **Version Control:** All SSoT files tracked in Git
- **Backup:** Included in project backups

---

**Last Updated:** 2025-01-24  
**Registry Version:** 1.0.0

