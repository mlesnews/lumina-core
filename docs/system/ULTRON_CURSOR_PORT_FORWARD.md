# ULTRON Cursor Port Forward Setup

## Mission
Enable ULTRON in Cursor IDE by forwarding KAIJU Iron Legion API through localhost to bypass Cursor's IP validation.

## Architecture

```
Cursor IDE → localhost:11435 → SSH Tunnel → KAIJU (10.17.17.11:3001) → Iron Legion API
```

## Current Status

✅ **Network Connectivity**: KAIJU accessible  
✅ **Cursor Config**: Updated to use `localhost:11435`  
⚠️ **Port Forward**: Needs manual SSH setup (authentication required)

## Manual Setup Steps

### Option 1: SSH Key Authentication (Recommended)

1. **Generate SSH key** (if not exists):
   ```powershell
   ssh-keygen -t ed25519 -f $env:USERPROFILE\.ssh\id_ed25519_kaiju
   ```

2. **Copy key to KAIJU**:
   ```powershell
   type $env:USERPROFILE\.ssh\id_ed25519_kaiju.pub | ssh 10.17.17.11 "cat >> ~/.ssh/authorized_keys"
   ```

3. **Start port forward**:
   ```powershell
   ssh -N -L 11435:localhost:3001 -i $env:USERPROFILE\.ssh\id_ed25519_kaiju 10.17.17.11
   ```

### Option 2: Password Authentication

```powershell
ssh -N -L 11435:localhost:3001 10.17.17.11
# Enter password when prompted
```

### Option 3: Windows Service (Persistent)

Create a scheduled task or Windows service to auto-start the port forward on boot.

## Verification

```powershell
# Test localhost endpoint
curl.exe http://localhost:11435/

# Should return:
# {"service":"Iron Legion llama.cpp - codellama:13b",...}

# Test models endpoint
curl.exe http://localhost:11435/v1/models

# Should return:
# {"object":"list","data":[{"id":"codellama:13b",...}]}
```

## Cursor Configuration

Already configured in `settings.json`:
```json
{
  "name": "ULTRON",
  "provider": "openai",
  "model": "codellama:13b",
  "apiBase": "http://localhost:11435/v1",
  "apiKey": "",
  "localOnly": true
}
```

## Troubleshooting

### Port 11435 shows "Ollama is running"
- **Issue**: Port forward pointing to wrong service
- **Fix**: Stop existing process, restart with correct port (3001)

### SSH connection fails
- **Issue**: Authentication required
- **Fix**: Set up SSH keys or use password authentication

### Cursor still shows "Invalid Model"
- **Issue**: Cursor validation
- **Fix**: Reload Cursor (Ctrl+R), verify localhost:11435 is accessible

## Network Team Coordination

### pfSense Firewall Rules
- **Status**: ✅ Port 3001 accessible from laptop (10.17.17.191)
- **Rule**: LAN to LAN pass rule exists
- **Action**: No changes needed

### Infrastructure Architecture
- **Port Forward**: SSH tunnel localhost:11435 → KAIJU:3001
- **Service**: Iron Legion llama.cpp API
- **Status**: Manual setup required (SSH auth)

## Next Steps

1. ✅ Cursor config updated
2. ⚠️ **Manual**: Set up SSH authentication to KAIJU
3. ⚠️ **Manual**: Start SSH port forward
4. ✅ Reload Cursor IDE (`Ctrl+Shift+P` to reload window)
5. ✅ Test ULTRON model selection

**Note**: `Ctrl+Shift+P` reloads Cursor window. `Ctrl+R` spawns a new AI AGENT Chat window.

## Files

- Port Forward Script: `scripts/kaiju_port_forward_service.ps1`
- Network Coordinator: `scripts/python/ultron_cursor_network_coordinator.py`
- Documentation: `docs/system/ULTRON_CURSOR_PORT_FORWARD.md`
