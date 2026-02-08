# Azure AD with Custom Profile - Configuration Guide

**Date**: 2026-01-02  
**Status**: 📋 **CONFIGURATION GUIDE**  
**Tag**: #LDAP #AZURE-AD #CUSTOM-PROFILE

---

## Overview

Since DSM doesn't have an "Active Directory" profile option, we use the **"Custom"** profile for Azure AD integration. This requires manual attribute mapping.

---

## Profile Type Selection

**Select**: **Custom** ✅

**Available Options** (in your DSM):
- ✅ **Custom** - Use this for Azure AD
- ❌ Standard - For Synology LDAP only
- ❌ IBM Lotus Domino - For IBM servers only
- ❌ Open Directory - For Mac only

---

## Custom Profile Configuration for Azure AD

### Step 1: Basic Connection Settings

**Domain/LDAP Server**: 
- Your Azure AD domain (e.g., `yourdomain.onmicrosoft.com`)

**Base DN**: 
- Format: `DC=yourdomain,DC=onmicrosoft,DC=com`
- Example: `DC=contoso,DC=onmicrosoft,DC=com`

**Port**: 
- **636** (LDAPS - recommended, secure)

**Enable SSL/TLS**: ✅ **CHECKED**

---

### Step 2: Authentication

**Use Client Certificate**: ✅ **CHECKED**
- Certificate: `C:\Users\mlesn\Desktop\ldap_client.crt`
- Private Key: `C:\Users\mlesn\Desktop\ldap_client.key`

**OR** Use Username/Password:
- Username: `username@yourdomain.onmicrosoft.com`
- Password: Your Azure AD password

---

### Step 3: Custom Attribute Mapping

When using "Custom" profile, you need to configure attribute mappings:

#### User Attributes

**User Base DN**: 
- Example: `OU=Users,DC=yourdomain,DC=onmicrosoft,DC=com`
- Or: `CN=Users,DC=yourdomain,DC=onmicrosoft,DC=com`

**User Filter**: 
- `(&(objectClass=user)(objectCategory=person))`

**User ID Attribute**: 
- `sAMAccountName` or `userPrincipalName`

**User Name Attribute**: 
- `displayName` or `cn`

**User Email Attribute**: 
- `mail` or `userPrincipalName`

**User Group Attribute**: 
- `memberOf`

#### Group Attributes

**Group Base DN**: 
- Example: `OU=Groups,DC=yourdomain,DC=onmicrosoft,DC=com`
- Or: `CN=Groups,DC=yourdomain,DC=onmicrosoft,DC=com`

**Group Filter**: 
- `(&(objectClass=group)(objectCategory=group))`

**Group Name Attribute**: 
- `cn` or `name`

**Group Member Attribute**: 
- `member`

---

## Common Azure AD Attribute Mappings

### For User Accounts:

| DSM Field | Azure AD Attribute | Notes |
|-----------|-------------------|-------|
| User ID | `sAMAccountName` | Or `userPrincipalName` |
| User Name | `displayName` | Or `cn` |
| Email | `mail` | Or `userPrincipalName` |
| Group Membership | `memberOf` | DN of groups |

### For Groups:

| DSM Field | Azure AD Attribute | Notes |
|-----------|-------------------|-------|
| Group Name | `cn` | Or `name` |
| Group Members | `member` | List of user DNs |

---

## Example Configuration

### Base DN
```
DC=contoso,DC=onmicrosoft,DC=com
```

### User Base DN
```
CN=Users,DC=contoso,DC=onmicrosoft,DC=com
```

### Group Base DN
```
CN=Users,DC=contoso,DC=onmicrosoft,DC=com
```

### User Filter
```
(&(objectClass=user)(objectCategory=person))
```

### Group Filter
```
(&(objectClass=group)(objectCategory=group))
```

---

## Testing the Configuration

1. **Test Connection**: Click "Test Connection" button
   - Should verify LDAP connectivity
   - Should verify authentication

2. **Verify Attributes**: After joining, check:
   - Users are visible in DSM
   - Groups are visible
   - User attributes are correct

3. **Test Login**: Try logging in with Azure AD credentials

---

## Troubleshooting

### Issue: "Users Not Found"
**Solutions**:
- Verify User Base DN is correct
- Check User Filter syntax
- Verify User ID Attribute matches Azure AD

### Issue: "Groups Not Found"
**Solutions**:
- Verify Group Base DN is correct
- Check Group Filter syntax
- Verify Group Name Attribute

### Issue: "Authentication Failed"
**Solutions**:
- Verify certificate files are correct
- Check Base DN format
- Try username/password authentication as test

### Issue: "Attribute Mapping Errors"
**Solutions**:
- Verify attribute names match Azure AD schema
- Check for typos in attribute names
- Use Azure AD schema browser to verify attributes

---

## Azure AD Schema Reference

Common Azure AD LDAP attributes:
- `sAMAccountName` - User login name
- `userPrincipalName` - User principal name (email format)
- `displayName` - Display name
- `cn` - Common name
- `mail` - Email address
- `memberOf` - Group membership (DN format)
- `objectClass` - Object class (user, group, etc.)
- `objectCategory` - Object category

---

## Next Steps After Configuration

1. ✅ Test connection
2. ✅ Join domain
3. ✅ Verify users sync
4. ✅ Verify groups sync
5. ✅ Test user login
6. ✅ Configure user permissions in DSM

---

## Summary

**For Azure AD with Custom Profile**:
- ✅ Select "Custom" profile type
- ✅ Configure Base DN: `DC=domain,DC=onmicrosoft,DC=com`
- ✅ Use LDAPS (port 636)
- ✅ Map attributes manually (see table above)
- ✅ Test connection before joining

---

**Last Updated**: 2026-01-02  
**DSM Version**: Without Active Directory profile option  
**For**: Azure AD integration
