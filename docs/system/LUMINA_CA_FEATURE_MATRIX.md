# Lumina Coding Assistant - Feature Matrix

## Vision

Lumina aggregates **peak features** from all major coding assistants while providing unified access to both local AI clusters and cloud providers with free/premium tiers.

## Feature Comparison: Lumina vs Competition

| Feature | Kilo | Cline | Continue | Cursor | Aider | Claude Code | **Lumina** |
|---------|------|-------|----------|--------|-------|-------------|------------|
| **Model Access** |
| Local Ollama | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| Multi-node cluster | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| OpenAI | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Anthropic | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Google Gemini | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ |
| Free tier aggregation | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Model aliases (ULTRON) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **UI/UX** |
| Sidebar chat | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Model selector | ✅ | ✅ | ✅ | ✅ | CLI | CLI | ✅ |
| Voice input | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Voice output (TTS) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 🔄 |
| Image upload | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| Streaming responses | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 |
| **Context** |
| Current file | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Selection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| @ file mentions | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 |
| @ symbol mentions | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | 🔄 |
| Codebase indexing | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | 🔄 |
| **Autonomous** |
| File editing | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 |
| File creation | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 |
| Terminal commands | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 |
| Git integration | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 🔄 |
| **Advanced** |
| Extended thinking | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 🔄 |
| Multi-file composer | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 |
| Tab completion | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | 🔄 |
| MCP tools | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | 🔄 |

**Legend:** ✅ Implemented | 🔄 Planned | ❌ Not Available

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    LUMINA IDE EXTENSION                        │
│  • JARVIS Chat (sidebar)                                       │
│  • Context manager (files, selection, @mentions)               │
│  • Voice I/O (Web Speech + ElevenLabs)                         │
│  • Code actions (apply, diff, insert)                          │
└────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────────┐
│                    LUMINA AI GATEWAY                           │
│  Port: 11435 | OpenAI-compatible API                           │
│  • Model registry & aliases                                    │
│  • Routing & load balancing                                    │
│  • Health monitoring                                           │
│  • Quota management                                            │
└────────────────────────────────────────────────────────────────┘
           │                    │                    │
           ▼                    ▼                    ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│  LOCAL CLUSTER   │  │   FREE TIER      │  │  PREMIUM TIER    │
│                  │  │                  │  │                  │
│ Kaiju (RTX 4090) │  │ Groq             │  │ OpenAI           │
│ • qwen2.5:72b    │  │ • llama-3.3-70b  │  │ • gpt-4o         │
│ • ULTRON alias   │  │                  │  │ • o1             │
│                  │  │ Together AI      │  │                  │
│ NAS (CPU)        │  │ • DeepSeek-R1    │  │ Anthropic        │
│ • Small models   │  │ • Qwen-Coder     │  │ • claude-sonnet  │
│                  │  │                  │  │                  │
│ Ultron (Laptop)  │  │ OpenRouter       │  │ Google           │
│ • Mobile GPU     │  │ • Free models    │  │ • gemini-2.0     │
└──────────────────┘  └──────────────────┘  └──────────────────┘
```

## Model Aliases

Quick access to common use cases:

| Alias | Provider | Model | Use Case |
|-------|----------|-------|----------|
| `ULTRON` | Local | qwen2.5:72b | Primary supermodel |
| `fast` | Groq | llama-3.1-8b | Quick responses |
| `smart` | Anthropic | claude-sonnet | Best overall |
| `code` | Together | Qwen-Coder-32B | Coding tasks |
| `reason` | OpenAI | o1 | Complex reasoning |
| `vision` | OpenAI | gpt-4o | Image analysis |
| `local-fast` | Local | llama3.2:3b | Fast local |
| `local-code` | Local | qwen2.5-coder:7b | Local coding |

## Implementation Status

### Phase 1: Foundation (Current)
- [x] AI Gateway config
- [x] Gateway service (FastAPI)
- [x] Basic IDE chat panel
- [x] Model selector
- [x] Context toggle
- [x] Voice input (Web Speech)
- [x] Image upload
- [x] Voice Actor service (ElevenLabs + fallback)
- [x] Voice output (TTS) in chat
- [x] Multiple voice personas (JARVIS, FRIDAY, ULTRON)

### Phase 2: Integration
- [ ] Gateway startup on boot
- [ ] Cloud provider authentication
- [ ] Streaming responses
- [ ] Health dashboard
- [ ] Quota tracking
- [ ] NVIDIA Audio2Face integration (avatar)

### Phase 3: Advanced Features
- [ ] @ file mentions
- [ ] Codebase indexing
- [ ] Autonomous file editing
- [ ] Git integration
- [ ] Whisper local STT

### Phase 4: Polish
- [ ] Extended thinking mode
- [ ] Multi-file composer
- [ ] MCP tool integration
- [ ] Performance optimization

## Configuration

### Gateway Config
`config/ai_gateway_config.json` - Model registry, endpoints, aliases

### API Keys (in Azure Key Vault or .env)
```
GROQ_API_KEY=...
TOGETHER_API_KEY=...
OPENROUTER_API_KEY=...
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_AI_API_KEY=...
ELEVENLABS_API_KEY=...
```

## Usage

### Start Gateway
```powershell
.\services\ai_gateway\start_gateway.ps1
```

### Test Gateway
```powershell
# List models
curl http://127.0.0.1:11435/v1/models

# Chat with alias
curl -X POST http://127.0.0.1:11435/v1/chat/completions `
  -H "Content-Type: application/json" `
  -d '{"model": "ULTRON", "messages": [{"role": "user", "content": "Hello"}]}'
```

## References

- `config/ai_gateway_config.json` - Gateway configuration
- `services/ai_gateway/gateway.py` - Gateway service
- `applications/ide_chat/` - IDE chat extension
- `config/host_identity_registry.json` - Cluster endpoints
