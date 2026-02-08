# ProtonPass-CLI Full Utilization Plan

**Date**: 2025-01-24  
**Status**: ⚠️ **SEVERELY UNDERUTILIZED** (1% usage - availability check only)  
**Goal**: 🎯 **100% Utilization** - Enterprise-grade password management  
**Tag**: #leverage

---

## Current State Assessment

### ❌ **Current Usage: 1%**

**Only Available Feature**:
- Basic availability check: `protonpass --version`

**Missing Features (99%)**:
- ❌ Password management (create, get, update, list, delete)
- ❌ Secure notes (create, get, update)
- ❌ Credit card management
- ❌ Authentication (login, logout, 2FA)
- ❌ Export/Import operations
- ❌ Security analysis & intelligence
- ❌ Automated password rotation
- ❌ Integration with Azure Key Vault
- ❌ Integration with existing workflows

### ✅ **What Exists**

1. **Comprehensive Implementation**: `scripts/python/protonpass_manager.py`
   - Full `ProtonPassManager` class with all capabilities
   - 500+ lines of implementation
   - **Status**: Exists but NOT integrated

2. **Analysis Documents**:
   - `protonpasscli_utilization_analysis.md` - Detailed capability analysis
   - `protonpasscli_final_assessment.md` - Assessment confirming 1% usage

3. **Azure Key Vault Infrastructure**:
   - Key Vault client exists (`AzureKeyVaultClient`)
   - **Policy**: All secrets MUST use Azure Key Vault

---

## Recommended Architecture: UnifiedSecretManager

### Dual Storage Strategy (ProtonPass + Azure Key Vault)

**Rationale**:
- **ProtonPass**: Zero-knowledge encryption, personal/private credentials
- **Azure Key Vault**: Enterprise compliance, audit trails, organizational secrets
- **Dual Storage**: Redundancy, compliance, flexibility

```python
class UnifiedSecretManager:
    """
    Unified secret management with ProtonPass + Azure Key Vault
    
    Strategy:
    - Personal/Private secrets → ProtonPass (zero-knowledge)
    - Organizational/Enterprise secrets → Azure Key Vault (compliance)
    - Critical secrets → Both (redundancy)
    """
    
    def __init__(self):
        self.proton_pass = ProtonPassManager()
        self.azure_vault = AzureKeyVaultClient(
            vault_url="https://jarvis-lumina.vault.azure.net/"
        )
        self.secret_mapping = {
            # Personal secrets → ProtonPass
            "github-personal-token": "protonpass",
            "aws-personal-credentials": "protonpass",
            
            # Enterprise secrets → Azure Key Vault
            "azure-openai-api-key": "azure",
            "service-bus-connection": "azure",
            "database-connection": "azure",
            
            # Critical secrets → Both
            "master-encryption-key": "both",
            "nas-credentials": "both"
        }
```

---

## Implementation Plan

### Phase 1: Installation & Setup (Priority: HIGH)

1. **Install ProtonPassCLI**
   ```powershell
   # Check if installed
   where.exe protonpass
   
   # If not installed, install via:
   # https://github.com/ProtonPass/protonpass-cli
   # Windows: Download from releases
   # Linux: Use package manager or install script
   ```

2. **Login to ProtonPass**
   ```bash
   protonpass login --username your@proton.me
   ```

3. **Verify Installation**
   ```python
   from scripts.python.protonpass_manager import ProtonPassManager
   manager = ProtonPassManager()
   if manager.cli_available:
       print("✅ ProtonPassCLI ready")
   ```

---

### Phase 2: UnifiedSecretManager Implementation (Priority: HIGH)

**File**: `scripts/python/unified_secret_manager.py`

**Features**:
- Dual storage (ProtonPass + Azure Key Vault)
- Intelligent routing based on secret type
- Fallback mechanisms
- Audit logging
- Secret rotation automation

**Integration Points**:
- Replace hardcoded secrets in code
- Integrate with JARVIS workflows
- Connect to SYPHON intelligence
- Enable automated rotation

---

### Phase 3: Integration with Existing Systems (Priority: MEDIUM)

1. **JARVIS Integration**
   - Replace hardcoded API keys
   - Use `UnifiedSecretManager.get_secret()` instead of config values

2. **SYPHON Integration**
   - Store extracted credentials in ProtonPass
   - Intelligence-driven password security analysis

3. **Azure Services Integration**
   - Keep enterprise secrets in Azure Key Vault
   - Use ProtonPass for personal/development credentials

4. **Cursor IDE Integration**
   - Retrieve secrets from ProtonPass for Cursor settings
   - Automate credential updates

---

### Phase 4: Advanced Features (Priority: LOW)

1. **Automated Password Rotation**
   - Schedule-based rotation
   - Security event-triggered rotation
   - Integration with ProtonPass rotation APIs

2. **Security Intelligence**
   - Weak password detection
   - Reused password analysis
   - Breach monitoring integration
   - Security scoring

3. **Backup & Disaster Recovery**
   - Automated ProtonPass exports
   - Encrypted backups to NAS
   - Restoration workflows

---

## Migration Strategy

### Step 1: Identify All Secrets

**Current Secret Locations**:
- `config/*.json` files
- Environment variables
- Hardcoded in code
- `.env` files (if any)

**Action**: Scan codebase for:
- API keys
- Passwords
- Tokens
- Connection strings
- Certificates

### Step 2: Categorize Secrets

**ProtonPass (Personal/Private)**:
- GitHub personal access tokens
- AWS personal credentials
- Personal API keys
- Development credentials

**Azure Key Vault (Enterprise)**:
- Azure OpenAI API keys
- Service Bus connections
- Database credentials
- Organizational secrets

**Both (Critical/Redundant)**:
- Master encryption keys
- NAS credentials
- Critical service credentials

### Step 3: Migrate Secrets

1. **Store in ProtonPass** (personal secrets):
   ```python
   manager = ProtonPassManager()
   manager.create_password(
       name="github-personal-token",
       username="mlesnews",
       password="ghp_xxx...",
       url="https://github.com"
   )
   ```

2. **Store in Azure Key Vault** (enterprise secrets):
   ```powershell
   az keyvault secret set `
       --vault-name jarvis-lumina `
       --name azure-openai-api-key `
       --value "xxx..."
   ```

3. **Update Code**:
   ```python
   # OLD (hardcoded)
   api_key = "hardcoded-key"
   
   # NEW (unified manager)
   from scripts.python.unified_secret_manager import UnifiedSecretManager
   secrets = UnifiedSecretManager()
   api_key = secrets.get_secret("azure-openai-api-key")
   ```

---

## Benefits of Full Utilization

### Security Benefits
- ✅ Zero-knowledge encryption (ProtonPass)
- ✅ Enterprise compliance (Azure Key Vault)
- ✅ Audit trails and access logs
- ✅ Automated rotation
- ✅ Breach detection integration

### Operational Benefits
- ✅ Centralized secret management
- ✅ No hardcoded secrets in code
- ✅ Automated credential updates
- ✅ Disaster recovery capabilities
- ✅ Developer-friendly API

### Compliance Benefits
- ✅ Azure Key Vault meets enterprise requirements
- ✅ ProtonPass provides zero-knowledge privacy
- ✅ Dual storage for redundancy
- ✅ Audit logging for compliance

---

## Quick Start: Get ProtonPassCLI Working

### 1. Check Installation
```powershell
where.exe protonpass
```

### 2. If Not Installed
- **Windows**: Download from https://github.com/ProtonPass/protonpass-cli/releases
- **Linux/Mac**: Follow installation instructions at https://github.com/ProtonPass/protonpass-cli

### 3. Test Installation
```python
python scripts/python/protonpass_manager.py
```

### 4. Login
```bash
protonpass login --username your@proton.me
```

### 5. Test Basic Operations
```python
from scripts.python.protonpass_manager import ProtonPassManager

manager = ProtonPassManager()
if manager.cli_available:
    # Create a test password
    manager.create_password(
        name="test-service",
        username="test-user",
        password="test-password"
    )
    
    # Retrieve it
    password = manager.get_password("test-service")
    print(f"Retrieved: {password}")
```

---

## Integration Checklist

- [ ] Install ProtonPassCLI
- [ ] Login to ProtonPass
- [ ] Create `UnifiedSecretManager` class
- [ ] Integrate with `AzureKeyVaultClient`
- [ ] Replace hardcoded secrets in code
- [ ] Update JARVIS workflows
- [ ] Integrate with SYPHON
- [ ] Implement automated rotation
- [ ] Add security intelligence
- [ ] Document all secret locations
- [ ] Create migration scripts
- [ ] Test disaster recovery

---

## References

- **ProtonPassCLI**: https://github.com/ProtonPass/protonpass-cli
- **Implementation**: `scripts/python/protonpass_manager.py`
- **Analysis**: `protonpasscli_utilization_analysis.md`
- **Assessment**: `protonpasscli_final_assessment.md`
- **Azure Key Vault**: `scripts/python/azure_service_bus_integration.py` (AzureKeyVaultClient)

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN  
**Priority**: 🔴 **HIGH** - Major security and operational improvement