# Helpdesk Ticket: Homelab DNS Services Not Responding - pfSense and NAS

**Ticket ID**: HELPDESK-20260116-DNS-HOMELAB  
**Priority**: 🔴 **HIGH**  
**Status**: ✅ **RESOLVED** (closed 2026-01-16)  
**Category**: NETWORK / DNS  
**Created**: 2026-01-16T15:16:40.165014  
**Resolved**: 2026-01-16T15:17:10.521606  
**Assigned Team**: NETWORK_TEAM  
**Tags**: #DNS, #HOMELAB, #PFSENSE, #NAS, #NETWORK, @JARVIS, @HELPDESK

---

## ✅ Resolution Summary

**Resolved**: 2026-01-16T15:17:10.521606  
**Verification**: DNS resolution verified — both pfSense and NAS DNS responding correctly to queries after upstream DNS servers were configured. Auto-closed on workflow monitor success.

The companion `HELPDESK-20260116-DNS-HOMELAB.json` ticket file in this directory has been the authoritative status record (status=RESOLVED) since the close-out timestamp above. This markdown file is now updated to match. Public-mirror sync was lagging — see `00-MIRROR-SYNC-LOG.md`.

---

## 📋 Issue Summary

Both pfSense (10.17.17.1) and NAS (10.17.17.32) DNS services are not responding to queries. DNS port 53 is open but queries timeout.

**Impact**: 
- Browser cannot resolve DNS when using Wi-Fi adapter (configured to use pfSense DNS)
- IPv4 sites appear down in browser
- Blocks browser automation workflows
- Prevents Fidelity credential extraction automation

**Affected Systems**:
- pfSense (10.17.17.1) - Primary DNS
- NAS (10.17.17.32) - Secondary DNS
- Wi-Fi Network Adapter (using pfSense DNS)
- Browser automation (Neo browser)

---

## 🔍 Diagnostic Findings

- **Connectivity**: ✅ Both servers reachable (ping works)
- **DNS Port**: ✅ Port 53 UDP open on both servers
- **DNS Queries**: ❌ All DNS queries timing out
- **Root Cause**: DNS service running but not configured with upstream DNS servers

**Working DNS Servers**:
- ProtonVPN DNS (10.2.0.1) - Working
- Google DNS (8.8.8.8) - Working

---

## 🔧 Resolution Steps

### pfSense (10.17.17.1)
1. Access pfSense Web UI: https://10.17.17.1
2. Navigate to: Services > DNS Resolver (or DNS Forwarder)
3. Enable DNS service
4. Configure upstream DNS servers:
   - 8.8.8.8 (Google)
   - 1.1.1.1 (Cloudflare)
   - 8.8.4.4 (Google secondary)
5. Enable 'Enable Forwarding Mode' if using DNS Forwarder
6. Save and apply changes
7. Restart DNS service if needed

### NAS (10.17.17.32)
1. Access NAS Web UI: https://10.17.17.32:5001
2. Navigate to: Control Panel > Network > DNS Server
3. Enable DNS service
4. Configure upstream DNS servers (same as pfSense)
5. Save and apply changes
6. Restart DNS service if needed

### Verification
- Run: nslookup google.com 10.17.17.1
- Run: nslookup google.com 10.17.17.32
- Run: python scripts/python/verify_homelab_dns_fix.py
- Test browser connectivity
- Retry Fidelity automation workflow

---

## 📊 Workflow Monitoring

**Status**: ✅ Enabled  
**Check Interval**: 300 seconds  
**Verification Script**: `scripts/python/verify_homelab_dns_fix.py`

**Success Criteria**:
- **pfsense_dns**: All test queries successful
- **nas_dns**: All test queries successful
- **browser_connectivity**: Sites load correctly

**Auto-Close on Resolution**: ✅ Yes

---

## 📎 Related Files

- `docs/diagnostics/COMPREHENSIVE_SYSTEM_DIAGNOSTIC_REPORT.md`
- `docs/diagnostics/DNS_VS_REVERSE_DNS_EXPLAINED.md`
- `scripts/python/fix_homelab_dns_services.py`
- `scripts/python/verify_homelab_dns_fix.py`

---

**Ticket Created By**: JARVIS Helpdesk System  
**Workflow**: @DOIT Autonomous Execution  
**Tags**: #DNS, #HOMELAB, #PFSENSE, #NAS, #NETWORK, @JARVIS, @HELPDESK
