# Comprehensive Homelab Control Audit

**Purpose:** Map EVERY device, service, application, feature, functionality, and option in the homelab ecosystem with AI control percentage scoring.

**Question:** "How much control does AI have over [X] compared to human?"
**Target:** 100% = AI can fully control/utilize. <100% = gaps exist.

**Last Updated:** 2026-02-04

---

## Scoring Legend

| Score | Meaning | Action Required |
|-------|---------|-----------------|
| 100% | Full AI control, fully automated | Maintain |
| 80-99% | Near-complete, minor gaps | Quick fixes |
| 60-79% | Partial control, significant gaps | Priority improvement |
| 40-59% | Limited control, major gaps | Needs development |
| 20-39% | Minimal control | Needs major work |
| 0-19% | No AI control | Manual only or needs full implementation |

---

# SECTION 1: CURSOR IDE (Template/Foundation)

## Overview

| Metric | Value |
|--------|-------|
| **Device/Service** | Cursor IDE |
| **Type** | Development Environment |
| **AI Integration** | Native Claude + Extensions |
| **Overall Control Score** | **72%** |

---

## 1.1 CURSOR FEATURES

### Chat & Conversation

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **Chat Panel (Cmd+L)** | ✅ Full | Query input | 95% | Open with Cmd+L, type question | ✅ Use for all code questions |
| **Inline Chat (Cmd+K)** | ✅ Full | Selection | 90% | Select code, Cmd+K | ✅ Use for quick edits |
| **Agent Mode** | ✅ Autonomous | Approval | 85% | Enable in chat, let agent work | ✅ Use for multi-file tasks |
| **Composer** | ✅ Full | Direction | 80% | Cmd+I for multi-file edits | ✅ Use for new features |
| **@-mentions** | ⚠️ Partial | Must invoke | 70% | Type @ then reference | ⚠️ AI should auto-suggest |
| **Context window** | ❌ Hidden | Cannot see | 30% | No visibility into usage | ❌ Need usage indicator |

**Section Score: 75%**

### Code Completion

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **Tab completion** | ✅ Auto | Accept/reject | 90% | Type, Tab to accept | ✅ Keep enabled |
| **Multi-line ghost** | ✅ Auto | Accept/reject | 85% | Wait for suggestion | ✅ Keep enabled |
| **Partial accept** | ⚠️ Partial | Word-by-word | 70% | Cmd+→ for partial | ⚠️ Learn shortcuts |
| **Completion trigger** | ❌ Manual | Must type | 40% | Only on typing | ❌ Could auto-trigger |

**Section Score: 71%**

### Agent Capabilities

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **File creation** | ✅ Full | Approval | 95% | Agent proposes, you approve | ✅ Working well |
| **File editing** | ✅ Full | Approval | 95% | Agent edits, you review | ✅ Working well |
| **Shell commands** | ✅ Full | Approval | 90% | Agent runs commands | ✅ Working well |
| **Multi-file edits** | ✅ Full | Approval | 90% | Agent coordinates | ✅ Working well |
| **Background tasks** | ⚠️ Limited | Must enable | 60% | Background agent feature | ⚠️ Use more |
| **MCP tools** | ⚠️ Partial | Config needed | 50% | Configure in settings | ⚠️ Enable more MCPs |
| **Browser automation** | ⚠️ MCP only | Extension | 40% | Via cursor-ide-browser MCP | ⚠️ Enable MCP |

**Section Score: 74%**

### Context Providers (@-mentions)

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **@File** | ✅ Can read | Must mention | 80% | @filename.py | ✅ Use frequently |
| **@Folder** | ✅ Can read | Must mention | 80% | @foldername/ | ✅ Use for context |
| **@Codebase** | ✅ Semantic | Must invoke | 75% | @Codebase query | ✅ Use for search |
| **@Web** | ✅ Search | Must invoke | 70% | @Web query | ✅ Use for research |
| **@Docs** | ⚠️ One-by-one | Must add | 40% | Add in settings | ❌ Bulk add needed |
| **@Git** | ⚠️ Partial | Must invoke | 60% | @Git for diff | ⚠️ Auto-awareness |
| **@Problems** | ⚠️ Partial | Must invoke | 60% | @Problems for lints | ⚠️ Auto-awareness |
| **@Image** | ✅ Vision | Must attach | 70% | Paste image | ✅ Use for UI |

**Section Score: 67%**

### Settings & Configuration

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **settings.json** | ❌ Cannot edit | Manual edit | 20% | Edit manually | ❌ AI should configure |
| **keybindings.json** | ❌ Cannot edit | Manual edit | 20% | Edit manually | ❌ AI should configure |
| **MCP config** | ❌ Cannot edit | Manual edit | 30% | .cursor/mcp.json | ❌ AI should configure |
| **Extension install** | ❌ Cannot | Manual | 10% | Marketplace | ❌ AI should install |
| **Model selection** | ⚠️ Suggests | User chooses | 50% | Settings dropdown | ⚠️ Auto-select |
| **Rules files** | ✅ Can create | Approval | 80% | .cursor/rules/ | ✅ Working |
| **Hooks** | ✅ Can create | Approval | 80% | .cursor/hooks/ | ✅ Working |

**Section Score: 41%**

### Indexing & Search

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **Codebase indexing** | ✅ Auto | Configure ignore | 85% | Automatic | ✅ Working |
| **Semantic search** | ✅ Full | Query | 80% | @Codebase | ✅ Working |
| **Symbol search** | ⚠️ Partial | Must invoke | 60% | Cmd+T | ⚠️ AI integration |
| **File search** | ⚠️ Partial | Must invoke | 60% | Cmd+P | ⚠️ AI integration |
| **Grep/ripgrep** | ✅ Full | Query | 85% | Agent uses rg | ✅ Working |

**Section Score: 74%**

### Debugging & Testing

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **Debug explain** | ✅ Can explain | Must ask | 70% | "Explain this error" | ✅ Use more |
| **Test generation** | ✅ Can generate | Must ask | 80% | "Write tests for X" | ✅ Use more |
| **Test running** | ⚠️ Via shell | Agent runs | 70% | Agent runs pytest | ⚠️ Integrate debugger |
| **Breakpoints** | ❌ Cannot set | Manual | 20% | Click gutter | ❌ AI should set |
| **Debug session** | ❌ Cannot control | Manual | 10% | F5 to start | ❌ Major gap |

**Section Score: 50%**

### Version Control

| Feature | AI Control | Human Control | Score | How to Use | Recommendation |
|---------|------------|---------------|-------|------------|----------------|
| **Git status** | ✅ Can check | Agent runs | 90% | Agent uses git | ✅ Working |
| **Git commit** | ✅ Can commit | Approval | 85% | Agent commits | ✅ Working |
| **Git push** | ⚠️ Restricted | Approval | 70% | Agent pushes | ⚠️ Safety first |
| **PR creation** | ✅ Via gh | Approval | 80% | Agent uses gh | ✅ Working |
| **Branch mgmt** | ✅ Full | Agent runs | 85% | Agent manages | ✅ Working |
| **Merge/rebase** | ⚠️ Careful | Approval | 60% | Manual preferred | ⚠️ Dangerous |

**Section Score: 78%**

---

## CURSOR OVERALL SCORES

| Category | Score | Status |
|----------|-------|--------|
| Chat & Conversation | 75% | 🟡 Good |
| Code Completion | 71% | 🟡 Good |
| Agent Capabilities | 74% | 🟡 Good |
| Context Providers | 67% | 🟡 Needs work |
| Settings & Config | 41% | 🔴 Major gap |
| Indexing & Search | 74% | 🟡 Good |
| Debugging & Testing | 50% | 🔴 Needs work |
| Version Control | 78% | 🟡 Good |
| **OVERALL** | **72%** | **🟡 Good but gaps** |

---

## CURSOR RECOMMENDATIONS

### High Priority (Score < 50%)

1. **Settings Configuration (41%)** — AI cannot modify settings.json, keybindings.json, or install extensions
 - **Fix:** Create scripts that AI can call to modify settings
 - **Script needed:** `scripts/python/cursor_settings_manager.py`

2. **Debugging & Testing (50%)** — AI cannot control debugger, set breakpoints
 - **Fix:** Integrate debug adapter protocol
 - **Workaround:** AI writes test scripts and runs them

### Medium Priority (Score 50-70%)

3. **Context Providers (67%)** — @Docs is one-by-one only
 - **Fix:** LUMINA_KNOWLEDGE_BASE.md as master index (DONE)
 - **Fix:** RoamWise MCP for bulk knowledge access

4. **Agent Capabilities (74%)** — MCP tools underutilized
 - **Fix:** Enable all MCP servers
 - **Action:** Verify MCP_DOCKER is enabled

### Maintain (Score > 75%)

5. **Chat, Completion, Git** — Working well, maintain current setup

---

# SECTION 2: HOMELAB DEVICES

## 2.1 KAIJU (Desktop PC)

| Metric | Value |
|--------|-------|
| **Device** | Kaiju_no_8 |
| **IP** | 10.17.17.11 |
| **Type** | Windows Desktop |
| **Role** | Iron Legion host, Ollama |
| **Overall Control Score** | **65%** |

### Features & Functions

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Ollama server** | ✅ API | Config | 90% | http://10.17.17.11:11434 | ✅ Working |
| **Iron Legion** | ✅ API | Config | 85% | http://10.17.17.11:3000 | ✅ Working |
| **Expert router** | ✅ API | Config | 80% | /expert endpoint | ✅ Working |
| **Model loading** | ⚠️ Via API | Manual | 60% | ollama pull/run | ⚠️ Auto-load |
| **GPU management** | ❌ No API | Manual | 20% | NVIDIA tools | ❌ Need monitoring |
| **Windows services** | ❌ No remote | RDP | 30% | RDP or SSH | ❌ Need automation |
| **File system** | ⚠️ Via MCP | Config | 50% | filesystem MCP | ⚠️ Enable |
| **Remote desktop** | ❌ Manual | RDP | 10% | RDP client | ❌ MANUS integration |

**Device Score: 65%**

### Recommendations

1. **Enable filesystem MCP** for Kaiju file access
2. **GPU monitoring script** — Create API for GPU stats
3. **MANUS integration** — Remote control via automation

---

## 2.2 NAS (Synology DS1821+)

| Metric | Value |
|--------|-------|
| **Device** | DS1821PLUS |
| **IP** | 10.17.17.32 |
| **Type** | NAS |
| **Role** | Storage, MCP hub, containers |
| **Overall Control Score** | **78%** |

### Services & Control

| Service | AI Control | Human | Score | Endpoint | Recommendation |
|---------|------------|-------|-------|----------|----------------|
| **Docker/DSM** | ✅ API | Config | 85% | Container Manager | ✅ Working |
| **n8n** | ✅ API | Workflows | 90% | :5678 | ✅ Working |
| **MANUS** | ✅ API | Config | 85% | :8085 | ✅ Working |
| **ElevenLabs MCP** | ✅ API | Config | 90% | :8086 | ✅ Working |
| **Filesystem MCP** | ✅ API | Config | 85% | :8099 | ✅ Working |
| **Git MCP** | ✅ API | Config | 80% | :8100 | ✅ Working |
| **Brave Search** | ✅ API | Config | 85% | :8101 | ✅ Working |
| **Puppeteer** | ✅ API | Config | 80% | :8102 | ✅ Working |
| **GitHub MCP** | ✅ API | Config | 80% | :8103 | ✅ Working |
| **Slack MCP** | ⚠️ API | Config | 60% | :8104 | ⚠️ Configure |
| **AWS Diagram** | ✅ API | Config | 75% | :8087 | ✅ Working |
| **AWS Docs** | ✅ API | Config | 75% | :8088 | ✅ Working |
| **AWS CDK** | ⚠️ API | Config | 60% | :8089 | ⚠️ Test |
| **Terraform** | ⚠️ API | Config | 60% | :8090 | ⚠️ Test |
| **Lambda MCP** | ⚠️ API | Config | 60% | :8091 | ⚠️ Test |
| **Cost Analysis** | ⚠️ API | Config | 60% | :8092 | ⚠️ Test |
| **Bedrock KB** | ⚠️ API | Config | 60% | :8093 | ⚠️ Test |
| **Nova Canvas** | ⚠️ API | Config | 60% | :8094 | ⚠️ Test |
| **SynoDownload** | ⚠️ API | Config | 70% | :8095 | ⚠️ Test |
| **SynoLink** | ⚠️ API | Config | 70% | :8096 | ⚠️ Test |
| **Postgres** | ⚠️ API | Config | 65% | :8097 | ⚠️ Test |
| **SQLite** | ⚠️ API | Config | 65% | :8098 | ⚠️ Test |
| **DSM API** | ⚠️ Partial | Auth | 50% | :5001 | ⚠️ Auth needed |
| **Disk health** | ❌ No API | DSM UI | 30% | DSM panel | ❌ Need monitoring |
| **Package mgmt** | ❌ No API | DSM UI | 20% | DSM panel | ❌ Need API |

**Device Score: 78%**

### Recommendations

1. **DSM API authentication** — Store creds in Azure Vault, enable API access
2. **Container health monitoring** — Script to check all containers
3. **Disk health API** — Create endpoint for SMART data

---

## 2.3 ULTRON (Laptop)

| Metric | Value |
|--------|-------|
| **Device** | Ultron Laptop |
| **IP** | 127.0.0.1 (localhost) |
| **Type** | Laptop |
| **Role** | Mobile dev, local Ollama |
| **Overall Control Score** | **70%** |

### Features & Functions

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Local Ollama** | ✅ API | Config | 90% | localhost:11434 | ✅ Working |
| **Cursor IDE** | ✅ Via agent | UI | 72% | See Section 1 | 🟡 Above |
| **Kilo Code** | ✅ Extension | Config | 75% | Extension panel | ✅ Working |
| **Docker Desktop** | ✅ API | UI | 80% | docker commands | ✅ Working |
| **Windows services** | ⚠️ PowerShell | Admin | 50% | Get-Service | ⚠️ Elevate |
| **File system** | ✅ Direct | Agent | 90% | Read/Write tools | ✅ Working |
| **Shell/terminal** | ✅ Full | Agent | 90% | Shell tool | ✅ Working |
| **Git** | ✅ Full | Agent | 85% | git commands | ✅ Working |
| **Browser** | ⚠️ MCP | Config | 50% | cursor-ide-browser | ⚠️ Enable |

**Device Score: 70%**

---

## 2.4 PFSENSE (Firewall)

| Metric | Value |
|--------|-------|
| **Device** | pfSense Firewall |
| **IP** | 10.17.17.1 |
| **Type** | Firewall |
| **Role** | Gateway, security |
| **Overall Control Score** | **25%** |

### Features & Functions

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Web UI** | ❌ No API | Browser | 20% | https://10.17.17.1 | ❌ Need API |
| **Firewall rules** | ❌ No API | UI | 10% | UI editing | ❌ Need automation |
| **VPN status** | ❌ No API | UI | 20% | UI monitoring | ❌ Need monitoring |
| **DHCP leases** | ❌ No API | UI | 20% | UI viewing | ❌ Need API |
| **DNS** | ❌ No API | UI | 20% | UI config | ❌ Need API |
| **Logs** | ❌ No API | UI | 30% | UI viewing | ❌ Syslog forward |
| **Package mgmt** | ❌ No API | UI | 10% | UI only | ❌ Need API |
| **IDS/IPS** | ❌ No API | UI | 20% | Snort/Suricata UI | ❌ Need alerts |

**Device Score: 25%**

### Recommendations (CRITICAL)

1. **Enable pfSense API** — Install `pfSense-api` package
2. **Syslog forwarding** — Send logs to NAS for AI analysis
3. **SNMP monitoring** — Enable for network stats
4. **Webhook alerts** — IDS alerts to n8n

---

# SECTION 3: FRAMEWORKS & SERVICES

## 3.1 Docker Framework

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Container list** | ✅ API | - | 95% | docker ps | ✅ Working |
| **Container start/stop** | ✅ API | - | 95% | docker start/stop | ✅ Working |
| **Container logs** | ✅ API | - | 90% | docker logs | ✅ Working |
| **Image pull** | ✅ API | - | 90% | docker pull | ✅ Working |
| **Compose up/down** | ✅ API | - | 85% | docker-compose | ✅ Working |
| **Volume management** | ✅ API | - | 85% | docker volume | ✅ Working |
| **Network management** | ✅ API | - | 80% | docker network | ✅ Working |
| **Build images** | ✅ API | Dockerfile | 80% | docker build | ✅ Working |
| **Registry push** | ⚠️ Auth | Credentials | 60% | docker push | ⚠️ Auth setup |

**Framework Score: 85%**

---

## 3.2 n8n Workflow Framework

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **List workflows** | ✅ API | - | 90% | API call | ✅ Working |
| **Execute workflow** | ✅ API | - | 90% | Webhook trigger | ✅ Working |
| **View executions** | ✅ API | - | 85% | API call | ✅ Working |
| **Create workflow** | ⚠️ API | Visual | 50% | API or UI | ⚠️ Use UI |
| **Edit workflow** | ⚠️ API | Visual | 40% | API or UI | ⚠️ Use UI |
| **Manage credentials** | ❌ UI only | Manual | 30% | n8n UI | ❌ Need API |
| **Error handling** | ✅ Automatic | Config | 80% | Workflow settings | ✅ Working |

**Framework Score: 66%**

---

## 3.3 MCP Framework (Model Context Protocol)

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Tool invocation** | ✅ Native | Agent | 95% | MCP tools | ✅ Working |
| **Resource access** | ✅ Native | Agent | 90% | MCP resources | ✅ Working |
| **Server discovery** | ✅ Auto | Config | 85% | mcps/ folder | ✅ Working |
| **Health checks** | ⚠️ Manual | Script | 50% | curl endpoints | ⚠️ Automate |
| **Server restart** | ⚠️ Docker | Manual | 60% | docker restart | ⚠️ Automate |
| **New server deploy** | ⚠️ Manual | Config | 40% | Manual setup | ⚠️ Templates |

**Framework Score: 70%**

---

## 3.4 ElevenLabs TTS Framework

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Text-to-speech** | ✅ API | - | 95% | MCP or API | ✅ Working |
| **Voice selection** | ✅ API | - | 90% | Voice ID param | ✅ Working |
| **Voice cloning** | ✅ API | Samples | 80% | Upload samples | ✅ Working |
| **Pronunciation dict** | ✅ API | Config | 75% | Dictionary API | ⚠️ Configure |
| **Quota monitoring** | ⚠️ API | Check | 60% | API call | ⚠️ Auto-alert |
| **Voice library** | ✅ API | - | 85% | List voices | ✅ Working |

**Framework Score: 81%**

---

## 3.5 Git/GitHub Framework

| Feature | AI Control | Human | Score | How to Use | Recommendation |
|---------|------------|-------|-------|------------|----------------|
| **Git operations** | ✅ CLI | Agent | 95% | git commands | ✅ Working |
| **GitHub API** | ✅ gh CLI | Agent | 90% | gh commands | ✅ Working |
| **PR management** | ✅ gh CLI | Agent | 85% | gh pr | ✅ Working |
| **Issue management** | ✅ gh CLI | Agent | 85% | gh issue | ✅ Working |
| **Actions/workflows** | ⚠️ API | Config | 60% | workflow files | ⚠️ Templates |
| **Secrets management** | ❌ Manual | UI | 30% | GitHub UI | ❌ API access |

**Framework Score: 74%**

---

# SECTION 4: OVERALL SCORES SUMMARY

## By Device

| Device | Score | Status | Priority |
|--------|-------|--------|----------|
| NAS | 78% | 🟡 Good | Maintain |
| Cursor IDE | 72% | 🟡 Good | Improve |
| Ultron Laptop | 70% | 🟡 Good | Improve |
| Kaiju Desktop | 65% | 🟡 Needs work | Improve |
| pfSense | 25% | 🔴 Critical | HIGH PRIORITY |

## By Framework

| Framework | Score | Status | Priority |
|-----------|-------|--------|----------|
| Docker | 85% | 🟢 Excellent | Maintain |
| ElevenLabs | 81% | 🟢 Excellent | Maintain |
| Git/GitHub | 74% | 🟡 Good | Minor fixes |
| MCP | 70% | 🟡 Good | Automate health |
| n8n | 66% | 🟡 Needs work | Improve API |

## By Category

| Category | Avg Score | Status |
|----------|-----------|--------|
| AI/ML Clusters | 82% | 🟢 Excellent |
| Storage/NAS | 78% | 🟡 Good |
| Development | 71% | 🟡 Good |
| Automation | 75% | 🟡 Good |
| Security/Network | 25% | 🔴 Critical |

---

# SECTION 5: ACTION PLAN

## Immediate (This Week)

1. **pfSense API** (25% → 60%) — Install API package, enable monitoring
2. **Cursor Settings Script** (41% → 70%) — Create settings manager
3. **MCP Health Automation** (50% → 80%) — Auto-check all MCPs

## Short-term (This Month)

4. **n8n API enhancement** — Workflow creation via API
5. **Kaiju GPU monitoring** — NVIDIA stats API
6. **DSM API authentication** — Full NAS control

## Medium-term (Next Quarter)

7. **pfSense full integration** — Rules, VPN, IDS via API
8. **Debug adapter integration** — Cursor debugger control
9. **Cross-device orchestration** — MANUS coordinates all devices

---

# SECTION 6: WHAT'S MISSING FOR 100%?

## To reach 100% AI control, we need:

| Gap | Current | Target | Fix |
|-----|---------|--------|-----|
| Cursor settings | 41% | 90% | Settings manager script |
| Cursor debugging | 50% | 85% | Debug adapter protocol |
| pfSense control | 25% | 80% | API package + integration |
| n8n workflow edit | 40% | 75% | API-based creation |
| GPU monitoring | 20% | 80% | NVIDIA API wrapper |
| DSM full control | 50% | 85% | Auth + API coverage |

---

**Total Ecosystem Score: 68%**

**Target Score: 90%+**

**Gap to close: 22 percentage points**

---

**Tags:** #audit #control #homelab #inventory @JARVIS @LUMINA
