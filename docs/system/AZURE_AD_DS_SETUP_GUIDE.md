# Azure AD Domain Services Setup Guide for DSM

**Date**: 2026-01-02  
**Status**: 📋 **SETUP GUIDE**  
**Tag**: #AZURE-AD #AAD-DS #LDAP #DSM

---

## Overview

Azure AD Domain Services (AAD DS) provides LDAP/LDAPS support for DSM, enabling LDAP authentication with Azure AD.

**Cost**: ~$100-200/month  
**Setup Time**: 1-2 hours  
**Deployment Time**: 20-30 minutes

---

## Prerequisites

- Azure subscription
- Azure AD tenant (you have: `matthewlesnewski.onmicrosoft.com`)
- Resource group (can create new)
- Virtual network (can create new)

---

## Step 1: Enable Azure AD Domain Services

### Via Azure Portal

1. **Navigate to Azure AD Domain Services**:
   - Azure Portal → Search "Azure AD Domain Services"
   - Click "Create" or "Add"

2. **Basic Configuration**:
   - **Subscription**: Your subscription
   - **Resource Group**: Create new `aadds-rg` or use existing
   - **DNS Domain Name**: `matthewlesnewski.onmicrosoft.com` (or custom)
   - **Region**: Choose closest to your location (e.g., `eastus`)

3. **Network Configuration**:
   - **Virtual Network**: Create new or select existing
   - **Subnet**: Create dedicated subnet for AAD DS
     - Subnet name: `aadds-subnet`
     - Address range: `/24` (e.g., `10.0.1.0/24`)

4. **Administrator Group**:
   - **AAD DC Administrators**: Select or create group
   - Add your account to this group

5. **Synchronization**:
   - **Scope**: All users (or selected OUs)
   - **Filtered Sync**: Optional

6. **Review and Create**:
   - Review settings
   - Click "Create"
   - Wait 20-30 minutes for deployment

---

## Step 2: Configure Network Connectivity

### Option A: VPN Connection (Recommended for On-Premises)

1. **Create VPN Gateway** (if needed):
   - Azure Portal → Virtual Network Gateway
   - Create Site-to-Site VPN
   - Configure on-premises router

2. **Verify Connectivity**:
   - Test connection from NAS to Azure VNet
   - Verify DNS resolution

### Option B: ExpressRoute (For Enterprise)

- Set up ExpressRoute connection
- Configure routing

---

## Step 3: Get AAD DS LDAP Endpoint

After deployment:

1. **Azure Portal → Azure AD Domain Services**
2. **Properties** tab
3. **LDAP Endpoint**: Note the endpoint
   - Format: `ldaps://[domain].onmicrosoft.com:636`
   - Example: `ldaps://matthewlesnewski.onmicrosoft.com:636`

4. **LDAP Read-Only Endpoint** (if applicable)

---

## Step 4: Configure DSM LDAP

1. **DSM → Control Panel → Domain/LDAP → Join**

2. **Profile Type**: Custom

3. **Basic Settings**:
   - **Domain/LDAP Server**: `matthewlesnewski.onmicrosoft.com` (AAD DS domain)
   - **Base DN**: `DC=matthewlesnewski,DC=onmicrosoft,DC=com`
   - **Port**: `636` (LDAPS)
   - **Enable SSL/TLS**: ✅ CHECKED

4. **Authentication**:
   - **Bind DN**: `ldapadm@matthewlesnewski.onmicrosoft.com`
   - **Password**: `8U4vCqLmvs7DsidyHfF#`
   - Or use certificate authentication

5. **Test Connection**: Click "Test Connection"

6. **Join Domain**: Click "Apply" or "Join"

---

## Step 5: Verify Configuration

1. **Check Domain Join Status**:
   - DSM → Control Panel → Domain/LDAP
   - Should show "Joined" status

2. **Test User Sync**:
   - DSM → Control Panel → Domain/LDAP → Users
   - Should show Azure AD users

3. **Test Authentication**:
   - Try logging in with Azure AD credentials

---

## Troubleshooting

### Issue: Cannot Connect to AAD DS

**Solutions**:
- Verify VPN/network connectivity
- Check firewall rules (port 636)
- Verify DNS resolution
- Check AAD DS health status in Azure Portal

### Issue: Authentication Fails

**Solutions**:
- Verify Bind DN format: `username@domain.onmicrosoft.com`
- Check password is correct
- Verify account is in AAD DC Administrators group
- Check account is enabled in Azure AD

### Issue: Users Not Syncing

**Solutions**:
- Check synchronization scope in AAD DS
- Verify users are in selected OUs
- Wait for sync cycle (can take 15-30 minutes)

---

## Cost Management

**Estimated Monthly Cost**:
- AAD DS: ~$100-200/month (depends on region)
- VPN Gateway: ~$30-100/month (if using VPN)
- Data transfer: Variable

**Cost Optimization**:
- Use same region for all resources
- Monitor data transfer
- Consider reserved instances if long-term

---

## Security Best Practices

1. **Enable LDAPS Only**: Use port 636, not 389
2. **Use Certificate Authentication**: More secure than passwords
3. **Limit AAD DC Administrators**: Only necessary users
4. **Monitor Access Logs**: Review regularly
5. **Enable MFA**: For Azure AD accounts

---

## Next Steps After Setup

1. ✅ Configure user permissions in DSM
2. ✅ Set up group synchronization
3. ✅ Configure SSO for applications
4. ✅ Monitor AAD DS health
5. ✅ Set up alerts for issues

---

**Last Updated**: 2026-01-02  
**Status**: Ready for setup  
**Estimated Time**: 1-2 hours total
