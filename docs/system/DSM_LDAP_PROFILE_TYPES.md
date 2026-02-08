# DSM LDAP Profile Types - Guide

**Date**: 2026-01-02  
**Status**: 📋 **REFERENCE**  
**Tag**: #LDAP #DSM #PROFILE-TYPE

---

## Profile Type Selection

When configuring LDAP in DSM, you must select the appropriate profile type based on your LDAP server.

---

## Available Profile Types

### 1. **Active Directory** ✅ **FOR AZURE AD**

**Use When**: Connecting to Microsoft Active Directory or Azure AD

**Characteristics**:
- Optimized for Microsoft AD/Azure AD
- Automatic attribute mapping
- Best compatibility with Azure AD
- Supports standard AD features (group membership, user attributes, etc.)

**Recommended For**:
- ✅ Azure AD (Microsoft 365)
- ✅ Microsoft Active Directory (on-premises)
- ✅ Windows Server AD

---

### 2. **Standard** ❌ **NOT FOR AZURE AD**

**Use When**: Connecting to Synology LDAP Server or Mac Open Directory

**Characteristics**:
- Designed for Synology's own LDAP Server
- Also works with Mac Open Directory
- Limited compatibility with other LDAP servers

**NOT Recommended For**:
- ❌ Azure AD
- ❌ Microsoft Active Directory
- ❌ Other enterprise LDAP servers

---

### 3. **Custom** ⚠️ **FALLBACK FOR AZURE AD**

**Use When**: Active Directory profile not available, or need custom attribute mapping

**Characteristics**:
- Manual attribute mapping required
- More configuration needed
- Flexible but more complex

**Use For**:
- Azure AD (if Active Directory option not available)
- Other LDAP servers
- Custom LDAP configurations

**Configuration Required**:
- User DN pattern
- Group DN pattern
- Attribute mappings (UID, GID, etc.)

---

### 4. **IBM Lotus Domino** (If Available)

**Use When**: Connecting to IBM Lotus Domino LDAP server

**NOT For**: Azure AD or Microsoft AD

---

## Recommendation for Azure AD

### ✅ **Custom** Profile (Required - Active Directory not available)
- ✅ Use this for Azure AD (Active Directory profile not available in your DSM)
- ⚠️ Requires manual attribute mapping
- ⚠️ More configuration needed
- ✅ Works well with proper configuration

### ❌ **NOT Recommended**:
- **Standard** - Not designed for Azure AD
- **IBM Lotus Domino** - For IBM servers only
- **Open Directory** - For Mac only

---

## How to Change Profile Type

1. In DSM, go to **Control Panel → Domain/LDAP**
2. If already joined, click **"Leave"** first
3. Go to **Join** tab
4. Select profile type from dropdown
5. Configure settings based on selected profile
6. Test connection
7. Join domain

---

## Profile Type Comparison

| Profile Type | Azure AD | Auto Config | Complexity | Recommended |
|-------------|----------|-------------|------------|-------------|
| **Active Directory** | ✅ Yes | ✅ Yes | Low | ✅ **BEST** |
| **Custom** | ✅ Yes | ❌ No | High | ⚠️ Fallback |
| **Standard** | ❌ No | ✅ Yes | Low | ❌ **NO** |

---

## Troubleshooting

### Issue: "Profile Type Not Available"
**Solution**: 
- Check DSM version (newer versions have Active Directory profile)
- Update DSM if needed
- Use Custom profile as fallback

### Issue: "Connection Works But Users Don't Sync"
**Solution**:
- Verify profile type matches your LDAP server
- Check attribute mappings (if using Custom)
- Verify Base DN is correct

### Issue: "Standard Profile Selected But Not Working"
**Solution**:
- Change to "Active Directory" or "Custom"
- Standard is only for Synology LDAP/Mac Open Directory

---

## Summary

**For Azure AD**: 
1. **First**: Try "Active Directory" profile
2. **Fallback**: Use "Custom" profile if Active Directory not available
3. **Never**: Use "Standard" profile for Azure AD

---

**Last Updated**: 2026-01-02  
**For**: Azure AD / Microsoft Active Directory integration
