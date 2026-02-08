# AIOS Quick Start - Deploy and Activate

**Date**: 2026-01-07  
**Status**: 🎯 QUICK START GUIDE  
**Priority**: 🔴🔴🔴 CRITICAL

## 🚀 Quick Activation (One Command)

```bash
python scripts/python/activate_aios.py
```

That's it! AIOS is now activated and ready to use.

## 📋 Full Deployment Process

### Step 1: Check Prerequisites

```bash
python scripts/python/lumina/aios_deploy.py --check-prerequisites
```

### Step 2: Deploy

```bash
python scripts/python/lumina/aios_deploy.py --deploy
```

### Step 3: Activate

```bash
python scripts/python/lumina/aios_deploy.py --activate
```

### Step 4: Verify

```bash
python scripts/python/lumina/aios_deploy.py --status
python scripts/python/lumina/aios_deploy.py --test
```

## 💻 Usage

### Python Code

```python
from lumina.aios import AIOS

# Initialize AIOS
aios = AIOS()

# Execute query
result = aios.execute("balance", use_flow=True, use_pegl=True)

# Access components
aios.peak.get_status()
aios.library.knowledge("topic")
aios.reality.infer("query")
```

## ✅ Verification

After activation, verify with:

```python
from lumina.aios import AIOS

aios = AIOS()
status = aios.get_status()

# Check key components
assert status['entry_layer']['peak'] == True
assert status['aos_core']['spatial_graph'] == True
```

## 🐳 Docker Deployment (Optional)

```bash
# Deploy with Docker
python scripts/python/lumina/aios_deploy.py --deploy --docker

# Or use docker-compose
cd docker
docker-compose up -d
```

## 📊 Status Check

```bash
# Quick status
python scripts/python/lumina/aios_deploy.py --status

# Detailed status
python scripts/python/activate_aios.py
```

## 🔧 Troubleshooting

### Issue: Import Errors

```bash
# Fix paths
python scripts/python/lumina/aios_deploy.py --fix-paths
```

### Issue: Components Not Initializing

```bash
# Reinitialize
python scripts/python/lumina/aios_deploy.py --reinit
```

### Issue: Check Dependencies

```bash
# Check all dependencies
python scripts/python/lumina/aios_deploy.py --check-dependencies
```

## Tags

#QUICK_START #DEPLOYMENT #ACTIVATION #AIOS @JARVIS @LUMINA

---

**Quick Start**: One command activation!

**Full Deployment**: Automated, verified, ready!
