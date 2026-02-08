# Pre-Reboot Checklist (2026-01-29)

**Purpose**: Quick verification that all fixes are in place before reboot, and what to check after reboot.

**Fully automatic reboot**: Run **`.\scripts\powershell\lumina_reboot_auto.ps1 -Restart`** — closes Cursor, stops Ollama/Docker, restarts PC (no manual steps). Post-reboot verify runs automatically at logon. Full flow: **`docs/system/REBOOT_MONITOR_SHUTDOWN_STARTUP.md`**.

---

## Before Reboot – Confirmed In Place

 ,|Item|Status|
|-----|-----|
|**Cursor – two cluster models only**|ULTRON (localhost:11434, qwen2.5-coder:7b) and Iron Legion (10.17.17.11:11434, codellama:13b) in Agent, Chat, Composer|
|**Default model**|`cursor.ai.model`: ULTRON|
|**Host identity**|Kaiju = 10.17.17.11, NAS = 10.17.17.32, pfSense = 10.17.17.1 in `config/host_identity_registry.json`|
|**Cluster registry**|`config/cluster_endpoint_registry.json` – ultron_local (11434), kaiju_iron_legion (10.17.17.11)|
|**Rules**|context_intent_baseline, troubleshooting_decisioning_workflow, cluster_single_node_presentation, host_identity_dns|
|**Memories**|host_identity_kaiju_nas_critical, MEMORY_INDEX, pre_action_checklist|
|**Baseline**|`docs/system/CONTEXT_AND_INTENT_BASELINE.md` – context score, confidence & courage|
|**maxTokens**|8192 globally and per model|

---

## Iron Legion Port Note

- **Cursor** points at **10.17.17.11:11434** (standard Ollama).
- **Cluster registry** lists kaiju_iron_legion at **10.17.17.11:11437** (status offline).
- **Host identity** lists Iron Legion Ollama at **10.17.17.11:11434**.

If after reboot **Iron Legion** doesn’t connect, confirm on Kaiju which port Ollama uses (11434 vs 11437). If it’s 11437, update Cursor’s Iron Legion `apiBase` in `.vscode/settings.json` to `http://10.17.17.11:11437`.

---

## After Reboot – Quick Checks

1. **Ollama (laptop)** – If you use ULTRON from this machine, ensure Ollama is running on the laptop (e.g. `http://localhost:11434/api/tags`).
2. **Cursor** – Open Cursor; in Agent/Chat/Composer model selector you should see **ULTRON** and **Iron Legion** only.
3. **Test ULTRON** – Select ULTRON, send a short prompt; confirm no “Connection stalled.”
4. **Test Iron Legion** – Select Iron Legion (with Kaiju powered and Ollama/cluster running on 10.17.17.11); confirm it connects or note the error.
5. **Persistent memory** – If anything “forgets” (e.g. host identity, cluster as single node), re-check `.cursor/rules` and `.cursor/memories` are loaded; refer to `MEMORY_INDEX.md` and `docs/system/PERSISTENT_MEMORY_MAP.md`.

---

## If Something Breaks

- **Connection stalled / invalid model**: Note which cluster (ULTRON vs Iron Legion) and which surface (Agent/Chat/Composer). PM000003102 is open for Cursor + local AI; add notes to the ticket or investigation brief.
- **Wrong host/IP**: Re-check `config/host_identity_registry.json` and `.cursor/memories/host_identity_kaiju_nas_critical.md` (Kaiju = .11, NAS = .32).

No further changes recommended before reboot; config and rules are consistent.
