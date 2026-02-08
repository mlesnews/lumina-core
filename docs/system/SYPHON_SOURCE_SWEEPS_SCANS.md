# SYPHON Source Sweeps & Scans

## Overview

Comprehensive system for sweeping and scanning all sources (internal and external) using SYPHON to extract actionable intelligence. Integrates with unified queue, holocron archive, and triage/BAU coordination.

## Features

- **Source Discovery**: Automatic cataloging of all sources
- **Deep Scanning**: Multiple scan types (quick, deep, targeted, full)
- **Intelligence Extraction**: SYPHON-powered intelligence gathering
- **Holocron Archive**: All data stored in holocron archive
- **Unified Queue Integration**: Scan results automatically added to queue
- **Triage/BAU Coordination**: Priority-based scanning
- **Scheduled Execution**: Integrated with kron scheduler

## Source Categories

### Internal Sources

#### 📧 Internal Email
- **Source ID**: `internal_email_all`
- **Scan Interval**: 60 minutes
- **Description**: All email accounts (secure and unsecure)

#### 📱 Internal SMS
- **Source ID**: `internal_sms_all`
- **Scan Interval**: 180 minutes (3 hours)
- **Description**: All SMS/text messages

#### 💬 Internal Messenger
- **Source ID**: `internal_messenger_all`
- **Scan Interval**: 240 minutes (4 hours)
- **Description**: All messenger platforms (Telegram, Discord, Slack, WhatsApp, etc.)

#### 📚 Internal Documentation
- **Source ID**: `internal_documentation_all`
- **Scan Interval**: 1440 minutes (24 hours)
- **Description**: All documentation files

#### 🗄️ Internal Holocron
- **Source ID**: `internal_holocron_all`
- **Scan Interval**: 480 minutes (8 hours)
- **Description**: All holocron databases

### External Sources

#### 🌐 Web Sources
- **Source ID**: `external_web_sources`
- **Scan Interval**: 240 minutes (4 hours)
- **Description**: Web sources for intelligence gathering

#### 🔌 API Sources
- **Source ID**: `external_api_sources`
- **Scan Interval**: 30 minutes
- **Description**: External API endpoints

#### 📱 Social Media Sources
- **Source ID**: `external_social_sources`
- **Scan Interval**: 120 minutes (2 hours)
- **Description**: Social media platforms

#### 📰 News Feed Sources
- **Source ID**: `external_news_sources`
- **Scan Interval**: 180 minutes (3 hours)
- **Description**: News feed sources

#### 📡 RSS Feed Sources
- **Source ID**: `external_rss_sources`
- **Scan Interval**: 120 minutes (2 hours)
- **Description**: RSS feed sources

### External Sources for Internal Systems

#### 📧 External Email Sources
- **Source ID**: `external_email_sources`
- **Scan Interval**: 360 minutes (6 hours)
- **Description**: External email sources (public archives, lists, etc.)

#### 📱 External SMS Sources
- **Source ID**: `external_sms_sources`
- **Scan Interval**: 480 minutes (8 hours)
- **Description**: External SMS sources (public databases, archives, etc.)

#### 💬 External Messenger Sources
- **Source ID**: `external_messenger_sources`
- **Scan Interval**: 240 minutes (4 hours)
- **Description**: External messenger sources (public channels, groups, etc.)

#### 📚 External Documentation Sources
- **Source ID**: `external_documentation_sources`
- **Scan Interval**: 1440 minutes (24 hours)
- **Description**: External documentation sources (public docs, wikis, etc.)

#### 🗄️ External Holocron Sources
- **Source ID**: `external_holocron_sources`
- **Scan Interval**: 1440 minutes (24 hours)
- **Description**: External holocron sources (public archives, databases, etc.)

## Scan Types

### Quick Scan
- **Type**: `ScanType.QUICK`
- **Description**: Fast surface scan
- **Use Case**: Frequent checks, due source scanning
- **Depth**: Limited depth, surface-level intelligence

### Deep Scan
- **Type**: `ScanType.DEEP`
- **Description**: Deep comprehensive scan
- **Use Case**: Thorough analysis, scheduled deep scans
- **Depth**: Full depth, comprehensive intelligence

### Targeted Scan
- **Type**: `ScanType.TARGETED`
- **Description**: Targeted scan of specific sources
- **Use Case**: Focused intelligence gathering
- **Depth**: Custom depth based on target

### Full Scan
- **Type**: `ScanType.FULL`
- **Description**: Full system scan
- **Use Case**: Complete system analysis
- **Depth**: Maximum depth, all intelligence

## Usage

### Initialize System
```python
from syphon_source_sweeps_scans import SyphonSourceSweepsScans, ScanType

sweeps_scans = SyphonSourceSweepsScans()
```

### Scan Single Source
```python
result = sweeps_scans.scan_source("internal_email_all", ScanType.QUICK)
print(f"Items found: {result.items_found}")
print(f"Intelligence: {result.intelligence_extracted}")
```

### Execute Comprehensive Sweep
```python
# Quick sweep of all sources
sweep_result = sweeps_scans.execute_sweep(scan_type=ScanType.QUICK)

# Deep sweep of specific categories
from syphon_source_sweeps_scans import SourceCategory
sweep_result = sweeps_scans.execute_sweep(
    scan_type=ScanType.DEEP,
    categories=[SourceCategory.INTERNAL_EMAIL, SourceCategory.EXTERNAL_WEB]
)
```

### Get Sources Due for Scan
```python
due_sources = sweeps_scans.get_sources_due_for_scan()
for source in due_sources:
    print(f"{source.name} - Due for scan")
```

### Generate Report
```python
report = sweeps_scans.generate_report()
print(f"Total Sources: {report['total_sources']}")
print(f"Enabled: {report['enabled_sources']}")
print(f"Due for Scan: {report['sources_due_for_scan']}")
```

## Integration

### With Kron Scheduler
- **Event**: `syphon_source_sweeps_scans`
- **Schedule**: Every 30 minutes (`*/30 * * * *`)
- **Priority**: HIGH
- **Description**: Comprehensive source sweeps and scans

### With Unified Queue Adapter
- **Automatic**: Scan results automatically added to queue
- **Priority**: Based on source priority
- **Metadata**: Includes scan ID, items found, intelligence extracted

### With SYPHON System
- **Intelligence Extraction**: All scans use SYPHON for intelligence extraction
- **Data Mining**: Deep analysis of all sources
- **Holocron Archive**: All data stored in holocron archive

### With Triage/BAU Coordinator
- **Priority-Based**: Sources scanned based on priority
- **Coordination**: Integrated with triage/BAU priorities
- **Load Balancing**: Scans distributed based on system load

## Scan Results

### ScanResult Structure
```python
{
    "scan_id": "scan_internal_email_all_20260110_143022",
    "source_id": "internal_email_all",
    "source_name": "All Email Accounts",
    "scan_type": "quick",
    "timestamp": "2026-01-10T14:30:22",
    "duration_seconds": 45.2,
    "items_found": 150,
    "items_processed": 150,
    "intelligence_extracted": 75,
    "errors": [],
    "metadata": {}
}
```

## Source Management

### Add Source
```python
from syphon_source_sweeps_scans import SourceDefinition, SourceCategory

new_source = SourceDefinition(
    source_id="custom_source",
    name="Custom Source",
    category=SourceCategory.EXTERNAL_WEB,
    url="https://example.com",
    enabled=True,
    priority=5,
    scan_interval_minutes=60
)

sweeps_scans.sources["custom_source"] = new_source
sweeps_scans._save_sources()
```

### Enable/Disable Source
```python
source = sweeps_scans.sources["internal_email_all"]
source.enabled = False  # Disable
sweeps_scans._save_sources()
```

### Update Scan Interval
```python
source = sweeps_scans.sources["internal_email_all"]
source.scan_interval_minutes = 30  # Scan every 30 minutes
sweeps_scans._save_sources()
```

## Scheduled Execution

### Kron Scheduler Integration
- **Event ID**: `syphon_source_sweeps_scans`
- **Schedule**: Every 30 minutes
- **Command**: `python scripts/python/syphon_source_sweeps_scans.py`
- **Auto-execution**: Scans sources due for scanning

### Manual Execution
```bash
python scripts/python/syphon_source_sweeps_scans.py
```

## Statistics

### Source Statistics
- **Total Sources**: All registered sources
- **Enabled Sources**: Currently active sources
- **Scan Count**: Total scans performed per source
- **Items Found**: Total items found per source
- **Last Scan**: Timestamp of last scan

### Scan History
- **Recent Scans**: Last 1000 scans stored
- **Success Rate**: Percentage of successful scans
- **Average Duration**: Average scan duration
- **Intelligence Extracted**: Total intelligence extracted

## Status

✅ **COMPLETE** - Comprehensive SYPHON source sweeps and scans system

Features:
- ✅ Source discovery and cataloging
- ✅ Multiple scan types (quick, deep, targeted, full)
- ✅ Intelligence extraction via SYPHON
- ✅ Unified queue integration
- ✅ Holocron archive integration
- ✅ Kron scheduler integration
- ✅ Source management
- ✅ Scan history tracking
- ✅ Comprehensive reporting

---

**Tags**: @SYPHON @SOURCE @SWEEPS @SCANS @INTELLIGENCE @HOLOCRON @QUEUE @KRON
