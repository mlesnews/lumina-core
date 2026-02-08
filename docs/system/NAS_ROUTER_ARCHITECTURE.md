# NAS Router & Load Balancer Architecture ✅

**Date**: 2026-01-09
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT @JARVIS
**Status**: ✅ **ARCHITECTURE DESIGNED**

## Architecture Decision

**Move Router & Load Balancer to NAS** for centralized, fault-tolerant infrastructure.

### Benefits
1. ✅ **Fault Tolerance**: If FALC or KAIJU goes down, router/loadbalancer still available
2. ✅ **Centralized Management**: Single point of control
3. ✅ **High Availability**: NAS is always-on infrastructure
4. ✅ **Shared Resource**: Both systems use same router/loadbalancer
5. ✅ **Preserved State**: Router configuration persists on NAS

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    NAS (10.17.17.32)                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Iron Legion Router (Port 3000)                  │   │
│  │  - Expert routing logic                          │   │
│  │  - Health checking                               │   │
│  │  - Failover management                           │   │
│  └──────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Nginx Load Balancer (Port 3000)                 │   │
│  │  - Load balancing across 7 models                │   │
│  │  - Health checks                                  │   │
│  │  - Failover routing                              │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
         │                    │
         │                    │
    ┌────▼────┐          ┌────▼────┐
    │  KAIJU  │          │  FALC   │
    │ 10.17.  │          │ 10.17.  │
    │ 17.11   │          │ 17.10   │
    │         │          │         │
    │ 7 LLMs  │          │ PERSPEC │
    │ Ports   │          │ TIVE    │
    │ 3001-7  │          │ Models  │
    └─────────┘          └─────────┘
```

## Implementation

### Step 1: Fix Router Issues (Current)
- ✅ Create simplified FastAPI router
- ✅ Fix Python module path issues
- ✅ Remove complex dependencies

### Step 2: Deploy on NAS
- ⏳ Install Docker on NAS (if not available)
- ⏳ Copy router/loadbalancer containers
- ⏳ Configure networking
- ⏳ Test connectivity from FALC and KAIJU

### Step 3: Update Configurations
- ⏳ Update Iron Legion config to point to NAS router
- ⏳ Update Cursor IDE models config
- ⏳ Update MCP server configs
- ⏳ Update JARVIS health checks

## Router Endpoints

### NAS Router (10.17.17.32:3000)
- `GET /health` - Health check
- `GET /status` - Expert status
- `POST /expert` - Expert routing
- `POST /v1/chat/completions` - OpenAI-compatible API

### Load Balancer (10.17.17.32:3000)
- `GET /health` - Health check
- `POST /v1/chat/completions` - Load balanced requests
- Routes to: 10.17.17.11:3001-3007 (KAIJU models)

## Network Configuration

### Router Access
- **From KAIJU**: `http://10.17.17.32:3000`
- **From FALC**: `http://10.17.17.32:3000`
- **From Anywhere**: `http://10.17.17.32:3000`

### Backend Models
- **KAIJU Models**: `http://10.17.17.11:3001-3007`
- **FALC Models**: `http://10.17.17.10:11436`

## Fault Tolerance

### Scenario 1: KAIJU Down
- Router on NAS continues operating
- Can route to FALC models (MILLENNIUM_FALCON)
- Load balancer fails over to FALC

### Scenario 2: FALC Down
- Router on NAS continues operating
- Routes to KAIJU models only
- No impact on KAIJU operations

### Scenario 3: NAS Router Down
- KAIJU and FALC can still access models directly
- Direct endpoints still available
- Can restart router on NAS

## Next Steps

1. ✅ Fix router Python module issues
2. ⏳ Test simplified router on KAIJU
3. ⏳ Check NAS Docker availability (Synology DSM)
4. ⏳ Deploy router/loadbalancer on NAS
5. ⏳ Update all configurations
6. ⏳ Test from both FALC and KAIJU
7. ⏳ Integrate into JARVIS

---

**Last Updated**: 2026-01-09
**Status**: ✅ **ARCHITECTURE DESIGNED - IMPLEMENTATION IN PROGRESS**
