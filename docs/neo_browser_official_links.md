# Neo Browser Official Links & Documentation

## Browser Information

**Browser Name:** Norton Neo  
**Company:** Gen Digital Inc (parent company of Norton)  
**Version:** 143.0.1736.170  
**Type:** AI-Native Browser (Chromium-based)  
**Location:** `C:\Users\mlesn\AppData\Local\Neo\Application\neo.exe`

---

## Official Direct Links

### Main Website & Download
- **Official Homepage:** https://neotoday.ai/
- **Download:** https://neotoday.ai/ (Free worldwide as of December 2025)

### Press Release & Announcement
- **Official Announcement:** https://www.prnewswire.com/news-releases/norton-neo-the-worlds-first-safe-ai-native-browser-now-available-for-free-worldwide-302630253.html

### Company Information
- **Gen Digital Inc:** https://www.gendigital.com/
- **Norton Products:** https://www.norton.com/

### Mobile Apps (Related)
- **iOS App Store:** https://apps.apple.com/us/app/neo-browser/id6752797120
- **Android (APK):** https://apkpure.com/neo-browser/com.dpns.browser

---

## Browser Features

- **AI-Native Browser** - Enhanced with AI capabilities
- **Unified Search & Chat** - Integrated AI assistant
- **Smart Tab Management** - Intelligent tab organization  
- **Built-in Ad Blocking** - Enhanced privacy and performance
- **Safety Features** - Norton security integration
- **Free Worldwide** - Available globally as of December 2025

---

## For LUMINA Integration

### Current Usage
1. **ElevenLabs Setup** - Opening ElevenLabs website for API key retrieval
2. **Cookie Extraction** - Accessing browser cookies for authentication (`extract_neo_cookies_for_idm.py`)
3. **Web Automation** - Launching websites programmatically

### Programmatic Access
```python
# Launch Neo Browser
neo_exe = r"C:\Users\mlesn\AppData\Local\Neo\Application\neo.exe"
subprocess.Popen([neo_exe, "https://example.com"])
```

### Cookies Location
- **Cookies Database:** `%LOCALAPPDATA%\Neo\User Data\Default\Cookies`
- **User Data:** `%LOCALAPPDATA%\Neo\User Data\Default`

### Automation Notes
- Chromium-based (supports Chrome DevTools Protocol)
- Can be controlled via browser automation tools
- Supports standard Chromium command-line flags
- Update service: `https://clients2.google.com/service/update2/crx`

---

## Technical Details

- **Base:** Chromium 143.x
- **Update Channel:** Chrome update service
- **Auto-Updates:** Enabled by default
- **Company:** Gen Digital Inc (formerly NortonLifeLock)

---

**Last Updated:** 2025-01-30  
**Source:** Executable metadata + Official press release + Web search
