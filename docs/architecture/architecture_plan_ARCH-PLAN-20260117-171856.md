# Architecture Plan: ARCH-PLAN-20260117-171856

**Created:** 2026-01-17 17:18:56

**Status:** ⏳ PENDING VALIDATION

**Validated By:** None

## Requirements

- **REQ-001** (must): KAIJU (Desktop/Server) must run 7 Iron Legion LLM nodes
- **REQ-002** (must): Laptop should use lightweight, appropriate tooling (NOT 7 nodes)
- **REQ-003** (must): Use what works best for each environment
- **REQ-004** (must): Documentation must match actual state
- **REQ-005** (should): Iron Legion currently working on Docker Compose

## Decisions

### DEC-001: Iron Legion

- **Tool:** Docker Compose
- **Location:** KAIJU (10.17.17.11)
- **Reasoning:** Currently working, meets requirement for 7 nodes, simple and effective
- **Alternatives:** Kubernetes, K3s, Docker Swarm

### DEC-002: Laptop K8s

- **Tool:** Docker Desktop K8s (reduced nodes) OR lightweight alternative
- **Location:** Laptop
- **Reasoning:** User doesn't want 7 nodes on laptop. Need lightweight solution.
- **Alternatives:** Reduce K8s nodes to 1-2, Disable K8s, Use Docker Compose, Use lightweight K3s

### DEC-003: Documentation

- **Tool:** Update documentation to match reality
- **Location:** All documentation
- **Reasoning:** Documentation must reflect actual state, not planned state
- **Alternatives:** Keep as-is, Mark as planned, Update to reality

## Migration Path

1. 1. Update documentation to reflect reality
1. 2. Reduce laptop K8s nodes (or disable if not needed)
1. 3. Keep Iron Legion on Docker Compose (no change needed)
1. 4. Verify alignment between docs and reality

## Risks

- Documentation confusion (mitigated by update)
- Laptop resource waste (mitigated by node reduction)
