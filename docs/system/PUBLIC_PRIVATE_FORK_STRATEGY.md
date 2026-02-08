# Public/Private Fork Strategy

## `.lumina` (Public GitHub) vs. `cedarbrook-*` (Private Company)

**Date Created:** December 10, 2025  
**Context:** Post-PC-Reset (OEM Bare Metal Windows 11 Pro - "Matt" Workstation)  
**Strategy:** Dual-tree architecture for open-source public repo + private company operations

---

## Overview: Two Distinct Trees

This project intentionally forks into **two independent but synchronized trees**:

### Tree 1: **PUBLIC GITHUB** 🌐

**Primary Location:** `.lumina/` (root)  
**Purpose:** Open-source community project  
**Audience:** GitHub public, OSS contributors, technical community  
**Content:** Generic frameworks, patterns, algorithms, educational materials  
**Data:** Sanitized, company-agnostic, example configs only  
**License:** MIT / Apache 2.0 (OSS)  
**Sync Direction:** Public ← Private (upstream extraction)

### Tree 2: **PRIVATE COMPANY** 🏢

**Primary Locations:**

- `cedarbrook-financial-services_llc-env/` (v0.1 - Original)
- `cedarbrook-financial-services_llc-env_portable/` (v0.2 - Portable)
- `cfs-llc-env/` (v1.0 - Optimized)

**Purpose:** Cedarbrook Financial Services LLC - actual business operations  
**Audience:** Internal team, partners, C-suite  
**Content:** Business logic, company workflows, financial models, proprietary algorithms  
**Data:** Real customer data, financial records, confidential IP  
**License:** Private / Proprietary  
**Sync Direction:** Private → Public (sanitized extraction)

---

## The Dual-Tree Architecture

```
my_projects/ (MASTER ROOT)
│
├── .lumina/ (v2.0 - PUBLIC GITHUB TREE)
│   ├── config/
│   │   ├── ai_token_request_tracker.json    (Generic - PUBLIC)
│   │   └── github_copilot_peak_patterns.json (Generic - PUBLIC)
│   ├── scripts/python/
│   │   ├── ai_request_tracker.py             (Generic framework - PUBLIC)
│   │   ├── abacus_todolist_sync.py           (Generic learner - PUBLIC)
│   │   └── holistic_todo_manager.py          (Generic tool - PUBLIC)
│   ├── docs/
│   │   ├── PROJECT_EVOLUTION_MANIFEST.md     (PUBLIC: Evolution story)
│   │   ├── AGENT_CHAT_HISTORIES_TOKEN_TRACKING.md (PUBLIC: Framework)
│   │   └── PUBLIC_PRIVATE_FORK_STRATEGY.md  (PUBLIC: This doc - transparency)
│   └── .CANONICAL                            (PUBLIC: Marker)
│
├── cedarbrook-financial-services_llc-env/ (v0.1 - PRIVATE COMPANY TREE)
│   ├── .lumina/ (Nested v0.1 config)
│   ├── cedarbrook_financial_services/       (PRIVATE: Real business)
│   │   ├── performance_monitor.py           (PRIVATE: ML models)
│   │   ├── customer_analysis.py             (PRIVATE: Actual data)
│   │   ├── financial_models.py              (PRIVATE: Trading logic)
│   │   └── proprietary_algorithms/          (PRIVATE: IP)
│   ├── data/
│   │   ├── customer_records/                (PRIVATE: PII, confidential)
│   │   ├── market_data/                     (PRIVATE: Proprietary feeds)
│   │   └── financial_transactions/          (PRIVATE: Real money)
│   ├── configs/
│   │   ├── api_keys.json                    (PRIVATE: Secrets)
│   │   ├── database_creds.json              (PRIVATE: Access)
│   │   └── internal_settings.json           (PRIVATE: Company IP)
│   └── .LEGACY                               (PRIVATE: Archive marker)
│
├── cedarbrook-financial-services_llc-env_portable/ (v0.2 - PRIVATE COMPANY TREE)
│   └── [Similar structure to v0.1]
│
└── cfs-llc-env/ (v1.0 - PRIVATE COMPANY TREE)
    └── [Similar structure with optimization phase]
```

---

## Content Classification & Sync Direction

### What Goes PUBLIC? (.lumina → GitHub)

**ALLOWED TO PUBLIC:**

1. **Generic Frameworks & Patterns**
   - AI token tracking architecture (generic)
   - Master/Padawan learner system (generic algorithm)
   - Rearview/lookback logic patterns
   - GitHub Copilot workflow templates
   - Peak patterns (conceptual, not company-specific)

2. **Educational Materials**
   - Architecture evolution documentation
   - System design decisions & rationale
   - Design patterns & best practices
   - ML/AI learning concepts
   - Open-source integrations

3. **Tools & Utilities (Sanitized)**
   - Generic TODO manager
   - Task classification algorithms
   - Learning progress trackers
   - Token budget frameworks
   - Holistic context integration patterns

4. **Configuration Templates (Examples)**
   - `.json` template structures (no real values)
   - Configuration schema documentation
   - Settings organization patterns
   - MCP integration examples

5. **Process Documentation**
   - Development workflows
   - Version evolution rationale
   - Migration guides
   - Architecture diagrams

**FORBIDDEN FROM PUBLIC:**

- 🔴 Customer data / PII
- 🔴 Financial records / transactions
- 🔴 API keys / secrets / credentials
- 🔴 Database connection strings
- 🔴 Proprietary algorithms
- 🔴 Real market data feeds
- 🔴 Trading logic / financial models
- 🔴 Competitor analysis
- 🔴 Pricing strategies
- 🔴 Internal metrics / financial performance

### What Stays PRIVATE? (cedarbrook-* trees)

**ALWAYS PRIVATE:**

1. **Business Logic**
   - Financial models & calculations
   - Trading algorithms
   - Risk assessment systems
   - Portfolio optimization
   - Market prediction models

2. **Data Assets**
   - Customer information (PII)
   - Real transactions
   - Market data feeds (proprietary)
   - Historical performance data
   - Deal records

3. **Sensitive Configurations**
   - API keys / authentication tokens
   - Database credentials
   - Third-party integrations (keys)
   - Internal deployment configs
   - Feature flags with business logic

4. **Company IP**
   - Proprietary algorithms
   - Competitive advantages
   - Strategic plans
   - Internal processes (if sensitive)
   - Partner agreements

---

## Sync Strategy: UNIDIRECTIONAL (Private → Public)

```
PRIVATE TREES (cedarbrook-*)           PUBLIC TREE (.lumina)
─────────────────────────────          ─────────────────────────
Business Implementation  ─────────────> Open-Source Framework
Real company operations                Generic patterns & concepts
Proprietary algorithms                 Sanitized, reusable tools
Customer/financial data                Educational documentation
Sensitive configs/IP                   Example templates & guides
                             (Extraction & Sanitization)
```

### Sync Workflow

```
1. DEVELOP IN PRIVATE
   └─ Build real features in cedarbrook-* trees
   └─ Implement business logic
   └─ Test with real data

2. EXTRACT GENERIC PATTERNS
   └─ Identify reusable frameworks
   └─ Strip company-specific logic
   └─ Remove sensitive data
   └─ Create generic templates

3. SANITIZE FOR PUBLIC
   └─ Replace real configs with examples
   └─ Remove hardcoded values
   └─ Add documentation
   └─ Create non-identifying examples

4. PUSH TO PUBLIC (.lumina)
   └─ Add to open-source version
   └─ Document design decisions
   └─ Share with GitHub community
   └─ Accept community feedback

5. INCORPORATE FEEDBACK
   └─ Apply OSS improvements to public
   └─ Backport useful changes to private (optional)
   └─ Evolve open-source version
   └─ Keep dual-tree benefits
```

---

## Practical Examples

### Example 1: Master/Padawan Learner System

**PRIVATE TREE (cedarbrook-cfs-llc-env):**

```python
# Private: Real company token costs & learning impact
class CompanyLearner:
    def log_teaching_interaction(self, agent, topic, effectiveness):
        """
        Track when senior staff (Master) teach junior staff (Padawan)
        Real context: Sales team training, risk officer mentorship
        Token cost: 0.5x multiplier (teaching is efficient for company)
        """
        cost = effectiveness * 0.5  # Company saves tokens on teaching
        self.company_budget.deduct(cost)
        self.record_learning_effectiveness(agent, effectiveness)
```

**PUBLIC TREE (.lumina):**

```python
# Public: Generic learner pattern for OSS users
class Learner:
    def log_learning_interaction(self, role, session_type, effectiveness):
        """
        Generic Master/Padawan learning pattern.
        
        Parameters:
            role: 'master' (teacher) or 'padawan' (learner)
            session_type: 'teaching', 'learning', 'practice', 'validation'
            effectiveness: 0.0-1.0 learning outcome
        
        Token multipliers:
            master (teaching): 0.5x
            padawan (learning): 1.0x
            pattern_harvest: 0.3x
            validation: 0.2x
        """
        multiplier = self.get_multiplier(role, session_type)
        effective_tokens = effectiveness * multiplier
        self.record_interaction(role, session_type, effective_tokens)
```

---

### Example 2: Token Tracking

**PRIVATE TREE:**

```json
{
  "agent_name": "Matt_CFO_AI",
  "company": "Cedarbrook Financial Services LLC",
  "real_budget": {
    "github_copilot": 500000,
    "azure_ai": 1000000,
    "internal_llm": "unlimited"
  },
  "cost_per_token": 0.000002,  // Actual company rates
  "sensitive_integrations": {
    "bloomberg_api": "prod-key-xyz",
    "proprietary_model_endpoint": "https://internal.company.com/models"
  }
}
```

**PUBLIC TREE:**

```json
{
  "agent_name": "example_agent",
  "budget": {
    "github_copilot": 100000,
    "azure_ai": 200000
  },
  "cost_per_token": 0.0000015,  // Example rate
  "example_integrations": {
    "github_copilot": "example-pattern",
    "open_source_model": "huggingface-reference"
  }
}
```

---

### Example 3: Performance Monitoring

**PRIVATE TREE:**

```python
# Real company performance metrics
class CFOPerformanceMonitor:
    def analyze_trading_performance(self):
        """Analyze actual trading results, P&L, risk metrics"""
        roi = self.calculate_real_roi()  # Real company returns
        risk_score = self.assess_portfolio_risk()  # Real exposure
        efficiency = self.calc_cost_efficiency()  # Real margins
```

**PUBLIC TREE:**

```python
# Generic educational ML anomaly detection
class AnomalyDetector:
    def detect_performance_patterns(self, time_series):
        """Detect anomalies in any time-series data using ML"""
        # Generic Q-learning approach
        # Example: learning progress, system metrics, budget trends
```

---

## Workspace Management: Preventing Accidental Edits

### Problem: "Nesting Logic Issue"

**What Happened (Pre-v2.0):**

```
cedarbrook-financial-services_llc-env/          ← PRIVATE
├── .lumina/                                     ← (nested in private!)
│   ├── config/
│   └── scripts/
└── [PRIVATE company code]

User Intent: Edit .lumina public version
Actual Action: Edited .lumina INSIDE cedarbrook (private tree!)
Result: Public repo contaminated with private data 😱
```

**Solution: Separate Root Trees**

```
my_projects/                                     ← Master root
├── .lumina/                                     ← PUBLIC (v2.0)
│   ├── config/
│   └── scripts/
│
├── cedarbrook-financial-services_llc-env/       ← PRIVATE (v0.1)
│   ├── cedarbrook_financial_services/
│   └── data/
│
└── [other private trees...]
```

### Enforcement: Workspace Boundary Rules

**`.editorconfig` (root):**

```ini
# Mark canonical public workspace
[.lumina/**]
root = true
insert_final_newline = true
charset = utf-8
# Add public headers
# Enable strict mode checks

# Mark legacy/private workspaces
[cedarbrook-*/**]
# Warning: Private tree - sanitize before GitHub push
# Add private headers: "CONFIDENTIAL - DO NOT PUBLIC"
```

**VS Code / Cursor Workspace Config:**

```json
{
  "folders": [
    {
      "path": ".lumina",
      "name": "PUBLIC: GitHub Open-Source (v2.0)",
      "color": "green",
      "description": "Edit here for public GitHub repo"
    },
    {
      "path": "cedarbrook-financial-services_llc-env",
      "name": "PRIVATE: Company v0.1 (Legacy)",
      "color": "red",
      "description": "⚠️ CONFIDENTIAL - Do NOT sync to GitHub"
    },
    {
      "path": "cfs-llc-env",
      "name": "PRIVATE: Company v1.0 (Active)",
      "color": "red",
      "description": "⚠️ CONFIDENTIAL - Do NOT sync to GitHub"
    }
  ],
  "settings": {
    "workbench.explorer.sortOrder": "mixed",
    "files.exclude": {
      "cedarbrook-*": false,
      ".lumina": false
    },
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": "explicit"
    }
  },
  "launch": {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "RUN: PUBLIC Tests (.lumina)",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/.lumina/tests/run_tests.py"
      },
      {
        "name": "RUN: PRIVATE Company Operations",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/cfs-llc-env/scripts/run_operations.py"
      }
    ]
  }
}
```

**File Headers (Automation):**

```python
# .lumina/scripts/example.py
"""
PUBLIC: Open-Source Framework Module
Location: .lumina/scripts/example.py
License: MIT / Apache 2.0
Safe for: GitHub public repository
"""

# cedarbrook-financial-services_llc-env/scripts/private.py
"""
⚠️ CONFIDENTIAL: Private Company Operations
Location: cedarbrook-financial-services_llc-env/scripts/private.py
Access: Internal Only
DO NOT: Sync to GitHub or public repositories
"""
```

---

## GitHub Repository Structure

### Public GitHub Repo: `.lumina` Tree

```
github.com/your-username/lumina

lumina/
├── README.md                                  (Generic project)
├── LICENSE                                    (MIT)
├── config/
│   ├── ai_token_request_tracker.json         (Example template)
│   └── github_copilot_peak_patterns.json     (Generic patterns)
├── scripts/python/
│   ├── ai_request_tracker.py                 (Reusable framework)
│   ├── learner_system.py                     (Generic Master/Padawan)
│   └── holistic_todo_manager.py              (Generic tool)
├── docs/
│   ├── ARCHITECTURE.md                       (Design decisions)
│   ├── PUBLIC_PRIVATE_FORK_STRATEGY.md      (This transparency doc)
│   ├── GETTING_STARTED.md                    (Tutorial)
│   └── CONTRIBUTING.md                       (OSS guidelines)
├── examples/
│   ├── config_example.json                   (Sample config)
│   └── learning_example.py                   (Sample usage)
└── tests/
    ├── test_learner.py
    └── test_token_tracker.py
```

### Private Repository: Company Trees

```
private-repo: cedarbrook-financial-services-operations

cedarbrook-operations/
├── cedarbrook-financial-services_llc-env/    (v0.1 archive)
├── cfs-llc-env/                              (v1.0 active)
│   ├── cedarbrook_financial_services/
│   │   ├── performance_monitor.py            (Real monitoring)
│   │   ├── trading_models.py                 (Real trading)
│   │   └── customer_analytics.py             (Real customer data)
│   ├── data/
│   │   ├── customer_records/
│   │   ├── transactions/
│   │   └── market_feeds/
│   ├── configs/
│   │   ├── api_keys.json
│   │   ├── database_creds.json
│   │   └── internal_apis.json
│   └── secrets/
│       └── [encrypted credentials]
└── docs/
    └── INTERNAL_OPERATIONS.md
```

---

## Sync Workflow: Private → Public

### Scenario: New Feature Developed in Private

**Step 1: Develop in Private (cedarbrook-*):**

```python
# cfs-llc-env/cedarbrook_financial_services/new_feature.py

def analyze_customer_portfolio(customer_id):
    """PRIVATE: Real company feature - analyze specific customer"""
    customer = db.get_customer(customer_id)  # Real data
    portfolio = fetch_real_portfolio(customer)  # Real positions
    risk = calculate_real_risk(portfolio)  # Real metrics
    return customer_analysis_report(portfolio, risk)
```

**Step 2: Extract Generic Pattern:**

```python
# Extract: What's reusable? "Portfolio analysis pattern"
def analyze_portfolio(portfolio_data):
    """Generic algorithm: analyze any portfolio structure"""
    risk_score = calculate_risk(portfolio_data)
    efficiency = calculate_efficiency(portfolio_data)
    return {risk: risk_score, efficiency: efficiency}
```

**Step 3: Create Public Version (Sanitized):**

```python
# .lumina/scripts/portfolio_analyzer.py
"""
PUBLIC: Generic Portfolio Analysis Framework
Example usage with anonymized data
"""

def analyze_portfolio_example(sample_portfolio):
    """
    Analyze portfolio structure (generic example)
    
    Args:
        sample_portfolio: Dict with 'holdings', 'weights', 'sectors'
    
    Returns:
        Dict with risk_score and efficiency metrics
    """
    risk = compute_risk_metric(sample_portfolio)
    efficiency = compute_efficiency_metric(sample_portfolio)
    return {"risk": risk, "efficiency": efficiency}
```

**Step 4: Document Design:**

```markdown
# .lumina/docs/PORTFOLIO_ANALYSIS.md

## Design Pattern: Portfolio Analysis

This pattern emerged from real-world portfolio management needs.

### Key Concepts:
- Risk calculation methods
- Efficiency metrics
- Time-series optimization

### Generic Usage:
[Example code with sample data]

### Real-World Application:
[General description without sensitive details]
```

---

## Preventing Data Leaks: Pre-Push Checklist

**Before pushing any changes to public `.lumina` repo:**

```bash
# 1. SCAN for private content
grep -r "cedarbrook\|cfs_\|customer_\|api_key\|secret\|PII\|confidential" .lumina/

# 2. CHECK for hardcoded values
grep -r ":[0-9]\{4,\}" .lumina/  # Credit cards, SSNs, etc.

# 3. VERIFY no config files
find .lumina -name "*.env" -o -name "*creds*" -o -name "*keys*"

# 4. SCAN for sensitive keywords
grep -i -r "trading\|roi\|customer\|proprietary\|internal\|confidential" .lumina/docs/

# 5. VERIFY all examples are sanitized
cat .lumina/config/*.json | grep -v "example\|sample\|template"

# 6. CHECK git history
git log --all --full-history --oneline | grep -i "secret\|key\|customer"

# 7. FINAL APPROVAL
echo "Ready for public push? (y/n)"
```

---

## Architecture Benefits

### For Public Community (.lumina)

✅ **Clean, maintainable open-source**

- No company data or secrets
- Reusable frameworks & patterns
- Educational value
- Community contributions
- Transparent development

✅ **Professional presence**

- Builds credibility
- Attracts talent & partners
- Showcases engineering practices
- Differentiates company

✅ **Business advantage**

- OSS projects build brand
- Attract community improvements
- Potential enterprise adoption
- Talent recruitment

### For Private Operations (cedarbrook-*)

✅ **Business continuity**

- Real proprietary algorithms
- Actual company data protected
- Competitive advantage maintained
- Regulatory compliance

✅ **Operational flexibility**

- Develop confidentially
- Experiment safely
- Real financial operations secure
- Customer data protected

✅ **Knowledge leverage**

- Extract learnings to public
- Get community feedback
- Backport improvements
- Evolve faster

---

## Implementation Checklist

### Immediate (This Week)

- [ ] Document public/private split in team wiki
- [ ] Set up `.editorconfig` with warnings for private trees
- [ ] Configure VS Code/Cursor workspace with color-coded folders
- [ ] Create file header templates (PUBLIC vs. CONFIDENTIAL)
- [ ] Add `.CANONICAL` marker to `.lumina` (✅ DONE)
- [ ] Add `.LEGACY` markers to private trees (✅ DONE)

### Short Term (This Month)

- [ ] Create GitHub public repo from `.lumina` tree
- [ ] Set up automated pre-push sanitization checks
- [ ] Document sync workflow (private → public)
- [ ] Create CONTRIBUTING.md for public repo
- [ ] Set up CI/CD for public releases
- [ ] Establish data classification policy

### Medium Term (Q1 2026)

- [ ] Automate sanitization pipeline
- [ ] Create public project roadmap
- [ ] Establish community governance
- [ ] Build OSS contributor guide
- [ ] Set up license compliance scanning
- [ ] Create public release process

### Long Term (2026+)

- [ ] Grow public community
- [ ] Accept community contributions
- [ ] Backport improvements to private
- [ ] Publish whitepapers / case studies
- [ ] Consider dual-licensing strategy
- [ ] Plan v3.0 evolution

---

## Summary

| Aspect | PUBLIC (.lumina) | PRIVATE (cedarbrook-*) |
|--------|------------------|------------------------|
| **Location** | `.lumina/` (root) | `cedarbrook-*-env/` trees |
| **Audience** | GitHub community, OSS | Internal team, partners |
| **Content** | Generic frameworks, patterns | Business logic, real data |
| **Data** | Example templates only | Real customer/financial data |
| **Secrets** | None | API keys, credentials, configs |
| **License** | MIT/Apache 2.0 | Proprietary |
| **GitHub** | Public repository | Never synced |
| **Sync Flow** | Private ← (extraction) → Public | Unidirectional (extraction) |
| **Edit Rules** | ✅ Active development | ⚠️ Reference only (legacy) |
| **Safety** | Safe to share | Confidential always |

---

## WOPR Operations: Coordinating the Fork

**For balanced development across both trees, use WOPR (War Operation Plan Response):**

See [WOPR_DUAL_TREE_BALANCE.md](./WOPR_DUAL_TREE_BALANCE.md) for complete strategy.

### Quick WOPR Commands

```bash
# Daily sync validation
python scripts/python/wopr_ops.py --daily-ops

# Monitor both trees
python scripts/python/wopr_monitoring.py --status

# Generate operational dashboard
python scripts/python/wopr_status_report.py --print
```

### Key WOPR Capabilities

- ✅ **Monitor** development activity in both trees
- ✅ **Coordinate** pattern extraction with checkpoints
- ✅ **Validate** code quality & security across both
- ✅ **Synchronize** shared base code (single source of truth)
- ✅ **Track** pending extractions & backports
- ✅ **Report** divergence, sync health, metrics

### WOPR Extraction Workflow

1. **Identify** code in private tree marked for extraction
2. **Extract** generic pattern (strip company-specific logic)
3. **Validate** reusability on generic data
4. **Sanitize** (pre-push scan for leaks)
5. **Review** extraction quality & compliance
6. **Commit** to public tree with proper documentation
7. **Backport** improvements (optional) back to private

**WOPR validates every step, blocking extractions that fail security or quality checks.**

---

---

**Document Status:** ✅ COMPLETE  
**Last Updated:** 2025-12-10  
**Classification:** Public Strategy (safe to share in GitHub README)
