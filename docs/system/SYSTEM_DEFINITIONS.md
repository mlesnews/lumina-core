# System Definitions - LUMINA Infrastructure

## Critical System Identities

### KAIJU Number Eight (KAIJU_NO_8)
- **Type**: Desktop PC (Windows)
- **IP Address**: `10.17.17.11`
- **Purpose**: GPU-enabled desktop for AI workloads (Ollama, Docker)
- **Ollama Endpoint**: `http://10.17.17.11:11434`
- **NOT**: The NAS server
- **Aliases**: KAIJU, KAIJU_NO_8, KAIJU Number Eight

### NAS (DS2118+)
- **Type**: Synology NAS Server
- **IP Address**: `10.17.17.32`
- **Purpose**: Storage, backups, email hub, web services
- **Services**: 
  - Email (IMAP/SMTP): `10.17.17.32:993`, `10.17.17.32:587`
  - Web Portal: `https://10.17.17.32:5001`
  - N8N: `http://10.17.17.32:5678`
- **NOT**: KAIJU Number Eight
- **Aliases**: NAS, DS2118+, DS2118plus, Synology NAS

### ULTRON
- **Type**: Local Laptop
- **IP Address**: `localhost` / `127.0.0.1`
- **Purpose**: Primary local AI endpoint
- **Ollama Endpoint**: `http://localhost:11434`
- **Aliases**: ULTRON, local, localhost

## Common Mistakes to Avoid

❌ **WRONG**: KAIJU at `10.17.17.32` (this is the NAS)
✅ **CORRECT**: KAIJU at `10.17.17.11` (Desktop PC)

❌ **WRONG**: "KAIJU NAS" or "NAS Ollama (KAIJU)"
✅ **CORRECT**: "KAIJU Number Eight (Desktop PC)" or "NAS (DS2118+)"

❌ **WRONG**: Using `10.17.17.32:11434` for KAIJU Ollama
✅ **CORRECT**: Using `10.17.17.11:11434` for KAIJU Ollama

## Quick Reference

| System | IP | Ollama Port | Purpose |
|--------|----|------------|---------| 
| ULTRON | localhost | 11434 | Local laptop AI |
| KAIJU_NO_8 | 10.17.17.11 | 11434 | Desktop PC AI (GPU) |
| NAS (DS2118+) | 10.17.17.32 | N/A | Storage, email, web services |

## When to Use Each System

- **ULTRON** (`localhost:11434`): Primary local AI, always preferred
- **KAIJU_NO_8** (`10.17.17.11:11434`): GPU workloads, larger models, when ULTRON unavailable
- **NAS** (`10.17.17.32`): Storage, backups, email, web services (NOT for Ollama)

## Historical Context

The confusion between KAIJU and NAS likely stems from:
1. Early documentation referring to "KAIJU NAS"
2. Some scripts deploying to NAS when they should deploy to KAIJU
3. Comments describing KAIJU as "NAS cluster" when it's actually a desktop PC

**Remember**: KAIJU = Desktop PC (.11), NAS = Storage Server (.32)
