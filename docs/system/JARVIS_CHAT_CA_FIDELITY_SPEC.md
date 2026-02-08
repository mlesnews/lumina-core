# JARVIS Chat - Cursor Agent (CA) Fidelity Specification

**Purpose**: Document all Cursor Agent/IDE features, MCP capabilities, and @PEAK functionality so JARVIS can replicate them, allowing extension uninstallation while retaining full capability.

**Date**: 2026-02-03  
**Version**: 1.0.0

---

## 1. CORE CURSOR AGENT TOOLS

### 1.1 File System Operations

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `Read` | Read file contents with line numbers | `jarvis_file_read()` |
| `Write` | Write/create files | `jarvis_file_write()` |
| `StrReplace` | Find and replace in files | `jarvis_str_replace()` |
| `Delete` | Delete files | `jarvis_file_delete()` |
| `LS` | List directory contents | `jarvis_ls()` |
| `Glob` | Find files by pattern | `jarvis_glob()` |
| `Grep` | Search file contents (ripgrep) | `jarvis_grep()` |

### 1.2 Shell/Terminal Operations

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `Shell` | Execute terminal commands | `jarvis_shell_exec()` |
| Background processes | Long-running commands with monitoring | `jarvis_background_task()` |
| Working directory | Stateful shell sessions | `jarvis_shell_session()` |

### 1.3 Code Intelligence

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `SemanticSearch` | Search code by meaning | `jarvis_semantic_search()` |
| `ReadLints` | Get linter errors | `jarvis_read_lints()` |
| Symbol lookup | Find definitions/references | `jarvis_symbol_lookup()` |

### 1.4 Task Management

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `TodoWrite` | Create/update task lists | `jarvis_todo_write()` |
| `Task` | Launch subagents for complex tasks | `jarvis_task_spawn()` |
| `AskQuestion` | Structured user input | `jarvis_ask_question()` |

### 1.5 Web/External

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `WebSearch` | Search the web | `jarvis_web_search()` |
| `WebFetch` | Fetch URL content | `jarvis_web_fetch()` |
| `GenerateImage` | AI image generation | `jarvis_generate_image()` |

---

## 2. MCP SERVER CAPABILITIES

### 2.1 cursor-ide-browser (Browser Automation)

| Tool | Function | JARVIS Implementation |
|------|----------|----------------------|
| `browser_navigate` | Navigate to URL | `jarvis_browser_navigate()` |
| `browser_snapshot` | Get page structure/elements | `jarvis_browser_snapshot()` |
| `browser_click` | Click elements | `jarvis_browser_click()` |
| `browser_type` | Type text (append) | `jarvis_browser_type()` |
| `browser_fill` | Fill input (replace) | `jarvis_browser_fill()` |
| `browser_scroll` | Scroll page | `jarvis_browser_scroll()` |
| `browser_tabs` | Manage browser tabs | `jarvis_browser_tabs()` |
| `browser_lock/unlock` | Session control | `jarvis_browser_lock()` |
| `browser_handle_dialog` | Handle alerts/prompts | `jarvis_browser_dialog()` |
| `browser_wait` | Wait for conditions | `jarvis_browser_wait()` |

**Workflow Pattern**:
```
browser_navigate -> browser_lock -> (interactions) -> browser_unlock
```

### 2.2 Homelab MCP Servers

| Server | Endpoint | Function |
|--------|----------|----------|
| MANUS | `10.17.17.32:8085` | General automation |
| ElevenLabs | `10.17.17.32:8086` | Voice synthesis |
| n8n | `10.17.17.32:5678` | Workflow automation |
| Filesystem | `10.17.17.32:8099` | NAS file access |
| Git | `10.17.17.32:8100` | Git operations |
| MCP Toolkit | `localhost:8080` | Local MCP hub |
| Iron Legion | `localhost:3000` | AI cluster routing |

---

## 3. AI CLUSTER CONFIGURATION

### 3.1 GPU Nodes (Ollama)

| Node | IP | GPU | VRAM | Endpoint |
|------|-----|-----|------|----------|
| ULTRON | localhost | RTX 5090 Laptop | 24GB | `http://localhost:11434/v1` |
| KAIJU | 10.17.17.11 | RTX 3090 | 24GB | `http://10.17.17.11:11437/v1` |

### 3.2 CPU Nodes (BitNet)

| Node | IP | Cores | Models | Endpoint |
|------|-----|-------|--------|----------|
| ULTRON-CPU | localhost | 16 | 2b, 3b, 8b | BitNet CLI |
| KAIJU-CPU | 10.17.17.11 | 16 | 2b, 3b, 8b | BitNet CLI |
| NAS-CPU | 10.17.17.32 | 4 | 0.7b, 2b | BitNet CLI |

### 3.3 Routing Strategy

```
1. Check local GPU (ULTRON) first
2. If busy (>85%), try KAIJU
3. If GPU unavailable, use BitNet CPU
4. Cloud fallback only if all local fails
```

---

## 4. @PEAK FEATURES & FUNCTIONALITY

### 4.1 PEAK Workflow Rules

| Rule | File | Function |
|------|------|----------|
| Troubleshooting/Decisioning | `troubleshooting_decisioning_workflow.mdc` | Full context before action |
| One-Shot No Mess | `one_shot_no_mess.mdc` | Perfect code every time |
| No Secrets Broadcast | `no_secrets_broadcast.mdc` | Security enforcement |
| Check Local First | `check_local_resources_first.mdc` | Search before creating |
| Fix Underlying Problem | `fix_underlying_problem.mdc` | Root cause, not suppression |
| Context Intent Baseline | `context_intent_baseline.mdc` | Confidence scoring |
| Git Workflow Validation | `git_workflow_validation.mdc` | Pre/post change checklists |
| Host Identity DNS | `host_identity_dns.mdc` | Kaiju=.11, NAS=.32 |
| Automation First | `automation_first.mdc` | AI does the heavy lifting |

### 4.2 PEAK Patterns

| Pattern | Description |
|---------|-------------|
| Test-First Policy | Always verify before implementing |
| WOPR Insights | 35 sparks from 10,000-year simulation |
| Parallel JHC Voting | 9x decision acceleration |
| Voice Command Chaining | 70% manual task reduction |
| Confidence-Based Autonomy | 60% supervision reduction |
| RR Methodology | Rest, Roast, Repair framework |

### 4.3 GAZE SYNC System

When JARVIS and operator in sync for 3+ seconds:
1. Visual cue (iris twinkle)
2. Audible cue (chime)
3. Flow state detection

---

## 5. IDE SETTINGS COMMONALITIES

### 5.1 Editor Configuration

```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "'Cascadia Code', 'Fira Code', monospace",
  "editor.fontLigatures": true,
  "editor.tabSize": 4,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll": "explicit"
  }
}
```

### 5.2 Cursor AI Settings

```json
{
  "cursor.ai.enabled": true,
  "cursor.ai.autoComplete": true,
  "cursor.ai.suggestions": true,
  "cursor.ai.chat": true,
  "cursor.ai.model": "ULTRON"
}
```

### 5.3 Custom Models Available

- ULTRON Cluster (localhost:11434)
- Iron Legion (10.17.17.11:11437)
- Qwen2.5 Coder 7B (local/remote)
- Qwen2.5 72B (local/remote)
- Llama3.2 3B/11B (local/remote)
- Codellama 13B (local/remote)

---

## 6. JARVIS CHAT IMPLEMENTATION

### 6.1 Core Module: `jarvis_chat_ca_fidelity.py`

```python
class JarvisChatCAFidelity:
    """Cursor Agent fidelity layer for JARVIS Chat"""
    
    # File operations
    def file_read(self, path: str, offset: int = None, limit: int = None) -> str
    def file_write(self, path: str, contents: str) -> bool
    def str_replace(self, path: str, old: str, new: str, replace_all: bool = False) -> bool
    def file_delete(self, path: str) -> bool
    def ls(self, path: str) -> List[str]
    def glob(self, pattern: str, target_dir: str = None) -> List[str]
    def grep(self, pattern: str, path: str = None) -> List[Match]
    
    # Shell operations
    def shell_exec(self, command: str, working_dir: str = None, timeout_ms: int = 30000) -> ShellResult
    def background_task(self, command: str) -> TaskHandle
    
    # Code intelligence
    def semantic_search(self, query: str, target_dirs: List[str] = None) -> List[Result]
    def read_lints(self, paths: List[str] = None) -> List[LintError]
    
    # Task management
    def todo_write(self, todos: List[Todo], merge: bool = True) -> bool
    def task_spawn(self, prompt: str, subagent_type: str = "generalPurpose") -> TaskResult
    
    # Web operations
    def web_search(self, query: str) -> SearchResults
    def web_fetch(self, url: str) -> str
    
    # Browser automation (via MCP)
    def browser_navigate(self, url: str) -> bool
    def browser_snapshot(self) -> PageSnapshot
    def browser_click(self, selector: str) -> bool
    def browser_type(self, selector: str, text: str) -> bool
    def browser_fill(self, selector: str, text: str) -> bool
    
    # AI routing
    def ai_chat(self, prompt: str, model: str = "auto") -> str
    def ai_complete(self, prefix: str, suffix: str = None) -> str
```

### 6.2 Integration Points

1. **Local AI Bridge**: `local_ai_context_bridge.py` - Routes to ULTRON/KAIJU/BitNet
2. **MCP Client**: `mcp_client.py` - Connects to homelab MCP servers
3. **Browser Automation**: Via `cursor-ide-browser` MCP
4. **Voice Integration**: `jarvis_voice_activation.py` + ElevenLabs MCP

---

## 7. EXTENSION UNINSTALLATION GUIDE

### 7.1 Extensions Safe to Uninstall (Functionality Retained in JARVIS)

| Extension | JARVIS Replacement |
|-----------|-------------------|
| Generic code formatters | `jarvis_format_code()` via LSP |
| Basic Git extensions | `jarvis_git_*()` functions |
| Simple file managers | `jarvis_file_*()` functions |
| Todo list extensions | `jarvis_todo_write()` |

### 7.2 Extensions Required (Not Replaceable)

| Extension | Reason |
|-----------|--------|
| Python (ms-python) | Language server, debugging |
| Pylance | Type checking, IntelliSense |
| GitLens | Deep Git integration |
| Lumina Core | IDE integration surface |

### 7.3 Post-Uninstall Checklist

- [ ] Verify JARVIS Chat connects to local AI clusters
- [ ] Test file operations via JARVIS
- [ ] Confirm browser automation works via MCP
- [ ] Validate voice commands (if enabled)
- [ ] Check all @PEAK rules still enforced

---

## 8. FRAMEWORKS INTEGRATION

### 8.1 Framework Categories (28+ Frameworks)

| Category | Count | Key Frameworks |
|----------|-------|----------------|
| **Workflow** | 2 | Water Workflow, Workflow Functionality |
| **Voice** | 2 | Voice Systems Test, Hybrid Voice |
| **Agent** | 4 | Agent Orchestrator, Subagent Delegation, Dynamic Spawner, Super Agent Backstories |
| **AI** | 4 | JARVIS AGI, Local AI Bridge, BitNet Inference, Three Tier AI |
| **Security** | 3 | Threat Response, Ethical Framework, AI Rights |
| **Platform** | 3 | Desktop, IDE, Mobile |
| **Collaboration** | 3 | Universal Collaboration, Coordination, Partnership |
| **Automation** | 3 | VA Action, Predictive Actions, WOPR Experiment |
| **Decision** | 2 | Database Engineering, Legal Consultation |
| **Monitoring** | 2 | Visual Detection, Syphon Data Intake |

### 8.2 Water Workflow System

The Water Workflow System provides autonomous execution philosophy:

```python
# Be like water - flow or escalate
jarvis.flow(
    task="deploy to production",
    context={"environment": "prod"},
    confidence="high"  # HIGH=flow, MEDIUM=caution, LOW=escalate
)
```

**Flow States:**
- `FLOWING` - Autonomous execution
- `DIVERTING` - Flowing around obstacle (escalation)
- `CONVERGING` - Flowing to destination (Grok)
- `BLOCKED` - Requires intervention

---

## 9. SUBAGENTS INTEGRATION

### 9.1 Subagent Domains (12+ Subagents)

| Domain | Subagents |
|--------|-----------|
| **Integration** | JARVIS Master, JARVIS Fulltime, Babelfish, Multi-Agent Orchestrator |
| **Multimedia** | ElevenLabs Voice Agent |
| **Workflow** | Project Manager, Autonomous AI Agent |
| **Monitoring** | IDE Notification, Outlier Detector |
| **Financial** | Financial Agent |
| **Life Domain** | Hybrid Psychologist |
| **Research** | Syphon Coordinator |

### 9.2 Subagent Delegation

```python
# Delegate task to specialized subagent
result = jarvis.delegate_task(
    agent_key="elevenlabs",
    task="synthesize voice",
    parameters={"text": "Hello world", "voice": "jarvis"}
)
```

### 9.3 Dynamic Subagent Spawning

```python
# Spawn subagent on demand
agent = jarvis.spawn_subagent("project_manager")

# Use predictive spawning via psychohistory
spawner = jarvis.load_framework("dynamic_spawner")
spawner.anticipate_and_spawn()
```

---

## 10. UNIFIED INTEGRATION

### 10.1 Single Entry Point

```python
from jarvis_chat_ca_fidelity import JarvisChatCAFidelity

jarvis = JarvisChatCAFidelity()

# Access all CA tools
content = jarvis.file_read("path/to/file.py")
result = jarvis.shell_exec("git status")

# Access all frameworks
frameworks = jarvis.list_frameworks()
water = jarvis.load_framework("water_workflow")

# Access all subagents
agents = jarvis.list_subagents()
jarvis.delegate_task("elevenlabs", "speak", {"text": "Hello"})

# System status
status = jarvis.system_status()
```

### 10.2 Module Dependencies

```
jarvis_chat_ca_fidelity.py
├── jarvis_chat_unified_integration.py (frameworks & subagents)
│   ├── water_workflow_system.py
│   ├── jarvis_agent_orchestrator.py
│   ├── jarvis_subagent_delegation.py
│   ├── dynamic_subagent_spawner.py
│   ├── local_ai_context_bridge.py
│   ├── bitnet_inference.py
│   └── ... (28+ frameworks)
└── (MCP integration - pending)
```

---

## 11. RELATED DOCUMENTATION

- [MAIN_GOAL_LOCAL_AI_CLUSTERS.md](MAIN_GOAL_LOCAL_AI_CLUSTERS.md) - Primary objective
- [homelab_mcp_hybrid_config.json](../../config/homelab_mcp_hybrid_config.json) - MCP configuration
- [local_ai_context_bridge.py](../../scripts/python/local_ai_context_bridge.py) - AI routing
- [bitnet_inference.py](../../scripts/python/bitnet_inference.py) - CPU inference
- [jarvis_chat_unified_integration.py](../../scripts/python/jarvis_chat_unified_integration.py) - Unified integration
- [.cursorrules](../../.cursorrules) - WOPR/PEAK rules

---

**Status**: This specification captures the current state of CA extensions, frameworks, and subagents. Implementation of `jarvis_chat_ca_fidelity.py` with `jarvis_chat_unified_integration.py` enables extension uninstallation while retaining full functionality including all 28+ frameworks and 12+ subagents.
