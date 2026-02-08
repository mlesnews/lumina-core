# LDAP Authentication Options - Password vs Certificates

**Date**: 2026-01-02  
**Status**: 📋 **AUTHENTICATION GUIDE**  
**Tag**: #LDAP #AUTHENTICATION #PASSWORD #CERTIFICATES

---

## Authentication Methods

DSM supports two authentication methods for LDAP:

1. **Certificate-Based Authentication** ✅ **RECOMMENDED** (More Secure)
2. **Username/Password Authentication** ⚠️ (Fallback)

---

## Option 1: Certificate-Based Authentication (Recommended)

### Configuration
- **Use Client Certificate**: ✅ **CHECKED**
- **Certificate File**: `C:\Users\mlesn\Desktop\ldap_client.crt`
- **Private Key File**: `C:\Users\mlesn\Desktop\ldap_client.key`
- **Password**: ❌ **NOT NEEDED** (certificates provide authentication)

### Why Use Certificates?
- ✅ More secure (mutual TLS authentication)
- ✅ No password stored
- ✅ Better for hardening LUMINA
- ✅ Industry best practice

---

## Option 2: Username/Password Authentication (Fallback)

### If Certificates Don't Work, Use This:

**Username**: 
- Format: `username@yourdomain.onmicrosoft.com`
- Example: `admin@contoso.onmicrosoft.com`
- **Use**: Your Azure AD Global Administrator or LDAP-enabled account

**Password**: 
- Your Azure AD account password
- **Use**: The password for the username above

### Important Notes:
- ⚠️ Password will be stored in DSM (encrypted)
- ⚠️ Less secure than certificates
- ⚠️ Use only if certificates don't work

---

## Which Password to Use?

### If Using Certificate Authentication:
- **Password**: ❌ **NOT NEEDED**
- Just use the certificate files

### If Using Username/Password Authentication:

**Option A: Service Account (Recommended)**
- **Username**: `ldapadm@matthewlesnewski.onmicrosoft.com`
- **Password**: Service account password (stored in Key Vault)
- **Why**: Dedicated account, better security, best practice

**Option B: Personal Admin Account**
- **Username**: `mlesnewski@gmail.com` (try this first)
- **Or**: `mlesnewski@matthewlesnewski.onmicrosoft.com` (if Gmail doesn't work)
- **Password**: Your Azure AD account password

---

## Azure AD Account Requirements

### For LDAP Authentication, You Need:

1. **Global Administrator** account (recommended)
   - Has full access to Azure AD
   - Can perform LDAP operations
   - Username: `admin@yourdomain.onmicrosoft.com` (or your admin account)

2. **OR** LDAP-enabled service account
   - Must have LDAP read permissions
   - Must be enabled for LDAP authentication

### Password:
- Use the password for whichever account you choose above
- This is your Azure AD account password (not a separate LDAP password)

---

## Recommendation

### Best Option: Create Service Account
1. Create dedicated service account: `ldapadm@matthewlesnewski.onmicrosoft.com`
2. Store credentials in Azure Key Vault
3. Use service account for LDAP authentication
4. See: `docs/system/CREATE_LDAP_SERVICE_ACCOUNT.md`

### Alternative 1: Certificate-Based Authentication
1. Select "Use Client Certificate"
2. Browse to certificate: `C:\Users\mlesn\Desktop\ldap_client.crt`
3. Browse to private key: `C:\Users\mlesn\Desktop\ldap_client.key`
4. **Leave password field empty** (if there is one)
5. Test connection

### If Certificates Don't Work: Username/Password
1. Uncheck "Use Client Certificate"
2. Enter username: `your-admin@yourdomain.onmicrosoft.com`
3. Enter password: Your Azure AD admin password
4. Test connection

---

## Security Considerations

### Certificate-Based (Recommended):
- ✅ No password stored
- ✅ Mutual TLS authentication
- ✅ More secure
- ✅ Better for compliance

### Username/Password:
- ⚠️ Password stored in DSM (encrypted)
- ⚠️ Single-factor authentication
- ⚠️ Less secure
- ⚠️ Use only if necessary

---

## Troubleshooting

### Issue: "Certificate Authentication Failed"
**Solutions**:
- Verify certificate files are correct
- Check certificate hasn't expired
- Try username/password as fallback
- Verify certificate format (PEM)

### Issue: "Password Authentication Failed"
**Solutions**:
- Verify username format: `user@domain.onmicrosoft.com`
- Check password is correct
- Verify account has LDAP permissions
- Check account is not locked/disabled

### Issue: "Both Methods Fail"
**Solutions**:
- Verify Base DN is correct
- Check LDAP port (636 for LDAPS)
- Verify SSL/TLS is enabled
- Check network connectivity
- Verify Azure AD LDAP is enabled

---

## Summary

**For Certificate-Based Auth**:
- ✅ Use certificates (no password needed)
- Certificate: `C:\Users\mlesn\Desktop\ldap_client.crt`
- Private Key: `C:\Users\mlesn\Desktop\ldap_client.key`

**For Username/Password Auth** (if needed):
- Username: `your-admin@yourdomain.onmicrosoft.com`
- Password: Your Azure AD admin account password

---

**Last Updated**: 2026-01-02  
**Recommendation**: Use certificate-based authentication when possible
