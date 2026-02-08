# Project Iron Curtain: Proactive Compusec Implementation Plan

**Code Name:** PROJECT IRON CURTAIN  
**Foundation:** Clawdbot/Moltbot Failure Analysis (Jan 2026)  
**Objective:** Immunize the Lumina ecosystem against viral AI project failure modes, identity hijacking, and unauthenticated public exposure.  
**Classification:** CRITICAL / LEVEL 5+

---

## 🛡️ 1. Identity & Rebranding Hardening (Handle-First Protocol)

The "10-second race condition" observed during the Clawdbot rebrand is now a primary threat vector.

### Actionable Implementation:
*   **Formal Policy:** Update `.cursorrules` and `identity_protection_rebranding.mdc` to mandate the "Handle-First" protocol.
*   **Procedure:** 
    1.  Secure target handles on GitHub, X, Discord, and relevant TLDs *before* initiating any rename.
    2.  Use account aliasing/redirection instead of deletion to prevent handle-squatting.
    3.  Verify handle ownership across all nodes in the cluster before announcing changes.

---

## 🧱 2. Network Perimeter & Service Binding Audit

Clawdbot's exposure was driven by unauthenticated gateways binding to `0.0.0.0`.

### Actionable Implementation:
*   **Black-Hole Port 18789:** Proactively block/black-hole port 18789 across all Lumina firewalls (pfSense, local host, and Docker) to prevent "copy-cat" Moltbot exposures.
*   **Loopback Enforcement Audit:** Create a Python utility (`scripts/python/audit_service_bindings.py`) to scan all running Lumina services. 
    *   **Rule:** Any internal-only gateway MUST bind to `127.0.0.1` or `::1` only.
    *   **Remote Access:** MUST be brokered via **Tailscale** or **Cloudflare Tunnel** with forced authentication.

---

## 🔑 3. Mandatory Authentication & Authorization (MAA)

Hundreds of Moltbot instances leaked API keys and PII due to zero-auth defaults.

### Actionable Implementation:
*   **JWT Everywhere:** Mandate JWT (JSON Web Token) validation for all cross-agent and cross-cluster communication (JARVIS ↔ ULTRON ↔ KAIJU).
*   **Zero-Trust Defaults:** All new Lumina services must initialize with a "Deny All" policy. Authentication must be explicitly configured before service startup.
*   **Token Isolation:** Rotate all HuggingFace and Anthropic tokens currently stored in `personaplex/.env` (remediating SECURITY-AUDIT-2026-01-27).

---

## 🧪 4. Proactive Security Testing (Red Teaming)

Clawdbot instances were compromised via 5-minute prompt injection to root shell.

### Actionable Implementation:
*   **Prompt Injection Suite:** Integrate `Giskard` or a custom Lumina-based "Prompt Jailbreak" test into the development cycle for all autonomous agents.
*   **Shodan/Censys Canary:** Implement a monthly cron job (`scripts/python/shodan_self_scan.py`) using Shodan/Censys APIs to search for our own IP space and identify any unauthenticated Lumina endpoints.

---

## 📦 5. Container & Host Hardening

Unauthenticated access to Moltbot containers frequently granted root access to the host machine.

### Actionable Implementation:
*   **Rootless Docker:** Enforce rootless containerization for all AI agent deployments.
*   **Read-Only Filesystems:** Mount application code directories as read-only within containers to prevent script injection and persistence.
*   **Capability Dropping:** Drop all non-essential Linux capabilities (e.g., `NET_RAW`, `SYS_ADMIN`) from Lumina container templates.

---

## 📈 Roadmap & Schedule

| Phase | Milestone | Target Date | Status |
| :--- | :--- | :--- | :--- |
| **Phase 1** | Port 18789 Black-hole & Service Audit | 2026-01-30 | ✅ Baseline Audit Complete |
| **Phase 2** | JWT Integration for Internal APIs | 2026-02-05 | ⏳ Pending |
| **Phase 3** | Rootless Docker Migration | 2026-02-15 | ⏳ Pending |
| **Phase 4** | Automated Shodan Canary Active | 2026-03-01 | ⏳ Pending |

---

## 📊 Baseline Audit Results (2026-01-29)

The initial `audit_service_bindings.py` run identified **48 unrestricted bindings**. 

### 🚨 Critical Review Items:
*   **Ollama (11434)**: Confirmed binding to `0.0.0.0`. While required for the cluster, this must be hardened via pfSense firewall rules to only allow `.11` and `.32` IPs.
*   **Management APIs (8998, 8080)**: Currently exposed to the local subnet. These should be moved to loopback-only and accessed via tunnel.
*   **OS Services (22, 3389)**: SSH and RDP are exposed. These require strictly enforced IP-allowlists on the router level.

### ✅ Pass:
*   **Port 18789**: Not found. Lumina is currently clean of the specific Clawdbot/Moltbot entry vector.

---

**Approval Required:** @LUMINA @USER  
**Prepared By:** JARVIS (via @SYPHON/RAPID Intelligence)
