# AI Request Template
## Structured Format for Effective AI Communication

**Version:** 1.0  
**Based on:** ML/AI Scientist Framework  
**Status:** ✅ **READY FOR USE**

---

## 📋 TEMPLATE

```markdown
# [Request Title]

## ROLE
[Define the AI's role and expertise]
Examples:
- Software Engineer
- Data Analyst
- System Architect
- Project Manager
- ML/AI Scientist

## CONTEXT (Priority Order)
### PRIMARY
[Essential information - load first]
- File paths
- Key data structures
- Critical constraints

### SECONDARY  
[Supporting information - load if needed]
- Related files
- Background information
- Additional context

### REFERENCE
[Available but don't load unless explicitly needed]
- Full conversation history
- Entire codebase
- Large documentation files

## TASK
**Action:** [Clear action verb]
**Goal:** [What success looks like]
**Constraints:** 
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## DECOMPOSITION
**Step 1:** [Specific action]
  → Validate: [How to check if successful]

**Step 2:** [Next action]
  → Validate: [How to check if successful]

**Step 3:** [Next action]
  → Validate: [How to check if successful]

## OUTPUT_FORMAT
[How to present results]
Examples:
- Markdown table
- JSON structure
- Code snippet
- Documentation

## SUCCESS_CRITERIA
- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)
- [ ] Criterion 3 (measurable)

## VALIDATION
[How to verify success]
- Check method 1
- Check method 2
```

---

## 📝 EXAMPLE: Find Outstanding VA Todos

```markdown
# Find Outstanding Virtual Assistant Todos

## ROLE
Todo Analyst / Software Engineer

## CONTEXT (Priority Order)
### PRIMARY
- Master todos: `data/todo/master_todos.json`
- Padawan todos: `data/ask_database/master_padawan_todos.json`
- VA keywords: ["virtual assistant", "VA", "JARVIS", "IMVA", "ACE", "AVA"]

### SECONDARY
- VA registry: `scripts/python/character_avatar_registry.py`
- Current VAs: JARVIS_VA, IMVA, ACE, AVA

### REFERENCE
- Full conversation history (only if needed)
- Entire codebase (only if needed)

## TASK
**Action:** Identify outstanding Virtual Assistant todos
**Goal:** List all pending/in-progress VA-related todos from master and padawan lists
**Constraints:** 
- Only check specified files
- Filter by VA keywords
- Status must be "pending" or "in_progress"
- Exclude completed todos

## DECOMPOSITION
**Step 1:** Load master_todos.json
  → Validate: File exists and is valid JSON

**Step 2:** Filter todos for VA keywords
  → Validate: Return count of matches

**Step 3:** Filter by status (pending/in_progress)
  → Validate: Return filtered list

**Step 4:** Load padawan todos (if exists)
  → Validate: File exists and is valid JSON

**Step 5:** Filter padawan todos for VA keywords
  → Validate: Return count of matches

**Step 6:** Format results
  → Validate: Output is readable markdown

## OUTPUT_FORMAT
Markdown table with columns:
- Todo ID
- Title
- Status
- Priority
- Category
- Description (truncated to 100 chars)

## SUCCESS_CRITERIA
- [ ] All VA todos identified from master list
- [ ] All VA todos identified from padawan list (if exists)
- [ ] Only pending/in_progress todos included
- [ ] Results formatted clearly
- [ ] No false positives (non-VA todos)

## VALIDATION
- Check: All todos contain VA keywords
- Check: All todos have status="pending" or "in_progress"
- Check: Output is readable markdown table
- Check: No completed todos in results
```

---

## 🎯 QUICK REFERENCE

### For Simple Requests:
```
ROLE: [Role]
TASK: [Action] → [Goal]
CONTEXT: [Primary only]
OUTPUT: [Format]
```

### For Complex Requests:
Use full template above.

---

## ✅ CHECKLIST

Before submitting a request:
- [ ] Role is defined
- [ ] Context is prioritized
- [ ] Task is clear and actionable
- [ ] Success criteria are measurable
- [ ] Output format is specified
- [ ] Validation method is clear

---

**Tags:** #TEMPLATE #AI_GUIDANCE #STRUCTURED_COMMUNICATION @JARVIS @LUMINA
