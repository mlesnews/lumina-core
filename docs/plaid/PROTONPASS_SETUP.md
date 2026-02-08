# Adding Plaid Credentials to ProtonPass

## Quick Guide

To store Plaid credentials in ProtonPass for automatic retrieval:

### Step 1: Create Plaid Item in ProtonPass

1. **Open ProtonPass app** (desktop or web)
2. **Create new item**:
   - Name: `Plaid` or `Plaid API` or `Plaid Credentials`
   - URL: `https://dashboard.plaid.com` (optional)

### Step 2: Add Credential Fields

Add these **custom fields** to the item:

- **Field 1**: 
  - Name: `client_id` (or `Client ID` or `client-id`)
  - Value: Your Plaid Client ID

- **Field 2**: 
  - Name: `secret` (or `Secret` or `api_secret` or `API Secret`)
  - Value: Your Plaid Secret

- **Field 3** (optional):
  - Name: `environment`
  - Value: `sandbox` or `production`

### Step 3: Verify

Run the credential finder to verify:

```bash
python scripts/python/protonpass_credential_finder.py --find-plaid
```

### Step 4: Sync to Azure Key Vault

Once credentials are in ProtonPass, sync them:

```bash
python scripts/python/setup_plaid_azure.py --from-protonpass
```

## Field Name Variations Supported

The system will automatically find credentials using these field name variations:

**Client ID fields**:
- `client_id`
- `Client ID`
- `client-id`
- `ClientID`
- `CLIENT_ID`

**Secret fields**:
- `secret`
- `Secret`
- `api_secret`
- `api-secret`
- `API Secret`
- `API_SECRET`
- `password` (if API key is stored in password field)

## Account Name Variations

The system searches for items with these names:
- `Plaid`
- `plaid`
- `Plaid API`
- `Plaid Credentials`
- `plaid-api`
- `Plaid.com`

Any item containing "plaid" in the name will be checked.

## Troubleshooting

### Credentials Not Found

1. **Check item name**: Make sure it contains "plaid"
2. **Check fields**: Verify field names match supported variations
3. **List all items**: 
   ```bash
   python scripts/python/protonpass_credential_finder.py --list
   ```
4. **Search for Plaid**:
   ```bash
   python scripts/python/protonpass_credential_finder.py --search plaid
   ```

### Authentication Issues

If ProtonPass CLI needs authentication:

```bash
python scripts/python/protonpass_auto_login.py
```

## Benefits

✅ **Automatic Retrieval**: Credentials automatically found and synced
✅ **Secure Storage**: Credentials stay in ProtonPass
✅ **Azure Sync**: Automatically synced to Azure Key Vault when needed
✅ **No Manual Entry**: No need to type credentials manually
