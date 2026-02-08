# ULTRON Agent Model Setup for Cursor IDE

## ✅ Configuration Complete

ULTRON has been configured for Cursor IDE's agent/composer model dropdown. The following configurations have been added:

### 1. Agent Models (`cursor.agent.customModels`)
- **ULTRON** - Local Docker/WSL Kali Linux (`http://localhost:11434`)
- **ULTRON Router** - Smart routing (`http://10.17.17.32:3008`)

### 2. Composer Models (`cursor.composer.customModels`)
- **ULTRON Cluster (Local Docker/WSL)** - Primary ULTRON instance
- **ULTRON Router (Smart Routing)** - Hybrid routing
- **KAIJU Iron Legion** - NAS-based models

### 3. Chat Models (`cursor.chat.customModels`)
- **ULTRON Cluster** - For chat interface
- **ULTRON Router** - For chat interface
- **KAIJU Iron Legion** - For chat interface

### 4. General Models (`cursor.model.customModels`)
- **ULTRON Cluster (Qwen2.5 72B)** - General purpose
- **ULTRON Router (Smart Routing)** - Routing-enabled
- **KAIJU Iron Legion** - NAS models

## How to Access ULTRON in Cursor

### Method 1: Agent/Composer Panel
1. Open Cursor IDE
2. Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac) to open Composer
3. Click on the model dropdown at the top
4. **ULTRON** should appear in the list
5. Select **ULTRON** to use it

### Method 2: Settings UI
1. Press `Ctrl+,` (or `Cmd+,` on Mac) to open Settings
2. Search for "models" or "ollama"
3. Find "Custom Models" section
4. Verify ULTRON is listed

### Method 3: Restart Cursor
After configuration, restart Cursor IDE to ensure all settings are loaded:
1. Close Cursor completely
2. Reopen Cursor
3. ULTRON should now be available in all model dropdowns

## Verification

Run the verification script:
```bash
python scripts/python/verify_ultron_cursor_config.py
```

This will check:
- ✅ Model configurations in all sections
- ✅ Ollama endpoint configuration
- ✅ Model availability

## Troubleshooting

### ULTRON Not Appearing in Dropdown

1. **Check Ollama is Running:**
   ```bash
   # Test connection
   curl http://localhost:11434/api/tags
   
   # If not running, start it
   ollama serve
   ```

2. **Verify Model is Available:**
   ```bash
   ollama list
   # Should show qwen2.5:72b
   ```

3. **Check Cursor Settings:**
   - Open Settings (`Ctrl+,`)
   - Search for "ollama"
   - Verify endpoint is: `http://localhost:11434`

4. **Restart Cursor:**
   - Sometimes settings require a full restart
   - Close completely and reopen

### Docker/WSL Access

If ULTRON is running in Docker or WSL:

1. **Docker:**
   ```bash
   # Check if container is running
   docker ps | grep ollama
   
   # If port mapping is different, update apiBase in settings.json
   ```

2. **WSL:**
   ```bash
   # From WSL, check if Ollama is accessible
   wsl curl http://localhost:11434/api/tags
   
   # May need to use WSL IP address instead of localhost
   # Update apiBase in settings.json with WSL IP
   ```

### Alternative Endpoint Configuration

If running in Docker/WSL with port forwarding:
- Update `apiBase` in all model configurations
- Use `http://127.0.0.1:11434` instead of `localhost`
- Or use WSL IP: `http://<WSL_IP>:11434`

## Configuration Files

- **Cursor Settings:** `.cursor/settings.json`
- **ULTRON Config:** `config/cursor_ultron_model_config.json`
- **Verification Script:** `scripts/python/verify_ultron_cursor_config.py`

## Next Steps

1. ✅ Configuration added to `.cursor/settings.json`
2. ⏭️ **Restart Cursor IDE** (required)
3. ⏭️ Open Composer (`Ctrl+I`) and select ULTRON from dropdown
4. ⏭️ Test with a simple prompt to verify it's working

---

**Status:** ✅ Configured - Ready for testing after Cursor restart
