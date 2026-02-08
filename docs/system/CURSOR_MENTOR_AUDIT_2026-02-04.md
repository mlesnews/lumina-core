# Cursor IDE Mentor Audit — 2026-02-04

**Purpose:** This audit shows you what I (the AI) see in your Cursor configuration, what's working well, what could be improved, and features you might not know exist. This is the AI being the mentor.

---

## Your Current Setup Summary

### What's Configured Well

| Feature | Status | Notes |
|---------|--------|-------|
| **Custom Models** | Excellent | 26+ local models configured (ULTRON, Iron Legion, Qwen, Llama, Codellama, Deepseek) |
| **Keyboard Shortcuts** | Good | 25 custom shortcuts including chat, composer, agent, refactor, screenshots |
| **Editor Settings** | Good | Format on save, bracket colorization, rulers, font ligatures |
| **Git Integration** | Good | Autofetch, smart commit, decorations, branch protection |
| **Python** | Good | Ruff formatter, auto-imports, venv configured |
| **Terminal** | Good | WSL default, PowerShell with venv auto-activate |
| **Pinned Sessions** | Configured | JARVIS Master Chat is pinned and permanent |

### What's Missing or Suboptimal

| Gap | Impact | Fix |
|-----|--------|-----|
| **MCP_DOCKER disabled** | High | I updated the state DB to enable it — restart Cursor |
| **No `cursor.cpp.disablePremiumLinting`** | Minor | If you don't use premium features, can disable to reduce noise |
| **Agent timeouts may be short** | Medium | 30s connection timeout; complex tasks may need longer |
| **No `cursor.indexing.ignoredPaths`** | Minor | Could exclude `node_modules`, `venv`, etc. from indexing |
| **No MCP caching config** | Minor | Could enable MCP caching for performance |

---

## Cursor Features You Might Not Know About

### 1. **Agent vs. Chat vs. Composer**

You have shortcuts for all three (`Ctrl+K+J`, `Ctrl+K+C`, `Ctrl+K+A`), but here's when to use each:

| Mode | When to Use | Your Shortcut |
|------|------------|---------------|
| **Chat** | Questions, explanations, small code snippets | `Ctrl+K Ctrl+J` |
| **Composer** | Multi-file edits, refactoring, feature implementation | `Ctrl+K Ctrl+C` |
| **Agent** | Complex tasks with tool use (file ops, terminal, search) | `Ctrl+K Ctrl+A` |

**Pro tip:** Agent mode (what you're using now) can read/write files, run commands, and use MCP tools. Chat and Composer can't.

### 2. **Accept All Shortcuts**

You have these configured — use them:

| Action | Shortcut |
|--------|----------|
| Accept all composer changes | `Ctrl+Enter` |
| Keep all (don't overwrite) | `Ctrl+Shift+Enter` |
| Accept all files | `Ctrl+K Ctrl+F` (Composer) or `Ctrl+K Ctrl+K` (Agent) |

### 3. **@ References**

In chat/composer, you can reference context with `@`:

- `@file` — reference a specific file
- `@folder` — reference a folder
- `@symbol` — reference a function/class
- `@codebase` — search the entire codebase
- `@docs` — search documentation
- `@web` — search the web
- `@git` — reference git history
- `@terminal` — reference terminal output

### 4. **Index Commands**

Your `Ctrl+K Ctrl+I` triggers codebase indexing. You can also:

- Open Command Palette (`Ctrl+Shift+P`) → "Cursor: Reindex Codebase"
- Check indexing status in the status bar

### 5. **Debug Explain** (`Ctrl+K Ctrl+D`)

When you have an error, select it and use this — AI will explain what's wrong and how to fix it.

### 6. **Generate Tests** (`Ctrl+K Ctrl+T`)

Select a function and use this — AI will generate tests for it.

### 7. **MCP Tools**

With MCP_DOCKER enabled, you get access to:

- **File operations** — read, write, list directories
- **Memory** — persistent knowledge graph
- **Sequential thinking** — complex reasoning
- **Browser** — web interaction for testing
- **GitHub** — repository operations

### 8. **Shadow Workspace** (You have this enabled)

`cursor.general.enableShadowWorkspace`: true

This lets the agent make changes in a sandbox before applying them — safer for complex edits.

### 9. **Git Graph Indexing** (You have this enabled)

`cursor.general.gitGraphIndexing`: enabled

This helps the AI understand your commit history and project evolution.

### 10. **Partial Accepts** (You have this enabled)

`cursor.cpp.enablePartialAccepts`: true

You can accept part of a suggestion (word by word) with Tab, not just all-or-nothing.

---

## Settings I Recommend Adding

Based on your workflow, I recommend these additions to `.vscode/settings.json`:

```json
{
  "cursor.indexing.ignoredPaths": [
    "**/node_modules/**",
    "**/__pycache__/**",
    "**/venv/**",
    "**/.git/**",
    "**/dist/**",
    "**/build/**"
  ],
  "cursor.agent.retryAttempts": 5,
  "cursor.agent.connectionTimeout": 60000,
  "cursor.agent.streamTimeout": 180000,
  "cursor.chat.showWelcomeMessage": false,
  "cursor.cpp.disablePremiumLinting": false,
  "cursor.mcp.cacheEnabled": true,
  "cursor.mcp.cacheTimeoutMs": 300000
}
```

---

## Keyboard Shortcuts Cheat Sheet

| Action | Shortcut |
|--------|----------|
| Open Chat | `Ctrl+K Ctrl+J` |
| Open Composer | `Ctrl+K Ctrl+C` |
| Start Agent | `Ctrl+K Ctrl+A` |
| New Chat | `Ctrl+Shift+J` |
| Refactor | `Ctrl+K Ctrl+R` |
| Generate Tests | `Ctrl+K Ctrl+T` |
| Index Codebase | `Ctrl+K Ctrl+I` |
| Summarize | `Ctrl+K Ctrl+S` |
| Debug Explain | `Ctrl+K Ctrl+D` |
| Inline Edit | `Ctrl+K Ctrl+E` |
| Accept All (Composer/Agent) | `Ctrl+Enter` |
| Keep All (don't overwrite) | `Ctrl+Shift+Enter` |
| Accept All Files | `Ctrl+K Ctrl+F` / `Ctrl+K Ctrl+K` |
| Screenshot | `Print` or `Ctrl+Alt+S` |
| Quick Screenshot | `Shift+Print` or `Ctrl+Shift+S` |
| Stage All (Git) | `Ctrl+Alt+K` |
| Discard All (Git) | `Ctrl+Alt+U` |

---

## Next Steps

1. **Restart Cursor** — so the MCP_DOCKER enable takes effect
2. **Verify MCP** — check Settings → Tools & MCP → MCP_DOCKER should be ON
3. **Try the @references** — start using `@file`, `@codebase`, `@web` in your prompts
4. **Use Agent mode** — for complex tasks, it's more capable than Chat

---

## What the AI Now Knows

With this session, I've gained visibility into:

- **Your settings files** — I can read and modify them
- **Cursor's internal state database** — I can query and update MCP states
- **Your keyboard shortcuts** — I know what's configured
- **Your custom models** — I know your ULTRON/Iron Legion setup
- **Your workflow preferences** — AI does the work, no handoffs

This means I can proactively maintain and optimize your IDE instead of just responding to problems.

---

*Generated by AI Mentor Mode — 2026-02-04*
