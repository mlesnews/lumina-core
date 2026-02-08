# Adding Stripe Credentials to ProtonPass

## Quick Guide

To store Stripe credentials in ProtonPass for automatic retrieval:

### Step 1: Create Stripe Item in ProtonPass

1. **Open ProtonPass app** (desktop or web)
2. **Create new item**:
   - Name: `Stripe` or `Stripe API` or `Stripe Credentials`
   - URL: `https://dashboard.stripe.com` (optional)

### Step 2: Add Credential Fields

Add these **custom fields** to the item:

- **Field 1**: 
  - Name: `publishable_key` (or `Publishable Key` or `publishable-key`)
  - Value: Your Stripe Publishable Key (starts with `pk_live_` or `pk_test_`)

- **Field 2**: 
  - Name: `secret_key` (or `Secret Key` or `secret-key` or `api_key`)
  - Value: Your Stripe Secret Key (starts with `sk_live_` or `sk_test_`)

### Step 3: Verify

Run the credential finder to verify:

```bash
python scripts/python/protonpass_credential_finder.py --find-stripe
```

## Field Name Variations Supported

The system will automatically find credentials using these field name variations:

**Publishable Key fields**:
- `publishable_key`
- `publishable-key`
- `Publishable Key`
- `publishablekey`
- `pk_live`
- `pk_test`

**Secret Key fields**:
- `secret_key`
- `secret-key`
- `Secret Key`
- `secretkey`
- `api_key`
- `api-key`
- `API Key`
- `sk_live`
- `sk_test`
- `password` (if API key is stored in password field)

## Account Name Variations

The system searches for items with these names:
- `Stripe`
- `stripe`
- `Stripe API`
- `Stripe Credentials`
- `stripe-api`
- `Stripe.com`

Any item containing "stripe" in the name will be checked.

## Environment Detection

The system automatically detects the environment (live/test) based on the key prefixes:
- `pk_live_` / `sk_live_` → Live mode
- `pk_test_` / `sk_test_` → Test mode

## Troubleshooting

### Credentials Not Found

1. **Check item name**: Make sure it contains "stripe"
2. **Check fields**: Verify field names match supported variations
3. **List all items**: 
   ```bash
   python scripts/python/protonpass_credential_finder.py --list
   ```
4. **Search for Stripe**:
   ```bash
   python scripts/python/protonpass_credential_finder.py --search stripe
   ```

### Authentication Issues

If ProtonPass CLI needs authentication:

```bash
python scripts/python/protonpass_auto_login.py
```

## Benefits

✅ **Automatic Retrieval**: Credentials automatically found and synced
✅ **Secure Storage**: Credentials stay in ProtonPass
✅ **Environment Detection**: Automatically detects live vs test mode
✅ **No Manual Entry**: No need to type credentials manually

## Getting Stripe API Keys

1. Log in to [Stripe Dashboard](https://dashboard.stripe.com)
2. Go to **Developers** → **API keys**
3. Copy your **Publishable key** and **Secret key**
4. Add them to ProtonPass as described above
