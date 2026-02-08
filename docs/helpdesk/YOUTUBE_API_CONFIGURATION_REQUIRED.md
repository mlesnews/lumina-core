# YouTube API Configuration Required

**Created**: 2026-02-03
**Status**: Open
**Priority**: Medium
**Category**: Configuration

---

## Issue

The YouTube Data API v3 is returning 403 Forbidden errors when using the API key stored in Azure Key Vault (`youtube-api-key`).

## Error

```
403 Client Error: Forbidden for url: https://www.googleapis.com/youtube/v3/channels
```

## Root Cause

The YouTube Data API v3 is likely **not enabled** in the Google Cloud Console project associated with the API key.

---

## Resolution Steps

### 1. Enable YouTube Data API v3

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Select the project associated with the API key
3. Navigate to **APIs & Services** → **Library**
4. Search for "YouTube Data API v3"
5. Click **Enable**

### 2. Verify API Key Restrictions

1. Go to **APIs & Services** → **Credentials**
2. Find the API key
3. Check **API restrictions**
4. Ensure YouTube Data API v3 is allowed

### 3. Check Quota

1. Go to **APIs & Services** → **Dashboard**
2. Select YouTube Data API v3
3. Check **Quotas** tab
4. Default: 10,000 units/day

---

## Current Workaround

Using web search to aggregate YouTube creator content (working):
- `COMMUNITY_FEED_30_DAY_INTEL_20260203.md`
- `YOUTUBE_COMMUNITY_INTEL_FULL_30_DAY_20260203.md`

---

## For Personal Watch History (Optional)

Personal data (watch history, subscriptions, likes) requires **OAuth 2.0** authentication:

1. Create OAuth 2.0 credentials in Google Cloud Console
2. Set up consent screen
3. Implement OAuth flow in syphon scripts
4. Store refresh token securely

This is optional - the current web search approach provides good community intelligence.

---

## Files Affected

- `scripts/python/syphon_youtube_api_channels.py` - API-based channel monitoring
- `scripts/python/syphon_youtube_watch_history_30_days.py` - Watch history (needs cookies)
- `scripts/python/syphon_youtube_account_data.py` - Account data (needs OAuth)

---

## References

- Azure Key Vault: `youtube-api-key` exists and is accessible
- Google Cloud Console: [console.cloud.google.com](https://console.cloud.google.com)
- YouTube Data API docs: [developers.google.com/youtube/v3](https://developers.google.com/youtube/v3)
