# DSM LDAP Authentication Fix - "Incorrect Authentication Information"

**Date**: 2026-01-02  
**Status**: 🔧 **TROUBLESHOOTING**  
**Tag**: #LDAP #DSM #AZURE-AD #FIX

---

## Problem

**Error**: "Incorrect authentication information"  
**Issue**: Bind DN field appears truncated: `ldapadm@matthewlesnewski.onmicr`  
**Expected**: `ldapadm@matthewlesnewski.onmicrosoft.com`

---

## Solution 1: Fix Truncated Username (Most Likely)

The DSM field may be truncating the username. Try these formats:

### Option A: Full UserPrincipalName (Recommended)
```
Bind DN or LDAP administrator account: ldapadm@matthewlesnewski.onmicrosoft.com
Password: 8U4vCqLmvs7DsidyHfF#
```

**Important**: Make sure the entire username is entered - check if DSM is cutting it off.

### Option B: Just Username (If Option A Fails)
```
Bind DN or LDAP administrator account: ldapadm
Password: 8U4vCqLmvs7DsidyHfF#
```

### Option C: Full DN Format (If Options A & B Fail)
```
Bind DN or LDAP administrator account: CN=ldapadm,CN=Users,DC=matthewlesnewski,DC=onmicrosoft,DC=com
Password: 8U4vCqLmvs7DsidyHfF#
```

---

## Solution 2: Use Admin Account Instead

If the service account doesn't work, try your admin account:

### Option A: Gmail Account
```
Bind DN or LDAP administrator account: mlesnewski@gmail.com
Password: [Your Azure/Gmail password]
```

### Option B: UserPrincipalName
```
Bind DN or LDAP administrator account: mlesnewski@matthewlesnewski.onmicrosoft.com
Password: [Your Azure AD password]
```

---

## Solution 3: Verify Service Account Status

The `ldapadm` service account might need additional configuration:

1. **Check if account is enabled**:
   ```powershell
   az ad user show --id ldapadm@matthewlesnewski.onmicrosoft.com
   ```

2. **Verify account has LDAP permissions**:
   - Account should have "Directory Readers" role (already assigned)
   - Account should not be locked
   - Account should not require password change

3. **Reset password if needed**:
   ```powershell
   az ad user update --id ldapadm@matthewlesnewski.onmicrosoft.com --password "NewPassword123!"
   ```

---

## Solution 4: Check Azure AD LDAP Configuration

Azure AD LDAP may need to be enabled:

1. **Verify LDAP is enabled** for your tenant
2. **Check if service accounts** can authenticate via LDAP
3. **Some Azure AD tenants** don't support LDAP for all account types

---

## Solution 5: Try Certificate Authentication

If password authentication fails, switch to certificate-based:

1. **In DSM LDAP config**:
   - Uncheck "Use password authentication"
   - Check "Use client certificate"
   - Certificate: `C:\Users\mlesn\Desktop\ldap_client.crt`
   - Private Key: `C:\Users\mlesn\Desktop\ldap_client.key`

---

## Step-by-Step Fix in DSM

1. **Clear the Bind DN field completely**
2. **Type the full username carefully**:
   - `ldapadm@matthewlesnewski.onmicrosoft.com`
   - Make sure it's not truncated
3. **Enter password**: `8U4vCqLmvs7DsidyHfF#`
4. **Click "Test Connection"** first (before Apply)
5. **If test fails**, try the other options above

---

## Quick Test Commands

### Test Service Account Password
```powershell
# Verify password is correct
az keyvault secret show --vault-name jarvis-lumina --name ldap-service-password --query value -o tsv
```

### Test Account Status
```powershell
# Check if account exists and is enabled
az ad user show --id ldapadm@matthewlesnewski.onmicrosoft.com --query "{displayName:displayName, accountEnabled:accountEnabled, userPrincipalName:userPrincipalName}"
```

---

## Most Likely Fix

**Try this first**:
1. In DSM, clear the Bind DN field
2. Enter: `ldapadm@matthewlesnewski.onmicrosoft.com` (make sure it's complete)
3. Password: `8U4vCqLmvs7DsidyHfF#`
4. Click "Test Connection"

If that fails, try just: `ldapadm` (without the domain)

---

## If All Else Fails

1. **Use your admin account** instead of service account
2. **Try certificate authentication** instead of password
3. **Check Azure AD logs** for authentication failures
4. **Verify Azure AD LDAP is enabled** for your tenant

---

**Last Updated**: 2026-01-02  
**Error**: "Incorrect authentication information"  
**Status**: Troubleshooting in progress
