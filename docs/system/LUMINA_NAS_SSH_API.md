# Lumina NAS SSH and API Integration

## Overview

NAS is integrated with Lumina via SSH for secure access and API integration for AI/automation.

**Source of Truth:** `config/lumina_nas_ssh_config.json`

## Configuration

### SSH Access
- **Host:** `10.17.17.32`
- **Port:** `22`
- **Username:** `backupadm`
- **Password:** Retrieved from Azure Key Vault (`jarvis-lumina` → `nas-password`)
- **Authentication:** Password-based (from Key Vault)

### Lumina Integration
- **R5 System:** NAS operations published to R5 Living Context Matrix
- **Memory Manager:** NAS operations stored in memory
- **Droid Actor System:** NAS operations can trigger droid workflows
- **API Endpoint:** `http://localhost:8000`

## Usage

### Python API

```python
from scripts.python.nas_azure_vault_integration import NASAzureVaultIntegration

# Initialize integration
nas = NASAzureVaultIntegration(vault_name="jarvis-lumina", nas_ip="10.17.17.32")

# Execute SSH command
result = nas.execute_ssh_command("df -h")
if result["success"]:
    print(result["output"])
else:
    print(f"Error: {result.get('error')}")

# Get SSH client for advanced operations
ssh_client = nas.get_ssh_client()
if ssh_client:
    # Use paramiko client directly for advanced operations
    stdin, stdout, stderr = ssh_client.exec_command("ls -la /volume1/backups")
    print(stdout.read().decode('utf-8'))
    ssh_client.close()
```

### Command Line

```bash
# Test SSH connection
python scripts/python/nas_azure_vault_integration.py --ssh-test

# Execute SSH command
python scripts/python/nas_azure_vault_integration.py --ssh "df -h"

# Execute multiple commands
python scripts/python/nas_azure_vault_integration.py --ssh "ls -la /volume1/backups"

# Test NAS API connection (Synology)
python scripts/python/nas_azure_vault_integration.py --test

# Upload file via NAS API
python scripts/python/nas_azure_vault_integration.py --upload file.txt --target /backups/MATT_Backups
```

## Lumina API Integration

### Event Publishing

NAS operations are automatically published to Lumina API:

**Event Types:**
- `nas_ssh_connected` - When SSH connection is established
- `nas_command_executed` - When commands are executed
- `nas_file_operation` - When file operations occur

**Example Event:**
```json
{
  "event_type": "nas_command_executed",
  "source": "nas_ssh",
  "data": {
    "command": "df -h",
    "result": {
      "success": true,
      "output": "...",
      "exit_status": 0
    }
  }
}
```

### R5 System Integration

NAS operations are aggregated into R5 Living Context Matrix:
- Command history
- File operations
- System status
- Resource usage

### Memory Manager Integration

NAS operations are stored in memory:
- Short-term: Recent operations
- Long-term: Important patterns and configurations
- Working: Current active operations

## Prerequisites

### 1. Install Dependencies

```powershell
pip install paramiko requests
```

### 2. Azure Key Vault Setup

Ensure NAS password is stored in Key Vault:
```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name nas-password `
    --value "PASSWORD"
```

### 3. SSH Access

- NAS must have SSH enabled
- Port 22 must be accessible
- User `backupadm` must have SSH access

## Security

### Authentication
- Password stored securely in Azure Key Vault
- Never hardcoded in scripts
- Retrieved at runtime

### Connection Security
- SSH encryption for all communications
- Auto-add host key (for initial connection)
- Configurable timeout

## Operations

### File Operations
- List directories
- Get file information
- Transfer files (SFTP)
- Monitor file changes

### System Operations
- Check disk usage
- Monitor services
- System health checks
- Resource monitoring

### Backup Operations
- Automated backups
- Backup verification
- Retention management

## Integration Points

### Lumina API Server
- Endpoint: `http://localhost:8000`
- Events published to `/r5/events`
- Operations logged and aggregated

### R5 Living Context Matrix
- NAS operations aggregated
- Patterns extracted
- Knowledge condensed

### Memory Manager
- Operations stored
- Context maintained
- Patterns learned

## Troubleshooting

### Connection Failed

1. **Check NAS SSH is enabled:**
   ```bash
   # From NAS admin interface, enable SSH service
   ```

2. **Verify network connectivity:**
   ```powershell
   Test-Connection 10.17.17.32
   Test-NetConnection -ComputerName 10.17.17.32 -Port 22
   ```

3. **Check credentials:**
   ```powershell
   # Verify password in Key Vault
   az keyvault secret show --vault-name jarvis-lumina --name nas-password
   ```

### Password Not Retrieved

1. **Check Azure login:**
   ```powershell
   az account show
   ```

2. **Verify Key Vault access:**
   ```powershell
   az keyvault show --name jarvis-lumina
   ```

3. **Check secret exists:**
   ```powershell
   az keyvault secret list --vault-name jarvis-lumina
   ```

## Related Files

- `config/lumina_nas_ssh_config.json` - SSoT configuration
- `scripts/python/nas_ssh_lumina_integration.py` - SSH client and API integration
- `config/lumina_network_drives.json` - Network drive mapping (SMB)
- `docs/system/LUMINA_NAS_SSH_API.md` - This documentation

---

**Last Updated:** 2025-01-24  
**Maintained By:** Lumina Project Team

