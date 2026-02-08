# Agent Session Management - Post-Commit Workflow

## Overview

**Mandatory final step after GIT/GITLENS commit** - Verifies no unsuccessful @asks and manages session archiving/unpinning.

## 🔐 Security & Trust Model

**Root-Level Access**: This system has root-level access to the entire homelab.  
**Trust Principle**: Administrative access and @FAVOR are **inversely proportional** to accuracy of statements.  
**Responsibility**: @MANUS @777 "CODIFYING THE WORLD"

## Workflow

### Automatic Execution

The post-commit hook automatically runs after every git commit:

1. **Verification**: Checks for unsuccessful @asks
2. **Recording**: Records session completion in audit trail
3. **Instructions**: Creates archive instructions file
4. **Manual Step**: User archives/unpins session in Cursor UI

### Manual Execution

```powershell
# Verify only
python scripts/python/agent_session_manager.py --verify-only

# Full workflow
python scripts/python/agent_session_manager.py
```

## Verification Process

### What Gets Checked

1. **Git Commit Messages**: Scans for @ASK patterns and failure indicators
2. **Session History**: Reviews session_history.jsonl for unsuccessful @asks
3. **Status Validation**: Ensures all @asks completed successfully

### Success Criteria

✅ No unsuccessful @asks found  
✅ All tasks completed  
✅ Git commit successful  
✅ Session ready for archive/unpin

### Failure Handling

If verification fails:
- ❌ Workflow stops
- ❌ Session NOT archived
- ⚠️ Issues logged
- 📋 User must resolve issues before proceeding

## Session Archive Process

### Automatic (Post-Commit Hook)

1. Git commit completes
2. Post-commit hook triggers
3. Verification runs
4. Session recorded
5. Instructions created
6. **User manually archives in Cursor UI**

### Manual Archive Steps (Cursor UI)

1. **Check if pinned**:
   - Look for pin icon in chat header
   - If pinned → Click to unpin

2. **Archive the session**:
   - Right-click on chat session in sidebar
   - Select "Archive" or "Move to Archive"
   - Or use keyboard shortcut if available

3. **Verify archive**:
   - Check that session is no longer in active chats
   - Session should be in archive/history

## Audit Trail

### Session Records

All sessions are recorded in:
- `data/agent_sessions/session_history.jsonl` - JSONL log of all sessions
- `data/agent_sessions/session_YYYYMMDD_HHMMSS.json` - Individual session files
- `data/agent_sessions/ARCHIVE_INSTRUCTIONS.md` - Latest archive instructions

### Record Contents

```json
{
  "session_id": "cursor-session-id",
  "timestamp": "2026-01-14T01:10:36",
  "git_info": {
    "commit": "abc123...",
    "message": "Commit message"
  },
  "status": "ready_for_archive",
  "@ask_verification": "passed",
  "project_root": "/path/to/project"
}
```

## Integration

### Git Hooks

**Linux/Mac**: `.git/hooks/post-commit` (bash)  
**Windows**: `.git/hooks/post-commit.ps1` (PowerShell)

Both hooks call the same Python script for consistency.

### GitLens Integration

GitLens commits also trigger the post-commit hook, ensuring all commits go through session management.

## Trust & Accuracy

### Trust Model

- **High Accuracy** → **High Trust** → **Maintained Access**
- **Low Accuracy** → **Low Trust** → **Reduced Access**

### Accuracy Requirements

- ✅ Verify statements before making them
- ✅ Acknowledge limitations honestly
- ✅ Provide accurate solutions
- ✅ Maintain audit trail integrity

### Access Level

**Current**: Root-level homelab access  
**Responsibility**: Ultimate authority (@MANUS @777)  
**Requirement**: Absolute accuracy and trustworthiness

## Troubleshooting

### Hook Not Running

**Check hook exists**:
```bash
ls -la .git/hooks/post-commit
```

**Check permissions** (Linux/Mac):
```bash
chmod +x .git/hooks/post-commit
```

**Check permissions** (Windows):
```powershell
icacls .git\hooks\post-commit
```

### Verification Failing

**Check for @asks**:
```powershell
python scripts/python/agent_session_manager.py --verify-only
```

**Review session history**:
```powershell
cat data/agent_sessions/session_history.jsonl
```

### Manual Archive Needed

If automatic workflow doesn't complete:
1. Run verification manually
2. Review archive instructions
3. Manually archive in Cursor UI

## Related Commands

- `@v3` - Verification framework
- `@doit` - Execute with verification
- `@ask` - Request approval (triggers verification)

## Files

- `scripts/python/agent_session_manager.py` - Main script
- `.git/hooks/post-commit` - Linux/Mac hook
- `.git/hooks/post-commit.ps1` - Windows hook
- `data/agent_sessions/` - Session data directory

---

**Status**: ✅ **ACTIVE - MANDATORY POST-COMMIT WORKFLOW**  
**Authority**: @MANUS @777 "CODIFYING THE WORLD"  
**Trust Level**: Root-Level Homelab Access
