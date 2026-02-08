# NAS Migration Plan: 'my_projects' Dropbox to NAS

## Overview
**Ticket**: PM000003051  
**Status**: 🟢 **READY FOR EXECUTION**  
**Severity**: CRITICAL  

This document outlines the comprehensive plan to migrate the entire `my_projects` directory from Dropbox to the local NAS storage.

## Objectives
1. **Resolve Space Issues**: Move ~1TB+ of data off the primary C: drive.
2. **Centralize Data**: Move from cloud-synced Dropbox to local high-speed NAS storage.
3. **Maintain Stability**: Ensure all Lumina systems, JARVIS scripts, and path references continue to work seamlessly.

## Migration Strategy

### Phase 1: Pre-Flight Analysis
- ✅ **Path Audit**: Identify all hardcoded references to `C:/Users/mlesn/Dropbox/my_projects`.
- ✅ **Connectivity Test**: Verified high-speed SFTP/SSH access to `10.17.17.32`.
- ✅ **Counter Sync**: Synchronized Problem Management (PM) ticket range to `3050+`.

### Phase 2: Execution Protocol
1. **Robocopy Migration**: Use `fast_c_to_d_migration.ps1` (enhanced for NAS) to mirror the directory structure.
   - Command: `robocopy "C:\Users\mlesn\Dropbox\my_projects" "\\10.17.17.32\volume1\lumina_storage\my_projects" /MIR /MT:16 /R:3 /W:5`
2. **Verification**: Conduct a checksum validation of the top 10 most critical project folders.
3. **Path Re-pointing**: Update the project root environment variables (`CFS_PROJECT_DIR`, etc.) to point to the new NAS mount point.

### Phase 3: Post-Migration Handover
1. **Holocron Sync**: Update the Holocron index with the new primary data locations.
2. **Resumption Test**: Restart the **JARVIS Command Center** and verify it correctly detects the new paths.
3. **Dropbox De-link**: Once verified, the Dropbox sync can be disabled for the legacy `my_projects` folder.

## System Impact
- **JARVIS**: No impact expected; uses relative path logic.
- **MANUS**: Requires update to window focus logic if folder names change.
- **R5 Matrix**: Will automatically re-index the new location upon next heartbeat.

## Status Summary
- ✅ **Migration Ticket**: PM000003051 created.
- ✅ **Infrastructure**: NAS confirmed at 39TB free.
- ✅ **Automation**: Scripts ready for high-speed transfer.

---
*Maintained by Storage Engineering Team (@c3po, @r2d2)*
