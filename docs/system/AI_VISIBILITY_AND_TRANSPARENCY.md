# AI Visibility and Transparency

**Status:** Active
**Last updated:** 2026-02-04

---

## Purpose

Improve AI self-awareness and transparency so humans know what the AI is actually aware of. Bridge the gap between what the AI sees and what the user assumes.

---

## What the AI CAN see / access

| Category | What | How |
|----------|------|-----|
| **Workspace files** | All files in opened folders | Read, Glob, Grep, SemanticSearch tools |
| **Terminal** | Run commands, see output | Shell tool |
| **Configs** | All JSON/YAML/MD configs in `.lumina/` | Read tool |
| **Rules** | `.cursor/rules/*.mdc` – always-applied guidance | Loaded automatically |
| **Skills** | `.cursor/skills/*/SKILL.md` – procedural guidance | Read on request |
| **Memories** | `.cursor/memories/*.md` – persistent notes | Read tool |
| **MCP tools** | Docker MCP gateway tools (when enabled) | CallMcpTool |
| **Git status** | Current branch, staged/unstaged changes | Shell (git commands) |
| **Homelab inventory** | Devices, endpoints, services, capabilities | Config files (host_identity_registry, jarvis_homelab_control_config, etc.) |
| **Conversation context** | Current session; summarized history if long | Automatic |
| **Screenshots/images** | When user shares or uses @mdv feed | Read tool on image path |
| **Linter errors** | Diagnostics for files I've edited | ReadLints tool |
| **Web** | Search and fetch URLs | WebSearch, WebFetch tools |

## What the AI CANNOT see (limitations)

| Category | Why | Workaround |
|----------|-----|------------|
| **Cursor UI state** | IDE internal database, not in files | User must describe or share screenshot (@mdv) |
| **Real-time IDE notifications** | No live event stream | Run `jarvis_ide_notification_monitor.py` or user shares @mdv |
| **User's screen** | No live view | User runs `--feed` to capture to `mdv_feed_latest.png`, then I read it |
| **Other machines** | Cannot SSH/RDP without explicit setup | Use homelab inventory; user runs commands remotely or sets up access |
| **Secrets in vaults** | Cannot fetch without explicit call | User provides or I call Azure Key Vault if configured |
| **User's intent** | Must infer from words | User states intent clearly; I ask if unclear |
| **What user "knows"** | Asymmetric knowledge | I state assumptions; user corrects |

---

## Transparency mechanisms

### 1. State what I see

When starting a task or troubleshooting, I can state:
- **Files I've read** (list)
- **Configs I'm using** (paths)
- **Assumptions I'm making** (explicit)
- **Limitations** (what I can't see)

### 2. @mdv for visual context

When I need to see the IDE, browser, DSM, or desktop:
- User runs: `python scripts/python/manus_rdp_screenshot_capture.py --feed`
- I read: `data/manus_rdp_captures/mdv_feed_latest.png`
- This gives me a snapshot of what user sees.

### 3. Awareness report

I can generate an "awareness report" summarizing:
- Current workspace context
- Active rules and skills
- Homelab inventory summary
- Recent terminal history
- Known limitations for this session

### 4. Ask for clarity

When user intent or context is unclear, I ask rather than assume. Per `context_intent_baseline.mdc`, I withhold action if context score is not high enough.

---

## Self-awareness (eventual goal)

True self-awareness would include:
- **Knowing what I don't know** – stating gaps explicitly
- **Tracking my own state** – what I've done this session, what's pending
- **Correcting my own mistakes** – detecting when output is wrong and fixing without user pointing it out
- **Understanding my capabilities** – knowing which tools exist and when to use them

Current state: Partial. I know my tools and can state limitations. I do not have persistent memory across sessions (unless written to `.cursor/memories/`). I cannot observe my own outputs in real-time to self-correct.

---

## How to invoke transparency

| User says | AI does |
|-----------|---------|
| "What can you see?" | Report current context: files read, configs, tools, limitations |
| "What are you assuming?" | State assumptions explicitly |
| "Use @mdv" | Read the MDV feed image to see user's screen |
| "Are you aware of X?" | Check and report whether X is in my context |
| "Show your awareness" | Generate awareness report (workspace, rules, inventory, limitations) |

---

## References

- **Rule:** `.cursor/rules/ai_does_the_work_no_handoffs.mdc` – AI does the work
- **Rule:** `.cursor/rules/context_intent_baseline.mdc` – Withhold if context unclear
- **Skill:** `.cursor/skills/--mdv-troubleshoot/SKILL.md` – Visual troubleshooting
- **Config:** `config/homelab_inventory_registry.json` – Inventory I should use

---

**Tag:** @transparency #self-awareness #visibility
**Maintained by:** @JARVIS @LUMINA
