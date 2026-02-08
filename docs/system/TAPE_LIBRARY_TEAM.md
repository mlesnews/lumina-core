# Tape Library Team

**Status**: Active  
**Motto**: "8-track, reel-to-reel, 20 meg disk packs - we handle all that data stuff so JARVIS can focus on the important work"

## Overview

The Tape Library Team is a specialized team within the @helpdesk system responsible for all data lifecycle management operations. Their core philosophy: **Data deletion is extremely dangerous** - even small deletions can have catastrophic consequences (the "two penny screw that takes down billion-dollar satellites").

## Core Principles

1. **Data deletion is extremely dangerous**: Even small deletions can have catastrophic consequences
2. **Larger data = higher temperature = greater weight = longer recreation time**: The larger the data, the more intense the risk
3. **Recovery time analysis**: Calculate time to recreate from scratch vs. restore from backup
4. **Always prefer archive over delete**: When possible, archive instead of deleting
5. **Multiple backup locations**: Critical data should have multiple backup locations

## Team Members

### Tape Librarian
- **Role**: Primary Data Archivist & Storage Manager
- **Specialization**: Tape library operations, archival storage management, data organization
- **Capabilities**: Archive data, manage tape library, organize storage, storage media operations

### Backup Specialist
- **Role**: Backup & Restore Operations
- **Specialization**: Backup creation, restore operations, backup verification, restore time analysis
- **Capabilities**: Create backups, restore data, verify backups, backup scheduling

### Retention Analyst
- **Role**: Retention Policy & Lifecycle Management
- **Specialization**: Retention policies, data lifecycle management, data recreation time analysis
- **Capabilities**: Retention policy management, lifecycle analysis, recreation time analysis, data value assessment

### Recovery Engineer
- **Role**: Recovery Time & Strategy Analysis
- **Specialization**: Recovery time objectives (RTO), recovery point objectives (RPO), data recreation vs restore analysis
- **Capabilities**: Recovery time analysis, recovery strategy planning, RTO/RPO analysis, disaster recovery

## Decision Framework

### Deletion Criteria
- Verify original data source exists
- Calculate recreation time vs restore time
- Assess data value and retention requirements
- Identify archive alternatives
- Review backup availability
- Calculate recovery time objectives

### Approval Required
- Any deletion requires Tape Library Team consensus
- Data size > 100 GB requires escalation
- Recreation time > restore time requires escalation
- No backup available requires escalation
- Critical system data requires escalation

### Archive Priorities
- **Critical**: Archive immediately, multiple locations
- **Important**: Archive to primary location, backup to secondary
- **Routine**: Archive to primary location
- **Low Priority**: Archive when space allows

## Storage Media

- **Tape Library**: Long-term archival, large datasets
- **Disk Packs**: Historical reference, specialized systems
- **Reel-to-Reel**: Historical archival, specialized formats
- **NAS**: Primary archive location, frequently accessed data
- **External Drive**: Secondary backup, portable archive
- **Cloud Storage**: Offsite backup, disaster recovery

## Workflow Structure

**CRITICAL**: Decision-making happens at the **END** of the workflow. We must **START at the BEGINNING** every single time:

1. **Problem Identification** - Identify and document the problem
2. **Impact Assessment** - Assess business impact, customer impact, system impact, financial impact
3. **Root Cause Analysis** - Analyze root cause and contributing factors
4. **Escalation Determination** - Determine ALL escalations required
5. **Prevention Strategies** - Develop immediate, short-term, and long-term prevention
6. **Decision Making** - THEN make the decision (LAST STEP)

This workflow ensures we never skip steps and always consider all factors before making decisions.

## Workflows

### Complete Workflow Execution

The Tape Library Team workflow (`scripts/python/tape_library_workflow.py`) enforces this structure:

```python
from tape_library_workflow import TapeLibraryWorkflow

workflow = TapeLibraryWorkflow()
result = workflow.execute_workflow(
    problem_description="Recursive snapshot consuming 1.22 TB",
    data_path="data/time_travel/snapshots/...",
    data_size_bytes=1337686952093,
    reported_by="Dropbox monitoring"
)

# Result contains all 6 steps in order:
# - step_1_problem_identification
# - step_2_impact_assessment (business, customer, system, financial, operational)
# - step_3_root_cause_analysis
# - step_4_escalation_determination
# - step_5_prevention_strategies
# - step_6_decision_making (FINAL STEP)
```

### Data Deletion Request
1. Tape Library Team receives deletion request
2. Retention Analyst assesses data value and retention requirements
3. Recovery Engineer calculates recreation time vs restore time
4. Tape Librarian identifies archive options (if deletion approved)
5. Team decision: Archive, Delete, or Escalate to JARVIS
6. If approved: Backup Specialist creates backup before deletion
7. Tape Librarian executes archive or deletion
8. Recovery Engineer documents recovery procedures

### Archive Request
1. Tape Librarian receives archive request
2. Backup Specialist verifies data integrity
3. Tape Librarian selects appropriate storage media
4. Backup Specialist creates archive backup
5. Tape Librarian organizes and catalogs archive
6. Retention Analyst updates retention records

### Restore Request
1. Backup Specialist receives restore request
2. Tape Librarian locates archive/backup
3. Recovery Engineer calculates restore time
4. Backup Specialist executes restore operation
5. Recovery Engineer verifies restore integrity

## Pathfinder Integration - Qui-Gon Jinn Logic

**CRITICAL**: When work is stopped/waiting (e.g., after ESCALATE decision), the Pathfinder automatically searches for the next breadcrumb to continue the workflow.

### Automatic Pathfinding

After workflow completes with approval pending, the Pathfinder automatically:
1. Analyzes current state (what's blocking)
2. Searches for solutions/next steps
3. Finds available paths forward
4. Bridges the gap automatically
5. Leads to the next breadcrumb

### Pathfinder Logic

The Pathfinder (`scripts/python/tape_library_pathfinder.py`) finds multiple paths:

1. **Approval Process Path** - Continue with escalation/approval workflow
2. **Prevention Strategies Path** - Execute immediate prevention (CAN PROCEED without approval)
3. **Prepare Implementation Path** - Prepare implementation details while waiting
4. **Precedent Search Path** - Search for similar past decisions
5. **Alternative Analysis Path** - Deep dive into alternative options

### Breadcrumbs

The Pathfinder generates breadcrumbs (next actionable steps) that can be executed immediately, even while waiting for approval. For example:

- Stop creating new snapshots until issue resolved
- Identify and disable snapshot creation processes
- Prepare detailed implementation plan
- Search workflow history for similar cases
- Analyze all decision alternatives in detail

### Integration with Workflow

The workflow automatically triggers pathfinder when work is blocked:

```python
# After decision is made and approval is pending
if approval_status == "pending":
    pathfinder = TapeLibraryPathfinder()
    pathfinding_result = pathfinder.find_paths_forward(workflow_file)
    # Next actions populated with breadcrumbs
```

## Integration

### Helpdesk Routing
- **Domain**: `data_lifecycle`
- **Keywords**: tape, archive, backup, restore, retention, data_lifecycle, data_deletion, data_preservation, storage, disk_pack, reel_to_reel, 8-track, nas_backup, recovery_time, rto, rpo, data_recreation, restore_time, data_migration, archival_storage

### JARVIS Delegation
JARVIS can delegate all data lifecycle management decisions to the Tape Library Team:

```python
from tape_library_team_decision_engine import TapeLibraryTeamDecisionEngine

engine = TapeLibraryTeamDecisionEngine()
assessment = engine.assess_data(data_path)
decision = engine.make_deletion_decision(assessment, reason="Space constraints")
```

## Example: Recursive Snapshot Decision

For the recursive snapshot consuming 1.22 TB:

**Assessment**:
- Size: 1,245.82 GB
- Criticality: Important
- Backup available: No
- Recreation time: 373.75 hours (~15.6 days)
- Restore time: Infinite (no backup)

**Decision**: **ESCALATE**
- Data size exceeds 1 TB threshold
- Requires JARVIS approval
- No backup available
- High recreation time

## Files

- **Team Config**: `config/helpdesk/tape_library_team.json`
- **Decision Engine**: `scripts/python/tape_library_team_decision_engine.py`
- **Helpdesk Integration**: `config/helpdesk/helpdesk_structure.json`
- **Routing**: `config/droid_actor_routing.json`

## Related Systems

- Data Lifecycle Manager (`scripts/python/data_lifecycle_manager.py`)
- Git Time Travel (`scripts/python/git_time_travel.py`)
- Universal Decision Tree (`scripts/python/universal_decision_tree.py`)

