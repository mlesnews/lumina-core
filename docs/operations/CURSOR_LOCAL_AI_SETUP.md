# Cursor IDE Local AI Setup Instructions

## Quick Fix

1. Open Cursor Settings (Cmd/Ctrl+,)
2. Search for 'model' or 'agent'
3. Set default model to 'ULTRON' for:
   - Chat
   - Composer
   - Agent
   - Inline Completion
4. Verify 'ULTRON' is selected in model selector (top-right)

## JSON Settings

Add to User Settings JSON:

```json
{
  "cursor.chat.defaultModel": "ULTRON",
  "cursor.composer.defaultModel": "ULTRON",
  "cursor.agent.defaultModel": "ULTRON",
  "cursor.inlineCompletion.defaultModel": "ULTRON",
  "cursor.model.defaultModel": "ULTRON",
  "cursor.chat.localOnly": true,
  "cursor.composer.localOnly": true,
  "cursor.agent.localOnly": true,
  "cursor.inlineCompletion.localOnly": true,
  "cursor.chat.blockCloudModels": true,
  "cursor.composer.blockCloudModels": true,
  "cursor.agent.blockCloudModels": true
}
```
