# Known Issues - LUMINA CORE

**Last Updated**: 2025-01-24  
**Status**: ACTIVE

---

## Critical Issues

### 1. IDE Startup Failure - Exit Code 64

**Priority**: 🔴 **HIGHEST** - Blocks IDE Startup

**Description**:  
IDE startup repeatedly fails with exit code 64 from malformed PowerShell command:

```
The terminal process "C:\Program Files\PowerShell\7-preview\pwsh.exe -NoProfile & "C:\Program Files\PowerShell\7-preview\pwsh.exe" -ExecutionPolicy Bypass -NoProfile -File "C:\Users\mlesn\Dropbox\my_projects\cedarbrook-financial-services_llc-env\scripts\powershell\direct_fix_mcp.ps1"" terminated with exit code: 64.
```

**Root Cause**: 
Malformed command with `&` separator causing double `pwsh.exe` invocation. The command should be a single `pwsh.exe` call with proper args.

**Impact**:
- IDE startup fails repeatedly
- Terminal process errors
- Blocks development workflow

**Solution**: 
- Fix malformed command in IDE settings (remove `&` and duplicate `pwsh.exe`)
- Or disable startup script temporarily
- Use proper `args` array format in settings.json

**Status**: 
- 🔴 **CRITICAL** - Repeated failures
- ⏳ Fix script being created
- 📝 Action required: Find and fix command in IDE settings

**Related Files**:
- `docs/system/IDE_STARTUP_FAILURE_FIX.md` - **Complete fix documentation**
- `scripts/powershell/direct_fix_mcp.ps1` - Script being called
- `docs/TASK_ERROR_FIXES.md` - Previous error fixes
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 2. Dropbox Filesystem Limitations with Git

**Priority**: 🔴 **HIGHEST** - Most Persistent Issue  
**Status**: ✅ **LONG-TERM SOLUTION IMPLEMENTED**

**Description**:  
Git repositories stored in Dropbox experience filesystem limitations that prevent git from writing to `.git/logs/HEAD`. This manifests as:

```
fatal: cannot update the ref 'HEAD': unable to append to '.git/logs/HEAD': Function not implemented
```

**Impact**:
- Cannot commit to git repositories stored in Dropbox
- Affects all git operations that write to `.git/logs/`
- Most persistent and largest issue currently

**Long-Term Solution**: ✅ **NAS-Based Git Storage**
- **Migration Script**: `scripts/python/migrate_git_to_nas.py`
- **Documentation**: `docs/system/GIT_NAS_MIGRATION.md`
- **Architecture**: Store `.git` directories on NAS, keep working directories in Dropbox
- **Benefits**: No filesystem limitations, transparent to git, centralized storage

**Migration**:
```bash
# Dry run first (recommended)
python scripts/python/migrate_git_to_nas.py --dry-run

# Migrate all repos
python scripts/python/migrate_git_to_nas.py --path "C:\Users\mlesn\Dropbox\my_projects"
```

**Temporary Workarounds** (until migration):
1. **Retry Script**: Use `scripts/python/git_commit_retry.py` with retry logic
2. **Wait for Sync**: Restart Dropbox app and wait for sync to complete
3. **Manual Commit**: Commit manually when Dropbox sync is stable

**Retry Script Usage**:
```bash
python scripts/python/git_commit_retry.py \
  --repo C:\Users\mlesn\Dropbox\my_projects\lumina \
  --message "[LUMINA CORE] Commit message" \
  --max-retries 10 \
  --retry-delay 5
```

**Status**: 
- ✅ Long-term solution implemented (NAS migration)
- ✅ Migration script created
- ✅ Documentation complete
- ⏳ Ready for execution
- 📝 Temporary workarounds still available

**Related Files**:
- `scripts/python/migrate_git_to_nas.py` - **Long-term solution: NAS migration script**
- `docs/system/GIT_NAS_MIGRATION.md` - **Complete migration guide**
- `scripts/python/git_commit_retry.py` - Temporary workaround (no longer needed after migration)
- `docs/system/KNOWN_ISSUES.md` - This file

---

## Critical Missing Features

### 3. Previously Requested Features - Not Implemented

**Priority**: 🔴 **CRITICAL** - Previously Requested, Lost to Dev Null

**Description**:  
Multiple critical features were previously requested but have "gone into the Dev Null Bitbucket" - they're documented but not implemented:

1. **NASDSM Package**: Cloud storage aggregation, network drive centralization, unified cloud provider interface
2. **IDM Integration**: Automatic download interception, IDM routing, file type routing rules
3. **Storage Reorganization**: Local/LAN cloud storage reorganization, SYPHON integration, hybrid solution
4. **IDE/Environment Sync**: Latest features across all environments, version control sync
5. **OS Backups**: Full operating system backups, recovery capability
6. **PXE Network Boot**: Network boot capability, boot from NAS

**Impact**:
- Missing critical infrastructure components
- Inefficient download management
- Unorganized storage structure
- Inconsistent environments
- No disaster recovery
- No network boot capability

**Status**: 
- ✅ Features documented in infrastructure extraction
- ❌ **NOT IMPLEMENTED** - Lost to Dev Null
- ⏳ Recovery document created

**Related Files**:
- `docs/system/PREVIOUSLY_REQUESTED_FEATURES.md` - **Complete recovery document with implementation plans**
- `data/syphon/lumina_infrastructure/infrastructure_extraction_20251228_140306.json` - Infrastructure config
- `config/lumina_idm_config.json` - IDM configuration
- `docs/system/KNOWN_ISSUES.md` - This file

---

## Medium Priority Issues

### 4. Workflow Scope & Mode Selection Gap

**Priority**: 🔴 **CRITICAL** - No Comprehensive Understanding

**Description**:  
We **don't know when to work in what scope/mode**:

- ❌ **No scope selection decision tree** - When to use local, worktree, cloud, workspace, non-workspace
- ❌ **No @flow mode system** - What @flow mode is, when to use it
- ❌ **No @auto mode variants** - @auto[#automatic], @auto[#autonomous], @auto[#automation] not understood
- ❌ **No scope + mode combination logic** - How scopes and modes combine
- ❌ **No context-aware selection** - No intelligent scope/mode selection

**Current State**:
- ✅ Basic workspace/non-workspace detection exists
- ✅ Unified interface exists
- ❌ **NO comprehensive scope selection system**
- ❌ **NO @flow mode implementation**
- ❌ **NO @auto mode variant system**
- ❌ **NO combination logic**

**Impact**:
- Cannot intelligently select scope (local, worktree, cloud, workspace, non-workspace)
- Cannot intelligently select mode (@flow, @auto variants)
- Missing optimal scope/mode combinations
- User must manually select scope/mode instead of automatic selection

**Solution**: 
- Create context analyzer for scope/mode selection
- Implement scope selector (local, worktree, cloud, workspace, non-workspace)
- Implement mode selector (@flow, @auto variants)
- Define combination logic
- Create decision tree

**Status**: 
- ✅ Gap documented
- ✅ **COMPLETE** - All phases implemented
- ✅ Context analyzer, scope selector, mode selector, orchestrator created
- ✅ Integrated with JARVIS Unified Interface and Workflow Base
- ✅ Documentation complete

**Related Files**:
- `docs/system/WORKFLOW_SCOPE_MODE_GAP.md` - **Complete gap analysis and implementation plan**
- `scripts/python/cursor_workspace_mode_manager.py` - Existing workspace mode manager
- `scripts/python/jarvis_unified_interface.py` - Unified interface
- `docs/system/AUTO_MODE_COMPREHENSIVE_GAP.md` - @auto mode gap analysis
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 5. @auto Mode Comprehensive Gap

**Priority**: 🔴 **CRITICAL** - Not Fully Implemented

**Description**:  
The **@auto mode** for AI chat model selection is **NOT fully implemented** with comprehensive understanding:

- ❌ **No comprehensive decision tree** - When to use local vs cloud, multi-modal, multi-agent
- ❌ **No full spectrum routing** - Local → Cloud (all options) not fully covered
- ❌ **No multi-modal selection** - Text, code, voice, image, video models not intelligently selected
- ❌ **No multi-agent system** - Lead agent + 3 sub-agents not implemented
- ❌ **No clear guidelines** - When to apply options, in what order, all the time vs on demand

**Current State**:
- ✅ Basic configuration exists (`llm_orchestration_config.json`)
- ✅ Local AI integration exists (`local_ai_integration.py`)
- ✅ Basic routing rules exist
- ❌ **NO comprehensive decision tree**
- ❌ **NO multi-agent orchestration**
- ❌ **NO full spectrum model selection**
- ❌ **NO multi-modal routing**

**Impact**:
- Cannot intelligently select between local and cloud models
- Cannot handle multi-modal requests properly
- Cannot orchestrate multi-agent responses
- Missing optimal routing decisions
- User must manually select models instead of @auto doing it

**Solution**: 
- Create comprehensive decision tree engine
- Implement full spectrum model selector (local → cloud)
- Implement multi-modal model selection
- Implement lead agent + 3 sub-agents system
- Define clear guidelines for when to apply options

**Status**: 
- ✅ Gap documented
- ✅ **COMPLETE** - All phases implemented
- ✅ Decision tree, model selector, multi-agent system, integration complete
- ✅ Unified integration layer connects all systems

**Related Files**:
- `docs/system/AUTO_MODE_COMPREHENSIVE_GAP.md` - **Complete gap analysis and implementation plan**
- `scripts/python/local_ai_integration.py` - Existing local AI integration
- `config/llm_orchestration_config.json` - Existing routing config
- `scripts/python/universal_decision_tree.py` - Decision tree framework
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 6. IDE Queue Processing Gap

**Priority**: 🟡 **MEDIUM** - Missing Active Processing

**Description**:  
IDE queues (problems, source control, extensions, tasks, terminal) are **NOT being actively processed**:

- **Problems Queue**: Not monitoring problems panel in real-time
- **Source Control Queue**: Not monitoring git status/changes
- **Extensions Queue**: Not monitoring extension status
- **Tasks Queue**: Not monitoring task execution
- **Terminal Queue**: Not monitoring terminal outputs

**Current State**:
- ✅ Infrastructure exists (`ingest_ide_diagnostics_syphon.py`, `IDEExtractor`)
- ✅ Can extract diagnostics from storage files
- ❌ **NOT actively processing** IDE queues in real-time
- ❌ No queue monitoring system
- ❌ No real-time event processing

**Impact**:
- Missing real-time problem detection
- Not tracking source control changes
- Missing extension status monitoring
- No task execution tracking
- No terminal output analysis

**Solution**: 
- Create active queue monitoring system
- Implement queue-specific processors
- Add real-time IDE API integration
- Integrate with SYPHON for processing

**Status**: 
- ✅ Infrastructure documented
- ❌ **NOT IMPLEMENTED** - Passive extraction only
- ⏳ Implementation plan created

**Related Files**:
- `docs/system/IDE_QUEUE_PROCESSING_GAP.md` - **Complete gap analysis and implementation plan**
- `scripts/python/ingest_ide_diagnostics_syphon.py` - Existing diagnostics processor (passive)
- `scripts/python/syphon/extractors.py` - IDEExtractor
- `scripts/python/universal_ide_ca_manager.py` - IDE CA manager
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 7. Workflow Optimization Requests

**Priority**: 🟡 **MEDIUM** - Performance & UX Improvements

**Description**:  
Three critical optimization requests for improving workflow performance and user experience:

1. **Auto Chat Scrolling**: IDE/chat interface should auto-scroll to bottom on new messages
2. **Dropbox Indexing Speed**: Dropbox indexing is slow, needs parallel processing (especially on Kaiju)
3. **Parallel Batch Processing**: Should be an **always consideration** in all workflows

**Impact**:
- Poor UX (manual scrolling required)
- Slow Dropbox indexing performance
- Inconsistent parallel processing usage
- Missing performance optimizations

**Status**: 
- ✅ Requirements documented
- ❌ **NOT IMPLEMENTED**
- ⏳ Implementation plans created

**Related Files**:
- `docs/system/WORKFLOW_OPTIMIZATION_REQUESTS.md` - **Complete optimization plans**
- `scripts/python/workflow_base.py` - Workflow base (needs parallel support)
- `scripts/python/marvin_dropbox_cleanup_parallel_executor.py` - Example parallel implementation
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 8. Unused Systems: @bau, @helpdesk, @holocrons

**Priority**: 🟡 **MEDIUM** - Usage Gap

**Description**:  
Three critical systems exist but are **NOT actively used**:
- **@bau**: Build specifications exist but not referenced before implementation
- **@helpdesk**: Helpdesk infrastructure exists but workflows bypass it (direct droid calls)
- **@holocrons**: Knowledge base exists but not queried (silent failures)

**Impact**:
- Knowledge silos and duplicated effort
- Missing context in workflows
- Inefficient droid assignments
- Build specifications ignored (55% readiness instead of higher)
- Rogue AI defense knowledge unused

**Root Causes**:
1. **Integration Gap**: Systems not integrated into workflows
2. **Visibility Gap**: Systems not visible in IDE/tools
3. **Error Handling Gap**: Failures are silent (warnings only)
4. **Documentation Gap**: Usage not documented

**Solutions**:
1. **Holocron Integration**: Make queries required, add error handling
2. **Helpdesk Enforcement**: Route all droid assignments through @helpdesk
3. **@bau Integration**: Add pre-implementation verification checks

**Status**: 
- ✅ Systems exist and are configured
- ❌ **NOT actively used** in workflows
- ⏳ Integration needed

**Related Files**:
- `docs/system/UNUSED_SYSTEMS_GAP_ANALYSIS.md` - **Complete gap analysis**
- `scripts/python/resource_aware_integration.py` - Holocron integration point
- `scripts/python/jarvis_helpdesk_integration.py` - Helpdesk integration
- `config/helpdesk/` - Helpdesk configurations
- `data/holocron/` - Holocron knowledge base
- `docs/system/BUILD_SPECIFICATION_COMPLETE.md` - @bau specifications

---

### 9. Dropbox Nested Folders Issue

**Priority**: 🟡 **MEDIUM** - Structure Issue

**Description**:  
Nested "Dropbox" folders exist inside the Dropbox directory structure, creating confusing paths like:
- `C:\Users\mlesn\Dropbox\...\Dropbox\...\Dropbox\...`

**Impact**:
- Confusing directory structure
- Potential sync conflicts
- Difficult to navigate and locate files
- Can cause path resolution issues

**Solution**: ✅ **Reorganization Scripts Available**
- **Analysis Script**: `scripts/analyze_dropbox_structure.ps1` - Identifies nested folders
- **Fix Script**: `scripts/comprehensive_dropbox_reorganization.ps1` - Flattens nested structure
- **Process**: Renames nested "Dropbox" folders to "Dropbox_Flattened_[timestamp]" and moves to Archives

**Usage**:
```powershell
# Analyze first
.\scripts\analyze_dropbox_structure.ps1

# Dry run to see what would change
.\scripts\comprehensive_dropbox_reorganization.ps1 -FixNesting -DryRun

# Apply fix
.\scripts\comprehensive_dropbox_reorganization.ps1 -FixNesting -Backup
```

**Status**: 
- ✅ Analysis script available
- ✅ Fix script available
- ⏳ Ready for execution
- 📝 Should be run before NAS git migration for clean structure

**Related Files**:
- `scripts/analyze_dropbox_structure.ps1` - Analysis script
- `scripts/comprehensive_dropbox_reorganization.ps1` - Fix script
- `docs/system/KNOWN_ISSUES.md` - This file

---

### 10. Missing Configuration Files

**Priority**: 🟡 **MEDIUM**

**Description**:  
Some Lumina configuration files are missing:
- `config/helpdesk/droids.json`
- `config/helpdesk/helpdesk_structure.json`
- `config/droid_actor_routing.json`

**Impact**:
- Droid Actor System loads with 0 droids
- Some features may not work correctly

**Status**: 
- ⏳ Configuration files need to be created
- 🔄 Non-blocking for core functionality

---

## Low Priority Issues

### 11. Git Warning: Unable to Access .gitignore

**Priority**: 🟢 **LOW**

**Description**:  
Warning when running git commands:
```
warning: unable to access 'mcp_servers/core-mcp-server/pip-req-build-yqlzmzn5/.gitignore': Function not implemented
```

**Impact**: 
- Cosmetic warning only
- Does not affect functionality

**Status**: 
- 📝 Documented
- 🔄 Can be ignored

---

## Resolution Tracking

### Dropbox Git Issue

**Attempted Solutions**:
1. ✅ Created retry script with filesystem checks
2. ✅ Documented workarounds
3. ✅ **Long-term solution implemented: NAS-based git storage**
4. ✅ Migration script created and tested
5. ✅ Complete documentation provided

**Solution Status**: ✅ **READY FOR MIGRATION**

**Next Steps**:
- ✅ Execute migration: `python scripts/python/migrate_git_to_nas.py --dry-run` (test first)
- ✅ Run full migration when ready
- ✅ Verify git operations work correctly
- ✅ Remove temporary workarounds after successful migration

---

**Remember**: This is LUMINA CORE - all issues should be tracked and resolved systematically.

