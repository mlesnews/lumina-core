# Compliance Rules: DNS Split & Migration Stability (+rule)

**Initiative**: #INITIATIVE (CR000003001)
**Governance**: Risk & Compliance (@rc/@rskcmp)
**Status**: 🔴 **ENFORCED**

---

## 📋 Operational Rules

### 1. DNS Consistency Rule
- **Rule**: Every Forward DNS change (A record) MUST be accompanied by a corresponding Reverse DNS (PTR) record.
- **Verification**: `NASDNSManager.ensure_dns_consistency()` must return `consistent: true`.
- **Penalty**: Non-compliant changes will be rolled back by @MARVIN.

### 2. Migration Bandwidth Throttling
- **Rule**: Background migration IOPS must not exceed 30% of available interface bandwidth during operational hours (08:00 - 20:00).
- **Metric**: Threshold = 200 Mbps (on 650 Mbps link).
- **Enforcement**: @manus will throttle robocopy tasks if OpenAI `ECONNRESET` rate exceeds 5% in 15 minutes.

### 3. Quorum Secret Verification
- **Rule**: All administrative credentials used for infrastructure changes must pass a 2/3 Triad Quorum check.
- **Failover**: Manual (Dashlane) tier is only permitted if Primary (Azure) and Secondary (Proton) are both confirmed offline.

---

## 🏛️ Audit Trail
- **Date**: 2026-01-08
- **Approved By**: @JARVIS (Acting CTO)
- **Supervised By**: @C-3PO (Protocol)
- **Monitored By**: @MARVIN (Security Engineering)
