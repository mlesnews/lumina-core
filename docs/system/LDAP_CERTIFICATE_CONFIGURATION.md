# LDAP Client Certificate Configuration

**Date**: 2026-01-02  
**Status**: ✅ SSH Fixed | ⚠️ Certificates Need to be Added to Key Vault

---

## ✅ Completed

### 1. SSH Public Key Failures - FIXED
- **Issue**: SSH was attempting public key authentication first, causing failures
- **Fix**: Updated `nas_azure_vault_integration.py` to use password-only authentication
- **Changes**:
  - Added `allow_agent=False` to disable SSH agent
  - Added `look_for_keys=False` to prevent public key attempts
  - Now uses password authentication directly from Azure Key Vault

### 2. Azure Key Vault Verification
- **Vault Name**: `jarvis-lumina` ✅
- **Vault URL**: `https://jarvis-lumina.vault.azure.net/` ✅
- **Status**: Fully configured and accessible ✅

---

## ⚠️ Pending: LDAP Client Certificates

### Current Status
LDAP client certificates are **NOT** currently in Azure Key Vault. They need to be added.

### Certificate Locations

#### Option 1: Azure Key Vault (Recommended)
Store certificates in Key Vault for secure, automated access:

```powershell
# Add certificate to Key Vault
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name ldap-client-certificate `
    --file "path/to/client.crt"

# Add private key to Key Vault
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name ldap-client-private-key `
    --file "path/to/client.key"
```

#### Option 2: Local Files (Manual)
If certificates are stored locally, provide paths when running the script:

```powershell
python scripts/python/configure_ldap_certificates_rdp.py `
    --cert-file "C:\path\to\client.crt" `
    --key-file "C:\path\to\client.key"
```

#### Option 3: Azure AD Certificate
If using Azure AD, certificates can be obtained from:
- **Azure Portal**: Azure Active Directory → App registrations → Your app → Certificates & secrets
- **Certificate Export**: Export the certificate and private key from your Azure AD app registration

---

## RDP/MANUS Automation

### Step 1: Prepare Certificates
Run the configuration script to prepare certificates on NAS:

```powershell
# If certificates are in Key Vault:
python scripts/python/configure_ldap_certificates_rdp.py

# If certificates are local files:
python scripts/python/configure_ldap_certificates_rdp.py `
    --cert-file "C:\path\to\client.crt" `
    --key-file "C:\path\to\client.key"
```

This will:
- Retrieve certificates from Key Vault (or use local files)
- Save certificates to NAS at `/tmp/ldap_certificates/`
- Create RDP automation script

### Step 2: RDP to MANUS
```powershell
mstsc /v:10.17.17.11
```

### Step 3: Upload Certificates via DSM
1. In RDP session, open DSM: `https://10.17.17.32:5001`
2. Navigate to: **Control Panel → Domain/LDAP**
3. Click: **Join** (or **Edit** if already joined)
4. In **Client Certificate** section:
   - **Certificate file**: `/tmp/ldap_certificates/client.crt`
   - **Private key file**: `/tmp/ldap_certificates/client.key`
5. Click: **Apply**

### Alternative: Copy Certificates from NAS
If DSM requires local file paths, copy from NAS:

```powershell
# From MANUS RDP session, copy certificates from NAS
scp admin@10.17.17.32:/tmp/ldap_certificates/client.crt C:\temp\
scp admin@10.17.17.32:/tmp/ldap_certificates/client.key C:\temp\
```

Then use local paths in DSM.

---

## Certificate File Formats

### Certificate (.crt or .pem)
```
-----BEGIN CERTIFICATE-----
[Base64 encoded certificate data]
-----END CERTIFICATE-----
```

### Private Key (.key or .pem)
```
-----BEGIN PRIVATE KEY-----
[Base64 encoded private key data]
-----END PRIVATE KEY-----
```

Or for RSA:
```
-----BEGIN RSA PRIVATE KEY-----
[Base64 encoded private key data]
-----END RSA PRIVATE KEY-----
```

---

## Troubleshooting

### SSH Connection Issues
- **Fixed**: Public key authentication failures resolved
- **Method**: Password-only authentication from Key Vault
- **Status**: ✅ Working

### Certificate Not Found
- **Error**: "Certificates not found in Key Vault"
- **Solution**: Add certificates to Key Vault using commands above
- **Or**: Use `--cert-file` and `--key-file` flags with local paths

### DSM Certificate Upload
- **Issue**: DSM asking for certificate location
- **Solution**: Use paths `/tmp/ldap_certificates/client.crt` and `/tmp/ldap_certificates/client.key`
- **Or**: Copy certificates to local machine and use local paths

---

## Scripts Created

1. **`scripts/python/configure_ldap_certificates_rdp.py`**
   - Retrieves certificates from Key Vault or local files
   - Saves certificates to NAS
   - Creates RDP automation script

2. **`scripts/powershell/upload_ldap_certificates_rdp.ps1`**
   - RDP automation instructions
   - Generated automatically by the Python script

---

## Next Steps

1. **Add certificates to Key Vault** (if not already done):
   ```powershell
   az keyvault secret set --vault-name jarvis-lumina --name ldap-client-certificate --file "cert.pem"
   az keyvault secret set --vault-name jarvis-lumina --name ldap-client-private-key --file "key.pem"
   ```

2. **Run configuration script**:
   ```powershell
   python scripts/python/configure_ldap_certificates_rdp.py
   ```

3. **RDP to MANUS and upload via DSM** (see Step 3 above)

---

**Last Updated**: 2026-01-02
