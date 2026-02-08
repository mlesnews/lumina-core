# Lumina Extensions — VSIX Only (No Marketplace Until Prod-Ready)

**Policy**: We do **not** publish Lumina extensions to any marketplace until they are prod-ready. Install **only** via the built `.vsix` file (BDA).

- **Cursor rule**: `.cursor/rules/no_publish_lumina_extensions.mdc` — always applied; agents must never suggest or run `vsce publish` for Lumina.
- **Why this matters / root cause**: See [LUMINA_EXTENSION_NEVER_PUBLISH_WHY.md](LUMINA_EXTENSION_NEVER_PUBLISH_WHY.md) (5W1H and safeguards).

---

## Do not publish

- **Do not** run `vsce publish` or `npx vsce publish` for Lumina Core, Lumina Premium, or any Lumina-branded extension.
- **Do not** publish to Open VSX, VS Code Marketplace, or Cursor marketplace until the extension is production-ready and we explicitly decide to publish.

---

## Install only via VSIX

- **Build**: `npx vsce package` (produces `lumina-core-2.0.0.vsix` or current version).
- **Install**: `cursor --install-extension path/to/lumina-core-2.0.0.vsix --force`.
- **One command**: Run BDA — see [LUMINA_EXTENSION_BDA.md](LUMINA_EXTENSION_BDA.md).

---

## If extensions are already on the marketplace (remove them)

If any Lumina extension appears in the marketplace (e.g. when you search "LUMINA"), they were published at some point. **Remove from ALL sources** — see [REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md](REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md) for the full checklist (VS Code Marketplace, Open VSX, Cursor) and all five extension IDs. Summary:

### VS Code Marketplace — CLI (fastest if you have vsce auth)

From a terminal where you can enter credentials or have a token:

```powershell
# One-time: log in as publisher (prompts for PAT)
npx vsce login lumina

# Then run the unpublish script from repo root:
.\vscode-extensions\unpublish_lumina_from_marketplace.ps1
```

Or unpublish manually per extension:

```powershell
cd vscode-extensions\lumina-core
npx vsce unpublish lumina.lumina-core

cd ..\lumina-premium
npx vsce unpublish lumina.lumina-premium
```

You need a [Personal Access Token](https://dev.azure.com) with **Marketplace (Publish)** scope for the publisher "lumina" when `vsce login lumina` prompts.

### Open VSX (open-vsx.org)

1. Go to [open-vsx.org](https://open-vsx.org) and sign in with the publisher account (e.g. "lumina").
2. Open the publisher namespace and find each Lumina extension.
3. Use the option to **Unpublish** or **Remove** each extension so they no longer appear in search.

### VS Code Marketplace — Web UI (if CLI fails)

1. Go to the [Visual Studio Marketplace publisher management](https://marketplace.visualstudio.com/manage).
2. Sign in and find each Lumina extension.
3. Unpublish or remove each so they are no longer listed.

### Cursor

- Cursor may list extensions from Open VSX or its own index. After unpublishing from Open VSX (and VS Code Marketplace if applicable), Cursor’s list should stop showing them once caches refresh, or after restarting Cursor.
- **Use only the VSIX install**: Uninstall any marketplace-installed Lumina extensions, then install from the `.vsix` via BDA so the only installed version is from our build.

---

## Summary

- **Use only VSIX** — BDA builds and installs from `.vsix`; no marketplace publish.
- **Remove from marketplace** — If they’re already listed, unpublish from Open VSX (and VS Code Marketplace) so we only use VSIX until prod-ready.
