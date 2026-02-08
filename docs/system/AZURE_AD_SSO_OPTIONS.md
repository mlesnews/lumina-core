# Azure AD SSO Options for DSM

**Date**: 2026-01-02  
**Status**: 📋 **EVALUATION & SETUP GUIDE**  
**Tag**: #LDAP #SSO #AZURE-AD #SAML #OAUTH

---

## Overview

Regular Azure AD does **NOT** support LDAP authentication. You have three options for SSO with DSM:

1. **Azure AD Domain Services (AAD DS)** - Provides LDAP/LDAPS
2. **SAML/OAuth** - Modern SSO (if DSM supports it)
3. **Synology Directory Server** - Local LDAP (not Azure, so not preferred)

---

## Option 1: Azure AD Domain Services (AAD DS)

### What It Is
- Managed domain service that provides LDAP/LDAPS
- Compatible with traditional LDAP applications
- Works with DSM's LDAP configuration

### Requirements
- Azure subscription
- Virtual network (VNet) in Azure
- Additional cost (~$100-200/month depending on region)
- Setup time: 1-2 hours

### Pros
- ✅ Works with existing DSM LDAP configuration
- ✅ No changes needed to current setup
- ✅ Provides LDAP/LDAPS (port 636)
- ✅ Managed service (Microsoft handles maintenance)

### Cons
- ❌ Additional monthly cost
- ❌ Requires Azure VNet setup
- ❌ Takes 20-30 minutes to deploy
- ❌ May require network configuration

### Setup Steps
1. **Enable Azure AD Domain Services**:
   ```powershell
   # Check if already enabled
   az ad ds list
   
   # If not, enable via Azure Portal:
   # Azure Portal → Azure AD Domain Services → Create
   ```

2. **Configure Network**:
   - Create/select VNet
   - Configure subnet for AAD DS
   - Set up DNS

3. **Wait for Deployment** (20-30 minutes)

4. **Get LDAP Endpoint**:
   - AAD DS provides LDAP endpoint
   - Format: `ldaps://[domain].onmicrosoft.com:636`

5. **Configure DSM**:
   - Use AAD DS LDAP endpoint
   - Bind DN: `ldapadm@[domain].onmicrosoft.com`
   - Base DN: `DC=[domain],DC=onmicrosoft,DC=com`

---

## Option 2: SAML/OAuth SSO

### What It Is
- Modern SSO protocol
- Works with Azure AD natively
- No additional services needed

### Requirements
- DSM must support SAML/OAuth
- Azure AD App Registration
- Configuration in both DSM and Azure AD

### Pros
- ✅ No additional cost
- ✅ Works with regular Azure AD
- ✅ Modern, secure protocol
- ✅ Better user experience

### Cons
- ❌ Requires DSM SAML/OAuth support
- ❌ Different configuration than LDAP
- ❌ May not work with all DSM features

### Setup Steps
1. **Check DSM SAML Support**:
   - DSM → Control Panel → Domain/LDAP
   - Look for "SAML" or "SSO" options
   - Check DSM version compatibility

2. **Create Azure AD App Registration**:
   ```powershell
   # Create app registration for SAML
   az ad app create --display-name "DSM SSO" --web-redirect-uris "https://[dsm-ip]:5001"
   ```

3. **Configure SAML in Azure AD**:
   - Azure Portal → Enterprise Applications
   - Add application → Non-gallery application
   - Configure SAML settings

4. **Configure SAML in DSM**:
   - Enter Azure AD SAML metadata
   - Configure certificate
   - Test connection

---

## Option 3: Synology Directory Server (Not Recommended)

### Why Not Recommended
- ❌ Not an Azure service (inconsistent with your preference)
- ❌ Requires local LDAP server setup
- ❌ Additional maintenance overhead
- ❌ Doesn't integrate with Azure AD

### When to Consider
- Only if you need local LDAP and can't use Azure services
- Not recommended for your use case

---

## Recommendation

### For Your Use Case

**Primary Recommendation**: **Azure AD Domain Services (AAD DS)**

**Why**:
- ✅ Works with your existing DSM LDAP configuration
- ✅ Consistent with Azure services preference
- ✅ No changes needed to current setup
- ✅ Provides LDAP/LDAPS as expected

**Alternative**: **SAML/OAuth** (if DSM supports it)
- Check DSM version and SAML support first
- If supported, this is the modern approach
- No additional cost

---

## Next Steps

1. **Check Azure AD Domain Services Status**:
   ```powershell
   az ad ds list
   ```

2. **Check DSM SAML Support**:
   - Review DSM documentation
   - Check Control Panel for SAML options

3. **Decide on Approach**:
   - If AAD DS: Enable and configure
   - If SAML: Set up app registration and configure

4. **Configure DSM**:
   - Use appropriate method based on choice

---

## Cost Comparison

| Option | Monthly Cost | Setup Time | Maintenance |
|--------|-------------|------------|-------------|
| AAD DS | ~$100-200 | 1-2 hours | Low (managed) |
| SAML/OAuth | $0 | 30-60 min | Low |
| Synology Directory Server | $0 | 1-2 hours | Medium |

---

## Security Comparison

| Option | Security | Encryption | MFA Support |
|--------|----------|------------|-------------|
| AAD DS | High | LDAPS (TLS) | Yes (via Azure AD) |
| SAML/OAuth | Very High | TLS | Yes (native) |
| Synology Directory Server | Medium | LDAPS (TLS) | Limited |

---

## Decision Matrix

**Choose AAD DS if**:
- ✅ You want to keep current LDAP configuration
- ✅ You're okay with additional Azure cost
- ✅ You need LDAP compatibility

**Choose SAML/OAuth if**:
- ✅ DSM supports it
- ✅ You want zero additional cost
- ✅ You prefer modern SSO protocols

**Choose Synology Directory Server if**:
- ❌ Only if you can't use Azure services (not recommended)

---

**Last Updated**: 2026-01-02  
**Status**: Evaluation in progress  
**Next**: Check AAD DS status and DSM SAML support
