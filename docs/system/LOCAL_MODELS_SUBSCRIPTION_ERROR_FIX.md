# Local Models Subscription Error - Permanent Fix

## Problem

**PERSISTENT ISSUE**: Local models (ULTRON, KAIJU) getting "invalid model" errors with messages about:
- "Selected model is not supported by bedrock"
- "Subscription plan required"
- "API key required"

**Root Cause**: Cursor is trying to validate local Ollama models through cloud providers (Bedrock) which require subscriptions/API keys - even though local models don't need these.

## Solution

### Automatic Fix Script

Run the permanent fix script:

```bash
python scripts/python/fix_local_models_no_subscription_error.py
```

This script:
1. ✅ Sets `localOnly: true` on all local models
2. ✅ Sets `skipProviderSelection: true` to skip provider dialogs
3. ✅ Sets `provider: "ollama"` explicitly
4. ✅ Sets `noProvider: true` to prevent provider validation
5. ✅ Sets `bypassCloudValidation: true` to bypass all cloud checks
6. ✅ Sets `requiresApiKey: false` (no API key needed for local!)
7. ✅ Sets `requiresSubscription: false` (no subscription needed for local!)
8. ✅ Removes all cloud-related fields (apiKey, subscriptionTier, bedrockEnabled, etc.)

### Auto-Fix on Startup

To prevent this from recurring, add to startup:

```bash
python scripts/python/auto_fix_local_models_on_startup.py
```

Or add to your startup scripts/automation.

## Configuration

### Required Flags for Local Models

All local models MUST have these flags:

```json
{
  "localOnly": true,
  "skipProviderSelection": true,
  "provider": "ollama",
  "noProvider": true,
  "bypassCloudValidation": true,
  "requiresApiKey": false,
  "requiresSubscription": false
}
```

### Removed Fields

These fields are removed from local models (they cause cloud validation):
- `apiKey`
- `authType`
- `authHeader`
- `subscriptionTier`
- `subscriptionPlan`
- `bedrockEnabled`
- `bedrockRegion`
- `awsRegion`
- `cloudProvider`

## Verification

After running the fix:

1. **Restart Cursor IDE**
2. **Check Model Selector** - Should show ULTRON/KAIJU without errors
3. **Test Chat** - Should work without subscription/API key errors
4. **Test Composer** - Should work without subscription/API key errors
5. **Test Agent** - Should work without subscription/API key errors

## Troubleshooting

### Still Getting Errors After Fix

1. **Restart Cursor** (completely close and reopen)
2. **Clear Cursor Cache**:
   - Close Cursor
   - Delete `%APPDATA%\Cursor\Cache` (Windows)
   - Restart Cursor
3. **Re-run Fix Script**:
   ```bash
   python scripts/python/fix_local_models_no_subscription_error.py
   ```
4. **Check User Settings** (not just workspace):
   - Cmd/Ctrl+, (User Settings)
   - Verify models are set to ULTRON/KAIJU
   - Verify no cloud models are selected

### Models Still Showing Cloud Validation

1. **Check Settings File**:
   ```bash
   cat .cursor/settings.json | grep -A 10 "ULTRON"
   ```
   Should show `"localOnly": true` and `"noProvider": true`

2. **Manually Verify Flags**:
   - Open `.cursor/settings.json`
   - Find ULTRON/KAIJU models
   - Verify all required flags are present

## Prevention

### Auto-Fix Script

Add to your automation:
- Startup scripts
- Cron jobs (Linux/Mac)
- Task Scheduler (Windows)
- Pre-commit hooks

### Monitoring

Check periodically:
```bash
python scripts/python/fix_local_models_no_subscription_error.py
```

If it reports "already configured correctly", you're good. If it makes changes, something reset the configuration.

## Status

✅ **Fix Script**: Available
✅ **Auto-Fix**: Available
✅ **Documentation**: Complete

**Last Updated**: 2025-01-05
**Issue**: PERSISTENT - Now scripted to prevent recurrence
