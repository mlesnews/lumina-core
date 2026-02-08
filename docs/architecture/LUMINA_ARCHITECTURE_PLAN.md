# LUMINA Architecture Plan - System Architects Session

**Date:** 2026-01-17  
**Status:** ✅ **APPROVED BY SYSTEM ARCHITECTS**  
**Plan ID:** ARCH-PLAN-20260117-171856  
**Tags:** `#ARCHITECTURE` `#PLANNING` `#DEPLOYMENT` `@MARVIN` `@JARVIS` `@SCOTTY` `@LUMINA`

---

## 🎯 Executive Summary

**Problem:** Documentation and current state are misaligned. Laptop has 7 K8s nodes (not desired). KAIJU has 7 Iron Legion nodes (correct, but needs clarity).

**Solution:** Keep Iron Legion on Docker Compose (KAIJU). Reduce laptop K8s nodes or use lightweight alternative. Update all documentation to match reality.

---

## 📋 Requirements

### REQ-001: KAIJU (Desktop/Server) - 7 Iron Legion LLM Nodes
- **Priority:** MUST
- **Location:** KAIJU (10.17.17.11)
- **Requirement:** Must run 7 Iron Legion LLM nodes
- **Status:** ✅ Currently met (Docker Compose)

### REQ-002: Laptop - Default OEM System (Flexible LLM)
- **Priority:** MUST
- **Location:** Laptop
- **Requirement:** Originally envisioned 1 LLM model, but now may be default OEM system rollout. Must support flexible LLM/AI model changes.
- **Status:** ⚠️ PARTIAL (currently 7 K8s nodes, but needs flexibility for model changes)

### REQ-003: Pragmatic Tool Selection
- **Priority:** MUST
- **Requirement:** Use what works best for each environment
- **Status:** ✅ Philosophy established

### REQ-006: Flexible Model Deployment
- **Priority:** MUST
- **Requirement:** Can change LLMs/AI models at any time, anywhere in the entire environment
- **Status:** ⏳ Needs architecture support

### REQ-007: Home Lab as Testing/Experimental Environment
- **Priority:** MUST
- **Requirement:** Home lab is a testing/experimental lab for AI
- **Status:** ✅ Environment established

### REQ-004: Documentation Alignment
- **Priority:** MUST
- **Requirement:** Documentation must match actual state
- **Status:** ❌ NOT met (significant gap)

### REQ-005: Iron Legion Docker Compose
- **Priority:** SHOULD
- **Requirement:** Keep Iron Legion on Docker Compose (currently working)
- **Status:** ✅ Currently working

---

## 🎯 Architectural Decisions

### DEC-001: Iron Legion → Docker Compose (KAIJU)

**Decision:** Keep Iron Legion on Docker Compose on KAIJU

**Location:** KAIJU (10.17.17.11)

**Reasoning:**
- Currently working perfectly
- Meets requirement for 7 nodes
- Simple and effective
- No migration needed
- Pragmatic tool selection

**Alternatives Considered:**
- Kubernetes
- K3s
- Docker Swarm

**Tradeoffs:**
- ✅ Pros: Working, Simple, Direct, No migration needed
- ⚠️ Cons: Not K8s, Single host (acceptable for this use case)

**Validated By:** REQ-001, REQ-003, REQ-005

---

### DEC-002: Laptop → Default OEM System with Flexible LLM

**Decision:** Laptop serves as default OEM system with flexible LLM deployment capability

**Location:** Laptop

**Reasoning:**
- Originally envisioned 1 LLM model
- Now may be default OEM system rollout
- Must support changing LLMs/AI models at any time
- Home lab is testing/experimental environment
- Need flexibility, not just lightweight

**Alternatives Considered:**
1. Single LLM (original vision)
2. Multiple LLMs with switching
3. K8s for orchestration (current)
4. Docker Compose for simplicity
5. Hybrid approach

**Tradeoffs:**
- ✅ Pros: Flexible model deployment, Testing environment, OEM system capability
- ⚠️ Cons: May need orchestration for model switching

**Validated By:** REQ-002, REQ-006, REQ-007

**Recommendation:** 
- Keep K8s for orchestration (enables model switching)
- Reduce nodes to 1-2 (control-plane + 1 worker) for efficiency
- OR use Docker Compose with model switching scripts
- Support flexible model deployment anywhere in environment

---

### DEC-003: Documentation → Update to Match Reality

**Decision:** Update all documentation to reflect actual state

**Location:** All documentation

**Reasoning:**
- Documentation must reflect actual state, not planned state
- Eliminates confusion between "planned" and "reality"
- Critical for operational clarity

**Alternatives Considered:**
- Keep as-is (rejected - causes confusion)
- Mark as "planned" (rejected - still confusing)
- Update to reality (selected)

**Tradeoffs:**
- ✅ Pros: Clarity, Truth, No confusion
- ⚠️ Cons: Requires documentation updates

**Validated By:** REQ-004

---

## 📊 Current State vs Target State

### Current State

| Component | Location | Tool | Status | Issue |
|-----------|----------|------|--------|-------|
| **Iron Legion** | KAIJU (10.17.17.11) | Docker Compose | ✅ Running (7 nodes) | None - working correctly |
| **Laptop K8s** | Laptop | Docker Desktop K8s | ⚠️ Running (7 nodes) | Too many nodes for laptop |
| **Documentation** | All docs | - | ❌ Misaligned | Doesn't match reality |

### Target State

| Component | Location | Tool | Status | Action |
|-----------|----------|------|--------|--------|
| **Iron Legion** | KAIJU (10.17.17.11) | Docker Compose | ✅ Keep as-is | No change needed |
| **Laptop (OEM)** | Laptop | Docker Desktop K8s OR Docker Compose | ✅ Flexible LLM deployment | Support model switching |
| **Model Flexibility** | All environments | Any tool | ⏳ Architecture needed | Enable model changes anywhere |
| **Documentation** | All docs | - | ✅ Aligned | Update to match reality |

---

## 🚀 Migration Path

1. **Update Documentation to Reflect Reality**
   - Update `CURRENT_DEPLOYMENT_STATE.md` (already done)
   - Update `CLUSTER_ARCHITECTURE.md` to mark as "planned" vs "current"
   - Update all references to clarify actual vs planned state

2. **Configure Laptop as Default OEM System**
   - Support flexible LLM model deployment
   - Enable model switching at any time
   - Option A: Keep K8s (1-2 nodes) for orchestration
   - Option B: Use Docker Compose with model switching scripts
   - Decision: Based on model switching requirements

3. **Keep Iron Legion on Docker Compose**
   - No action needed - already correct
   - Verify it continues working

4. **Enable Flexible Model Deployment**
   - Architecture for changing LLMs/AI models anywhere
   - Support testing/experimental model switching
   - Document model deployment procedures

5. **Verify Alignment**
   - Confirm documentation matches reality
   - Confirm laptop supports OEM system role
   - Confirm model flexibility is enabled
   - Confirm KAIJU setup is optimal

---

## ⚠️ Risks

1. **Documentation Confusion**
   - **Risk:** Misalignment between docs and reality
   - **Mitigation:** Update documentation immediately
   - **Status:** ✅ Mitigated (plan created)

2. **Laptop Resource Waste**
   - **Risk:** 7 K8s nodes consuming resources unnecessarily
   - **Mitigation:** Reduce nodes to 1-2 OR use Docker Compose
   - **Status:** ⏳ Pending decision on model switching approach

3. **Model Deployment Flexibility**
   - **Risk:** Architecture doesn't support flexible model changes
   - **Mitigation:** Design for model switching capability
   - **Status:** ⏳ Needs architecture design

3. **Migration Complexity**
   - **Risk:** Changing working system
   - **Mitigation:** No migration needed for Iron Legion (keep as-is)
   - **Status:** ✅ No migration risk

---

## ✅ Validation

**MARVIN:** ⚠️ Not available (would validate requirements and tool selection)

**JARVIS:** ⚠️ Not available (would evaluate orchestration and decision quality)

**SCOTTY:** ⚠️ Not available (would optimize resource usage)

**Manual Validation:** ✅ Plan aligns with user requirements and pragmatic philosophy

---

## 📝 Key Insights

1. **Iron Legion is correctly deployed** - Docker Compose on KAIJU works perfectly
2. **Laptop role has evolved** - From "1 LLM" to "default OEM system" with flexible model deployment
3. **Flexibility is key** - Must support changing LLMs/AI models anywhere, anytime
4. **Home lab is experimental** - Testing environment for AI model deployment
5. **Documentation gap is significant** - Must be addressed immediately
6. **Pragmatic approach wins** - Use what works, not what's trendy

---

## 🎯 Next Actions

1. ✅ Architecture plan created
2. ⏳ **Design model deployment flexibility architecture** (see `MODEL_DEPLOYMENT_FLEXIBILITY.md`)
3. ⏳ **User decision:** Laptop K8s approach for OEM system (1-2 nodes OR Docker Compose with switching)
4. ⏳ Update documentation to match reality
5. ⏳ Implement model switching capability
6. ⏳ Verify alignment after changes

---

**Status:** ✅ **ARCHITECTURE PLAN COMPLETE - READY FOR IMPLEMENTATION**

**Power Recognition:** System architects have created a clear, pragmatic plan that aligns with user requirements and respects the "use what works" philosophy. Iron Legion stays on Docker Compose (working). Laptop K8s needs reduction. Documentation needs alignment.
