# @RR Tag Routing Quick Reference

**Quick lookup for tag combinations and their effects on @RR definitions**

---

## 🎯 @RR Definition Selection Rules

### Rule 1: Standalone @RR
- **Tag:** `@RR`
- **Definition:** PRIMARY - "Roast & Repair"
- **Behavior:** Identify issues → Fix them
- **Use When:** General problem-solving, code review, maintenance

### Rule 2: @RR + Security Context
- **Tags:** `@RR @COMPUSEC` OR `@RR @F4`
- **Definition:** SECONDARY - "Rapid Response"
- **Behavior:** Fastest threat response
- **Use When:** Security threats, urgent security operations

### Rule 3: @RR + Execution Context
- **Tags:** `@RR @DOIT`
- **Definition:** SECONDARY - "Rapid Response"
- **Behavior:** Speed-optimized execution
- **Use When:** Autonomous execution, urgent deployments

### Rule 4: @RR + Quantification
- **Tags:** `@RR @PEAK`
- **Definition:** ACTIVE priority (current active definition)
- **Behavior:** Effectiveness-quantified response
- **Use When:** Need quantified effectiveness tracking

### Rule 5: @RR + Validation
- **Tags:** `@RR @MARVIN`
- **Definition:** PRIMARY (with validation)
- **Behavior:** Roast & Repair with reality checking
- **Use When:** Need validation before execution

---

## 🔄 Tag Combination Matrix

| Combination | @RR Mode | Primary Behavior | Speed | Validation |
|-------------|----------|------------------|-------|------------|
| `@RR` | PRIMARY | Roast & Repair | Normal | None |
| `@RR @COMPUSEC` | SECONDARY | Rapid Response | Fast | Security |
| `@RR @DOIT` | SECONDARY | Rapid Response | Fastest | None |
| `@RR @F4` | SECONDARY | Rapid Response | Fast | Security |
| `@RR @PEAK` | ACTIVE | Quantified | Normal | Metrics |
| `@RR @MARVIN` | PRIMARY | Roast & Repair | Normal | Reality Check |
| `@RR @JARVIS` | SECONDARY | Rapid Response | Fast | Coordinated |
| `@RR @COMPUSEC @F4` | SECONDARY | Rapid Response | Fastest | Security |
| `@RR @DOIT @PEAK` | SECONDARY | Rapid Response | Fastest | Metrics |

---

## 📋 Role Responsibilities Quick Lookup

### @JARVIS
- **Primary:** Orchestration, execution coordination
- **With @RR:** Coordinates rapid response
- **With @DOIT:** Autonomous execution coordinator
- **With @PEAK:** Quantified operations coordinator

### @RR
- **Primary:** Roast & Repair (default)
- **Secondary:** Rapid Response (security/execution context)
- **Tertiary:** Root Cause Analysis (deep investigation)

### @PEAK
- **Primary:** Definition management, quantification
- **With @RR:** @RR definition manager
- **With @DOIT:** Execution optimization metrics
- **With @COMPUSEC:** Security effectiveness scoring

### @DOIT
- **Primary:** Autonomous execution
- **With @RR:** Rapid autonomous execution
- **With @PEAK:** Quantified execution paths
- **With @COMPUSEC:** Security-focused execution

### @MARVIN
- **Primary:** Reality checking, validation
- **With @RR:** Validates @RR responses
- **With @DOIT:** Validates autonomous execution
- **With @COMPUSEC:** Security threat validation

### @COMPUSEC
- **Primary:** Security operations
- **With @RR:** Security rapid response (switches @RR to secondary)
- **With @F4:** Threat response coordination
- **With @PEAK:** Security effectiveness quantification

### @F4
- **Primary:** Threat response (Fight/Fix/Fail/Forever)
- **With @COMPUSEC:** Security-focused threat response
- **With @RR:** Rapid threat response
- **With @PEAK:** Quantified response effectiveness

---

## 🚀 Common Tag Patterns

### Pattern 1: Fast Execution
```
@DOIT @RR
→ Rapid autonomous execution
→ Skip confirmations
→ Maximum speed
```

### Pattern 2: Security Response
```
@COMPUSEC @RR @F4
→ Security rapid response
→ Threat neutralization
→ Fastest security response
```

### Pattern 3: Validated Execution
```
@JARVIS @RR @MARVIN
→ Coordinated rapid response
→ Reality-checked
→ Validated before execution
```

### Pattern 4: Quantified Operations
```
@RR @PEAK @DOIT
→ Rapid response
→ Effectiveness quantified
→ Optimized execution
```

### Pattern 5: Deep Analysis
```
@RR @MARVIN @PEAK
→ Root cause analysis (if tertiary active)
→ Reality-checked
→ Quantified effectiveness
```

---

## 💡 Tag Selection Guidelines

### When to Use PRIMARY @RR (Roast & Repair)
- General problem-solving
- Code review
- System maintenance
- Non-urgent issues
- Need thorough analysis

### When to Use SECONDARY @RR (Rapid Response)
- Security threats (`@COMPUSEC`, `@F4`)
- Urgent deployments (`@DOIT`)
- Time-sensitive tasks
- Need speed over thoroughness

### When to Use TERTIARY @RR (Root Cause Analysis)
- Complex issues
- Recurring problems
- System architecture analysis
- Need deep investigation

### When to Combine Tags
- **@RR @DOIT:** Need fast autonomous execution
- **@RR @COMPUSEC:** Security rapid response needed
- **@RR @MARVIN:** Need validation before execution
- **@RR @PEAK:** Need effectiveness tracking
- **@RR @F4:** Security threat response needed

---

## 🎯 Quick Decision Tree

```
Request Type?
├─ Security Threat?
│  └─→ @RR @COMPUSEC @F4 (SECONDARY - Rapid Response)
├─ Urgent Deployment?
│  └─→ @RR @DOIT (SECONDARY - Rapid Response)
├─ Need Validation?
│  └─→ @RR @MARVIN (PRIMARY - Roast & Repair with validation)
├─ Need Quantification?
│  └─→ @RR @PEAK (ACTIVE - Quantified)
└─ General Problem?
   └─→ @RR (PRIMARY - Roast & Repair)
```

---

**Tags:** #RR #TAG_ROUTING #QUICK_REFERENCE #ROLES #RESPONSIBILITIES @JARVIS @LUMINA @PEAK @RR
