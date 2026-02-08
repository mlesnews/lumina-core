# SSH Connections Audit

## Overview

Audit of all SSH connections in the codebase to ensure password-only authentication is properly configured.

## SSH Connections Status

### ✅ Fixed (Password-Only Auth)

1. **`nas_azure_vault_integration.py`** (line 313-323)
   - ✅ `allow_agent=False, look_for_keys=False`
   - ✅ Password from Azure Key Vault

2. **`nas_migration_status.py`** (line 69-78)
   - ✅ `allow_agent=False, look_for_keys=False`
   - ✅ Password authentication

3. **`verify_nas_cron_tasks.py`** (line 62-73, 176-186)
   - ✅ `allow_agent=False, look_for_keys=False`
   - ✅ Password authentication

4. **`nas_kron_daemon_manager.py`** (line 185-191, 315-321)
   - ✅ `allow_agent=False, look_for_keys=False`
   - ✅ Password authentication (with key_filename fallback)

5. **`jarvis_storage_engineering_team.py`** (line 180-188, 258-266)
   - ✅ `allow_agent=False, look_for_keys=False` (FIXED)
   - ✅ Password authentication

6. **`nas_physics_cache.py`** (line 187-196, 235-244)
   - ✅ `allow_agent=False, look_for_keys=False`
   - ✅ Password authentication

### ⚠️ Needs Review

1. **`physics_matrix_engine.py`** (line 90, 108)
   - ⚠️ Need to verify if password-only flags are present
   - Location: SSH connections for physics matrix operations

2. **`deploy_nas_migration.py`** (line 131-144)
   - ⚠️ Has key_filename option with password fallback
   - May need to ensure password-only is default

## Configuration Files

### ✅ NAS SSH Config
- **File**: `config/lumina_nas_ssh_config.json`
- **Auth**: Password-only (`preferred_auth: "password"`)
- **Key Path**: `null`

### ✅ pfSense SSH Config
- **File**: `config/lumina_pfsense_ssh_config.json`
- **Auth**: Password-only (`preferred_auth: "password"`)
- **Key Path**: `null`

## Standard Pattern

All SSH connections should follow this pattern:

```python
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname=host,
    port=port,
    username=username,
    password=password,
    timeout=30,
    allow_agent=False,      # Disable SSH agent (prevents publickey attempts)
    look_for_keys=False     # Don't look for SSH keys (password-only auth)
)
```

## Sudoless Root Access

### Configuration Status
- **NAS**: Password-only auth configured
- **pfSense**: Password-only auth configured
- **KAIJU**: Needs verification
- **Other HOMELAB**: Needs verification

### Notes
- Sudoless root access typically requires:
  - User in sudoers file with NOPASSWD
  - Or direct root user access
  - Or specific group memberships (e.g., docker group)

## RDP Async @FF Testing

### Status
- **File**: `scripts/python/manus_keyboard_rdp_recording_workflow.py`
- **Purpose**: Record keyboard shortcuts during RDP sessions
- **Testing**: Needs verification

## Next Steps

1. ✅ Verify `physics_matrix_engine.py` SSH connections
2. ✅ Review `deploy_nas_migration.py` key_filename usage
3. ⚠️ Document sudoless root access configuration
4. ⚠️ Verify RDP async @ff testing status

## Tags

@HOMELAB #SSH #AUDIT #PASSWORD_AUTH #SUDOLESS_ROOT #RDP
