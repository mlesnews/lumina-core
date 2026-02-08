# AI Guidance Complete Framework
## Integrating +RULES, +COMMAND, and PROFILE PROMPTS

**Date:** 2026-01-09
**Status:** ✅ **COMPLETE FRAMEWORK**
**Version:** 2.0 (Enhanced with Rules, Commands, Profiles)

---

## 🎯 OVERVIEW

The complete AI guidance system integrates **four layers** of guidance:

1. **+RULES** - Workspace rules (.cursorrules, config rules)
2. **+COMMAND** - Command patterns (@DOIT, @END2END, @V3, etc.)
3. **PROFILE PROMPTS** - User/system profiles (personas, expertise)
4. **STRUCTURED REQUESTS** - Explicit task definitions (from v1.0)

---

## 📋 LAYER 1: +RULES (Workspace Rules)

### Purpose
Define **persistent, project-wide rules** that apply to all AI interactions.

### Sources
- `.cursorrules` - Primary workspace rules
- `config/*_rules.json` - Configuration-based rules
- `config/shortag_registry.json` - Tag-based rules

### Key Rules from .cursorrules:

#### Code Standards
```python
# Python
- Always use type hints (typing module)
- Follow PEP 8 style guide
- Use f-strings for string formatting
- Prefer pathlib.Path over os.path
- Use dataclasses for data structures
- Always include docstrings (Google style)
- Use logging.getLogger() for logging
- Never use print() for production code
```

#### Directive System
```
@fullauto - Default mode (full automation)
@ask - Request approval before proceeding
@ASK - ONE AI TOKEN REQUEST (token tracking)
@manual - User handles manually
```

#### Precedence Rule
```
UPPERCASE TRUMPS LOWERCASE
@ASK > @ask
@DOIT > @doit
@FULLAUTO > @fullauto
```

#### Tag System
```
#JARVIS - JARVIS system
@jarvis - JARVIS mention
@r5 - R5 Living Context Matrix
@v3 - V3 Verification Logic
#peak - PEAK quality standards
#bullshitmeter - Reliability tracking
```

### How AI Should Use Rules:
1. **Always check .cursorrules first** - These are persistent
2. **Apply rules automatically** - No need to ask
3. **Respect precedence** - UPPERCASE > lowercase
4. **Follow code standards** - Enforce in all code generation
5. **Use tags appropriately** - Follow tag definitions

---

## 🎮 LAYER 2: +COMMAND (Command Patterns)

### Purpose
Define **action-oriented commands** that trigger specific behaviors.

### Command Patterns:

#### Execution Commands
```
@DOIT - Execute immediately, end-to-end
@END2END - Full end-to-end validation
@V3 - Verification, Validation, Verify (3-step)
```

#### Directive Commands
```
@FULLAUTO - Full automation (default)
@ASK - Request approval
@MANUAL - Manual handling
```

#### System Commands
```
@JARVIS - Use JARVIS system
@R5 - Use R5 Living Context Matrix
@V3 - Use V3 verification
@AIQ - Use AI Quorum system
```

### Command Semantics:

#### @DOIT
**Meaning:** Execute immediately, complete end-to-end
**Includes:** @END2END validation
**Behavior:**
- Execute the task completely
- Perform end-to-end validation
- Look for discoveries and alternatives
- Address context confidence concerns
- Report findings

**Example:**
```
User: "@DOIT - Create character avatar system"
AI:
1. Creates system
2. Validates end-to-end
3. Discovers patterns
4. Explores alternatives
5. Reports confidence score
```

#### @END2END
**Meaning:** Full end-to-end validation
**Behavior:**
- Validate all components
- Check integration points
- Discover patterns
- Explore alternatives
- Calculate confidence score

#### @V3
**Meaning:** Verify, Validate, Verify (3-step process)
**Behavior:**
- Step 1: Verify inputs
- Step 2: Validate process
- Step 3: Verify outputs
- Always runs before main workflow

### How AI Should Use Commands:
1. **Parse commands first** - Check for @COMMAND patterns
2. **Respect precedence** - UPPERCASE > lowercase
3. **Execute completely** - @DOIT means full execution
4. **Include validation** - @DOIT includes @END2END
5. **Report results** - Always report command execution

---

## 👤 LAYER 3: PROFILE PROMPTS (User/System Profiles)

### Purpose
Define **personas, expertise, and behavioral patterns** for AI interactions.

### Profile Types:

#### 1. Person Profiles
**Location:** `data/lumina_person_profiles/profiles.json`
**Purpose:** Define user personas, expertise, preferences

**Structure:**
```json
{
  "profile_id": "user_001",
  "name": "User Name",
  "expertise": ["Software Engineering", "AI Systems"],
  "preferences": {
    "communication_style": "direct",
    "detail_level": "high",
    "validation_required": true
  },
  "persona": "ML/AI Scientist"
}
```

#### 2. System Profiles
**Location:** `config/temperature_control_profiles.json`
**Purpose:** Define system behavior profiles

**Structure:**
```json
{
  "profile_id": "scientist",
  "name": "ML/AI Scientist",
  "temperature": 0.7,
  "expertise": [
    "Machine Learning",
    "AI Systems",
    "Human-AI Interaction"
  ],
  "approach": "data-driven, systematic, evidence-based"
}
```

#### 3. Role Profiles
**Purpose:** Define AI roles for specific tasks

**Examples:**
- **ML/AI Scientist** - Data-driven analysis, systematic problem-solving
- **Software Engineer** - Code-first, practical solutions
- **System Architect** - Big picture, integration focus
- **Project Manager** - Coordination, timeline focus

### How AI Should Use Profiles:
1. **Check for profile** - Look for explicit role/profile
2. **Apply persona** - Use profile's expertise and approach
3. **Respect preferences** - Follow user preferences
4. **Adapt communication** - Match profile's style
5. **Use expertise** - Leverage profile's knowledge areas

---

## 📝 LAYER 4: STRUCTURED REQUESTS (v1.0 Framework)

### Purpose
Define **explicit, structured task definitions** for clarity.

### Template:
```markdown
## ROLE
[Define AI's role]

## CONTEXT (Priority Order)
### PRIMARY
[Essential information]

### SECONDARY
[Supporting information]

### REFERENCE
[Available but don't load]

## TASK
**Action:** [Clear action verb]
**Goal:** [What success looks like]
**Constraints:** [Limitations]

## DECOMPOSITION
**Step 1:** [Action] → Validate: [How to check]

## OUTPUT_FORMAT
[How to present results]

## SUCCESS_CRITERIA
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## 🔄 INTEGRATION: How All Layers Work Together

### Processing Order:
1. **+RULES** (Persistent) - Load workspace rules first
2. **+COMMAND** (Action) - Parse command patterns
3. **PROFILE** (Persona) - Apply user/system profile
4. **STRUCTURED REQUEST** (Task) - Execute structured task

### Example Flow:

```
User Request:
"@DOIT - Find outstanding VA todos as ML/AI Scientist"

Processing:
1. +RULES: Load .cursorrules
   → Apply code standards
   → Check directive system (@DOIT = full execution)
   → Check precedence (UPPERCASE @DOIT)

2. +COMMAND: Parse @DOIT
   → Execute immediately
   → Include @END2END validation
   → Report discoveries

3. PROFILE: Apply "ML/AI Scientist"
   → Use data-driven approach
   → Systematic problem-solving
   → Evidence-based recommendations
   → Clear metrics

4. STRUCTURED REQUEST: Execute task
   → ROLE: ML/AI Scientist
   → TASK: Find outstanding VA todos
   → CONTEXT: Master/padawan todos
   → OUTPUT: Markdown table
   → VALIDATION: End-to-end check
```

---

## 📊 COMPLETE REQUEST TEMPLATE (v2.0)

```markdown
# [Request Title]

## +RULES (Auto-Loaded)
[AI automatically loads .cursorrules and config rules]

## +COMMAND
[Command patterns to execute]
Examples:
- @DOIT - Execute end-to-end
- @END2END - Full validation
- @V3 - 3-step verification
- @FULLAUTO - Full automation
- @ASK - Request approval

## PROFILE
**Role:** [ML/AI Scientist, Software Engineer, etc.]
**Persona:** [From profiles.json if available]
**Expertise:** [Relevant knowledge areas]
**Approach:** [How this role thinks/works]

## CONTEXT (Priority Order)
### PRIMARY
[Essential information - load first]

### SECONDARY
[Supporting information - load if needed]

### REFERENCE
[Available but don't load unless needed]

## TASK
**Action:** [Clear action verb]
**Goal:** [What success looks like]
**Constraints:** [Limitations/requirements]

## DECOMPOSITION
**Step 1:** [Specific action]
  → Validate: [How to check if successful]

**Step 2:** [Next action]
  → Validate: [How to check if successful]

## OUTPUT_FORMAT
[How to present results]

## SUCCESS_CRITERIA
- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)

## VALIDATION
[How to verify success]
- @END2END if @DOIT
- @V3 if specified
- Custom validation
```

---

## 🎯 EXAMPLES

### Example 1: Simple Request with Command
```
User: "@DOIT - Find outstanding VA todos"

AI Processing:
1. +RULES: Load .cursorrules (code standards, tags)
2. +COMMAND: @DOIT → Execute end-to-end with validation
3. PROFILE: Default (or detect from context)
4. STRUCTURED:
   - TASK: Find VA todos
   - CONTEXT: Master/padawan todos
   - OUTPUT: Markdown table
   - VALIDATION: @END2END check
```

### Example 2: Complex Request with Profile
```
User: "As ML/AI Scientist, @DOIT - Analyze AI guidance process and provide framework"

AI Processing:
1. +RULES: Load .cursorrules
2. +COMMAND: @DOIT → Full execution + validation
3. PROFILE: ML/AI Scientist
   - Data-driven analysis
   - Systematic problem-solving
   - Evidence-based recommendations
   - Clear metrics
4. STRUCTURED:
   - ROLE: ML/AI Scientist
   - TASK: Analyze process, create framework
   - CONTEXT: Previous requests, tool usage
   - OUTPUT: Comprehensive framework document
   - VALIDATION: @END2END analysis
```

### Example 3: Request with Multiple Commands
```
User: "@V3 @DOIT - Create character system"

AI Processing:
1. +RULES: Load .cursorrules
2. +COMMAND:
   - @V3 → 3-step verification first
   - @DOIT → Then full execution
3. PROFILE: Default
4. STRUCTURED:
   - Execute @V3 verification
   - Then execute @DOIT task
   - Include @END2END validation
```

---

## 🔍 AI PROCESSING CHECKLIST

When receiving a request, AI should:

### 1. Parse +RULES
- [ ] Load .cursorrules
- [ ] Check config/*_rules.json
- [ ] Load shortag_registry.json
- [ ] Apply code standards
- [ ] Check directive system
- [ ] Respect precedence (UPPERCASE > lowercase)

### 2. Parse +COMMAND
- [ ] Detect @COMMAND patterns
- [ ] Parse command semantics
- [ ] Check precedence
- [ ] Plan command execution
- [ ] Include required validations

### 3. Apply PROFILE
- [ ] Check for explicit role/profile
- [ ] Load profile from profiles.json if available
- [ ] Apply persona and expertise
- [ ] Adapt communication style
- [ ] Use profile's approach

### 4. Execute STRUCTURED REQUEST
- [ ] Define role (from profile or request)
- [ ] Load context (priority order)
- [ ] Decompose task
- [ ] Execute steps with validation
- [ ] Format output
- [ ] Validate success criteria

### 5. Execute COMMANDS
- [ ] Run @V3 if specified
- [ ] Execute @DOIT task
- [ ] Include @END2END if @DOIT
- [ ] Report discoveries
- [ ] Provide metrics

---

## 📈 METRICS & VALIDATION

### Quality Metrics:
- **Rule Compliance:** % of rules followed
- **Command Execution:** Commands executed correctly
- **Profile Match:** Profile applied correctly
- **Structured Request:** Template followed
- **Overall Quality:** Composite score

### Validation:
- **@V3:** 3-step verification
- **@END2END:** End-to-end validation
- **Success Criteria:** All criteria met
- **Rule Compliance:** All rules followed

---

## 🎓 KEY PRINCIPLES

1. **Rules are Persistent** - Always apply workspace rules
2. **Commands are Actions** - Execute immediately when detected
3. **Profiles are Personas** - Adapt behavior to profile
4. **Structure is Clarity** - Use structured requests for complex tasks
5. **Precedence Matters** - UPPERCASE > lowercase
6. **Validation is Required** - @DOIT includes @END2END
7. **Metrics are Essential** - Always provide measurable results

---

## 📚 DOCUMENTATION

- **Framework v1.0:** `AI_GUIDANCE_PROCESS_ROAST_AND_REPAIR.md`
- **Request Template:** `AI_REQUEST_TEMPLATE.md`
- **This Document:** `AI_GUIDANCE_COMPLETE_FRAMEWORK.md`
- **Rules:** `.cursorrules`
- **Commands:** See command patterns above
- **Profiles:** `data/lumina_person_profiles/profiles.json`

---

**Tags:** #AI_GUIDANCE #RULES #COMMANDS #PROFILES #FRAMEWORK #COMPLETE @JARVIS @LUMINA

**Status:** ✅ **COMPLETE FRAMEWORK v2.0 - READY FOR USE**
