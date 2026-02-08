# Command Patterns Reference
## Complete Guide to +COMMAND Patterns

**Date:** 2026-01-09
**Status:** ✅ **COMPLETE REFERENCE**

---

## 🎮 COMMAND PATTERNS

### Execution Commands

#### @DOIT
**Meaning:** Execute immediately, complete end-to-end
**Includes:** @END2END validation automatically
**Behavior:**
- Execute the task completely
- Perform end-to-end validation
- Look for discoveries and alternatives
- Address context confidence concerns
- Report findings and metrics

**Usage:**
```
@DOIT - [Task description]
```

**Example:**
```
User: "@DOIT - Create character avatar system"
AI:
1. Creates complete system
2. Validates end-to-end
3. Discovers patterns
4. Explores alternatives
5. Reports confidence score
6. Provides metrics
```

**Precedence:** UPPERCASE @DOIT > lowercase @doit

---

#### @END2END
**Meaning:** Full end-to-end validation
**Behavior:**
- Validate all components
- Check integration points
- Discover patterns
- Explore alternatives
- Calculate confidence score
- Report issues and recommendations

**Usage:**
```
@END2END - [Validation scope]
```

**Example:**
```
User: "@END2END - Validate character system"
AI:
1. Validates character registry
2. Checks hierarchy consistency
3. Verifies MOB system
4. Tests integration points
5. Calculates confidence score
6. Reports findings
```

**Note:** Automatically included with @DOIT

---

#### @V3
**Meaning:** Verify, Validate, Verify (3-step process)
**Behavior:**
- Step 1: Verify inputs
- Step 2: Validate process
- Step 3: Verify outputs
- Always runs before main workflow

**Usage:**
```
@V3 - [Task description]
```

**Example:**
```
User: "@V3 - Create character system"
AI:
1. Verify: Check inputs (requirements, context)
2. Validate: Validate process (architecture, design)
3. Verify: Verify outputs (code, tests, docs)
```

**Implementation:** `scripts/python/v3_verification.py`

---

### Directive Commands

#### @FULLAUTO
**Meaning:** Full automation mode (default)
**Behavior:**
- Execute without approval
- Full automation
- No user interaction required

**Usage:**
```
@FULLAUTO - [Task description]
```

**Precedence:** UPPERCASE @FULLAUTO > lowercase @fullauto

---

#### @ASK
**Meaning:** Request approval before proceeding
**Behavior:**
- Request user approval
- Wait for confirmation
- Proceed after approval

**Usage:**
```
@ASK - [Task description]
```

**Precedence:** UPPERCASE @ASK > lowercase @ask

**Note:** UPPERCASE @ASK = ONE AI TOKEN REQUEST (token tracking system)

---

#### @MANUAL
**Meaning:** User handles manually
**Behavior:**
- Don't execute automatically
- Provide instructions
- User handles execution

**Usage:**
```
@MANUAL - [Task description]
```

---

### System Commands

#### @JARVIS
**Meaning:** Use JARVIS system
**Behavior:**
- Route through JARVIS
- Use JARVIS automation
- Apply JARVIS patterns

**Usage:**
```
@JARVIS - [Task description]
```

**Context Weight:** 1.0
**AI Weight:** 0.8
**Human Weight:** 0.2

---

#### @R5
**Meaning:** Use R5 Living Context Matrix
**Behavior:**
- Aggregate context
- Extract patterns
- Generate living context matrix

**Usage:**
```
@R5 - [Task description]
```

**Implementation:** `scripts/python/r5_living_context_matrix.py`

**Context Weight:** 1.0
**AI Weight:** 0.9
**Human Weight:** 0.1

---

#### @V3
**Meaning:** Use V3 verification logic
**Behavior:**
- Apply 3-step verification
- Always part of global workflow
- Runs before main workflow execution

**Usage:**
```
@V3 - [Task description]
```

**Implementation:** `scripts/python/v3_verification.py`

**Context Weight:** 1.0
**AI Weight:** 0.8
**Human Weight:** 0.2

---

#### @AIQ
**Meaning:** Use AI Quorum system
**Behavior:**
- Get AI consensus
- Use quorum for decisions
- Apply AIQ patterns

**Usage:**
```
@AIQ - [Decision description]
```

**Context Weight:** 1.0
**AI Weight:** 0.9
**Human Weight:** 0.1

---

## 🔄 COMMAND COMBINATIONS

### @V3 @DOIT
**Meaning:** Verify first, then execute
**Behavior:**
1. Run @V3 verification
2. Then execute @DOIT task
3. Include @END2END validation

**Example:**
```
User: "@V3 @DOIT - Create character system"
AI:
1. @V3: Verify inputs, validate process, verify outputs
2. @DOIT: Execute task completely
3. @END2END: Validate end-to-end
```

---

### @ASK @DOIT
**Meaning:** Request approval, then execute
**Behavior:**
1. Request approval
2. Wait for confirmation
3. Execute @DOIT task

**Example:**
```
User: "@ASK @DOIT - Delete old files"
AI:
1. @ASK: "Are you sure you want to delete old files?"
2. Wait for user confirmation
3. @DOIT: Execute deletion
```

---

## 📊 PRECEDENCE RULES

### UPPERCASE > lowercase
```
@DOIT > @doit
@ASK > @ask
@FULLAUTO > @fullauto
@V3 > @v3
```

### Execution Order
1. **@V3** - Verification first (if specified)
2. **@ASK** - Request approval (if specified)
3. **@DOIT** - Execute task
4. **@END2END** - Validate (automatic with @DOIT)

---

## 🎯 USAGE GUIDELINES

### When to Use @DOIT
- Complex tasks requiring full execution
- Tasks needing end-to-end validation
- Tasks requiring discovery and alternatives
- Tasks needing confidence scoring

### When to Use @END2END
- Validation-only tasks
- System health checks
- Integration validation
- Quality assurance

### When to Use @V3
- Critical tasks requiring verification
- Tasks with high risk
- Tasks needing 3-step validation
- Pre-workflow verification

### When to Use @ASK
- Destructive operations
- High-risk tasks
- Tasks requiring user input
- Tasks needing approval

### When to Use @MANUAL
- Tasks user wants to handle
- Tasks requiring manual intervention
- Tasks AI shouldn't execute
- Learning/educational tasks

---

## 📝 EXAMPLES

### Example 1: Simple Execution
```
User: "@DOIT - Find outstanding VA todos"
AI: Executes task completely with validation
```

### Example 2: Verification First
```
User: "@V3 @DOIT - Create character system"
AI: Verifies first, then executes
```

### Example 3: Approval Required
```
User: "@ASK @DOIT - Delete old files"
AI: Requests approval, then executes
```

### Example 4: System Integration
```
User: "@JARVIS @DOIT - Automate workflow"
AI: Uses JARVIS system to execute task
```

### Example 5: Context Aggregation
```
User: "@R5 @DOIT - Analyze codebase"
AI: Uses R5 to aggregate context, then executes
```

---

## 🔍 COMMAND DETECTION

### Pattern Matching
- **@COMMAND** - Uppercase (high priority)
- **@command** - Lowercase (lower priority)
- **@COMMAND @COMMAND** - Multiple commands

### Parsing Rules
1. Detect all @COMMAND patterns
2. Check precedence (UPPERCASE > lowercase)
3. Determine execution order
4. Plan command execution
5. Execute in order

---

## ✅ VALIDATION

### Command Execution Validation
- [ ] Command detected correctly
- [ ] Precedence applied correctly
- [ ] Execution order correct
- [ ] All commands executed
- [ ] Results reported

---

**Tags:** #COMMANDS #PATTERNS #REFERENCE #GUIDE @JARVIS @LUMINA

**Status:** ✅ **COMPLETE REFERENCE**
