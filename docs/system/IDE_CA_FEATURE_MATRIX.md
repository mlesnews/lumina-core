# IDE & Coding Assistant Feature Matrix

**Purpose:** Complete mapping of features, functions, and capabilities across ALL IDEs and Coding Assistants in the Lumina ecosystem.

**Last Updated:** 2026-02-04

---

## Quick Answer: What Does Cursor Have That Kilo Code Doesn't?

| Feature | Cursor (Native) | Kilo Code | Gap |
|---------|-----------------|-----------|-----|
| **Claude 3.5/4 Sonnet** | ✅ Built-in | ❌ No | Cloud model access |
| **Agent Mode (multi-file)** | ✅ Coordinated edits | ⚠️ Limited | True codebase-wide orchestration |
| **@Codebase semantic search** | ✅ Built-in | ⚠️ Requires embeddings setup | Pre-indexed semantic search |
| **@Web real-time search** | ✅ Built-in | ❌ No | Live web search |
| **Shadow Workspace** | ✅ Safe sandboxing | ❌ No | Preview changes before apply |
| **Inline image understanding** | ✅ Vision models | ❌ No | Screenshot/diagram analysis |
| **MCP Tools (native)** | ✅ Deep integration | ⚠️ Extension-level | Native tool calling |
| **Background Agents** | ✅ Runs while you work | ❌ No | Async task processing |
| **Premium model rotation** | ✅ GPT-5, Claude 4, etc. | ❌ Local only | Latest cloud models |
| **Bugs/Tab autocomplete** | ✅ Cursor Tab | ⚠️ Basic completion | Multi-line ghost text |

### What Kilo Code Has That Cursor Doesn't:

| Feature | Kilo Code | Cursor | Advantage |
|---------|-----------|--------|-----------|
| **100% Local/Air-gapped** | ✅ | ❌ | Zero data leakage |
| **Unlimited usage** | ✅ Free | ❌ Token limits | No budget concerns |
| **@PEAK patterns** | ✅ Native | ❌ No | Pattern-first development |
| **R5 Living Context** | ✅ Integrated | ❌ No | Cross-session memory |
| **Custom modes** | ✅ 10+ modes | ⚠️ Limited | /code /ask /debug /yolo etc. |
| **Boomerang tasks** | ✅ Orchestrator mode | ❌ No | Subtask isolation |
| **JARVIS integration** | ✅ Native | ❌ No | Agent ecosystem |
| **Voice output** | ✅ ElevenLabs | ❌ No | TTS for responses |

---

## Complete Feature Matrix: All Coding Assistants

### Legend
- ✅ = Full support
- ⚠️ = Partial/limited
- ❌ = Not available
- 🔧 = Requires setup/config
- 💰 = Paid feature

---

## CODE GENERATION

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Inline completion** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Multi-line completion** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| **Ghost text preview** | ⚠️ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Fill-in-the-middle** | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **Code from comment** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Function generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Class generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Boilerplate generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## CHAT & CONVERSATION

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Chat panel** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Inline chat** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Context awareness** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Multi-turn memory** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Code explanation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Error explanation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Conversation export** | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ |

---

## REFACTORING & EDITING

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Rename symbol** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Extract function** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Extract variable** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Inline variable** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ⚠️ |
| **Multi-file refactor** | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| **Diff preview** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Accept/reject hunks** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |

---

## CONTEXT PROVIDERS (@-mentions)

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **@File** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **@Folder** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| **@Codebase** | 🔧 | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| **@Web** | ❌ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **@Docs** | 🔧 | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ |
| **@Terminal** | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **@Git** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| **@Problems** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |
| **@Clipboard** | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ |
| **@Image** | ❌ | ⚠️ | ❌ | ❌ | ✅ | ✅ | ❌ |

---

## AGENT & AUTOMATION

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Agent mode** | ⚠️ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Multi-file edits** | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Shell commands** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Browser automation** | ❌ | ❌ | ✅ | ⚠️ | ⚠️ MCP | ❌ | ❌ |
| **Background tasks** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| **PR from issue** | ❌ | ❌ | ❌ | ❌ | ⚠️ | ✅ | ❌ |
| **Auto-approve (YOLO)** | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Checkpoints/undo** | ✅ | ❌ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| **Boomerang tasks** | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |

---

## TESTING & DEBUGGING

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Test generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Test explanation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Debug assistance** | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Debug mode** | ✅ | ❌ | ❌ | ✅ | ⚠️ | ❌ | ❌ |
| **Error fix suggestions** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Stack trace analysis** | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ |

---

## DOCUMENTATION

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Docstring generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **README generation** | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **API docs** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ |
| **Comment generation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Architecture docs** | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ⚠️ | ❌ |

---

## MODEL & PROVIDER

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Local Ollama** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| **OpenAI** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Anthropic** | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Azure OpenAI** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ⚠️ | ❌ |
| **Google/Gemini** | ✅ | ✅ | ✅ | ⚠️ | ✅ | ❌ | ❌ |
| **Custom endpoint** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| **Model switching** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Auto model select** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ |

---

## SECURITY & PRIVACY

| Feature | Kilo Code | Continue | Cline | Roo | Cursor | Copilot | CodeWhisperer |
|---------|-----------|----------|-------|-----|--------|---------|---------------|
| **Fully offline** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Air-gap mode** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **No telemetry** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| **Local secrets** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| **PII protection** | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | ✅ |
| **Code filtering** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Security scanning** | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ✅ |

---

## UNIQUE FEATURES

| Feature | Tool | Description |
|---------|------|-------------|
| **@PEAK patterns** | Kilo Code | Pattern-first development, reusable solutions |
| **R5 Living Context** | Kilo Code | Cross-session persistent memory |
| **Boomerang tasks** | Kilo/Roo | Orchestrate subtasks with isolation |
| **JARVIS integration** | Kilo Code | Agent ecosystem, voice, helpdesk |
| **Custom modes** | Kilo/Roo | /code /ask /debug /yolo /architect |
| **Shadow Workspace** | Cursor | Preview changes before applying |
| **Background agents** | Cursor | Async multi-file tasks |
| **PR from issue** | Copilot | Auto-create PR from GitHub issue |
| **Reference tracking** | CodeWhisperer | Shows code references for licensing |
| **Repository map** | Continue | Semantic codebase structure |

---

## IDE FEATURE MATRIX

### Legend
- ✅ = Full support
- ⚠️ = Partial/limited
- ❌ = Not available

| Feature | Cursor | VS Code | JetBrains | Neovim |
|---------|--------|---------|-----------|--------|
| **Kilo Code** | ✅ | ✅ | ✅ | ✅ |
| **Continue** | ✅ | ✅ | ❌ | ⚠️ |
| **Cline** | ✅ | ✅ | ⚠️ | ❌ |
| **Roo** | ✅ | ✅ | ❌ | ❌ |
| **Native AI chat** | ✅ | ⚠️ | ⚠️ | ❌ |
| **Agent mode** | ✅ | ⚠️ ext | ⚠️ | ❌ |
| **MCP tools** | ✅ | ⚠️ ext | ❌ | ❌ |
| **Inline completion** | ✅ | ✅ | ✅ | ✅ |
| **Copilot support** | ✅ | ✅ | ✅ | ✅ |
| **CodeWhisperer** | ⚠️ | ✅ | ✅ | ❌ |
| **Multi-file edit** | ✅ | ⚠️ | ⚠️ | ⚠️ |
| **Git integration** | ✅ | ✅ | ✅ | ✅ |
| **Task system** | ✅ | ✅ | ✅ | ⚠️ |
| **Debug integration** | ✅ | ✅ | ✅ | ⚠️ |
| **Remote dev** | ⚠️ | ✅ | ✅ | ✅ |
| **Vim motions** | ✅ ext | ✅ ext | ✅ | ✅ |
| **Performance** | Good | Good | Heavy | Fast |
| **Cost** | 💰 | Free | 💰 | Free |

---

## DECISION GUIDE: When to Use What

### Use KILO CODE (LOCAL) When:
- ✅ Simple code generation
- ✅ Single-file edits
- ✅ Documentation
- ✅ Test generation (single file)
- ✅ Code explanation
- ✅ Debugging (single context)
- ✅ Refactoring (single file)
- ✅ Sensitive/PII code
- ✅ Unlimited iteration needed
- ✅ Air-gap required

### Use CURSOR (CLOUD) When:
- ✅ Large codebase-wide changes
- ✅ Complex multi-file orchestration
- ✅ @Web research needed
- ✅ @Image/screenshot analysis
- ✅ Novel architecture design
- ✅ Tasks requiring Claude 4+ reasoning
- ✅ Background async tasks

### Use CONTINUE When:
- ✅ Alternative completion suggestions
- ✅ Quick inline completions
- ✅ @Codebase semantic search
- ✅ Repository map visualization

### Use CLINE When:
- ✅ Browser automation needed
- ✅ Plan-first approach preferred
- ✅ Checkpoint-based development
- ✅ Human-in-the-loop required

### Use ROO When:
- ✅ Complex orchestrated workflows
- ✅ Boomerang task isolation
- ✅ Custom mode switching
- ✅ Multi-step project management

### Use COPILOT When:
- ✅ PR creation from GitHub issues
- ✅ GitHub-native integration needed
- ✅ Team collaboration features
- ✅ Already in GitHub ecosystem

### Use CODEWHISPERER When:
- ✅ AWS ecosystem development
- ✅ Code reference/licensing concerns
- ✅ Security scanning required

---

## Summary Table: Feature Gaps

| Gap Area | Missing In | Available In | Priority |
|----------|-----------|--------------|----------|
| Real-time web search | Kilo/Continue/Cline | Cursor/Copilot | Medium |
| Vision/image analysis | All local CAs | Cursor/Copilot | Low |
| Background agents | All local CAs | Cursor/Copilot | Medium |
| Shadow workspace | All except Cursor | Cursor | Low |
| PR from issue | All except Copilot | Copilot | Medium |
| Boomerang tasks | All except Kilo/Roo | Kilo/Roo | High |
| Air-gap mode | Cloud CAs | Local CAs | Critical |
| Unlimited usage | Cloud CAs | Local CAs | Critical |
| @PEAK patterns | All except Kilo | Kilo | High |
| R5 context | All except Kilo | Kilo | High |

---

**Tags:** #feature-matrix #ca #ide #comparison @JARVIS @LUMINA
