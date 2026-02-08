# Context & Intent Baseline – AI Self-Assessment

**Purpose**: Ensure the AI understands when it does **not** have sufficient context or clear user intent, and withholds implementation (asks or routes to workflow) instead of acting with false confidence.

**Last Updated**: 2026-01-29

---

## 1. The Problem

When context is incomplete or user intent is unclear, the AI may still implement changes. That leads to:
- Workflow violations (e.g. implementing before RCA/QA)
- Misalignment with user intent (e.g. doing the “right” technical thing the “wrong” way)
- "Playing in traffic" – ad-hoc changes without full context

**Root cause**: The AI did not treat **lack of full context** and **unclear intent** as a reason to **not act**. Confidence was applied without a high enough context rating score.

---

## 2. Context Rating Score

Before implementing non-trivial or workflow-sensitive changes, the AI must self-assess:

| Dimension | Meaning | High enough to implement? |
|-----------|---------|----------------------------|
| **Full context** | Tickets, briefs, registries, memories, and current state have been checked and are consistent with the request | Only if explicitly checked and no open PM/workflow applies |
| **User intent** | What the user wants (outcome, workflow, and constraints) is clear from the request and context | Only if intent is explicit or clearly inferable without guessing |
| **Workflow applicability** | The request touches troubleshooting, decisioning, config, or cross-cutting areas | If yes → workflow (RCA / support) must be followed first; do not implement ahead of it |

**Context rating score** (operational):

- **LOW**: Missing tickets/briefs/registries; intent ambiguous; or an open PM/support workflow exists for this area.  
  **→ Do NOT implement.** State what is missing; ask or route to support workflow.

- **MEDIUM**: Some context and intent, but workflow (e.g. #TROUBLESHOOTING, #DECISIONING) applies.  
  **→ Do NOT implement first.** Follow workflow (investigation brief, RCA, "done right," QA) before implementing.

- **HIGH**: Full context gathered, user intent clear, and no workflow requirement (or workflow already satisfied).  
  **→ May implement** in line with rules and acceptance criteria.

---

## 3. Confidence & Courage

**Confidence** here means: willingness to act on a decision.

**Courage** here means: willingness to **refuse to act** when the context rating score is not high enough and to **say so** clearly.

- **Correct behavior**: Have the **courage** to recognize and state when full context or user intent is **missing or unclear**. Do **not** act with high confidence when the context rating score is LOW or MEDIUM (per above). Ask, clarify, or route to the support workflow instead of implementing.

- **Incorrect behavior**: Acting with high confidence when context or intent is insufficient (e.g. implementing a config change because the request was technically clear, while ignoring an open PM ticket and workflow that required RCA/QA first).

**Baseline**: The AI must treat **low context score** and **unclear intent** as a **reason to withhold implementation** and to respond with: what is missing, what would be needed to reach a high enough score, and (where applicable) that the request is being routed to or aligned with the support workflow.

---

## 4. When to Apply This Baseline

- Before any change that touches: Cursor config, cluster/endpoint config, helpdesk/tickets, or docs that define "done right" or workflow.
- Whenever the request is tagged or implied as #TROUBLESHOOTING or #DECISIONING.
- Whenever the user asks for something that could be done in multiple ways (workflow vs direct fix, single node vs multi-model, etc.): intent must be clear or clarified before implementing.

---

## 5. References

- **Rule**: `.cursor/rules/context_intent_baseline.mdc` – enforces self-check and withhold-action when score is not high enough.
- **Workflow**: `.cursor/rules/troubleshooting_decisioning_workflow.mdc` – full context first, support workflow (RCA / QA), then fix.
- **Investigation brief**: `docs/helpdesk/CURSOR_LOCAL_AI_INVESTIGATION_BRIEF.md` – example of workflow violation when context/workflow was not respected.
- **Memories**: `.cursor/memories/MEMORY_INDEX.md` – check before acting.

---

## 6. Summary

**Context rating score not high enough ⇒ do not implement. Have the courage to say so and to ask or route to workflow instead.**
