# 🌐 SiderAI Wisebase + RoamWise.AI.lesnewski.local Integration

## 🎯 Overview

**RoamWise.AI.lesnewski.local** is a hybrid web frontend server that combines two knowledge systems:

```
┌─────────────────────────────────────────────────────────────┐
│         RoamWise.AI.lesnewski.local (Web Frontend)          │
│                    Port: 5000                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────┐    ┌──────────────────────┐    │
│  │   SiderAI Wisebase   │    │   RoamResearch       │    │
│  │   (Half 1)           │    │   Lifetime Account   │    │
│  │                      │    │   (Half 2)           │    │
│  │  • Knowledge Base     │    │  • Personal Graph    │    │
│  │  • AI Summarization  │    │  • Lifetime Access   │    │
│  │  • Content Analysis  │    │  • Note Connections  │    │
│  └──────────────────────┘    └──────────────────────┘    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         WoW Atlas-Style Pathfinder                  │  │
│  │         • Node Visualization                         │  │
│  │         • Word Cloud                                 │  │
│  │         • Knowledge Graph                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Architecture

### Components

| Component | Role | Location | Status |
|-----------|------|----------|--------|
| **SiderAI Wisebase** | Knowledge extraction & summarization | Browser Extension + API | ✅ Active |
| **RoamResearch** | Personal knowledge graph | Cloud (Lifetime Account) | ✅ Active |
| **RoamWise Server** | Web frontend aggregator | `roamwise.ai.lesnewski.local:5000` | ✅ Ready |
| **Pathfinder** | WoW Atlas-style visualization | Server-side | ✅ Ready |

---

## 📋 Configuration

### 1. Domain Setup

**Domain**: `RoamWise.AI.lesnewski.local` (or `roamwise.ai.lesnewski.local`)

**Hosts File Entry** (Windows):
```
127.0.0.1    RoamWise.AI.lesnewski.local
127.0.0.1    roamwise.ai.lesnewski.local
```

**Setup Script**:
```powershell
.\scripts\python\roamwise_setup_hosts.ps1
```

### 2. Server Configuration

**File**: `config/roamwise_config.json`

```json
{
  "siderai_wisebase": {
    "api_key": "YOUR_SIDERAI_API_KEY",
    "base_url": "https://api.sider.ai/wisebase",
    "enabled": true
  },
  "roamresearch": {
    "api_key": "YOUR_ROAMRESEARCH_API_KEY",
    "base_url": "https://roamresearch.com/api",
    "graph_name": "lesnewski_lifetime",
    "account_type": "lifetime",
    "enabled": true
  },
  "roamwise": {
    "domain": "roamwise.ai.lesnewski.local",
    "port": 5000,
    "data_dir": "data/roamwise",
    "pathfinder": {
      "style": "wow_atlas",
      "grid_size": 10,
      "max_connections": 7
    }
  }
}
```

### 3. Environment Variables

```bash
# SiderAI Wisebase
SIDERAI_WISEBASE_API_KEY=your_key_here

# RoamResearch
ROAMRESEARCH_API_KEY=your_key_here
```

---

## 🚀 Running the Server

### Start RoamWise Server

```powershell
# From project root
python scripts/python/roamwise_server.py --host 0.0.0.0 --port 5000

# Or with custom domain
python scripts/python/roamwise_server.py --host RoamWise.AI.lesnewski.local --port 5000
```

### Access Points

| URL | Description |
|-----|-------------|
| `http://RoamWise.AI.lesnewski.local:5000` | Main Atlas Interface |
| `http://localhost:5000` | Localhost access |
| `http://127.0.0.1:5000` | IP access |
| `http://RoamWise.AI.lesnewski.local:5000/api/status` | API Status |
| `http://RoamWise.AI.lesnewski.local:5000/api/data` | All Data (JSON) |
| `http://RoamWise.AI.lesnewski.local:5000/api/wordcloud` | Word Cloud Data |

---

## 🔗 Integration Points

### SiderAI Wisebase Integration

**Purpose**: Extract and summarize content from web pages (YouTube, articles, etc.)

**Features**:
- Real-time content analysis
- AI-powered summarization
- Knowledge extraction
- Context linking

**Integration Script**: `scripts/python/jarvis_sider_roamwise_integration.py`

```python
from jarvis_sider_roamwise_integration import JARVISSiderAIIntegration

sider = JARVISSiderAIIntegration()
result = sider.wisebase_query("What is quantum computing?")
```

### RoamResearch Integration

**Purpose**: Personal knowledge graph with lifetime account access

**Features**:
- Bidirectional links
- Block references
- Daily notes
- Graph queries

**Integration Script**: `scripts/python/jarvis_sider_roamwise_integration.py`

```python
from jarvis_sider_roamwise_integration import JARVISRoamResearchIntegration

roam = JARVISRoamResearchIntegration()
result = roam.query_graph("[[AI Philosophy]]")
```

---

## 🎨 Frontend Features

### WoW Atlas-Style Pathfinder

- **Node Visualization**: Interactive knowledge nodes
- **Path Finding**: Connections between concepts
- **Zone Mapping**: Organized knowledge areas
- **Search**: Real-time node search

### Word Cloud

- **Popularity Visualization**: Word frequency analysis
- **Source Linking**: Links to database, holocron, videos
- **Interactive**: Click words to explore
- **Dynamic**: Updates from live data

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/status` | GET | System status |
| `/api/data` | GET | All nodes/paths/zones |
| `/api/path?from=X&to=Y` | GET | Find path between nodes |
| `/api/zone/<name>` | GET | Get zone map |
| `/api/wordcloud` | GET | Word cloud data |
| `/api/holocron?query=X` | GET | Search holocron |
| `/api/videos?search=X` | GET | Search video archive |

---

## 🔄 Data Flow

```
┌─────────────┐
│  SiderAI    │
│  Wisebase   │──┐
└─────────────┘  │
                  ├──► RoamWise Server ──► Web Frontend
┌─────────────┐  │         │
│ RoamResearch│──┘         │
│  (Lifetime) │            ▼
└─────────────┘      ┌─────────────┐
                     │  Pathfinder │
                     │  (WoW Atlas)│
                     └─────────────┘
```

---

## 🛠️ Troubleshooting

### Server Won't Start

1. **Check Flask Installation**:
   ```bash
   pip install flask flask-cors
   ```

2. **Check Port Availability**:
   ```powershell
   netstat -ano | findstr :5000
   ```

3. **Check Hosts File**:
   ```powershell
   Get-Content C:\Windows\System32\drivers\etc\hosts | Select-String "roamwise"
   ```

### Domain Not Resolving

1. **Add to Hosts File**:
   ```powershell
   Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "127.0.0.1 RoamWise.AI.lesnewski.local"
   ```

2. **Or Use Setup Script**:
   ```powershell
   .\scripts\python\roamwise_setup_hosts.ps1
   ```

### SiderAI Not Connecting

1. **Check API Key**:
   ```python
   import os
   print(os.getenv("SIDERAI_WISEBASE_API_KEY"))
   ```

2. **Test Endpoint**:
   ```python
   from jarvis_sider_roamwise_integration import JARVISSiderAIIntegration
   sider = JARVISSiderAIIntegration()
   print(sider.wisebase_available)
   ```

---

## 📚 Related Files

| File | Purpose |
|------|---------|
| `scripts/python/roamwise_server.py` | Main server implementation |
| `scripts/python/jarvis_sider_roamwise_integration.py` | Integration classes |
| `scripts/python/roamwise_config.py` | Configuration manager |
| `scripts/python/roamwise_hybrid_datafeed.py` | Data aggregation |
| `scripts/python/roamwise_setup_hosts.ps1` | Hosts file setup |
| `roamwise_ai_frontend_integration.md` | Frontend architecture docs |

---

## 🎯 Quick Start

1. **Setup Hosts File**:
   ```powershell
   .\scripts\python\roamwise_setup_hosts.ps1
   ```

2. **Configure API Keys**:
   ```powershell
   $env:SIDERAI_WISEBASE_API_KEY="your_key"
   $env:ROAMRESEARCH_API_KEY="your_key"
   ```

3. **Start Server**:
   ```powershell
   python scripts/python/roamwise_server.py
   ```

4. **Access Frontend**:
   ```
   http://RoamWise.AI.lesnewski.local:5000
   ```

---

## 🔐 Security Notes

- **Local Network Only**: Server runs on `.local` domain (not publicly accessible)
- **API Keys**: Store in environment variables, not in code
- **CORS**: Enabled for local development
- **File Access**: Restricted to `data/` directory

---

**Status**: ✅ **INTEGRATION DOCUMENTED - READY FOR USE**

**Tags**: `#SIDERAI` `#WISEBASE` `#ROAMWISE` `#ROAMRESEARCH` `@JARVIS` `@LUMINA`
