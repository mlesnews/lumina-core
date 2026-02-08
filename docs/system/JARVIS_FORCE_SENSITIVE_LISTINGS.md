# JARVIS Force-Sensitive Listings System

## Overview

The JARVIS Force-Sensitive Listings System maintains active/live black/white/grey listings representing the three orders of Force-sensitives:

1. **Jedi (Light Side/White)** - Order, Balance, Harmony
   - Allowed, approved, safe operations
   - Whitelist entries

2. **Sith (Dark Side/Black)** - Chaos, Power, Domination
   - Forbidden, blocked, restricted operations
   - Blacklist entries

3. **Gray Jedi (Balance/Grey)** - @quant @bal, Chaos & Entropy in balance
   - Conditional, balanced, quantum state operations
   - Greylist entries with quantum balance tracking

## Force Orders

### Jedi (Light Side/White)
- **Alignment**: Order, Balance, Harmony
- **Listing Type**: Whitelist
- **Purpose**: Allowed, approved, safe operations
- **Examples**: Approved APIs, safe commands, trusted models

### Sith (Dark Side/Black)
- **Alignment**: Chaos, Power, Domination
- **Listing Type**: Blacklist
- **Purpose**: Forbidden, blocked, restricted operations
- **Examples**: Blocked APIs, dangerous commands, forbidden models

### Gray Jedi (Balance/Grey)
- **Alignment**: @quant @bal, Chaos & Entropy in balance
- **Listing Type**: Greylist
- **Purpose**: Conditional, balanced, quantum state operations
- **Features**:
  - **@quant Score**: Quantum state score (0.0 - 1.0)
  - **@bal Score**: Balance score (0.0 - 1.0)
  - **Chaos Score**: Measure of chaos (0.0 - 1.0)
  - **Entropy Score**: Measure of entropy (0.0 - 1.0)

## Quantum Balance Tracking

Gray Jedi (Grey) listings automatically calculate and track:

- **@quant Score**: Quantum state measurement (default: 0.50)
- **@bal Score**: Balance measurement (default: 0.50)
- **Chaos Score**: Chaos measurement (calculated dynamically)
- **Entropy Score**: Entropy measurement (calculated dynamically)

These scores represent the balance between order (Jedi) and chaos (Sith), with Gray Jedi maintaining equilibrium.

## Usage

### CLI Interface

```bash
# Show statistics
python scripts/python/jarvis_force_sensitive_listings.py --stats

# List all listings
python scripts/python/jarvis_force_sensitive_listings.py --list

# Add to blacklist (Sith)
python scripts/python/jarvis_force_sensitive_listings.py --add-black "Direct OpenAI API"

# Add to whitelist (Jedi)
python scripts/python/jarvis_force_sensitive_listings.py --add-white "Azure OpenAI"

# Add to greylist (Gray Jedi) - automatically calculates @quant, @bal, chaos, entropy
python scripts/python/jarvis_force_sensitive_listings.py --add-gray "GROK API"

# Check if a name is in listings
python scripts/python/jarvis_force_sensitive_listings.py --check "OpenAI"
```

### Programmatic Usage

```python
from scripts.python.jarvis_force_sensitive_listings import (
    get_force_listings,
    ForceOrder,
    ListingType
)

listings = get_force_listings()

# Add to blacklist (Sith)
listings.add_to_blacklist("Direct OpenAI API", "Blocked cloud API provider")

# Add to whitelist (Jedi)
listings.add_to_whitelist("Azure OpenAI", "Approved cloud API provider")

# Add to greylist (Gray Jedi) - automatically calculates quantum balance
entry = listings.add_to_greylist("GROK API", "Conditional access based on decision tree")
print(f"@quant: {entry.quant_score:.2f}, @bal: {entry.bal_score:.2f}")
print(f"Chaos: {entry.chaos_score:.2f}, Entropy: {entry.entropy_score:.2f}")

# Check a listing
result = listings.check_listing("OpenAI")
print(f"Listing: {result['listing_type']}")
print(f"Force Order: {result['force_order']}")
print(f"Status: {result['status']}")

# Get all listings
all_listings = listings.get_all_listings()
print(f"Jedi (Whitelist): {all_listings['statistics']['jedi_count']}")
print(f"Sith (Blacklist): {all_listings['statistics']['sith_count']}")
print(f"Gray Jedi (Greylist): {all_listings['statistics']['gray_jedi_count']}")
```

## Integration with Blacklist Enforcer

The Force-Sensitive Listings system integrates with the JARVIS Blacklist/Restriction Enforcer:

- **Sith (Black) listings** → Blocked operations
- **Jedi (White) listings** → Allowed operations
- **Gray Jedi (Grey) listings** → Conditional operations based on quantum balance

## Live Updates

The system maintains active/live listings with:
- Automatic periodic saves
- Quantum balance calculations for Grey listings
- Real-time status tracking

## Data Storage

Listings are stored in:
- **File**: `data/force_sensitive_listings/force_listings.json`
- **Format**: JSON with full listing details and quantum balance information

## Example Output

```
================================================================================
FORCE-SENSITIVE LISTINGS STATISTICS
================================================================================
⚪ Jedi (Whitelist): 1
⚫ Sith (Blacklist): 1
⚫⚪ Gray Jedi (Greylist): 2
Total: 4
================================================================================

================================================================================
JARVIS FORCE-SENSITIVE LISTINGS
================================================================================

⚪ JEDI (Whitelist): 1 entries
   - Azure OpenAI

⚫ SITH (Blacklist): 1 entries
   - Direct OpenAI API

⚫⚪ GRAY JEDI (Greylist): 2 entries
   - GROK API
     @quant: 0.50, @bal: 0.50
     Chaos: 0.66, Entropy: 1.00
================================================================================
```

## Tags

@JARVIS @DOIT @QUANT @BAL #FORCE #JEDI #SITH #GRAY_JEDI #CHAOS #ENTROPY #BALANCE
