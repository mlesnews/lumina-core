# Lumina Multi-Distribution Architecture

**Date:** 2026-01-27
**Version:** 1.0.0
**Status:** ✅ ACTIVE
**Classification:** PUBLIC (Architecture Strategy)

---

## Executive Summary

This document defines the comprehensive multi-distribution architecture for the Lumina project. The Lumina ecosystem is structured into four distinct distributions that share a unified foundation (`lumina_core`) while maintaining clear separation between open-source, premium SaaS, proprietary company, and mobile variants.

### Distribution Overview

| Distribution | Location | License | Audience | Purpose |
|-------------|----------|---------|----------|---------|
| **lumina-oss** | `.lumina/` | MIT | GitHub community | Open-source foundation |
| **lumina-premium** | `vscode-extensions/lumina-premium/` | PROPRIETARY | Paid subscribers | Premium SaaS features |
| **lumina-ce** | `cedarbrook-financial-services-env/` | PROPRIETARY | Cedarbrook CFS LLC | Company operations |
| **lumina-mobile** | `mobile-app/` | PROPRIETARY | Mobile users | Remote monitoring & control |

---

## Architecture Principles

### 1. Unified Foundation
All distributions share `lumina_core` as the common foundation:
- Core Jarvis integration manager
- Extension bridge patterns
- Attribution engine
- Capability router

### 2. Fork Strategy Compliance
- **PUBLIC (.lumina/)**: Generic frameworks, MIT licensed, no secrets
- **PRIVATE (cedarbrook-*/mobile/)**: Business logic, proprietary data, secured
- **Unidirectional Sync**: Private → Public (sanitized extraction)

### 3. Distribution Tiers

```
┌─────────────────────────────────────────────────────────────────┐
│                    LUMINA ECOSYSTEM                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              LUMINA_CORE (Shared Foundation)             │    │
│  │  ┌─────────────┐ ┌─────────────┐ ┌───────────────────┐  │    │
│  │  │ Integration │ │ Attribution │ │ Capability Router │  │    │
│  │  │   Manager   │ │   Engine    │ │                   │  │    │
│  │  └─────────────┘ └─────────────┘ └───────────────────┘  │    │
│  └─────────────────────────────────────────────────────────┘    │
│           │                    │                    │            │
│           ▼                    ▼                    ▼            │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐      │
│  │lumina-oss   │      │lumina-premium      │lumina-ce    │      │
│  │(MIT License)│      │(SaaS Subscription) │(Proprietary)│      │
│  └─────────────┘      └─────────────┘      └─────────────┘      │
│                                                                 │
│           │                    │                    │            │
│           └────────────────────┼────────────────────┘            │
│                                ▼                                 │
│                    ┌─────────────────────┐                       │
│                    │    LUMINA MOBILE    │                       │
│                    │  (Remote Admin)     │                       │
│                    └─────────────────────┘                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Distribution Details

### 1. lumina-oss (Open Source Distribution)

**Location:** `.lumina/`
**License:** MIT
**Repository:** GitHub public repo

#### Features
- GitHub/GitLens integration
- Local enterprise Git configuration
- NAS cloud services (generic patterns)
- Storage provider configurations
- TODO status tracking (@MASTER/@PADAWAN)
- Unified queue viewer
- Footer ticker
- File auto-close (generic)
- Voice controls (pattern only)

#### Constraints
- ✅ No API keys or secrets
- ✅ No company names (Cedarbrook, CFS LLC)
- ✅ No real customer data
- ✅ Generic example configurations only
- ✅ MIT license required

#### Package Structure
```
.lumina/
├── vscode-extensions/
│   ├── lumina-core/          # Main open-source extension
│   ├── cursor-active-model-status/
│   ├── cursor-voice-controls/
│   ├── file-auto-close/
│   ├── lumina-footer-ticker/
│   └── lumina-unified-queue/
├── lumina_core/
│   └── jarvis/
│       └── extensions/
│           └── integration_manager.py
├── config/
├── scripts/
├── docs/
└── README.md
```

---

### 2. lumina-premium (SaaS Add-On Pack)

**Location:** `vscode-extensions/lumina-premium/`
**License:** PROPRIETARY
**Distribution:** Private VSIX, not on marketplace

#### Features
- **Advanced Progress Tracking:** Enhanced airport signboard style
- **Premium Integrations:** Exclusive API connectors
- **Enhanced Attribution:** Extended attribution engine
- **Priority Support:** SLA-backed support features
- **Custom Branding:** White-label options
- **Analytics Dashboard:** Usage analytics and insights
- **License Management:** Subscription validation

#### Tier Differentiation

| Feature | OSS | Premium |
|---------|-----|---------|
| Basic Extensions | ✅ | ✅ |
| Progress Indicator | Basic | Advanced |
| Attribution Engine | Standard | Extended |
| Analytics | ❌ | ✅ |
| Priority Queue | ❌ | ✅ |
| Custom Branding | ❌ | ✅ |
| SLA Support | ❌ | ✅ |

#### Package Structure
```
vscode-extensions/lumina-premium/
├── package.json              # PROPRIETARY license, private: true
├── extension.js              # Main extension entry
├── premium/
│   ├── license_manager.js    # Subscription validation
│   ├── analytics.js          # Usage analytics
│   ├── advanced_progress.js  # Enhanced progress indicator
│   └── premium_integrations.js
└── README.md                 # Private documentation
```

---

### 3. lumina-ce (Cedarbrook Enterprise)

**Location:** `cedarbrook-financial-services-env/`
**License:** PROPRIETARY
**Access:** Internal only

#### Features
- **Financial Services Integration:** Bloomberg, proprietary trading APIs
- **Customer Analytics:** Real customer data processing
- **Portfolio Management:** Investment portfolio tracking
- **Risk Assessment:** Proprietary risk models
- **Performance Monitoring:** Real-time performance dashboards
- **Compliance Tools:** Regulatory compliance features
- **Audit Logging:** Comprehensive audit trails

#### Security Requirements
- 🔐 All secrets in Azure Key Vault
- 🔐 No hardcoded credentials
- 🔐 Encrypted data at rest
- 🔐 Role-based access control
- 🔐 Audit logging required

#### Package Structure
```
cedarbrook-financial-services-env/
├── .lumina/                  # Nested Lumina structure
├── cedarbrook_financial_services/
│   ├── performance_monitor.py
│   ├── trading_models.py
│   ├── customer_analytics.py
│   └── risk_assessment.py
├── data/
│   ├── customer_records/     # PII - encrypted
│   ├── transactions/         # Financial data - encrypted
│   └── market_feeds/         # Proprietary feeds
├── configs/
│   ├── api_keys.json         # Azure Key Vault references
│   ├── database_creds.json   # Encrypted connections
│   └── internal_apis.json    # Internal API configs
├── secrets/
│   └── .gitkeep             # Placeholder - real secrets in Key Vault
├── docs/
│   └── INTERNAL_OPERATIONS.md
└── README.md                 # Confidential - Internal only
```

---

### 4. lumina-mobile (Remote Administration)

**Location:** `mobile-app/`
**License:** PROPRIETARY
**Platform:** Cross-platform (iOS/Android)

#### @PEAK Remote Administration Features

The `@PEAK` system provides comprehensive remote administration and monitoring capabilities:

##### 9 Life Domains Monitored

1. **💰 Financial Domain**
   - Income/expense tracking
   - Investment portfolio value
   - Budget adherence
   - Credit score monitoring

2. **🏠 Physical Environment Domain**
   - Home automation status
   - Security system monitoring
   - Energy consumption
   - Space organization score

3. **🧠 Intellectual Domain**
   - Learning hours logged
   - Knowledge acquisition rate
   - Skill development progress
   - Curiosity engagement

4. **💪 Physical Health Domain**
   - Exercise frequency
   - Sleep quality metrics
   - Nutrition tracking
   - Vital signs monitoring

5. **❤️ Social/Relationship Domain**
   - Relationship quality scores
   - Communication frequency
   - Social interaction hours
   - Community engagement

6. **🎯 Career/Purpose Domain**
   - Professional goal progress
   - Skill alignment score
   - Contribution impact
   - Legacy building metrics

7. **🌱 Personal Growth Domain**
   - Self-awareness score
   - Habit completion rate
   - Challenge acceptance
   - Transformation progress

8. **🎨 Creative Domain**
   - Creative output frequency
   - Artistic expression score
   - Innovation metrics
   - Aesthetic engagement

9. **⚡ Energy/Exergy Domain**
   - Overall vitality score
   - Energy distribution
   - Restoration efficiency
   - Peak performance windows

#### Mobile App Architecture

```
mobile-app/
├── src/
│   ├── main/
│   │   ├── java/com/lumina/mobile/
│   │   │   ├── MainActivity.kt
│   │   │   ├── LuminaApplication.kt
│   │   │   └── core/
│   │   │       ├── PeakAdminManager.kt
│   │   │       ├── LifeDomainMonitor.kt
│   │   │       ├── RemoteCommandHandler.kt
│   │   │       └── SecureCommunication.kt
│   │   └── res/
│   │       ├── layout/
│   │       ├── values/
│   │       └── drawable/
│   ├── test/
│   └── androidTest/
├── lib/
│   ├── peak_core/           # @PEAK system core
│   ├── domain_monitor/      # Life domain monitoring
│   ├── remote_admin/        # Remote administration
│   └── secure_channel/      # Encrypted communication
├── config/
│   └── firebase.json        # Push notifications
└── README.md                # Internal documentation
```

#### @PEAK Features

**Remote Administration Capabilities:**
- Real-time system status monitoring
- Agent task management
- Configuration updates
- Emergency shutdown
- Performance tuning
- Access revocation

**Dashboard Widgets:**
- Overall @PEAK score (0-100)
- Domain-by-domain breakdown
- Trend analysis
- Goal tracking
- Alert notifications

---

## Integration Points

### Extension Dependencies

```
lumina-oss (MIT)
    │
    ├──▶ lumina-core (depends on)
    │       ├── GitHub Copilot
    │       ├── GitLens
    │       └── lumina_core framework
    │
    └──▶ lumina-premium (optional)
            ├── Requires lumina-core
            ├── License key validation
            └── Subscription check

lumina-premium (SaaS)
    │
    ├──▶ lumina-core (required)
    │       └── Provides base functionality
    │
    └──▶ Azure Key Vault (secrets)
            └── License validation

lumina-ce (Enterprise)
    │
    ├──▶ lumina-core (required)
    │       └── Extended with financial features
    │
    ├──▶ Azure Key Vault (required)
    │       └── All secrets management
    │
    └──▶ Proprietary APIs
            └── Bloomberg, internal systems

lumina-mobile (Remote)
    │
    ├──▶ lumina-core (remote client)
    │       └── Connects via secure channel
    │
    ├──▶ @PEAK System
    │       └── Life domain monitoring
    │
    └──▶ Firebase Cloud Messaging
            └── Push notifications
```

### Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA FLOW DIAGRAM                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐                                                   │
│  │   User      │                                                   │
│  └──────┬──────┘                                                   │
│         │                                                          │
│         ▼                                                          │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────────┐   │
│  │ IDE Plugin  │────▶│ lumina_core │────▶│ Remote Services     │   │
│  │ (OSS/Premium)│     │   Framework │     │ (Azure, APIs)       │   │
│  └─────────────┘     └──────┬──────┘     └─────────────────────┘   │
│                             │                                      │
│         ┌───────────────────┼───────────────────┐                  │
│         ▼                   ▼                   ▼                  │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐          │
│  │ Analytics   │     │ Attribution │     │ Mobile App  │          │
│  │ (Premium)   │     │ Engine      │     │ (Remote)    │          │
│  └─────────────┘     └─────────────┘     └─────────────┘          │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    CEDARBROOK ENTERPRISE                    │   │
│  │  ┌───────────┐  ┌───────────┐  ┌─────────────────────────┐  │   │
│  │  │ Financial │  │ Customer  │  │ Compliance & Audit      │  │   │
│  │  │ Services  │  │ Analytics │  │                         │  │   │
│  │  └───────────┘  └───────────┘  └─────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Security Architecture

### Secrets Management Hierarchy

| Priority | Storage | Use Case |
|----------|---------|----------|
| 1 | Azure Key Vault | Production secrets, API keys |
| 2 | ProtonPass CLI | Development secrets |
| 3 | Environment Variables | Runtime configuration |
| 4 | Encrypted Config Files | Backup storage |

### Access Control Matrix

| Component | OSS | Premium | CE | Mobile |
|-----------|-----|---------|-----|--------|
| Core Framework | ✅ | ✅ | ✅ | ✅ |
| Attribution Engine | ✅ | ✅ | ✅ | ✅ |
| License Management | ❌ | ✅ | ✅ | ✅ |
| Financial APIs | ❌ | ❌ | ✅ | ❌ |
| Customer Data | ❌ | ❌ | ✅ | View-only |
| @PEAK Admin | ❌ | ❌ | ✅ | ✅ |
| Audit Logs | ❌ | ✅ | ✅ | ✅ |

### Security Checklist

- [ ] No API keys in source code
- [ ] No passwords in source code
- [ ] No connection strings in source code
- [ ] All secrets use Azure Key Vault
- [ ] No secrets in comments
- [ ] Regular security audits
- [ ] Compliance verification

---

## Deployment Strategy

### Build Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT PIPELINE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐                                                │
│  │ Source Code │                                                │
│  └──────┬──────┘                                                │
│         │                                                       │
│         ▼                                                       │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────────┐   │
│  │   Build     │────▶│   Test      │────▶│   Security Scan │   │
│  │  (TypeScript│     │  (Unit/Int) │     │  (Secrets Audit)│   │
│  │   Python)   │     │             │     │                 │   │
│  └─────────────┘     └─────────────┘     └─────────────────┘   │
│         │                  │                     │              │
│         │                  ▼                     ▼              │
│         │           ┌─────────────┐     ┌─────────────┐        │
│         │           │  Linter     │     │  Fail if    │        │
│         │           │  (Zero Err) │     │  Secrets    │        │
│         │           └─────────────┘     └─────────────┘        │
│         │                  │                     │              │
│         └──────────────────┼─────────────────────┘              │
│                            ▼                                    │
│                  ┌─────────────────┐                            │
│                  │   Fork Check    │                            │
│                  │ (Public/Private)│                            │
│                  └────────┬────────┘                            │
│                           │                                     │
│         ┌─────────────────┼─────────────────┐                   │
│         ▼                 ▼                 ▼                   │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐           │
│  │  lumina-oss │   │lumina-premium│  │  lumina-ce  │           │
│  │  (GitHub)   │   │ (SaaS Dist) │   │ (Enterprise)│           │
│  └─────────────┘   └─────────────┘   └─────────────┘           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Distribution Artifacts

| Distribution | Artifact | Location | Deployment |
|-------------|----------|----------|------------|
| lumina-oss | VSIX | `vscode-extensions/lumina-complete/` | GitHub Releases |
| lumina-premium | VSIX | `vscode-extensions/lumina-premium/` | Private Distribution |
| lumina-ce | Python | `cedarbrook-financial-services-env/` | Internal Servers |
| lumina-mobile | APK/AAB | `mobile-app/dist/` | App Stores (Enterprise) |

---

## Version Management

### Version Scheme

```
MAJOR.MINOR.PATCH[-DISTRIBUTION]

Examples:
- 3.0.0        = OSS version
- 3.0.0-premium = Premium add-on version
- 3.0.0-ce     = Cedarbrook Enterprise version
- 3.0.0-mobile = Mobile app version
```

### Compatibility Matrix

| lumina-core | lumina-premium | lumina-ce | lumina-mobile |
|-------------|----------------|-----------|---------------|
| 3.0.0 | 1.0.0+ | 1.0.0+ | 1.0.0+ |
| 2.x.x | 1.x.x+ | 1.x.x+ | 1.x.x+ |

---

## Documentation Requirements

### Required Documentation

| Document | Distribution | Location |
|----------|-------------|----------|
| README.md | All | Root of each distribution |
| API_REFERENCE.md | Premium, CE | Distribution root |
| DEPLOYMENT_GUIDE.md | CE, Mobile | Distribution root |
| SECURITY.md | All | docs/ |
| LICENSE | All | Distribution root |
| CHANGELOG.md | All | Distribution root |
| CONTRIBUTING.md | OSS | .lumina/ root |

---

## Quick Start

### For OSS Users
```bash
# Clone the public repository
git clone https://github.com/mlesnews/lumina-ai.git
cd lumina

# Install VSIX extension
cursor --install-extension vscode-extensions/lumina-complete/lumina-core-3.0.0.vsix
```

### For Premium Subscribers
```bash
# Obtain private VSIX from distribution channel
# Install with license key
cursor --install-extension vscode-extensions/lumina-premium/lumina-premium-1.0.0.vsix

# Configure license
# (Settings > Lumina Premium > License Key)
```

### For Cedarbrook Employees
```bash
# Access internal repository
git clone git@internal.cedarbrook.cfs:lumina-enterprise.git
cd cedarbrook-financial-services-env

# Set up Azure Key Vault access
az login
az keyvault secret download --vault-name jarvis-lumina --name api-key --file config/api_keys.json

# Run enterprise services
python -m cedarbrook_financial_services.main
```

### For Mobile Users
```bash
# Download from enterprise app store
# Install APK/AAB
# Connect to @PEAK admin interface
# Configure remote monitoring domains
```

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| `docs/system/PUBLIC_PRIVATE_FORK_STRATEGY.md` | Fork architecture |
| `.kilocode/rules/secrets.md` | Secrets management |
| `.kilocode/rules/due_diligence_quality_standards.md` | Quality standards |
| `.kilocode/rules/fork_strategy_review.md` | Fork compliance |
| `docs/SECURITY_AUDIT_REPORT_2026-01-27.md` | Security compliance |

---

## Summary

The Lumina multi-distribution architecture provides:

| Benefit | Description |
|---------|-------------|
| **Clear Separation** | Public vs private vs enterprise vs mobile |
| **Shared Foundation** | lumina_core reduces duplication |
| **Fork Compliance** | Unidirectional sync with sanitization |
| **Security First** | Azure Key Vault for all secrets |
| **Scalability** | Tiered distribution model |
| **Remote Administration** | @PEAK system for mobile control |

**Document Version:** 1.0.0
**Last Updated:** 2026-01-27
**Maintained By:** @JARVIS @LUMINA
