# Where We Are, Where We've Been, Where We're Going

**Date**: 2026-01-30  
**Purpose**: Reconcile the roadmap with reality so we can follow it again.

---

## Where we are (current state)

### Two roadmaps, not one

| Source | What it is | Last meaningful update |
|--------|------------|------------------------|
| **ROADMAP.md** (root) | High-level phases: Core → Integration → Interfaces → Quality → Advanced | Phase 1 marked complete, Phase 2 in progress; milestones say Q1/Q2 **2025** (we're in Jan **2026**) |
| **data/roadmap/master_roadmap.json** | Sprint/backlog: current_sprint, backlog, focus_areas | 2026-01-28; focus = Homelab 10K; current_sprint has Proximity Chat, Laptop Disk Migration, Phase 1 homelab items (many pending) |

So: **we have two roadmaps**, and neither has been the single source of truth. ROADMAP.md is strategic but dated (2025 milestones). master_roadmap.json is tactical (sprint items) but current_sprint is a mix of old (Jan 17) and new (Jan 28 homelab phases); nothing there is being driven as "the" plan.

### What the roadmaps say vs what we've been doing

- **ROADMAP.md** says: Phase 1 Core complete, Phase 2 Integration in progress (system integration, config, dashboard).
- **master_roadmap.json** says: focus = Homelab 10K; current_sprint = Proximity Chat, Laptop Disk Migration, Phase 1 homelab (learning, autonomy 50%, efficiency 60%, self-sustaining).
- **Reality**: We've been doing **tactical, non-roadmap work**: homelab architecture/audit docs, NAS deploy, Cursor/retry rules, version policy (2.0.0), internal-error workaround, batch-commit policy, BDA, workflow/request-ID docs. That work is valuable but **not** clearly mapped to roadmap items, so the roadmap feels unused.

### Summary: where we are

- **Strategically**: Phase 1 (Core) done per ROADMAP.md; Phase 2 (Integration) "in progress" but not being tracked against the roadmap.
- **Tactically**: master_roadmap has Homelab 10K and a current_sprint full of pending/in-progress items that we haven't been following.
- **Emotionally**: We haven't been following the roadmap; we need one place to look and a small set of "what's next."

---

## Where we've been (recent reality)

Work that actually happened recently (not necessarily on the roadmap):

- **Homelab**: Architecture, audit, topology, control, prioritization fallback (multiple *COMPLETE*.md).
- **Deployment**: NAS, Synology API, containerization, MCP servers.
- **Cursor/Lumina**: Retry rules, no --no-verify rule, internal-error workaround (Request ID rerun), version policy (2.0.0), BDA, workflow/request workflow, one-shot/accept-changes docs.
- **Security/workflow**: Pre-commit validator fix, batch-commit policy, no-secrets rules.
- **Unfinished**: Batch commits (we undid the big --no-verify commit; changes are unstaged, need batch commits with validator). Extension at 2.0.0 but BDA not re-run for 2.0.0 VSIX.

So: **we've been doing real work**, but it's been **reactive and tactical**. The roadmap exists but wasn't the driver.

---

## Main goal (#1 priority)

**Get local AI clusters online and active** — every cloud AI token request burns money. To do it we need: **(1) a working Lumina extension** (BDA, loads in Cursor), **(2) superagent JARVIS** (route requests to ULTRON / Iron Legion first, cloud fallback). Full spec: [MAIN_GOAL_LOCAL_AI_CLUSTERS.md](MAIN_GOAL_LOCAL_AI_CLUSTERS.md). All other roadmap work supports this.

---

## Where we're going (reconcile and next steps)

### 1. Pick one "source of truth" for "what's next"

**Recommendation**:

- **Strategic (themes/phases)**: Keep **ROADMAP.md** as the high-level story (Phase 1 done, Phase 2 in progress, Phase 3+ planned). Update it once: fix dates (2025 → 2026) and add a short "Current focus" section at the top that points to the tactical list.
- **Tactical (this week/sprint)**: Use **master_roadmap.json** as the sprint. Prune or complete stale current_sprint items; add 1–3 **concrete** next items (e.g. "Batch-commit all current changes in batches," "Run BDA for 2.0.0," "Update ROADMAP.md dates and current focus"). Run `show_master_roadmap.py` regularly so the roadmap is visible.

That way: **ROADMAP.md = where we're going (phases)**. **master_roadmap.json = what we're doing now (sprint)**.

### 2. Immediate next steps (main goal first)

**#1 priority**: Get local AI clusters online and active (working Lumina extension + superagent JARVIS). See [MAIN_GOAL_LOCAL_AI_CLUSTERS.md](MAIN_GOAL_LOCAL_AI_CLUSTERS.md).

Then so we're not carrying loose ends:

1. **Lumina extension working** — Run BDA so the extension is built/installed at 2.0.0; reload Cursor; confirm it loads. (This is part of the main goal.)
2. **Batch-commit** current changes (per no_commit_no_verify rule); get to a clean, committed state.
3. **Roadmap sync**:  
   - In **ROADMAP.md**: add a "Current focus (2026-01)" section at the top; fix Q1/Q2 2025 → 2026.  
   - In **master_roadmap.json**: mark completed what's done; move "batch commit" and "BDA 2.0.0" into current_sprint if you want them tracked; drop or backlog items that are no longer relevant.

### 3. Resuming the roadmap

After the immediate steps:

- **Phase 2 (ROADMAP.md)** remains "Integration": system integration layer, config management, unified dashboard. Pick **one** of these (e.g. config management or one integration milestone) and add 1–3 concrete tasks to master_roadmap current_sprint. Work from the sprint; update ROADMAP.md when a phase milestone is done.
- **Homelab 10K (master_roadmap)** is the other big theme. Either treat "Phase 1: Enable Learning Systems" (or one Phase 1 item) as the next homelab goal and put it in the sprint, or explicitly backlog it until after Phase 2 progress. Don't try to "follow" both ROADMAP.md and Homelab 10K in parallel until the sprint is small and visible.

### 4. Keeping it going

- **Weekly**: Run `show_master_roadmap.py`; complete or defer sprint items; add next 1–3 tasks from ROADMAP.md or Homelab backlog.
- **When we drift**: Re-open this doc (or a short "roadmap sync" checklist); reconcile "where we are" with "where we're going" again.

---

## One-paragraph summary

We have two roadmaps (ROADMAP.md = phases, master_roadmap.json = sprint) and we haven't been following either; we've been doing tactical work (homelab, deploy, Cursor rules, version, workflow). To get back on track: (1) Use ROADMAP.md for strategy and master_roadmap for tactics. (2) Do the immediate cleanup (batch commit, BDA 2.0.0, roadmap sync). (3) Put 1–3 concrete "next" items in the sprint from Phase 2 or Homelab Phase 1. (4) Review the sprint weekly and keep ROADMAP.md and master_roadmap in sync.

---

**Related**: [MASTER_ROADMAP_GUIDE.md](../MASTER_ROADMAP_GUIDE.md), [ROADMAP.md](../../ROADMAP.md), [NEXT_STEPS_ROADMAP.md](NEXT_STEPS_ROADMAP.md), `data/roadmap/master_roadmap.json`, `scripts/python/show_master_roadmap.py`
