# WakaTime Quick Start Guide for LUMINA

## Overview

This quick start guide helps you set up all WakaTime sharing features for the LUMINA project in minutes.

## Prerequisites

- WakaTime account ([Sign up](https://wakatime.com/signup))
- WakaTime plugin installed in your IDE
- `.wakatime-project` file configured (✅ Already done for LUMINA)

## Quick Setup Steps

### 1. Get Your WakaTime Credentials

1. Log in to [WakaTime Dashboard](https://wakatime.com/dashboard)
2. Go to Settings → Account
3. Note your **Username** (e.g., `@yourusername`)
4. Go to Settings → API
5. Generate an **API Key** (store securely!)

### 2. Update Badges in README

Run the badge updater script:

```bash
# Set environment variables
$env:WAKATIME_USER_ID = "your_user_id"
$env:WAKATIME_USERNAME = "@yourusername"

# Run updater
python scripts/python/update_wakatime_badges.py
```

Or manually update `README_LUMINA.md`:
- Replace `{user_id}` with your WakaTime user ID
- Replace `@username` with your WakaTime username

### 3. Enable Project Sharing

1. Go to [WakaTime Dashboard](https://wakatime.com/dashboard)
2. Navigate to Projects
3. Find "LUMINA" project
4. Enable public sharing
5. Copy the badge URL

### 4. Set Up Goals (Optional)

1. Go to WakaTime Dashboard → Goals
2. Create a goal:
   - **Weekly Hours**: 20+ hours
   - **Daily Consistency**: Code every day
   - **Project Focus**: 80%+ time on LUMINA
3. Enable public sharing

### 5. Configure Email Reports (Optional)

1. Go to Settings → Email Reports
2. Add recipient emails
3. Set frequency (weekly recommended)
4. Customize report content

### 6. Generate Embeddable Charts

1. Go to [WakaTime Share](https://wakatime.com/share)
2. Navigate to "Embeddable Charts"
3. Create charts for:
   - Coding activity (last 30 days)
   - Language breakdown
   - Project time distribution
4. Copy embed codes
5. Add to documentation

### 7. Set Up API Integration (Advanced)

1. Store API key in Azure Key Vault:
   ```powershell
   # Example (adjust for your setup)
   az keyvault secret set --vault-name lumina-vault --name wakatime-api-key --value "your_api_key"
   ```

2. Use the integration script:
   ```python
   from scripts.python.wakatime_integration import WakaTimeAPI
   import os

   api_key = os.getenv("WAKATIME_API_KEY")
   client = WakaTimeAPI(api_key)
   stats = client.get_stats("last_7_days")
   ```

## Verification Checklist

- [ ] WakaTime plugin installed and tracking
- [ ] `.wakatime-project` file exists (✅ Done)
- [ ] Badges added to README
- [ ] Project sharing enabled
- [ ] Goals configured (optional)
- [ ] Email reports set up (optional)
- [ ] Charts generated (optional)
- [ ] API integration configured (optional)

## Files Created

1. ✅ `docs/WAKATIME_SHARING_SETUP.md` - Complete documentation
2. ✅ `config/wakatime_config.json` - Configuration template
3. ✅ `scripts/python/wakatime_integration.py` - API client
4. ✅ `scripts/python/update_wakatime_badges.py` - Badge updater
5. ✅ `README_LUMINA.md` - Updated with badges section

## Next Steps

1. **Update Badges**: Replace placeholders with your WakaTime credentials
2. **Enable Sharing**: Make your project public in WakaTime settings
3. **Create Charts**: Generate embeddable charts for documentation
4. **Set Goals**: Create and share coding goals
5. **Automate**: Use scripts to keep badges updated

## Resources

- [WakaTime Share Page](https://wakatime.com/share)
- [WakaTime API Docs](https://wakatime.com/developers)
- [Complete Setup Guide](WAKATIME_SHARING_SETUP.md)

## Support

For issues or questions:
- Check [Complete Setup Guide](WAKATIME_SHARING_SETUP.md)
- Review WakaTime [Documentation](https://wakatime.com/help)
- Open an issue in the LUMINA repository

---

**Last Updated**: 2026-01-09
