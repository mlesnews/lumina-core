# Cursor IDE "Connection Stalled" Workflow Fix

## Problem Statement

**Error**: `Connection stalled` / `LTe: Connection stalled`
**Location**: Cursor IDE Agent Backend Streaming
**Request ID**: `a2155803-eda4-4daf-88ef-927515c31d0c`
**Impact**: VS Code/Cursor IDE workflows not executing, agent chat/composer not responding

## Root Cause Analysis

The "Connection stalled" error occurs when the Cursor agent backend cannot maintain a streaming connection. Based on your configuration, this is likely caused by:

1. **Ollama Service Not Running**: Your Cursor is configured to use local Ollama models (`ULTRON` at `http://localhost:11434`), but the service may not be running or accessible.

2. **Network Connectivity Issues**: Localhost connection to Ollama may be blocked or timing out.

3. **Timeout Configuration**: The agent backend may be timing out before Ollama responds, especially for larger models like `ULTRON_72B`.

4. **Agent Backend Streaming Issues**: The Cursor agent backend may be overwhelmed or encountering internal errors.

5. **Model Availability**: The configured models (`qwen2.5-coder:7b`, `qwen2-72b:latest`) may not be available in Ollama.

## Current Configuration Analysis

From `.vscode/settings.json`:

```json
{
  "cursor.ai.model": "ULTRON",
  "cursor.agent.customModels": [
    {
      "name": "ULTRON",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434",
      "timeout": null  // ⚠️ MISSING TIMEOUT
    },
    {
      "name": "ULTRON_72B",
      "timeout": 120000,  // ✅ HAS TIMEOUT
      "maxTokens": 4096
    }
  ]
}
```

**Issues Identified**:
- Primary model `ULTRON` has no timeout configuration
- No retry logic configured
- No connection health checks
- No fallback mechanism

## Diagnostic Steps

### Step 1: Verify Ollama Service Status

```powershell
# Check if Ollama service is running
Get-Service -Name "*ollama*" -ErrorAction SilentlyContinue

# Test Ollama API connectivity
Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -Method GET -UseBasicParsing

# Check if port 11434 is listening
Test-NetConnection -ComputerName localhost -Port 11434
```

### Step 2: Verify Model Availability

```powershell
# List available models in Ollama
$response = Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing
$models = ($response.Content | ConvertFrom-Json).models
$models | Select-Object name

# Check if required models exist
$requiredModels = @("qwen2.5-coder:7b", "qwen2-72b:latest")
foreach ($model in $requiredModels) {
    $exists = $models | Where-Object { $_.name -like "*$model*" }
    if ($exists) {
        Write-Host "✅ $model is available" -ForegroundColor Green
    } else {
        Write-Host "❌ $model is NOT available" -ForegroundColor Red
    }
}
```

### Step 3: Test Model Response Time

```powershell
# Test model response (simple completion)
$body = @{
    model = "qwen2.5-coder:7b"
    prompt = "Hello"
    stream = $false
} | ConvertTo-Json

$startTime = Get-Date
try {
    $response = Invoke-WebRequest -Uri "http://localhost:11434/api/generate" `
        -Method POST `
        -Body $body `
        -ContentType "application/json" `
        -TimeoutSec 30 `
        -UseBasicParsing
    $endTime = Get-Date
    $duration = ($endTime - $startTime).TotalSeconds
    Write-Host "✅ Model responded in $duration seconds" -ForegroundColor Green
} catch {
    Write-Host "❌ Model failed to respond: $($_.Exception.Message)" -ForegroundColor Red
}
```

## Fix Implementation

### Fix 1: Add Timeout Configuration to Primary Model

**File**: `.vscode/settings.json`

Update the `ULTRON` model configuration to include timeout and maxTokens:

```json
{
  "cursor.agent.customModels": [
    {
      "title": "ULTRON Cluster (Local Only)",
      "name": "ULTRON",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "apiBase": "http://localhost:11434",
      "contextLength": 8192,
      "timeout": 60000,  // ✅ ADD: 60 second timeout
      "maxTokens": 2000,  // ✅ ADD: Token limit
      "description": "ULTRON Cluster Router - Fast coding model (qwen2.5-coder:7b) - LOCAL ONLY, NO API KEY REQUIRED",
      "localOnly": true,
      "skipProviderSelection": true,
      "requiresApiKey": false,
      "requiresSubscription": false
    }
  ]
}
```

### Fix 2: Add Retry Configuration

**File**: `.vscode/settings.json` (add to root level)

```json
{
  "cursor.agent.retryAttempts": 3,
  "cursor.agent.retryDelay": 1000,
  "cursor.agent.connectionTimeout": 30000,
  "cursor.agent.streamTimeout": 120000
}
```

### Fix 3: Add Health Check Script

**File**: `scripts/python/diagnose_cursor_connection.py`

See separate file creation below.

## Workflow Recovery Steps

### Immediate Actions

1. **Restart Ollama Service**:
   ```powershell
   # Windows Service
   Restart-Service -Name "Ollama" -ErrorAction SilentlyContinue

   # Or if running as process
   Get-Process -Name "ollama" -ErrorAction SilentlyContinue | Stop-Process -Force
   Start-Process "ollama" -ArgumentList "serve"
   ```

2. **Restart Cursor IDE**: Close and reopen Cursor to reset the agent backend connection.

3. **Run Diagnostic Script**:
   ```powershell
   cd c:\Users\mlesn\Dropbox\my_projects\.lumina
   python scripts/python/diagnose_cursor_connection.py
   ```

4. **Verify Model Availability**:
   ```powershell
   ollama list
   # If models missing:
   ollama pull qwen2.5-coder:7b
   ollama pull qwen2-72b:latest
   ```

### Long-term Solutions

1. **Add Pre-flight Checks**: Create a startup script that verifies Ollama is running before Cursor starts.

2. **Implement Fallback Models**: Configure fallback to cloud models if local Ollama fails.

3. **Monitor Connection Health**: Set up periodic health checks and alerts.

4. **Optimize Model Configuration**: Adjust timeout and token limits based on your hardware capabilities.

## Prevention

1. **Auto-start Ollama**: Configure Ollama to start automatically with Windows.

2. **Health Check Automation**: Run diagnostic script on Cursor startup.

3. **Configuration Validation**: Validate settings.json on workspace load.

4. **Connection Pooling**: Implement connection pooling for better reliability.

## Related Documentation

- `docs/system/CURSOR_MODEL_CONNECTION_FIX.md`
- `docs/system/CONNECTION_ERRORS_AND_CURSOR_STABILITY_FIXES.md`
- `config/cursor_ultron_model_config.json`

## Status

- [ ] Diagnostic script created
- [ ] Settings.json updated with timeout configuration
- [ ] Ollama service verified running
- [ ] Models verified available
- [ ] Connection tested and working
- [ ] Workflow recovery verified

---

**Last Updated**: 2026-01-28
**Request ID**: a2155803-eda4-4daf-88ef-927515c31d0c
