# Azure AD LDAP Username Guide

**Date**: 2026-01-02  
**Status**: 📋 **USERNAME CONFIGURATION**  
**Tag**: #LDAP #AZURE-AD #USERNAME

---

## Your Azure AD Configuration

**Tenant Domain**: `matthewlesnewski.onmicrosoft.com`  
**Admin Account**: `mlesnewski@gmail.com` (External account - Gmail)

---

## Username Format for LDAP Authentication

### Option 1: Use Gmail Address Directly (Try This First)

**Username**: `mlesnewski@gmail.com`  
**Password**: Your Gmail account password (the one you use to sign in to Azure)

**Why**: If your Gmail account is the tenant admin, Azure AD may accept it directly.

---

### Option 2: Use User Principal Name (If Option 1 Doesn't Work)

Azure AD may have created a userPrincipalName for your account. Try:

**Username**: `mlesnewski@matthewlesnewski.onmicrosoft.com`  
**Password**: Your Azure AD account password

**Note**: This might be different from your Gmail password if Azure AD created a separate account.

---

### Option 3: Check Your Actual Azure AD Account

To find your exact Azure AD username:

1. **Azure Portal**: https://portal.azure.com
   - Go to **Azure Active Directory** → **Users**
   - Find your account (`mlesnewski@gmail.com`)
   - Check the **User principal name** field

2. **Microsoft 365 Admin Center**: https://admin.microsoft.com
   - Go to **Users** → **Active users**
   - Find your account
   - Check the **Username** field

---

## What to Try in DSM

### First Attempt: Gmail Address
```
Username: mlesnewski@gmail.com
Password: [Your Gmail/Azure password]
```

### If That Doesn't Work: Try User Principal Name
```
Username: mlesnewski@matthewlesnewski.onmicrosoft.com
Password: [Your Azure AD password]
```

---

## Important Notes

### External Accounts in Azure AD
- Gmail accounts can be tenant admins in Azure AD
- For LDAP, Azure AD may require the userPrincipalName format
- Some Azure AD configurations don't allow external accounts for LDAP

### If LDAP Authentication Fails
1. **Verify LDAP is enabled** for your tenant
2. **Check if external accounts** can authenticate via LDAP
3. **Create a service account** in Azure AD if needed:
   - Format: `service-account@matthewlesnewski.onmicrosoft.com`
   - Assign Global Administrator or appropriate permissions
   - Use this account for LDAP authentication

---

## Base DN Configuration

**Base DN**: `DC=matthewlesnewski,DC=onmicrosoft,DC=com`

---

## Testing

1. Try `mlesnewski@gmail.com` first
2. If that fails, try `mlesnewski@matthewlesnewski.onmicrosoft.com`
3. If both fail, check Azure AD user settings or create a service account

---

## Troubleshooting

### Issue: "Authentication Failed" with Gmail Address
**Solution**: 
- Try the userPrincipalName format: `mlesnewski@matthewlesnewski.onmicrosoft.com`
- Verify the password is correct
- Check if LDAP is enabled for external accounts

### Issue: "User Not Found"
**Solution**:
- Verify the account exists in Azure AD
- Check the User principal name in Azure Portal
- Ensure the account has appropriate permissions

### Issue: "LDAP Not Enabled"
**Solution**:
- Azure AD LDAP may need to be enabled
- Some tenants require specific licensing
- Contact Azure support if needed

---

## Summary

**For Your Configuration**:
- **Tenant**: `matthewlesnewski.onmicrosoft.com`
- **Admin Account**: `mlesnewski@gmail.com`
- **Try Username**: `mlesnewski@gmail.com` (first)
- **Fallback Username**: `mlesnewski@matthewlesnewski.onmicrosoft.com`
- **Password**: Your Azure AD/Gmail account password

---

**Last Updated**: 2026-01-02  
**For**: Azure AD LDAP authentication with external (Gmail) admin account
