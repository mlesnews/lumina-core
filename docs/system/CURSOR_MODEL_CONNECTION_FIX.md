# Cursor Model Connection Fix Guide

## Problem

You're seeing connection errors in Cursor IDE:
- Error: "Selected model is not supported by bedrock"
- All model modes (Auto, Local, Cloud) are failing

## System Architecture

- **ULTRON** = Laptop (localhost) - Local Ollama instance
- **KAIJU** = Desktop PC (KAIJU Number Eight) - Remote Ollama instance at 10.17.17.11:11434
- **NAS** = DS2118+ (Synology) - NAS server at 10.17.17.32
- **NAS** = DS2118+ (Synology) - Network Attached Storage

## Root Cause

Cursor is configured to use **local Ollama models** (ULTRON), but:
1. **Docker Desktop is not running** (Ollama runs in Docker)
2. **Local Ollama is not accessible** on `localhost:11434`
3. When Cursor can't connect to local models, it tries to fall back to cloud models (Bedrock)
4. Bedrock fallback is failing because the selected model isn't supported or credentials aren't configured

## Solution Options

### Option 1: Start Docker Desktop (Recommended)

1. **Start Docker Desktop**
   - Open Docker Desktop application
   - Wait for it to fully start (whale icon in system tray)
   - Verify Docker is running: `docker ps` should work

2. **Start Ollama Container** (if using Docker)
   ```powershell
   docker start ollama
   ```
   Or if Ollama is configured to auto-start with Docker, it should start automatically.

3. **Verify Ollama is Running**
   ```powershell
   # Test connection
   Test-NetConnection -ComputerName localhost -Port 11434
   
   # Or use the diagnostic tool
   python scripts/python/jarvis_cursor_model_diagnostic.py
   ```

4. **In Cursor IDE**
   - Click the model selector in the top-right
   - Select **"ULTRON"** (should now be accessible)
   - Verify it's working by sending a test message

### Option 2: Use KAIJU Temporarily (Quick Fix)

If Docker/Ollama won't start immediately, you can temporarily use **KAIJU** (Desktop PC - KAIJU Number Eight) which is currently accessible:

1. **In Cursor IDE**
   - Click the model selector in the top-right
   - Select **"KAIJU (Iron Legion)"** instead of ULTRON
   - This uses the Desktop PC (KAIJU Number Eight) Ollama instance at `10.17.17.11:11434`

2. **Verify Connection**
   - Send a test message in Cursor Chat
   - Should work immediately (KAIJU is accessible)

3. **Switch Back to ULTRON Later**
   - Once Docker/Ollama is running locally
   - Switch back to "ULTRON" in the model selector

### Option 3: Disable Cloud Fallback (Prevent Bedrock Errors)

If you want to prevent Cursor from trying cloud models when local models aren't available:

1. **In Cursor Settings** (`.cursor/settings.json`):
   - Ensure all models have `"localOnly": true`
   - Ensure all models have `"skipProviderSelection": true`
   - This prevents Cursor from trying cloud fallback

2. **In Cursor UI**:
   - Go to Settings > Features
   - Make sure Chat, Composer, and Agent all use local models only
   - Disable any cloud model options

## Diagnostic Tool

Run the diagnostic tool to check current status:

```powershell
python scripts/python/jarvis_cursor_model_diagnostic.py
```

This will:
- Check if local Ollama is running
- Check if Docker is running
- Check if KAIJU is accessible
- Verify Cursor settings configuration
- Provide specific recommendations

## Prevention

To prevent this issue in the future:

1. **Auto-start Docker Desktop** on Windows login
   - Docker Desktop Settings > General > "Start Docker Desktop when you log in"

2. **Auto-start Ollama Container**
   - Configure Docker to auto-start the Ollama container
   - Or use a Docker Compose file with `restart: unless-stopped`

3. **Monitor Health**
   - Use JARVIS Compound Log Admin to monitor Ollama health
   - Set up alerts if Ollama becomes unavailable

## Current Status

Based on the last diagnostic:
- ✅ **ULTRON is running** - Local Ollama is now accessible!
- ⚠️ **KAIJU Number Eight** (10.17.17.11) - Not currently accessible (but ULTRON is working)
- ❌ **Local Ollama is not running** - Start Docker Desktop
- ❌ **Docker is not running** - Start Docker Desktop first
- ✅ **Cursor settings are correct** - Configured for ULTRON

## Quick Fix Command

To quickly switch to KAIJU in Cursor (manual):
1. Open Cursor IDE
2. Click model selector (top-right)
3. Select "KAIJU (Iron Legion)"
4. Test with a chat message

## Long-term Fix

1. Start Docker Desktop
2. Wait for Ollama to start
3. Switch back to "ULTRON" in Cursor
4. Verify everything works

---

**Note**: The "bedrock" error occurs because Cursor tries cloud models when local models fail. Once local models (ULTRON) or KAIJU are working, the error will disappear.
