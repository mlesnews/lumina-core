# AIOS Deployment and Activation Guide

**Date**: 2026-01-07  
**Status**: 🎯 DEPLOYMENT READY  
**Priority**: 🔴🔴🔴 CRITICAL

## Quick Start

### 1. Deploy AIOS

```bash
# From project root
python scripts/python/lumina/aios_deploy.py --deploy
```

### 2. Activate AIOS

```bash
# Activate AIOS
python scripts/python/lumina/aios_deploy.py --activate

# Or use the activation script
python scripts/python/activate_aios.py
```

### 3. Verify Deployment

```bash
# Check status
python scripts/python/lumina/aios_deploy.py --status

# Test all components
python scripts/python/lumina/aios_deploy.py --test
```

## Deployment Steps

### Step 1: Prerequisites

**Required**:
- Python 3.11+
- All Lumina dependencies installed
- Docker (for infrastructure layer)
- Project root access

**Check Prerequisites**:
```bash
python scripts/python/lumina/aios_deploy.py --check-prerequisites
```

### Step 2: Initialize Components

**Initialize All Layers**:
```bash
python scripts/python/lumina/aios_deploy.py --init-all
```

This initializes:
- Entry Layer (Peak)
- Knowledge Layer (Library, Digest)
- Inference Layer (Reality systems)
- Transformation Layer (PEGL, Flow)
- AOS Core (Spatial Graph, Quantum, HID)
- Foundation (Reality Layer Zero)

### Step 3: Verify Integration

**Verify All Components**:
```bash
python scripts/python/lumina/aios_deploy.py --verify
```

### Step 4: Activate

**Activate AIOS**:
```bash
python scripts/python/lumina/aios_deploy.py --activate
```

## Activation Methods

### Method 1: Direct Activation

```python
from lumina.aios import AIOS

# Initialize and activate
aios = AIOS()

# Verify activation
status = aios.get_status()
print(status)
```

### Method 2: Activation Script

```bash
python scripts/python/activate_aios.py
```

### Method 3: Service Mode

```bash
# Start as service
python scripts/python/lumina/aios_service.py --start

# Stop service
python scripts/python/lumina/aios_service.py --stop

# Status
python scripts/python/lumina/aios_service.py --status
```

## Deployment Architecture

### Local Deployment

```
Project Root
    ↓
scripts/python/lumina/
    ↓
AIOS (aios.py)
    ↓
All Components Initialized
    ↓
Ready for Use
```

### Docker Deployment

```
Docker Compose
    ↓
API Gateway
    ↓
AIOS Service
    ↓
All Components
    ↓
Ready for Use
```

## Activation Checklist

- [ ] Prerequisites checked
- [ ] All components initialized
- [ ] Integration verified
- [ ] Health checks passed
- [ ] AIOS activated
- [ ] Status confirmed
- [ ] Test query executed

## Health Checks

### Component Health

```python
from lumina.aios import AIOS

aios = AIOS()
status = aios.get_status()

# Check each layer
assert status['entry_layer']['peak'] == True
assert status['knowledge_layer']['library'] == True
assert status['inference_layer']['reality'] == True
assert status['transformation_layer']['pegl'] == True
assert status['aos_core']['spatial_graph'] == True
assert status['foundation']['layer_zero'] == True
```

### Functional Test

```python
# Execute test query
result = aios.execute("balance", use_flow=True, use_pegl=True)

# Verify result
assert result['result'] is not None
assert len(result['steps']) > 0
```

## Troubleshooting

### Issue: Components Not Initializing

**Solution**:
```bash
# Check dependencies
python scripts/python/lumina/aios_deploy.py --check-dependencies

# Reinitialize
python scripts/python/lumina/aios_deploy.py --reinit
```

### Issue: Import Errors

**Solution**:
```bash
# Fix paths
python scripts/python/lumina/aios_deploy.py --fix-paths

# Verify imports
python scripts/python/lumina/aios_deploy.py --verify-imports
```

### Issue: Docker Not Available

**Solution**:
- Install Docker Desktop
- Or use local deployment mode
- Infrastructure layer will show as "external"

## Production Deployment

### Step 1: Environment Setup

```bash
# Set environment variables
export AIOS_MODE=production
export AIOS_LOG_LEVEL=INFO
export AIOS_DOCKER_ENABLED=true
```

### Step 2: Deploy

```bash
# Full deployment
python scripts/python/lumina/aios_deploy.py --deploy --production

# With Docker
python scripts/python/lumina/aios_deploy.py --deploy --docker
```

### Step 3: Monitor

```bash
# Monitor status
python scripts/python/lumina/aios_deploy.py --monitor

# Health check
python scripts/python/lumina/aios_deploy.py --health
```

## Tags

#DEPLOYMENT #ACTIVATION #AIOS #PRODUCTION @JARVIS @LUMINA

---

**Deployment**: Simple, automated, verified

**Activation**: One command, full system ready
