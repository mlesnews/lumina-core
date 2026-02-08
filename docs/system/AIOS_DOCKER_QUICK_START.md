# AIOS Docker Quick Start

**Date**: 2026-01-07  
**Status**: ✅ QUICK START READY  
**Priority**: 🔴🔴🔴 CRITICAL

## 🚀 Quick Start (3 Commands)

### Linux/Mac

```bash
cd docker/aios
./build.sh
./deploy.sh
./activate.sh
```

### Windows (PowerShell)

```powershell
cd docker/aios
.\build.ps1
.\deploy.ps1
.\activate.ps1
```

## What Gets Deployed

### Services

1. **AIOS Service** (Port 8080)
   - Complete AIOS implementation
   - All Lumina components
   - Full integration

2. **API Gateway** (Port 3000)
   - Unified API entry point
   - Routes to AIOS service
   - Health checks

3. **Redis** (Port 6379)
   - Caching layer
   - State management

4. **PostgreSQL** (Port 5432)
   - Persistent storage
   - Data persistence

## Verify Deployment

### Check Status

```bash
docker-compose -f docker/aios/docker-compose.yml ps
```

### Test API

```bash
# Health check
curl http://localhost:3000/health

# Status
curl http://localhost:3000/status

# Execute query
curl -X POST http://localhost:3000/execute \
  -H "Content-Type: application/json" \
  -d '{"query": "balance", "use_flow": true, "use_pegl": true}'
```

## Management Commands

### View Logs

```bash
docker logs -f aios
```

### Restart

```bash
docker-compose -f docker/aios/docker-compose.yml restart aios
```

### Stop

```bash
docker-compose -f docker/aios/docker-compose.yml down
```

### Update

```bash
./build.sh
docker-compose -f docker/aios/docker-compose.yml up -d --force-recreate
```

## Tags

#QUICK_START #DOCKER #AIOS #DEPLOYMENT @JARVIS @LUMINA

---

**Quick Start**: 3 commands, full deployment!

**Status**: ✅ Ready for production!
