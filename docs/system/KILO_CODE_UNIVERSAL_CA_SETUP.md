# Kilo Code as Universal Coding Assistant

## Vision

Make **Kilo Code** the single unified interface that incorporates features from all other CAs:
- Kilo Code (primary)
- Continue
- Cline
- Cursor Agent
- Jarvis Chat

## Feature Matrix - What Each CA Offers

| Feature | Kilo Code | Continue | Cline | Cursor | Jarvis Chat |
|---------|-----------|----------|-------|--------|-------------|
| Inline Completion | ✅ | ✅ | ❌ | ✅ | ❌ |
| Chat Interface | ✅ | ✅ | ✅ | ✅ | ✅ |
| Code Actions | ✅ | ✅ | ✅ | ✅ | ✅ |
| Terminal Execution | ✅ | ❌ | ✅ | ✅ | ✅ |
| Browser Automation | ✅ | ❌ | ✅ | ✅ | ✅ |
| File Operations | ✅ | ✅ | ✅ | ✅ | ✅ |
| MCP Support | ✅ | ✅ | ✅ | ✅ | ✅ |
| Voice Input | ⚠️ WIP | ❌ | ❌ | ❌ | ✅ (custom) |
| Local LLM | ✅ | ✅ | ✅ | ✅ | ✅ |
| Custom Modes | ✅ | ❌ | ❌ | ❌ | ✅ |
| Checkpoints/Undo | ✅ | ❌ | ❌ | ❌ | ❌ |
| Multi-file Edits | ✅ | ✅ | ✅ | ✅ | ✅ |

## Voice Input Setup - Kilo Voice System

Full-featured voice system with STT + TTS + IDE control.

### Features

| Feature | Status |
|---------|--------|
| Push-to-talk (Ctrl+Shift+K) | ✅ |
| Continuous listening mode | ✅ |
| Local Whisper transcription | ✅ |
| ElevenLabs TTS feedback | ✅ |
| IDE voice commands | ✅ |
| Terminal voice commands | ✅ |
| Git voice commands | ✅ |
| Auto-send to Kilo Code | ✅ |

### Quick Start

```bash
# Start in push-to-talk mode (recommended)
python scripts/python/kilo_voice_system.py --ptt

# Start in continuous listening mode
python scripts/python/kilo_voice_system.py --continuous
```

### Voice Commands

**System:**
- "stop listening" - Exit voice mode
- "pause" / "resume" - Pause/resume listening
- "quiet mode" / "voice mode" - Toggle TTS

**IDE Control:**
- "save" / "save file"
- "undo" / "redo"
- "format code"
- "go to line 42"
- "find search term"

**Terminal:**
- "run command npm install"
- "clear terminal"

**Git:**
- "git status"
- "git commit fix the bug"
- "git push" / "git pull"

**Navigation:**
- "open file app.py"
- "go to definition"
- "show files" / "show terminal"

**Chat (default):**
Any other speech is sent directly to Kilo Code chat.

## MCP Integration

Kilo Code supports MCP servers. Configure in `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "lumina-compute": {
      "command": "python",
      "args": ["path/to/mcp_server.py"],
      "env": {}
    }
  }
}
```

## Custom Modes for Universal CA

Create custom modes that match other CA behaviors:

```json
{
  "customModes": [
    {
      "name": "Jarvis Mode",
      "description": "Full Jarvis capabilities",
      "tools": ["shell", "browser", "file", "mcp"],
      "systemPrompt": "You are Jarvis..."
    },
    {
      "name": "Continue Mode",
      "description": "Continue-style interactions",
      "tools": ["file", "code"],
      "systemPrompt": "Focus on inline edits..."
    }
  ]
}
```

## Configuration for Universal CA

### 1. Point to Global Compute Pool

```json
{
  "ollamaBaseUrl": "http://localhost:8080",
  "ollamaModelId": "qwen2.5:32b-instruct-q4_K_M",
  "ollamaNumCtx": 32768
}
```

### 2. Enable All Tools

In Kilo Code settings:
- ✅ Shell/Terminal execution
- ✅ Browser automation
- ✅ File read/write
- ✅ MCP servers
- ✅ Checkpoints

### 3. Auto-Approval Settings

```json
{
  "autoApprovalEnabled": true,
  "allowedCommands": ["git", "npm", "python", "node"],
  "deniedCommands": ["rm -rf /", "format"]
}
```

## Implementation Plan

### Phase 1: Voice Input (High Priority)
- [ ] Create `kilo_voice_input.py` bridge
- [ ] Configure local Whisper for transcription
- [ ] Set up hotkey (Ctrl+Shift+K)
- [ ] Auto-paste to Kilo Code

### Phase 2: MCP Integration
- [ ] Register compute pool as MCP server
- [ ] Add file system MCP
- [ ] Add browser automation MCP

### Phase 3: Custom Modes
- [ ] Create "Jarvis Mode" with full tools
- [ ] Create "Code Review Mode"
- [ ] Create "Architect Mode" for planning

### Phase 4: Feature Parity
- [ ] Import Jarvis Chat features
- [ ] Import Continue inline features
- [ ] Import Cline tools

## Quick Start

```bash
# 1. Configure Kilo Code to use Global Compute Pool
python scripts/python/set_kilo_cluster.py

# 2. Install voice bridge
python scripts/python/kilo_voice_input.py --install

# 3. Test voice input
python scripts/python/kilo_voice_input.py --test

# 4. Use Kilo Code with voice!
# Press Ctrl+Shift+K to speak, release to send
```

---

Tags: @PEAK @KILO_CODE @UNIVERSAL_CA @VOICE #automation
