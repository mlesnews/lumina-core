# R5 Living Context Matrix + Local AI Context Bridge Integration

**Date**: 2026-02-02
**Status**: ✅ Integrated
**Tags**: #R5 #CONTEXT-BRIDGE #LOCAL-AI #KNOWLEDGE-PIPELINE @JARVIS @LUMINA

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LUMINA KNOWLEDGE PIPELINE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────┐      ┌─────────────────────┐             │
│   │  R5 LIVING CONTEXT  │      │  LOCAL AI CONTEXT   │             │
│   │       MATRIX        │      │       BRIDGE        │             │
│   │                     │      │                     │             │
│   │  • IDE Sessions     │      │  • Docs (6,675)     │             │
│   │  • @PEAK Patterns   │─────▶│  • Config files     │             │
│   │  • @WHATIF Scenarios│      │  • Cursor Rules     │             │
│   │  • Learned Wisdom   │      │  • R5 Matrix ←──────│             │
│   │                     │      │                     │             │
│   └──────────┬──────────┘      └──────────┬──────────┘             │
│              │                            │                         │
│              │      AGGREGATED            │                         │
│              │      KNOWLEDGE             │                         │
│              └───────────┬────────────────┘                         │
│                          │                                          │
│                          ▼                                          │
│              ┌───────────────────────┐                              │
│              │   SYSTEM PROMPT       │                              │
│              │   INJECTION           │                              │
│              │                       │                              │
│              │  • R5 @PEAK patterns  │                              │
│              │  • Retrieved docs     │                              │
│              │  • Project context    │                              │
│              └───────────┬───────────┘                              │
│                          │                                          │
│                          ▼                                          │
│              ┌───────────────────────┐                              │
│              │   LOCAL OLLAMA        │                              │
│              │   (qwen2.5:7b, etc)   │                              │
│              │                       │                              │
│              │   NOW HAS:            │                              │
│              │   ✅ Project knowledge │                              │
│              │   ✅ R5 patterns       │                              │
│              │   ✅ Full context      │                              │
│              └───────────────────────┘                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Knowledge Sources

### R5 Living Context Matrix (Dynamic)

| Feature | Description |
|---------|-------------|
| **Source** | IDE chat sessions (Cursor, VS Code, etc.) |
| **Extracts** | @PEAK patterns, @WHATIF scenarios |
| **Storage** | `data/r5_living_matrix/` |
| **Output** | `LIVING_CONTEXT_MATRIX_PROMPT.md` |
| **Integration** | Azure Service Bus, n8n, Jupyter |

**Example @PEAK Pattern**:
> **Handle-First Rebranding Protocol**: Secure all target handles (GitHub, X, Discord, Domain) *before* releasing old handles during rebrands to prevent identity hijacking.

### Local AI Context Bridge (Static + R5)

| Feature | Description |
|---------|-------------|
| **Indexed** | 6,675 documents, 12,483 topics |
| **Sources** | docs/, config/, .cursor/rules/, R5 data |
| **Retrieval** | Keyword-based relevance scoring |
| **Injection** | System prompt with relevant context |

---

## How Integration Works

### 1. R5 Captures Patterns

```python
# R5 extracts @PEAK from IDE sessions
r5.ingest_session({
    "messages": [...],
    "patterns": ["@PEAK: Handle-First Protocol..."]
})
```

### 2. Context Bridge Indexes R5

```python
# Context Bridge indexes R5's output
DOC_PATHS = [
    ...
    "data/r5_living_matrix/",  # R5 patterns included
]
```

### 3. Local AI Gets Full Context

```python
# When you chat, system prompt includes:
# 1. R5 Living Context Matrix (learned patterns)
# 2. Retrieved relevant docs
# 3. Project-specific context

bridge.chat_with_context("What @PEAK patterns exist?")
```

---

## Usage

### Index Everything (Including R5)

```bash
python scripts/python/local_ai_context_bridge.py --reindex
```

### Chat with Full Context

```bash
python scripts/python/local_ai_context_bridge.py --chat "What @PEAK patterns have we learned?" --model qwen2.5:7b
```

### Run R5 Aggregation

```bash
python scripts/python/r5_living_context_matrix.py
```

---

## What This Solves

**Before**: Local AI said "I don't have access to local files"

**After**: Local AI has:
- ✅ 6,675 indexed documents
- ✅ 12,483 searchable topics
- ✅ R5 @PEAK patterns (learned wisdom)
- ✅ Project configuration knowledge
- ✅ Cursor rules and memories

---

## Files

| File | Purpose |
|------|---------|
| `scripts/python/r5_living_context_matrix.py` | R5 pattern extraction system |
| `scripts/python/local_ai_context_bridge.py` | Context injection for local AI |
| `data/r5_living_matrix/LIVING_CONTEXT_MATRIX_PROMPT.md` | R5 output (injected into prompts) |
| `data/local_ai_context/document_index.json` | Indexed document metadata |
| `data/local_ai_context/topic_index.json` | Topic-to-document mapping |

---

## Performance Note

The integration is complete, but local AI inference is slow due to:
- GPU VRAM shared by 31 Windows apps
- Even 7B models show 31% CPU offload
- Recommendation: Close Edge/Chrome tabs, Docker, Claude Desktop before heavy AI use

See: `docs/system/OLLAMA_PERFORMANCE_TUNING_GUIDE.md`
