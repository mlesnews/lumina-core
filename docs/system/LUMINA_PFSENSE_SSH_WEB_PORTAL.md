# Lumina pfSense SSH and Web Portal Integration

## Overview

pfSense is integrated with Lumina via SSH for secure command-line access and web portal for GUI-based management.

**Source of Truth:** `config/lumina_pfsense_ssh_config.json`

## Configuration

### SSH Access
- **Host:** `10.17.17.1`
- **Port:** `22`
- **Username:** `admin`
- **Password:** Retrieved from Azure Key Vault (`jarvis-lumina` → `pfsense-password`)
- **Authentication:** Password-based (from Key Vault)

### Web Portal Access
- **URL:** `https://10.17.17.1`
- **Port:** `443`
- **Username:** `admin`
- **Password:** Retrieved from Azure Key Vault (`jarvis-lumina` → `pfsense-password`)
- **SSL Verification:** Disabled (self-signed certificate)

### Lumina Integration
- **R5 System:** pfSense operations published to R5 Living Context Matrix
- **Memory Manager:** pfSense operations stored in memory
- **Droid Actor System:** pfSense operations can trigger droid workflows
- **API Endpoint:** `http://localhost:8000`

## Usage

### Python API

```python
from scripts.python.pfsense_azure_vault_integration import PFSenseAzureVaultIntegration

# Initialize integration
pfsense = PFSenseAzureVaultIntegration(vault_name="jarvis-lumina", pfsense_ip="10.17.17.1")

# Test web portal connection
if pfsense.test_web_portal_connection():
    print("Web portal is accessible")

# Login to web portal
if pfsense.login_web_portal():
    print("Successfully logged in")

# Execute SSH command
result = pfsense.execute_ssh_command("uptime")
if result["success"]:
    print(result["output"])

# Get SSH client for advanced operations
ssh_client = pfsense.get_ssh_client()
if ssh_client:
    stdin, stdout, stderr = ssh_client.exec_command("pfctl -s info")
    print(stdout.read().decode('utf-8'))
    ssh_client.close()
```

### Command Line

```bash
# Test web portal connection
python scripts/python/pfsense_azure_vault_integration.py --test

# Test web portal login
python scripts/python/pfsense_azure_vault_integration.py --test-web

# Test SSH connection
python scripts/python/pfsense_azure_vault_integration.py --ssh-test

# Execute SSH command
python scripts/python/pfsense_azure_vault_integration.py --ssh "uptime"

# Execute multiple commands
python scripts/python/pfsense_azure_vault_integration.py --ssh "pfctl -s info"
```

### PowerShell Testing

```powershell
# Test all connections (pfSense and NAS)
.\scripts\powershell\Test-PFSenseAndNASConnections.ps1

# Test with custom vault
.\scripts\powershell\Test-PFSenseAndNASConnections.ps1 -VaultName "my-vault"
```

## Operations

### SSH Commands

Common pfSense SSH commands:
- `uptime` - System uptime
- `pfctl -s info` - Firewall information
- `ifconfig` - Network interface configuration
- `netstat -rn` - Routing table
- `top` - System processes
- `df -h` - Disk usage

### Web Portal

Access the web portal at `https://10.17.17.1` for:
- Firewall rule management
- Traffic monitoring
- Network configuration
- VPN setup
- System status
- Logs and diagnostics

## Lumina Integration

### R5 System Integration

pfSense operations are automatically published to Lumina API:

```json
{
  "event_type": "pfsense_ssh_command",
  "source": "pfsense_azure_vault",
  "data": {
    "command": "uptime",
    "result": {
      "success": true,
      "output": "...",
      "exit_status": 0
    }
  }
}
```

### Memory Manager Integration

pfSense operations are stored in memory:
- SSH command history
- Web portal login events
- System status checks
- Network diagnostics

## Prerequisites

### Azure Key Vault Setup

Ensure pfSense password is stored in Key Vault:

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name pfsense-password `
    --value "YOUR_PFSENSE_PASSWORD"
```

### Python Dependencies

```bash
pip install azure-keyvault-secrets azure-identity paramiko requests
```

### pfSense Configuration

1. **Enable SSH on pfSense:**
   - Navigate to System → Advanced → Admin Access
   - Enable SSH
   - Configure SSH port (default: 22)

2. **Verify Web Portal:**
   - Access `https://10.17.17.1`
   - Verify SSL certificate (may need to accept self-signed cert)

3. **Network Connectivity:**
   - Ensure workstation can reach pfSense IP
   - Firewall rules allow SSH (port 22) and HTTPS (port 443)

## Troubleshooting

### SSH Connection Issues

1. **Check SSH is enabled on pfSense:**
   ```bash
   # From pfSense web portal: System → Advanced → Admin Access
   # Enable SSH service
   ```

2. **Verify network connectivity:**
   ```powershell
   Test-Connection 10.17.17.1
   ```

3. **Test SSH manually:**
   ```bash
   ssh admin@10.17.17.1
   ```

4. **Verify credentials in Key Vault:**
   ```powershell
   az keyvault secret show --vault-name jarvis-lumina --name pfsense-password
   ```

### Web Portal Issues

1. **Check web portal accessibility:**
   ```powershell
   Invoke-WebRequest -Uri "https://10.17.17.1" -SkipCertificateCheck
   ```

2. **Verify SSL certificate:**
   - pfSense uses self-signed certificates by default
   - Browser may require accepting certificate warning

3. **Check firewall rules:**
   - Ensure HTTPS (port 443) is allowed

## Security Notes

- **SSH Access:** Use strong passwords and consider key-based authentication
- **Web Portal:** Use HTTPS and consider restricting access by IP
- **Credentials:** Never hardcode passwords - always use Azure Key Vault
- **Network:** Consider VPN access for remote management

## Related Documentation

- `config/lumina_pfsense_ssh_config.json` - SSoT configuration
- `scripts/python/pfsense_azure_vault_integration.py` - SSH client and web portal integration
- `scripts/powershell/Test-PFSenseAndNASConnections.ps1` - Connection testing script
- `docs/system/LUMINA_NAS_SSH_API.md` - NAS integration documentation

