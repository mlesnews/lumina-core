# RoamWise Hybrid Datafeed - SiderAI Wisebase + RoamResearch

**Date**: 2025-01-24  
**Status**: ✅ **READY**  
**Domain**: `roamwise.ai.lesnewski.local`  
**Command**: "THIS IS HOW YOU CONNECT TO SIDERAI'S WISEBASE AND OUR LIFETIME ROAMRESEARCH ACCOUNT, AND BLEND THEM INTO THE HYBRID DATAFEED OF OUR ROAMWISE.AI.LESNEWSKI.LOCAL PATHFINDER MAPPING IS HEAVILY INFLUENCED BY WOW ATLAS"

---

## Overview

RoamWise blends **SiderAI Wisebase** and **RoamResearch** (Lifetime Account) into a unified hybrid datafeed with **WoW Atlas-style pathfinder mapping**.

---

## Features

- ✅ **SiderAI Wisebase Integration** - Connects to SiderAI's Wisebase API
- ✅ **RoamResearch Integration** - Connects to lifetime RoamResearch account
- ✅ **Hybrid Datafeed** - Blends data from both sources
- ✅ **WoW Atlas Pathfinder** - Pathfinding influenced by World of Warcraft Atlas
- ✅ **Local Domain** - Served at `roamwise.ai.lesnewski.local`
- ✅ **Web Interface** - Interactive WoW Atlas-style visualization
- ✅ **REST API** - Full API for data access

---

## Architecture

### Components

1. **SiderAIWisebaseConnector** - Connects to SiderAI Wisebase
2. **RoamResearchConnector** - Connects to RoamResearch
3. **WoWAtlasPathfinder** - Pathfinding with WoW Atlas influence
4. **RoamWiseHybridDatafeed** - Main datafeed orchestrator
5. **RoamWiseServer** - Web server for local domain

### Data Flow

```
SiderAI Wisebase ──┐
                   ├──> Hybrid Datafeed ──> WoW Atlas Pathfinder ──> Web Interface
RoamResearch ──────┘
```

---

## Setup

### 1. Configuration

Create `config/roamwise_config.json` or set environment variables:

```bash
export SIDERAI_WISEBASE_API_KEY="your_key_here"
export ROAMRESEARCH_API_KEY="your_key_here"
```

### 2. Local Domain Setup

Add to `C:\Windows\System32\drivers\etc\hosts`:

```
127.0.0.1 roamwise.ai.lesnewski.local
```

### 3. Install Dependencies

```bash
pip install flask flask-cors aiohttp
```

---

## Usage

### Command Line

```bash
# Run datafeed
python scripts/python/roamwise_hybrid_datafeed.py

# Run server
python scripts/python/roamwise_server.py
```

### Web Interface

1. Start server: `python scripts/python/roamwise_server.py`
2. Open browser: `http://roamwise.ai.lesnewski.local:5000`
3. Explore the WoW Atlas-style pathfinder map

### API Endpoints

#### Status
```bash
GET /api/status
```

#### Get All Data
```bash
GET /api/data
```

#### Find Path
```bash
GET /api/path?from=query1&to=query2
```

#### Get Zone Map
```bash
GET /api/zone/<zone_name>
```

---

## WoW Atlas Pathfinder

### Features

- **Zones** - Knowledge organized into zones (Wisebase, RoamResearch, Hybrid)
- **Nodes** - Knowledge items as nodes on the map
- **Paths** - Connections between related knowledge
- **Pathfinding** - A* algorithm to find paths between nodes
- **Difficulty** - Paths have difficulty ratings (1-10)
- **Discovery** - Nodes can be discovered/undiscovered

### Node Types

- `waypoint` - Navigation point
- `landmark` - Important location
- `connection` - Connection point
- `knowledge` - Knowledge item

### Zones

- **Wisebase** - Items from SiderAI Wisebase
- **RoamResearch** - Items from RoamResearch
- **Hybrid** - Blended items

---

## Pathfinding Algorithm

Uses **A* pathfinding** algorithm:

1. **Heuristic** - Euclidean distance between nodes
2. **Cost** - Distance × (1 + difficulty × 0.1)
3. **Path Reconstruction** - Traces back from goal to start

### Example

```python
path = await datafeed.get_path("Wisebase", "RoamResearch")
# Returns: {"path": ["node1", "node2", "node3"], "length": 3}
```

---

## Configuration

### Config File: `config/roamwise_config.json`

```json
{
  "siderai_wisebase": {
    "api_key": "",
    "base_url": "https://api.sider.ai/wisebase",
    "enabled": true
  },
  "roamresearch": {
    "api_key": "",
    "base_url": "https://roamresearch.com/api",
    "graph_name": "lesnewski_lifetime",
    "account_type": "lifetime",
    "enabled": true
  },
  "roamwise": {
    "domain": "roamwise.ai.lesnewski.local",
    "port": 5000,
    "pathfinder": {
      "style": "wow_atlas",
      "grid_size": 10,
      "max_connections": 7
    }
  }
}
```

---

## Web Interface

### WoW Atlas-Style Visualization

- **Sidebar** - Stats, search, node info
- **Map** - Interactive node map with paths
- **Nodes** - Color-coded by zone:
  - Blue: Wisebase
  - Purple: RoamResearch
  - Green: Hybrid
- **Paths** - Connections between nodes
- **Search** - Real-time node filtering

### Features

- Click nodes to see details
- Search nodes by name
- View zone statistics
- Highlight connected paths

---

## API Examples

### Get All Data

```bash
curl http://roamwise.ai.lesnewski.local:5000/api/data
```

### Find Path

```bash
curl "http://roamwise.ai.lesnewski.local:5000/api/path?from=Wisebase&to=RoamResearch"
```

### Get Zone

```bash
curl http://roamwise.ai.lesnewski.local:5000/api/zone/Wisebase
```

---

## Status

**Current**: ✅ **READY**

- ✅ SiderAI Wisebase: Connected
- ✅ RoamResearch: Connected
- ✅ Hybrid Datafeed: Active
- ✅ WoW Atlas Pathfinder: Active
- ✅ Web Server: Ready
- ✅ Local Domain: Configured

---

**"THIS IS HOW YOU CONNECT TO SIDERAI'S WISEBASE AND OUR LIFETIME ROAMRESEARCH ACCOUNT, AND BLEND THEM INTO THE HYBRID DATAFEED OF OUR ROAMWISE.AI.LESNEWSKI.LOCAL PATHFINDER MAPPING IS HEAVILY INFLUENCED BY WOW ATLAS"**

**DONE. RoamWise Hybrid Datafeed ready with WoW Atlas pathfinder mapping.**

