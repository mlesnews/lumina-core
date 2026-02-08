# LDAP Domain Join - Quick Reference Card

**Date**: 2026-01-02  
**Status**: ✅ **READY TO EXECUTE**

---

## ✅ Pre-Flight Check

Certificates verified and ready:
- ✅ Certificate: `/tmp/ldap_certificates/client.crt`
- ✅ Private Key: `/tmp/ldap_certificates/client.key`
- ✅ Both files exist and are readable on NAS

---

## 🚀 Quick Start (5 Steps)

### Step 1: RDP to MANUS
```powershell
mstsc /v:10.17.17.11
```

### Step 2: Open DSM
```
https://10.17.17.32:5001
```

### Step 3: Navigate
```
Control Panel → Domain/LDAP → Join
```

### Step 4: Configure
- **Profile Type**: **Custom** ✅ **SELECT THIS**
  - ❌ **NOT "Standard"** (for Synology LDAP only)
  - ❌ **NOT "IBM Lotus Domino"** (for IBM servers only)
  - ❌ **NOT "Open Directory"** (for Mac only)
- **Domain**: Your Azure AD domain
- **Port**: `636` (LDAPS)
- **SSL/TLS**: ✅ Enabled
- **Certificate**: Browse to `C:\Users\mlesn\Desktop\ldap_client.crt`
- **Private Key**: Browse to `C:\Users\mlesn\Desktop\ldap_client.key`

### Step 5: Join
- Click **"Test Connection"** first
- If successful, click **"Apply"** or **"Join"**

---

## 📋 Certificate Paths (Browse in DSM)

**On Your Desktop:**
```
Certificate: C:\Users\mlesn\Desktop\ldap_client.crt
Private Key: C:\Users\mlesn\Desktop\ldap_client.key
```

**Note**: In DSM, click "Browse" and navigate to your Desktop folder, then select these files.

---

## ⚠️ Troubleshooting

**Connection Failed?**
- Verify port 636 (LDAPS)
- Check firewall rules
- Test DNS resolution

**Authentication Failed?**
- Verify certificate paths are correct
- Try password-based auth as fallback
- Check Azure AD credentials

**Base DN Not Found?**
- Format: `DC=domain,DC=com`
- Retrieve from Azure AD configuration

---

## ✅ Verification

After joining, verify:
```powershell
python scripts/python/verify_sso_readiness.py --vault-name jarvis-lumina --nas-ip 10.17.17.32
```

Expected: ✅ SSO READY

---

**Estimated Time**: 15-30 minutes  
**Difficulty**: Medium  
**Full Guide**: `docs/system/LDAP_DOMAIN_JOIN_GUIDE.md`
