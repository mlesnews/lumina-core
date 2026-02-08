# Remove Lumina Extensions from ALL Marketplace Sources

**Goal**: Remove every Lumina extension from every place they were published. No Lumina extensions are to remain on any public marketplace.

**RCA**: Root cause of the publish was **AI (agent) action, not human**. See [LUMINA_EXTENSION_NEVER_PUBLISH_WHY.md](LUMINA_EXTENSION_NEVER_PUBLISH_WHY.md).

**Route through Helpdesk (create tickets)**: Run `python scripts/python/create_lumina_unpublish_helpdesk_tickets.py` to create PM, C, T tickets and assign to helpdesk_support. See [LUMINA_UNPUBLISH_VIA_HELPDESK.md](LUMINA_UNPUBLISH_VIA_HELPDESK.md).

---

## How long were they up?

**We cannot determine duration from this repo.** Publication is done via `vsce publish` or marketplace web UIs; there is no log here of when that happened. To find out how long they were up:

- **Open VSX**: Sign in at [open-vsx.org](https://open-vsx.org), open the publisher namespace, and check each extension’s page for “first published” / “published” date.
- **VS Code Marketplace**: Sign in at [marketplace.visualstudio.com/manage](https://marketplace.visualstudio.com/manage), open each extension, and check the listing/publish history for the first publish date.

---

## All Lumina extensions to remove (publisher: lumina)

| Extension ID | Display name |
|--------------|--------------|
| `lumina.lumina-core` | Lumina Core |
| `lumina.lumina-premium` | Lumina Premium (Private Paid Add-On) |
| `lumina.lumina-unified-queue` | Lumina Unified Queue |
| `lumina.lumina-footer-ticker` | Lumina Footer Ticker |
| `lumina.lumina-file-auto-close` | Lumina File Auto-Close |

Remove every one of these from **every** source below.

---

## Source 1 — VS Code Marketplace (Microsoft)

**URL**: [https://marketplace.visualstudio.com/manage](https://marketplace.visualstudio.com/manage)

1. Sign in with the Microsoft account that owns the **lumina** publisher.
2. For each extension in the table above:
   - Open the extension.
   - Use **Unpublish** or **Remove** so it is no longer listed.
3. Confirm: search for “LUMINA” or “lumina” and ensure no Lumina extensions appear.

**CLI (optional, after auth)**  
From repo root, in a terminal where you can enter credentials:

```powershell
npx vsce login lumina
Set-Location "vscode-extensions"; .\unpublish_lumina_from_marketplace.ps1
```

If the script fails (e.g. “Aborted” or not logged in), use the web UI above to unpublish every extension.

---

## Source 2 — Open VSX (open-vsx.org)

**URL**: [https://open-vsx.org](https://open-vsx.org)

1. Sign in with the account that owns the **lumina** publisher.
2. Open the publisher namespace and find every Lumina extension (all five in the table above).
3. For each one: use **Unpublish** or **Remove** so it no longer appears in search.
4. Confirm: search for “LUMINA” or “lumina” and ensure no Lumina extensions appear.

---

## Source 3 — Cursor extension list

Cursor can show extensions from Open VSX and/or VS Code Marketplace. There is no separate “Cursor marketplace” to unpublish from.

- After you remove all Lumina extensions from **Open VSX** and **VS Code Marketplace**, Cursor’s extension list should stop showing them once caches refresh (or after restarting Cursor).
- If any Lumina extension still appears in Cursor: uninstall it there, and install only from the built `.vsix` (BDA). See [LUMINA_EXTENSION_VSIX_ONLY.md](LUMINA_EXTENSION_VSIX_ONLY.md).

---

## Source 4 — GitHub (remove extensions from GitHub)

Lumina Core and Lumina Premium `package.json` reference a GitHub repository (e.g. lumina-ai). To remove the extensions from GitHub — confession is good for the conscience — choose one:

**Option A — Make the repo private (recommended)**  
1. Go to the repository on GitHub (e.g. `https://github.com/<owner>/lumina-ai`).  
2. **Settings** → **General** → scroll to **Danger Zone**.  
3. **Change repository visibility** → **Make private**.  
4. Confirm. The repo stays for your use but is no longer publicly listed or discoverable.

**Option B — Delete the repository**  
1. Go to the repository on GitHub.  
2. **Settings** → **General** → **Danger Zone** → **Delete this repository**.  
3. Type the repo name to confirm. This is **permanent**; the repo and its history are removed from GitHub.

If you have other repos that contain or reference Lumina extensions, repeat for each. Only you can change visibility or delete repos you own; do this in the GitHub web UI while signed in.

---

## Checklist — remove from ALL sources

Use this to confirm you’ve covered everything:

- [ ] **VS Code Marketplace** — All five Lumina extensions unpublished/removed (web UI or CLI script).
- [ ] **Open VSX** — All five Lumina extensions unpublished/removed.
- [ ] **Cursor** — No Lumina extensions installed from marketplace; only VSIX install (BDA) used.
- [ ] **GitHub** — Lumina extension repo(s) made private or deleted (e.g. lumina-ai).
- [ ] **Verification** — Search “LUMINA” / “lumina” on Open VSX and VS Code Marketplace; no Lumina extensions listed.

When all boxes are checked, Lumina has been removed from all known marketplace and GitHub sources.
