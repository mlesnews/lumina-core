# Lumina Premium Addon/XPAC System

## Overview

All features in this session are part of the **@premium @lumina @addon @xpac** system with **#steammarketing** integration.

**Repository Destination:**
- All @premium features → **private_company_repo** + **premium_private_repo**
- All @addon features → **private_company_repo** + **premium_private_repo**
- All @xpac features → **private_company_repo** + **premium_private_repo**

**NOT in public repo** - These are premium/private features.

## Classification

**Important:** @xpac is for **Lumina v2.0+ versions** (major version upgrades), not individual feature packages. Individual features are @addon.

### @premium Features

Premium Lumina features requiring premium tier access:

1. **SYPHON Financial Strategies WOPR**
   - SYPHON extraction with WOPR pattern matching
   - Financial strategy intelligence extraction
   - Tags: @syphon, @wopr, @financial, @premium

2. **TradingView + 3commas Force Multiplier**
   - Deep mapping and integration
   - Critical force multiplier identification
   - Tags: @tradingview, @3commas, @force_multiplier, @premium

3. **Operator Input Learning System**
   - Track and learn from @op @inputs
   - Pattern recognition and consolidation detection
   - Tags: @op, @learning, @premium

### @addon Features

Lumina addons that extend core functionality (individual feature packages):

1. **Fidelity Investments SYPHON**
   - Fidelity stock trading, options, Tesla analysis
   - Microsoft Copilot (Money) integration
   - Tags: @fidelity, @tesla, @options, @addon

2. **Financial Life Domains Force Multipliers**
   - Complete financial life domain system
   - 10 domains, 25 force multipliers, 7 cross-domain integrations
   - Tags: @financial, @force_multiplier, @addon

### @addon Features (Updated)

Lumina addons that extend core functionality:

1. **Fidelity Investments SYPHON**
   - Fidelity stock trading, options, Tesla analysis
   - Microsoft Copilot (Money) integration
   - Tags: @fidelity, @tesla, @options, @addon

2. **Financial Life Domains Force Multipliers**
   - Complete financial life domain system
   - 10 domains, 25 force multipliers, 7 cross-domain integrations
   - Tags: @financial, @force_multiplier, @addon

### @xpac (Expansion Pack)

**@xpac is for Lumina v2.0+ versions ONLY** - Major version upgrades, not individual feature packages.

**Important Distinction:**
- **@addon** = Individual feature packages (like "Financial Life Domains Force Multipliers")
- **@xpac** = Lumina v2.0+ major version upgrades

Expansion packs represent major version milestones:
- Lumina v2.0+ = @xpac
- Major version upgrades
- Complete version releases
- Tags: @xpac, @lumina, #steammarketing, version: "v2.0+"

## Steam Marketing (#steammarketing)

All features are tracked for Steam marketing:
- Feature descriptions
- Tags and metadata
- Marketing materials
- DLC/expansion pack structure

## Registration

Features are automatically registered with:
- @premium tag for premium features
- @addon tag for addons
- @xpac tag for expansion packs
- #steammarketing tag for Steam marketing

## Usage

### Register Features

```python
from scripts.python.jarvis_lumina_premium_addon_tracker import LuminaPremiumAddonTracker

tracker = LuminaPremiumAddonTracker()

feature = {
    "name": "Feature Name",
    "type": "premium",  # or "addon" or "xpac"
    "description": "Feature description",
    "tags": ["@tag1", "@tag2"]
}

tracker.register_premium_feature(feature)
```

### Get Steam Marketing Data

```python
steam_data = tracker.get_steam_marketing_data()
# Returns all features with marketing metadata
```

## Tags

@JARVIS @PREMIUM @LUMINA @ADDON @XPAC #STEAMMARKETING
