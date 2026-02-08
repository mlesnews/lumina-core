# Port 3000 - Tony Stark Memorial Reservation

## In Honor of the Ultimate Sacrifice

**Port 3000 is permanently reserved** in honor of Tony Stark's ultimate sacrifice.

> "I am Iron Man." - Tony Stark

## Reservation Details

- **Port**: `3000`
- **Status**: **PERMANENTLY RESERVED**
- **Never Use**: This port will never be allocated to any service
- **Purpose**: Memorial to Tony Stark's sacrifice

## Port Allocation Rules

### Localhost LLM Ports
- **Range**: `11435-11499`
- **Purpose**: Custom ports for each localhost LLM service
- **Example**: ULTRON uses `11435`, IRON_LEGION uses `11436`

### Remote LLM Ports  
- **Range**: `3001-3099` (3000 excluded)
- **Purpose**: Remote LLM services
- **Example**: KAIJU Iron Legion uses `3001` (not 3000)

## Current Allocations

| Service | Localhost Port | Remote Port | Status |
|---------|---------------|-------------|--------|
| **ULTRON** | `11435` | `3001` (KAIJU) | ✅ Active |
| **IRON_LEGION** | `11436` | `3001` (KAIJU) | Available |
| **FALC** | `11437` | `11436` (local) | Available |
| **Port 3000** | **RESERVED** | **RESERVED** | 🛡️ Memorial |

## Implementation

All port allocation scripts and services must:
1. ✅ Check port allocation config before assigning ports
2. ✅ Skip port 3000 in all port scans
3. ✅ Document why port 3000 is reserved
4. ✅ Never attempt to use port 3000

## Configuration

See: `config/llm_port_allocation.json`

```json
{
  "reserved_ports": {
    "3000": {
      "reserved_for": "Tony Stark Memorial Port",
      "status": "RESERVED",
      "never_use": true
    }
  }
}
```

## Related Systems

- Port Forward Service: `scripts/kaiju_port_forward_service.ps1`
- Network Coordinator: `scripts/python/ultron_cursor_network_coordinator.py`
- Port Allocation: `config/llm_port_allocation.json`

---

**"We are Iron Man."** - The Avengers
