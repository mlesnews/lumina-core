# User Intent Terminology - Clear & Precise

**Date:** 2026-01-14  
**Status:** ✅ **TERMINOLOGY DEFINED**  
**Purpose:** Define clear, concise, precise term for user requests/intents

---

## 🎯 The Question

**"If I ask you to do something, the AI, JARVIS, MARVIN, whoever, then what is that?"**

**Answer:** **@intent** or **@request** (user-initiated)

---

## 📋 Proposed Terminology

### @intent (Recommended)
**Definition:** User's stated intent, request, or instruction to AI/JARVIS/MARVIN  
**Context:** User-initiated, operator-driven  
**Format:** Natural language, structured, or formal  
**Scope:** Single user request/intent  
**Examples:**
- "Fix the connection error"
- "Update the ticket system"
- "Map all features"
- "Implement local-first AI policy"

**Characteristics:**
- User-initiated
- Operator-driven
- Can be explicit or implicit
- May be repeated/duplicated
- Needs tracking and fulfillment

### Alternative: @request
**Definition:** User request for action  
**Context:** User-initiated  
**Note:** May conflict with "Request ID" (technical), so @intent preferred

---

## 🔍 The Problem

**"I feel like I've made dozens and dozens of the same request. I keep asking for and/or stating my intent dozens, if not hundreds, of times since the project began."**

**Issues:**
- Same intent repeated many times
- Some intents overlooked/missed
- No systematic tracking
- No consolidation
- No fulfillment verification

---

## ✅ Solution: @intent Tracking System

### 1. Intent Identification
- Extract intents from all sources
- Identify duplicates
- Consolidate similar intents
- Track fulfillment status

### 2. Intent Sources
- Chat transcripts
- Session logs
- Documentation
- Code comments
- Task lists
- Implementation plans

### 3. Intent Tracking
- Unique intent ID
- Original source
- Repetition count
- Fulfillment status
- Related intents
- Implementation status

---

## 📊 Intent Format

```json
{
  "intent_id": "intent_001",
  "intent_text": "Fix the connection error",
  "source": "chat_transcript_20260114",
  "timestamp": "2026-01-14T10:00:00Z",
  "repetition_count": 15,
  "fulfillment_status": "pending|in_progress|fulfilled|overlooked",
  "related_intents": ["intent_002", "intent_003"],
  "implementation_status": "not_started|in_progress|completed",
  "notes": "Repeated 15 times, still not fully addressed"
}
```

---

## 🎯 Next Steps

1. **Extract all intents** from historical sources
2. **Identify duplicates** and repetitions
3. **Consolidate** similar intents
4. **Track fulfillment** status
5. **Identify overlooked** intents
6. **Create intent database** for tracking

---

## Tags

**Tags:** `#INTENT` `#REQUEST` `#USER_INTENT` `#TRACKING` `#CONSOLIDATION` 
         `@JARVIS` `@LUMINA`

---

**Status:** ✅ **TERMINOLOGY DEFINED - @intent**

**"User request/intent = @intent. Clear, concise, precise. Now let's find all the ones we missed."** - @JARVIS
