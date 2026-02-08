# Lumina Deployment Guide

## 🚀 Overview

This guide provides step-by-step instructions for deploying Lumina systems.

## 📋 Prerequisites

### System Requirements

- Python 3.9+
- Windows 10/11 or Linux
- PowerShell 7+ (Windows)
- Docker (optional, for containerized deployment)
- Network access to home lab infrastructure

### Dependencies

```bash
pip install -r requirements.txt
```

## 🔧 Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd lumina
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configuration

Copy example configuration:
```bash
cp config/example_config.yaml config/lumina_config.yaml
```

Edit `config/lumina_config.yaml` with your settings.

## 📦 Deployment Options

### Option 1: Local Deployment

#### Start All Systems

```bash
python scripts/python/lumina_integration.py
```

#### Start Individual Systems

```bash
# Network Health Monitor
python scripts/python/network_health_monitor.py start

# Error Operations Center
python scripts/python/enterprise_error_operations_center.py start

# Galactic Illumination
python scripts/python/lumina_galactic_illumination.py
```

### Option 2: Docker Deployment

#### Build Containers

```bash
docker-compose build
```

#### Start Services

```bash
docker-compose up -d
```

#### View Logs

```bash
docker-compose logs -f
```

### Option 3: Service Deployment

#### Windows Service

```powershell
# Install as service
python scripts/python/service_installer.py install
```

#### Linux Systemd

```bash
# Install service
sudo cp systemd/lumina.service /etc/systemd/system/
sudo systemctl enable lumina
sudo systemctl start lumina
```

## 🔍 Verification

### Check System Status

```bash
python scripts/python/lumina_integration.py --status
```

### Verify Integrations

```bash
python scripts/python/lumina_integration.py --verify
```

### Test Individual Systems

```bash
# Network Health
python scripts/python/network_health_monitor.py status

# Error Ops
python scripts/python/enterprise_error_operations_center.py status

# Galactic Illumination
python scripts/python/lumina_galactic_illumination.py --status
```

## 🔄 Updates

### Update Systems

```bash
git pull
pip install -r requirements.txt --upgrade
```

### Restart Services

```bash
# Docker
docker-compose restart

# Service
sudo systemctl restart lumina  # Linux
# Or restart Windows service
```

## 🛠️ Troubleshooting

### Common Issues

1. **Port Conflicts**
   - Check if ports are already in use
   - Modify port configuration in config

2. **Missing Dependencies**
   - Run `pip install -r requirements.txt`
   - Check Python version

3. **Configuration Errors**
   - Validate config: `python scripts/python/validate_config.py`
   - Check config file syntax

4. **Network Issues**
   - Verify network connectivity
   - Check firewall rules
   - Verify home lab access

### Logs

Logs are located in:
- `data/logs/` - Application logs
- `data/error_ops_center/ops_center.log` - Error ops logs
- `data/network_health/` - Network health logs

## 📊 Monitoring

### Dashboard Access

```bash
# Unified Dashboard
python scripts/python/lumina_dashboard.py

# Individual Dashboards
python scripts/python/network_health_dashboard.py
```

### Health Checks

```bash
# System Health
curl http://localhost:8000/health

# Individual System Health
curl http://localhost:8000/api/v1/network-health/status
```

## 🔐 Security

### Authentication

Configure authentication in `config/lumina_config.yaml`:
```yaml
security:
  enabled: true
  api_key: "your-api-key"
  jwt_secret: "your-secret"
```

### Network Security

- Use HTTPS in production
- Configure firewall rules
- Enable rate limiting
- Use VPN for remote access

## 🚨 Rollback

### Rollback Procedure

1. Stop services
2. Restore previous version
3. Restore configuration backup
4. Restart services

```bash
# Docker
docker-compose down
git checkout <previous-version>
docker-compose up -d

# Local
git checkout <previous-version>
pip install -r requirements.txt
```

## 📝 Post-Deployment

### Verification Checklist

- [ ] All systems started successfully
- [ ] Integrations active
- [ ] Network connectivity verified
- [ ] Error monitoring active
- [ ] Dashboard accessible
- [ ] Logs being generated
- [ ] No critical errors

### Next Steps

1. Configure monitoring alerts
2. Set up backup procedures
3. Document custom configurations
4. Train operators
5. Schedule regular maintenance

---

**Last Updated**: 2025-01-28

