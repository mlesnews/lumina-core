# Team Ticket Assignment System

## Overview

C-3PO (Helpdesk Coordinator) automatically assigns all tickets to teams with proper team structure, ensuring proper management and coordination.

## Team Structure (Required)

All tickets are assigned to teams with the following structure:

### Required Roles

1. **Team Manager**: `@c3po` (Helpdesk Coordinator)
   - Manages workflow, coordination, escalation
   - Ensures protocol compliance
   - Distributes workload

2. **Technical Lead**: `@r2d2` or team-specific (Technical Lead Engineer)
   - Implements technical solutions
   - Provides technical leadership
   - Primary assignee for technical work

3. **Business Lead**: Domain-specific (Optional)
   - Business strategy and requirements
   - Domain expertise
   - Only for teams that require business input

## Team Assignment Logic

Tickets are automatically routed to appropriate teams based on issue type and content:

### Docker/Container Issues
- **Team**: Docker Engineering Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@r2d2`
- **Business Lead**: Docker Engineering Lead
- **Keywords**: docker, container, ollama, ultron, kaiju

### Storage/NAS Issues
- **Team**: Storage Engineering Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@r2d2`
- **Business Lead**: Storage Engineering Lead
- **Keywords**: storage, nas, disk, space, capacity

### Network Issues
- **Team**: Network Support Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@r2d2`
- **Business Lead**: None (technical team)
- **Keywords**: network, connectivity, ssh, vpn, firewall

### Security Issues
- **Team**: Security & Threat Analysis Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@k2so`
- **Business Lead**: None (security team)
- **Keywords**: security, threat, access, breach

### Health/System Issues
- **Team**: System Health & Operations Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@2-1b`
- **Business Lead**: None (operations team)
- **Keywords**: health, monitoring, recovery, system

### AI/Intelligence Issues
- **Team**: AI & Intelligence Team
- **Team Manager**: `@c3po`
- **Technical Lead**: `@marvin` or `@r5`
- **Business Lead**: None (technical team)
- **Keywords**: ai, intelligence, model, llm, machine learning

## Ticket Assignment Format

All tickets include a `team_assignment` section:

```json
{
  "team_assignment": {
    "team_id": "docker_engineering",
    "team_name": "Docker Engineering Team",
    "division": "Docker Engineering",
    "team_manager": "@c3po",        // Required
    "technical_lead": "@r2d2",      // Required
    "business_lead": "Docker Engineering Lead",  // Optional
    "primary_assignee": "@r2d2",
    "assigned_at": "2026-01-01T09:45:08.169577",
    "assigned_by": "@c3po"
  }
}
```

## Usage

### Automatic Assignment

Tickets are automatically assigned when created:

```bash
python scripts/python/jarvis_pr_ticket_coordinator.py --create \
  --title "Issue Title" \
  --description "Description" \
  --type bug_fix
```

C-3PO automatically:
1. Routes ticket to appropriate team
2. Assigns Team Manager (`@c3po`)
3. Assigns Technical Lead (team-specific)
4. Assigns Business Lead (if applicable)
5. Sets Primary Assignee (Technical Lead)

### Manual Assignment

Assign existing ticket to specific team:

```bash
python scripts/python/jarvis_c3po_ticket_assigner.py --assign HELPDESK-0001 --team docker_engineering
```

### Assign All Unassigned

Assign all unassigned tickets:

```bash
python scripts/python/jarvis_c3po_ticket_assigner.py --assign-all
```

### Get Team Tickets

View all tickets for a team:

```bash
python scripts/python/jarvis_c3po_ticket_assigner.py --team-tickets docker_engineering
```

## Team Management Workflow

1. **Ticket Created**: PR and ticket created with cross-reference
2. **C-3PO Assignment**: C-3PO assigns ticket to appropriate team
3. **Team Structure**: Ticket includes Team Manager, Technical Lead, Business Lead
4. **Team Coordination**: Team Manager (`@c3po`) coordinates workflow
5. **Technical Work**: Technical Lead (`@r2d2` or team-specific) implements solution
6. **Business Input**: Business Lead provides domain expertise (if applicable)
7. **Resolution**: Team resolves ticket with proper coordination

## Example: HELPDESK-0001

**Ticket**: Fix: Invalid 'Iron Legion' model references

**Team Assignment**:
- **Team**: Docker Engineering Team
- **Team Manager**: `@c3po` (coordinates workflow)
- **Technical Lead**: `@r2d2` (implements fix)
- **Business Lead**: Docker Engineering Lead (provides Docker expertise)
- **Primary Assignee**: `@r2d2` (works on ticket)

**Status**: `assigned` (ready for team to work on)

## Integration

The team assignment system integrates with:

- **PR/Ticket Coordinator**: Automatic team assignment on ticket creation
- **Organizational Structure**: Uses organizational structure for team routing
- **Helpdesk System**: Routes to appropriate helpdesk teams
- **@DOIT**: Can auto-assign tickets for autonomous tasks

## Benefits

1. **Proper Management**: Team Manager ensures coordination
2. **Technical Leadership**: Technical Lead provides expertise
3. **Business Input**: Business Lead provides domain knowledge
4. **Clear Ownership**: Primary Assignee clearly identified
5. **Team Coordination**: All team members know their roles
6. **Escalation Path**: Clear escalation through Team Manager

## Status Flow

- `open` → Ticket created, not yet assigned
- `assigned` → C-3PO assigned to team (Team Manager, Technical Lead, Business Lead set)
- `in_progress` → Team working on ticket
- `review` → Under review
- `resolved` → Issue resolved
- `closed` → Ticket closed/completed
