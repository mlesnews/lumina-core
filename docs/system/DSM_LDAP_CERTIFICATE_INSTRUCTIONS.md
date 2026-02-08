# DSM LDAP Certificate Instructions

**Date**: 2026-01-02  
**Status**: ✅ Configuration Ready | ⚠️ Certificate Fields Optional

---

## When DSM Asks for Certificate Location

### If DSM prompts for "Client Certificate" and "Private Key":

**OPTION 1: Skip Certificates (Recommended for Azure AD)**
- Leave both fields **EMPTY**
- Click **Next** or **Apply**
- DSM will use basic username/password authentication
- This works for most Azure AD LDAP configurations

**OPTION 2: Use Certificates (If Required)**
If DSM requires certificates and won't proceed without them:

1. **Get Certificates Ready:**
   ```powershell
   # If you have certificate files:
   python scripts/python/configure_ldap_certificates_rdp.py `
       --cert-file "C:\path\to\client.crt" `
       --key-file "C:\path\to\client.key"
   ```

2. **Certificates will be saved to NAS at:**
   - Certificate: `/tmp/ldap_certificates/client.crt`
   - Private Key: `/tmp/ldap_certificates/client.key`

3. **In DSM, enter these paths:**
   - Certificate file: `/tmp/ldap_certificates/client.crt`
   - Private key file: `/tmp/ldap_certificates/client.key`

---

## Quick Decision Guide

**Use this if DSM asks for certificates:**

```
┌─────────────────────────────────────────────────┐
│  Is DSM requiring certificates (won't proceed)?  │
└─────────────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
       YES                     NO
        │                       │
        │              ┌────────┴────────┐
        │              │ Leave fields     │
        │              │ EMPTY and click  │
        │              │ Next/Apply       │
        │              └──────────────────┘
        │
        ▼
┌───────────────────────┐
│ Get certificates from │
│ Azure AD or Key Vault │
└───────────────────────┘
        │
        ▼
┌───────────────────────┐
│ Run certificate script │
│ to save to NAS         │
└───────────────────────┘
        │
        ▼
┌───────────────────────┐
│ Enter paths in DSM:   │
│ /tmp/ldap_certificates/│
│ client.crt            │
│ client.key            │
└───────────────────────┘
```

---

## Certificate Sources

### From Azure AD
1. Azure Portal → Azure Active Directory
2. App registrations → Your app
3. Certificates & secrets
4. Export certificate and private key

### From Azure Key Vault
```powershell
# Add to Key Vault first:
az keyvault secret set --vault-name jarvis-lumina --name ldap-client-certificate --file "cert.pem"
az keyvault secret set --vault-name jarvis-lumina --name ldap-client-private-key --file "key.pem"

# Then run:
python scripts/python/configure_ldap_certificates_rdp.py
```

---

## Current Status

✅ **SSH Connection**: Fixed (password-only auth)  
✅ **Azure Key Vault**: Verified and accessible  
✅ **LDAP Configuration**: Ready (certificates optional)  
⚠️ **Certificates**: Not in Key Vault (usually not needed)

---

**Recommendation**: Try leaving certificate fields empty first. Most Azure AD LDAP configurations work without client certificates.
