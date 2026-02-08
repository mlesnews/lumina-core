# Session Ask Resolution Workflow

**Status**: ✅ OPERATIONAL  
**Purpose**: Verify, validate, and archive sessions when all asks are resolved and approved

---

## 🎯 Overview

Every session should ask: **"Are there any unresolved asks?"**

If verified, validated, and verified again, and upper management (JARVIS/MARVIN) approves, then:
1. Pin the chat
2. Archive it
3. Rename with final status

---

## 🔄 Workflow

```
Session End → Extract Asks → Verify Completion → JARVIS Review → MARVIN Review → Pin/Archive/Rename
```

### Step-by-Step

1. **Extract Asks**
   - Scan session for @ask patterns
   - Extract user requests
   - Match with todos

2. **Verify Completion**
   - Check if all asks are resolved
   - Verify with master todo list
   - Check completion evidence

3. **JARVIS Review** (Systematic)
   - Task well-defined?
   - Dependencies met?
   - Status accurate?
   - Priority appropriate?

4. **MARVIN Review** (Philosophical)
   - Aligns with Lumina mission?
   - Serves the purpose?
   - Meaningful?

5. **Archive if Approved**
   - Pin chat
   - Rename with final status
   - Move to archive directory

---

## ✅ This Session - All Resolved!

### Session Asks (3 total)

1. ✅ **Create trailer videos for pilot episode**
   - **Status**: Complete
   - **Evidence**: 8 video files created in `output/videos/`
   - **JARVIS**: ✅ Verified
   - **MARVIN**: ✅ Verified

2. ✅ **SYPHON video/audio breakdown with @ask-requested**
   - **Status**: Complete
   - **Evidence**: System created, @ask extraction working
   - **JARVIS**: ✅ Verified
   - **MARVIN**: ✅ Verified

3. ✅ **Git/GitLens Integration marked as complete**
   - **Status**: Complete
   - **Evidence**: Updated ROADMAP.md, completion doc created
   - **JARVIS**: ✅ Verified
   - **MARVIN**: ✅ Verified

### Additional Work Completed

- ✅ Master To-Do List System
- ✅ Dual To-Do System (Master + Verified)
- ✅ NAS Holocron Backup (rolling logs)
- ✅ Cursor Agent Chat Renamer (dynamic scaling)
- ✅ Session Ask Resolver
- ✅ Pin/Archive/Rename Manager

---

## 📋 Usage

### Run Session Ask Resolution

```bash
python scripts/python/session_ask_resolver.py
```

### VSCode Task

- `✅ Session: Check & Resolve All Asks` - Check and resolve session asks

---

## 🎯 Decision Criteria

### Ready to Archive When:

- ✅ All asks extracted
- ✅ All asks resolved (evidence provided)
- ✅ JARVIS review: ✅ Verified
- ✅ MARVIN review: ✅ Verified
- ✅ Fully approved by upper management

### Not Ready When:

- ⚠️ Unresolved asks exist
- ⚠️ Verification failed
- ⚠️ Validation concerns
- ⚠️ Management approval pending

---

## 🔗 Integration

- **Dual To-Do System** - Verifies against master/verified lists
- **Verification Workflow** - JARVIS/MARVIN triple-check
- **Cursor Chat Manager** - Pin/Archive/Rename operations
- **NAS Holocron** - Backup and logging

---

**Status**: All session asks resolved and approved! ✅  
**Ready for**: Pin, Archive, Rename

