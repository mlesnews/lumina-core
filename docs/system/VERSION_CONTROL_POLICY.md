# Version Control Policy

**Purpose**: Single place to check how we version the repo and shipped artifacts so we increment correctly.

---

## Current state (as of 2026-01)

| What | Where | Current version |
|------|--------|------------------|
| **Repo / product** (source of truth for "LUMINA vX") | `.cursor/workspace.json` → `version` | **2.0.0** |
| **Tasks schema** | `.cursor/tasks.json` → `version` | **2.0.0** |
| **Lumina Core extension** (VSIX we ship) | `vscode-extensions/lumina-core/package.json` → `version` | **2.0.0** (aligned with repo) |
| Root package (quality tools) | `package.json` → `version` | 1.0.0 |
| Other VSIX extensions | Each `package.json` | 1.0.0 |

**Aligned**: Workspace and Lumina Core extension both **2.0.0** (single version line).

---

## Policy (how to increment correctly)

### 1. Repo / product version (2.0.0)

- **Source of truth**: `.cursor/workspace.json` → `"version": "X.Y.Z"`.
- **Keep in sync**: `.cursor/tasks.json` → `"version"` (same as workspace when you touch tasks).
- **When to bump**:
  - **MAJOR (3.0.0)**: Breaking or major product/repo-wide change; new “generation” of LUMINA.
  - **MINOR (2.1.0)**: New features or notable changes across the repo; non-breaking.
  - **PATCH (2.0.1)**: Fixes, docs, config-only; no behavior change.

### 2. Lumina Core extension (recommended: match repo)

- **Where**: `vscode-extensions/lumina-core/package.json` → `"version"`.
- **Choice**:
  - **Option A – Match repo**: Set to same as workspace (e.g. **2.0.0**) so “v2.0” = repo and extension. Bump together on release.
  - **Option B – Extension own line**: Keep extension on its own semver (e.g. 3.0.0). Bump when you ship extension changes; repo can stay at 2.0.0 until a full product release.
- **When to bump**: Same semver idea (major = breaking, minor = feature, patch = fix). If Option A, bump in lockstep with workspace.

### 3. Other packages

- Root `package.json`, other extensions, platform_apps: bump when that specific package is released or you want to track its version; no need to match workspace unless you decide they’re part of “LUMINA vX”.

---

## Checklist for a release

- [ ] Bump **workspace** (`.cursor/workspace.json`) and **tasks** (`.cursor/tasks.json`) to the new version (e.g. 2.1.0).
- [ ] Bump **lumina-core** `vscode-extensions/lumina-core/package.json` to the same version.
- [ ] Run BDA: `.\vscode-extensions\lumina-core\build_and_install.ps1`. (Script reads version from `package.json`; VSIX = `lumina-core-{version}.vsix` — same as git branch / repo when aligned.)
- [ ] Tag in Git if desired (e.g. `v2.0.0`).

---

## Recommendation applied

- If “we are v2.0” should mean **everything** (repo + extension): set `vscode-extensions/lumina-core/package.json` to `"version": "2.0.0"` and run BDA again.
- If the extension is intentionally “3.x” and repo stays 2.0: document that in this file and in release notes so it’s clear we’re not incrementing wrong—we have two version lines.

---

**Last updated**: 2026-01-30
