# 🔍 KAIJU Iron Legion Cluster - SSH Diagnostics

## Critical Finding

**❌ All KAIJU endpoints are inaccessible from local machine:**
- `http://10.17.17.32:11434` - Connection refused
- `http://10.17.17.32:11437` - Connection refused  
- `http://10.17.17.32:3008` - Connection refused
- `http://kaiju_no_8:11434` - Connection timeout
- `http://lesnewski.local:11437` - DNS resolution failed

**This is likely the root cause** - Cursor can't reach KAIJU, so it's falling back to incorrect model configuration.

## SSH Into KAIJU

### Step 1: Connect via SSH

```bash
# Try one of these (adjust username as needed):
ssh admin@10.17.17.32
ssh mlesn@10.17.17.32
ssh lesnewski@10.17.17.32

# Or using hostname:
ssh admin@kaiju_no_8
```

### Step 2: Run Diagnostic Commands

Once connected, run these commands on KAIJU:

#### Check Ollama Service Status
```bash
systemctl status ollama || service ollama status || ps aux | grep ollama
```

#### Check Listening Ports
```bash
netstat -tuln | grep -E '11434|11437|3008' || ss -tuln | grep -E '11434|11437|3008'
```

#### Check Docker Containers (if using Docker)
```bash
docker ps | grep -i ollama || docker ps -a | grep -i ollama
```

#### List Available Models
```bash
ollama list || /usr/local/bin/ollama list || ~/.local/bin/ollama list
```

#### Test Ollama API Locally
```bash
curl -s http://localhost:11434/api/tags | head -50
```

#### Check Ollama Process
```bash
ps aux | grep -i ollama | grep -v grep
```

#### Check Network Configuration
```bash
ip addr show || ifconfig
```

## Quick Diagnostic Script

A diagnostic script has been created: `scripts/python/kaiju_diagnostics.sh`

**To use it:**
1. Transfer the script to KAIJU (via SCP or copy-paste)
2. Make it executable: `chmod +x kaiju_diagnostics.sh`
3. Run it: `bash kaiju_diagnostics.sh`

## Expected Findings & Solutions

### Scenario 1: Ollama Not Running
**Symptom**: `ps aux | grep ollama` shows nothing

**Solution**:
```bash
# If using systemd:
sudo systemctl start ollama
sudo systemctl enable ollama

# If using Docker:
docker-compose up -d
# or
docker start ollama-container

# If installed manually:
ollama serve &
```

### Scenario 2: Ollama Running But Wrong Port
**Symptom**: Ollama is running but on different port

**Check**:
```bash
netstat -tuln | grep ollama
```

**Solution**: Update Cursor settings to use correct port, or reconfigure Ollama to use standard port (11434)

### Scenario 3: Ollama Only Listening on localhost
**Symptom**: `curl localhost:11434/api/tags` works, but external access fails

**Solution**: Configure Ollama to listen on all interfaces:
```bash
# Edit Ollama config or start with:
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

### Scenario 4: Firewall Blocking
**Symptom**: Ollama running, but ports not accessible externally

**Solution**: Check and update firewall rules:
```bash
# Check firewall
iptables -L -n | grep -E '11434|11437|3008'

# If using Synology, check DSM Firewall settings
```

### Scenario 5: No Models Installed
**Symptom**: Ollama running but `ollama list` shows no models

**Solution**: Pull required models:
```bash
ollama pull llama3
ollama pull codellama:13b
ollama pull llama3.2:11b
# ... etc
```

## After Fixing on KAIJU

1. **Verify from KAIJU**:
   ```bash
   curl http://localhost:11434/api/tags
   ```

2. **Test from local machine**:
   ```bash
   curl http://10.17.17.32:11434/api/tags
   ```

3. **Update Cursor** (if needed):
   - If port changed, update `.cursor/settings.json`
   - Restart Cursor
   - Test in Chat

## Root Cause Analysis

The "Iron Legion" model error is likely caused by:
1. **KAIJU cluster is down/not accessible** ← **Most likely**
2. Cursor falls back to cached/incorrect configuration
3. Cursor tries to use "Iron Legion" as model name instead of actual model

**Once KAIJU is accessible, the error should resolve.**

---

**Created**: 2025-12-31  
**Status**: Active - Ready for SSH diagnostics
