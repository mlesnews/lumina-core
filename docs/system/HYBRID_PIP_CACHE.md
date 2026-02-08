# Hybrid Pip Cache - Implementation

**Date**: 2026-01-14
**Status**: ✅ **IMPLEMENTED**
**Tags**: `#PIP` `#CACHE` `#HYBRID` `#NAS` `#FALLBACK` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Strategy: Local Primary → NAS Fallback

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Pip Cache Request                     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  Check Local Cache   │
            │  (Primary)           │
            └──────┬───────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
    ✅ Available          ❌ Unavailable
        │                     │
        ▼                     ▼
┌───────────────┐    ┌──────────────────┐
│ Use Local     │    │ Check NAS Cache  │
│ (Fast)        │    │ (Fallback)       │
└───────────────┘    └──────┬───────────┘
                            │
                    ┌───────┴────────┐
                    │                │
                ✅ Available    ❌ Unavailable
                    │                │
                    ▼                ▼
            ┌──────────────┐  ┌──────────────┐
            │ Use NAS      │  │ Use Local    │
            │ (Fallback)   │  │ (Forced)     │
            └──────────────┘  └──────────────┘
```

---

## ✅ Implementation

### Core Components

**1. Hybrid Cache Manager**
- **File**: `scripts/python/hybrid_pip_cache_manager.py`
- **Function**: Manages local (primary) and NAS (fallback) caches
- **Features**:
  - Auto-detects cache availability
  - Automatic fallback
  - Optional cache syncing
  - Status reporting

**2. Setup Script**
- **File**: `scripts/powershell/setup_hybrid_pip_cache.ps1`
- **Function**: One-time setup and configuration
- **Usage**: Run once to configure hybrid cache

---

## 🚀 Usage

### Initial Setup

```powershell
# Run setup script
.\scripts\powershell\setup_hybrid_pip_cache.ps1
```

This will:
1. Check local and NAS cache availability
2. Configure pip to use hybrid cache
3. Set local as primary, NAS as fallback

### Check Status

```powershell
python scripts/python/hybrid_pip_cache_manager.py --status
```

**Output**:
```
============================================================
HYBRID PIP CACHE STATUS
============================================================

Local Cache:
  Path: C:\Users\mlesn\AppData\Local\pip\cache
  Status: ✅ Available

NAS Cache:
  Path: \\10.17.17.32\data\cache\pip
  Status: ❌ Unavailable (VPN required?)

Active Cache:
  Path: C:\Users\mlesn\AppData\Local\pip\cache
  Type: local
  Primary: local
============================================================
```

### Configure Cache

```powershell
# Configure with local primary
python scripts/python/hybrid_pip_cache_manager.py --configure --primary local

# Configure with NAS primary (if VPN available)
python scripts/python/hybrid_pip_cache_manager.py --configure --primary nas
```

### Sync Caches (Optional)

```powershell
# Sync local → NAS (for sharing)
python scripts/python/hybrid_pip_cache_manager.py --sync --direction local_to_nas

# Sync NAS → local (download shared cache)
python scripts/python/hybrid_pip_cache_manager.py --sync --direction nas_to_local

# Bidirectional sync
python scripts/python/hybrid_pip_cache_manager.py --sync --direction bidirectional
```

---

## 🔧 How It Works

### 1. Cache Detection

**Local Cache**:
- Path: `C:\Users\mlesn\AppData\Local\pip\cache`
- Check: File system write test
- Always available (unless disk full)

**NAS Cache**:
- Path: `\\10.17.17.32\data\cache\pip`
- Check: Network path accessibility + write test
- Available when: VPN connected, NAS accessible

### 2. Fallback Logic

**Primary: Local** (Default):
1. Check local cache availability
2. If available → use local (fast)
3. If unavailable → check NAS
4. If NAS available → use NAS (fallback)
5. If both unavailable → use local (forced, may fail)

**Primary: NAS** (Optional):
1. Check NAS cache availability
2. If available → use NAS (shared)
3. If unavailable → check local
4. If local available → use local (fallback)
5. If both unavailable → use NAS (forced, may fail)

### 3. Configuration

**Environment Variable** (Takes Precedence):
```powershell
$env:PIP_CACHE_DIR = "C:\Users\mlesn\AppData\Local\pip\cache"
```

**Pip Config** (Backup):
```ini
[global]
cache-dir = C:\Users\mlesn\AppData\Local\pip\cache
```

---

## 📊 Scenarios

### Scenario 1: Normal Operation (On-site)

**Status**:
- Local: ✅ Available
- NAS: ✅ Available (optional)

**Behavior**:
- Uses local cache (fast)
- NAS available for sharing (if sync enabled)

### Scenario 2: Remote Work (VPN Connected)

**Status**:
- Local: ✅ Available
- NAS: ✅ Available (via VPN)

**Behavior**:
- Uses local cache (fast, no VPN latency)
- NAS available for fallback or sharing

### Scenario 3: Remote Work (No VPN)

**Status**:
- Local: ✅ Available
- NAS: ❌ Unavailable (no VPN)

**Behavior**:
- Uses local cache (works offline)
- NAS unavailable (expected)

### Scenario 4: Local Cache Full/Unavailable

**Status**:
- Local: ❌ Unavailable (disk full or error)
- NAS: ✅ Available

**Behavior**:
- Automatically falls back to NAS
- Logs warning about fallback
- Continues working

### Scenario 5: Both Unavailable

**Status**:
- Local: ❌ Unavailable
- NAS: ❌ Unavailable

**Behavior**:
- Uses local (forced, may fail)
- Logs error
- Pip operations may fail

---

## 🔄 Cache Syncing (Optional)

### When to Sync

**Sync Local → NAS**:
- After installing packages locally
- To share cache with other machines
- Before going remote (if you want NAS cache)

**Sync NAS → Local**:
- When joining new machine
- To download shared cache
- After NAS cache updated by others

**Bidirectional Sync**:
- Keep both caches in sync
- Share across machines
- Redundancy

### Sync Process

**What Gets Synced**:
- `wheels/` - Built wheel files
- `http/` - HTTP cache (older pip)
- `http-v2/` - HTTP cache (pip 23.3+)

**Sync Logic**:
- Only syncs if file doesn't exist in destination
- Or if source is newer than destination
- Preserves timestamps

---

## ✅ Benefits

### Performance
- ✅ **Fast**: Uses local cache when available (no network latency)
- ✅ **Reliable**: Falls back to NAS if local unavailable
- ✅ **Offline**: Works without VPN for local cache

### Flexibility
- ✅ **Automatic**: No manual switching needed
- ✅ **Adaptive**: Detects availability and adjusts
- ✅ **Configurable**: Can set primary to local or NAS

### Sharing
- ✅ **Optional Sync**: Share cache across machines
- ✅ **NAS Access**: Multiple machines can use NAS cache
- ✅ **Redundancy**: Both caches available

### Disk Space
- ✅ **Local Primary**: Minimal local disk usage (typical 100MB-2GB)
- ✅ **NAS Fallback**: Can use NAS when local full
- ✅ **Optional NAS**: Only uses NAS when needed

---

## 📋 Configuration Options

### Primary Cache

**Local** (Recommended):
- Fast, always available
- Works offline
- No VPN needed

**NAS**:
- Shared across machines
- Saves local disk space
- Requires VPN when remote

### Sync Settings

**Disabled** (Default):
- No syncing
- Each cache independent
- Faster (no sync overhead)

**Enabled**:
- Sync on demand
- Share cache across machines
- Useful for team environments

---

## 🚨 Troubleshooting

### Issue: NAS Not Available

**Symptoms**: Status shows NAS unavailable

**Solutions**:
1. Connect to VPN (if remote)
2. Check NAS accessibility: `Test-Path "\\10.17.17.32\data\"`
3. Verify network connection
4. Use local cache only (works fine)

### Issue: Local Cache Full

**Symptoms**: Local cache unavailable, falls back to NAS

**Solutions**:
1. Clean local cache: `pip cache purge`
2. Increase local disk space
3. Use NAS as primary (if VPN available)
4. Sync to NAS and clear local

### Issue: Sync Fails

**Symptoms**: Sync command fails

**Solutions**:
1. Check VPN connection (if remote)
2. Verify NAS path accessible
3. Check write permissions
4. Run sync with verbose logging

---

## 📝 Summary

**Strategy**: ✅ **Local Primary → NAS Fallback**

**Implementation**: ✅ **Complete**

**Status**: ✅ **Ready to Use**

**Benefits**:
- Fast local cache (primary)
- Automatic NAS fallback
- Optional cache sharing
- Works offline
- VPN-independent for local operations

---

**Status**: ✅ **HYBRID CACHE IMPLEMENTED**
**Primary**: ✅ **LOCAL (FAST)**
**Fallback**: ✅ **NAS (SHARED)**
**Tags**: `#PIP` `#CACHE` `#HYBRID` `#NAS` `#FALLBACK` `@LUMINA` `@JARVIS` `#PEAK`
