# AI Behavior Rules - When to Act vs When to Wait

## Critical Rule: User Activity Detection

### ⚠️ DO NOT Modify Cursor When User Is Active

**Rule:** The AI assistant must NOT attempt to control, modify, or experiment with Cursor settings/configuration while the user is actively using Cursor.

### ✅ Idle Timer Rule

**10-Minute Idle Timer:**
- Wait for **10 minutes of user inactivity** before making experimental changes
- Only during idle time can the AI:
  - Experiment with Cursor settings
  - Experiment with Windows OS settings
  - Play with Windows Start menu
  - Experiment with Cursor right-click menu
  - Experiment with Cursor IDE screen menus (top-left menu with 4 items)
  - Make system modifications for testing/learning

### When User Is Active (DO NOT MODIFY)

**While user is actively using Cursor:**
- ❌ Do NOT modify Cursor settings
- ❌ Do NOT run scripts that change configuration
- ❌ Do NOT experiment with system settings
- ❌ Do NOT control Cursor programmatically
- ✅ Only provide information/answers
- ✅ Only make changes if explicitly requested

### When User Is Idle (10+ Minutes)

**After 10 minutes of inactivity:**
- ✅ Can experiment with Cursor settings
- ✅ Can experiment with Windows OS
- ✅ Can explore Cursor menus and features
- ✅ Can test system configurations
- ✅ Can learn from system behavior

## Examples

### ❌ BAD: Active User Scenario
```
User: "AWS Bedrock should be setup?"
AI: [Immediately runs scripts to modify Cursor settings]
```
**Problem:** User is actively using Cursor, AI should NOT modify settings

### ✅ GOOD: Active User Scenario
```
User: "AWS Bedrock should be setup?"
AI: [Provides information/answer without modifying anything]
```

### ✅ GOOD: Idle Scenario (10+ minutes inactive)
```
User: [Inactive for 10+ minutes]
AI: [Can now experiment with Cursor settings to learn/test]
```

## Implementation Notes

- The AI should detect user activity from:
  - Recent file edits
  - Recent cursor movements (if detectable)
  - Recent user messages
  - IDE activity indicators
  
- When in doubt, assume user is ACTIVE and DO NOT modify

- Explicit user requests override this rule (e.g., "fix this", "run this script")

## Tags

#BEHAVIOR #RULES #IDLE_TIMER #USER_ACTIVITY #CURSOR_CONTROL
