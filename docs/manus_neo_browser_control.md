# MANUS-NEO Browser Full Control System (Hybrid Approach)

## Overview

MANUS now has **complete control** over NEO browser using a hybrid multi-method approach. This gives maximum flexibility and reliability for browser automation tasks.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              MANUS-NEO Browser Control System               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  METHOD 1: PROCESS CONTROL                                  │
│  ├── Direct executable launch                               │
│  ├── Process management (start/stop/monitor)               │
│  └── Command-line arguments                                 │
│                                                              │
│  METHOD 2: CHROME DEVBTOOLS PROTOCOL (CDP)                  │
│  ├── Full browser automation                                │
│  ├── JavaScript execution                                   │
│  ├── Page navigation & interaction                          │
│  └── Network & cookie management                            │
│                                                              │
│  METHOD 3: FILE SYSTEM ACCESS                               │
│  ├── Cookie extraction (SQLite database)                    │
│  ├── Browser history                                        │
│  ├── Preferences/settings                                   │
│  └── User data access                                       │
│                                                              │
│  METHOD 4: HIGH-LEVEL AUTOMATION                            │
│  ├── Form filling                                           │
│  ├── Website signup automation                              │
│  ├── API key extraction                                     │
│  └── Task orchestration                                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. `manus_neo_browser_control.py`

**Full control system** with all methods:

```python
from manus_neo_browser_control import MANUSNEOBrowserControl

browser = MANUSNEOBrowserControl(headless=False)

# Launch browser
browser.launch("https://elevenlabs.io")

# Navigate
browser.navigate("https://elevenlabs.io/app/settings/api-keys")

# Execute JavaScript
result = browser.execute_script("document.title")

# Get cookies
cookies = browser.get_cookies(domain="elevenlabs.io")

# Get browser history
history = browser.get_browser_history(limit=100)

# Close
browser.close()
```

### 2. `manus_neo_integration.py`

**High-level integration layer** for MANUS:

```python
from manus_neo_integration import MANUSNEOIntegration

integration = MANUSNEOIntegration()

# Simple operations
integration.open_website("https://elevenlabs.io")
cookies = integration.get_cookies_for_domain("elevenlabs.io")

# Automated tasks
result = integration.automate_elevenlabs_setup()
```

---

## Control Methods

### Method 1: Process Control

**Direct executable management:**

- Launch NEO with custom arguments
- Monitor process status
- Graceful shutdown or force kill
- Multiple profiles support

**Use cases:**
- Starting browser with specific settings
- Launching with remote debugging enabled
- Profile management

### Method 2: Chrome DevTools Protocol (CDP)

**Full browser automation:**

- Navigate to URLs
- Execute JavaScript
- Interact with page elements
- Network monitoring
- Cookie management
- Screenshot capture

**Use cases:**
- Form filling
- Button clicking
- Data extraction
- Dynamic content interaction

### Method 3: File System Access

**Direct data access:**

- Read cookies from SQLite database
- Extract browser history
- Read/write preferences
- Access user data files

**Use cases:**
- Cookie extraction for authentication
- History analysis
- Settings backup/restore
- Data migration

### Method 4: High-Level Automation

**Combined operations:**

- Website signup automation
- API key extraction
- Form submission
- Multi-step workflows

**Use cases:**
- ElevenLabs API key setup
- Account creation workflows
- Automated testing

---

## Usage Examples

### Example 1: Basic Browser Control

```python
from manus_neo_browser_control import MANUSNEOBrowserControl

browser = MANUSNEOBrowserControl()

# Launch and navigate
browser.launch("https://example.com")
time.sleep(3)

# Get page info
info = browser.get_page_info()
print(f"Title: {info.get('title')}")

# Close
browser.close()
```

### Example 2: Cookie Extraction

```python
# Launch browser
browser.launch()
time.sleep(2)

# Extract cookies
cookies = browser.get_cookies(domain="elevenlabs.io")

for cookie in cookies:
    print(f"{cookie['name']}: {cookie['value']}")
```

### Example 3: Automated ElevenLabs Setup

```python
from manus_neo_integration import MANUSNEOIntegration

integration = MANUSNEOIntegration()

# Automate setup
result = integration.automate_elevenlabs_setup()

if result.get("success"):
    print(f"API Key: {result['api_key']}")
```

### Example 4: JavaScript Execution

```python
browser.launch("https://example.com")
time.sleep(3)

# Execute JavaScript
title = browser.execute_script("return document.title")
print(f"Page title: {title}")

# Fill form field
browser.execute_script("""
    document.querySelector('input[name="email"]').value = 'test@example.com';
""")
```

---

## Command Line Interface

### Basic Operations

```bash
# Launch browser
python scripts/python/manus_neo_browser_control.py --launch "https://elevenlabs.io"

# Extract cookies
python scripts/python/manus_neo_browser_control.py --cookies "elevenlabs.io"

# Get browser history
python scripts/python/manus_neo_browser_control.py --history 20

# Test all methods
python scripts/python/manus_neo_browser_control.py --test
```

### Integration Layer

```bash
# Open website
python scripts/python/manus_neo_integration.py --open "https://elevenlabs.io"

# Get cookies
python scripts/python/manus_neo_integration.py --cookies "elevenlabs.io"

# Automated ElevenLabs setup
python scripts/python/manus_neo_integration.py --elevenlabs
```

---

## Technical Details

### NEO Browser Paths

- **Executable:** `%LOCALAPPDATA%\Neo\Application\neo.exe`
- **User Data:** `%LOCALAPPDATA%\Neo\User Data`
- **Cookies:** `%LOCALAPPDATA%\Neo\User Data\Default\Cookies`
- **History:** `%LOCALAPPDATA%\Neo\User Data\Default\History`
- **Preferences:** `%LOCALAPPDATA%\Neo\User Data\Default\Preferences`

### Chrome DevTools Protocol

- **Port:** 9222 (default)
- **Endpoint:** `http://localhost:9222`
- **Session:** Auto-detected or manually specified

### Command-Line Arguments

Common NEO/Chromium arguments:
- `--remote-debugging-port=9222` - Enable CDP
- `--user-data-dir=<path>` - User data directory
- `--profile-directory=Default` - Profile to use
- `--headless=new` - Headless mode
- `--disable-web-security` - Disable CORS (for automation)

---

## Integration with MANUS

MANUS can use this system for:

1. **Website Automation**
   - Form filling
   - Button clicking
   - Data extraction

2. **Authentication Management**
   - Cookie extraction
   - Session management
   - Token retrieval

3. **API Key Setup**
   - Automated signup workflows
   - API key extraction
   - Credential storage

4. **Web Scraping**
   - Dynamic content extraction
   - JavaScript-rendered pages
   - Screenshot capture

5. **Testing & Monitoring**
   - Website status checks
   - Content verification
   - Performance monitoring

---

## Advantages of Hybrid Approach

✅ **Reliability** - Multiple methods = fallback options  
✅ **Flexibility** - Choose best method for each task  
✅ **Performance** - Direct file access is fastest  
✅ **Control** - Process management gives full control  
✅ **Automation** - CDP enables complex interactions  
✅ **Data Access** - File system access for offline data  

---

## Dependencies

- **Python:** 3.8+
- **requests:** For CDP communication
- **sqlite3:** Built-in, for cookie/history access
- **subprocess:** Built-in, for process control
- **shutil:** Built-in, for file operations

**No external browser automation libraries required!**  
(Works directly with NEO's Chromium-based architecture)

---

## Future Enhancements

- [ ] Playwright integration (optional)
- [ ] Selenium integration (optional)
- [ ] Screenshot capture
- [ ] Video recording
- [ ] Network request interception
- [ ] Proxy support
- [ ] Multi-profile management
- [ ] Session persistence

---

**Last Updated:** 2025-01-30  
**Status:** OPERATIONAL  
**Version:** 1.0

