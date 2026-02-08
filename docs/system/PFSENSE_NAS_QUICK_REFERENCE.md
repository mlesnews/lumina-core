# pfSense and NAS Quick Reference

## Quick Access URLs

### pfSense
- **Web Portal:** https://10.17.17.1
- **SSH:** `ssh admin@10.17.17.1`
- **Ports:** 443 (HTTPS), 22 (SSH)

### NAS (Synology DSM)
- **Web Portal (HTTPS):** https://10.17.17.32:5001
- **Web Portal (HTTP):** http://10.17.17.32:5000
- **SSH:** `ssh backupadm@10.17.17.32`
- **API:** http://10.17.17.32:5001/webapi
- **Ports:** 5001 (HTTPS), 5000 (HTTP), 22 (SSH)

## Credentials

All credentials stored in Azure Key Vault: `jarvis-lumina`

- **pfSense Password:** `pfsense-password`
- **NAS Password:** `nas-password`

## Quick Test Commands

### PowerShell - Test All Connections
```powershell
.\scripts\powershell\Test-PFSenseAndNASConnections.ps1
```

### Python - pfSense
```bash
# Test web portal
python scripts/python/pfsense_azure_vault_integration.py --test

# Test web login
python scripts/python/pfsense_azure_vault_integration.py --test-web

# Test SSH
python scripts/python/pfsense_azure_vault_integration.py --ssh-test

# Execute SSH command
python scripts/python/pfsense_azure_vault_integration.py --ssh "uptime"
```

### Python - NAS
```bash
# Test SSH
python scripts/python/nas_azure_vault_integration.py --ssh-test

# Test API
python scripts/python/nas_azure_vault_integration.py --test

# Execute SSH command
python scripts/python/nas_azure_vault_integration.py --ssh "df -h"
```

## Configuration Files

- **pfSense:** `config/lumina_pfsense_ssh_config.json`
- **NAS:** `config/lumina_nas_ssh_config.json`

## Documentation

- **pfSense:** `docs/system/LUMINA_PFSENSE_SSH_WEB_PORTAL.md`
- **NAS:** `docs/system/LUMINA_NAS_SSH_API.md`

## Common Operations

### pfSense
- View firewall status: `pfctl -s info`
- Check system uptime: `uptime`
- View network interfaces: `ifconfig`
- View routing table: `netstat -rn`

### NAS
- Check disk usage: `df -h`
- List files: `ls -la /volume1/backups`
- System info: `uname -a`
- Check services: `systemctl status`

## Troubleshooting

### Connection Issues
1. Verify network connectivity: `Test-Connection <IP>`
2. Check credentials in Key Vault
3. Verify services are enabled (SSH, web portal)
4. Check firewall rules

### Credential Issues
```powershell
# Check pfSense password
az keyvault secret show --vault-name jarvis-lumina --name pfsense-password

# Check NAS password
az keyvault secret show --vault-name jarvis-lumina --name nas-password
```

