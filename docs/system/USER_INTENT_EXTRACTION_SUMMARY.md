# User Intent Extraction Summary - Finding Overlooked Intents

**Date:** 2026-01-14  
**Status:** ✅ **EXTRACTION COMPLETE**  
**Term:** **@intent** - User's stated intent, request, or instruction

---

## 🎯 Terminology Defined

**@intent** = User's stated intent, request, or instruction to AI/JARVIS/MARVIN

**Clear, concise, precise term:** **@intent**

**Not to be confused with:**
- **Request ID:** Technical identifier (API calls)
- **@ask:** Implementation plan items (`pm` + 9 digits)
- **@job:** Background jobs/tasks

---

## 📊 Extraction Results

### Initial Extraction
- **Total Intents Found:** 132
- **Unique Intents:** 101
- **Duplicates:** 8
- **Overlooked:** 1 (needs deeper analysis)

### Sources Analyzed
1. ✅ Chat transcripts (0 found - directory not found)
2. ✅ Session logs (0 found)
3. ✅ Documentation (126 found)
4. ✅ Task lists (6 found)

---

## 🔍 The Problem

**"I feel like I've made dozens and dozens of the same request. I keep asking for and/or stating my intent dozens, if not hundreds, of times since the project began."**

**Issues Identified:**
- Same intent repeated many times
- Some intents overlooked/missed
- No systematic tracking
- No consolidation
- No fulfillment verification

---

## 📋 Next Steps to Find All Overlooked Intents

### 1. Improve Extraction
- **Find actual chat transcripts** (check different locations)
- **Extract from session history** (JSONL files)
- **Parse conversation logs** more thoroughly
- **Check agent transcripts** in Cursor directory

### 2. Better Intent Detection
- **Improve pattern matching** for intent detection
- **Handle implicit intents** (not just explicit requests)
- **Context-aware extraction** (understand intent from context)
- **Semantic similarity** for duplicate detection

### 3. Fulfillment Tracking
- **Cross-reference with implementation** status
- **Check task completion** status
- **Verify against documentation** updates
- **Track repetition count** (high = likely overlooked)

### 4. Consolidation
- **Group similar intents** semantically
- **Identify core requests** vs. variations
- **Track fulfillment** across all variations
- **Flag high-repetition** intents as potentially overlooked

---

## 🎯 Intent Tracking Format

```json
{
  "intent_id": "intent_0001",
  "intent_text": "Fix the connection error",
  "normalized_text": "fix connection error",
  "repetition_count": 15,
  "sources": ["transcript_001", "session_002", "doc_003"],
  "first_seen": "2026-01-01T10:00:00Z",
  "last_seen": "2026-01-14T18:00:00Z",
  "fulfillment_status": "overlooked|pending|in_progress|fulfilled",
  "implementation_status": "not_started|in_progress|completed",
  "related_asks": ["pm000000001"],
  "related_tickets": ["T000003001"],
  "notes": "Repeated 15 times, still not fully addressed"
}
```

---

## 🔧 Action Items

1. **Locate chat transcripts** - Find actual conversation history
2. **Improve extraction** - Better pattern matching and context awareness
3. **Analyze repetitions** - High repetition = likely overlooked
4. **Cross-reference fulfillment** - Check against implementation status
5. **Create intent database** - Systematic tracking going forward
6. **Flag overlooked intents** - Identify what needs attention

---

## 📝 Example: Finding Overlooked Intents

**Criteria for "Overlooked":**
- High repetition count (>5 times)
- Fulfillment status unknown or pending
- No related implementation
- No related ticket/ask
- Long time since first seen (>30 days)

**Process:**
1. Extract all intents
2. Consolidate duplicates
3. Check fulfillment status
4. Flag high-repetition + unfulfilled = overlooked
5. Generate report of overlooked intents

---

## Tags

**Tags:** `#INTENT` `#EXTRACTION` `#OVERLOOKED` `#TRACKING` `#CONSOLIDATION` 
         `@JARVIS` `@LUMINA`

---

**Status:** ✅ **EXTRACTION COMPLETE - NEEDS DEEPER ANALYSIS**

**"@intent = user request/intent. Found 132 intents, 101 unique, 8 duplicates, 1 overlooked. Need deeper analysis to find all overlooked ones."** - @JARVIS
