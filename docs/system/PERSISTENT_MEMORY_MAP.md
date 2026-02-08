# Persistent Memory Map – Where Knowledge Survives Reboot

**Last Updated**: 2026-01-29
**Purpose**: Map where critical knowledge is stored so it is not forgotten on reboot. Use this when adding or changing facts that must persist.

---

## The Problem

Critical facts (e.g. **Kaiju = desktop 10.17.17.11, NAS = 10.17.17.32**) have been explained 3+ times and forgotten on reboot because:

- Memory retrieval is not automatic; agents must actively read memories.
- No single place encoded the host identity; configs conflated Kaiju with NAS (*.32).
- Configs were not pulling from DNS or a single host registry.

---

## Where Persistence Lives (Use All for Critical Facts)

### 1. Cursor rules (always applied)

- **Path**: `.cursor/rules/*.mdc`
- **When**: Loaded every session; `alwaysApply: true` rules are always in context.
- **Use for**: Non-negotiable rules (e.g. host identity, no secrets).
- **Example**: `.cursor/rules/host_identity_dns.mdc` – Kaiju=*.11, NAS=*.32.

### 2. Cursor memories (checked on demand)

- **Path**: `.cursor/memories/*.md`
- **When**: Agent must open/index; list in `MEMORY_INDEX.md` and check before relevant work.
- **Use for**: Critical (5+) facts that must be checked before editing configs.
- **Index**: `.cursor/memories/MEMORY_INDEX.md` – list all critical memories and when to check.

### 3. Config SSOT (single source of truth)

- **Path**: `config/host_identity_registry.json` (host→IP); other configs reference or derive from it.
- **When**: Scripts and configs read this file; prefer populating from DNS when available.
- **Use for**: Canonical host→IP and derived endpoints so configs stay consistent.

### 4. Documentation

- **Path**: `docs/` (e.g. this file, architecture docs).
- **When**: Searched or linked; not always in context.
- **Use for**: Explanations, runbooks, and pointers to rules/memories/registry.

---

## Making a New Fact Persistent (Checklist)

1. **Encode in a rule** if it must never be violated: add or update `.cursor/rules/*.mdc` with `alwaysApply: true`.
2. **Add a memory** if it’s critical (5+) and must be checked before certain work: add `.cursor/memories/<name>_critical.md` and list it in `MEMORY_INDEX.md`.
3. **Add to config SSOT** if it’s a host/endpoint/value other configs should use: update `config/host_identity_registry.json` (or the appropriate registry).
4. **Document** in `docs/` and link to the rule/memory/registry so humans and agents can find it.

---

## Current Critical Persistence (Host Identity)

| Fact | Rule | Memory | Config SSOT |
|------|------|--------|-------------|
| Kaiju = 10.17.17.11 (desktop only) | `host_identity_dns.mdc` | `host_identity_kaiju_nas_critical.md` | `host_identity_registry.json` |
| NAS = 10.17.17.32 | same | same | same |
| Prefer DNS for host→IP | same | same | same (dns_note) |
| Identity Protection (Handle-First) | `identity_protection_rebranding.mdc` | `viral_ai_identity_protection_critical.md` | N/A |

---

## Tools and Resources

- **Rules**: `.cursor/rules/` – always-applied and conditional rules.
- **Memories**: `.cursor/memories/` + `MEMORY_INDEX.md` – when to check which memory.
- **Host registry**: `config/host_identity_registry.json` – canonical host→IP; target for DNS pull.
- **Cluster/endpoint registry**: `config/cluster_endpoint_registry.json` – references host identity; `configuration_sources.host_identity_ssot` points to host registry.

To improve consistency: before editing any endpoint or cluster config, read `MEMORY_INDEX.md`, then the relevant memory and `config/host_identity_registry.json`.
