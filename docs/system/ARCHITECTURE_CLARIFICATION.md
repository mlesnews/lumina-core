# Architecture Clarification - IDM & Download Management

**Date**: 2026-01-09  
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT  
**Status**: ⚠️ **ARCHITECTURE CLARIFICATION NEEDED**

## Current Situation

### IDM Usage
- **Currently**: IDM is being used **remotely on KAIJU** (via SSH)
- **Assumption**: IDM should be used **locally on FALC** (laptop)
- **Issue**: If laptop is remote, we need different approach

## System Architecture

### KAIJU_NO_8 (Desktop)
- **Location**: `10.17.17.11`
- **Role**: Primary LLM cluster (Iron Legion)
- **Storage**: D drive (primary), M drive (NAS)
- **IDM**: Currently installed and running
- **Status**: Remote access via SSH

### FALC / MILLENNIUM_FALCON (Laptop)
- **Location**: Local (this machine)
- **Role**: Secondary LLM cluster (PERSPECTIVE models)
- **Storage**: C drive (local)
- **IDM**: Should be used here for downloads
- **Status**: Local access

## Download Strategy

### Option 1: Local FALC (Current Assumption)
- ✅ Use IDM on FALC (laptop) locally
- ✅ Downloads managed by JARVIS
- ✅ Application noise filtered locally
- ✅ Direct file access

### Option 2: Remote FALC
- ⚠️ Cannot use IDM directly (remote)
- ⚠️ Need alternative: DSM Download Manager or direct download
- ⚠️ Or: Use IDM on KAIJU and transfer files

## Recommended Approach

### For Local FALC
1. **Use IDM on FALC** (laptop) for downloads
2. **JARVIS manages** download process
3. **Filter application noise** locally
4. **Direct file management**

### For Remote FALC
1. **Use NAS DSM Download Manager** (primary)
2. **Or use IDM on KAIJU** and transfer
3. **JARVIS coordinates** remotely
4. **Centralized management**

## Next Steps

1. ⚠️ Clarify FALC location (local vs remote)
2. ⚠️ Reconfigure download strategy based on location
3. ⚠️ Set up ProtonVPN on both hosts
4. ⚠️ Integrate JARVIS download management

---

**Last Updated**: 2026-01-09  
**Status**: ⚠️ **CLARIFICATION NEEDED**
