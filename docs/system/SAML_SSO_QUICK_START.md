# SAML SSO Quick Start Guide

**Date**: 2026-01-02  
**Status**: 🚀 **QUICK START**  
**Tag**: #SAML #SSO #QUICK-START

---

## ⚡ Quick Setup (5 Steps)

### Step 1: Install SSO Server in DSM
- **DSM → Package Center → Search "SSO Server" → Install**
- Open SSO Server application

### Step 2: Configure SSO Server (IdP)
- **SSO Server → General Settings**: Set server URL (must be HTTPS)
- **SSO Server → Service → SAML**: Enable SAML Server
- **Copy these values** (you'll need them):
  - IdP Single Sign-On URL
  - IdP Entity ID  
  - Certificate (download)

### Step 3: Create Enterprise App in Azure AD
- **Azure Portal → Azure AD → Enterprise Applications → New application**
- **Name**: "Synology DSM SSO"
- **Type**: "Create your own application"
- **Set up single sign on → SAML**

### Step 4: Configure SAML in Azure AD
- **Basic SAML Configuration**:
  - Identifier: [IdP Entity ID from Step 2]
  - Reply URL: `https://10.17.17.32:5001/sso/acs`
  - Sign on URL: `https://10.17.17.32:5001`
- **User Attributes**:
  - Unique User Identifier: `user.userprincipalname`
  - Email: `user.mail`
  - Display Name: `user.displayname`
- **Certificate**: Upload from SSO Server or use Azure AD default

### Step 5: Configure DSM SSO Client
- **DSM → Control Panel → Domain/LDAP → SSO Client**
- **Enable SAML SSO**: ✅
- **IdP Information** (from Azure AD):
  - IdP Entity ID
  - IdP Single Sign-On URL
  - IdP Certificate
- **SP Information** (from SSO Server):
  - SP Entity ID
  - SP Assertion Consumer Service URL
- **Save**

---

## ✅ Test SSO

1. **Assign users in Azure AD**:
   - Enterprise Applications → Your DSM app → Users and groups → Add

2. **Test login**:
   - Log out of DSM
   - Try logging in → Should redirect to Azure AD
   - After Azure AD login → Should redirect back to DSM

---

## ⚠️ Important Notes

### HTTPS Requirement
- **SSO Server requires HTTPS** with valid certificate
- If using IP address (`10.17.17.32`), you may need:
  - Self-signed certificate (DSM can generate)
  - Or set up domain name with proper certificate

### Domain Name (Recommended)
- For production, consider setting up a domain name
- Example: `nas.yourdomain.com`
- Makes SAML configuration easier and more secure

---

## 🔧 Troubleshooting

### Issue: SSO Not Working
- ✅ Verify URLs match exactly (case-sensitive)
- ✅ Check certificate is valid
- ✅ Verify user is assigned to app in Azure AD
- ✅ Check DSM logs: Control Panel → Info Center → Log Center

### Issue: Redirect Loop
- ✅ Check Reply URL matches exactly: `https://10.17.17.32:5001/sso/acs`
- ✅ Verify certificate is correct
- ✅ Clear browser cache

### Issue: Users Not Found
- ✅ Verify user attribute mapping
- ✅ Check user exists in Azure AD
- ✅ Verify user is assigned to application

---

## 📋 Configuration Checklist

- [ ] SSO Server package installed
- [ ] SSO Server configured as IdP
- [ ] IdP URLs and Entity ID copied
- [ ] Certificate downloaded from SSO Server
- [ ] Enterprise Application created in Azure AD
- [ ] SAML configured in Azure AD
- [ ] Reply URL and Sign on URL set correctly
- [ ] User attributes configured
- [ ] Certificate uploaded to Azure AD
- [ ] DSM SSO Client configured
- [ ] IdP information entered in DSM
- [ ] SP information entered in DSM
- [ ] Users assigned in Azure AD
- [ ] SSO tested successfully

---

## 📚 Full Documentation

- **Complete Guide**: `docs/system/DSM_SAML_SSO_SETUP_GUIDE.md`
- **Setup Script**: `scripts/python/setup_dsm_saml_sso.py`

---

## 💰 Cost

**FREE** - No additional Azure services needed!

---

**Last Updated**: 2026-01-02  
**Estimated Setup Time**: 30-60 minutes
