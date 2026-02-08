# Federated Compute Pool

## Vision

**Compound compute by adding more labs.** Each lab you add increases the total pool.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         LUMINA FEDERATION                                       │
│                     http://localhost:8080                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐               │
│  │   HomeBase      │   │   Office Lab    │   │   Cloud Lab     │               │
│  │   (Primary)     │   │  (via Tailscale)│   │ (via Tunnel)    │               │
│  │                 │   │                 │   │                 │               │
│  │  ULTRON-GPU     │   │  Workstation-1  │   │  GPU-Instance   │               │
│  │  ULTRON-CPU     │   │  Workstation-2  │   │  CPU-Instance   │               │
│  │  Kaiju          │   │                 │   │                 │               │
│  │  NAS            │   │                 │   │                 │               │
│  │                 │   │                 │   │                 │               │
│  │  40 cores       │   │  +24 cores      │   │  +16 cores      │               │
│  │  128GB RAM      │   │  +64GB RAM      │   │  +32GB RAM      │               │
│  │  24GB VRAM      │   │  +16GB VRAM     │   │  +24GB VRAM     │               │
│  └────────┬────────┘   └────────┬────────┘   └────────┬────────┘               │
│           │                     │                     │                         │
│           └─────────────────────┴─────────────────────┘                         │
│                                 │                                               │
│                    ═════════════════════════════                                │
│                    TOTAL: 80 cores, 224GB RAM, 64GB VRAM                        │
│                    ═════════════════════════════                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## How It Works

### 1. Federation Structure

- **Labs**: Physical or logical groupings of compute resources
- **Nodes**: Individual machines running Ollama/inference
- **Pool**: All labs combined into one unified endpoint

### 2. Adding a New Lab

#### Option A: Via API (Dynamic)

```bash
curl -X POST http://localhost:8080/federation/labs \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Office Lab",
    "location": "Downtown Office",
    "nodes": [
      {
        "name": "Workstation-1",
        "host": "100.64.0.10",
        "port": 11434,
        "type": "gpu",
        "specs": {
          "gpu": "RTX 4090",
          "cpu": "Ryzen 9 7950X",
          "ram_gb": 64
        }
      },
      {
        "name": "Workstation-2",
        "host": "100.64.0.11",
        "port": 11434,
        "type": "cpu",
        "specs": {
          "cpu": "Ryzen 7 5800X",
          "ram_gb": 32
        }
      }
    ]
  }'
```

#### Option B: Via Config File

Edit `config/federated_compute_pool.json`:

```json
{
  "labs": {
    "HomeBase": { ... },
    "OfficeLab": {
      "name": "Office Lab",
      "location": "Downtown",
      "status": "active",
      "nodes": [
        {
          "name": "Workstation-1",
          "host": "100.64.0.10",
          "port": 11434,
          "type": "gpu"
        }
      ]
    }
  }
}
```

### 3. Connectivity Options

| Method | Latency | Setup | Best For |
|--------|---------|-------|----------|
| **Local LAN** | <1ms | None | Same building |
| **Tailscale** | 10-50ms | Install app | Different locations |
| **Cloudflare Tunnel** | 20-100ms | Create tunnel | Behind firewall |
| **WireGuard** | 5-30ms | Configure VPN | Direct connection |

#### Tailscale Setup (Recommended)

1. Install Tailscale on all machines: `tailscale up`
2. All machines join the same tailnet
3. Use Tailscale IPs (100.x.x.x) in config
4. Automatic encryption, NAT traversal

#### Cloudflare Tunnel Setup

1. Create tunnel: `cloudflared tunnel create ollama-lab`
2. Configure: expose `localhost:11434` via tunnel
3. Use tunnel hostname in config
4. Zero-trust security

### 4. Scaling Examples

#### Current: HomeBase Only
```
Labs: 1
Nodes: 4
GPU: 24GB
CPU: 40 cores
RAM: 128GB
```

#### Add Office Lab (+2 nodes)
```
Labs: 2
Nodes: 6
GPU: 40GB (+16)
CPU: 64 cores (+24)
RAM: 192GB (+64)
```

#### Add Cloud Lab (+2 nodes)
```
Labs: 3
Nodes: 8
GPU: 64GB (+24)
CPU: 80 cores (+16)
RAM: 224GB (+32)
```

### 5. API Reference

#### Get Federation Status
```
GET /health
GET /federation/status
```

#### List All Models
```
GET /api/tags
```

#### Add New Lab
```
POST /federation/labs
Content-Type: application/json

{
  "name": "Lab Name",
  "location": "Description",
  "nodes": [...]
}
```

#### Chat Completion (routes to best node)
```
POST /api/chat
POST /v1/chat/completions
```

### 6. Routing Logic

The federation router automatically:

1. **Health checks** all nodes every 30 seconds
2. **Selects fastest** healthy node for each request
3. **Prefers GPU** nodes for large models (32B+)
4. **Fails over** if a node becomes unavailable
5. **Load balances** based on active requests

### 7. Security Considerations

- Use Tailscale or Cloudflare for encrypted transport
- Don't expose Ollama directly to internet
- Consider authentication for federation API
- Monitor for unauthorized lab additions

---

## Quick Start

```powershell
# Start the federated router
python services/federated_pool/federated_router.py

# Check status
curl http://localhost:8080/health

# Add a new lab
curl -X POST http://localhost:8080/federation/labs -d '...'

# Use unified endpoint
curl http://localhost:8080/api/chat -d '{"model":"qwen2.5:7b","messages":[...]}'
```

---

Tags: @PEAK @FEDERATION @SCALABILITY #automation
