# Synology SAML SSO Complete Setup Guide

## Prerequisites

- Synology DSM access: https://10.17.17.32:5001
- Azure AD access: https://portal.azure.com
- Admin privileges on both systems

## Step-by-Step Setup

### Step 1: Install SSO Server Package

1. Open DSM: https://10.17.17.32:5001
2. Go to **Package Center**
3. Search for **"SSO Server"**
4. Click **Install**
5. Wait for installation to complete

### Step 2: Configure SSO Server as Identity Provider

1. Open **SSO Server** application in DSM
2. Go to **Identity Provider** tab
3. Enable **"Enable SSO Server as Identity Provider"**
4. Note the following (you'll need these for Azure):
   - **Entity ID**: (shown in SSO Server)
   - **SSO URL**: (shown in SSO Server)
   - **Certificate**: Download the certificate

### Step 3: Create Azure AD Enterprise Application

#### Option A: Via Azure Portal (Recommended)

1. Go to: https://portal.azure.com
2. Navigate to: **Azure Active Directory** > **Enterprise applications**
3. Click: **New application**
4. Click: **Create your own application**
5. Enter:
   - **Name**: Synology DSM SSO
   - **Type**: Integrate any other application you don't find in the gallery
6. Click **Create**

#### Option B: Via Azure CLI

```bash
# Create app registration
az ad app create \
  --display-name "Synology DSM SSO" \
  --identifier-uris "https://synology-dsm.local"

# Get app ID
APP_ID=$(az ad app list --display-name "Synology DSM SSO" --query "[0].appId" -o tsv)

# Create service principal
az ad sp create --id $APP_ID
```

**Note**: You'll need a verified domain in Azure AD. If you don't have one:
- Use a placeholder URL (e.g., `https://synology-dsm.local`)
- Verify your domain later
- Update the identifier URI after verification

### Step 4: Configure SAML in Azure AD

1. In your Enterprise Application, go to **Single sign-on**
2. Select **SAML**
3. Click **Edit** on Basic SAML Configuration
4. Enter:
   - **Identifier (Entity ID)**: From Step 2 (SSO Server Entity ID)
   - **Reply URL (Assertion Consumer Service URL)**: `https://10.17.17.32:5001/portal/sso/acs`
   - **Sign on URL**: From Step 2 (SSO Server SSO URL)
5. Click **Save**
6. Download **Federation Metadata XML** (you'll need this for DSM)

### Step 5: Configure DSM SSO Client

1. In DSM, open **SSO Server**
2. Go to **Service Provider** tab
3. Click **Add**
4. Select **Import from metadata file**
5. Upload the **Federation Metadata XML** from Azure AD
6. Configure:
   - **Entity ID**: From Azure AD (Identifier/Entity ID)
   - **ACS URL**: `https://10.17.17.32:5001/portal/sso/acs`
7. Click **Save**

### Step 6: Assign Users in Azure AD

1. In Azure AD Enterprise Application, go to **Users and groups**
2. Click **Add user/group**
3. Select users or groups who should have access to DSM
4. Click **Assign**

### Step 7: Test SSO

1. Log out of DSM
2. Try to log in
3. You should be redirected to Azure AD login
4. After successful Azure AD login, you should be redirected back to DSM
5. You should be logged in automatically

## Troubleshooting

### Issue: "Incorrect Authorization information"
- **Solution**: Check that username format matches Azure AD (usually `username@domain.com`)

### Issue: Redirect loop
- **Solution**: Verify ACS URL matches exactly in both Azure AD and DSM

### Issue: Certificate errors
- **Solution**: Ensure certificates are properly configured in both systems

## Configuration Files

- Azure AD App Config: See `azure_app_config.json` (generated)
- Setup Script: `scripts/nas/sso/setup_saml_sso.sh`

## Next Steps After Setup

1. Test SSO login flow
2. Configure user mapping (if needed)
3. Set up group-based access (optional)
4. Document the setup for team reference
