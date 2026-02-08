# Data Classification Policy

**Effective Date:** December 10, 2025  
**Owner:** Security & Compliance Team  
**Audience:** All developers, DevOps, data handlers

---

## Purpose

Classify data into security/privacy tiers to ensure:

- 🔴 Confidential data never reaches public repos
- 🟢 Public frameworks are safe for GitHub
- 🟡 Internal tools are properly protected
- ✅ Compliance with regulations (GDPR, SOC 2, etc.)

---

## Classification Levels

### 🟢 PUBLIC

**Definition:** Safe to share publicly on GitHub

**Characteristics:**

- ✅ No personally identifiable information (PII)
- ✅ No credentials, API keys, secrets
- ✅ No company-specific logic
- ✅ No real customer data
- ✅ Generic frameworks & patterns
- ✅ Educational content
- ✅ Example configurations (with sample values)

**Examples:**

- `.lumina/scripts/python/ai_request_tracker.py` (generic framework)
- `.lumina/config/github_copilot_peak_patterns.json` (pattern templates)
- `.lumina/docs/ARCHITECTURE.md` (design documentation)
- `.lumina/examples/config_example.json` (example with dummy data)

**Storage:**

- `.lumina/` directory (root)
- GitHub public repository
- Community access allowed

**Retention:**

- Indefinite (public repos are forever)
- Versioning via GitHub releases

**Access Controls:**

- Public (anyone can read)
- Contributor review required for changes
- GitHub Actions CI/CD

**Handling Rules:**

- ✅ Can be pushed to public GitHub
- ✅ Can be shared in documentation
- ✅ Can be included in presentations
- ✅ Can be forked by community
- ❌ Cannot contain any real data
- ❌ Cannot reference real customers

---

### 🟡 INTERNAL

**Definition:** For internal use only, not public

**Characteristics:**

- ✅ Company-specific but not sensitive
- ✅ Design decisions, architecture
- ✅ Process documentation
- ❌ No PII or customer data
- ❌ No credentials
- ❌ Not production-critical secrets

**Examples:**

- Internal design documents
- Team workflows & processes
- Non-sensitive configuration notes
- Development roadmap (non-public)
- Meeting notes
- Architecture decisions

**Storage:**

- Private repositories or internal wiki
- NAS/shared drives with access controls
- Encrypted if at rest

**Retention:**

- As per company policy (typically 1-3 years)
- Archive older versions

**Access Controls:**

- Team/company only
- Role-based access (RBAC)
- Audit logging recommended

**Handling Rules:**

- ❌ Cannot push to public GitHub
- ✅ Can discuss in team meetings
- ✅ Can share with team members
- ❌ Cannot share externally
- ✅ Can be backed up to NAS

---

### 🔴 CONFIDENTIAL

**Definition:** Highly sensitive data - company proprietary & regulated

**Characteristics:**

- ❌ Real customer data, PII
- ❌ Real credentials, API keys, tokens
- ❌ Proprietary algorithms & IP
- ❌ Financial data, trading logic
- ❌ Production secrets
- ❌ Competitive information

**Examples:**

- `cedarbrook-*/cedarbrook_financial_services/` (real operations)
- `cedarbrook-*/data/customer_records/` (PII)
- `cedarbrook-*/configs/api_keys.json` (credentials)
- Real trading models, market data
- Actual customer portfolios
- Production database credentials

**Storage:**

- Private company repositories
- Encrypted local storage
- NAS with strict access controls
- Never in public cloud without encryption

**Retention:**

- Per compliance requirements (GDPR: 7 years, etc.)
- Secure deletion when no longer needed
- Audit trail maintained

**Access Controls:**

- Restricted to authorized personnel only
- Multi-factor authentication (MFA) required
- Role-based access (RBAC)
- Audit logging mandatory
- Encryption at rest & in transit

**Handling Rules:**

- 🔴 **NEVER** push to GitHub (public or private)
- 🔴 **NEVER** include in code samples
- 🔴 **NEVER** screenshot or share externally
- 🔴 **NEVER** commit to .lumina tree
- ✅ Can be accessed by authorized team
- ✅ Can be backed up securely
- ✅ Requires approval for any cross-team access

---

### 🔒 RESTRICTED (subset of CONFIDENTIAL)

**Definition:** Most sensitive - regulatory, legal, or security-critical

**Characteristics:**

- 🔒 Highly regulated (HIPAA, PCI-DSS, etc.)
- 🔒 Legal or licensing information
- 🔒 Security vulnerabilities (before patches)
- 🔒 Executive strategy & plans
- 🔒 Negotiation details

**Examples:**

- Patient data (if applicable)
- Credit card data (PCI-DSS)
- Legal contracts, NDAs
- Zero-day security vulnerabilities
- CEO strategy memos

**Storage:**

- Encrypted vaults only (1Password, HashiCorp Vault)
- Air-gapped systems recommended
- Limited local copies

**Access Controls:**

- Need-to-know basis strictly enforced
- Approval from security officer required
- Separate audit logs (immutable)
- Time-limited access tokens

**Handling Rules:**

- 🔒 Requires explicit approval to access
- 🔒 Cannot be copied or duplicated
- 🔒 Must be deleted after use
- 🔒 Discussed in secure channels only
- 🔒 Breaches reported immediately

---

## How to Classify Data

### Decision Tree

```
Start
  ↓
Does it contain real customer/personal data?
  ├─ YES → CONFIDENTIAL (🔴)
  └─ NO  ↓
     Does it contain credentials, API keys, or secrets?
       ├─ YES → CONFIDENTIAL (🔴)
       └─ NO  ↓
          Does it contain company-specific business logic?
            ├─ YES (proprietary) → CONFIDENTIAL (🔴)
            ├─ YES (internal tool) → INTERNAL (🟡)
            └─ NO  ↓
               Is it generic framework or pattern?
                 ├─ YES → PUBLIC (🟢)
                 └─ NO  → INTERNAL (🟡)
```

### Examples

| Data | Classification | Reason |
|------|---|---|
| `ai_request_tracker.py` (generic) | 🟢 PUBLIC | Generic framework, no company data |
| `customer_records.csv` | 🔴 CONFIDENTIAL | Real customer PII |
| `api_keys.json` | 🔴 CONFIDENTIAL | Credentials |
| Trading algorithm (real) | 🔴 CONFIDENTIAL | Proprietary IP |
| Portfolio analyzer (generic) | 🟢 PUBLIC | Generic pattern, no real data |
| Team meeting notes | 🟡 INTERNAL | Company-specific, not sensitive |
| Performance monitor (real) | 🔴 CONFIDENTIAL | Real customer data inside |
| System architecture diagram | 🟢 PUBLIC | Generic design |
| Zero-day vulnerability | 🔒 RESTRICTED | Before patch released |

---

## Handling by Classification

### PUBLIC Data (🟢)

**Collection:**

- No special controls needed

**Storage:**

- `.lumina/` directory (Git tracked)
- GitHub public repository

**Transmission:**

- Email OK (no encryption needed)
- Public discussions OK
- Any public channel OK

**Retention:**

- Keep indefinitely (GitHub history)

**Deletion:**

- Never delete (public history is forever)
- If needed: Create new repo, NEVER overwrite history

**Audit:**

- GitHub commit history (public)
- No special audit needed

---

### INTERNAL Data (🟡)

**Collection:**

- Minimize collection to business needs
- Approval from manager

**Storage:**

- Private repositories
- Internal wiki/documentation
- NAS with folder-level access control

**Transmission:**

- Encrypted email (TLS) or internal messaging
- Not on public channels

**Retention:**

- Typically 1-3 years
- Per company retention policy

**Deletion:**

- Secure deletion from all systems
- Audit log of deletion

**Audit:**

- Access logs maintained
- Change tracking (Git/wiki history)

---

### CONFIDENTIAL Data (🔴)

**Collection:**

- Minimize collection
- Explicit approval from security officer
- Signed data handling agreement

**Storage:**

- Encrypted at rest
- Private company systems only
- NAS with strict RBAC
- Never in `.lumina/`
- Never in public GitHub

**Transmission:**

- Encrypted email (PGP) or secure messaging
- VPN required for remote access
- Never screenshots or copy-paste
- Audit log of every transmission

**Retention:**

- Comply with regulations (GDPR: 7 years)
- Retention policy documented

**Deletion:**

- Crypto-erase (not just deletion)
- Audit log of destruction
- Certificate of destruction

**Audit:**

- Complete access log (who, when, what)
- Change log
- Export/download log
- Breach detection systems

---

### RESTRICTED Data (🔒)

**Collection:**

- VP/Director approval required
- Legal review often needed
- Purpose statement required

**Storage:**

- Encrypted vaults only (1Password, Vault)
- Air-gapped systems
- Limited copies (preferably 1)

**Transmission:**

- Executive/secure channels only
- In-person when possible
- Encrypted with PGP, signed

**Retention:**

- Legal/regulatory requirements
- Often longer (7+ years)
- Regular review for continued need

**Deletion:**

- Requires approval from legal
- Crypto-erase
- Written destruction log

**Audit:**

- Immutable audit log
- Time-synchronized records
- Quarterly access reviews
- Breach triggers immediate incident response

---

## Compliance Frameworks

### GDPR (European Data)

- **Class:** 🔴 CONFIDENTIAL / 🔒 RESTRICTED
- **Right to be forgotten:** Must delete within 30 days
- **Data transfers:** Must be encrypted & justified
- **Breach notification:** 72 hours required
- **Storage:** Cannot store in non-EU without compliance

### PCI-DSS (Payment Card Data)

- **Class:** 🔒 RESTRICTED
- **Encryption:** Required for storage & transmission
- **Access:** Role-based, need-to-know only
- **Audit:** Quarterly security audits, annual penetration testing
- **Retention:** Minimal - delete after purpose served

### HIPAA (Health Data - if applicable)

- **Class:** 🔒 RESTRICTED
- **Encryption:** Required (AES-256 minimum)
- **Audit trails:** Complete & immutable
- **Access logs:** Every access logged
- **Breach:** Notification within 60 days

### SOC 2 (System & Organization Controls)

- **Classification:** Enforced across all levels
- **Audit trails:** Required for all data
- **Access controls:** Documented & reviewed
- **Retention policies:** Documented
- **Annual audit:** Third-party validation

---

## Practical Checklist

### Before Publishing Code

- [ ] No real customer/company data in examples
- [ ] No hardcoded API keys or credentials
- [ ] No internal URLs or endpoints
- [ ] No proprietary algorithm details
- [ ] Run `pre_push_sanitization.py` - PASS
- [ ] Code review by security team - APPROVED
- [ ] All configs are templates with `_example` or sample values
- [ ] Documentation doesn't reveal sensitive patterns

### Before Sharing Data

- [ ] Classified correctly (PUBLIC/INTERNAL/CONFIDENTIAL/RESTRICTED)
- [ ] Encryption enabled if CONFIDENTIAL/RESTRICTED
- [ ] Recipients have need-to-know
- [ ] Purpose clearly stated
- [ ] Audit log entry created
- [ ] Recipient acknowledges data handling policy

### Before Storing Data

- [ ] Encryption enabled if not PUBLIC
- [ ] Access controls configured (RBAC)
- [ ] Retention policy defined
- [ ] Backup/recovery plan in place
- [ ] Audit logging enabled (if not PUBLIC)
- [ ] DLP (Data Loss Prevention) configured

---

## Violations & Incidents

### Incident Reporting

If you accidentally expose confidential data:

1. **Immediately:**
   - Stop the action (delete, revoke, etc.)
   - Notify security officer
   - Do NOT cover it up

2. **Within 1 hour:**
   - Document what happened
   - Assess impact (how much data, how many people)
   - Begin containment

3. **Within 24 hours:**
   - Notify affected parties (if required)
   - Legal review
   - Incident report filed
   - Corrective actions

4. **Ongoing:**
   - Monitor for misuse
   - Update security controls
   - Conduct post-mortem
   - Share lessons learned

### Consequences

- **First violation:** Written warning + retraining
- **Second violation:** Disciplinary action + suspension of access
- **Intentional breach:** Termination + potential legal action

---

## Questions?

Contact: security@[domain] or your manager

**Remember:** When in doubt, classify HIGHER (more restrictive). It's easier to declassify later than to deal with a breach.

---

**Document Status:** ✅ COMPLETE  
**Last Updated:** 2025-12-10  
**Next Review:** 2026-06-10
