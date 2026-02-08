# CompuSec Security Engineering Team

## Team Structure

The CompuSec Security Engineering Team consists of three AI security agents working in a layered defense model with cross-checking responsibilities.

### @MARVIN - Internal Security Lead
- **Primary Domain:** Internal security threats
  - Secret/credential leak detection
  - Internal data exposure
  - Configuration security
  - Code security scanning
  - Insider threat patterns
- **Secondary Role:** Cross-check for @HK-47 external findings

### @HK-47 - External Security Lead
- **Primary Domain:** External security threats
  - Perimeter defense
  - External API security
  - Network intrusion detection
  - External attack vectors
  - Threat intelligence
- **Secondary Role:** Cross-check for @MARVIN internal findings

### @WOPR - Threat Simulation & Validation
- **Primary Domain:** War games and threat modeling
  - Attack simulation
  - Threat scenario modeling
  - Security posture validation
  - Red team exercises
- **Secondary Role:** Validate findings from both MARVIN and HK-47

## Cross-Check Protocol

```
┌─────────────────────────────────────────────────────┐
│                  Security Event                      │
└─────────────────────────────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            ▼                         ▼
    ┌──────────────┐          ┌──────────────┐
    │   @MARVIN    │◄────────►│   @HK-47     │
    │  (Internal)  │  Cross   │  (External)  │
    └──────────────┘  Check   └──────────────┘
            │                         │
            └────────────┬────────────┘
                         ▼
                  ┌──────────────┐
                  │    @WOPR     │
                  │ (Validation) │
                  └──────────────┘
```

## Incident SEC-2026-0108-001 Post-Mortem

**What happened:** Secret (ProtonPass extra password) was exposed in terminal output.

**Who should have caught it:**
1. **@MARVIN (Primary):** Internal secret leak - FAILED TO DETECT
2. **@HK-47 (Cross-Check):** Should have flagged command construction with secrets - FAILED TO DETECT
3. **@WOPR:** Not invoked for this operation

**Root Cause:**
- Neither MARVIN nor HK-47 had pre-execution command scanning
- Cross-check protocol not implemented for shell command construction

**Remediation Required:**
- [ ] MARVIN: Add pre-execution shell command scanning for secrets
- [ ] HK-47: Add cross-check hook for MARVIN's internal operations
- [ ] WOPR: Add threat scenario for "AI accidentally exposes secrets"
- [ ] Implement mutual notification when either agent detects anomalies

## Reporting Chain

```
CompuSec Team → @RR (Risk & Compliance) → The Professor
```

All security incidents must be reported through this chain.

---

*Document created after SEC-2026-0108-001 incident*
*Owner: @RR (Risk & Compliance)*
