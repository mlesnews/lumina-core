# Helpdesk Support Teams

## Overview

Three new teams have been created to support the droid team operations:

1. **Helpdesk Support Team** (`@helpdesk`) - Helpdesk operations and ticket management
2. **Problem Management Team** (`@pm[#problem #management]`) - Problem identification and resolution
3. **Change Management Team** (`@cm[#change #management]`) - Change management and deployment

## Team Structure

All teams follow the standard team structure pattern:

### Required Roles
- **Team Manager**: `@c3po` (Helpdesk Coordinator)
- **Technical Lead**: `@r2d2` (Technical Lead Engineer)
- **Business Lead**: Domain-specific (varies by team)

## 1. Helpdesk Support Team

**Team ID**: `helpdesk_support`  
**Tags**: `#helpdesk`, `@helpdesk`  
**Config**: `config/helpdesk/helpdesk_support_team.json`  
**Job Slots**: 10  
**Frameworks**: MANUS, ELEVENLABS, DOCKER, n8n  
**Cloud Platforms**: Azure, AWS

### Purpose
Helpdesk operations, ticket management, workflow coordination, and droid team support with full framework and cloud platform integration.

### Job Slots (Team Members)
1. **Team Manager** - `@c3po` (Helpdesk Coordinator)
2. **Technical Lead** - `@r2d2` (Technical Lead Engineer)
3. **Helpdesk Analyst 1** - Ticket triage, workflow coordination, droid team support (Smart Agent)
4. **Helpdesk Coordinator 1** - Helpdesk coordination, protocol enforcement, team support (Smart Agent)
5. **Helpdesk Engineer 1** - Helpdesk automation, system integration, workflow engineering (Smart Agent)
6. **Framework Specialist - MANUS** - Workstation control and automation (Smart Agent)
7. **Framework Specialist - ElevenLabs** - Voice synthesis and audio processing (Smart Agent)
8. **Framework Specialist - Docker** - Container management and orchestration (Smart Agent)
9. **Cloud Specialist - Azure** - Azure platform integration (Smart Agent)
10. **Cloud Specialist - AWS** - AWS platform integration (Smart Agent)
11. **Workflow Specialist - n8n** - Workflow automation and integration (Smart Agent)

### Capabilities
- Ticket management
- Workflow coordination
- Droid team support
- Escalation management
- Protocol enforcement
- System integration
- Workflow engineering
- **Framework Support**: MANUS, ELEVENLABS, DOCKER, n8n
- **Cloud Platform Support**: Azure, AWS

### Ticket Numbering Standard
All tickets use 9-digit format with prefix:
- **PM** (Problem Management): `PM000000001`
- **CR** (Change Request): `CR000000001`
- **T** (Task): `T000000001`

See `docs/system/HELPDESK_TICKET_NUMBERING.md` for full standard.

## 5. Linguistics & Human Behavioral Studies Team

**Team ID**: `linguistics_human_behavioral_studies`  
**Tags**: `#linguistics`, `#human-behavioral-studies`, `#speech-pathology`, `@DOC`, `@HR`, `@team`  
**Config**: `config/teams/linguistics_team.json`  
**Job Slots**: 7  
**Frameworks**: ELEVENLABS, MANUS, DOCKER, n8n  
**Cloud Platforms**: Azure, AWS

### Purpose
Initial linguistics team focused on human behavioral studies, speech pathology, and language analysis. Led by **@DOC** with specialized speech pathologist agents and linguistics specialists.

### Team Lead
- **@DOC** - Team Lead & Medical/Linguistic Specialist
  - Medical linguistics, speech pathology, human behavioral analysis
  - Max tickets: 12

### Job Slots (Team Members)
1. **Team Lead** - @DOC (Medical/Linguistic Specialist)
2. **Speech Pathologist 1** - General speech and language pathology
3. **Speech Pathologist 2** - Pediatric speech pathology, early intervention
4. **Speech Pathologist 3** - Adult/Neurological speech pathology
5. **Linguist 1** - Behavioral linguistics, communication patterns
6. **Linguist 2** - Computational linguistics, NLP
7. **Linguist 3** - Applied linguistics, language acquisition

### Capabilities
- Human behavioral linguistics
- Speech pathology
- Language analysis
- Communication pattern studies
- Conversation analysis
- Language disorder assessment
- Therapeutic linguistics
- Computational linguistics
- Applied linguistics
- **Framework Support**: ELEVENLABS, MANUS, DOCKER, n8n
- **Cloud Platform Support**: Azure, AWS

### Integrations
- **JARVIS**: Conversational system and language analysis
- **Medical**: @DOC integration
- **Helpdesk**: @c3po coordination
- **Frameworks**: ELEVENLABS, MANUS, DOCKER, n8n
- **Cloud Platforms**: Azure, AWS

### Routing Keywords
- linguistics
- speech_pathology
- human_behavioral_studies
- language_analysis
- medical_linguistics
- communication_disorders

See `docs/system/LINGUISTICS_TEAM.md` for full documentation.

### Routing Keywords
- helpdesk
- support
- ticket
- workflow
- coordination

## 2. Problem Management Team

**Team ID**: `problem_management`  
**Tags**: `#problem`, `#management`, `@pm`  
**Config**: `config/helpdesk/problem_management_team.json`  
**Job Slots**: 9  
**Frameworks**: DOCKER, MARVIN, R5, n8n  
**Cloud Platforms**: Azure, AWS

### Purpose
Problem identification, root cause analysis, resolution management with full framework and cloud platform integration.

### Job Slots (Team Members)
1. **Team Manager** - `@c3po` (Problem Management Coordinator)
2. **Technical Lead** - `@r2d2` (Technical Lead Engineer)
3. **Problem Analyst 1** - Problem identification, root cause analysis, trend analysis (Smart Agent)
4. **Problem Manager 1** - Problem management, resolution coordination, prevention strategies (Smart Agent)
5. **Problem Engineer 1** - Problem resolution, automated fixes, prevention implementation (Smart Agent)
6. **Framework Specialist - Docker** - Container problem resolution (Smart Agent)
7. **Cloud Specialist - Azure** - Azure platform problem resolution (Smart Agent)
8. **Cloud Specialist - AWS** - AWS platform problem resolution (Smart Agent)
9. **Analytics Specialist - Marvin** - Complex problem analysis (`@marvin`)

### Capabilities
- Problem identification
- Root cause analysis
- Pattern recognition
- Trend analysis
- Resolution coordination
- Prevention strategies
- Automated fixes
- **Framework Support**: DOCKER, MARVIN, R5, n8n
- **Cloud Platform Support**: Azure, AWS

### Routing Keywords
- problem
- root cause
- issue
- bug
- error
- failure

## 3. Change Management Team

**Team ID**: `change_management`  
**Tags**: `#change`, `#management`, `@cm`  
**Config**: `config/helpdesk/change_management_team.json`  
**Job Slots**: 10  
**Frameworks**: DOCKER, MANUS, ELEVENLABS, n8n  
**Cloud Platforms**: Azure, AWS

### Purpose
Change management, impact analysis, deployment coordination with full framework and cloud platform integration.

### Job Slots (Team Members)
1. **Team Manager** - `@c3po` (Change Management Coordinator)
2. **Technical Lead** - `@r2d2` (Technical Lead Engineer)
3. **Change Analyst 1** - Change impact analysis, risk assessment, change tracking (Smart Agent)
4. **Change Manager 1** - Change management, approval coordination, change planning (Smart Agent)
5. **Change Engineer 1** - Change implementation, deployment management, rollback procedures (Smart Agent)
6. **Framework Specialist - Docker** - Container deployment (Smart Agent)
7. **Framework Specialist - MANUS** - Workstation control deployment (Smart Agent)
8. **Framework Specialist - ElevenLabs** - Voice deployment (Smart Agent)
9. **Cloud Specialist - Azure** - Azure platform deployment (Smart Agent)
10. **Cloud Specialist - AWS** - AWS platform deployment (Smart Agent)
11. **Deployment Specialist - n8n** - Workflow deployment (Smart Agent)

### Capabilities
- Change impact analysis
- Risk assessment
- Change tracking
- Approval coordination
- Change planning
- Rollback planning
- Change implementation
- Deployment management
- **Framework Support**: DOCKER, MANUS, ELEVENLABS, n8n
- **Cloud Platform Support**: Azure, AWS

### Routing Keywords
- change
- deployment
- update
- modification
- release
- rollout

## 4. JARVIS Superagent Team

**Team ID**: `jarvis_superagent`  
**Tags**: `#jarvis`, `@jarvis`, `#superagent`, `#all_areas`, `#orchestration`  
**Config**: `config/helpdesk/jarvis_superagent_team.json`  
**Job Slots**: 11  
**Frameworks**: MANUS, ELEVENLABS, DOCKER, n8n, JARVIS  
**Cloud Platforms**: Azure, AWS

### Purpose
Comprehensive system orchestration, coordination, and execution across all domains with full framework and cloud platform mastery.

### Job Slots (Team Members)
1. **Team Manager** - `@c3po` (JARVIS Superagent Coordinator)
2. **Technical Lead** - `@r2d2` (Technical Lead Engineer - All Domains)
3. **Orchestration Specialist 1** - Cross-domain coordination (Smart Agent)
4. **Framework Master - MANUS** - Comprehensive workstation control (Smart Agent)
5. **Framework Master - ElevenLabs** - Advanced voice systems (Smart Agent)
6. **Framework Master - Docker** - Advanced container orchestration (Smart Agent)
7. **Cloud Master - Azure** - Comprehensive Azure platform expertise (Smart Agent)
8. **Cloud Master - AWS** - Comprehensive AWS platform expertise (Smart Agent)
9. **Workflow Master - n8n** - Advanced automation (Smart Agent)
10. **Integration Architect** - Multi-platform design (Smart Agent)
11. **Security Master** - `@k2so` (Comprehensive security)

### Capabilities
- Cross-domain orchestration
- Multi-platform integration
- Advanced framework mastery
- Comprehensive cloud platform expertise
- Integration architecture
- Security mastery
- **Framework Mastery**: MANUS, ELEVENLABS, DOCKER, n8n, JARVIS
- **Cloud Platform Mastery**: Azure, AWS

## Integration

### Ticket Routing
Tickets are automatically routed to these teams based on content:

- **Helpdesk/Support issues** → Helpdesk Support Team
- **Problem/Issue/Bug issues** → Problem Management Team
- **Change/Deployment issues** → Change Management Team
- **Cross-domain/Orchestration/Complex** → JARVIS Superagent Team

### Team Assignment
All tickets assigned to these teams include:
- Team Manager: `@c3po`
- Technical Lead: `@r2d2`
- Business Lead: Domain-specific
- Primary Assignee: Technical Lead

### Framework Integrations
All teams support comprehensive framework integrations:
- **MANUS**: Workstation control and automation
- **ELEVENLABS**: Voice synthesis and audio processing
- **DOCKER**: Container management and orchestration
- **n8n**: Workflow automation and integration
- **JARVIS**: System orchestration (Superagent team)

### Cloud Platform Integrations
All teams support comprehensive cloud platform integrations:
- **Azure**: Azure Key Vault, Azure OpenAI, Azure Storage, Azure Functions, Azure Logic Apps
- **AWS**: AWS Bedrock, AWS S3, AWS Lambda, AWS Secrets Manager, AWS CloudWatch

### Smart/Intelligent Agents
All job slots (except Team Managers and Technical Leads) are implemented as Smart/Intelligent Agents with:
- Framework-specific expertise
- Cloud platform-specific expertise
- Intelligent routing and coordination
- Automated workflow capabilities

### Helpdesk Configuration
Teams are registered in `config/helpdesk/helpdesk_structure.json`:
- Routing domains configured
- Tags defined
- Team configurations available
- Job slots documented
- Framework integrations specified
- Cloud platform integrations specified

## Usage

### Automatic Routing
Tickets are automatically routed when created:

```bash
python scripts/python/jarvis_pr_ticket_coordinator.py --create \
  --title "Problem: System error" \
  --description "Root cause analysis needed" \
  --type bug_fix
```

**Result**: Routed to Problem Management Team

### Manual Assignment
Assign ticket to specific team:

```bash
python scripts/python/jarvis_c3po_ticket_assigner.py --assign HELPDESK-XXXX --team problem_management
```

### Team Queries
Get all tickets for a team:

```bash
python scripts/python/jarvis_c3po_ticket_assigner.py --team-tickets helpdesk_support
```

## Support for Droid Team

These teams support the droid team by:

1. **Helpdesk Support**: Manages tickets and workflows for droids
2. **Problem Management**: Identifies and resolves problems affecting droids
3. **Change Management**: Manages changes and deployments for droid systems

All teams coordinate through `@c3po` (Team Manager) and `@r2d2` (Technical Lead) to ensure proper support for droid operations.
