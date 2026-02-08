# SSH Key Security Audit & Infosec Recommendations
**Request ID:** 2a1be10b-ab14-450e-a0cd-9092d107310e  
**Date:** 2026-01-02  
**Auditor:** LUMINA Infosec Engineering Team  
**Tags:** #INFOSEC #DROIDS #SSH #AUTHENTICATION

## Executive Summary

This document provides an information security engineering perspective on the SSH key authentication implementation for NAS access in the LUMINA project.

### Current Implementation Status
✅ **SSH Key Authentication:** Implemented and functional  
⚠️ **Security Posture:** Good, but requires hardening  
🔴 **Critical Issues:** 2 identified  
🟡 **Medium Issues:** 3 identified  
🟢 **Low Issues:** 2 identified

---

## Security Assessment

### ✅ Strengths

1. **Key Type Selection**
   - Using `ed25519` keys (modern, secure, fast)
   - Stronger than RSA-2048, smaller key size
   - Recommended by NIST and security best practices

2. **Key Storage**
   - Keys stored in `~/.ssh/` directory (standard location)
   - Proper directory permissions (700)
   - Private key not exposed in code

3. **Authentication Flow**
   - Key-first authentication (faster, more secure)
   - Password fallback for resilience
   - No hardcoded credentials

4. **Connection Security**
   - Using Paramiko (reliable SSH library)
   - Proper timeout handling
   - Disabled agent/key lookup to prevent failed attempts

### 🔴 Critical Security Issues

#### Issue 1: Private Key File Permissions
**Severity:** HIGH  
**Risk:** Unauthorized key access could lead to NAS compromise

**Current State:**
- Private key permissions not explicitly set to 600
- Windows file system may not enforce Unix permissions correctly

**Recommendation:**
```python
# In setup_ssh_keys_for_nas.py, after key generation:
private_key_path.chmod(0o600)  # rw------- (owner read/write only)
```

**Fix Required:** ✅ YES

#### Issue 2: Password Fallback Without Rate Limiting
**Severity:** HIGH  
**Risk:** Brute force attacks if key is compromised

**Current State:**
- Password fallback is always available
- No rate limiting on failed authentication attempts
- No alerting on password fallback usage

**Recommendation:**
- Log all password fallback events
- Alert on password fallback usage (should be rare)
- Consider disabling password auth after key is verified working
- Implement rate limiting on NAS SSH server

**Fix Required:** ✅ YES

### 🟡 Medium Security Issues

#### Issue 3: No Key Rotation Policy
**Severity:** MEDIUM  
**Risk:** Long-lived keys increase exposure window

**Current State:**
- No automatic key rotation
- No expiration dates on keys
- No key rotation documentation

**Recommendation:**
- Implement 90-day key rotation policy
- Add key expiration metadata
- Create automated rotation script
- Document rotation procedures

**Fix Required:** ⚠️ RECOMMENDED

#### Issue 4: No Key Usage Auditing
**Severity:** MEDIUM  
**Risk:** Cannot detect unauthorized key usage

**Current State:**
- No logging of key-based connections
- No audit trail of SSH access
- No monitoring of key usage patterns

**Recommendation:**
- Enable SSH connection logging on NAS
- Log all SSH connections (success and failure)
- Monitor for unusual access patterns
- Integrate with security monitoring system

**Fix Required:** ⚠️ RECOMMENDED

#### Issue 5: AutoAddPolicy for Host Keys
**Severity:** MEDIUM  
**Risk:** Man-in-the-middle attacks

**Current State:**
```python
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```

**Recommendation:**
- Use `RejectPolicy` in production
- Maintain known_hosts file
- Verify host keys on first connection
- Use host key pinning

**Fix Required:** ⚠️ RECOMMENDED

### 🟢 Low Security Issues

#### Issue 6: No Key Encryption at Rest
**Severity:** LOW  
**Risk:** Key theft if system is compromised

**Current State:**
- Private key stored unencrypted on disk
- Relies on file system permissions

**Recommendation:**
- Consider encrypting private key with passphrase
- Use OS-level encryption (BitLocker/FileVault)
- Store key in secure keychain/credential store

**Fix Required:** ℹ️ OPTIONAL

#### Issue 7: No Multi-Factor Authentication
**Severity:** LOW  
**Risk:** Single factor authentication

**Current State:**
- Only SSH key authentication (single factor)
- No 2FA/MFA requirement

**Recommendation:**
- Consider SSH certificate-based authentication
- Implement MFA for sensitive operations
- Use SSH key + password (two factors)

**Fix Required:** ℹ️ OPTIONAL

---

## DROIDS Integration Recommendations

### For @DROIDS Security Team

1. **Key Lifecycle Management**
   - Integrate SSH key rotation into DROIDS workflow
   - Add key expiration alerts
   - Automate key rotation via DROIDS

2. **Security Monitoring**
   - Feed SSH connection logs to DROIDS monitoring
   - Alert on password fallback usage
   - Track key usage patterns

3. **Compliance**
   - Document SSH key policy in security handbook
   - Add SSH key management to security checklist
   - Include in security audits

---

## Implementation Fixes

### Fix 1: Secure Key Permissions
**Priority:** CRITICAL  
**File:** `setup_ssh_keys_for_nas.py`

```python
# After key generation, ensure secure permissions
if sys.platform != 'win32':
    private_key_path.chmod(0o600)  # rw------- on Unix
else:
    # Windows: Use icacls or similar
    import stat
    os.chmod(private_key_path, stat.S_IREAD | stat.S_IWRITE)
```

### Fix 2: Password Fallback Logging
**Priority:** CRITICAL  
**File:** `ssh_connection_helper.py`

```python
import logging
logger = logging.getLogger("SSHConnection")

# In connect_to_nas(), when falling back to password:
if password:
    logger.warning(f"SSH key auth failed for {username}@{nas_ip}, using password fallback")
    # Alert security team
```

### Fix 3: Host Key Verification
**Priority:** MEDIUM  
**File:** `ssh_connection_helper.py`

```python
from paramiko import RejectPolicy

# Use known_hosts file
known_hosts = Path.home() / ".ssh" / "known_hosts"
if known_hosts.exists():
    ssh.load_host_keys(str(known_hosts))
    ssh.set_missing_host_key_policy(RejectPolicy())
else:
    # First connection: verify and save
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Save host key after first successful connection
```

---

## Security Best Practices Checklist

- [x] Use strong key type (ed25519)
- [x] Store keys in secure location (~/.ssh)
- [ ] Set proper file permissions (600)
- [ ] Implement key rotation policy
- [ ] Enable connection logging
- [ ] Use host key verification
- [ ] Log password fallback events
- [ ] Document key management procedures
- [ ] Integrate with security monitoring
- [ ] Regular security audits

---

## Compliance Notes

### NIST 800-53 Compliance
- **AC-3:** Access Enforcement ✅ (Key-based access)
- **AC-7:** Unsuccessful Logon Attempts ⚠️ (Needs rate limiting)
- **AC-17:** Remote Access ✅ (SSH key authentication)
- **IA-5:** Authenticator Management ⚠️ (Needs rotation policy)

### CIS Benchmarks
- **5.2.1:** Ensure SSH key-based authentication ✅
- **5.2.2:** Ensure SSH password authentication is disabled ⚠️ (Currently enabled as fallback)
- **5.2.3:** Ensure SSH host key verification ⚠️ (Using AutoAddPolicy)

---

## Recommendations Summary

### Immediate Actions (This Week)
1. ✅ Fix private key file permissions
2. ✅ Add password fallback logging
3. ✅ Document key management procedures

### Short-Term Actions (This Month)
1. ⚠️ Implement host key verification
2. ⚠️ Enable SSH connection logging on NAS
3. ⚠️ Create key rotation script

### Long-Term Actions (This Quarter)
1. ℹ️ Implement automated key rotation
2. ℹ️ Integrate with DROIDS security monitoring
3. ℹ️ Consider MFA for sensitive operations

---

## Conclusion

The SSH key implementation is **functionally sound** but requires **security hardening** to meet enterprise infosec standards. The critical issues should be addressed immediately, while medium and low priority items can be scheduled for future sprints.

**Overall Security Rating:** 🟡 **GOOD** (with fixes) → 🟢 **EXCELLENT** (after all recommendations)

---

**Next Steps:**
1. Review and approve this audit
2. Prioritize fixes based on risk assessment
3. Implement critical fixes (Fix 1 & 2)
4. Schedule medium-priority improvements
5. Integrate with @DROIDS security monitoring

**Audit Completed By:** LUMINA Infosec Engineering Team  
**Review Required By:** @INFOSEC @DROIDS
