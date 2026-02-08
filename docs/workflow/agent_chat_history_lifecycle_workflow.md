# Agent Chat History Lifecycle Workflow

## Overview

Complete workflow for managing agent chat session histories from inception/creation through successful completion, V3 verification, and archival. This workflow ensures proper session management and maintains audit trails throughout the agent lifecycle.

**Tags**: #SESSION_MANAGEMENT #AGENT_LIFECYCLE #V3_VERIFICATION #ARCHIVE #WORKFLOW @JARVIS @MANUS @LUMINA

---

## Workflow Stages

### Stage 1: Session Creation/Inception

**Status**: `ACTIVE` → `PINNED` (if important)

**Actions**:
1. New agent chat session created in Cursor IDE
2. Session metadata initialized:
   - Session ID generated
   - Timestamp recorded
   - Initial status: `ACTIVE`
   - Message count: 0
   - Agent count: 0

**Files Created**:
- Session data in Cursor IDE internal storage
- Optional: Session metadata file in `data/agent_sessions/`

**Workflow Manager**: `CursorChatSessionWorkflowManager`
- Analyzes session for importance
- May auto-pin if high activity score
- Tracks session metadata

**Key Components**:
- `cursor_chat_session_workflow_manager.py` - Session workflow management
- Session metadata tracking
- Activity score calculation

---

### Stage 2: Active Development

**Status**: `ACTIVE` or `PINNED`

**Actions**:
1. Agent chat session actively used
2. Messages exchanged
3. Tasks completed
4. Code changes made
5. Session metadata updated:
   - Message count incremented
   - Last activity timestamp updated
   - Activity score calculated
   - Topics extracted from messages

**Tracking**:
- Session history maintained in `session_history.jsonl`
- Individual session files created: `session_YYYYMMDD_HHMMSS.json`
- Activity score: Based on recency, message count, agent count

**Workflow Patterns** (if applicable):
- `ACTIVE_TO_PIN` - Pin important active sessions
- `DUPLICATE_AND_PIN` - Backup important sessions
- `RENAME_BY_TOPIC` - Organize by content

**Key Components**:
- `agent_session_manager.py` - Session tracking
- `cursor_chat_session_workflow_manager.py` - Workflow patterns

---

### Stage 3: Task Completion & Git Commit

**Status**: `ACTIVE` or `PINNED` → `READY_FOR_VERIFICATION`

**Actions**:
1. All tasks completed
2. Code changes committed to git
3. Git commit message includes:
   - Task description
   - @ASK verification status
   - Related ticket references

**Verification**:
- No unsuccessful @asks found
- All tasks completed
- Git commit successful
- Session ready for V3 verification

**Files Updated**:
- `session_history.jsonl` - Session entry added
- `session_YYYYMMDD_HHMMSS.json` - Individual session file
- Git commit with session metadata

**Key Components**:
- `agent_session_manager.py` - Post-commit workflow
- `verify_no_unsuccessful_asks()` - @ASK verification
- `record_session_completion()` - Session recording

---

### Stage 4: V3 Verification (CRITICAL STEP)

**Status**: `READY_FOR_VERIFICATION` → `V3_VERIFIED`

**Actions**:
1. **V3 Verification System** runs triple-check:
   - **V1**: Verify Work (tasks completed correctly)
   - **V2**: Validate Integration (code integrates properly)
   - **V3**: Verify Truth (final verification)

2. V3 verification checks:
   - All @asks successful
   - No blocking issues
   - Code quality verified
   - Integration validated
   - Truth verified

**V3 Verification Components**:
- `v3_judicial_approval.py` - Core V3 framework
- `v3_verification.py` - Verification logic
- `v3_pin_decision_system.py` - Pin/unpin decisions

**Verification Process**:
```python
# V3 Verification Flow
1. V1: Verify Work
   - Check all tasks completed
   - Verify no errors
   - Confirm code quality

2. V2: Validate Integration
   - Check integration points
   - Verify dependencies
   - Validate connections

3. V3: Verify Truth
   - Final truth check
   - Judicial approval
   - Ready for archive
```

**Status Update**:
- Session status: `V3_VERIFIED`
- V3 ticket ID recorded
- Verification timestamp logged

**Key Files**:
- `lumina_core/workflow/v3_judicial_approval.py`
- `scripts/python/v3_verification.py`
- `scripts/python/v3_pin_decision_system.py`

---

### Stage 5: Pre-Archive Preparation

**Status**: `V3_VERIFIED` → `READY_FOR_ARCHIVE`

**Actions**:
1. **Archive Instructions Created**:
   - `ARCHIVE_INSTRUCTIONS.md` generated
   - Contains session metadata
   - Lists manual steps for archiving

2. **Session Status Updated**:
   - Status: `ready_for_archive`
   - @ask_verification: `passed`
   - V3 verification: `passed`

3. **Final Checks**:
   - All @asks verified successful
   - Git commit completed
   - V3 verification passed
   - Session ready for archive

**Files Created**:
- `data/agent_sessions/ARCHIVE_INSTRUCTIONS.md`
- Session entry in `session_history.jsonl`
- Individual session file: `session_YYYYMMDD_HHMMSS.json`

**Key Components**:
- `agent_session_manager.py` - `create_archive_instructions()`
- `execute_post_commit_workflow()` - Complete workflow

**Archive Instructions Content**:
```markdown
# Agent Session Archive Instructions

## Session Completion Verification
- Date: [timestamp]
- Status: ✅ All @asks verified successful
- Action Required: Archive or unpin this agent chat session

## Verification Results
✅ No unsuccessful @asks found
✅ All tasks completed
✅ Git commit completed
✅ V3 verification passed
✅ Session ready for archive/unpin

## Manual Steps (Cursor UI)
1. Check if session is pinned → Unpin if needed
2. Archive the session
3. Verify archive
```

---

### Stage 6: Archive & Unpin

**Status**: `READY_FOR_ARCHIVE` → `ARCHIVED`

**Actions**:
1. **Unpin Session** (if pinned):
   - Check pin icon in chat header
   - Click to unpin if pinned
   - Note: Archiving may auto-unpin in Cursor IDE

2. **Archive Session**:
   - Right-click on chat session in sidebar
   - Select "Archive" or "Move to Archive"
   - Or use keyboard shortcut if available

3. **Verify Archive**:
   - Check session no longer in active chats
   - Session moved to archive/history
   - Archive timestamp recorded

**Workflow Patterns**:
- `PIN_TO_ARCHIVE` - Pin → Archive (done)
- `ACTIVE_TO_ARCHIVE` - Active → Archive (cleanup)
- `DUPLICATE_BEFORE_ARCHIVE` - Duplicate → Archive (safe)

**Status Update**:
- Session status: `ARCHIVED`
- Archive timestamp: [timestamp]
- Unpinned: `true` (if was pinned)

**Key Components**:
- `cursor_chat_session_workflow_manager.py` - Archive workflow
- `_execute_archive()` - Archive execution
- `_execute_unpin()` - Unpin execution

**Note**: In Cursor IDE, archiving may automatically unpin the session. The workflow handles both operations to ensure proper state.

---

### Stage 7: Post-Archive (Optional)

**Status**: `ARCHIVED` → `ARCHIVED` (long-term)

**Actions** (Optional):
1. **Archive Management**:
   - Old archives can be reviewed
   - Very old archives can be deleted (90+ days)
   - Archive restoration if needed

2. **Archive Patterns**:
   - `ARCHIVE_TO_ACTIVE` - Restore from archive
   - `ARCHIVE_TO_DELETE` - Final cleanup (90+ days)
   - `ARCHIVE_TO_UNREAD` - Mark for review

**Workflow Patterns**:
- `OLD_ARCHIVE_TO_DELETE` - Delete old archives (90+ days)
- `ARCHIVE_TO_ACTIVE` - Restore archived session

**Key Components**:
- `cursor_chat_session_workflow_manager.py` - Archive management
- Archive cleanup workflows

---

## Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT CHAT HISTORY LIFECYCLE                  │
└─────────────────────────────────────────────────────────────────┘

1. SESSION CREATION
   ├─ New chat session created
   ├─ Status: ACTIVE
   └─ Metadata initialized

2. ACTIVE DEVELOPMENT
   ├─ Messages exchanged
   ├─ Tasks completed
   ├─ Code changes made
   └─ Activity tracked

3. TASK COMPLETION & GIT COMMIT
   ├─ All tasks completed
   ├─ Git commit successful
   ├─ @ASK verification passed
   └─ Status: READY_FOR_VERIFICATION

4. V3 VERIFICATION ⭐ CRITICAL
   ├─ V1: Verify Work
   ├─ V2: Validate Integration
   ├─ V3: Verify Truth
   └─ Status: V3_VERIFIED

5. PRE-ARCHIVE PREPARATION
   ├─ Archive instructions created
   ├─ Session status updated
   └─ Status: READY_FOR_ARCHIVE

6. ARCHIVE & UNPIN
   ├─ Unpin session (if pinned)
   ├─ Archive session
   ├─ Verify archive
   └─ Status: ARCHIVED

7. POST-ARCHIVE (Optional)
   ├─ Archive management
   └─ Long-term storage
```

---

## Key Workflow Components

### 1. Agent Session Manager
**File**: `scripts/python/agent_session_manager.py`

**Responsibilities**:
- Verify no unsuccessful @asks
- Record session completion
- Create archive instructions
- Execute post-commit workflow

**Key Methods**:
- `verify_no_unsuccessful_asks()` - @ASK verification
- `record_session_completion()` - Session recording
- `create_archive_instructions()` - Archive prep
- `execute_post_commit_workflow()` - Complete workflow

### 2. Cursor Chat Session Workflow Manager
**File**: `scripts/python/cursor_chat_session_workflow_manager.py`

**Responsibilities**:
- Manage session workflows
- Execute archive/unpin actions
- Apply workflow patterns
- Analyze session metadata

**Key Methods**:
- `analyze_session()` - Session analysis
- `recommend_workflow_pattern()` - Pattern recommendation
- `execute_workflow_pattern()` - Pattern execution
- `_execute_archive()` - Archive execution
- `_execute_unpin()` - Unpin execution

### 3. V3 Verification System
**Files**:
- `lumina_core/workflow/v3_judicial_approval.py`
- `scripts/python/v3_verification.py`
- `scripts/python/v3_pin_decision_system.py`

**Responsibilities**:
- Triple-check verification (V1, V2, V3)
- Judicial approval for operations
- Truth verification
- Pin/unpin decisions

---

## Workflow Execution

### Automated Workflow (Post-Commit)

```bash
# After git commit, run:
python scripts/python/agent_session_manager.py

# This executes:
1. verify_no_unsuccessful_asks()
2. record_session_completion("ready_for_archive")
3. create_archive_instructions()
4. Display summary with next steps
```

### Manual Archive Steps (Cursor UI)

1. **Check if pinned**:
   - Look for pin icon in chat header
   - If pinned → Click to unpin

2. **Archive session**:
   - Right-click on chat session in sidebar
   - Select "Archive" or "Move to Archive"
   - Or use keyboard shortcut

3. **Verify archive**:
   - Check session no longer in active chats
   - Session should be in archive/history

---

## Session Status Flow

```
ACTIVE
  ↓
PINNED (optional, if important)
  ↓
READY_FOR_VERIFICATION (after git commit)
  ↓
V3_VERIFIED (after V3 verification)
  ↓
READY_FOR_ARCHIVE (pre-archive prep)
  ↓
ARCHIVED (final state)
```

---

## Workflow Patterns

### Pattern: ACTIVE_TO_ARCHIVE
- **When**: Active session completed, 7+ days old, low activity
- **Actions**: `[ARCHIVE]`
- **Use Case**: Completed project sessions, old inactive sessions

### Pattern: PIN_TO_ARCHIVE
- **When**: Pinned session completed
- **Actions**: `[UNPIN, ARCHIVE]`
- **Use Case**: Important work done, ready to archive

### Pattern: DUPLICATE_BEFORE_ARCHIVE
- **When**: Important session, substantial content
- **Actions**: `[DUPLICATE, ARCHIVE]`
- **Use Case**: Safe archiving with backup

### Pattern: RENAME_AND_ARCHIVE
- **When**: Generic session name, completed work
- **Actions**: `[RENAME, ARCHIVE]`
- **Use Case**: Better organization before archiving

---

## Data Files

### Session History
**File**: `data/agent_sessions/session_history.jsonl`

**Format**: JSONL (one JSON object per line)

**Example Entry**:
```json
{
  "session_id": "unknown",
  "timestamp": "2026-01-14T02:53:17.969792",
  "git_info": {
    "commit": "e22713d774c7352cfc12de5fa0b5ef52b0a998e1",
    "message": "feat: Add NAS deployment automation + complete workflow map"
  },
  "project_root": "C:\\Users\\mlesn\\Dropbox\\my_projects\\.lumina",
  "status": "ready_for_archive",
  "@ask_verification": "passed"
}
```

### Individual Session Files
**Location**: `data/agent_sessions/session_YYYYMMDD_HHMMSS.json`

**Content**: Complete session metadata including:
- Session ID
- Timestamp
- Git info
- Status
- @ASK verification
- V3 verification status

### Archive Instructions
**File**: `data/agent_sessions/ARCHIVE_INSTRUCTIONS.md`

**Content**: Manual archive steps and session metadata

---

## Integration Points

### Git Integration
- Session completion triggers after git commit
- Git commit message includes session metadata
- Commit hash recorded in session data

### V3 Verification Integration
- V3 verification required before archive
- V3 ticket ID recorded in session metadata
- Judicial approval for archive operations

### Cursor IDE Integration
- Session management via Cursor IDE UI
- Archive/unpin via @FF menu options
- Session metadata tracked in Cursor IDE

### MANUS Integration
- MANUS can automate Cursor IDE operations
- Session workflow automation via MANUS
- Control operations for archive/unpin

---

## Success Criteria

### Session Completion
- ✅ All @asks verified successful
- ✅ All tasks completed
- ✅ Git commit successful
- ✅ V3 verification passed
- ✅ Session ready for archive

### Archive Completion
- ✅ Session unpinned (if was pinned)
- ✅ Session archived in Cursor IDE
- ✅ Archive verified
- ✅ Session metadata recorded
- ✅ Audit trail maintained

---

## Error Handling

### Unsuccessful @asks
- **Action**: Do not proceed to archive
- **Resolution**: Fix unsuccessful @asks first
- **Status**: Session remains ACTIVE/PINNED

### V3 Verification Failure
- **Action**: Do not proceed to archive
- **Resolution**: Fix issues, re-run V3 verification
- **Status**: Session remains READY_FOR_VERIFICATION

### Archive Failure
- **Action**: Retry archive operation
- **Resolution**: Manual archive via Cursor UI
- **Status**: Session remains READY_FOR_ARCHIVE

---

## Best Practices

1. **Always run V3 verification** before archiving
2. **Verify all @asks successful** before completion
3. **Create archive instructions** for manual steps
4. **Maintain audit trail** in session_history.jsonl
5. **Unpin before archiving** (if pinned)
6. **Verify archive** after completion
7. **Use workflow patterns** for consistent management
8. **Track session metadata** throughout lifecycle

---

## Related Documentation

- `data/agent_sessions/ARCHIVE_INSTRUCTIONS.md` - Archive instructions template
- `scripts/python/agent_session_manager.py` - Session manager implementation
- `scripts/python/cursor_chat_session_workflow_manager.py` - Workflow manager
- `lumina_core/workflow/v3_judicial_approval.py` - V3 verification framework
- `docs/system/V3_PIN_DECISION_INTEGRATION.md` - V3 pin decision system

---

**Tags**: #SESSION_MANAGEMENT #AGENT_LIFECYCLE #V3_VERIFICATION #ARCHIVE #WORKFLOW #LIFECYCLE @JARVIS @MANUS @LUMINA @V3

**Last Updated**: 2026-01-14
**Version**: 1.0
