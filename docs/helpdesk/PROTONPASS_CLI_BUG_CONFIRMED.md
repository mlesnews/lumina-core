# ProtonPass CLI Bug - Confirmed Across Versions

**Date**: 2026-01-16 (opened) · 2026-05-07 (closed with workaround)  
**Status**: ✅ **RESOLVED — WORKAROUND IN PLACE** (originally CONFIRMED upstream bug)  
**Priority**: 🟡 **MEDIUM** (downgraded from CRITICAL — no longer a blocker)  
**Closure Reason**: Upstream Proton bug, but local workaround (`scripts/python/protonpass_auto_login.py`) has been in production use since 2026-01-21 and reliably retrieves credentials. Ticket closed 2026-05-07 after 3+ months of stable workaround operation.

---

## 🐛 Bug Confirmation

### Versions Affected
- ✅ **v1.3.2** (previous installation) - **BUG PRESENT**
- ✅ **v1.3.5** (new installation via winget) - **BUG STILL PRESENT**

### Error Details
```
ERROR pass-cli\src\main.rs:257 (v1.3.5) / main.rs:254 (v1.3.2)
Session is some but needs extra password
Error: Error deleting base dir
Caused by: The process cannot access the file because it is being used by another process. (os error 32)
```

### Installation Location (v1.3.5)
```
C:\Users\mlesn\AppData\Local\Microsoft\WinGet\Packages\Proton.ProtonPass.CLI_Microsoft.Winget.Source_8wekyb3d8bbwe\pass-cli.exe
```

---

## 📊 Impact

### What Works
- ✅ Installation succeeds
- ✅ CLI executable is valid
- ✅ Version command works (`--version`)

### What Fails
- ❌ **ALL CLI operations fail** (`item list`, `item view`, etc.)
- ❌ Cannot authenticate properly
- ❌ Cannot retrieve any credentials
- ❌ **100% reproducible** - happens every time

---

## 🔍 Root Cause

**Confirmed**: This is a **persistent bug in ProtonPass CLI** that:
1. Affects multiple versions (1.3.2, 1.3.5)
2. Occurs on first CLI operation after any authentication attempt
3. Is a session management bug in the Rust codebase
4. Cannot be worked around by:
   - Reinstalling
   - Clearing session files
   - Rebooting
   - Using different installation methods

---

## 🎯 Next Steps

### Immediate Actions
1. **Report Bug to ProtonPass**
   - File detailed bug report
   - Include error details and versions affected
   - Request urgent fix

2. **Implement Workaround**
   - Use ProtonPass GUI to manually retrieve credentials
   - Store in Azure Key Vault for automation
   - Bypass CLI entirely

3. **Monitor for Updates**
   - Check for ProtonPass CLI updates
   - Test new versions when available

---

## 📝 Bug Report Template

**Title**: ProtonPass CLI Session Management Bug - Blocks All Operations

**Versions Affected**: 1.3.2, 1.3.5

**Error**: 
```
ERROR pass-cli\src\main.rs:257: Session is some but needs extra password
Error: Error deleting base dir
Caused by: The process cannot access the file because it is being used by another process. (os error 32)
```

**Steps to Reproduce**:
1. Install ProtonPass CLI (any version)
2. Attempt to authenticate
3. Run any CLI command (`item list`, `item view`, etc.)
4. Error occurs immediately

**Expected**: CLI operations should work after authentication

**Actual**: All CLI operations fail with session management error

**Workaround**: Use ProtonPass GUI instead of CLI

---

## 🏷️ Tags

`#HELPDESK` `#PROTONPASS` `#CLI_BUG` `#CONFIRMED` `#CRITICAL` `#BLOCKER` `#JARVIS`

---

**Status**: ✅ **RESOLVED — WORKAROUND IN PLACE** (closed 2026-05-07)

**Resolution**: Upstream Proton CLI bug was never patched, but `scripts/python/protonpass_auto_login.py` provides a reliable session-establishment workaround that has been in active use since 2026-01-21 (referenced across cluster-restart and credential-copy workflows). System operations are unblocked.

**Recommendation (going forward)**: Continue using `protonpass_auto_login.py` for automation. Re-test direct `pass-cli.exe` operations only after a major Proton release. Azure Key Vault remains a viable fallback if Proton ecosystem becomes unsuitable.

**If upstream patches the CLI**: Re-open this ticket and verify on the new version.
