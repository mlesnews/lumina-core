# Cursor Model Visibility Guide - Show Active AI Model in Chat

**Date**: 2025-01-24  
**Status**: ⚠️ **CRITICAL UX ISSUE - LONGSTANDING REQUEST**  
**Tag**: @CURSOR #ux #model-visibility #chat-session

---

## Problem Statement

**User Request**: Display the **current active/live AI model** in the Cursor chat session interface.

**Issue**: It's currently **difficult or impossible to see which model is actively being used** during chat sessions, making it hard to verify:
- If local models (ULTRON, IRON LEGION) are actually active
- If cloud models (Claude, GPT) are being used instead
- Which specific model is responding
- Model switching status

**Impact**: 
- ❌ Cannot verify local AI usage
- ❌ Cannot confirm cost control (local vs cloud)
- ❌ Unclear which model capabilities are available
- ❌ Difficult to troubleshoot model selection issues

---

## Current State in Cursor

### Where Model Information May Appear

1. **Chat Panel Header**:
   - Model selector dropdown (if visible)
   - May show selected model
   - May not show actual active model

2. **Chat Message Indicators**:
   - Some versions show model name per message
   - Not consistently visible
   - May require hover or click

3. **Settings**:
   - Default model set in settings
   - Actual active model may differ
   - No live indicator

### Limitations

- Model selector may not be visible by default
- Selected model ≠ active model (fallback may occur)
- No persistent model indicator in chat UI
- No visual feedback when model changes

---

## Solutions & Workarounds

### Solution 1: Check Model Selector Dropdown (If Available)

1. **Open Chat Panel**:
   - Press `Ctrl+L` (or `Cmd+L` on Mac)
   - Or click chat icon in sidebar

2. **Look for Model Selector**:
   - Check top of chat panel
   - Look for dropdown/selector showing model name
   - Click to see available models

3. **Verify Selected Model**:
   - Check if selected model matches expected (ULTRON, etc.)
   - Note: Selected may not equal active (if connection fails)

### Solution 2: Check Response Metadata (If Available)

1. **Inspect Chat Messages**:
   - Hover over AI response messages
   - Look for tooltips showing model info
   - Check message metadata (if accessible)

2. **Check Network Activity** (Advanced):
   - Open browser DevTools (if Cursor uses webview)
   - Monitor network requests
   - Check API endpoints being called:
     - `localhost:11434` = Local Ollama
     - `api.anthropic.com` = Claude (cloud)
     - `api.openai.com` = GPT (cloud)

### Solution 3: Test with Model-Specific Prompts

Ask the model to identify itself:

```
"What model are you? Please identify your name and version."
```

Expected responses:
- ULTRON/local models: May mention Ollama, model name
- Claude: "I'm Claude, an AI assistant..."
- GPT: "I'm ChatGPT, a language model..."

**Limitation**: Model may not always identify itself accurately.

### Solution 4: Monitor Usage Dashboard

1. **Check Cursor Usage Dashboard** (if available):
   - Look for API usage stats
   - Check which providers are being used
   - Monitor token usage per model

2. **Check Anthropic Dashboard** (for cloud):
   - If using Claude, check Anthropic dashboard
   - Monitor API calls and usage
   - If usage increases = using cloud

### Solution 5: Force Model Indicator (Settings)

Try these settings to make model more visible:

```json
{
  "cursor.chat.showModel": true,
  "cursor.chat.modelIndicator": true,
  "cursor.chat.displayActiveModel": true,
  "cursor.composer.showModel": true,
  "cursor.agent.showModel": true
}
```

**Note**: These settings may not exist in all Cursor versions.

---

## Recommended Workflow

### Daily Verification Checklist

1. **Before Starting Work**:
   - [ ] Open Cursor Chat (`Ctrl+L`)
   - [ ] Check model selector dropdown
   - [ ] Verify shows ULTRON or local model (not Claude/GPT)
   - [ ] Take screenshot if possible

2. **During Chat Sessions**:
   - [ ] Periodically check model selector
   - [ ] Ask model to identify itself if uncertain
   - [ ] Monitor network activity (if possible)
   - [ ] Note any model switching

3. **After Session**:
   - [ ] Verify usage dashboard (if available)
   - [ ] Check Anthropic dashboard (should be zero if using local)
   - [ ] Document which model was used

---

## Enhancement Request: Ideal Solution

### What Should Be Visible

1. **Persistent Model Indicator**:
   - Always visible in chat panel header
   - Shows current active model name
   - Updates when model changes
   - Color-coded (green = local, red = cloud)

2. **Per-Message Model Tags**:
   - Each message shows which model generated it
   - Small badge/indicator next to message
   - Clickable for model details

3. **Model Status Indicator**:
   - Connection status (connected/disconnected)
   - Model health/availability
   - Response time indicator

4. **Model History**:
   - Show model switching history
   - Log of which models were used when
   - Fallback events logged

### Feature Request Template

```
Feature: Persistent Model Indicator in Cursor Chat

Request: Always show the active AI model in the chat interface

Rationale:
- Users need to verify local vs cloud model usage
- Cost control requires model visibility
- Troubleshooting needs model identification
- User experience requires transparency

Location: Chat panel header, persistent and always visible

Details:
- Show model name (e.g., "ULTRON (qwen2.5:72b)")
- Show endpoint (e.g., "localhost:11434")
- Color code (green = local, yellow = hybrid, red = cloud)
- Update in real-time when model changes
- Include connection status indicator
```

---

## Current Workarounds Summary

| Method | Effectiveness | Ease of Use | Reliability |
|--------|--------------|-------------|-------------|
| Model Selector Dropdown | ⭐⭐⭐ Medium | ⭐⭐⭐ Easy | ⭐⭐ Medium |
| Network Monitoring | ⭐⭐⭐⭐ High | ⭐⭐ Hard | ⭐⭐⭐⭐ High |
| Model Self-Identification | ⭐⭐ Low | ⭐⭐⭐ Easy | ⭐⭐ Medium |
| Usage Dashboard | ⭐⭐⭐⭐ High | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ High |
| Settings Indicators | ⭐ Unknown | ⭐⭐⭐ Easy | ⭐ Unknown |

---

## Implementation Script (Future)

Create a helper script to check active model:

```python
#!/usr/bin/env python3
"""
Check Active Cursor Model
Monitors Cursor chat to identify active AI model
"""

# Future implementation:
# 1. Parse Cursor chat logs
# 2. Monitor network activity
# 3. Query Ollama API status
# 4. Display active model indicator
```

**Status**: Not yet implemented - placeholder for future enhancement

---

## Related Documentation

- **ULTRON Activation**: `docs/system/ULTRON_COMPLETE_IMPLEMENTATION_GUIDE.md`
- **IRON LEGION Activation**: `docs/system/IRON_LEGION_COMPLETE_IMPLEMENTATION_GUIDE.md`
- **Switch to Local AI**: `docs/system/SWITCH_CURSOR_TO_LOCAL_AI.md`
- **Local AI Usage Proof**: `docs/system/LOCAL_AI_USAGE_PROOF.md`

---

## Action Items

### Immediate (User)
- [ ] Check model selector dropdown in chat
- [ ] Test model self-identification prompts
- [ ] Monitor usage dashboard
- [ ] Document findings

### Short-term (Development)
- [ ] Create model verification script
- [ ] Add model indicator to Cursor settings
- [ ] Document Cursor version-specific differences
- [ ] Create troubleshooting guide

### Long-term (Feature Request)
- [ ] Submit feature request to Cursor team
- [ ] Create persistent model indicator extension
- [ ] Implement model monitoring dashboard
- [ ] Add model history logging

---

**Last Updated**: 2025-01-24  
**Status**: ⚠️ **CRITICAL UX ISSUE - NEEDS RESOLUTION**  
**Maintained By**: @CURSOR #ux