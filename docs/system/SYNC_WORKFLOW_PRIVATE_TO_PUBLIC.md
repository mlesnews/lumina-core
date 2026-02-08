# Sync Workflow: Private → Public Extraction

**Purpose:** How to safely extract features from private company trees (`cedarbrook-*`) to public GitHub tree (`.lumina`)

**Audience:** Development team, DevOps, code review leads

**Integration:** Uses WOPR (War Operation Plan Response) for operational monitoring, validation, and coordination

See [WOPR_DUAL_TREE_BALANCE.md](./WOPR_DUAL_TREE_BALANCE.md) for complete operational strategy.

---

## Overview: Unidirectional Sync

```
PRIVATE TREES (cfs-llc-env v1.0)    EXTRACTION & SANITIZATION    PUBLIC TREE (.lumina v2.0)
────────────────────────────────────────────────────────────────────────────────────────
Real company operations ────────────────────────────────────────> Open-source framework
Proprietary algorithms                  (Strip IP, add docs)      Reusable patterns
Customer data, credentials              (Generic examples)        Educational content
Sensitive configs, real data            (Validate no leaks)       Safe for community
```

---

## Workflow: Step-by-Step

### Phase 1: Identify Reusable Feature (Private)

**Location:** Work in `cfs-llc-env/` (v1.0 active operations)

**Task:** You've built a successful feature. Is it reusable?

```python
# Example: Real company feature in cfs-llc-env/
class PortfolioAnalyzer:
    def calculate_risk(self, customer_id):
        """Real company: analyze specific customer portfolio"""
        customer = db.fetch_customer(customer_id)  # Real data
        portfolio = fetch_real_positions(customer)  # Real positions
        risk_score = ml_model.predict(portfolio)  # Proprietary model
        return risk_score, recommendation_email(customer.email)
```

**Questions to ask:**

- ✅ Is the core algorithm **reusable** on generic data?
- ✅ Can I strip the company-specific logic?
- ✅ Does it solve a **common problem** others face?
- ❌ Does it contain **PII, secrets, or IP**?
- ❌ Is it **tightly coupled** to real customer data?

**Decision:**

- **YES to reusable?** → Proceed to Phase 2
- **NO?** → Keep private, don't extract

---

### Phase 2: Extract Generic Pattern (Private)

**Location:** Still in `cfs-llc-env/`

**Task:** Isolate the reusable algorithm from company-specific context

```python
# Extract: Core portfolio analysis pattern (generic)
class PortfolioAnalyzer:
    def calculate_risk(self, portfolio_data):
        """Generic: analyze any portfolio structure"""
        # portfolio_data: {holdings: [...], weights: [...], sectors: [...]}
        features = self.extract_features(portfolio_data)
        risk_score = self.score_risk(features)
        efficiency = self.score_efficiency(portfolio_data)
        return {
            "risk": risk_score,
            "efficiency": efficiency
        }
```

**Key changes:**

- ❌ Remove: `customer_id`, database calls, real data access
- ❌ Remove: Email sending, recommendation logic
- ❌ Remove: Proprietary model (or replace with generic equivalent)
- ✅ Add: Generic data structure documentation
- ✅ Add: Example usage with sample data

---

### Phase 3: Create Public Version (Private & Public)

**Location:** Create new file in `.lumina/scripts/python/`

**Task:** Write public version with sanitized examples

```python
# .lumina/scripts/python/portfolio_analyzer.py
"""
PUBLIC: Generic Portfolio Analysis Framework
Location: .lumina/scripts/python/portfolio_analyzer.py
License: MIT / Apache 2.0

Simple framework for analyzing portfolio structures.
Emerged from real-world portfolio management patterns.
"""

class PortfolioAnalyzer:
    """Analyze portfolio risk and efficiency."""

    def calculate_risk(self, portfolio_data):
        """
        Calculate risk score for any portfolio structure.

        Args:
            portfolio_data (dict): {
                "holdings": [...],      # Security holdings
                "weights": [...],       # Allocation weights
                "sectors": [...]        # Sector allocations
            }

        Returns:
            dict: {
                "risk_score": float,      # 0.0-1.0
                "efficiency": float       # 0.0-1.0
            }

        Example:
            >>> analyzer = PortfolioAnalyzer()
            >>> portfolio = {
            ...     "holdings": ["AAPL", "MSFT", "GOOGL"],
            ...     "weights": [0.3, 0.5, 0.2],
            ...     "sectors": ["Tech", "Tech", "Tech"]
            ... }
            >>> result = analyzer.calculate_risk(portfolio)
            >>> print(result)
            {'risk_score': 0.65, 'efficiency': 0.72}
        """
        # Generic algorithm (no company data)
        features = self.extract_features(portfolio_data)
        risk = self.score_risk(features)
        efficiency = self.score_efficiency(portfolio_data)
        return {"risk_score": risk, "efficiency": efficiency}
```

---

### Phase 4: Document Design Decision (Public)

**Location:** Create file in `.lumina/docs/patterns/`

**Task:** Explain why this pattern exists, how to use it

```markdown
# Portfolio Analysis Pattern

## Origin

This pattern emerged from real-world portfolio management needs in 
financial operations. It extracts the core risk/efficiency calculation 
logic into a reusable framework.

## Problem

How do you analyze portfolio structures without:
- Coupling to specific customer databases
- Exposing proprietary trading algorithms
- Requiring real market data feeds

## Solution

Generic portfolio analyzer that works with:
- **Any data structure:** holdings, weights, sectors
- **Any risk model:** plug in your own scoring
- **Any use case:** evaluation, backtesting, monitoring

## Implementation

See: `.lumina/scripts/python/portfolio_analyzer.py`

## Example Usage

```python
analyzer = PortfolioAnalyzer()
portfolio = {
    "holdings": ["AAPL", "MSFT", "GOOGL"],
    "weights": [0.3, 0.5, 0.2],
    "sectors": ["Tech", "Tech", "Tech"]
}
result = analyzer.calculate_risk(portfolio)
```

## Extending

To use with your own data:

1. Transform your data to generic portfolio format
2. Optionally extend risk/efficiency scorers
3. Run analysis on anonymous portfolio data

## See Also

- [Master/Padawan Learner Pattern](../learner_pattern.md)
- [Token Tracking Framework](../token_tracking.md)

```

---

### Phase 5: Code Review & Sanitization Check (Private or Public)

**Location:** GitHub PR from `feature/extract-portfolio-analyzer` branch

**Task:** Verify no sensitive data leaked

**Checklist:**

```markdown
## Pre-Push Sanitization Checklist

- [ ] Run `python scripts/python/pre_push_sanitization.py` - PASS
- [ ] No company names (cedarbrook, CFS)
- [ ] No customer data (IDs, names, emails)
- [ ] No API keys or credentials
- [ ] No internal endpoints or URLs
- [ ] No proprietary algorithm details
- [ ] All configs are templates/examples
- [ ] File has PUBLIC header
- [ ] Documentation explains generic use case
- [ ] Examples use sample data
- [ ] Tests don't reference real company
- [ ] Code review: 2 approvals (dev + security)
```

**Review criteria:**

- ✅ Code is reusable
- ✅ Pattern is novel (not already in registry)
- ✅ No sensitive data
- ✅ Well documented
- ✅ Includes tests and examples

**If PASS:** Proceed to Phase 6  
**If FAIL:** Return to Phase 3 (sanitize more)

---

### Phase 6: Update Pattern Registry (.lumina)

**Location:** `.lumina/config/github_copilot_peak_patterns.json`

**Task:** Register the new pattern so Copilot can reference it

```json
{
  "pattern_name": "PortfolioAnalysis",
  "pattern_id": "portfolio_analysis_v1",
  "source": "Real-world portfolio management workflows",
  "description": "Analyze portfolio risk and efficiency",
  "implementations": [
    {
      "language": "python",
      "file": "scripts/python/portfolio_analyzer.py",
      "class": "PortfolioAnalyzer"
    }
  ],
  "use_cases": [
    "Portfolio evaluation",
    "Risk assessment",
    "Efficiency monitoring",
    "Backtesting"
  ],
  "token_multiplier": 0.8,
  "copilot_can_reference": true
}
```

---

### Phase 7: Push to GitHub (Public Only)

**Location:** GitHub public repo (or prepare for PR)

**Steps:**

```bash
# 1. Run final sanitization check
python scripts/python/pre_push_sanitization.py

# 2. Verify all files are in .lumina only
git diff --name-only origin/main | grep -v "^\.lumina/"
# Should return EMPTY (no private files)

# 3. Create release branch
git checkout -b release/lumina-v2.1

# 4. Commit with pattern reference
git add .lumina/scripts/python/portfolio_analyzer.py
git add .lumina/docs/patterns/portfolio_analysis.md
git add .lumina/config/github_copilot_peak_patterns.json
git commit -m "feat: Add PortfolioAnalysis pattern

- Generic portfolio risk/efficiency analyzer
- Extracted from real-world financial workflows
- Includes examples and comprehensive docs
- Refs: #42 (GitHub issue for pattern harvesting)"

# 5. Push to GitHub
git push origin release/lumina-v2.1

# 6. Create PR with template
```

---

### Phase 8: Backport Improvements (Optional)

**Location:** Back to `cfs-llc-env/` (v1.0 private)

**Task:** Optional - apply OSS improvements back to private

**If community contributes:** Updates to public `PortfolioAnalyzer`

- Security fixes? **Backport immediately**
- Performance improvements? **Consider backporting**
- Novel algorithm? **Use in next v1.1**

**If no community uptake:** Keep private version as-is

---

## Common Scenarios

### Scenario A: Bug Fix in Public Pattern

**Situation:** User finds bug in `.lumina/portfolio_analyzer.py`

**Process:**

1. Fix in public repo
2. Create patch
3. Apply patch to private version in `cfs-llc-env/`
4. Test in private
5. Deploy updated private version

### Scenario B: New Feature in Private

**Situation:** Company builds new trading risk model in `cfs-llc-env/`

**Process:**

1. Is it reusable? (Ask Phase 1 questions)
2. If YES → Extract to public per Phases 2-7
3. If NO → Keep private only
4. If MAYBE → Ask code review team

### Scenario C: Security Patch Needed

**Situation:** Security issue found in public pattern

**Process:**

1. Fix immediately in `.lumina/`
2. Create urgent release
3. Apply fix to private `cfs-llc-env/`
4. Run security audit on both
5. Deploy critical patch

---

## Automation & Tools

### Pre-Push Checker

```bash
# Before any GitHub push
python scripts/python/pre_push_sanitization.py

# Must return: ✅ PASSED
```

### Pattern Harvester (Planned)

```bash
# Auto-extract patterns from successful Copilot sessions
python scripts/python/harvest_patterns.py --lookback 7d --format peak_pattern
```

### Sync Validator (Planned)

```bash
# Validate private tree hasn't drifted from public
python scripts/python/validate_tree_sync.py --private cfs-llc-env --public .lumina
```

---

## Timeline

**Immediate (This Week):**

- ✅ Document this workflow
- ✅ Set up pre-push checker
- ✅ Train team on phases

**Short Term (This Month):**

- [ ] Extract 2-3 proven patterns to public
- [ ] Gather community feedback
- [ ] Refine pattern registry

**Medium Term (Q1 2026):**

- [ ] Automate pattern harvesting
- [ ] Set up CI/CD for releases
- [ ] Enable community contributions

---

## Troubleshooting

### Q: How do I know if something is reusable?

**A:** Ask:

1. Does it solve a generic problem?
2. Can it work with generic data?
3. Would others find it useful?
4. Can I explain it without company context?

If all YES → Likely reusable.

### Q: What if I extract something and find a leak later?

**A:** Immediately:

1. Create issue on GitHub (public)
2. Apply fix to `.lumina/`
3. Apply fix to `cfs-llc-env/`
4. Audit both trees
5. Contact GitHub security if critical

### Q: Can I extract confidential algorithms?

**A:** NO. Never extract:

- Trading algorithms
- Risk models using real data
- Customer analysis logic
- Proprietary scoring systems

Extract only: Generic frameworks, design patterns, educational concepts.

### Q: Who approves extractions?

**A:** Code review required from:

- 1 senior engineer (architecture)
- 1 security officer (no leaks)
- 1 business owner (IP cleared)

---

## Success Metrics

- ✅ 3+ patterns extracted to public per month
- ✅ 0 security leaks in `.lumina/`
- ✅ 90+ community feedback/issues per pattern
- ✅ 2+ backported improvements per quarter
- ✅ GitHub stars growing 25%+ YoY

---

**Document Status:** ✅ COMPLETE  
**Last Updated:** 2025-12-10  
**Owner:** Development Team Lead
