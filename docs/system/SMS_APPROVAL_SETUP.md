# SMS Approval System Setup Guide

## Current Status

The SMS approval system is implemented and ready, but needs the exact secret names from Azure Key Vault where your phone numbers are stored.

## Setup Steps

### Step 1: Identify Phone Number Secret Names

I've listed all 64 secrets in your Azure Key Vault, but none have obvious phone-related names. 

**Please provide the exact secret names** that contain:
- Your phone number (mlesn)
- Glenda's phone number

### Step 2: Update Configuration

Once you provide the secret names, I'll update `config/sms_approval_config.json`:

```json
{
  "phone_secrets": {
    "primary_user": {
      "secret_name": "YOUR_SECRET_NAME_HERE",
      "description": "Primary user (mlesn) phone number"
    },
    "secondary_user": {
      "secret_name": "GLENDA_SECRET_NAME_HERE",
      "description": "Secondary user (Glenda) phone number"
    }
  }
}
```

### Step 3: Test

After configuration, test the system:

```bash
python scripts/python/dead_man_switch_sms_approval.py --test
```

## Alternative: If Phone Numbers Are in Different Format

If your phone numbers are stored:
- In a JSON structure within another secret
- With different field names
- In a combined secret

Please let me know the format and I'll update the system to parse it correctly.

## All Azure Key Vault Secrets (64 total)

I've listed all secret names. None appear to be phone numbers based on naming. The phone numbers might be:
1. Stored under non-obvious names
2. Part of a larger JSON structure
3. In a different vault or location

**Please share the exact secret names** and I'll configure the system immediately!
