# User Preferences & Memory

**Date**: 2026-01-02  
**Status**: ✅ ACTIVE

## Critical Preferences (+++++)

### Azure Key Vault for Credentials (+++++)
**IMPORTANCE**: CRITICAL (Level 5)  
**Status**: ALWAYS USE

**Rule**: Always use Azure Key Vault for retrieving credentials. Never hardcode or use default credentials.

**Implementation**:
- Use `NASAzureVaultIntegration` class for NAS credentials
- All scripts should retrieve credentials from Azure Key Vault
- Credentials are cached in-memory with 30-minute TTL (matching NAS proxy-cache retention)
- Vault name: `jarvis-lumina`
- Secrets: `nas-username`, `nas-password`

**Examples**:
- ✅ NAS migration scripts: Retrieve from Azure Vault
- ✅ SSH connections: Use credentials from Azure Vault
- ✅ SMB mappings: Use credentials from Azure Vault
- ❌ Hardcoded passwords
- ❌ Environment variables for sensitive credentials
- ❌ Default/prompted credentials

**Tags**: @AZURE @VAULT @CREDENTIALS @SECURITY

---

## Rating System

Importance ratings using plus signs (similar to 1-5 star rating system):

- `+` = Level 1 - Low importance
- `++` = Level 2 - Below average importance  
- `+++` = Level 3 - Medium/average importance
- `++++` = Level 4 - High importance
- `+++++` = Level 5 - Critical/highest importance

**Usage**: When creating memories or documenting preferences, use the plus rating system:
```
Example: "Always use Azure Key Vault for credentials (+++++)"
```

---

**Tag**: @MEMORY @PREFERENCES @RATING
