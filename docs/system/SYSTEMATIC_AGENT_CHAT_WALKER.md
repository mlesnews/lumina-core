# Systematic Agent Chat Walker

**Date:** January 9, 2025  
**Status:** ✅ Operational

---

## Overview

Systematic and programmatic walker that processes all agent-chat sessions to:
- Process **@ask** directives (@ask and @ASK)
- Manage **@stack-heap** memory
- Fix **#workflows** with **@puppetmaster-workflow**

---

## Components

### 1. @ask Processor

**Purpose:** Process @ask directives in agent chat sessions

**Handles:**
- `@ask` (lowercase) - Request approval/interaction directive
- `@ASK` (uppercase) - AI token request tracking system

**Functions:**
- Find @ask directives in session content
- Process and track @ask requests
- Resolve pending @ask requests

### 2. @stack-heap Manager

**Purpose:** Memory management for agent chat sessions

**Components:**
- **Stack:** Current active context (LIFO)
- **Heap:** Long-term memory storage (key-value)

**Operations:**
- `push_to_stack()` - Push context to stack
- `pop_from_stack()` - Pop context from stack
- `store_to_heap()` - Store to long-term memory
- `get_from_heap()` - Retrieve from long-term memory
- `cleanup_heap()` - Cleanup old entries

### 3. @puppetmaster-workflow

**Purpose:** Workflow orchestration and fixing

**Functions:**
- Identify workflow issues in sessions
- Fix incomplete workflows
- Optimize workflow execution
- Track workflow fixes

---

## Usage

### Walk All Sessions

```bash
# Walk all sessions and process @ask, @stack-heap, and workflows
python scripts/python/systematic_agent_chat_walker.py --walk --fix-workflows
```

### Cleanup Heap

```bash
# Cleanup heap entries older than 30 days
python scripts/python/systematic_agent_chat_walker.py --cleanup-heap 30
```

---

## Processing Flow

1. **Discovery**
   - Discover all agent chat sessions (transcripts + chat sessions)
   - From CursorAgentHistoryProcessor
   - From SYPHON

2. **For Each Session:**
   - Push context to stack
   - Find and process @ask directives
   - Store session metadata to heap
   - Identify workflow issues
   - Fix workflows (if --fix-workflows)
   - Pop context from stack

3. **Results**
   - Summary statistics
   - Detailed session results
   - Saved to `data/systematic_walker/`

---

## Output

### Statistics
- Sessions processed
- @ask directives found
- @ask directives processed
- Workflow issues found
- Workflows fixed
- Stack operations
- Heap operations

### Results File
- JSON file with complete results
- Location: `data/systematic_walker/walk_results_*.json`

---

## Integration

### With @JARVIS
- JARVIS can trigger systematic walks
- Stack-heap provides context for JARVIS decisions
- Workflow fixes improve JARVIS operations

### With @SYPHON
- SYPHON discovers sessions
- SYPHON data feeds into walker
- Pattern detection enhances processing

### With @WOPR
- WOPR uses stack-heap data
- WOPR analyzes workflow patterns
- WOPR informs workflow fixes

---

## Example Output

```
🚶 SYSTEMATIC AGENT CHAT WALKER
   Processing all sessions programmatically
================================================================================

🔍 Discovering agent chat sessions...
   ✅ Found 21 transcripts
   ✅ Found 52 chat sessions
   📊 Total sessions to process: 73

📋 PROCESSING SESSIONS
   📋 @ask directive found: ...
   🎫 @ASK token request found: ...
   🔧 Fixed workflow issue: ...

✅ SYSTEMATIC WALK COMPLETE
   Sessions processed: 73
   @ask directives found: 150+
   @ask directives processed: 150+
   Workflow issues found: 25
   Workflows fixed: 25
   Stack operations: 146
   Heap operations: 73
```

---

## Best Practices

1. **Regular Walks**
   - Run weekly to process new sessions
   - Cleanup heap monthly
   - Fix workflows as needed

2. **Stack Management**
   - Keep stack size reasonable
   - Pop after processing each session
   - Use stack for context tracking

3. **Heap Management**
   - Store important session metadata
   - Cleanup old entries regularly
   - Use meaningful keys

4. **Workflow Fixes**
   - Review fixes before applying
   - Test fixed workflows
   - Document workflow changes

---

## Related Systems

- **@JARVIS** - Automation coordination
- **@SYPHON** - Intelligence extraction
- **@WOPR** - Pattern analysis
- **@puppetmaster-workflow** - Workflow orchestration
- **@ask** - Approval system
- **@stack-heap** - Memory management

---

**Last Updated:** January 9, 2025  
**Status:** ✅ Operational
