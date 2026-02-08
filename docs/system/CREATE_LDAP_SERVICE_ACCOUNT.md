# Create LDAP Service Account in Azure AD

**Date**: 2026-01-02  
**Status**: 📋 **BEST PRACTICE GUIDE**  
**Tag**: #LDAP #AZURE-AD #SERVICE-ACCOUNT #SECURITY

---

## Why Create a Service Account?

✅ **Better Security**: Dedicated account for LDAP only  
✅ **Best Practice**: Separate service accounts from personal accounts  
✅ **Easier Management**: Can be managed independently  
✅ **Audit Trail**: Clear separation of service vs. personal access  
✅ **Password Policy**: Can have different password requirements  

---

## Create Service Account in Azure AD

### Option 1: Via Azure Portal (Recommended)

1. **Go to Azure Portal**: https://portal.azure.com
2. **Navigate to**: Azure Active Directory → Users
3. **Click**: "+ New user" or "+ Create new user"
4. **Fill in**:
   - **User name**: `ldapadm@matthewlesnewski.onmicrosoft.com`
   - **Name**: `LDAP Admin Service Account`
   - **First name**: `LDAP`
   - **Last name**: `Admin`
   - **Password**: 
     - ✅ **Let me create the password** (recommended)
     - Or use a strong password you create
   - **Roles**: 
     - Select **"Global Administrator"** (for full LDAP access)
     - Or **"Directory Readers"** (if you want minimal permissions)
5. **Click**: "Create"

### Option 2: Via Azure CLI

```powershell
# Create the service account
az ad user create `
    --display-name "LDAP Admin Service Account" `
    --user-principal-name "ldapadm@matthewlesnewski.onmicrosoft.com" `
    --password "YourStrongPassword123!" `
    --force-change-password-next-login false

# Assign Global Administrator role (if needed)
az role assignment create `
    --role "Global Administrator" `
    --assignee "ldapadm@matthewlesnewski.onmicrosoft.com"
```

---

## Account Configuration

### Username
- **Format**: `ldapadm@matthewlesnewski.onmicrosoft.com`
- **Full UPN**: `ldapadm@matthewlesnewski.onmicrosoft.com`

### Password
- Create a **strong password** (meet Azure AD password requirements)
- **Store securely** in Azure Key Vault (recommended)
- **Enable password expiration** (optional, but recommended)

### Permissions
- **Minimum**: Directory Readers (for LDAP read access)
- **Recommended**: Global Administrator (for full LDAP functionality)
- **Alternative**: Custom role with LDAP-specific permissions

---

## Store Credentials in Azure Key Vault

After creating the account, store credentials securely:

```powershell
# Store username
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name ldap-service-username `
    --value "ldapadm@matthewlesnewski.onmicrosoft.com"

# Store password
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name ldap-service-password `
    --value "YourStrongPassword123!"
```

---

## Use in DSM LDAP Configuration

### Username
```
ldapadm@matthewlesnewski.onmicrosoft.com
```

### Password
```
[The password you created for the service account]
```

### Base DN
```
DC=matthewlesnewski,DC=onmicrosoft,DC=com
```

---

## Security Best Practices

### ✅ Do:
- Use a dedicated service account
- Store password in Azure Key Vault
- Use strong password (meet complexity requirements)
- Enable MFA if possible (may require app password for LDAP)
- Rotate password regularly
- Monitor account usage
- Use least privilege (Directory Readers if possible)

### ❌ Don't:
- Use personal accounts for service authentication
- Share service account credentials
- Use weak passwords
- Disable password expiration (unless necessary)
- Use service account for interactive login

---

## Alternative: Minimal Permissions

If you want to use minimal permissions instead of Global Administrator:

### Create Custom Role (Optional)

1. **Azure Portal**: Azure Active Directory → Roles and administrators
2. **Create custom role** with:
   - Read directory data
   - Read all users
   - Read all groups
   - LDAP read permissions

### Assign Directory Readers Role

```powershell
az role assignment create `
    --role "Directory Readers" `
    --assignee "ldapadm@matthewlesnewski.onmicrosoft.com"
```

**Note**: Directory Readers may have limited functionality. Global Administrator is recommended for full LDAP functionality.

---

## Verification

After creating the account:

1. **Verify account exists**:
   ```powershell
   az ad user show --id "ldapadm@matthewlesnewski.onmicrosoft.com"
   ```

2. **Test LDAP authentication** (from DSM):
   - Use username: `ldapadm@matthewlesnewski.onmicrosoft.com`
   - Use password: [Service account password]
   - Test connection in DSM

---

## Summary

**Service Account Details**:
- **Username**: `ldapadm@matthewlesnewski.onmicrosoft.com`
- **Password**: [Create strong password]
- **Role**: Global Administrator (recommended) or Directory Readers
- **Purpose**: LDAP authentication for DSM

**Next Steps**:
1. Create account in Azure AD
2. Store credentials in Key Vault
3. Use in DSM LDAP configuration
4. Test connection

---

**Last Updated**: 2026-01-02  
**Recommendation**: ✅ **YES - Create dedicated service account**
