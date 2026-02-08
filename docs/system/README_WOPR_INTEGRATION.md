"""
WOPR Integration Summary: Balancing Dual-Tree Development
Location: .lumina/docs/system/README_WOPR_INTEGRATION.md
License: MIT / Apache 2.0
Public: System integration overview

Executive summary of how WOPR orchestrates balanced development between
PUBLIC (.lumina) and PRIVATE (cedarbrook-*) trees.
"""

# 🎯 WOPR Integration Summary: Dual-Tree Balance

## The Challenge

You're building two related but divergent codebases:

| Aspect | PRIVATE (cfs-llc-env) | PUBLIC (.lumina) |
|--------|-----|--------|
| **Content** | Real business logic, real data, secrets | Generic frameworks, sanitized, OSS |
| **Development** | Production company code | Reusable open-source patterns |
| **Audience** | Internal team | GitHub community |
| **License** | Proprietary | MIT/Apache 2.0 |

**The Problem:** How do you develop in PRIVATE while extracting and maintaining synchronized code patterns in PUBLIC?

---

## The Solution: WOPR Operations

**WOPR** (War Operation Plan Response) is your **development operations framework** that handles the coordination, validation, and synchronization.

### What WOPR Does

```
┌─────────────────────────────────────────┐
│         WOPR COMMAND CENTER             │
│  (Monitoring, Validation, Coordination) │
├─────────────────────────────────────────┤
│                                         │
│  ✓ Track development in both trees      │
│  ✓ Coordinate extraction workflow       │
│  ✓ Validate code quality & security     │
│  ✓ Synchronize shared base code         │
│  ✓ Generate operational metrics         │
│  ✓ Block unsafe extractions             │
│  ✓ Manage version consistency           │
│                                         │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┴────────────┐
    ▼                         ▼
PRIVATE TREE            PUBLIC TREE
(Production)            (OSS)
```

---

## WOPR Operations in Action

### Scenario: Extracting a Feature

**You build a new algorithm in your PRIVATE tree:**

```python
# cfs-llc-env/portfolio_analyzer.py - REAL COMPANY CODE
class PortfolioAnalyzer:
    def calculate_risk(self, customer_id):
        customer = DB.fetch(customer_id)      # Real data
        positions = fetch_real_positions(...)  # Real positions
        risk = ML_MODEL.predict(positions)    # Proprietary
        email_customer(...)                   # Company logic
        return risk
```

**WOPR helps you extract just the generic algorithm:**

```
STEP 1: Identify
  ↓ [WOPR marks for extraction]
STEP 2: Extract Generic Version
  ↓ [Remove customer_id, real data, company logic]
  
  # .lumina/portfolio_analysis.py - GENERIC
  class PortfolioAnalyzer:
      def calculate_risk(self, portfolio_data):
          features = extract_features(portfolio_data)
          risk = score_risk(features)
          return risk
  
  ↓ [WOPR validates reusability]
STEP 3: Validate
  ↓ [Check: no company refs, no secrets, generic algo]
STEP 4: Sanitization Scan
  ↓ [WOPR pre-push scan blocks leaks]
STEP 5: Push to Public
  ↓ [Commit to GitHub]
STEP 6: Complete
  ↓ [WOPR updates extraction log]
```

**All with WOPR checkpoints ensuring quality & security.**

---

## WOPR's Four Key Functions

### 1. MONITOR (Track Both Trees)

```bash
python scripts/python/wopr_ops.py --daily-ops
```

**Checks:**

- Is code quality maintained in both?
- Are shared patterns still synchronized?
- Any security violations?
- Extraction queue status?
- Development blockers?

**Output:** Daily operational status

### 2. COORDINATE (Manage Extraction Pipeline)

```bash
# Mark code for extraction
wopr_ops.py --phase extraction --task portfolio_analyzer --status pending

# Track extraction progress
wopr_ops.py --phase extraction --task portfolio_analyzer --status in-progress

# Complete extraction
wopr_ops.py --phase extraction --task portfolio_analyzer --status completed
```

**What WOPR orchestrates:**

- Extraction workflow (7 steps)
- Code review gate
- Sanitization validation
- Quality checks
- Version consistency

### 3. VALIDATE (Ensure Quality & Security)

**Every extraction WOPR validates:**

✅ **Code Reusability**

- Generic algorithm (works on any data)?
- Not tightly coupled to company context?
- Solves a general problem?

✅ **Security Compliance**

- No company references (cedarbrook, etc.)?
- No real data/credentials?
- No PII (customer names, emails)?
- No API keys or secrets?

✅ **Code Quality**

- Passes linting?
- Tests passing?
- Documentation complete?
- Follows style guide?

**If ANY check fails:** WOPR blocks the extraction ❌

### 4. SYNCHRONIZE (Keep Shared Code Consistent)

Some code is **shared between trees** (same in both):

```
Shared Base Patterns:
├── ai_token_request_tracker.json
├── ai_token_request_tracker.py
├── token_budget_enforcement.py
├── aiq_triage_jedi.py
└── pre_push_sanitization.py
```

**WOPR ensures they stay in sync:**

```bash
wopr_ops.py --phase synchronization --task cross-tree-hash-check
```

**Output:**

```
✅ ai_token_request_tracker.py - SYNCED
✅ token_budget_enforcement.py - SYNCED
❌ wopr_monitoring.py - DIVERGED (needs update)
```

---

## Three Development Patterns

### Pattern 1: Shared Base Code (Synchronized)

```
.lumina/ai_token_request_tracker.py  ← SOURCE OF TRUTH
    ↓ (read-only copy)
cfs-llc-env/ai_token_request_tracker.py  ← IMPORTED

WOPR Action: Validate both are identical
```

**When to use:** Generic frameworks that both need (token tracking, budget enforcement, routing)

### Pattern 2: Company Extension (Inheritance)

```python
# PUBLIC: Generic base
# .lumina/portfolio_analysis.py
class PortfolioAnalyzer:
    def calculate_risk(self, data):
        return self.score_risk(data)

# PRIVATE: Company-specific override
# cfs-llc-env/portfolio_analysis_cedarbrook.py
from lumina.portfolio_analysis import PortfolioAnalyzer

class CedarbrookPortfolioAnalyzer(PortfolioAnalyzer):
    def calculate_risk(self, customer_id):
        data = DB.fetch(customer_id)
        return super().calculate_risk(data)
```

**When to use:** When company needs specialized behavior (real data, custom logic)

### Pattern 3: Private Only (No Extraction)

```python
# cfs-llc-env/proprietary_trading_algorithm.py
class TradingEngine:
    """NEVER extracted - pure company IP"""
    def trade(self, ...):
        # Proprietary algorithms, real money
        ...
```

**When to use:** Proprietary IP that should never be public

---

## WOPR Command Quick Reference

```bash
# Daily Operations
wopr_ops.py --daily-ops              # Full health check
wopr_monitoring.py --status          # Tree monitoring
wopr_status_report.py --print        # Operational dashboard

# Extraction Workflow
wopr_ops.py --phase extraction --task NAME --status pending        # Mark
wopr_ops.py --phase extraction --task NAME --status in-progress   # Validate
wopr_ops.py --phase extraction --task NAME --status completed     # Complete

# Synchronization
wopr_ops.py --phase synchronization --task cross-tree-hash-check  # Check sync
wopr_ops.py --apply-patch cfs-llc-env/                           # Fix divergence

# Weekly Review
wopr_ops.py --weekly-review --analyze-divergence  # Full analysis
```

---

## Real Example: Feature Extraction Timeline

**Monday:** New feature built in private tree

```bash
git commit -am "feat: Portfolio risk analyzer"
# Code uses real customer data, proprietary algorithms
```

**Tuesday:** Mark for potential extraction

```bash
wopr_ops.py --phase extraction --task portfolio_analyzer --status pending
# WOPR notes: "Core algorithm may be reusable"
```

**Wednesday:** Extract generic version

```python
# Strip company logic, create .lumina/portfolio_analysis.py
# Generic version accepts any data structure
```

**Thursday:** Validation

```bash
wopr_ops.py --phase extraction --task portfolio_analyzer --status in-progress

# WOPR checks:
# ✅ No company references
# ✅ No real data access
# ✅ Generic algorithm
# ✅ Tests passing
# ✅ Pre-push scan: PASS
```

**Friday:** Push to GitHub

```bash
cd .lumina
git push origin main
# Portfolio analysis pattern now in public GitHub
```

**Monday:** Mark complete

```bash
wopr_ops.py --phase extraction --task portfolio_analyzer --status completed
# WOPR logs: "Extraction complete, extraction time 5 days"
```

---

## Success Metrics (Tracked by WOPR)

```bash
wopr_status_report.py --metrics
```

| Metric | Target | Purpose |
|--------|--------|---------|
| **Sync Health** | >95% | Ensure shared code stays consistent |
| **Extraction Success** | >90% | Most extractions pass validation |
| **Security Violations** | 0 | No data leaks to public |
| **Code Quality** | >A | Maintain standards in both trees |
| **Extraction Velocity** | 2-3/week | Regular pattern flow to public |
| **Reuse Ratio** | >70% | HIGH code sharing (good design) |

---

## WOPR Protects You From

### ❌ Accidentally Leaking Secrets

```python
# WOPR blocks this
# .lumina/api_handler.py
API_KEY = "sk-prod-12345..."  # ← Detected by pre-push scan
```

**WOPR action:** Blocks commit until removed ✅

### ❌ Extracting Non-Reusable Code

```python
# WOPR blocks this
class CedarbrookReportGenerator:
    """Too company-specific"""
    def __init__(self):
        self.company_name = "Cedarbrook Financial"  # ← Detected
```

**WOPR action:** Reusability check fails ✅

### ❌ Keeping Code Out of Sync

```bash
# WOPR detects this
❌ ai_token_request_tracker.py differs between trees
   .lumina/: hash_abc123
   cfs-llc-env/: hash_def456
```

**WOPR action:** Alerts you to sync divergence ✅

### ❌ Breaking Shared Code

```python
# WOPR prevents this
# Someone edits shared code in cfs-llc-env/, forgetting it's also in .lumina/
# WOPR detects divergence on next sync check
```

**WOPR action:** Forces re-synchronization ✅

---

## Getting Started with WOPR

### 1. Check Current Status (Today)

```bash
python scripts/python/wopr_ops.py --daily-ops
python scripts/python/wopr_status_report.py --print
```

### 2. Schedule Weekly Reviews (Every Friday)

```bash
python scripts/python/wopr_ops.py --weekly-review
```

### 3. Use WOPR for All Extractions

When extracting a feature, use WOPR workflow:

1. Mark with WOPR
2. Extract to PUBLIC
3. Validate with WOPR
4. Push to GitHub
5. Complete in WOPR

### 4. Daily Sync Checks

```bash
python scripts/python/wopr_ops.py --daily-ops
# Just 30 seconds, catches issues early
```

---

## Files to Read

| Document | Purpose |
|----------|---------|
| [WOPR_DUAL_TREE_BALANCE.md](./WOPR_DUAL_TREE_BALANCE.md) | Complete strategy & architecture |
| [WOPR_QUICK_OPS_GUIDE.md](./WOPR_QUICK_OPS_GUIDE.md) | Day-to-day operations guide |
| [SYNC_WORKFLOW_PRIVATE_TO_PUBLIC.md](./SYNC_WORKFLOW_PRIVATE_TO_PUBLIC.md) | 7-phase extraction process |
| [PUBLIC_PRIVATE_FORK_STRATEGY.md](./PUBLIC_PRIVATE_FORK_STRATEGY.md) | Fork architecture & rules |

---

## Summary

**WOPR = Development Operations for Dual-Tree Balance**

- ✅ Monitors both trees continuously
- ✅ Coordinates extraction workflow with validation checkpoints
- ✅ Validates code quality, security, reusability
- ✅ Synchronizes shared base code (single source of truth)
- ✅ Tracks metrics & generates reports
- ✅ Blocks unsafe extractions automatically

**Result:** You can develop production code in PRIVATE while safely extracting generic patterns to PUBLIC, with WOPR ensuring quality, security, and consistency automatically.

---

**Project:** .lumina v2.0 + WOPR Operations  
**Status:** FULLY INTEGRATED ✅  
**Last Updated:** 2025-12-10

## Automation & Enforcement Layer

- JARVIS auto-orchestrates WOPR runs and shift handoffs
- Marvin enforces pessimistic QA gates on extractions and shared code
- HK-47 probes perimeter (MCP/LB) and flags external risks to WOPR
- Selector obeys Council policy (allow/deny models, temp caps) and logs to R5

## Next Steps

1. Run morning check: `wopr_ops.py --daily-ops`
2. Review WOPR dashboard: `wopr_status_report.py --print`
3. Read full strategy: [WOPR_DUAL_TREE_BALANCE.md](./WOPR_DUAL_TREE_BALANCE.md)
4. Use for your next extraction: Follow [WOPR_QUICK_OPS_GUIDE.md](./WOPR_QUICK_OPS_GUIDE.md)
