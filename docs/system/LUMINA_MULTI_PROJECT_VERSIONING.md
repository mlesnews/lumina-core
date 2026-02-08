# LUMINA Multi-Project Versioning Strategy

**Date**: 2026-01-28
**Status**: ✅ **ACTIVE**

---

## 🎯 Overview

LUMINA maintains **four parallel projects** with synchronized versioning:

1. **PUBLIC** (Open-Source) - Currently **v2.0**
2. **PREMIUM** - Commercial features
3. **MOBILE** - Mobile platform
4. **PRIVATE-COMPANY** - Complete ecosystem (full version)

---

## 📊 Current Version Status

| Project | Current Version | Next Version | Status |
|---------|---------------|--------------|--------|
| **PUBLIC** | v2.0 | v2.1.0 or v3.0.0 | ✅ Active |
| **PREMIUM** | TBD | Sync to PUBLIC | 🔄 Pending |
| **MOBILE** | TBD | Sync to PUBLIC | 🔄 Pending |
| **PRIVATE-COMPANY** | TBD | Sync to PUBLIC | 🔄 Pending |

---

## 🔄 Version Synchronization Rules

### Major Versions (X.0.0)
- **Breaking changes** across all projects
- **All projects must sync** to same major version
- **Example**: v2.0.0 → v3.0.0 (complete restructure)

### Minor Versions (X.Y.0)
- **New features** added
- **All projects sync** to same minor version
- **Example**: v2.0.0 → v2.1.0 (cleanup, new features)

### Patch Versions (X.Y.Z)
- **Bug fixes** only
- **Projects can diverge** (project-specific fixes)
- **Example**: v2.1.0 → v2.1.1 (PUBLIC), v2.1.2 (PREMIUM)

---

## 🏗️ Cleanup Version Decision

### Current State
- **PUBLIC**: v2.0 (open-source baseline)
- **Cleanup Scope**: Major cleanup of entire codebase

### Version Options

#### Option 1: v2.1.0 (Minor Release)
**Rationale**:
- Incremental cleanup
- Backward compatible
- Maintains API compatibility
- All projects sync to v2.1.0

**Use When**:
- Cleanup is incremental
- No breaking changes
- Maintain compatibility

#### Option 2: v3.0.0 (Major Release)
**Rationale**:
- Complete restructure
- Breaking changes acceptable
- New architecture
- All projects sync to v3.0.0

**Use When**:
- Complete restructure
- Breaking changes needed
- New architecture

---

## 📋 Cleanup Impact on All Projects

### PUBLIC (Open-Source)
- **Scope**: Cleanup open-source codebase
- **Target**: Remove duplicates, organize structure
- **Impact**: Public-facing code quality improvement

### PREMIUM
- **Scope**: Cleanup premium features
- **Target**: Organize commercial features
- **Impact**: Better premium feature organization

### MOBILE
- **Scope**: Cleanup mobile-specific code
- **Target**: Organize mobile platform code
- **Impact**: Better mobile development experience

### PRIVATE-COMPANY (Complete Ecosystem)
- **Scope**: Complete cleanup of entire ecosystem
- **Target**: Organize all code, docs, configs, environments
- **Impact**: Complete system organization

---

## 🔄 Synchronization Process

### Step 1: Determine Base Version
- **Current**: PUBLIC v2.0
- **Decision**: v2.1.0 (incremental) or v3.0.0 (major)

### Step 2: Apply Cleanup
- Execute cleanup plan
- Test all changes
- Verify functionality

### Step 3: Version All Projects
- **PUBLIC**: Tag as new version
- **PREMIUM**: Sync to same version
- **MOBILE**: Sync to same version
- **PRIVATE-COMPANY**: Sync to same version

### Step 4: Release
- Release PUBLIC (open-source)
- Release PREMIUM (commercial)
- Release MOBILE (mobile platform)
- Release PRIVATE-COMPANY (complete ecosystem)

---

## 📊 Version History

### v2.0 (Current - PUBLIC)
- Open-source baseline
- Initial public release

### v2.1.0 (Planned - All Projects)
- Cleanup release
- Incremental improvements
- All projects synchronized

### v3.0.0 (Future - All Projects)
- Major restructure (if needed)
- Breaking changes
- New architecture
- All projects synchronized

---

## 🎯 Recommendations

### For Current Cleanup

**Recommendation**: **v2.1.0** (Minor Release)

**Rationale**:
1. Incremental cleanup is safer
2. Maintains backward compatibility
3. Easier to sync across all projects
4. Can always bump to v3.0.0 later if needed

**If Complete Restructure Needed**: **v3.0.0** (Major Release)

---

## 📝 Version Tagging Convention

### Git Tags
- `v2.1.0-public` - PUBLIC release
- `v2.1.0-premium` - PREMIUM release
- `v2.1.0-mobile` - MOBILE release
- `v2.1.0-private` - PRIVATE-COMPANY release

### Unified Tag
- `v2.1.0` - All projects synchronized

---

## ✅ Success Criteria

**Version synchronization is successful when**:
- ✅ All four projects at same major.minor version
- ✅ Cleanup applied consistently across all projects
- ✅ Release notes synchronized
- ✅ Documentation updated for all projects
- ✅ Changelog maintained for all projects

---

**Status**: ✅ **VERSIONING STRATEGY DEFINED**

**Next Action**: Determine cleanup version (v2.1.0 or v3.0.0) and apply to all projects
