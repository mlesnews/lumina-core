# ProtonPass Mobile Phone Retrieval - User Account

**Date**: 2026-01-12  
**Account**: USERNAME (configured via `PROTONPASS_USERNAME` environment variable)  
**Location**: Mobile phone number stored in ProtonPass under user account

## Overview

The notification system retrieves your mobile phone number from **ProtonPass CLI** by searching for the user account (configured via `PROTONPASS_USERNAME`) and extracting the mobile phone field.

## How It Works

1. **Search ProtonPass**: Lists all items in ProtonPass
2. **Find User Account**: Searches for items with username/name containing the configured username (default: from `PROTONPASS_USERNAME` environment variable)
3. **Extract Mobile Phone**: Retrieves mobile phone number from the user account item
4. **Use for SMS**: Automatically uses this phone number for SMS (PRODUCTION) notifications

## Authentication

**ProtonPass CLI requires authentication:**

```bash
# Login to ProtonPass CLI (if not already logged in)
# Path: %LOCALAPPDATA%\Programs\ProtonPass\pass-cli.exe login
```

**Note:** If ProtonPass items are protected with an extra password, you may need to unlock them first.

## Configuration

**Set your ProtonPass username for account search:**

```bash
# Windows PowerShell
$env:PROTONPASS_USERNAME = "YOUR_USERNAME"

# Linux/Mac
export PROTONPASS_USERNAME="YOUR_USERNAME"
```

If not set, the system will attempt to find accounts matching common patterns.

## Secret Name Mapping

The system searches for mobile phone using these secret names (in order):
1. `sms-phone-number` - Standard SMS phone number secret
2. `mobile` - Mobile phone field
3. `phone` - Phone number field

**Special Handling:** When searching for any of these, the system automatically:
- Lists all ProtonPass items
- Finds the user account (by configured username)
- Extracts mobile phone from that account

## Field Extraction

The system looks for mobile phone in these fields (in order):
- `mobile` - Direct mobile field
- `phone` - Phone field
- `mobilePhone` - Mobile phone field
- `phoneNumber` - Phone number field
- `extraFields` - Custom fields array (searches for phone/mobile types)
- `customFields` - Custom fields array (searches for phone/mobile types)

## Verification

To verify mobile phone retrieval:

```bash
python scripts/python/ask_ticket_email_notifier.py --test
```

Expected output:
- ✅ "Found mobile phone in user ProtonPass account"
- ✅ SMS (PRODUCTION) channel configured

## Troubleshooting

### Mobile Phone Not Found

1. **Check ProtonPass Authentication:**
   ```bash
   # Windows
   %LOCALAPPDATA%\Programs\ProtonPass\pass-cli.exe info
   ```

2. **Verify User Account Exists:**
   ```bash
   # List all ProtonPass items
   pass-cli.exe item list --output json
   ```
   Look for items with username/name matching your configured `PROTONPASS_USERNAME`

3. **Check Mobile Phone Field:**
   ```bash
   # View account item (replace YOUR_USERNAME with your actual username)
   pass-cli.exe item view --item-title "YOUR_USERNAME" --output json
   ```
   Verify mobile phone field exists in the item

### Authentication Required

If you see "Session is some but needs extra password":
- ProtonPass items are protected with an extra password
- Unlock ProtonPass in the desktop app first
- Or provide extra password when prompted

## Integration

The mobile phone retrieval is integrated into:
- `UnifiedSecretsManager._get_from_protonpass()` - ProtonPass retrieval
- `UnifiedSecretsManager._get_mobile_from_user_account()` - User account search
- `AskTicketEmailNotifier._load_nas_email_config()` - Notification configuration

---

**Tags**: `#PROTONPASS` `#MOBILE` `#SMS` `#TRIAD` `#CREDENTIALS` `@JARVIS` `@LUMINA`
