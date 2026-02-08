# NAS Lightweight Containers Deployment Guide

## Overview

This guide explains how to deploy routers, handlers, and other lightweight containers to the NAS (DS1821PLUS) using Synology Container Manager.

## Why Deploy to NAS?

### ✅ Suitable for NAS (DS1821PLUS)
- **Routers**: ULTRON Router, Intelligent LLM Router
- **Handlers**: Request handlers, message processors
- **MCP Servers**: Lightweight API services
- **Monitoring**: Health checks, system monitoring
- **API Gateways**: Lightweight API routing
- **Low CPU/Memory**: Services that don't need heavy compute

### ❌ NOT Suitable for NAS
- **Heavy LLM Containers**: Run on KAIJU desktop (10.17.17.11) or local
- **GPU Workloads**: Run on KAIJU desktop (has RTX 3090)
- **High CPU/Memory**: Services requiring significant resources

## Prerequisites

1. **Synology Container Manager** installed on NAS
   - Install via: DSM Package Center → Container Manager
   - Or: DSM Package Center → Docker (older versions)

2. **SSH Access** to NAS
   - Enable SSH: Control Panel → Terminal & SNMP → Enable SSH
   - Default port: 22

3. **NAS Credentials** in Azure Key Vault
   - Username and password stored securely

## Services Available for Deployment

### 1. ULTRON Router
- **Port**: 3008
- **Description**: Smart routing between local, KAIJU desktop, and NAS
- **Resources**: 512MB RAM, 1.0 CPU
- **Endpoint**: `http://DS1821PLUS:3008`

### 2. Intelligent LLM Router
- **Port**: 3009
- **Description**: Advanced model selection and routing
- **Resources**: 1GB RAM, 1.5 CPU
- **Endpoint**: `http://DS1821PLUS:3009`

### 3. MCP Server Bridge
- **Port**: 3010
- **Description**: Lightweight API bridge for MCP servers
- **Resources**: 256MB RAM, 0.5 CPU
- **Endpoint**: `http://DS1821PLUS:3010`

### 4. Health Monitor
- **Port**: 3011
- **Description**: System health checks and monitoring
- **Resources**: 256MB RAM, 0.5 CPU
- **Endpoint**: `http://DS1821PLUS:3011`

## Deployment Methods

### Method 1: Automated Deployment (Recommended)

```bash
# Check NAS connectivity and Container Manager
python scripts/python/deploy_lightweight_containers_to_nas.py check

# Deploy a specific service
python scripts/python/deploy_lightweight_containers_to_nas.py deploy --service ultron_router

# Deploy all services
python scripts/python/deploy_lightweight_containers_to_nas.py deploy-all
```

### Method 2: Manual Deployment via DSM

1. **Open Container Manager** in DSM
2. **Create Project** → **From docker-compose.yml**
3. **Upload** the generated `docker-compose.yml` file
4. **Deploy** the container

### Method 3: Manual Deployment via SSH

```bash
# 1. Copy files to NAS
scp -r containerization/services/nas-lightweight/ultron-router/ \
    admin@10.17.17.32:/volume1/docker/

# 2. SSH to NAS
ssh admin@10.17.17.32

# 3. Navigate to service directory
cd /volume1/docker/ultron-router

# 4. Deploy with docker-compose
docker-compose up -d

# 5. Check status
docker ps | grep ultron-router
```

## Container Manager vs Docker

Synology Container Manager is a GUI wrapper around Docker. It provides:
- **Web UI**: Easy container management via DSM
- **Docker CLI**: Full Docker compatibility via SSH
- **Resource Limits**: CPU and memory limits per container
- **Auto-restart**: Container restart policies

## Resource Limits

NAS containers are limited to prevent resource exhaustion:

| Service Type | CPU Limit | Memory Limit |
|-------------|-----------|--------------|
| Router | 1.0-1.5 | 512MB-1GB |
| Handler | 0.5-1.0 | 256MB-512MB |
| Monitor | 0.5 | 256MB |
| API Gateway | 0.5-1.0 | 256MB-512MB |

## Network Configuration

All containers are on the `nas-lightweight-network` bridge network:
- **Internal communication**: Use service names
- **External access**: Use NAS IP (10.17.17.32) + port
- **Port mapping**: Host port → Container port

## Health Checks

All containers include health checks:
- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3
- **Start period**: 10 seconds

Check health:
```bash
curl http://10.17.17.32:3008/health
```

## Monitoring

### View Running Containers
```bash
# Via SSH
ssh admin@10.17.17.32 "docker ps"

# Via Container Manager UI
DSM → Container Manager → Container
```

### View Logs
```bash
# Via SSH
ssh admin@10.17.17.32 "docker logs ultron-router"

# Via Container Manager UI
DSM → Container Manager → Container → Logs
```

### Resource Usage
```bash
# Via SSH
ssh admin@10.17.17.32 "docker stats"
```

## Troubleshooting

### Container Won't Start
1. Check logs: `docker logs <container-name>`
2. Verify resources: Ensure CPU/memory limits are appropriate
3. Check ports: Ensure port isn't already in use
4. Verify network: Check network connectivity

### Container Keeps Restarting
1. Check health endpoint: `curl http://10.17.17.32:<port>/health`
2. Review logs for errors
3. Verify dependencies are available
4. Check resource limits (may be too restrictive)

### Cannot Connect to Container
1. Verify port mapping: `docker ps` shows port mapping
2. Check firewall: Ensure port is open in DSM
3. Test connectivity: `curl http://10.17.17.32:<port>/health`
4. Check network: Verify container is on correct network

## Best Practices

1. **Resource Limits**: Always set appropriate CPU/memory limits
2. **Health Checks**: Include health check endpoints
3. **Logging**: Use structured logging for easier debugging
4. **Restart Policy**: Use `unless-stopped` for production services
5. **Backup**: Regularly backup container configurations
6. **Updates**: Keep containers updated for security

## Integration with Other Systems

### ULTRON (Local)
- Connects to NAS routers via `http://10.17.17.32:<port>`
- Routes requests through NAS when appropriate

### KAIJU (Desktop)
- Can use NAS routers for load balancing
- Offloads lightweight routing to NAS

### Cursor IDE
- Configured to use NAS routers when available
- Falls back to local/KAIJU if NAS is unavailable

## Security Considerations

1. **SSH Keys**: Use SSH keys instead of passwords
2. **Firewall**: Only expose necessary ports
3. **Updates**: Keep Container Manager and containers updated
4. **Credentials**: Store credentials in Azure Key Vault
5. **Network**: Use bridge networks for isolation

## Next Steps

1. **Deploy Services**: Run automated deployment script
2. **Verify Health**: Check all health endpoints
3. **Configure Routing**: Update Cursor IDE and other clients
4. **Monitor**: Set up monitoring and alerts
5. **Document**: Update service documentation

---

**#JARVIS #DS1821PLUS #CONTAINER-MANAGER #LIGHTWEIGHT #ROUTERS #HANDLERS**
