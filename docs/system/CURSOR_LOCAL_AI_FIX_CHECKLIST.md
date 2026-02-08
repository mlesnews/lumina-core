# Cursor + Local AI Fix Checklist

**Last Updated**: 2026-01-29
**Purpose**: Single checklist to fix and verify Cursor working with local AI clusters (Ultron + Iron Legion).

**Support team investigation**: PM ticket **PM000003102** is open. Support teams (Problem Management, QA/QC) are to **investigate and work the issue** per `docs/helpdesk/CURSOR_LOCAL_AI_INVESTIGATION_BRIEF.md`. Do not treat as fully resolved until RCA and QA sign-off. Avoid ad-hoc changes ("playing in traffic").

---

## What We Have (Ready to Use)

| Item | Location | Purpose |
|------|----------|---------|
| **Host identity** | `config/host_identity_registry.json`, `.cursor/rules/host_identity_dns.mdc`, `.cursor/memories/host_identity_kaiju_nas_critical.md` | Kaiju = 10.17.17.11 (desktop), NAS = 10.17.17.32, pfSense = 10.17.17.1; no alias for NAS |
| **Cluster endpoints** | `config/cluster_endpoint_registry.json` | Ultron (localhost:11434, router :8080), Iron Legion (10.17.17.11:11437, marks 3001–3007) |
| **Cursor custom models** | `.vscode/settings.json` | **ULTRON**, **ULTRON_72B** (localhost:11434), **Iron Legion** (10.17.17.11:11434) for Agent, Chat, Composer |
| **Timeouts & retries** | `.vscode/settings.json` | timeout 60s/120s, retry 3, connectionTimeout 30s, streamTimeout 120s |
| **Quick fix guide** | `docs/system/CURSOR_CONNECTION_STALLED_QUICK_FIX.md` | Ollama check, model pull, restart Cursor |
| **Persistent memory** | `.cursor/memories/`, `docs/system/PERSISTENT_MEMORY_MAP.md` | Host identity and rules survive reboot |

---

## Fix / Verify Steps

### 1. Local Ollama (Ultron cluster)

```powershell
# Is Ollama running?
Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing

# If not: ollama serve
# Models present?
ollama list
# If missing: ollama pull qwen2.5-coder:7b  ;  ollama pull qwen2-72b:latest
```

### 2. Iron Legion (Kaiju_no_8 desktop)

- Kaiju = **10.17.17.11** only (not NAS).
- Ensure Ollama (or cluster) on Kaiju is running and reachable from this machine:
  - `http://10.17.17.11:11434/api/tags` (Ollama)
  - Or expert router `http://10.17.17.11:3000` if you use that.
- If Iron Legion is offline, Cursor will still work with **ULTRON** and **ULTRON_72B** (localhost).

### 3. Cursor model selection

- In Cursor: open model selector (top-right).
- You should see: **ULTRON**, **ULTRON_72B**, **Iron Legion**.
- Default is **ULTRON** (localhost). Switch to **Iron Legion** to use Kaiju (10.17.17.11) when that cluster is up.

### 4. Restart Cursor

- Fully quit Cursor, reopen the project so it reloads settings and reconnects to Ollama (and Iron Legion if reachable).

### 5. If it still stalls

- See `docs/system/CURSOR_CONNECTION_STALLED_QUICK_FIX.md` and `docs/system/CURSOR_CONNECTION_STALLED_WORKFLOW_FIX.md`.
- Optional: run `python scripts/python/diagnose_cursor_connection.py` if that script exists.

---

## Two Clusters in Cursor

| Cursor model | Cluster | Endpoint | When to use |
|--------------|---------|----------|-------------|
| **ULTRON** | Ultron (laptop) | http://localhost:11434 | Default; fast local coding |
| **ULTRON_72B** | Ultron (laptop) | http://localhost:11434 | Heavier tasks, same machine |
| **Iron Legion** | Kaiju_no_8 (desktop) | http://10.17.17.11:11434 | When Kaiju desktop is on and you want its models |

---

## Summary

**Yes — we have what we need to fix the local AI and Cursor issue:**

1. Host identity is correct and persisted (Kaiju=*.11, NAS=*.32, pfSense=*.1, one NAS).
2. Cluster registry and host registry are the SSOT for endpoints.
3. Cursor has ULTRON, ULTRON_72B, and **Iron Legion** as custom models (Agent, Chat, Composer).
4. Timeouts and retries are set to reduce “connection stalled” issues.
5. Checklist and quick-fix docs exist; restart Cursor after any config change.

If Cursor still fails, the usual cause is Ollama not running or not reachable (localhost for Ultron, 10.17.17.11 for Iron Legion). Use the steps above to verify both, then restart Cursor.
