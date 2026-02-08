# Homelab Inventory & Automation Contract

**Status:** Active  
**Last updated:** 2026-02-04

---

## Bottom line: our expectation

**Automation and autonomy are driven by leveraging resources and assets as defined by our hw/sw @homelab inventory—all features, functions, applications, services—for every device in the ecosystem.**

- **No ad-hoc automation:** Automation and autonomous agents MUST use the canonical homelab inventory as the source of truth for what exists, where it lives, and what it can do.
- **Inventory-first:** Before designing or executing automation (scripts, n8n, JARVIS control, MCP, cron, agents), consult the inventory to discover devices, endpoints, capabilities, and services.
- **Every device, every capability:** The inventory defines, per device and per asset: hardware, software, applications, services, features, and functions. Automation leverages these definitions; it does not invent endpoints or assume devices.

---

## What counts as “the homelab inventory”

The inventory is the **set of canonical configs and discovery outputs** that together define the ecosystem. Use them as a single logical inventory.

| Asset | Purpose | Location |
|-------|---------|----------|
| **Host identity (devices)** | Hostname → IP, type, role; cluster endpoints | `config/host_identity_registry.json` |
| **JARVIS homelab control** | Systems, frameworks, services, endpoints, capabilities, monitoring | `config/jarvis_homelab_control_config.json` |
| **AI ecosystem (entities)** | Digital employees, technical_systems, applications, services; taxonomy | `config/homelab_ai_ecosystem.json` |
| **Port assignments** | Port → host, service, purpose; port forwarding | `config/homelab_port_assignments.json` |
| **CPU / architecture** | Per-host or cluster CPU architecture | `config/homelab_cpu_architecture.json` |
| **Comprehensive audit** | Full hw/sw discovery (devices, OS, apps, network, services) | `scripts/python/homelab_comprehensive_inventory_audit.py` + outputs |
| **Inventory registry (index)** | Single pointer to this contract and all inventory assets | `config/homelab_inventory_registry.json` |

Additional references: `config/homelab_mcp_hybrid_config.json`, `config/cluster_endpoint_registry.json`, `config/jarvis_lumina_homelab_connection.json`, NAS/deploy configs under `containerization/` and `deploy_to_nas/`.

---

## Required behavior

1. **Automation design**  
   When adding or changing automation (scripts, workflows, cron, n8n, MCP, JARVIS control): resolve devices, endpoints, and capabilities from the inventory configs above. Do not hardcode IPs or ports that contradict `host_identity_registry.json` or `homelab_port_assignments.json`.

2. **Autonomous agents (e.g. JARVIS)**  
   When controlling systems, running health checks, or orchestrating services: read from `jarvis_homelab_control_config.json` (and related inventory assets) to know what systems exist, their endpoints, and what monitoring/control is defined. Prefer the inventory over hardcoded lists.

3. **Discovery and audits**  
   Use `homelab_comprehensive_inventory_audit.py` (and any other discovery scripts) to refresh device/app/service data; treat their outputs as part of the inventory. Where possible, feed audit results back into the canonical configs so the inventory stays current.

4. **New devices or services**  
   When adding a new device, application, or service to the homelab: add it to the appropriate inventory asset (host identity, JARVIS control config, ecosystem, or port assignments) so automation and autonomy can leverage it consistently.

---

## References

- **JARVIS homelab control:** `config/jarvis_homelab_control_config.json`  
- **JARVIS–Lumina–Homelab:** `docs/system/JARVIS_LUMINA_HOMELAB_CONNECTION.md`  
- **Host identity (Kaiju/NAS):** `.cursor/rules/host_identity_dns.mdc`, `config/host_identity_registry.json`  
- **Automation-first:** `.cursor/rules/automation_first.mdc`, `docs/system/AUTOMATION_FIRST.md`  
- **Inventory registry:** `config/homelab_inventory_registry.json`

---

**Maintained by:** @JARVIS @LUMINA  
**Tag:** @homelab #automation #autonomy #inventory
