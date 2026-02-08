# Lumina Sidebar – Skeleton (Cline / Continue Pattern)

**Purpose:** Bare-bones reference for how Cline (and similar CAs) contribute a chat/sidebar so Lumina can match the pattern and avoid the "no data provider" error.

**Last updated:** 2026-02-01

---

## Cline skeleton (from Cline `package.json`)

### 1. Activity bar container

```json
"viewsContainers": {
  "activitybar": [
    {
      "id": "claude-dev-ActivityBar",
      "title": "Cline",
      "icon": "assets/icons/icon.svg"
    }
  ]
}
```

### 2. One webview view in that container

**Critical:** The view must have `"type": "webview"`. Without it, the workbench does **not** call `resolveWebviewView()` and the view stays broken or shows a placeholder.

```json
"views": {
  "claude-dev-ActivityBar": [
    {
      "type": "webview",
      "id": "claude-dev.SidebarProvider",
      "name": "",
      "icon": "assets/icons/icon.svg"
    }
  ]
}
```

### 3. Extension code

- Register a `WebviewViewProvider` for the view id:
  `vscode.window.registerWebviewViewProvider("claude-dev.SidebarProvider", provider)`
- Implement `resolveWebviewView(webviewView, context, token)` and set `webviewView.webview.html` (and options, message handlers, etc.).

---

## Lumina application of the pattern

- **Container:** `lumina` (Activity Bar, icon `$(sparkle)`).
- **View:** One webview view with `"type": "webview"`, id `lumina.welcome`, name `Lumina`.
- **Provider:** `LuminaWelcomeViewProvider` registered for `lumina.welcome`; on visibility or button click, run `jarvis.chat.open` and show welcome HTML.
- **File Cleanup Stack:** Contributed under **Explorer** (not Lumina) so it uses a tree view in the standard Explorer container and avoids the "no data provider" issue in custom containers.

---

## Why the tree view failed in Lumina

- We contributed a **tree view** (`lumina.fileCleanupStack`) in the Lumina container without `type: "webview"`.
- Cursor/VS Code in this setup did not resolve the tree data provider for that container (extension-qualified view id mismatch or timing).
- Moving the tree to **Explorer** and using a **webview** in Lumina (with `"type": "webview"`) follows Cline’s pattern and avoids the error.

---

## Activation (how other CAs do it)

- **Cline:** Uses `onStartupFinished`, `onLanguage`, `workspaceContains:evals.env`. Does **not** use `onView` for the sidebar. Activates soon after startup; `activate()` is async and does heavy init (e.g. `await initialize(context)`) then registers the webview provider. Logs activation time.
- **Other Lumina extensions** (file-auto-close, cursor-active-model-status, lumina-footer-ticker, etc.): All use **`onStartupFinished`** so they activate once the workbench is ready.
- **Lumina Core (aligned with CAs):** Uses **`onStartupFinished`** (like Cline and the other Lumina extensions) so all Lumina commands and status bars are registered from the start; also keeps `onView:lumina.welcome`, `onView:lumina.fileCleanupStack`, and the progress `onCommand` events. Heavy init remains deferred with `setTimeout(runLuminaFullActivation, 300)` so startup doesn't stall; full activation errors are caught and logged.
- **Lumina `activate()`:** Registers the webview provider and `lumina.openJarvisChat`, then defers all other work to `setTimeout(runLuminaFullActivation, 300)` inside try/catch. So `activate()` returns quickly; the sidebar can resolve immediately; heavy init runs 300ms later so startup and first-view open don't block and failures don’t crash the host.

---

## References

- Cline: `package.json` → `viewsContainers`, `views` with `"type": "webview"`, `activationEvents` (onStartupFinished, onLanguage).
- VS Code: [Webview API](https://code.visualstudio.com/api/extension-guides/webview), [Contribution Points – views](https://code.visualstudio.com/api/references/contribution-points), [Activation Events](https://code.visualstudio.com/api/references/activation-events).
- Lumina: `vscode-extensions/lumina-core/package.json`, `src/extension.ts` (LuminaWelcomeViewProvider, runLuminaFullActivation).
