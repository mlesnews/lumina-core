# AI Guidance Quick Reference
## Complete Framework at a Glance

**Version:** 2.0
**Status:** ✅ **READY FOR USE**

---

## 🎯 THE FOUR LAYERS

```
1. +RULES      → Persistent workspace rules (.cursorrules)
2. +COMMAND    → Action commands (@DOIT, @END2END, @V3)
3. PROFILE     → Personas/profiles (ML/AI Scientist, etc.)
4. STRUCTURED  → Explicit task definitions (template)
```

---

## 📋 QUICK TEMPLATE

```markdown
# [Request Title]

## +COMMAND
@DOIT - [Execute end-to-end]
@END2END - [Full validation]
@V3 - [3-step verification]

## PROFILE
**Role:** ML/AI Scientist
**Approach:** Data-driven, systematic, evidence-based

## CONTEXT
### PRIMARY
[Essential - load first]

### SECONDARY
[Supporting - load if needed]

## TASK
**Action:** [Clear verb]
**Goal:** [Success criteria]
**Constraints:** [Limitations]

## OUTPUT_FORMAT
[Markdown table, JSON, etc.]

## SUCCESS_CRITERIA
- [ ] Criterion 1
- [ ] Criterion 2
```

---

## 🎮 COMMAND QUICK REFERENCE

| Command     | Meaning             | Includes                        |
| ----------- | ------------------- | ------------------------------- |
| `@DOIT`     | Execute end-to-end  | @END2END automatically          |
| `@END2END`  | Full validation     | Pattern discovery, alternatives |
| `@V3`       | 3-step verification | Verify → Validate → Verify      |
| `@FULLAUTO` | Full automation     | Default mode                    |
| `@ASK`      | Request approval    | Wait for confirmation           |
| `@MANUAL`   | User handles        | Provide instructions            |

**Precedence:** UPPERCASE > lowercase

---

## 👤 PROFILE QUICK REFERENCE

| Profile               | Expertise           | Approach                                |
| --------------------- | ------------------- | --------------------------------------- |
| **ML/AI Scientist**   | ML, AI Systems, HCI | Data-driven, systematic, evidence-based |
| **Software Engineer** | Code, Architecture  | Code-first, practical solutions         |
| **System Architect**  | Integration, Design | Big picture, integration focus          |
| **Project Manager**   | Coordination        | Timeline, coordination focus            |

---

## 📊 PROCESSING ORDER

```
1. Load +RULES (.cursorrules)
2. Parse +COMMAND patterns
3. Apply PROFILE persona
4. Execute STRUCTURED request
5. Run validations (@END2END if @DOIT)
6. Report results with metrics
```

---

## ✅ CHECKLIST

Before submitting:
- [ ] Command patterns specified (@DOIT, etc.)
- [ ] Profile/role defined
- [ ] Context prioritized (PRIMARY, SECONDARY)
- [ ] Task is clear and actionable
- [ ] Success criteria measurable
- [ ] Output format specified

---

## 📚 FULL DOCUMENTATION

- **Complete Framework:** `AI_GUIDANCE_COMPLETE_FRAMEWORK.md`
- **Command Patterns:** `COMMAND_PATTERNS_REFERENCE.md`
- **Request Template:** `AI_REQUEST_TEMPLATE.md`
- **Roast & Repair:** `AI_GUIDANCE_PROCESS_ROAST_AND_REPAIR.md`

---

**Tags:** #QUICK_REFERENCE #AI_GUIDANCE #FRAMEWORK @JARVIS @LUMINA
