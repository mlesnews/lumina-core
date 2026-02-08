# Lumina Company Customization Guide

**Date:** 2025-01-24  
**Status:** ✅ Complete

## Overview

Lumina can be customized to represent your company for internal use, while maintaining Lumina Project branding for public-facing materials (GitHub, VS Code extensions).

## Configuration

### Company Configuration File

**Location**: `config/lumina_company_config.json`

This is the Single Source of Truth (SSoT) for company customization. It contains:

- **Company Information**: Name, domain, description
- **Branding Modes**: Internal (company) and Public (Lumina Project)
- **Docker Configuration**: Container names, volumes, networks for each mode
- **LLM Cluster Settings**: Endpoints, ports, models

### Branding Modes

#### Internal Mode (Company Branding)

For internal/private use with your company branding:

- **Maintainer**: Your company name (e.g., "Cedarbrook Financial Services LLC")
- **Container Prefix**: Company prefix (e.g., "cfs")
- **Container Names**: `cfs-ollama-primary`, `cfs-llm-loadbalancer`, etc.
- **Volumes**: `cfs-ollama-data`
- **Networks**: `cfs-llm-cluster`
- **Images**: `cedarbrook/ollama:latest`

#### Public Mode (Lumina Project Branding)

For public-facing materials (GitHub, VS Code extensions):

- **Maintainer**: "Lumina Project"
- **Container Prefix**: "lumina"
- **Container Names**: `lumina-ollama-primary`, `lumina-llm-loadbalancer`, etc.
- **Volumes**: `lumina-ollama-data`
- **Networks**: `lumina-llm-cluster`
- **Images**: `lumina/ollama:latest`

## Usage

### Apply Company Branding

```powershell
# Apply internal (company) branding
.\scripts\powershell\apply-company-branding.ps1 -Mode internal

# Apply public (Lumina Project) branding
.\scripts\powershell\apply-company-branding.ps1 -Mode public
```

### Customize Your Company Information

Edit `config/lumina_company_config.json`:

```json
{
  "company": {
    "name": "Cedarbrook Financial Services LLC",
    "legal_name": "Cedarbrook Financial Services LLC",
    "short_name": "CFS",
    "domain": "cedarbrook.financial",
    "email_domain": "@cedarbrook.financial",
    "website": "https://cedarbrook.financial"
  },
  "branding": {
    "active_mode": "internal"
  }
}
```

## What Gets Updated

When you apply company branding, the following files are updated:

1. **docker-compose.ollama-cluster.yml**
   - Container names
   - Volume names
   - Network names

2. **Dockerfiles**
   - `services/ollama/Dockerfile`
   - `services/ollama/Dockerfile.dev`
   - Maintainer labels
   - Description text

3. **Nginx Configuration**
   - `services/ollama/nginx/nginx.conf`
   - Upstream server names

## Example: Cedarbrook Financial Services LLC

### Internal Configuration

```json
{
  "branding": {
    "active_mode": "internal"
  },
  "docker": {
    "internal": {
      "maintainer": "Cedarbrook Financial Services LLC",
      "container_names": {
        "ollama_primary": "cfs-ollama-primary",
        "loadbalancer": "cfs-llm-loadbalancer"
      }
    }
  }
}
```

### Public Configuration

```json
{
  "branding": {
    "active_mode": "public"
  },
  "docker": {
    "public": {
      "maintainer": "Lumina Project",
      "container_names": {
        "ollama_primary": "lumina-ollama-primary",
        "loadbalancer": "lumina-llm-loadbalancer"
      }
    }
  }
}
```

## Workflow

### For Internal Development

1. Set `active_mode` to `"internal"` in `config/lumina_company_config.json`
2. Run: `.\scripts\powershell\apply-company-branding.ps1 -Mode internal`
3. All Docker configurations will use your company branding
4. Start cluster: `docker-compose -f docker-compose.ollama-cluster.yml up -d`

### For Public Release (GitHub/VS Code Extension)

1. Set `active_mode` to `"public"` in `config/lumina_company_config.json`
2. Run: `.\scripts\powershell\apply-company-branding.ps1 -Mode public`
3. All Docker configurations will use Lumina Project branding
4. Commit and push to GitHub
5. Publish VS Code extension

## Integration with Lumina

**The local LLM cluster remains inseparable from Lumina**, regardless of branding mode:

- **Internal Mode**: Lumina customized for your company
- **Public Mode**: Lumina Project (open source/public)

Both modes maintain:
- ✅ Full Lumina functionality
- ✅ Integrated LLM cluster
- ✅ Resource-aware context management
- ✅ Air-gapped security
- ✅ All Lumina features

## Verification

After applying branding, verify:

```powershell
# Check container names in compose file
Get-Content docker-compose.ollama-cluster.yml | Select-String "container_name"

# Check Dockerfile maintainer
Get-Content services/ollama/Dockerfile | Select-String "maintainer"

# Check active mode
(Get-Content config/lumina_company_config.json | ConvertFrom-Json).branding.active_mode
```

## Best Practices

1. **Use Internal Mode** for:
   - Local development
   - Internal deployments
   - Company-specific configurations

2. **Use Public Mode** for:
   - GitHub repositories
   - VS Code extension marketplace
   - Open source contributions
   - Public documentation

3. **Keep Configuration Updated**:
   - Update `config/lumina_company_config.json` when company info changes
   - Re-apply branding after configuration changes
   - Document any custom configurations

## Summary

- ✅ **Internal Use**: Customize Lumina with your company branding
- ✅ **Public Use**: Use Lumina Project branding for GitHub/VS Code
- ✅ **Seamless Switching**: Easy to switch between modes
- ✅ **SSoT Configuration**: Single source of truth in `config/lumina_company_config.json`
- ✅ **Integrated**: LLM cluster remains inseparable from Lumina in both modes

---

**Maintained By**: Lumina Project  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

