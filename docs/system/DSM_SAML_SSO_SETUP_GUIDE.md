# DSM SAML SSO Setup Guide with Azure AD

**Date**: 2026-01-02  
**Status**: 📋 **SETUP GUIDE**  
**Tag**: #SAML #SSO #AZURE-AD #DSM

---

## Overview

Configure SAML SSO between DSM and Azure AD using Synology SSO Server package.

**Cost**: $0 (no additional Azure services needed)  
**Setup Time**: 30-60 minutes  
**Requires**: Synology SSO Server package installed on DSM

---

## Prerequisites

- DSM with Synology SSO Server package installed
- Azure AD tenant (`matthewlesnewski.onmicrosoft.com`)
- Admin access to both DSM and Azure AD
- Valid domain name for DSM (for HTTPS)

---

## Step 1: Install Synology SSO Server

1. **DSM → Package Center**
2. **Search**: "SSO Server"
3. **Install**: Synology SSO Server
4. **Open**: SSO Server application

---

## Step 2: Configure SSO Server as Identity Provider (IdP)

1. **SSO Server → General Settings**:
   - **Server URL**: Enter DSM URL with valid domain
     - Example: `https://nas.yourdomain.com:5001`
     - Must be HTTPS with valid certificate

2. **SSO Server → Service → SAML**:
   - **Enable SAML Server**: ✅ CHECKED
   - **Note the following** (you'll need these):
     - **IdP Single Sign-On URL**: Copy this
     - **IdP Entity ID**: Copy this
     - **Certificate**: Download the certificate

3. **Save Configuration**

---

## Step 3: Register DSM as Application in Azure AD

1. **Azure Portal → Azure Active Directory → Enterprise Applications**

2. **New Application**:
   - Click "New application"
   - Click "Create your own application"
   - **Name**: "Synology DSM SSO"
   - **Type**: "Integrate any other application you don't find in the gallery"
   - Click "Create"

3. **Configure SAML**:
   - Click "Set up single sign on"
   - Select "SAML"

4. **Basic SAML Configuration**:
   - **Identifier (Entity ID)**: Enter IdP Entity ID from SSO Server
   - **Reply URL (Assertion Consumer Service URL)**: 
     - Format: `https://[dsm-url]:5001/sso/acs`
     - Example: `https://nas.yourdomain.com:5001/sso/acs`
   - **Sign on URL**: 
     - Format: `https://[dsm-url]:5001`
     - Example: `https://nas.yourdomain.com:5001`

5. **User Attributes & Claims**:
   - **Unique User Identifier**: `user.userprincipalname`
   - **Email**: `user.mail`
   - **Display Name**: `user.displayname`

6. **SAML Signing Certificate**:
   - Upload certificate from SSO Server
   - Or use Azure AD certificate

7. **Save Configuration**

---

## Step 4: Configure DSM as Service Provider (SP)

1. **DSM → Control Panel → Domain/LDAP → SSO Client**

2. **Enable SAML SSO**: ✅ CHECKED

3. **IdP Information** (from Azure AD):
   - **IdP Entity ID**: From Azure AD SAML configuration
   - **IdP Single Sign-On URL**: From Azure AD SAML configuration
   - **IdP Certificate**: Upload from Azure AD

4. **SP Information**:
   - **SP Entity ID**: From SSO Server (IdP Entity ID)
   - **SP Assertion Consumer Service URL**: From SSO Server

5. **User Attribute Mapping**:
   - **User ID**: `userPrincipalName` or `mail`
   - **Email**: `mail`
   - **Display Name**: `displayName`

6. **Save Configuration**

---

## Step 5: Test SSO

1. **Test from Azure AD**:
   - Azure Portal → Enterprise Applications → Your DSM app
   - Click "Test single sign-on"
   - Should redirect to DSM login

2. **Test from DSM**:
   - Log out of DSM
   - Try logging in with Azure AD credentials
   - Should redirect to Azure AD login
   - After login, should redirect back to DSM

---

## Step 6: Assign Users/Groups

1. **Azure Portal → Enterprise Applications → Your DSM app → Users and groups**

2. **Add User/Group**:
   - Click "Add user/group"
   - Select users or groups
   - Click "Assign"

3. **Verify Access**:
   - Assigned users can now SSO to DSM
   - Unassigned users cannot access

---

## Troubleshooting

### Issue: SSO Not Working

**Solutions**:
- Verify URLs match exactly (case-sensitive)
- Check certificate is valid and uploaded correctly
- Verify user is assigned to application
- Check DSM logs for errors
- Verify HTTPS certificate is valid

### Issue: Redirect Loop

**Solutions**:
- Check Reply URL matches exactly
- Verify certificate is correct
- Check user attribute mapping
- Clear browser cache

### Issue: Users Not Found

**Solutions**:
- Verify user attribute mapping
- Check user exists in Azure AD
- Verify user is assigned to application
- Check userPrincipalName format

---

## Security Best Practices

1. **Use HTTPS**: Required for SAML
2. **Valid Certificates**: Use proper SSL certificates
3. **Limit Access**: Only assign necessary users/groups
4. **Enable MFA**: For Azure AD accounts
5. **Monitor Logs**: Review access regularly

---

## Benefits of SAML SSO

✅ **No Additional Cost**: Uses regular Azure AD  
✅ **Modern Protocol**: Industry standard  
✅ **Better Security**: Certificate-based  
✅ **User Experience**: Single sign-on  
✅ **MFA Support**: Native Azure AD MFA

---

## Comparison: SAML vs AAD DS

| Feature | SAML SSO | AAD DS |
|---------|----------|--------|
| Cost | $0 | ~$100-200/month |
| Setup Time | 30-60 min | 1-2 hours |
| Protocol | SAML | LDAP/LDAPS |
| MFA | Native | Via Azure AD |
| Maintenance | Low | Managed by Microsoft |

---

## Next Steps

1. ✅ Test SSO with test user
2. ✅ Assign production users/groups
3. ✅ Configure user permissions in DSM
4. ✅ Set up monitoring/alerts
5. ✅ Document for team

---

**Last Updated**: 2026-01-02  
**Status**: Ready for setup  
**Estimated Time**: 30-60 minutes
