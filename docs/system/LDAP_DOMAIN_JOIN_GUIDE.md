# LDAP Domain Join - Step-by-Step Guide

**Date**: 2026-01-02  
**Status**: 📋 **READY TO EXECUTE**  
**Tag**: #LDAP #SSO #DOMAIN-JOIN #MANUAL

---

## Prerequisites Checklist

Before starting, verify:

- [x] Certificates generated and on NAS (`/tmp/ldap_certificates/`)
- [x] LDAP configuration prepared
- [x] Azure AD credentials available
- [x] RDP access to MANUS (10.17.17.11)
- [x] DSM web interface accessible (10.17.17.32:5001)

---

## Step 1: Verify Certificates on NAS

**Action**: Run verification script

```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/verify_ldap_certificates.py --nas-ip 10.17.17.32
```

**Expected Result**: 
- ✅ Certificates exist on NAS
- ✅ File permissions correct
- ✅ Certificate format valid

---

## Step 2: RDP to MANUS

**Action**: Connect to MANUS via RDP

```powershell
mstsc /v:10.17.17.11
```

**Credentials**: Use your MANUS credentials

**Why**: DSM web interface requires manual interaction for security (cannot be automated)

---

## Step 3: Open DSM Web Interface

**Action**: In RDP session, open browser and navigate to:

```
https://10.17.17.32:5001
```

**Note**: You may see a certificate warning - this is normal for self-signed certificates. Click "Advanced" → "Proceed to site".

**Login**: Use your DSM admin credentials

---

## Step 4: Navigate to LDAP Configuration

**Action**: Follow these navigation steps:

1. Click **Control Panel** (top menu)
2. Click **Domain/LDAP** (left sidebar)
3. Click **Join** tab (if not already selected)

**Location**: `Control Panel → Domain/LDAP → Join`

---

## Step 5: Configure LDAP Connection

**Action**: Fill in the LDAP connection details

### Profile Type

**IMPORTANT**: Select the correct profile type:
- **Custom** ✅ **USE THIS** (for Azure AD - allows manual attribute mapping)
- **Standard** ❌ **NOT FOR AZURE AD** (for Synology LDAP Server only)
- **IBM Lotus Domino** ❌ **NOT FOR AZURE AD** (for IBM Lotus Domino servers only)
- **Open Directory** ❌ **NOT FOR AZURE AD** (for Mac Open Directory only)

**Why**: Since "Active Directory" profile is not available in your DSM version, use "Custom" profile for Azure AD. This allows you to manually configure the attribute mappings needed for Azure AD.

### Basic Settings

**Domain/LDAP Server**: 
- Enter your Azure AD domain (e.g., `yourdomain.onmicrosoft.com`)

**Base DN**: 
- Example: `DC=yourdomain,DC=onmicrosoft,DC=com`
- Or retrieve from Azure AD configuration

**Port**: 
- **636** (LDAPS - recommended, secure)
- Or **389** (LDAP - not recommended)

**Enable SSL/TLS**: ✅ **CHECKED** (required for security)

---

## Step 6: Configure Authentication

**Action**: Select authentication method

### Option A: Certificate-Based Authentication (Recommended - More Secure)

1. Select **"Use client certificate"** or **"Certificate authentication"**
2. **Certificate File**: 
   - Path: `/tmp/ldap_certificates/client.crt`
   - Or browse to: `/tmp/ldap_certificates/client.crt`
3. **Private Key File**: 
   - Path: `/tmp/ldap_certificates/client.key`
   - Or browse to: `/tmp/ldap_certificates/client.key`

**Why**: Certificate-based authentication is more secure than password-based.

### Option B: Password-Based Authentication (Alternative)

If certificate authentication doesn't work:

1. **Username**: Enter Azure AD admin username
   - Format: `username@yourdomain.onmicrosoft.com`
2. **Password**: Enter Azure AD admin password

**Note**: Password will be stored securely in DSM.

---

## Step 7: Test Connection

**Action**: Before joining, test the connection

1. Click **"Test Connection"** or **"Verify"** button
2. Wait for verification result

**Expected Result**: 
- ✅ Connection successful
- ✅ Authentication successful
- ✅ Base DN found

**If Error**: 
- Check network connectivity
- Verify LDAP port (636 for LDAPS)
- Verify credentials/certificates
- Check firewall rules

---

## Step 8: Join Domain

**Action**: Complete the domain join

1. Review all settings
2. Click **"Apply"** or **"Join"** button
3. Wait for join process to complete (may take 1-2 minutes)

**Expected Result**: 
- ✅ Domain join successful
- ✅ "Successfully joined domain" message
- ✅ Status shows "Joined"

---

## Step 9: Verify Domain Join

**Action**: Verify the join was successful

### In DSM:
1. Go to **Control Panel → Domain/LDAP**
2. Check status: Should show **"Joined"** or **"Connected"**
3. Check **"Users"** tab: Should show Azure AD users (may take a few minutes to sync)

### Via Script:
```powershell
cd C:\Users\mlesn\Dropbox\my_projects\.lumina
python scripts/python/verify_sso_readiness.py --vault-name jarvis-lumina --nas-ip 10.17.17.32
```

**Expected Result**: 
- ✅ Domain joined: YES
- ✅ SSO ready: YES

---

## Step 10: Configure User Synchronization (Optional)

**Action**: Configure how users are synchronized

1. Go to **Control Panel → Domain/LDAP → Users**
2. Configure sync settings:
   - **Sync Interval**: How often to sync (e.g., every 15 minutes)
   - **User Filter**: Which users to sync (optional)
   - **Group Filter**: Which groups to sync (optional)

**Note**: Initial sync may take several minutes depending on number of users.

---

## Troubleshooting

### Issue: "Connection Failed"
**Solutions**:
- Verify LDAP port (636 for LDAPS)
- Check firewall allows port 636
- Verify DNS resolution for domain
- Test: `telnet yourdomain.onmicrosoft.com 636`

### Issue: "Authentication Failed"
**Solutions**:
- Verify certificate files exist: `/tmp/ldap_certificates/client.crt` and `.key`
- Check certificate permissions (should be readable)
- Try password-based authentication as fallback
- Verify Azure AD credentials

### Issue: "Base DN Not Found"
**Solutions**:
- Verify Base DN format: `DC=domain,DC=com`
- Try retrieving Base DN from Azure AD
- Check Azure AD domain configuration

### Issue: "Certificate Invalid"
**Solutions**:
- Regenerate certificates if needed
- Verify certificate format (PEM)
- Check certificate expiration date
- Ensure private key matches certificate

---

## Post-Join Configuration

### 1. Verify SSO Works
- Test login with Azure AD credentials
- Verify user permissions are correct
- Check group membership sync

### 2. Configure Applications (If Needed)
- Some applications may need SAML/OAuth configuration
- Check application-specific SSO requirements

### 3. Monitor Sync Status
- Check sync logs in DSM
- Monitor for sync errors
- Verify user count matches Azure AD

---

## Security Notes

✅ **Certificate-Based Authentication**: More secure than passwords
✅ **LDAPS (Port 636)**: Encrypted connection
✅ **Certificates on NAS**: Secured with proper permissions
⚠️ **Manual Process**: Required for security (cannot be automated)

---

## Next Steps After Join

1. ✅ Verify SSO functionality
2. ✅ Test user login
3. ✅ Configure application SSO (if needed)
4. ✅ Monitor sync status
5. ✅ Set up certificate rotation schedule

---

## Related Documentation

- `docs/system/SSO_READINESS_STATUS.md` - SSO status
- `docs/system/LDAP_CERTIFICATE_CONFIGURATION.md` - Certificate setup
- `docs/system/NEXT_STEPS_CURRENT.md` - Current tasks

---

**Last Updated**: 2026-01-02  
**Estimated Time**: 15-30 minutes  
**Difficulty**: Medium (requires RDP and web interface navigation)
