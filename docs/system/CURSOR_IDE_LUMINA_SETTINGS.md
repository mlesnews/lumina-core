# Cursor IDE / VS Code Settings for LUMINA
## Custom-Tailored Configuration with SYPHON White/Black-Listing

**Date:** 2026-01-09
**Status:** ✅ **COMPLETE CONFIGURATION**
**Version:** 1.0

---

## 🎯 OVERVIEW

This document describes the custom-tailored Cursor IDE and VS Code settings specifically configured for the LUMINA project, including SYPHON white/black-listing strategies.

---

## 📁 CONFIGURATION FILES

### 1. `.vscode/settings.json`
**Purpose:** VS Code workspace settings
**Location:** `.vscode/settings.json`
**Status:** ✅ Created

### 2. `config/syphon_whitelist_blacklist.json`
**Purpose:** SYPHON white/black-listing configuration
**Location:** `config/syphon_whitelist_blacklist.json`
**Status:** ✅ Created

### 3. `.cursorrules`
**Purpose:** Cursor IDE rules (already exists)
**Location:** `.cursorrules`
**Status:** ✅ Existing

---

## 🔍 SYPHON WHITE/BLACK-LISTING STRATEGIES

### SYPHON Definition
- **SYPHON** = `#syphon` - Lower ranked alias for `@grep`
- **Precedence:** 2 (vs @grep precedence: 1)
- **Usage:** Pattern matching and search operations
- **Context Weight:** 0.8
- **AI Weight:** 0.8
- **Human Weight:** 0.2

### Whitelist Strategy (Always Include)

#### Files/Patterns:
```
**/scripts/python/**/*.py
**/config/**/*.json
**/docs/**/*.md
**/.cursorrules
**/data/todo/**/*.json
**/data/system/**/*.json
**/data/god_loop/**/*.json
**/data/gitlens_followup_automation/**/*.json
**/data/retry_manager_diagnostics/**/*.json
**/docker/**/*.py
**/docker/**/*.yml
```

#### Directories:
- `scripts/python`
- `config`
- `docs`
- `docker`
- `data/todo`
- `data/system`
- `data/god_loop`
- `data/gitlens_followup_automation`
- `data/retry_manager_diagnostics`

#### File Extensions:
- `.py` (Python)
- `.json` (Configuration/Data)
- `.md` (Documentation)
- `.yml`, `.yaml` (Docker/Config)
- `.sh`, `.ps1` (Scripts)

### Blacklist Strategy (Always Exclude)

#### Files/Patterns:
```
**/node_modules/**
**/__pycache__/**
**/*.pyc
**/.pytest_cache/**
**/venv/**
**/.venv/**
**/env/**
**/.env
**/dist/**
**/build/**
**/*.egg-info/**
**/.mypy_cache/**
**/.ruff_cache/**
**/data/local_backup/**
**/data/**/*.encrypted
**/archive/**
**/certificates/**
**/HKLM/**
**/.cursor/**
**/.git/**
```

#### Directories:
- `node_modules`
- `__pycache__`
- `.pytest_cache`
- `venv`, `.venv`, `env`
- `dist`, `build`
- `.mypy_cache`, `.ruff_cache`
- `data/local_backup`
- `archive`
- `certificates`
- `HKLM`
- `.cursor`
- `.git`

#### File Extensions:
- `.pyc`, `.pyo`, `.pyd` (Compiled Python)
- `.encrypted` (Encrypted files)
- `.log`, `.tmp`, `.temp` (Temporary files)
- `.bak`, `.backup` (Backup files)
- `.swp`, `.swo` (Editor swap files)

---

## ⚙️ CURSOR IDE SPECIFIC SETTINGS

### AI Context Settings

#### Exclusions (Blacklist):
```json
"cursor.aiContextExclude": [
  "**/node_modules/**",
  "**/__pycache__/**",
  "**/*.pyc",
  "**/.pytest_cache/**",
  "**/venv/**",
  "**/data/local_backup/**",
  "**/archive/**",
  "**/.git/**"
]
```

#### Inclusions (Whitelist):
```json
"cursor.aiContextInclude": [
  "**/scripts/python/**/*.py",
  "**/config/**/*.json",
  "**/docs/**/*.md",
  "**/.cursorrules",
  "**/data/todo/**/*.json",
  "**/data/system/**/*.json"
]
```

#### Limits:
- **Max Context Size:** 1MB (1,000,000 bytes)
- **Max Files:** 50 files
- **Max Context Length (Chat):** 100,000 characters

### Composer Settings
```json
"cursor.composer.enabled": true,
"cursor.composer.maxFiles": 50,
"cursor.composer.maxContextSize": 1000000
```

### Agent Settings
```json
"cursor.agent.enabled": true,
"cursor.agent.maxSteps": 50,
"cursor.agent.timeout": 300000  // 5 minutes
```

---

## 🔎 SEARCH SETTINGS

### Search Exclusions (Blacklist):
```json
"search.exclude": {
  "**/node_modules": true,
  "**/__pycache__": true,
  "**/*.pyc": true,
  "**/venv": true,
  "**/data/local_backup": true,
  "**/archive": true,
  "**/.git": true
}
```

### Search Inclusions (Whitelist):
- Explicitly includes important directories
- Uses `search.useIgnoreFiles: true`
- Follows `.gitignore` patterns

---

## 📂 FILE EXPLORER SETTINGS

### File Nesting:
```json
"explorer.fileNesting.patterns": {
  "*.py": "${capture}.pyc, ${capture}.pyo, ${capture}.pyd, __pycache__",
  "*.json": "${capture}.json.bak, ${capture}.json.backup",
  "*.md": "${capture}.md.bak, ${capture}.md.backup",
  ".cursorrules": ".cursorrules.bak",
  "docker-compose.yml": "docker-compose.*.yml, Dockerfile, .dockerignore"
}
```

### Sort Order:
- **Type:** Files sorted by type
- **Confirm Delete:** Enabled
- **Confirm Drag & Drop:** Enabled

---

## 🐍 PYTHON SETTINGS

### Analysis:
```json
"python.analysis.exclude": [
  "**/node_modules",
  "**/venv",
  "**/__pycache__",
  "**/data/local_backup",
  "**/archive"
],
"python.analysis.include": [
  "scripts/python",
  "config",
  "docker"
]
```

### Linting:
- **Pylint:** Disabled
- **Flake8:** Enabled
- **MyPy:** Enabled

### Formatting:
- **Provider:** Black
- **Line Length:** 100 characters

### Testing:
- **Pytest:** Enabled
- **Unittest:** Disabled

---

## 🔄 INTEGRATION WITH AI GUIDANCE FRAMEWORK

### SYPHON Integration:
```json
"lumina.syphon.enabled": true,
"lumina.syphon.patterns": [
  "**/scripts/python/**",
  "**/config/**",
  "**/docs/**",
  "**/.cursorrules"
],
"lumina.syphon.exclude": [
  "**/node_modules/**",
  "**/__pycache__/**",
  "**/venv/**",
  "**/data/local_backup/**",
  "**/archive/**"
]
```

### JARVIS Integration:
```json
"lumina.jarvis.enabled": true,
"lumina.jarvis.autoDetect": true
```

### R5 Integration:
```json
"lumina.r5.enabled": true,
"lumina.r5.autoAggregate": true
```

### V3 Integration:
```json
"lumina.v3.enabled": true,
"lumina.v3.autoVerify": true
```

---

## 📊 SETTINGS SUMMARY

### File Exclusions:
- ✅ **Files Exclude:** 20+ patterns
- ✅ **File Watcher Exclude:** 15+ patterns
- ✅ **Search Exclude:** 20+ patterns
- ✅ **AI Context Exclude:** 10+ patterns

### File Inclusions:
- ✅ **AI Context Include:** 6+ patterns
- ✅ **Search Include:** Implicit (via whitelist)
- ✅ **Python Analysis Include:** 3 directories

### Performance:
- ✅ **AI Context Max Size:** 1MB
- ✅ **AI Context Max Files:** 50
- ✅ **Composer Max Files:** 50
- ✅ **Agent Max Steps:** 50
- ✅ **Agent Timeout:** 5 minutes

---

## 🎯 USAGE

### For Users:
1. Settings are automatically applied when opening workspace
2. SYPHON whitelist/blacklist is enforced automatically
3. AI context follows whitelist/blacklist rules
4. Search operations respect exclusions

### For AI:
1. Check `.vscode/settings.json` for workspace settings
2. Check `config/syphon_whitelist_blacklist.json` for SYPHON rules
3. Respect whitelist/blacklist when performing operations
4. Use SYPHON patterns for lower-priority searches
5. Use @grep for high-priority pattern searches

---

## 🔧 MAINTENANCE

### Updating Whitelist:
1. Edit `config/syphon_whitelist_blacklist.json`
2. Add patterns to `whitelist.patterns`
3. Sync with `.vscode/settings.json` if needed

### Updating Blacklist:
1. Edit `config/syphon_whitelist_blacklist.json`
2. Add patterns to `blacklist.patterns`
3. Sync with `.vscode/settings.json` if needed

### Syncing Settings:
- Settings auto-sync when `config/syphon_whitelist_blacklist.json` changes
- Manual sync: Update `.vscode/settings.json` manually

---

## 📚 RELATED DOCUMENTATION

- **AI Guidance Framework:** `AI_GUIDANCE_COMPLETE_FRAMEWORK.md`
- **Command Patterns:** `COMMAND_PATTERNS_REFERENCE.md`
- **SYPHON Config:** `config/syphon_whitelist_blacklist.json`
- **VS Code Settings:** `.vscode/settings.json`
- **Cursor Rules:** `.cursorrules`

---

**Tags:** #CURSOR_IDE #VSCODE #SETTINGS #SYPHON #WHITELIST #BLACKLIST #LUMINA @JARVIS @LUMINA

**Status:** ✅ **COMPLETE CONFIGURATION - READY FOR USE**
