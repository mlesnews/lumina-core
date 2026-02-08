# Quality of Life (QOL) Docker Tools Catalog

## Overview

Essential Docker marketplace tools that significantly improve LUMINA development and operations quality of life. All tools are lightweight and suitable for NAS (DS1821PLUS) deployment.

## Quick Start

```bash
# List all available QOL tools
python scripts/python/deploy_qol_tools_to_nas.py list

# Prepare deployment files
python scripts/python/deploy_qol_tools_to_nas.py prepare
```

## QOL Tools by Category

### 🐳 Container Management

#### Portainer
- **Image**: `portainer/portainer-ce:latest`
- **Port**: 9000
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**: 
  - Web UI for Docker management
  - No more command-line Docker commands
  - Visual container management
  - Easy log viewing
  - Resource monitoring
- **Access**: `http://10.17.17.32:9000`

#### Watchtower
- **Image**: `containrrr/watchtower:latest`
- **Resources**: 256MB RAM, 0.5 CPU
- **Benefits**:
  - Automatic container updates
  - No manual `docker pull` needed
  - Keeps everything up-to-date
  - Configurable update schedule
- **Note**: Runs in background, no web UI

### 📊 Monitoring & Observability

#### Uptime Kuma
- **Image**: `louislam/uptime-kuma:latest`
- **Port**: 3001
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Monitor all services
  - Status page for services
  - Alert notifications
  - Uptime tracking
- **Access**: `http://10.17.17.32:3001`

#### Prometheus
- **Image**: `prom/prometheus:latest`
- **Port**: 9090
- **Resources**: 1GB RAM, 1.5 CPU
- **Benefits**:
  - Metrics collection
  - Time-series database
  - Query language (PromQL)
  - Integrates with Grafana
- **Access**: `http://10.17.17.32:9090`

#### Grafana
- **Image**: `grafana/grafana:latest`
- **Port**: 3000
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Beautiful dashboards
  - Visualize metrics
  - Alerting
  - Multiple data sources
- **Access**: `http://10.17.17.32:3000` (admin/admin - change immediately!)

### 🔄 Reverse Proxy

#### Traefik
- **Image**: `traefik:v2.11`
- **Ports**: 80, 443, 8080 (dashboard)
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Automatic SSL (Let's Encrypt)
  - Service discovery
  - Load balancing
  - Modern reverse proxy
- **Access**: 
  - HTTP: `http://10.17.17.32:80`
  - HTTPS: `https://10.17.17.32:443`
  - Dashboard: `http://10.17.17.32:8080`

#### Nginx Proxy Manager
- **Image**: `jc21/nginx-proxy-manager:latest`
- **Ports**: 81 (admin), 80, 443
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Easy web UI for proxy management
  - SSL certificate management
  - Access lists
  - User-friendly
- **Access**: `http://10.17.17.32:81` (admin@example.com/changeme)

### 📝 Logging

#### Loki
- **Image**: `grafana/loki:latest`
- **Port**: 3100
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Log aggregation
  - Integrates with Grafana
  - Efficient storage
  - Query logs easily
- **Access**: `http://10.17.17.32:3100`

### 💾 Caching & Storage

#### Redis
- **Image**: `redis:7-alpine`
- **Port**: 6379
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Fast caching layer
  - Session storage
  - Message queue
  - Pub/sub
- **Access**: `redis://10.17.17.32:6379`

#### MinIO
- **Image**: `minio/minio:latest`
- **Ports**: 9000 (API), 9001 (Console)
- **Resources**: 1GB RAM, 1.5 CPU
- **Benefits**:
  - S3-compatible storage
  - Object storage
  - Web UI for management
  - API compatible with AWS S3
- **Access**: 
  - API: `http://10.17.17.32:9000`
  - Console: `http://10.17.17.32:9001` (minioadmin/minioadmin)

### 💾 Backup

#### Duplicati
- **Image**: `linuxserver/duplicati:latest`
- **Port**: 8200
- **Resources**: 1GB RAM, 1.5 CPU
- **Benefits**:
  - Automated backups
  - Multiple destinations
  - Encryption
  - Scheduling
- **Access**: `http://10.17.17.32:8200`

#### Vaultwarden
- **Image**: `vaultwarden/server:latest`
- **Port**: 80
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Self-hosted password manager
  - Bitwarden-compatible
  - Secure credential storage
  - Mobile apps work
- **Access**: `http://10.17.17.32:80`

### 💻 Development Tools

#### Code Server
- **Image**: `codercom/code-server:latest`
- **Port**: 8080
- **Resources**: 2GB RAM, 2.0 CPU
- **Benefits**:
  - VS Code in browser
  - Code from anywhere
  - Full VS Code features
  - Extensions support
- **Access**: `http://10.17.17.32:8080`

#### PostgreSQL
- **Image**: `postgres:16-alpine`
- **Port**: 5432
- **Resources**: 1GB RAM, 1.5 CPU
- **Benefits**:
  - Production-ready database
  - Reliable storage
  - Full SQL support
  - Backup/restore
- **Access**: `postgresql://lumina@10.17.17.32:5432/lumina`

#### RabbitMQ
- **Image**: `rabbitmq:3-management-alpine`
- **Ports**: 5672 (AMQP), 15672 (Management)
- **Resources**: 512MB RAM, 1.0 CPU
- **Benefits**:
  - Message queue
  - Task distribution
  - Workflow orchestration
  - Management UI
- **Access**: 
  - AMQP: `amqp://lumina@10.17.17.32:5672`
  - Management: `http://10.17.17.32:15672` (lumina/password)

#### FileBrowser
- **Image**: `filebrowser/filebrowser:latest`
- **Port**: 80
- **Resources**: 256MB RAM, 0.5 CPU
- **Benefits**:
  - Web file manager
  - Easy file access
  - Upload/download
  - File sharing
- **Access**: `http://10.17.17.32:80`

### 🔧 Network Tools

#### Whoami
- **Image**: `traefik/whoami:latest`
- **Port**: 80
- **Resources**: 64MB RAM, 0.25 CPU
- **Benefits**:
  - Testing tool
  - Debugging
  - Service verification
- **Access**: `http://10.17.17.32:80`

## Recommended QOL Stack

### Essential (Start Here)
1. **Portainer** - Container management
2. **Watchtower** - Auto-updates
3. **Uptime Kuma** - Service monitoring
4. **Traefik** - Reverse proxy

### Enhanced
5. **Grafana** - Dashboards
6. **Prometheus** - Metrics
7. **Redis** - Caching
8. **Code Server** - Remote development

### Complete Stack
9. **MinIO** - Object storage
10. **PostgreSQL** - Database
11. **RabbitMQ** - Message queue
12. **Loki** - Log aggregation
13. **Vaultwarden** - Password manager
14. **Duplicati** - Backups
15. **FileBrowser** - File management

## Resource Planning

### Lightweight Stack (Recommended for NAS)
- Portainer, Watchtower, Uptime Kuma, Traefik, Redis, FileBrowser
- **Total**: ~2GB RAM, ~4 CPU cores

### Medium Stack
- Add Grafana, Prometheus, Loki, Code Server
- **Total**: ~5GB RAM, ~8 CPU cores

### Full Stack
- All tools
- **Total**: ~15GB RAM, ~20 CPU cores

## Integration with LUMINA

### JARVIS Integration
- **Portainer**: Monitor all JARVIS containers
- **Uptime Kuma**: Monitor JARVIS services
- **Grafana**: JARVIS metrics dashboards
- **Redis**: Cache JARVIS responses
- **RabbitMQ**: JARVIS task queue

### ULTRON/KAIJU Integration
- **Prometheus**: Monitor LLM performance
- **Grafana**: Visualize model metrics
- **Traefik**: Route requests to ULTRON/KAIJU
- **Uptime Kuma**: Monitor cluster health

### MCP Servers Integration
- **Traefik**: Route MCP server requests
- **Uptime Kuma**: Monitor MCP server health
- **Portainer**: Manage MCP containers
- **Redis**: Cache MCP responses

## Security Best Practices

1. **Change Default Passwords**:
   - Grafana: Change admin password
   - MinIO: Set MINIO_ROOT_PASSWORD
   - PostgreSQL: Set POSTGRES_PASSWORD
   - RabbitMQ: Set RABBITMQ_DEFAULT_PASS
   - Code Server: Set PASSWORD
   - Vaultwarden: Set ADMIN_TOKEN

2. **Use Azure Key Vault**:
   - Store all passwords in Key Vault
   - Retrieve at runtime
   - Never hardcode credentials

3. **Network Security**:
   - Use Traefik for SSL termination
   - Enable authentication where possible
   - Restrict access to management UIs

4. **Backup**:
   - Use Duplicati for automated backups
   - Backup volumes regularly
   - Test restore procedures

## Deployment

```bash
# Prepare deployment files
python scripts/python/deploy_qol_tools_to_nas.py prepare

# Review generated files
cat containerization/services/nas-qol-tools/docker-compose.yml
cat containerization/services/nas-qol-tools/DEPLOYMENT.md

# Deploy to NAS (manual steps in DEPLOYMENT.md)
```

## Benefits Summary

✅ **Portainer**: No more Docker CLI - manage everything via web UI
✅ **Watchtower**: Containers stay updated automatically
✅ **Uptime Kuma**: Know immediately when something breaks
✅ **Grafana**: Beautiful dashboards for all metrics
✅ **Traefik**: Easy SSL and routing
✅ **Redis**: Fast caching for better performance
✅ **Code Server**: Code from anywhere, any device
✅ **MinIO**: S3-compatible storage for backups/data
✅ **Vaultwarden**: Secure password management
✅ **FileBrowser**: Easy file access without SSH

---

**#JARVIS #QOL #DOCKER-MARKETPLACE #NAS #DS1821PLUS #LUMINA**
