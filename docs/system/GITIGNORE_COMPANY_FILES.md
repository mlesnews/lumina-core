# Gitignore for Company-Specific Files

**Date:** 2025-01-24  
**Status:** ✅ Complete

## Overview

The `.gitignore` file has been configured to protect company-specific files containing private information. This ensures that when you commit to public repositories (GitHub, VS Code extensions), no private company data is exposed.

## Protected Files

### Company Configuration

- `config/lumina_company_config.json` - Contains real company information
  - **Template Available**: `config/lumina_company_config.json.example`
  - Copy the example and customize for your company
  - The actual config file is ignored by git

### Company-Specific Docker Files

When in **internal mode** (company branding), these files are ignored:
- `docker-compose*.yml` - Company-branded compose files
- `services/**/Dockerfile` - Dockerfiles with company maintainer
- `services/**/Dockerfile.dev` - Development Dockerfiles with company branding
- `nginx/nginx.conf` - Nginx configs with company-specific upstream names

**Note**: Public mode files (Lumina Project branding) can be committed.

### Company-Specific Documentation

- `QUICK_START_CFS.md` - Company-specific quick start guides
- `README-CFS.md` - Company-specific README files
- `*CFS*.md` - Any documentation with company branding

### Company-Specific Scripts

- `scripts/**/*cfs*.ps1` - Scripts with hardcoded company information
- `scripts/**/*company*.ps1` - Company-specific scripts
- `scripts/**/*internal*.ps1` - Internal mode scripts

### Secrets and Keys

- `**/secrets/company/` - Company-specific secrets
- `**/secrets/cfs/` - CFS-specific secrets
- `**/*company*.key` - Company key files
- `**/*cfs*.key` - CFS key files
- `**/*company*.pem` - Company certificate files
- `**/*cfs*.pem` - CFS certificate files

### Company Data and Logs

- `logs/company/` - Company-specific logs
- `logs/cfs/` - CFS-specific logs
- `data/company/` - Company-specific data
- `data/cfs/` - CFS-specific data

## Workflow for Public Commits

### Before Committing to Public Repository

1. **Switch to Public Mode**:
   ```powershell
   .\scripts\powershell\apply-company-branding.ps1 -Mode public
   ```

2. **Verify Files**:
   ```powershell
   git status
   ```

3. **Commit Public Files**:
   ```powershell
   git add .
   git commit -m "Update Lumina configuration"
   ```

### After Committing

Switch back to internal mode for local development:
```powershell
.\scripts\powershell\apply-company-branding.ps1 -Mode internal
```

## Template Files

### Company Configuration Template

**Location**: `config/lumina_company_config.json.example`

This is a template file that **can be committed** to git. It contains placeholder values that you can copy and customize:

```powershell
# Copy template to actual config (this file will be ignored)
Copy-Item config\lumina_company_config.json.example config\lumina_company_config.json

# Edit with your company information
# The actual file is in .gitignore
```

## Verification

### Check What's Ignored

```powershell
# See ignored files
git status --ignored

# Check if company config is ignored
git check-ignore -v config/lumina_company_config.json
```

### Verify Before Commit

```powershell
# See what will be committed
git status

# Should NOT see:
# - config/lumina_company_config.json
# - Company-specific Docker files (if in internal mode)
# - Company-specific documentation
```

## Best Practices

1. **Always Use Public Mode for Commits**
   - Switch to public mode before committing
   - Verify with `git status` that no company files are included

2. **Use Template Files**
   - Commit template/example files
   - Keep actual config files in .gitignore

3. **Review Before Committing**
   - Always run `git status` before committing
   - Check that no private information is included

4. **Separate Public and Private Repos**
   - Consider having separate repositories:
     - Public: Lumina Project (public mode)
     - Private: Company-specific (internal mode)

## What CAN Be Committed

✅ **Public Mode Files**:
- Lumina Project branded Docker files
- Public documentation
- Template/example files
- Lumina Project branding

✅ **Template Files**:
- `config/lumina_company_config.json.example`
- Example Docker files
- Public documentation templates

## What CANNOT Be Committed

❌ **Company-Specific Files**:
- `config/lumina_company_config.json` (real company data)
- Company-branded Docker files (internal mode)
- Company-specific documentation
- Company secrets and keys
- Company-specific scripts with hardcoded info

## Summary

- ✅ Company configuration file is protected
- ✅ Company-specific Docker files are ignored (when in internal mode)
- ✅ Company secrets and keys are protected
- ✅ Template files can be committed
- ✅ Public mode files can be committed
- ✅ Easy workflow: Switch to public mode before committing

---

**Maintained By**: Lumina Project  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

