# WOPR Architecture: Visual System Design

## System Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                    WOPR DEVELOPMENT ORCHESTRATION                      │
│                                                                        │
│  "How to Balance Development Between PRIVATE and PUBLIC Trees"        │
└────────────────────────────────────────────────────────────────────────┘

                          ┌─────────────────────┐
                          │   WOPR COMMAND      │
                          │   CENTER            │
                          │                     │
                          │ ✓ Monitor           │
                          │ ✓ Coordinate        │
                          │ ✓ Validate          │
                          │ ✓ Synchronize       │
                          └──────────┬──────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
                    ▼                ▼                ▼
            ┌──────────────┐  ┌──────────────┐  ┌─────────────┐
            │  MONITOR     │  │ COORDINATE   │  │  VALIDATE   │
            │  MODULE      │  │  MODULE      │  │  MODULE     │
            ├──────────────┤  ├──────────────┤  ├─────────────┤
            │ • Tree health│  │ • Extraction │  │ • Security  │
            │ • Code sync  │  │ • Workflow   │  │ • Quality   │
            │ • Security   │  │ • Phases     │  │ • Reusable  │
            │ • Metrics    │  │ • Validation │  │ • Sanitize  │
            └────────┬─────┘  └──────┬───────┘  └──────┬──────┘
                     │               │                 │
                     └───────────────┼─────────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
        ▼                            ▼                            ▼
┌─────────────────────┐    ┌─────────────────────┐    ┌──────────────────┐
│   PRIVATE TREE      │    │  SHARED CODE        │    │   PUBLIC TREE    │
│   (cfs-llc-env)     │    │  (SSOT)             │    │   (.lumina)      │
├─────────────────────┤    ├─────────────────────┤    ├──────────────────┤
│ • Production code   │    │ • Generic base      │    │ • Generic        │
│ • Real data/logic   │    │ • Patterns          │    │   patterns       │
│ • Proprietary IP    │    │ • Frameworks        │    │ • Sanitized      │
│ • Company-specific  │    │ • Utilities         │    │ • OSS-ready      │
│ • Secrets (stored)  │    │                     │    │ • Public GitHub  │
│                     │    │ Status: SYNCED      │    │                  │
└────────┬────────────┘    └─────────┬───────────┘    └────────┬─────────┘
         │                           │                        │
         │                           │                        │
         └─ Daily Sync Check ────────┴────── Daily Sync Check─┘
         └─ Extraction Workflow ───────────► Verification ──┘
         └─ Development ─────────────────► GitHub ──┘
```

---

## Development Workflow with WOPR

```
START: New Feature in PRIVATE Tree
│
├─ Monday: Code Feature
│  ├─ Build in cfs-llc-env/ (private tree)
│  └─ Uses real data, company logic
│
├─ Tuesday: Check Reusability
│  ├─ Is this feature generic enough?
│  ├─ WOPR: Mark for extraction (pending)
│  └─ Review: What parts are public?
│
├─ Wednesday: Extract to PUBLIC
│  ├─ Create .lumina/version of code
│  ├─ Remove company references
│  ├─ Remove real data access
│  └─ Keep generic algorithm
│
├─ Thursday: WOPR Validation
│  ├─ ✅ Security scan (no secrets, no PII)
│  ├─ ✅ Reusability check (generic algorithm)
│  ├─ ✅ Code quality (tests, linting)
│  ├─ ✅ Pre-push sanitization
│  └─ If ANY fail: back to Wednesday
│
├─ Friday: Push to GitHub
│  ├─ Commit to .lumina on main
│  ├─ WOPR: Update extraction log
│  └─ Code now public/open-source
│
└─ END: Code in both trees, patterns synchronized
```

---

## Extraction Pipeline (7 Steps with WOPR Checkpoints)

```
┌─ Phase 1: IDENTIFY ─────────────────────────────┐
│ Developer marks code for extraction in PRIVATE  │
│ Status: pending                                 │
│ WOPR: Create extraction task record             │
└───────────────────────────────────────────────┬─┘
                                                │
                                ┌───────────────▼
┌─ Phase 2: EXTRACT ──────────────────────────┐
│ Copy code from PRIVATE to PUBLIC             │
│ Remove company-specific logic                │
│ Create .lumina/version                       │
│ Status: in-progress                          │
│ WOPR: Track extraction in progress           │
└───────────────────────────────────────────┬─┘
                                            │
                        ┌───────────────────▼
┌─ Phase 3: VALIDATE ─────────────────────┐
│ Is it truly generic? (No company refs)   │
│ Is it reusable? (Works on any data)      │
│ WOPR Checks:                             │
│  ✅ No cedarbrook references            │
│  ✅ No customer IDs in code             │
│  ✅ No secrets/API keys                 │
│  ✅ Generic algorithm                   │
│ Status: validation                       │
└───────────────────────────────────────┬─┘
                                        │
                    ┌───────────────────▼
┌─ Phase 4: SANITIZE ──────────────────┐
│ Pre-push security scan                │
│ Check for:                            │
│  • Hardcoded credentials              │
│  • Real customer data                 │
│  • PII (emails, names, SSN)           │
│  • API keys or tokens                 │
│  • Internal URLs or IPs               │
│ WOPR: Run sanitization scanner        │
│ If ANY found: BLOCK (return to Ph 2)  │
│ Status: sanitized                     │
└───────────────────────────────────────┬──┐
                                        │  │
                    ┌───────────────────▼  │
┌─ Phase 5: CODE REVIEW ───────────────┐  │
│ Human review by team                 │  │
│ Check:                               │  │
│  • Code quality                      │  │
│  • Documentation complete?           │  │
│  • Tests passing?                    │  │
│  • Follows style guide?              │  │
│ Status: approved                     │  │
└───────────────────────────────────────┬─┤
                                        │ │
                    ┌───────────────────▼ │
┌─ Phase 6: PUSH TO GITHUB ────────────┐ │
│ Commit to .lumina/main               │ │
│ Code now public                      │ │
│ WOPR: Mark extraction as pushed      │ │
│ Status: deployed                     │ │
└───────────────────────────────────────┬─┤
                                        │ │
                    ┌───────────────────▼ │
┌─ Phase 7: COMPLETE ──────────────────┐ │
│ WOPR marks extraction complete       │ │
│ Log velocity (time from identify)    │ │
│ Mark hash for sync verification      │ │
│ Status: completed                    │ │
└──────────────────────────────────────┘ │
                                         │
                    ┌────────────────────┘
                    │
                    ▼
        ┌────────────────────────┐
        │ EXTRACTION COMPLETE    │
        │ Pattern now in PUBLIC  │
        │ Both trees updated     │
        └────────────────────────┘
```

---

## Code Patterns: How They Flow

### Pattern 1: Shared Base Code (Synchronized)

```
PRIVATE TREE                    PUBLIC TREE (SSOT)
┌─────────────────────┐         ┌──────────────────────┐
│ cfs-llc-env/        │         │ .lumina/             │
│                     │◄────────│                      │
│ ai_token_tracker.py │  (copy) │ ai_token_tracker.py  │
│ (read-only mirror)  │         │ (source of truth)    │
└─────────────────────┘         └──────────────────────┘
                                       ▲
                                       │
                                WOPR Sync Check
                                (hash must match)
```

**Usage:** Generic utility code needed by both (token tracking, enforcement)

### Pattern 2: Private Extensions (Inheritance)

```
PUBLIC BASE                     PRIVATE EXTENSION
┌────────────────────┐         ┌──────────────────────┐
│ .lumina/           │         │ cfs-llc-env/         │
│                    │         │                      │
│ class Analyzer:    │         │ from .lumina import  │
│   def analyze():   │◄────────│ Analyzer             │
│     return data    │ (inherit)│                      │
└────────────────────┘         │ class CFS_Analyzer:  │
                               │   def analyze():     │
                               │     real_data = DB() │
                               │     return super()   │
                               └──────────────────────┘
```

**Usage:** When private needs company-specific behavior on top of generic base

### Pattern 3: Private Only (No Sync)

```
PRIVATE TREE                    (NOT IN PUBLIC)
┌──────────────────────────────┐
│ cfs-llc-env/                 │
│                              │
│ class TradingEngine:         │
│   """Proprietary code"""     │
│   def execute_trade():       │
│     # Real money, secret IP  │
│     ...                      │
│                              │
│ Status: NEVER EXTRACTED      │
└──────────────────────────────┘
```

**Usage:** Proprietary IP that should never be public

---

## WOPR Validation Pipeline

```
Code arrives for extraction
        │
        ▼
┌────────────────────┐
│ SECURITY SCAN      │
├────────────────────┤
│ ✓ No credentials?  │
│ ✓ No customer ID?  │
│ ✓ No company ref?  │
│ ✓ No PII?          │
└─────────┬──────────┘
          │
    [FAIL]└──► BLOCK ❌ (return to developer)
    [PASS]└──┐
             ▼
    ┌────────────────────┐
    │ REUSABILITY CHECK  │
    ├────────────────────┤
    │ ✓ Generic algo?    │
    │ ✓ Works on any     │
    │   data structure?  │
    │ ✓ Not tied to      │
    │   company context? │
    └─────────┬──────────┘
              │
        [FAIL]└──► BLOCK ❌
        [PASS]└──┐
                 ▼
        ┌────────────────────┐
        │ QUALITY CHECK      │
        ├────────────────────┤
        │ ✓ Tests pass?      │
        │ ✓ Linting ok?      │
        │ ✓ Documented?      │
        │ ✓ Style guide?     │
        └─────────┬──────────┘
                  │
            [FAIL]└──► BLOCK ❌
            [PASS]└──┐
                     ▼
            ✅ APPROVED
            Ready for push
            to GitHub
```

---

## Daily Operations: WOPR Monitoring

```
Every Morning:
┌──────────────────────────────────────┐
│ python wopr_ops.py --daily-ops       │
├──────────────────────────────────────┤
│ Check 1: Tree Health                 │
│  • PRIVATE tree status               │
│  • PUBLIC tree status                │
│  • Any blockers?                     │
│                                      │
│ Check 2: Synchronization             │
│  • Shared code in sync?              │
│  • Hash mismatches?                  │
│  • Need sync fixes?                  │
│                                      │
│ Check 3: Security                    │
│  • Any leaks detected?               │
│  • Secrets exposed?                  │
│  • Compliance ok?                    │
│                                      │
│ Check 4: Extraction Pipeline         │
│  • Pending extractions?              │
│  • In-progress tasks?                │
│  • Waiting for review?               │
│                                      │
│ Check 5: Metrics                     │
│  • Sync health %                     │
│  • Extraction success rate           │
│  • Code quality trend                │
│                                      │
│ Output: ✅ ALL GREEN (proceed)       │
│    or   ❌ ALERTS (fix before dev)   │
└──────────────────────────────────────┘
        │
        ├─► All Good? → Continue Development
        │
        └─► Issues? → Fix First (e.g., sync divergence)
```

---

## Weekly Review: WOPR Analytics

```
Every Friday:
┌────────────────────────────────────────┐
│ python wopr_ops.py --weekly-review     │
├────────────────────────────────────────┤
│ Report 1: Divergence Analysis          │
│  • What's different between trees?     │
│  • Need to reconcile anything?         │
│  • Planned or accidental?              │
│                                        │
│ Report 2: Extraction Velocity          │
│  • How many features extracted?        │
│  • How long on average?                │
│  • Blockers slowing us down?           │
│                                        │
│ Report 3: Code Quality Trends          │
│  • Test coverage trend                 │
│  • Bug rate trend                      │
│  • Performance impact                  │
│                                        │
│ Report 4: Security Metrics             │
│  • Zero leaks this week?               │
│  • Scan effectiveness                  │
│  • Compliance status                   │
│                                        │
│ Report 5: Team Impact                  │
│  • How much time on extractions?       │
│  • Blocking issues?                    │
│  • Training needed?                    │
│                                        │
│ Action Items for Next Week             │
└────────────────────────────────────────┘
```

---

## Risk Mitigation: What WOPR Prevents

```
Risk 1: LEAKING SECRETS
┌───────────────────────┐
│ Accidentally commit   │     WOPR Response:
│ API_KEY = "xxxx"     │     ✅ Blocks at push
│ PASSWORD = "xxxx"    │     ✅ Pre-commit scan
│ to PUBLIC GitHub     │     ✅ Alerts team
└───────────────────────┘

Risk 2: EXPOSING REAL DATA
┌───────────────────────┐
│ Customer names,       │     WOPR Response:
│ emails, SSNs          │     ✅ Detects patterns
│ accidentally in code  │     ✅ Sanitization scan
│ pushed to public      │     ✅ Blocks suspicious
└───────────────────────┘

Risk 3: CODE DIVERGENCE
┌───────────────────────┐
│ Shared code updated   │     WOPR Response:
│ in PRIVATE but not    │     ✅ Daily hash check
│ reflected in PUBLIC   │     ✅ Detects mismatch
│ (or vice versa)       │     ✅ Alerts for sync
└───────────────────────┘

Risk 4: EXTRACTING NON-REUSABLE CODE
┌───────────────────────┐
│ Company-specific      │     WOPR Response:
│ code pushed to GitHub │     ✅ Reusability check
│ as generic            │     ✅ Reference detection
│ (confusing users)     │     ✅ Blocks approval
└───────────────────────┘

Risk 5: QUALITY REGRESSION
┌───────────────────────┐
│ Public code quality   │     WOPR Response:
│ drops due to merging  │     ✅ Pre-merge checks
│ broken private code   │     ✅ Test requirement
│ patterns              │     ✅ Code review gate
└───────────────────────┘
```

---

## System Dependencies

```
WOPR Core
├── wopr_ops.py
│   ├── Status tracking
│   ├── Phase management
│   ├── Daily operations
│   └── Weekly reviews
│
├── wopr_monitoring.py
│   ├── Tree health checks
│   ├── Security alerts
│   └── Performance tracking
│
├── wopr_integration.py
│   ├── Holocron Archive integration
│   ├── Threat intelligence feeds
│   └── Coordinated response
│
├── wopr_status_report.py
│   └── Operational dashboard
│
├── pre_push_sanitization.py
│   ├── Secret detection
│   ├── PII scanning
│   └── Leak prevention
│
└── token_budget_enforcement.py
    └── Development resource tracking
```

---

## Summary Table

| Aspect | Purpose | Command |
|--------|---------|---------|
| **Daily Monitor** | Tree health check | `wopr_ops.py --daily-ops` |
| **Weekly Review** | Analytics & metrics | `wopr_ops.py --weekly-review` |
| **Mark Extraction** | Start pipeline | `wopr_ops.py --phase extraction --task X --status pending` |
| **Validate Extract** | Security/quality check | `wopr_ops.py --phase extraction --task X --status in-progress` |
| **Push Complete** | Extraction finished | `wopr_ops.py --phase extraction --task X --status completed` |
| **Sync Check** | Validate shared code | `wopr_ops.py --phase synchronization --task cross-tree-hash-check` |
| **Status Report** | Current dashboard | `wopr_status_report.py --print` |

---

**Document:** WOPR Architecture Diagram  
**Purpose:** Visual reference for dual-tree development system  
**Status:** Reference Complete ✅
