# Port 3000 - Tony Stark Memorial

## Status: PERMANENTLY RESERVED

Port 3000 is **permanently reserved** in honor of Tony Stark's ultimate sacrifice.

## Purpose

This port serves as a **memorial tribute** and is **not to be used for any services**.

## Port Assignments

| Port | Purpose | Status |
|------|---------|--------|
| **3000** | **Tony Stark Memorial** | **RESERVED - DO NOT USE** |
| 3001 | KAIJU Iron Legion - Main LLM | Operational |
| 3002 | KAIJU Iron Legion - Mark II | Available |
| 3003 | KAIJU Iron Legion - Mark III | Available |
| 11435 | Localhost port forward for Cursor | Operational |

## Iron Legion Main LLM

The **main LLM service** runs on **port 3001** on KAIJU (10.17.17.11).

- **Direct Access**: `http://10.17.17.11:3001`
- **Cursor Integration**: `http://localhost:11435/v1` (via SSH port forward)

## Configuration

- **Port Assignments**: `config/homelab_port_assignments.json`
- **Cluster Config**: `config/ultron_cluster_selection.json`

## Notes

- Port 3000 is **sacred** and must never be assigned to services
- All LLM services use ports 3001+ on KAIJU
- Cursor IDE integration uses localhost:11435 port forward to bypass IP validation

---

*"Part of the journey is the end."* - Tony Stark
