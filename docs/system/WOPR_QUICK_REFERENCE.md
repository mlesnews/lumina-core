# WOPR Quick Reference Card

**Keep this handy while developing!**

---

## 🎯 THE BALANCE CHALLENGE

You have TWO mirrored codebases:

```
PRIVATE (cfs-llc-env)        PUBLIC (.lumina)
├─ Real code                 ├─ Generic patterns
├─ Company data              ├─ OSS-ready
├─ Proprietary IP            ├─ GitHub
└─ Secrets stored            └─ Community use
```

**Goal:** Extract generic patterns from PRIVATE to PUBLIC safely

---

## ⚡ QUICK START (Today)

### Morning Check (30 seconds)

```bash
cd d:\Dropbox\my_projects
python scripts/python/wopr_ops.py --daily-ops
```

**Expected output:**

```
✅ PRIVATE tree: OK
✅ PUBLIC tree: OK  
✅ Shared code: SYNCED
✅ No security alerts
✅ Ready to develop
```

### If Something's Wrong ❌

```bash
python scripts/python/wopr_status_report.py --print
# Shows what needs attention
```

---

## 🔄 THREE CODE PATTERNS

### Pattern 1️⃣ Shared Base (Both Trees, Must Stay Synced)

```python
# File exists in BOTH locations (identical)
.lumina/ai_token_request_tracker.py  ← SOURCE OF TRUTH
cfs-llc-env/ai_token_request_tracker.py  ← MIRROR COPY

# WOPR ensures they stay identical
# If one changes, update the other & run sync check
```

**When to use:** Generic utilities both teams need

### Pattern 2️⃣ Private Extension (Inheritance)

```python
# PUBLIC: Generic base
.lumina/portfolio_analyzer.py
    class PortfolioAnalyzer:
        def calculate_risk(self, data):
            return score(data)

# PRIVATE: Company-specific override  
cfs-llc-env/portfolio_analyzer_cedarbrook.py
    from .lumina import PortfolioAnalyzer
    class CedarbrookAnalyzer(PortfolioAnalyzer):
        def calculate_risk(self, customer_id):
            data = get_real_data(customer_id)
            return super().calculate_risk(data)
```

**When to use:** Need company-specific behavior on generic base

### Pattern 3️⃣ Private Only (Never Extract)

```python
# PRIVATE ONLY - NEVER in .lumina
cfs-llc-env/trading_engine.py
    class ProprietaryTradingEngine:
        """Never extracted - company IP"""
```

**When to use:** Proprietary algorithms, real customer logic

---

## 📋 EXTRACTION WORKFLOW (When Adding Feature to Public)

### The 7-Step Process

```
┌─ STEP 1: Code Feature in PRIVATE ─┐
│ cfs-llc-env/my_feature.py          │
│ (Uses real data, company logic)    │
└────────────────────────────────────┘
             ↓
┌─ STEP 2: Mark with WOPR ──────────┐
│ wopr_ops.py --phase extraction     │
│  --task my_feature --status        │
│  pending                           │
└────────────────────────────────────┘
             ↓
┌─ STEP 3: Extract Generic Version ─┐
│ .lumina/my_feature.py              │
│ (Remove company logic)             │
└────────────────────────────────────┘
             ↓
┌─ STEP 4: Validate with WOPR ──────┐
│ Security: ✅ No secrets?           │
│ Reusable: ✅ Generic?              │
│ Quality:  ✅ Tests pass?           │
│ Scan:     ✅ Pre-push scan         │
│                                    │
│ If ANY fail: Go back to STEP 3     │
│ If all pass: Continue              │
└────────────────────────────────────┘
             ↓
┌─ STEP 5: Code Review ─────────────┐
│ Team review of .lumina/my_feature  │
│ Check: Quality, docs, tests        │
└────────────────────────────────────┘
             ↓
┌─ STEP 6: Push to GitHub ──────────┐
│ git push .lumina main              │
│ Feature now public/OSS             │
└────────────────────────────────────┘
             ↓
┌─ STEP 7: Mark Complete ───────────┐
│ wopr_ops.py --phase extraction     │
│  --task my_feature --status        │
│  completed                         │
└────────────────────────────────────┘
```

---

## 🛡️ WOPR VALIDATION GATES (Automatic)

Every extraction WOPR checks **ALL** of these:

### ✅ Security Gate

```
❌ BLOCKED if found:
  • API_KEY = "..."
  • password = "..."
  • customer_id in code
  • cedarbrook references
  • Real employee emails
```

### ✅ Reusability Gate

```
❌ BLOCKED if:
  • Company-specific logic
  • Only works with real data
  • Hardcoded company values
  
✅ PASS if:
  • Works with any data
  • Generic algorithm
  • No company context needed
```

### ✅ Quality Gate

```
❌ BLOCKED if:
  • Tests failing
  • Linting errors
  • Missing documentation
  
✅ PASS if:
  • All tests green
  • Code style ok
  • Docs complete
```

---

## 🔧 WOPR COMMAND REFERENCE

### Daily Operations

```bash
# Check tree health (run every morning)
python scripts/python/wopr_ops.py --daily-ops

# View status dashboard
python scripts/python/wopr_status_report.py --print

# Quick monitoring
python scripts/python/wopr_monitoring.py --status
```

### Extraction Workflow

```bash
# Mark code for extraction
python scripts/python/wopr_ops.py --phase extraction \
  --task FEATURE_NAME --status pending

# During validation
python scripts/python/wopr_ops.py --phase extraction \
  --task FEATURE_NAME --status in-progress

# After pushing to GitHub
python scripts/python/wopr_ops.py --phase extraction \
  --task FEATURE_NAME --status completed
```

### Synchronization

```bash
# Check if shared code is in sync
python scripts/python/wopr_ops.py --phase synchronization \
  --task cross-tree-hash-check

# Fix divergence
python scripts/python/wopr_ops.py --apply-patch cfs-llc-env/
```

### Weekly Review

```bash
# Full analysis and metrics
python scripts/python/wopr_ops.py --weekly-review
```

---

## 📊 SUCCESS METRICS (Tracked Automatically)

| Metric | Target | Check |
|--------|--------|-------|
| Sync Health | >95% | Shared code consistency |
| Extraction Success | >90% | Features approved/extracted |
| Security Violations | 0 | No leaks to public |
| Code Quality | >A | Both trees maintained |
| Extraction Velocity | 2-3/week | Pattern flow to public |

---

## ⚠️ COMMON MISTAKES & HOW WOPR BLOCKS THEM

### ❌ Mistake 1: Forgetting to Remove Secrets

```python
# PRIVATE version (ok)
API_KEY = "sk-prod-abc123"

# You copy to PUBLIC by accident...
# WOPR BLOCKS: "❌ Secret detected: API_KEY"
```

### ❌ Mistake 2: Extracting Non-Generic Code

```python
# Too specific to company
class CedarbrookReportGenerator:
    company_name = "Cedarbrook Financial"  # ← Company ref!
    
# WOPR BLOCKS: "❌ Contains company references"
```

### ❌ Mistake 3: Forgetting to Sync Shared Code

```bash
# Someone updates ai_token_tracker.py in PRIVATE only
# Next morning...
# WOPR ALERTS: "❌ Sync divergence detected"
```

### ❌ Mistake 4: Pushing Tests That Don't Pass

```python
# PUBLIC code with failing tests
class Analyzer:
    def broken_method(self):
        return None  # No implementation
        
# WOPR BLOCKS: "❌ Tests failing"
```

---

## 📅 WEEKLY ROUTINE

### Monday

```bash
# Start of week sync check
python wopr_ops.py --daily-ops
```

### Tuesday-Thursday

```bash
# As you build features:
# 1. Code in PRIVATE
# 2. Mark with WOPR when ready
# 3. Extract to PUBLIC
# 4. WOPR validates
# 5. Submit for review
```

### Friday

```bash
# Weekly deep dive
python wopr_ops.py --weekly-review

# Check:
# - How many features extracted?
# - Any sync issues?
# - Code quality trends?
# - Security metrics?
# - Team blockers?
```

---

## 🚨 IF SOMETHING BREAKS

### Sync Divergence Detected

```bash
# WOPR error: "ai_token_tracker.py diverged"

# Check difference
diff .lumina/ai_token_tracker.py cfs-llc-env/ai_token_tracker.py

# Fix by updating the copy
cp cfs-llc-env/ai_token_tracker.py .lumina/
# OR edit the PRIVATE one if PUBLIC has the correct version

# Verify sync fixed
python wopr_ops.py --phase synchronization --task cross-tree-hash-check
```

### Extraction Blocked by Security

```bash
# WOPR error: "❌ Secret detected: PASSWORD"

# Find and remove it
grep -r "PASSWORD" .lumina/my_feature.py

# Edit file to remove secret

# Try validation again
python wopr_ops.py --phase extraction --task my_feature --status in-progress
```

### Code Quality Issues

```bash
# WOPR error: "❌ Tests failing"

# Run tests locally
pytest .lumina/tests/

# Fix failing tests

# Verify
pytest .lumina/tests/  # Should pass

# Continue extraction
python wopr_ops.py --phase extraction --task my_feature --status in-progress
```

---

## 💡 TIPS & TRICKS

### Tip 1: Use WOPR for Confidence

When extracting a feature, WOPR does the safety checks:

- Run `--daily-ops` before starting work
- Use WOPR to validate before pushing
- Trust the system = safe extraction

### Tip 2: Tag Code for WOPR

```python
# Mark code that may be extractable
class PortfolioAnalyzer:
    """
    WOPR_EXTRACTABLE: true
    WOPR_SECURITY: no-secrets, no-pii
    
    Generic portfolio analysis - safe to extract
    """
    def calculate_risk(self, data):
        ...
```

### Tip 3: Daily Sync = Peace of Mind

```bash
# 30 seconds every morning
python wopr_ops.py --daily-ops

# This catches issues early before they compound
```

### Tip 4: Weekly Review for Big Picture

```bash
# Friday: step back and review
python wopr_ops.py --weekly-review

# See: velocity, quality, security trends
# Plan: next week's extractions
```

### Tip 5: When in Doubt, Ask WOPR

```bash
# Not sure if code is extractable?
python wopr_status_report.py --print

# Shows what's pending, in progress, completed
# Helps you decide next steps
```

---

## 📚 DOCUMENTATION

| Doc | Purpose |
|-----|---------|
| **README_WOPR_INTEGRATION.md** | Start here - high-level overview |
| **WOPR_ARCHITECTURE_DIAGRAM.md** | Visual system design |
| **WOPR_DUAL_TREE_BALANCE.md** | Complete strategy |
| **WOPR_QUICK_OPS_GUIDE.md** | Day-to-day operations |
| **PUBLIC_PRIVATE_FORK_STRATEGY.md** | Architecture decisions |
| **SYNC_WORKFLOW_PRIVATE_TO_PUBLIC.md** | 7-phase extraction detail |

---

## ✅ CHECKLIST: Using WOPR

- [ ] Ran `wopr_ops.py --daily-ops` this morning
- [ ] Feature built in PRIVATE tree
- [ ] Decided: is it extractable? (Check WOPR_DUAL_TREE_BALANCE.md)
- [ ] If yes: Created generic version in PUBLIC (.lumina)
- [ ] Marked with WOPR: `--phase extraction --task X --status pending`
- [ ] Validated with WOPR: `--status in-progress`
  - [ ] No secrets/PII
  - [ ] Generic algorithm
  - [ ] Tests pass
  - [ ] Pre-push scan clear
- [ ] Code review done
- [ ] Pushed to GitHub
- [ ] Marked complete with WOPR: `--status completed`
- [ ] Next Friday: Run `wopr_ops.py --weekly-review`

---

**WOPR Quick Reference Card**  
**Keep this in your terminal for easy access**  
**Version:** 1.0  
**Last Updated:** 2025-12-10  

```bash
# Bookmark these commands
alias wopr-daily="python scripts/python/wopr_ops.py --daily-ops"
alias wopr-review="python scripts/python/wopr_ops.py --weekly-review"
alias wopr-status="python scripts/python/wopr_status_report.py --print"
```

---

## One Last Thing

> **The Balance is Simple:**
>
> - 🏢 **PRIVATE:** Real code, company logic, secrets safe
> - 🌍 **PUBLIC:** Generic patterns, OSS-ready, GitHub community
> - 🔄 **WOPR:** Keeps them synced, safe, and quality ✅
>
> Extract features safely. Build openly. Sleep well knowing WOPR is watching.
