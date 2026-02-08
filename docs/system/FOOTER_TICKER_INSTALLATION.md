# LUMINA Core Footer Ticker Banner - Installation Guide

**Date:** 2026-01-09
**Component:** LUMINA Core
**Tags:** #JARVIS @LUMINA #LUMINA_CORE #INSTALLATION

---

## Installation Steps

### 1. Install Extension Dependencies

```bash
cd vscode-extensions/lumina-footer-ticker
npm install
```

### 2. Compile Extension

```bash
npm run compile
```

### 3. Activate in Cursor IDE

1. Open Cursor IDE
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Reload Window"
4. Select "Developer: Reload Window"
5. Extension will activate automatically

### 4. Verify Installation

- Check status bar for ticker banner
- Should see rotating footer items
- Click to pause/resume

---

## Configuration

### Auto-Generated Config

Configuration file will be created at:
`config/footer_ticker_config.json`

### Manual Configuration

Edit `config/footer_ticker_config.json`:

```json
{
  "scroll_speed": 30,
  "item_spacing": 50,
  "loop": true,
  "pause_on_hover": true,
  "items": [...]
}
```

### Cursor IDE Settings

Open Cursor settings (`Ctrl+,`) and search for "lumina":

- `lumina.footerTicker.enabled` - Enable/disable
- `lumina.footerTicker.scrollSpeed` - Scroll speed
- `lumina.footerTicker.itemSpacing` - Item spacing
- `lumina.footerTicker.pauseOnHover` - Pause on hover

---

## Troubleshooting

### Extension Not Loading

1. Check `out/extension.js` exists
2. Verify compilation succeeded
3. Check Cursor IDE Developer Console for errors
4. Reload window

### Ticker Not Showing

1. Verify extension is enabled in settings
2. Check `lumina.footerTicker.enabled` is `true`
3. Verify configuration file exists
4. Check status bar is visible

### Performance Issues

1. Reduce scroll speed
2. Reduce number of items
3. Increase item spacing
4. Disable pause on hover

---

## Status

**Installation:** In progress
**Extension:** Ready to compile
**Configuration:** Auto-generated
**Activation:** Requires Cursor IDE reload

---

**Tags:** #JARVIS @LUMINA #LUMINA_CORE #INSTALLATION
