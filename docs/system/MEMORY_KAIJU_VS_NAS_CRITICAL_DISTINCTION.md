# MEMORY: KAIJU vs NAS - CRITICAL SYSTEM DISTINCTION
**Priority: +++++ (5/5 - HIGHEST)**
**Category: System Architecture / Infrastructure**
**Last Updated**: 2025-01-02

## ⚠️ CRITICAL: NEVER CONFUSE THESE SYSTEMS

### KAIJU Number Eight (KAIJU_NO_8)
- **Type**: Desktop PC (Windows)
- **IP Address**: `10.17.17.11`
- **Ollama Endpoint**: `http://10.17.17.11:11434`
- **Purpose**: GPU-enabled desktop for AI workloads (Ollama, Docker)
- **Aliases**: KAIJU, KAIJU_NO_8, KAIJU Number Eight
- **NOT**: The NAS server

### NAS (DS2118+)
- **Type**: Synology NAS Server
- **IP Address**: `10.17.17.32`
- **Purpose**: Storage, backups, email hub, web services
- **Services**: 
  - Email (IMAP/SMTP): `10.17.17.32:993`, `10.17.17.32:587`
  - Web Portal: `https://10.17.17.32:5001`
  - N8N: `http://10.17.17.32:5678`
- **Ollama**: ❌ NOT an Ollama endpoint
- **Aliases**: NAS, DS2118+, DS2118plus, Synology NAS
- **NOT**: KAIJU or an AI endpoint

## 🚨 COMMON MISTAKES TO AVOID

### ❌ WRONG
- KAIJU at `10.17.17.32` (this is the NAS)
- "KAIJU NAS" or "NAS Ollama (KAIJU)"
- Using `10.17.17.32:11434` for KAIJU Ollama
- Treating KAIJU as if it were the NAS server

### ✅ CORRECT
- KAIJU at `10.17.17.11` (Desktop PC)
- "KAIJU Number Eight (Desktop PC)" or "KAIJU_NO_8"
- Using `10.17.17.11:11434` for KAIJU Ollama
- KAIJU = Desktop PC, NAS = Storage Server (separate systems)

## 📋 Quick Reference Table

| System | IP | Ollama | Purpose |
|--------|----|--------|---------|
| **ULTRON** | localhost | ✅ | Local laptop AI |
| **KAIJU_NO_8** | 10.17.17.11 | ✅ | Desktop PC AI (GPU) |
| **NAS (DS2118+)** | 10.17.17.32 | ❌ | Storage, email, web services |

## 🔍 Historical Context

**Root Cause**: Early documentation incorrectly described KAIJU as being on the NAS or as "KAIJU NAS", leading to widespread confusion across 887+ code references.

**Resolution**: Critical files have been corrected. Always refer to `docs/system/SYSTEM_DEFINITIONS.md` when adding new code.

## 📝 Code Guidelines

When writing code that references these systems:

1. **Always use explicit comments**:
   ```python
   # KAIJU Number Eight (Desktop PC at 10.17.17.11), NOT NAS
   kaiju_endpoint = "http://10.17.17.11:11434"
   ```

2. **Never use "KAIJU NAS"** - use:
   - "KAIJU Number Eight"
   - "KAIJU_NO_8"
   - "KAIJU (Desktop PC)"

3. **Verify IP addresses**:
   - KAIJU = `.11`
   - NAS = `.32`

4. **Check endpoint usage**:
   - KAIJU Ollama = `10.17.17.11:11434`
   - NAS services = `10.17.17.32` (various ports, NOT 11434)

## 🎯 When to Use Each System

- **ULTRON** (`localhost:11434`): Primary local AI, always preferred
- **KAIJU_NO_8** (`10.17.17.11:11434`): GPU workloads, larger models, when ULTRON unavailable
- **NAS** (`10.17.17.32`): Storage, backups, email, web services (NOT for Ollama)

## 🔗 Related Documentation

- `docs/system/SYSTEM_DEFINITIONS.md` - Complete system definitions
- `docs/system/KAIJU_NAS_CLARIFICATION.md` - Root cause analysis
- `docs/system/KAIJU_NAS_CONFUSION_REPORT.md` - Diagnostic report

## ⚡ Remember

**KAIJU = Desktop PC (.11), NAS = Storage Server (.32)**

This distinction is **CRITICAL** for:
- Correct endpoint configuration
- Proper system routing
- Accurate documentation
- Avoiding connection errors

**NEVER CONFUSE THESE SYSTEMS AGAIN.**
