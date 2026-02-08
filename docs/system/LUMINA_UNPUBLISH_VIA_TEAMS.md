# Use Company Microsoft Teams for Lumina Unpublish Task

**Goal**: Route the “remove Lumina from all marketplaces” task through your company’s Microsoft Teams so the right person can execute it and track it.

---

## Why use Teams

- **Visibility**: Post the task in a channel (e.g. Engineering, DevOps, or a dedicated “Lumina” channel) so the owner and others see it.
- **Ownership**: Assign or @mention the person who has the **lumina** publisher account (VS Code Marketplace + Open VSX).
- **Audit**: The request and completion can be discussed and confirmed in the same thread.

---

## Option A — Post the task manually in Teams

1. Open the channel where you want this tracked (e.g. Engineering, DevOps).
2. Post the content below (or run the script once to get a formatted copy — see Option B).
3. @mention the person who will perform the unpublish.
4. When done, they reply in the thread and check off the items.

**Message to post** (copy from [REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md](REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md) or use the script output):

- **Title**: **Action required: Unpublish all Lumina extensions from marketplaces**
- **RCA**: AI (agent) published; not human. See repo: `docs/system/LUMINA_EXTENSION_NEVER_PUBLISH_WHY.md`
- **Extensions to remove** (publisher: lumina): Lumina Core, Lumina Premium, Lumina Unified Queue, Lumina Footer Ticker, Lumina File Auto-Close (all five).
- **Steps**:
  1. **VS Code Marketplace**: https://marketplace.visualstudio.com/manage — sign in, unpublish/remove each of the five.
  2. **Open VSX**: https://open-vsx.org — sign in, open publisher **lumina**, unpublish/remove each of the five.
  3. **Cursor**: After 1 and 2, Cursor will stop showing them once caches refresh; use only VSIX install (BDA).
- **Checklist**: VS Code Marketplace done | Open VSX done | Verification search done.

---

## Option B — Post via Incoming Webhook (automated post to a channel)

If your company uses **Teams Incoming Webhooks**, you can post the task from the repo so it appears in a channel automatically.

### 1. Create the webhook in Teams (one-time)

1. In Teams, open the channel where the task should appear.
2. **⋯** (channel options) → **Connectors** (or **Manage channel** → **Connectors**).
3. Add **Incoming Webhook**, name it (e.g. “Lumina repo”), copy the webhook URL.
4. Store the URL in a **secret store** (e.g. Azure Key Vault, env var, or a local config that is **not** committed). Do **not** put the URL in the repo (see [no_secrets_broadcast](.cursor/rules/no_secrets_broadcast.mdc)).

### 2. Configure the script

- **Option 2a — Environment variable**  
  Set `TEAMS_WEBHOOK_URL` to the webhook URL (e.g. in your shell profile or a `.env` file that is gitignored).

- **Option 2b — Config file**  
  Copy the example and add the URL in a file that is **not** committed:
  - From: `config/teams_webhook_config.json.example`
  - To: `config/teams_webhook_config.json` (and add `config/teams_webhook_config.json` to `.gitignore` if not already).
  - Replace the placeholder with the real webhook URL.

### 3. Run the script

From repo root:

```powershell
python scripts/python/post_lumina_unpublish_to_teams.py
```

- If a webhook URL is configured (env or config), the script posts the task to the channel.
- If not, it prints the message so you can paste it into Teams (Option A).

---

## Summary

- **Use company Teams** to assign and track the Lumina unpublish task.
- **Option A**: Copy the task from REMOVE_LUMINA_FROM_ALL_MARKETPLACES.md (or script output) and post it in the right channel; @mention the owner.
- **Option B**: Configure a Teams Incoming Webhook (URL in env or local config, not in repo), then run `post_lumina_unpublish_to_teams.py` to post the task to the channel.
