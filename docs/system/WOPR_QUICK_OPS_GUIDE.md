"""
WOPR Dual-Tree Operations Quick Guide
Location: .lumina/docs/system/WOPR_QUICK_OPS_GUIDE.md
License: MIT / Apache 2.0
Public: Development operations reference

Quick start for using WOPR to balance development between PUBLIC and PRIVATE trees.
"""

# 🚀 WOPR Dual-Tree Operations Quick Guide

## The Balance Problem

You have two mirrored trees:

- **PRIVATE** (`cfs-llc-env/`) - Real company code, real data, IP
- **PUBLIC** (`.lumina/`) - Generic frameworks, sanitized, OSS-ready

**Challenge:** How to develop in PRIVATE while extracting reusable patterns to PUBLIC, keeping them synchronized?

**Solution:** WOPR handles the coordination.

---

## Morning Routine: Check Sync Status

```bash
cd d:\Dropbox\my_projects

# 1. Check overall health
python scripts/python/wopr_ops.py --daily-ops

# 2. Check trees are properly synchronized
python scripts/python/wopr_monitoring.py --status

# 3. View operational dashboard
python scripts/python/wopr_status_report.py --print
```

**Expected Output:**

```
✅ Shared code sync: 100% (all base patterns matched)
✅ Security violations: 0
✅ Pending extractions: 2 (on track)
✅ Sync health: 95%
```

---

## Development Workflow

### When Adding New Code to PRIVATE Tree

```
1. Write code in cfs-llc-env/
2. Test thoroughly with real data
3. Code review & merge to private

✓ Is this reusable?
   YES → Tag it: # @WOPR_EXTRACT: YES
   NO  → Leave alone (company-specific)
```

### Example: Portfolio Analysis Feature

**Step 1: Write in PRIVATE**

```python
# cfs-llc-env/cedarbrook_services/portfolio_analyzer.py

class PortfolioAnalyzer:
    """
    Real company: Analyze customer portfolios
    
    @WOPR_EXTRACT: YES - Core algorithm is reusable
    @WOPR_SANITIZE: Remove customer_id, real data access
    """
    
    def calculate_risk(self, customer_id):
        # Real company: fetch real data
        customer = DB.fetch(customer_id)
        positions = fetch_real_positions(customer)
        risk_score = ML_MODEL.predict(positions)
        
        # Notify customer
        email_alert(customer.email, risk_score)
        return risk_score
```

**Step 2: Mark for Extraction**

```bash
# Tell WOPR this code is ready to extract
python scripts/python/wopr_ops.py \
  --phase "extraction" \
  --task "mark_portfolio_analyzer" \
  --status "pending" \
  --notes "Core algorithm is reusable on generic data"
```

**Step 3: Create Public Version**

```python
# .lumina/scripts/python/portfolio_analysis.py

class PortfolioAnalyzer:
    """Generic portfolio analysis - works on any data structure"""
    
    def calculate_risk(self, portfolio_data):
        """
        Args:
            portfolio_data: {holdings: [...], weights: [...], ...}
        Returns:
            {"risk": score, "efficiency": value}
        """
        features = self.extract_features(portfolio_data)
        risk = self.score_risk(features)
        efficiency = self.score_efficiency(portfolio_data)
        
        return {
            "risk": risk,
            "efficiency": efficiency
        }
    
    def extract_features(self, portfolio_data):
        # Generic feature extraction (no company-specific logic)
        return {...}
    
    def score_risk(self, features):
        # Generic risk scoring
        return score
```

**Step 4: Validate with WOPR**

```bash
# WOPR validates the extraction
python scripts/python/wopr_ops.py \
  --phase "extraction" \
  --task "validate_portfolio_analyzer" \
  --status "in-progress" \
  --notes "Checking reusability and security"
```

**What WOPR checks:**

- ✅ No company references (cedarbrook, financial-services, etc.)
- ✅ No real data access (database, API, file reading)
- ✅ No PII (customer names, emails, IDs)
- ✅ Generic algorithm (works on any data)
- ✅ No secrets (API keys, credentials, configs)

**Step 5: Sanitization Scan**

```bash
# WOPR runs pre-push sanitization
cd .lumina
python ../../scripts/python/pre_push_sanitization.py

# Output:
# ✅ PASS - Safe to push to GitHub
```

**Step 6: Commit to Public**

```bash
cd .lumina
git add scripts/python/portfolio_analysis.py docs/...
git commit -m "feat: add generic portfolio analysis framework"
git push origin main
```

**Step 7: Mark Extraction Complete**

```bash
python scripts/python/wopr_ops.py \
  --phase "extraction" \
  --task "portfolio_analyzer" \
  --status "completed" \
  --notes "Extracted to .lumina/scripts/python/portfolio_analysis.py"
```

---

## Synchronization: Shared Base Code

**Some code is genuinely SHARED** - same in both trees (read-only):

```
Base Patterns (SYNCED):
├── ai_token_request_tracker.json
├── ai_token_request_tracker.py
├── token_budget_enforcement.py
├── aiq_triage_jedi.py
└── pre_push_sanitization.py
```

**Sync Strategy:**

- `.lumina/` is the **source of truth** (canonical)
- `cfs-llc-env/` imports/copies from `.lumina/`
- WOPR validates they stay in sync

**Check sync:**

```bash
python scripts/python/wopr_ops.py \
  --phase "synchronization" \
  --task "cross-tree-hash-check" \
  --compare ".lumina/" "cfs-llc-env/"
```

**If out of sync:**

```
❌ ai_token_request_tracker.py - DIVERGED
  .lumina/ version: hash_abc123
  cfs-llc-env/ version: hash_def456
  
Action: Copy from .lumina/ to cfs-llc-env/
```

---

## Weekly Review: WOPR Dashboard

**Every Friday:** Run full operational review

```bash
python scripts/python/wopr_status_report.py --print
```

**Review these metrics:**

| Metric | Target | Action if Miss |
|--------|--------|-----------------|
| Sync Health | >95% | Identify divergence issues |
| Security Violations | 0 | Fix before next extraction |
| Extraction Queue | <5 pending | Schedule for extraction |
| Code Quality | >A | Review failing files |
| Test Coverage | >80% | Add missing tests |

---

## When Things Go Wrong

### Problem: Code Can't Be Extracted

**Example:** Risk scoring uses proprietary ML model

```python
class RiskScorer:
    def score(self, features):
        # ❌ This can't be extracted - proprietary model
        return PROPRIETARY_ML_MODEL.predict(features)
```

**Solution:** Extract the interface, not the implementation

```python
# PUBLIC: Generic interface
class RiskScorer:
    def score(self, features):
        """Override in subclasses with actual scoring logic"""
        raise NotImplementedError()

# PRIVATE: Real implementation
class CedarbrookRiskScorer(RiskScorer):
    def score(self, features):
        return PROPRIETARY_ML_MODEL.predict(features)
```

### Problem: Public Code Has Leaked Company Data

**WOPR blocks this automatically:**

```bash
# Pre-push scan found leaks!
❌ FAIL - portfolio_analysis.py contains:
  Line 42: cedarbrook-specific customer analysis
  Line 67: Reference to internal database
  
Action: Remove company-specific code before extracting
```

**Fix:** Remove all company references

```python
# BEFORE (has cedarbrook reference)
def analyze_cedarbrook_customer(customer_id):
    ...

# AFTER (generic)
def analyze_portfolio(portfolio_data):
    ...
```

### Problem: Trees Get Out of Sync

**WOPR detects this:**

```bash
python scripts/python/wopr_ops.py --weekly-review

⚠️  DIVERGENCE DETECTED
  ai_token_request_tracker.py differs between trees
  
Reason: Fix applied to .lumina but not cfs-llc-env

Action: 
  1. Copy updated file from .lumina/ to cfs-llc-env/
  2. Re-run sync check
  3. Commit in cfs-llc-env/
```

---

## Daily Checklist

**Do this every day:**

```
☐ Morning: python scripts/python/wopr_ops.py --daily-ops
☐ Check: Any red flags in WOPR status?
☐ Develop: Add code to PRIVATE tree (cfs-llc-env)
☐ Tag: Mark reusable code with @WOPR_EXTRACT
☐ Test: Run tests in both trees
```

**Do this every week:**

```
☐ Friday: python scripts/python/wopr_status_report.py --print
☐ Review: Pending extractions ready?
☐ Extract: Move 2-3 patterns to PUBLIC
☐ Sync: Verify shared code matches
☐ Report: Note metrics, blockers, next week plan
```

---

## Key Principles

1. **Develop in PRIVATE first** (real use drives real code)
2. **Extract patterns, not implementations** (generic algorithms)
3. **Inherit, don't fork** (PUBLIC base class → PRIVATE subclass)
4. **WOPR validates everything** (security, quality, reusability)
5. **Keep shared code synced** (single source of truth in PUBLIC)
6. **Tag code for extraction** (@WOPR_EXTRACT comments)
7. **Review weekly** (metrics, progress, blockers)

---

## Common Scenarios

### Scenario 1: Bug Fix in Public Code

```
1. Fix found in .lumina/ (PUBLIC)
2. Update there first ✓
3. Run: wopr_ops --sync-check
4. WOPR copies to cfs-llc-env/ ✓
5. Done
```

### Scenario 2: New Feature in Private Code

```
1. Code written in cfs-llc-env/ ✓
2. Tag with @WOPR_EXTRACT if reusable
3. Tested with real data ✓
4. Extracted to .lumina/ (remove company bits)
5. WOPR validates extraction ✓
6. Push to GitHub ✓
7. Mark complete in WOPR ✓
```

### Scenario 3: Company-Specific Enhancement

```
1. Code added in cfs-llc-env/
2. Extends base from .lumina/ (inheritance)
3. No new file in .lumina/ needed
4. WOPR tracks as "private extension" ✓
```

### Scenario 4: Security Patch Needed

```
1. Issue found in token_budget_enforcement.py (SHARED)
2. Fix in .lumina/ first ✓
3. Run: wopr_ops --apply-patch cfs-llc-env/
4. Both trees updated ✓
5. WOPR validates sync ✓
```

---

## WOPR Command Reference

```bash
# Daily health check
wopr_ops.py --daily-ops

# Full monitoring
wopr_monitoring.py --status

# Operational dashboard
wopr_status_report.py --print

# Mark code for extraction
wopr_ops.py --phase extraction --task NAME --status pending

# Validate extraction
wopr_ops.py --phase extraction --task NAME --status in-progress

# Complete extraction
wopr_ops.py --phase extraction --task NAME --status completed

# Check sync
wopr_ops.py --phase synchronization --task cross-tree-hash-check

# Apply patch across trees
wopr_ops.py --apply-patch cfs-llc-env/

# Weekly review
wopr_ops.py --weekly-review --analyze-divergence
```

---

## Success Metrics

**Track these with WOPR:**

| Metric | Target | Current |
|--------|--------|---------|
| Sync health | >95% | ? |
| Security violations | 0 | ? |
| Extraction success rate | >90% | ? |
| Code reuse ratio | >70% | ? |
| Time saved via reuse | | ? |

```bash
# See all metrics
python scripts/python/wopr_status_report.py --metrics
```

---

## Next Steps

1. **Today:** Run morning WOPR check
2. **This Week:** Extract 1-2 patterns using WOPR workflow
3. **Friday:** Review metrics with WOPR dashboard
4. **Ongoing:** Use WOPR for all extractions & sync validation

---

**Status:** WOPR Operational ✅  
**Last Updated:** 2025-12-10
