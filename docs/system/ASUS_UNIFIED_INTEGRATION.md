# ASUS Unified Integration (@ASUS_UI)

**Short Name**: `@ASUS_UI` or `@ASUS_UNIFIED`

## Overview

Unified integration for ASUS Armoury Crate + MyASUS. Provides a single interface to both systems.

**Previous Name**: `ArmouryCrateMyASUSHybrid` (too long! 😅)

## Usage

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate_myasus_hybrid import create_hybrid_integration

# Create unified integration
asus_ui = create_hybrid_integration()

# Use it
result = await asus_ui.process_request({
    "action": "hybrid",  # Get data from both AC + MyASUS
    "source": "auto"
})
```

## Features

- **Armoury Crate**: Lighting, performance, macros, gaming
- **MyASUS**: Diagnostics, updates, support, optimization
- **Unified**: Single interface for both

## Short Tags

- `@ASUS_UI` - Primary short name
- `@ASUS_UNIFIED` - Alternative short name
