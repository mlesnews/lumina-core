# Local First Strategy — Kilo Code + Ollama

**Goal:** Spread remaining 43% Cursor usage across the month by using Kilo Code (local Ollama) as primary.

**Date:** 2026-02-04
**Days Remaining in Feb:** ~24 days
**Target:** ~1.8% Cursor usage per day max

---

## The Strategy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LOCAL FIRST HIERARCHY                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  🟢 TIER 1: KILO CODE (LOCAL) — USE FIRST                                   │
│  ├── Code completion / autocomplete                                         │
│  ├── Simple refactoring                                                     │
│  ├── Documentation generation                                               │
│  ├── Code explanations                                                      │
│  ├── Small file edits                                                       │
│  ├── Single-file bug fixes                                                  │
│  ├── Test generation (single file)                                          │
│  └── Quick Q&A about code                                                   │
│                                                                              │
│  🟡 TIER 2: KILO + LOCAL MODELS — TRY FIRST                                 │
│  ├── Multi-file refactoring (use /orchestrator mode)                        │
│  ├── Architecture decisions (use /architect mode)                           │
│  ├── Complex debugging (use /debug mode)                                    │
│  ├── Security review (use /security mode)                                   │
│  └── Research tasks (local web search)                                      │
│                                                                              │
│  🔴 TIER 3: CURSOR (CLOUD) — ONLY WHEN NEEDED                               │
│  ├── Large codebase-wide changes (Agent mode)                               │
│  ├── Complex multi-file coordinated edits                                   │
│  ├── Tasks requiring Claude's reasoning for novel problems                  │
│  ├── Web research that needs current 2026 data                              │
│  └── When local models can't handle the complexity                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Daily Usage Budget

| Metric | Value |
|--------|-------|
| **Remaining Cursor budget** | 43% |
| **Days left in Feb** | ~24 |
| **Daily allowance** | ~1.8% |
| **Reserve for complex tasks** | 10% |
| **Usable daily** | ~1.4% |

---

## Kilo Code Quick Start

### Switch to Kilo in VS Code/Cursor

1. **Open Kilo Code panel** (Ctrl+Shift+K or via extension)
2. **Select mode** based on task:

| Task Type | Mode | Shortcut |
|-----------|------|----------|
| Writing code | `/code` | Ctrl+Shift+1 |
| Questions only | `/ask` | Ctrl+Shift+2 |
| Design/planning | `/architect` | Ctrl+Shift+3 |
| Debugging | `/debug` | Ctrl+Shift+4 |
| Complex workflows | `/orchestrator` | Ctrl+Shift+5 |
| Fast iteration | `/yolo` | Ctrl+Shift+8 |

### Your Local Models (Iron Legion)

| Model | Best For | Context |
|-------|----------|---------|
| `codellama:13b` | Code generation, complex | 16K |
| `llama3.2:11b` | General, reasoning | 8K |
| `qwen2.5-coder:1.5b` | Fast completions | 4K |

**Endpoint:** `http://10.17.17.11:3001` (Kaiju via Iron Legion)

---

## Decision Flowchart

```
START: New coding task
   │
   ▼
Is it a simple task? ──Yes──► Use KILO (/code mode)
   │
   No
   │
   ▼
Can local model handle it? ──Yes──► Use KILO (/architect or /orchestrator)
   │
   No (need more reasoning power)
   │
   ▼
Is it < 3 files? ──Yes──► Use KILO with multiple passes
   │
   No (large codebase change)
   │
   ▼
Use CURSOR (Agent mode) ◄── Budget: ~1.4% daily
```

---

## Practical Examples

### ✅ Use Kilo For (LOCAL):

```
"Add a function to parse JSON in utils.py"
"Explain this regex pattern"
"Write tests for the UserService class"
"Refactor this function to use async/await"
"Add type hints to this module"
"Generate docstrings for these functions"
"Debug why this loop isn't working"
"Create a simple CLI script"
```

### 🔴 Use Cursor For (CLOUD):

```
"Refactor the entire authentication system across 20 files"
"Design and implement a new microservice architecture"
"Find and fix all instances of SQL injection across the codebase"
"Create a comprehensive test suite for the entire API"
"Migrate the database schema with coordinated code changes"
```

---

## Kilo Configuration Check

Run this to verify your Kilo setup:

```powershell
# Check Ollama is running on Kaiju
curl http://10.17.17.11:11434/api/tags

# Check Iron Legion load balancer
curl http://10.17.17.11:3000/health

# List available models
curl http://10.17.17.11:11434/api/tags | jq '.models[].name'
```

---

## VS Code / Cursor Settings for Local First

Add to your user settings:

```json
{
  "kilo-code.provider": "ollama",
  "kilo-code.apiUrl": "http://10.17.17.11:11434",
  "kilo-code.model": "codellama:13b",
  "kilo-code.autoTrigger": true,
  "kilo-code.suggestionDelay": 100,

  // Reduce Cursor auto-triggers
  "cursor.agent.preferLocal": true,
  "cursor.chat.autoSuggest": false,
  "cursor.autocomplete.enabled": false
}
```

---

## Mode-Specific Tips

### /code mode
- Best for actual implementation
- Uses `codellama:13b` by default
- Full tool access

### /ask mode (READ-ONLY)
- Perfect for learning, explanations
- Uses less compute
- Can't make changes

### /yolo mode
- Auto-approves safe operations
- Great for rapid iteration
- Still blocks destructive commands

### /orchestrator mode
- Breaks complex tasks into subtasks
- Each subtask runs isolated
- Good for multi-file work

---

## Weekly Check-In

Every few days, check your Cursor usage:

1. **Settings > Subscription** or account dashboard
2. **Target:** No more than ~10% usage per week
3. **If over budget:** Increase Kilo usage, reduce Cursor

---

## Emergency Fallback

If Ollama/Kaiju is down:

1. **Local fallback:** Ultron laptop with Ollama
2. **Cloud fallback:** Cursor (but budget carefully)

Check cluster status:
```powershell
python scripts/python/check_kilo_api_config.py
```

---

## Summary

| Priority | Tool | For |
|----------|------|-----|
| 1st | Kilo Code + Ollama | 90% of tasks |
| 2nd | Cursor Chat | Questions requiring Claude |
| 3rd | Cursor Agent | Large coordinated changes |

**Remember:** Local is free. Cloud is limited. Use local first.

---

**Tags:** #local-first #kilo #ollama #budget @JARVIS
