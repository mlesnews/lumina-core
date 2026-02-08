# Lumina Ollama Docker Cluster Setup

**Date:** 2025-01-24  
**Status:** ✅ Configuration Complete

## Overview

This document describes the complete setup and configuration for the **Lumina Local LLM Cluster** using Docker. The local LLM cluster is an **inseparable component of Lumina** - providing secure, private, local inference capabilities for all Lumina services.

## Architecture

The Lumina LLM cluster consists of:

- **3 Ollama Instances**: Primary, Secondary, and Tertiary for load distribution and redundancy
- **1 Nginx Load Balancer**: Routes requests across Ollama instances on port 3000
- **Shared Volume**: All instances share the same model storage for efficiency

```
┌─────────────────────────────────────────────────────────────┐
│         Lumina LLM Load Balancer (Port 3000)               │
│                      (Nginx)                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
│ Ollama       │ │ Ollama     │ │ Ollama     │
│ Primary      │ │ Secondary  │ │ Tertiary   │
│ (3001)       │ │ (3002)      │ │ (3003)      │
└──────────────┘ └─────────────┘ └────────────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
              ┌────────▼────────┐
              │  Shared Volume  │
              │ (lumina-ollama) │
              └─────────────────┘
```

## Configuration Files

### 1. Docker Compose Configuration
**Location**: `cedarbrook-financial-services_llc-env/containerization/docker-compose.ollama-cluster.yml`

**Services**:
- `ollama-primary`: Primary Ollama instance on port 3001 (container: `lumina-ollama-primary`)
- `ollama-secondary`: Secondary Ollama instance on port 3002 (container: `lumina-ollama-secondary`)
- `ollama-tertiary`: Tertiary Ollama instance on port 3003 (container: `lumina-ollama-tertiary`)
- `ollama-loadbalancer`: Nginx load balancer on port 3000 (container: `lumina-llm-loadbalancer`)

### 2. Nginx Load Balancer Configuration
**Location**: `cedarbrook-financial-services_llc-env/containerization/services/ollama/nginx/nginx.conf`

**Features**:
- Least connections load balancing
- Health checks and failover
- Long timeouts for LLM requests (300s)
- Streaming support for real-time responses
- WebSocket support for chat endpoints

### 3. Model Setup Scripts
**Locations**:
- `cedarbrook-financial-services_llc-env/containerization/services/ollama/setup-iron-legion-models.sh` (Bash)
- `cedarbrook-financial-services_llc-env/containerization/services/ollama/setup-iron-legion-models.ps1` (PowerShell)

## Setup Instructions

### Prerequisites

1. **Docker and Docker Compose**
   ```powershell
   # Verify Docker is installed
   docker --version
   docker-compose --version
   ```

2. **Required Ports Available**
   - 3000: Load Balancer (Iron Legion main cluster endpoint)
   - 3001: Ollama Primary
   - 3002: Ollama Secondary
   - 3003: Ollama Tertiary

### Step 1: Start the Ollama Cluster

Navigate to the containerization directory:

```powershell
cd cedarbrook-financial-services_llc-env/containerization
```

Start the cluster:

```powershell
docker-compose -f docker-compose.ollama-cluster.yml up -d
```

Verify all services are running:

```powershell
docker-compose -f docker-compose.ollama-cluster.yml ps
```

Expected output:
```
NAME                          STATUS
iron-legion-ollama-primary    Up
iron-legion-ollama-secondary   Up
iron-legion-ollama-tertiary   Up
iron-legion-loadbalancer      Up
```

### Step 2: Pull Required Models

The Iron Legion cluster requires the following models (as per Kilo Code configuration):

- **codellama:13b** (Primary model)
- **llama3.2:11b** (Secondary model)
- **qwen2.5-coder:1.5b-base** (Lightweight model)

#### Using PowerShell (Windows):

```powershell
cd cedarbrook-financial-services_llc-env/containerization/services/ollama
.\setup-iron-legion-models.ps1
```

#### Using Bash (Linux/WSL):

```bash
cd cedarbrook-financial-services_llc-env/containerization/services/ollama
chmod +x setup-iron-legion-models.sh
./setup-iron-legion-models.sh
```

#### Manual Model Pull:

You can also pull models manually using curl:

```powershell
# Pull primary model
curl -X POST http://localhost:3000/api/pull -d '{"name": "codellama:13b"}'

# Pull secondary model
curl -X POST http://localhost:3000/api/pull -d '{"name": "llama3.2:11b"}'

# Pull lightweight model
curl -X POST http://localhost:3000/api/pull -d '{"name": "qwen2.5-coder:1.5b-base"}'
```

### Step 3: Verify Setup

#### Check Load Balancer Health:

```powershell
curl http://localhost:3000/health
```

Expected: `healthy`

#### List Available Models:

```powershell
curl http://localhost:3000/api/tags
```

#### Test Inference:

```powershell
curl -X POST http://localhost:3000/api/generate -d '{
  "model": "codellama:13b",
  "prompt": "Hello, world!",
  "stream": false
}'
```

## Integration with Kilo Code

The Iron Legion cluster is configured to work with Kilo Code according to the configuration in:

**Location**: `config/kilo_code_optimized_config.json`

**Key Settings**:
- **Base URL**: `http://localhost:3000` (Lumina LLM Cluster - main endpoint)
- **Primary Endpoint**: `http://localhost:3001` (Direct access to primary)
- **API Type**: `ollama`
- **Models**: codellama:13b, llama3.2:11b, qwen2.5-coder:1.5b-base
- **Branding**: All components branded under Lumina Project

### Cursor IDE Configuration

1. **Open Cursor Settings**
2. **Navigate to Kilo Code settings**
3. **Set base URL**: `http://localhost:3000`
4. **Select primary model**: `codellama:13b`

## Service Management

### Start Cluster

```powershell
docker-compose -f docker-compose.ollama-cluster.yml up -d
```

### Stop Cluster

```powershell
docker-compose -f docker-compose.ollama-cluster.yml down
```

### View Logs

```powershell
# All services
docker-compose -f docker-compose.ollama-cluster.yml logs -f

# Specific service
docker-compose -f docker-compose.ollama-cluster.yml logs -f ollama-primary
```

### Restart Service

```powershell
docker-compose -f docker-compose.ollama-cluster.yml restart ollama-primary
```

## Load Balancing Strategy

The Nginx load balancer uses **least connections** strategy:

- Routes requests to the Ollama instance with the fewest active connections
- Automatically fails over if an instance becomes unavailable
- Health checks every 30 seconds
- Failover timeout: 30 seconds after 3 failures

## Model Storage

All Ollama instances share a single Docker volume (`ollama-data`) for model storage:

- **Location**: Docker volume `ollama-data`
- **Shared**: All instances access the same models
- **Persistent**: Models persist across container restarts
- **Efficient**: Single copy of each model, shared by all instances

## Health Checks

All services include health checks:

- **Ollama Instances**: Check `/api/tags` endpoint
- **Load Balancer**: Check `/health` endpoint
- **Interval**: 30 seconds
- **Timeout**: 10 seconds
- **Retries**: 3

## Troubleshooting

### Cluster Not Starting

1. **Check Port Availability**:
   ```powershell
   netstat -ano | findstr "3000 3001 3002 3003"
   ```

2. **Check Docker Logs**:
   ```powershell
   docker-compose -f docker-compose.ollama-cluster.yml logs
   ```

### Models Not Loading

1. **Check Volume Mount**:
   ```powershell
   docker volume inspect containerization_ollama-data
   ```

2. **Pull Models Directly**:
   ```powershell
   docker exec -it iron-legion-ollama-primary ollama pull codellama:13b
   ```

### Load Balancer Not Responding

1. **Check Nginx Configuration**:
   ```powershell
   docker exec -it iron-legion-loadbalancer nginx -t
   ```

2. **Check Nginx Logs**:
   ```powershell
   docker logs iron-legion-loadbalancer
   ```

### Connection Timeouts

1. **Increase Timeouts** in `nginx.conf`:
   ```
   proxy_connect_timeout 600s;
   proxy_send_timeout 600s;
   proxy_read_timeout 600s;
   ```

2. **Restart Load Balancer**:
   ```powershell
   docker-compose -f docker-compose.ollama-cluster.yml restart ollama-loadbalancer
   ```

## Performance Optimization

### Resource Allocation

For optimal performance, allocate resources based on your hardware:

```yaml
# Add to docker-compose.ollama-cluster.yml
deploy:
  resources:
    limits:
      cpus: '2.0'
      memory: 8G
    reservations:
      cpus: '1.0'
      memory: 4G
```

### Model Selection Strategy

According to Kilo Code configuration:

- **Complex tasks**: Use `codellama:13b` (primary)
- **Medium complexity**: Use `llama3.2:11b` (secondary)
- **Quick completions**: Use `qwen2.5-coder:1.5b-base` (lightweight)

## Security Considerations

1. **Local Only**: The cluster is configured for local access only
2. **No Authentication**: Currently no authentication (suitable for local development)
3. **Network Isolation**: Services are on a dedicated Docker network
4. **Volume Security**: Models stored in Docker volumes (not exposed to host)

## Monitoring

### Service Status

```powershell
docker-compose -f docker-compose.ollama-cluster.yml ps
```

### Resource Usage

```powershell
docker stats iron-legion-ollama-primary iron-legion-ollama-secondary iron-legion-ollama-tertiary
```

### API Health

```powershell
# Load balancer (main cluster)
curl http://localhost:3000/health

# Primary instance
curl http://localhost:3001/api/tags

# Secondary instance
curl http://localhost:3002/api/tags

# Tertiary instance
curl http://localhost:3003/api/tags
```

## Next Steps

1. ✅ **Cluster Running**: Verify all services are up
2. ✅ **Models Installed**: Verify required models are available
3. ✅ **Load Balancer Working**: Test the load balancer endpoint
4. ✅ **Kilo Code Integration**: Configure Kilo Code to use the cluster
5. ✅ **Testing**: Run inference tests to verify functionality

## References

- **Kilo Code Configuration**: `config/kilo_code_optimized_config.json`
- **Iron Legion Cluster Config**: `cedarbrook-financial-services_llc-env/llm_cluster/configs/iron_legion_cluster.json`
- **Ollama Documentation**: https://github.com/ollama/ollama
- **Nginx Load Balancing**: https://nginx.org/en/docs/http/load_balancing.html

---

**Last Updated**: 2025-01-24  
**Version**: 1.0.0  
**Maintained By**: Lumina Project

## Branding

All Docker containers, images, and documentation are branded under **Lumina Project** for GitHub, VS Code extensions, and public-facing materials. This ensures:

- ✅ No private personal or business information is exposed
- ✅ Consistent branding across all Lumina components
- ✅ Ready for public GitHub repositories and VS Code extension marketplace
- ✅ Local LLM cluster is inseparable from Lumina identity

