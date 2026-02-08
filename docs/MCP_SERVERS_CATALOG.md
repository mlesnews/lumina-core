# MCP Servers Catalog - Complete Guide

## Overview

This catalog contains **21+ MCP servers** available for deployment to NAS (DS1821PLUS) via Synology Container Manager. All servers are lightweight and suitable for NAS deployment.

## Quick Start

```bash
# List all available MCP servers
python scripts/python/deploy_mcp_servers_to_nas.py list

# Deploy recommended servers
python scripts/python/deploy_mcp_servers_to_nas.py deploy

# Deploy ALL servers
python scripts/python/deploy_mcp_servers_to_nas.py deploy --all

# Deploy specific servers
python scripts/python/deploy_mcp_servers_to_nas.py deploy --servers n8n filesystem git

# Add specific servers to deployment
python scripts/python/deploy_mcp_servers_to_nas.py add --servers aws-diagram aws-terraform
```

## Available MCP Servers

### Workflow & Automation

#### n8n
- **Image**: `n8nio/n8n:latest`
- **Port**: 5678
- **Resources**: 2GB RAM, 2.0 CPU
- **Description**: Workflow automation platform
- **Endpoint**: `http://10.17.17.32:5678`

### AWS MCP Servers (8 servers)

#### AWS Diagram
- **Image**: `public.ecr.aws/aws-mcp-servers/aws-diagram-mcp-server:latest`
- **Port**: 8087
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Generate AWS architecture diagrams

#### AWS Documentation
- **Image**: `public.ecr.aws/aws-mcp-servers/aws-documentation-mcp-server:latest`
- **Port**: 8088
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Access AWS documentation

#### AWS CDK
- **Image**: `public.ecr.aws/aws-mcp-servers/cdk-mcp-server:latest`
- **Port**: 8089
- **Resources**: 1GB RAM, 1.5 CPU
- **Description**: CDK project management

#### Terraform
- **Image**: `public.ecr.aws/aws-mcp-servers/terraform-mcp-server:latest`
- **Port**: 8090
- **Resources**: 1GB RAM, 1.5 CPU
- **Description**: Infrastructure as Code

#### AWS Lambda
- **Image**: `public.ecr.aws/aws-mcp-servers/lambda-mcp-server:latest`
- **Port**: 8091
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Lambda function management

#### AWS Cost Analysis
- **Image**: `public.ecr.aws/aws-mcp-servers/cost-analysis-mcp-server:latest`
- **Port**: 8092
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Cost optimization

#### AWS Bedrock Knowledge Base
- **Image**: `public.ecr.aws/aws-mcp-servers/bedrock-kb-retrieval-mcp-server:latest`
- **Port**: 8093
- **Resources**: 1GB RAM, 1.5 CPU
- **Description**: RAG capabilities

#### AWS Nova Canvas
- **Image**: `public.ecr.aws/aws-mcp-servers/nova-canvas-mcp-server:latest`
- **Port**: 8094
- **Resources**: 1GB RAM, 1.5 CPU
- **Description**: Visual canvas for AI

### Synology-Specific (2 servers)

#### Synology Download Station
- **Image**: `ghcr.io/akitchin/synology-download-mcp:latest`
- **Port**: 8095
- **Resources**: 256MB RAM, 0.5 CPU
- **Description**: Manage downloads on Synology NAS

#### SynoLink
- **Image**: `ghcr.io/do-boo/mcp-synolink:latest`
- **Port**: 8096
- **Resources**: 256MB RAM, 0.5 CPU
- **Description**: File operations on Synology NAS

### Database (2 servers)

#### PostgreSQL
- **Image**: `modelcontextprotocol/server-postgres:latest`
- **Port**: 8097
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: PostgreSQL database operations

#### SQLite
- **Image**: `modelcontextprotocol/server-sqlite:latest`
- **Port**: 8098
- **Resources**: 256MB RAM, 0.5 CPU
- **Description**: SQLite database operations

### Filesystem (1 server)

#### Filesystem
- **Image**: `modelcontextprotocol/server-filesystem:latest`
- **Port**: 8099
- **Resources**: 256MB RAM, 0.5 CPU
- **Description**: File operations

### Git (1 server)

#### Git
- **Image**: `modelcontextprotocol/server-git:latest`
- **Port**: 8100
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Git operations

### Web & API (2 servers)

#### Brave Search
- **Image**: `modelcontextprotocol/server-brave-search:latest`
- **Port**: 8101
- **Resources**: 256MB RAM, 0.5 CPU
- **Description**: Web search
- **Requires**: Brave API key (from Azure Key Vault)

#### Puppeteer
- **Image**: `modelcontextprotocol/server-puppeteer:latest`
- **Port**: 8102
- **Resources**: 1GB RAM, 1.5 CPU
- **Description**: Web automation

### Development Tools (2 servers)

#### GitHub
- **Image**: `modelcontextprotocol/server-github:latest`
- **Port**: 8103
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: GitHub operations
- **Requires**: GitHub Personal Access Token (from Azure Key Vault)

#### Slack
- **Image**: `modelcontextprotocol/server-slack:latest`
- **Port**: 8104
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Slack integration
- **Requires**: Slack Bot Token (from Azure Key Vault)

### Custom/Local (2 servers)

#### MANUS
- **Build**: Local Dockerfile
- **Port**: 8085
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Unified Control Interface

#### ElevenLabs
- **Build**: Local Dockerfile
- **Port**: 8086
- **Resources**: 512MB RAM, 1.0 CPU
- **Description**: Text-to-Speech
- **Requires**: ElevenLabs API key (from Azure Key Vault)

## Recommended Servers for NAS

These servers are recommended for initial deployment:

1. **n8n** - Workflow automation
2. **MANUS** - Unified control
3. **ElevenLabs** - Text-to-speech
4. **Filesystem** - File operations
5. **Git** - Git operations
6. **Synology Download** - NAS-specific
7. **SynoLink** - NAS-specific

## Resource Requirements

### Lightweight (< 512MB RAM)
- Synology Download, SynoLink
- SQLite, Filesystem
- Brave Search

### Medium (512MB - 1GB RAM)
- Most AWS servers
- PostgreSQL, Git
- GitHub, Slack
- MANUS, ElevenLabs

### Heavy (> 1GB RAM)
- n8n (2GB)
- AWS CDK, Terraform
- AWS Bedrock KB, Nova Canvas
- Puppeteer

## Port Allocation

Ports are automatically assigned:
- **5678**: n8n
- **8085-8086**: Custom (MANUS, ElevenLabs)
- **8087-8094**: AWS servers
- **8095-8096**: Synology servers
- **8097-8104**: Other servers

## Adding New MCP Servers

To add a new MCP server to the catalog:

1. Edit `scripts/python/mcp_servers_catalog.py`
2. Add server configuration to `MCP_SERVERS_CATALOG`
3. Run `python scripts/python/deploy_mcp_servers_to_nas.py list` to verify

Example:
```python
"new-server": {
    "name": "new-mcp-server",
    "description": "New MCP Server Description",
    "image": "dockerhub/user/image:latest",
    "port": 8105,
    "memory_limit": "512m",
    "cpu_limit": "1.0",
    "restart_policy": "unless-stopped",
    "volumes": ["new-server-data:/app/data"]
}
```

## Security Notes

- **ALL API KEYS** must be stored in Azure Key Vault
- Never hardcode credentials in docker-compose.yml
- Use environment variables that pull from Key Vault at runtime
- Review each server's security requirements before deployment

## Deployment Workflow

1. **List available servers**: `python scripts/python/deploy_mcp_servers_to_nas.py list`
2. **Select servers**: Choose based on your needs
3. **Prepare deployment**: `python scripts/python/deploy_mcp_servers_to_nas.py deploy --servers server1 server2`
4. **Review files**: Check generated `docker-compose.yml`
5. **Deploy to NAS**: Follow instructions in `DEPLOYMENT.md`
6. **Configure Cursor**: Update `.cursor/mcp_config.json`

## Troubleshooting

### Server Won't Start
- Check resource limits (may be too restrictive)
- Verify Docker image exists
- Check logs: `docker logs <container-name>`

### Port Conflicts
- Each server gets a unique port
- Check if port is already in use
- Modify port in catalog if needed

### Missing API Keys
- Ensure keys are in Azure Key Vault
- Verify environment variables are set correctly
- Check server documentation for required keys

---

**#JARVIS #MCP #DOCKER-HUB #NAS #DS1821PLUS #CATALOG**
