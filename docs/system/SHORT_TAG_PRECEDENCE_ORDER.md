# Short @Tag Precedence Order - Agent Chat Context Meta

**Date**: 2026-01-03  
**Status**: ✅ **ACTIVE PRECEDENCE RULES**  
**Tag**: @JARVIS @MARVIN @AI @CONTEXT

---

## Precedence Order Rules

### Rule #1: UPPERCASE TRUMPS LOWERCASE

**CRITICAL RULE**: **UPPERCASE tags have higher precedence than lowercase tags**

- ✅ **`@ASK`** (uppercase) > **`@ask`** (lowercase)
- ✅ **`@DOIT`** (uppercase) > **`@doit`** (lowercase)
- ✅ **`@FULLAUTO`** (uppercase) > **`@fullauto`** (lowercase)
- ✅ **UPPERCASE = Higher priority, stronger directive**
- ✅ **lowercase = Lower priority, weaker directive**

**Why**: Subconscious pattern - uppercase naturally draws attention and indicates importance/priority.

---

## Complete Precedence Hierarchy

### Level 1: UPPERCASE Directives (Highest Precedence)

**UPPERCASE tags always win over lowercase**

1. **`@ASK`** - ONE AI TOKEN REQUEST (uppercase)
2. **`@DOIT`** - ORDER 66 execution (uppercase)
3. **`@FULLAUTO`** - Full automation (uppercase)
4. **`@MANUAL`** - Manual override (uppercase)

### Level 2: Lowercase Directives (Lower Precedence)

**Lowercase tags are overridden by uppercase**

1. **`@ask`** - AI interaction directive (lowercase)
2. **`@doit`** - Execution directive (lowercase)
3. **`@fullauto`** - Automation directive (lowercase)
4. **`@manual`** - Manual directive (lowercase)

### Level 3: System Tags (Contextual)

**System tags provide context but don't override directives**

1. **`@grep`** - Pattern search tool (WINS in pattern hierarchy)
2. **`@v3`** - V3 Verification Logic
3. **`@r5`** - R5 Living Context Matrix
4. **`@jarvis`** - J.A.R.V.I.S. system
5. **`@lumina`** - Project Lumina ecosystem

### Level 4: Hashtag Categories (Lowest Precedence)

**Hashtags provide categorization but lowest precedence**

1. **`#syphon`** - grep alias (lower ranked)
2. **`#patterns`** - Pattern concepts
3. **`#peak`** - PEAK quality standards
4. **`#decisioning`** - Decision-making process
5. **`#audit`** - Audit process
6. **`#triage`** - Triage/assessment

---

## Precedence Examples

### Example 1: UPPERCASE vs lowercase

```
Input: "@ask @ASK"
Result: @ASK wins (uppercase trumps lowercase)
Behavior: ONE AI TOKEN REQUEST (not AI interaction directive)
```

### Example 2: Directive Conflict

```
Input: "@fullauto @FULLAUTO"
Result: @FULLAUTO wins (uppercase trumps lowercase)
Behavior: Full automation with uppercase priority
```

### Example 3: Multiple Directives

```
Input: "@ask @DOIT @fullauto"
Result: @DOIT wins (uppercase, highest priority)
Behavior: ORDER 66 execution (uppercase directive)
```

### Example 4: System Tags + Directives

```
Input: "@jarvis @ASK @v3"
Result: @ASK wins (uppercase directive), @jarvis and @v3 provide context
Behavior: ONE AI TOKEN REQUEST with JARVIS and V3 verification context
```

---

## Precedence Resolution Algorithm

### Step 1: Identify All Tags

Extract all `@tags` and `#hashtags` from input.

### Step 2: Separate by Case

Group tags by:
- **UPPERCASE** directives
- **lowercase** directives
- **System** tags (mixed case, contextual)
- **Hashtags** (categories)

### Step 3: Apply Precedence Rules

1. **UPPERCASE directives** → Highest priority
2. **lowercase directives** → Lower priority (overridden by uppercase)
3. **System tags** → Contextual (don't override directives)
4. **Hashtags** → Categorization (lowest precedence)

### Step 4: Resolve Conflicts

- If multiple **UPPERCASE** directives: Use first encountered or most specific
- If **UPPERCASE** + **lowercase**: **UPPERCASE wins**
- If multiple **lowercase**: Use first encountered
- **System tags** and **hashtags** provide context but don't override

---

## Tag Type Precedence

### 1. Directives (Highest)

**UPPERCASE Directives**:
- `@ASK` - ONE AI TOKEN REQUEST
- `@DOIT` - ORDER 66 execution
- `@FULLAUTO` - Full automation
- `@MANUAL` - Manual override

**lowercase Directives**:
- `@ask` - AI interaction
- `@doit` - Execution
- `@fullauto` - Automation
- `@manual` - Manual

### 2. System Tags (Contextual)

- `@grep` - Pattern search (WINS in pattern hierarchy)
- `@v3` - V3 Verification Logic
- `@r5` - R5 Living Context Matrix
- `@jarvis` - J.A.R.V.I.S. system
- `@lumina` - Project Lumina ecosystem
- `@c3po` - C-3PO Protocol Droid
- `@helpdesk` - Helpdesk system

### 3. Hashtags (Categorization)

- `#syphon` - grep alias
- `#patterns` - Pattern concepts
- `#peak` - PEAK quality standards
- `#decisioning` - Decision-making
- `#audit` - Audit process
- `#triage` - Triage/assessment
- `#TOYSAAC` - Think Of Yourself As A Customer

---

## Special Cases

### Pattern Search Hierarchy

Within pattern search tags:
1. **`@grep`** - WINS! (highest precedence)
2. **`#syphon`** - Lower ranked alias
3. **`#patterns`** - Lowest ranked concepts

**Note**: Even within this hierarchy, uppercase versions would trump lowercase if they existed.

### Directive Override Chain

```
@MANUAL > @FULLAUTO > @DOIT > @ASK (uppercase)
@manual > @fullauto > @doit > @ask (lowercase)
```

**UPPERCASE always trumps lowercase at any level.**

---

## Implementation Notes

### Agent Chat Context Metadata

When processing agent chat context metadata:

1. **Extract all tags** from input
2. **Categorize by case** (UPPERCASE, lowercase, mixed)
3. **Apply precedence rules** (UPPERCASE trumps lowercase)
4. **Resolve conflicts** using precedence hierarchy
5. **Apply directives** in precedence order
6. **Include context tags** (system tags, hashtags) for context

### Subconscious Pattern Recognition

**Why UPPERCASE trumps lowercase:**
- ✅ Natural attention draw (uppercase stands out)
- ✅ Visual hierarchy (uppercase = importance)
- ✅ Pattern recognition (uppercase = priority)
- ✅ Subconscious preference (naturally gravitate to uppercase)
- ✅ **"Its utility in the Force is strong"** - The uppercase precedence rule is powerful and naturally intuitive

---

## Quick Reference Table

| Precedence | Tag Type | Example | Behavior |
|------------|----------|---------|----------|
| **1** | UPPERCASE Directive | `@ASK` | Highest priority, trumps lowercase |
| **2** | lowercase Directive | `@ask` | Lower priority, overridden by uppercase |
| **3** | System Tag | `@jarvis` | Contextual, doesn't override directives |
| **4** | Hashtag | `#peak` | Categorization, lowest precedence |

---

## Summary

✅ **UPPERCASE TRUMPS LOWERCASE** - Critical precedence rule  
✅ **UPPERCASE directives** = Highest priority  
✅ **lowercase directives** = Lower priority (overridden by uppercase)  
✅ **System tags** = Contextual (don't override)  
✅ **Hashtags** = Categorization (lowest precedence)

**Key Rule**: When in doubt, **UPPERCASE wins**. This is why uppercase is used subconsciously - it naturally indicates priority and importance.

**"Its utility in the Force is strong"** - The uppercase precedence rule is powerful, intuitive, and naturally aligns with how humans process visual hierarchy. UPPERCASE commands attention and priority, making it the perfect pattern for directive precedence in agent chat context metadata.

---

**Last Updated**: 2026-01-03  
**Maintained By**: @JARVIS @MARVIN
