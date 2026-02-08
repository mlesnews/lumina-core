# AI Guidance Process: Roast & Repair
## ML/AI Scientist Perspective on Effective AI Communication

**Date:** 2026-01-09  
**Status:** 🔥 **ROAST COMPLETE** → 🔧 **REPAIR IN PROGRESS**  
**Role:** Machine Learning AI Scientist

---

## 🔥 THE ROAST: What's Wrong with Our Current Approach

### 1. **Context Overload Without Structure**
**Problem:** We're dumping massive context dumps (2849-line JSON files, entire conversation histories) without clear structure or prioritization.

**Why This Fails:**
- LLMs have attention limits - they can't effectively process everything
- No clear signal-to-noise ratio
- Important information gets lost in the noise
- The AI has to guess what's relevant

**Evidence:**
- User: "We still have outstanding for virtual assistants"
- AI: Spent time reading 2849-line JSON files, searching multiple directories
- Result: Found the todo, but the process was inefficient

### 2. **Ambiguous Intent Signals**
**Problem:** Requests are vague or implicit rather than explicit.

**Examples:**
- "We still have outstanding for virtual assistants" → What does "outstanding" mean? Pending todos? Missing features? Bugs?
- "Please roast and repair this entire process" → What specific process? The todo checking? The communication? The system?

**Why This Fails:**
- LLMs are literal - they interpret based on patterns
- Ambiguity leads to wasted effort on wrong interpretations
- No clear success criteria

### 3. **No Clear Task Decomposition**
**Problem:** We're asking for complex multi-step tasks without breaking them down.

**Example:**
- "Check master and paddy todo lists for outstanding Virtual Assistant items"
- Should be: "1) Load master_todos.json, 2) Filter for VA-related items, 3) Check status='pending', 4) Report findings"

**Why This Fails:**
- LLMs work better with explicit step-by-step instructions
- No clear checkpoint for validation
- Hard to debug when things go wrong

### 4. **Missing Feedback Loops**
**Problem:** We don't provide explicit feedback on what worked/didn't work.

**Why This Fails:**
- No learning from mistakes
- Same patterns repeat
- Can't optimize the process

### 5. **Inconsistent Formatting and Structure**
**Problem:** Information comes in different formats (JSON, markdown, code, natural language) without standardization.

**Why This Fails:**
- LLMs are sensitive to format
- Inconsistent formats = inconsistent parsing
- Hard to extract structured information

### 6. **No Explicit Role Definition**
**Problem:** We're not clearly defining what role the AI should take.

**Why This Fails:**
- Different roles = different outputs
- "ML/AI Scientist" vs "Software Engineer" vs "Project Manager" = different approaches
- No clear persona = generic responses

### 7. **Over-Reliance on Semantic Search**
**Problem:** We use semantic search for everything, even when exact matching would work.

**Why This Fails:**
- Semantic search is probabilistic - can miss exact matches
- Slower than grep/exact search
- Can return irrelevant results

### 8. **No Clear Success Metrics**
**Problem:** We don't define what "done" looks like.

**Why This Fails:**
- AI doesn't know when to stop
- Can over-engineer or under-deliver
- No validation criteria

---

## 🔧 THE REPAIR: ML/AI Scientist's Framework for Effective AI Guidance

### Principle 1: **Structured Context with Clear Hierarchy**

**DO:**
```
CONTEXT (Priority Order):
1. PRIMARY: [What the AI needs to know NOW]
2. SECONDARY: [Supporting information]
3. REFERENCE: [Available but not loaded unless needed]
```

**DON'T:**
- Dump entire files without filtering
- Load everything "just in case"
- Mix priorities

**Example:**
```
PRIMARY CONTEXT:
- User wants to check VA todos
- Master todos file: data/todo/master_todos.json
- Padawan todos file: data/ask_database/master_padawan_todos.json

SECONDARY CONTEXT:
- VA registry exists at scripts/python/character_avatar_registry.py
- Current VAs: JARVIS_VA, IMVA, ACE, AVA

REFERENCE (Don't Load):
- Full conversation history (only if needed)
- Entire codebase (only if needed)
```

### Principle 2: **Explicit Intent with Structured Format**

**DO:**
```
TASK: [Clear action verb]
GOAL: [What success looks like]
CONSTRAINTS: [Limitations/requirements]
OUTPUT_FORMAT: [How to present results]
```

**DON'T:**
- Use vague language
- Assume implicit understanding
- Skip output format

**Example:**
```
TASK: Identify outstanding Virtual Assistant todos
GOAL: List all pending/in-progress VA-related todos from master and padawan lists
CONSTRAINTS: 
  - Only check master_todos.json and master_padawan_todos.json
  - Filter by keywords: "virtual assistant", "VA", "JARVIS", "IMVA", "ACE", "AVA"
  - Status must be "pending" or "in_progress"
OUTPUT_FORMAT: Markdown list with todo ID, title, status, priority
```

### Principle 3: **Task Decomposition with Checkpoints**

**DO:**
```
STEP 1: [Specific action]
  → VALIDATE: [How to check if step succeeded]
STEP 2: [Next action]
  → VALIDATE: [How to check if step succeeded]
...
```

**DON'T:**
- Give multi-step tasks as one instruction
- Skip validation steps
- Assume steps are obvious

**Example:**
```
STEP 1: Load master_todos.json
  → VALIDATE: File exists and is valid JSON
STEP 2: Filter todos for VA keywords
  → VALIDATE: Return count of matches
STEP 3: Filter by status (pending/in_progress)
  → VALIDATE: Return filtered list
STEP 4: Format results
  → VALIDATE: Output is readable markdown
```

### Principle 4: **Role-Based Persona Definition**

**DO:**
```
ROLE: [Specific role]
EXPERTISE: [Relevant knowledge areas]
APPROACH: [How this role thinks/works]
OUTPUT_STYLE: [How this role communicates]
```

**DON'T:**
- Use generic "assistant" role
- Mix multiple roles
- Skip role definition

**Example:**
```
ROLE: Machine Learning AI Scientist
EXPERTISE: 
  - LLM behavior and optimization
  - Human-AI interaction design
  - Information architecture
  - Cognitive load management
APPROACH:
  - Data-driven analysis
  - Systematic problem-solving
  - Evidence-based recommendations
  - Clear hypothesis testing
OUTPUT_STYLE:
  - Structured with clear sections
  - Evidence-backed claims
  - Actionable recommendations
  - Metrics and measurements
```

### Principle 5: **Explicit Feedback Loops**

**DO:**
```
FEEDBACK_FORMAT:
- What worked: [Specific examples]
- What didn't work: [Specific examples]
- Why: [Root cause analysis]
- Next iteration: [How to improve]
```

**DON'T:**
- Give vague feedback
- Skip the "why"
- Don't suggest improvements

### Principle 6: **Tool Selection Strategy**

**DO:**
- Use exact matching (grep) for known strings
- Use semantic search for concepts/patterns
- Use file reading for structured data
- Use codebase_search for "how does X work?"

**DON'T:**
- Use semantic search for exact strings
- Use grep for conceptual queries
- Read entire files when you need one value

### Principle 7: **Success Metrics Definition**

**DO:**
```
SUCCESS_CRITERIA:
- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)
- [ ] Criterion 3 (measurable)

VALIDATION:
- How to verify each criterion
- What "done" looks like
```

---

## 🎯 REPAIRED PROCESS: New AI Guidance Framework

### Template: Effective AI Request

```markdown
# AI Request Template

## ROLE
[Define the AI's role and expertise]

## CONTEXT (Priority Order)
### PRIMARY
[Essential information - load first]

### SECONDARY  
[Supporting information - load if needed]

### REFERENCE
[Available but don't load unless explicitly needed]

## TASK
**Action:** [Clear action verb]
**Goal:** [What success looks like]
**Constraints:** [Limitations/requirements]

## DECOMPOSITION
**Step 1:** [Specific action]
  → Validate: [How to check]

**Step 2:** [Next action]
  → Validate: [How to check]

## OUTPUT_FORMAT
[How to present results]

## SUCCESS_CRITERIA
- [ ] Criterion 1
- [ ] Criterion 2

## FEEDBACK_LOOP
[How to provide feedback for improvement]
```

---

## 📊 COMPARISON: Before vs After

### BEFORE (Current Process):
```
User: "We still have outstanding for virtual assistants. So make sure you're going by the master to do list and the paddy one to do list."

AI Actions:
1. Searches for todo files (multiple searches)
2. Reads 2849-line JSON file
3. Searches for "paddy" files
4. Reads master todo report
5. Creates checker script
6. Runs script
7. Creates documentation

Issues:
- Unclear what "outstanding" means
- Searched multiple places unnecessarily
- Created tool instead of direct answer
- No clear success criteria
```

### AFTER (Repaired Process):
```
User Request (Structured):
ROLE: Software Engineer / Todo Analyst
CONTEXT:
  PRIMARY: Master todos at data/todo/master_todos.json
  PRIMARY: Padawan todos at data/ask_database/master_padawan_todos.json
  SECONDARY: VA registry exists
TASK:
  Action: Identify outstanding VA todos
  Goal: List pending/in-progress VA-related todos
  Constraints: Only check specified files, filter by VA keywords
OUTPUT_FORMAT: Markdown list with ID, title, status, priority
SUCCESS_CRITERIA:
  - [ ] All VA todos identified
  - [ ] Status is pending or in_progress
  - [ ] Results are formatted clearly

AI Actions:
1. Load master_todos.json (targeted)
2. Filter for VA keywords (exact matching)
3. Filter by status (exact matching)
4. Format results
5. Report findings

Result: Direct answer in < 5 tool calls
```

---

## 🧪 TESTING THE REPAIRED PROCESS

### Test Case 1: Find Outstanding VA Todos

**Request (Repaired):**
```
ROLE: Todo Analyst
CONTEXT:
  PRIMARY: data/todo/master_todos.json
  PRIMARY: data/ask_database/master_padawan_todos.json
TASK:
  Action: Find VA todos with status="pending" or "in_progress"
  Goal: List outstanding VA-related todos
  Keywords: ["virtual assistant", "VA", "JARVIS", "IMVA", "ACE", "AVA"]
OUTPUT_FORMAT: Markdown table
SUCCESS_CRITERIA:
  - [ ] All VA todos found
  - [ ] Only pending/in_progress included
  - [ ] Clear formatting
```

**Expected Behavior:**
1. Load master_todos.json (1 file read)
2. Filter by keywords (in-memory)
3. Filter by status (in-memory)
4. Format as markdown table
5. Report (direct answer)

**Tool Calls:** ~3-4 (vs 10+ before)

---

## 🎓 KEY LEARNINGS FOR AI GUIDANCE

### 1. **Be Explicit, Not Implicit**
- Don't: "Check for outstanding items"
- Do: "Find todos where status='pending' AND category contains 'VA'"

### 2. **Structure Context by Priority**
- Don't: Load everything
- Do: Load only what's needed, in priority order

### 3. **Define Success Before Starting**
- Don't: "Find the todos"
- Do: "List todos matching [criteria] in [format]"

### 4. **Use Appropriate Tools**
- Don't: Semantic search for exact strings
- Do: grep/exact matching for known strings

### 5. **Provide Feedback Loops**
- Don't: Silent failures
- Do: Explicit feedback on what worked/didn't

### 6. **Decompose Complex Tasks**
- Don't: "Do this complex thing"
- Do: "Step 1: X, Step 2: Y, Step 3: Z"

### 7. **Define Role and Expertise**
- Don't: Generic assistant
- Do: Specific role with clear expertise

---

## 🔄 ITERATIVE IMPROVEMENT PROCESS

### Cycle:
1. **Request** (Structured format)
2. **Execute** (AI follows structure)
3. **Evaluate** (Check success criteria)
4. **Feedback** (What worked/didn't)
5. **Refine** (Update process)
6. **Repeat**

### Feedback Template:
```
EXECUTION_RESULT:
- What worked: [Specific examples]
- What didn't: [Specific examples]
- Why: [Root cause]
- Next iteration: [Improvements]
```

---

## 📝 IMPLEMENTATION: Updated Guidance System

### For Users:
1. Use structured request template
2. Define role explicitly
3. Prioritize context
4. Decompose tasks
5. Define success criteria

### For AI:
1. Follow structured format
2. Use appropriate tools
3. Validate at each step
4. Report clearly
5. Request feedback

---

## 🎯 IMMEDIATE ACTION ITEMS

1. **Create Request Template** ✅ (This document)
2. **Update User Guidelines** (How to make effective requests)
3. **Create AI Response Template** (How AI should structure responses)
4. **Implement Feedback Loop** (How to improve iteratively)
5. **Test with Real Requests** (Validate the framework)

---

## 📊 METRICS FOR SUCCESS

**Efficiency:**
- Tool calls per request (target: < 5 for simple tasks)
- Time to answer (target: < 30 seconds)
- Context size (target: < 10KB primary context)

**Accuracy:**
- Correct interpretation rate (target: > 90%)
- Relevant results (target: > 95%)
- User satisfaction (target: > 80%)

**Clarity:**
- Structured output (target: 100%)
- Clear success criteria (target: 100%)
- Actionable feedback (target: 100%)

---

## 🔚 CONCLUSION

**The Problem:** We're treating AI like a human, using natural language without structure.

**The Solution:** Treat AI like a system - give it structured inputs, clear instructions, and explicit validation.

**The Framework:** Use the template above for all AI requests.

**Next Steps:** Test the framework with real requests and iterate based on feedback.

---

**Tags:** #AI_GUIDANCE #ML_SCIENCE #PROCESS_IMPROVEMENT #HUMAN_AI_INTERACTION #STRUCTURED_COMMUNICATION @JARVIS @LUMINA

**Created:** 2026-01-09  
**Status:** 🔧 **FRAMEWORK COMPLETE - READY FOR TESTING**
