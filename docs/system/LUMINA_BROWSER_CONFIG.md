# Lumina Browser Configuration

## Overview

The Lumina project uses **Neo browser** as the preferred browser for all operations. Chrome should **NOT** be used.

## Source of Truth

**File:** `config/lumina_browser_config.json`

## Preferred Browser

- **Primary Browser:** Neo
- **Executable:** `neo.exe`
- **Priority:** 1 (Highest)

## Excluded Browsers

The following browsers should **NOT** be used:
- Chrome
- chrome.exe
- Google Chrome

## Configuration

### Browser Tools

1. **MCP Browser Extension**
   - Enabled: Yes
   - Preferred Browser: Neo
   - Location: MCP cursor-browser-extension server

2. **Roo Code Browser Tool**
   - Enabled: Yes
   - Preferred Browser: Neo
   - Viewport Size: 1280x800

### User Agent

Default user agent string for Neo browser:
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Neo/1.0 Safari/537.36
```

### Protected Processes

- **Protected:** `neo.exe`
- **Excluded:** `chrome.exe`, `brave.exe`

## Usage

When using browser tools or extensions:
1. Ensure Neo browser is installed
2. Configure tools to use Neo instead of Chrome
3. Update any scripts that reference Chrome to use Neo

## Related Files

- `config/lumina_browser_config.json` - Browser configuration SSoT
- `config/kilo_code_optimized_config.json` - Kilo Code configuration
- `cedarbrook-financial-services_llc-env/roo-code-extension/roo-code-settings.json` - Roo Code settings

---

**Remember:** Always use Neo browser, never Chrome.

