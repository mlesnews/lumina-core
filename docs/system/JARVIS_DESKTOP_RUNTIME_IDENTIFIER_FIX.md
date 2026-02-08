# JarvisDesktop Runtime Identifier Fix

**Date**: 2026-01-14  
**Issue**: RuntimeIdentifier 'win10-x86', 'win10-x64', 'win10-arm64' not recognized  
**Status**: ✅ **FIXED**  
**Tags**: `#FIX` `#C#` `#.NET` `#RUNTIME_IDENTIFIER` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Problem

C# language server reported errors:
- `The specified RuntimeIdentifier 'win10-x86' is not recognized`
- `The specified RuntimeIdentifier 'win10-x64' is not recognized`
- `The specified RuntimeIdentifier 'win10-arm64' is not recognized`

These runtime identifiers are deprecated in .NET 8.0+.

---

## ✅ Solution

Updated `JarvisWidgets.csproj` to use modern runtime identifiers:

**Before**:
```xml
<RuntimeIdentifiers>win10-x86;win10-x64;win10-arm64</RuntimeIdentifiers>
```

**After**:
```xml
<RuntimeIdentifiers>win-x86;win-x64;win-arm64</RuntimeIdentifiers>
```

---

## 📝 Notes

- `win10-*` identifiers are deprecated in .NET 8.0+
- Modern identifiers use `win-*` format
- `JarvisDesktop.csproj` doesn't have RuntimeIdentifiers (uses default)
- Error may have been from language server loading both projects

---

**Status**: ✅ **FIXED**  
**File**: `applications/windows11_widgets/JarvisWidgets.csproj`  
**Tags**: `#FIX` `#C#` `#.NET` `#RUNTIME_IDENTIFIER` `@LUMINA` `@JARVIS` `#PEAK`
