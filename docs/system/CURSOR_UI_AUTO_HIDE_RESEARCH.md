# Cursor IDE UI Auto-Hide Research Results

**Date**: 2026-01-04  
**Status**: 📊 **RESEARCH COMPLETE**  
**Tags**: #CURSOR #UI #AUTO_HIDE #RESEARCH @JARVIS @LUMINA

---

## Executive Summary

**Finding**: Cursor IDE does **not** have built-in auto-hide functionality for header/chat pane. However, since Cursor is based on VS Code, VS Code extension APIs can be used to implement custom UI modifications.

---

## Research Findings

### 1. Cursor IDE Architecture

✅ **Cursor is VS Code-based**
- Cursor IDE is built on VS Code (Electron-based)
- VS Code extension APIs are compatible
- Extension format: `.vsix` files
- Extension manifest: `package.json` with VS Code API

✅ **Existing Extensions in Codebase**
- `lumina-ai.vsix` - Existing Lumina extension
- `cursor_active_model_tracker.py` - Displays model status in UI
- Extensions integrated: Kilo Code, Continue, Cline

### 2. UI Customization Capabilities

❌ **Built-in Auto-Hide: NOT Available**
- No native auto-hide for header bar
- No native auto-hide for chat pane
- Users report challenges hiding UI elements
- Forum discussions indicate limitations

✅ **Available Customization Options**
- **Compact Mode**: Reduces visual clutter (doesn't auto-hide)
- **Chat Settings**: Auto-scroll, fade animations, history visibility
- **Open Chat in Editor**: Moves chat to editor tab
- **Export Chat**: Save conversations as markdown

### 3. Implementation Approaches

#### Approach 1: VS Code Extension API (Recommended)
**Status**: ✅ **FEASIBLE**

**Method**:
- Create VS Code extension (compatible with Cursor)
- Use `vscode.window` API for UI manipulation
- Inject CSS via `vscode.workspace.getConfiguration`
- Use Webview API for custom UI components

**Limitations**:
- Limited access to Cursor-specific UI elements
- May not work for all UI sections
- Requires extension development

**Files Needed**:
- `package.json` (extension manifest)
- `extension.js` (main extension code)
- CSS injection code
- JavaScript for hover behavior

#### Approach 2: User Styles (Quick Fix)
**Status**: ⚠️ **LIMITED**

**Method**:
- Add custom CSS to Cursor settings
- Use browser DevTools to inject JavaScript
- Modify `.cursor/settings.json`

**Limitations**:
- Limited to CSS-only changes
- JavaScript injection requires DevTools
- Not persistent across restarts
- May break with Cursor updates

#### Approach 3: Feature Request
**Status**: ⏳ **LONG-TERM**

**Method**:
- Request feature from Cursor team
- Engage with community forums
- Wait for official implementation

**Timeline**: Unknown (could be months/years)

### 4. Transcription API Research

❌ **No Public Transcription API Found**
- No documented API for transcription control
- No pause/resume API found
- No auto-send API found

✅ **Possible Workarounds**:
- Use VS Code extension API to interact with chat input
- Monitor text input events
- Implement pause/resume logic in extension
- Auto-send via keyboard simulation (limited)

### 5. Button Controls

✅ **Extension API Can Add Buttons**
- VS Code extension API supports custom buttons
- Can add to status bar, command palette
- Can create custom webview with buttons
- Limited to extension-defined locations

❌ **Cannot Modify Existing Buttons**
- Cannot modify Cursor's native buttons
- Cannot add buttons to transcription area directly
- Would need custom UI overlay

---

## Recommended Implementation Strategy

### Phase 1: VS Code Extension (Immediate)
1. **Create Extension Structure**
   - `package.json` with VS Code API
   - `extension.js` for activation
   - CSS injection via configuration

2. **Implement Auto-Hide**
   - Use CSS injection for header/chat pane
   - JavaScript for hover behavior
   - Configuration for delays

3. **Test Compatibility**
   - Verify works in Cursor IDE
   - Test with existing extensions
   - Check for conflicts

### Phase 2: Transcription Improvements (Medium-term)
1. **Extension API Integration**
   - Monitor chat input events
   - Implement pause/resume logic
   - Auto-send after silence

2. **Custom UI Overlay**
   - Create webview with expanded buttons
   - Overlay on transcription area
   - Integrate with chat input

### Phase 3: Feature Request (Long-term)
1. **Community Engagement**
   - Post feature request on Cursor forums
   - Gather user support
   - Track official updates

---

## Technical Details

### VS Code Extension API

**Available APIs**:
```javascript
// CSS Injection
vscode.workspace.getConfiguration().update('workbench.colorCustomizations', {...});

// Webview API
vscode.window.createWebviewPanel(...);

// Status Bar
vscode.window.createStatusBarItem(...);

// Commands
vscode.commands.registerCommand(...);
```

**Limitations**:
- Cannot directly modify Cursor's UI DOM
- Limited to extension-defined areas
- CSS injection may not persist

### CSS Injection Method

**User Settings Approach**:
```json
{
  "workbench.colorCustomizations": {
    "titleBar.activeBackground": "#00000000"
  }
}
```

**Extension Approach**:
- Inject CSS via webview
- Use `vscode.workspace.getConfiguration`
- May require extension restart

---

## Next Steps

### Immediate Actions
1. ✅ Research complete
2. ⏳ Create VS Code extension structure
3. ⏳ Implement CSS injection
4. ⏳ Test in Cursor IDE

### Medium-term Actions
1. ⏳ Implement transcription pause/resume
2. ⏳ Add expanded button controls
3. ⏳ Create custom UI overlay

### Long-term Actions
1. ⏳ Submit feature request to Cursor team
2. ⏳ Engage with community
3. ⏳ Monitor official updates

---

## Resources

### Documentation
- [VS Code Extension API](https://code.visualstudio.com/api)
- [Cursor IDE Documentation](https://docs.cursor.com)
- [Cursor Forum](https://forum.cursor.com)

### Community Tools
- [Cursor Workspace Configurator](https://github.com/fisapool/cursor-workspace-configurator)
- Existing extensions: Kilo Code, Continue, Cline

### Codebase References
- `config/lumina_extensions_integration.json` - Extension config
- `scripts/python/cursor_active_model_tracker.py` - UI integration example
- `lumina-ai.vsix` - Existing extension file

---

## Conclusion

**Feasibility**: ✅ **MODERATE**

- **Auto-hide UI**: Possible via VS Code extension (limited)
- **Transcription improvements**: Possible via extension API (workarounds needed)
- **Button controls**: Possible via custom webview (overlay approach)

**Recommendation**: Proceed with VS Code extension development, understanding limitations and using workarounds where needed.

---

**Tags**: #CURSOR #UI #AUTO_HIDE #RESEARCH #VS_CODE_EXTENSION @JARVIS @LUMINA
