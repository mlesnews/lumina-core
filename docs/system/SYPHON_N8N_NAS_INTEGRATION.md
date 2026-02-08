# SYPHON N8N@NAS Integration

## Overview

Comprehensive integration of all SYPHON sources with N8N workflows running on NAS (10.17.17.32:5678). All intelligence extraction (email, SMS, social-news-education) routes through N8N workflows on NAS.

## Architecture

```
┌─────────────────┐
│  Email Sources  │
│  SMS Sources    │──┐
│  Education      │  │
│  Sources        │  │
└─────────────────┘  │
                     │
                     ▼
         ┌───────────────────────┐
         │   N8N@NAS             │
         │   (10.17.17.32:5678)  │
         │                        │
         │  ┌─────────────────┐ │
         │  │ Email Workflow   │ │
         │  │ SMS Workflow     │ │
         │  │ Education        │ │
         │  │ Workflow         │ │
         │  └─────────────────┘ │
         └───────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   SYPHON System       │
         │   (10.17.17.11:8000) │
         │                        │
         │  Intelligence         │
         │  Extraction           │
         └───────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   Unified Queue       │
         │   Holocron Archive    │
         └───────────────────────┘
```

## Workflows

### 1. Email SYPHON Workflow

**Schedule**: Every 2 hours  
**Trigger**: Schedule Trigger  
**Process**:
1. Fetch all emails from NAS email accounts (IMAP)
2. Format email data for SYPHON
3. Extract intelligence via SYPHON API
4. Save intelligence to NAS storage
5. Add to unified queue

**Webhook**: `http://10.17.17.32:5678/webhook/email/syphon`

### 2. SMS SYPHON Workflow

**Schedule**: Every 3 hours  
**Trigger**: Webhook + Schedule Trigger  
**Process**:
1. Receive SMS via webhook or scheduled fetch
2. Format SMS data for SYPHON
3. Extract intelligence via SYPHON API
4. Save intelligence to NAS storage
5. Add to unified queue

**Webhook**: `http://10.17.17.32:5678/webhook/sms/syphon`

### 3. Social-News-Education SYPHON Workflow

**Schedule**: Every 6 hours  
**Trigger**: Schedule Trigger  
**Sources**:
- ArXiv (white papers, research papers)
- ResearchGate (thesis, publications)
- Web sources (PDF white papers, thesis)

**Process**:
1. Fetch from ArXiv, ResearchGate, web sources
2. Merge and format education sources
3. Extract intelligence via SYPHON API
4. Save intelligence to NAS storage
5. Add to unified queue

**Webhook**: `http://10.17.17.32:5678/webhook/education/syphon`

## Deployment

### Deploy All Workflows

```bash
python scripts/python/deploy_syphon_n8n_workflows_nas.py
```

This will:
1. Check N8N connection on NAS
2. Create/update email workflow
3. Create/update SMS workflow
4. Create/update education workflow
5. Save deployment report

### Manual Workflow Import

1. Access N8N on NAS: `http://10.17.17.32:5678`
2. Import workflow JSON files from `data/n8n_syphon_workflows/`
3. Configure credentials (IMAP, API keys)
4. Activate workflows

## Configuration

### N8N Settings

**File**: `config/n8n_nas_communication_config.json`

```json
{
  "n8n_host": "10.17.17.32",
  "n8n_port": 5678,
  "nas_host": "nas.lesnewski.local",
  "nas_n8n_url": "http://nas.lesnewski.local:5678"
}
```

### SYPHON API Endpoints

- **Email**: `http://10.17.17.11:8000/api/syphon/email`
- **SMS**: `http://10.17.17.11:8000/api/syphon/sms`
- **Web/Education**: `http://10.17.17.11:8000/api/syphon/web`

### Unified Queue API

- **Add Item**: `http://10.17.17.11:8000/api/unified-queue/add`

## Data Storage

### Intelligence Storage

All extracted intelligence is saved to NAS storage:

- **Email**: `/data/syphon/email_intelligence/YYYY-MM-DD_email_intelligence.jsonl`
- **SMS**: `/data/syphon/sms_intelligence/YYYY-MM-DD_sms_intelligence.jsonl`
- **Education**: `/data/syphon/education_intelligence/YYYY-MM-DD_education_intelligence.jsonl`

### Workflow Registry

**File**: `data/n8n_syphon_workflows/deployed_workflows.json`

Tracks all deployed workflows with IDs and URLs.

## Monitoring

### Workflow Status

Check workflow execution in N8N:
- Access: `http://10.17.17.32:5678`
- View executions, logs, errors

### Deployment Reports

**Location**: `data/n8n_syphon_workflows/deployment_report_*.json`

Contains deployment timestamps, results, and workflow IDs.

## Integration Points

### With SYPHON Source Sweeps & Scans

- N8N workflows trigger SYPHON extraction
- Results feed into unified queue
- Deduplication handled by SYPHON system

### With Unified Queue

- All intelligence automatically added to queue
- Priority-based processing
- Status tracking

### With Holocron Archive

- Intelligence stored in holocron
- Version tracking
- Query capabilities

## Status

✅ **COMPLETE** - SYPHON N8N@NAS Integration

Features:
- ✅ Email SYPHON workflow
- ✅ SMS SYPHON workflow
- ✅ Social-News-Education SYPHON workflow
- ✅ Automated deployment script
- ✅ NAS storage integration
- ✅ Unified queue integration
- ✅ Workflow registry and monitoring

---

**Tags**: @SYPHON @N8N @NAS #EMAIL #SMS #EDUCATION #WHITE_PAPER #THESIS @JARVIS @LUMINA
