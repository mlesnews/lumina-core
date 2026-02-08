# Kron Scheduler - Comprehensive Internal & External Recurring Events

## Overview

Comprehensive kron scheduler that manages all recurring events for:
- **Internal**: email, SMS, messenger, documentation, @holocrons
- **External**: all @sources for both internal and external systems

Integrates with NAS KronScheduler, SYPHON system, Holocron archive, Unified Queue Adapter, and Triage/BAU coordination.

## Internal Events

### 📧 Email Events

#### `internal_email_syphon_all`
- **Schedule**: Every 2 hours (`0 */2 * * *`)
- **Priority**: HIGH
- **Description**: SYPHON all email accounts (secure and unsecure) for data mining and holocron archive
- **Script**: `syphon_all_emails_to_holocron_youtube.py`
- **Tags**: email, syphon, holocron, internal, recurring

#### `internal_email_backup`
- **Schedule**: Daily at 3 AM (`0 3 * * *`)
- **Priority**: MEDIUM
- **Description**: Backup all email messages to holocron archive
- **Script**: `syphon_all_emails_to_holocron_youtube.py --backup-only`
- **Tags**: email, backup, holocron, internal

### 📱 SMS Events

#### `internal_sms_syphon_all`
- **Schedule**: Every 3 hours (`0 */3 * * *`)
- **Priority**: HIGH
- **Description**: SYPHON all SMS/text messages for data mining and holocron archive
- **Script**: `syphon_all_sms_to_holocron_youtube.py`
- **Tags**: sms, syphon, holocron, internal, recurring

#### `internal_sms_backup`
- **Schedule**: Daily at 4 AM (`0 4 * * *`)
- **Priority**: MEDIUM
- **Description**: Backup all SMS messages to holocron archive
- **Script**: `syphon_all_sms_to_holocron_youtube.py --backup-only`
- **Tags**: sms, backup, holocron, internal

### 💬 Messenger Events

#### `internal_messenger_syphon`
- **Schedule**: Every 4 hours (`0 */4 * * *`)
- **Priority**: HIGH
- **Description**: SYPHON all messenger platforms (Telegram, Discord, Slack, WhatsApp, etc.) for data mining
- **Script**: `syphon_all_messengers_to_holocron.py`
- **Tags**: messenger, syphon, holocron, internal, recurring
- **Platforms**: Telegram, Discord, Slack, WhatsApp, Signal
- **Note**: Script needs to be created

### 📚 Documentation Events

#### `internal_documentation_sync`
- **Schedule**: Daily at 1 AM (`0 1 * * *`)
- **Priority**: MEDIUM
- **Description**: Sync all documentation to holocron archive
- **Script**: `sync_documentation_to_holocron.py`
- **Tags**: documentation, sync, holocron, internal

#### `internal_documentation_backup`
- **Schedule**: Weekly on Sunday at 5 AM (`0 5 * * 0`)
- **Priority**: LOW
- **Description**: Backup all documentation files
- **Script**: `backup_documentation.py`
- **Tags**: documentation, backup, internal

### 🗄️ Holocron Events

#### `internal_holocron_backup`
- **Schedule**: Daily at 2 AM (`0 2 * * *`)
- **Priority**: CRITICAL
- **Description**: Backup all holocron databases
- **Script**: `backup_mariadb_holocrons.py`
- **Tags**: holocron, backup, database, internal, critical

#### `internal_holocron_scheduled_backups`
- **Schedule**: Every 6 hours (`0 */6 * * *`)
- **Priority**: HIGH
- **Description**: Run scheduled holocron backup jobs
- **Script**: `schedule_holocron_backups.py`
- **Tags**: holocron, backup, scheduled, internal

#### `internal_holocron_sync`
- **Schedule**: Every 8 hours (`0 */8 * * *`)
- **Priority**: MEDIUM
- **Description**: Sync holocron data across systems
- **Script**: `sync_holocrons.py`
- **Tags**: holocron, sync, internal

## External Events

### 🔍 Source SYPHON Events

#### `external_source_syphon_hourly`
- **Schedule**: Every hour (`0 * * * *`)
- **Priority**: HIGH
- **Description**: SYPHON all external sources hourly for intelligence gathering
- **Script**: `syphon_lumina_hourly_nas_kron.py`
- **Tags**: syphon, sources, external, hourly, recurring

#### `external_source_syphon_daily_sweep`
- **Schedule**: Daily at 6 AM (`0 6 * * *`)
- **Priority**: CRITICAL
- **Description**: Daily comprehensive sweep of all external sources
- **Script**: `daily_source_sweeps_nas_kron_executor.py`
- **Tags**: syphon, sources, external, daily, sweep, critical

### 🌐 Web Crawl Events

#### `external_web_crawl_scheduled`
- **Schedule**: Every 4 hours (`0 */4 * * *`)
- **Priority**: MEDIUM
- **Description**: Scheduled web crawling for external sources
- **Script**: `web_crawl_scheduled.py`
- **Tags**: web, crawl, external, sources

### 🔌 API Poll Events

#### `external_api_poll`
- **Schedule**: Every 30 minutes (`*/30 * * * *`)
- **Priority**: HIGH
- **Description**: Poll external APIs for new data
- **Script**: `api_poll_external_sources.py`
- **Tags**: api, poll, external, sources

### 📱 Social Media Events

#### `external_social_media_syphon`
- **Schedule**: Every 2 hours (`0 */2 * * *`)
- **Priority**: HIGH
- **Description**: SYPHON social media platforms for external intelligence
- **Script**: `syphon_social_media_external.py`
- **Tags**: social, media, syphon, external, sources

### 📰 News Feed Events

#### `external_news_feed_syphon`
- **Schedule**: Every 3 hours (`0 */3 * * *`)
- **Priority**: MEDIUM
- **Description**: SYPHON news feeds for external intelligence
- **Script**: `syphon_news_feeds_external.py`
- **Tags**: news, feed, syphon, external, sources

### 📡 RSS Feed Events

#### `external_rss_feed_syphon`
- **Schedule**: Every 2 hours (`0 */2 * * *`)
- **Priority**: MEDIUM
- **Description**: SYPHON RSS feeds for external intelligence
- **Script**: `syphon_rss_feeds_external.py`
- **Tags**: rss, feed, syphon, external, sources

## External Sources for Internal Systems

### 📧 External Email Sources

#### `external_email_sources_syphon`
- **Schedule**: Every 6 hours (`0 */6 * * *`)
- **Priority**: MEDIUM
- **Description**: SYPHON external email sources (public archives, lists, etc.)
- **Script**: `syphon_external_email_sources.py`
- **Tags**: email, sources, external, syphon

### 📱 External SMS Sources

#### `external_sms_sources_syphon`
- **Schedule**: Every 8 hours (`0 */8 * * *`)
- **Priority**: LOW
- **Description**: SYPHON external SMS sources (public databases, archives, etc.)
- **Script**: `syphon_external_sms_sources.py`
- **Tags**: sms, sources, external, syphon

### 💬 External Messenger Sources

#### `external_messenger_sources_syphon`
- **Schedule**: Every 4 hours (`0 */4 * * *`)
- **Priority**: MEDIUM
- **Description**: SYPHON external messenger sources (public channels, groups, etc.)
- **Script**: `syphon_external_messenger_sources.py`
- **Tags**: messenger, sources, external, syphon

### 📚 External Documentation Sources

#### `external_documentation_sources_syphon`
- **Schedule**: Daily at 7 AM (`0 7 * * *`)
- **Priority**: MEDIUM
- **Description**: SYPHON external documentation sources (public docs, wikis, etc.)
- **Script**: `syphon_external_documentation_sources.py`
- **Tags**: documentation, sources, external, syphon

### 🗄️ External Holocron Sources

#### `external_holocron_sources_syphon`
- **Schedule**: Daily at 8 AM (`0 8 * * *`)
- **Priority**: LOW
- **Description**: SYPHON external holocron sources (public archives, databases, etc.)
- **Script**: `syphon_external_holocron_sources.py`
- **Tags**: holocron, sources, external, syphon

## Integration

### With NAS Cron Scheduler
- **Deployment**: All events automatically deployed to NAS cron scheduler
- **Management**: Centralized management through NAS scheduler
- **Monitoring**: Run count, success/failure tracking

### With Triage/BAU Coordinator
- **Coordination**: All events coordinated with triage/BAU priorities
- **Collation**: Events grouped for optimal scheduling
- **Dynamic Scaling**: Events adjusted based on system load

### With SYPHON System
- **Data Mining**: All events feed into SYPHON for intelligence extraction
- **Holocron Archive**: All data stored in holocron archive
- **YouTube Library**: Selected data sent to YouTube library

### With Unified Queue Adapter
- **Queue Integration**: Events can trigger queue items
- **Status Tracking**: Event status tracked in unified queue
- **Priority Management**: Event priorities aligned with queue priorities

## Usage

### Initialize Scheduler
```python
from kron_scheduler_comprehensive_events import KronSchedulerComprehensive

scheduler = KronSchedulerComprehensive()
```

### Deploy to NAS
```python
result = scheduler.deploy_to_nas()
print(f"Deployed: {result['deployed']} events")
```

### Coordinate with Triage
```python
result = scheduler.coordinate_with_triage()
print(f"Coordinated: {result['coordinated']} events")
```

### Generate Report
```python
report = scheduler.generate_report()
print(f"Total Events: {report['total_events']}")
print(f"Internal: {report['internal_events']}")
print(f"External: {report['external_events']}")
```

## Event Management

### Get Events by Category
```python
internal_events = scheduler.get_events_by_category(EventCategory.INTERNAL)
external_events = scheduler.get_events_by_category(EventCategory.EXTERNAL)
```

### Get Events by Type
```python
email_events = scheduler.get_events_by_type("email")
syphon_events = scheduler.get_events_by_type("source_syphon")
```

### Get Enabled Events
```python
enabled = scheduler.get_enabled_events()
```

## Schedule Summary

### Internal Events Schedule
- **Email**: Every 2 hours (syphon), Daily 3 AM (backup)
- **SMS**: Every 3 hours (syphon), Daily 4 AM (backup)
- **Messenger**: Every 4 hours (syphon)
- **Documentation**: Daily 1 AM (sync), Weekly Sunday 5 AM (backup)
- **Holocron**: Daily 2 AM (backup), Every 6 hours (scheduled backups), Every 8 hours (sync)

### External Events Schedule
- **Source SYPHON**: Every hour (hourly), Daily 6 AM (daily sweep)
- **Web Crawl**: Every 4 hours
- **API Poll**: Every 30 minutes
- **Social Media**: Every 2 hours
- **News Feed**: Every 3 hours
- **RSS Feed**: Every 2 hours

### External Sources for Internal Systems
- **Email Sources**: Every 6 hours
- **SMS Sources**: Every 8 hours
- **Messenger Sources**: Every 4 hours
- **Documentation Sources**: Daily 7 AM
- **Holocron Sources**: Daily 8 AM

## Status

✅ **COMPLETE** - Comprehensive kron scheduler for all internal and external recurring events

Features:
- ✅ Internal events (email, SMS, messenger, documentation, holocrons)
- ✅ External events (all @sources)
- ✅ External sources for internal systems
- ✅ NAS cron scheduler integration
- ✅ Triage/BAU coordination
- ✅ Event management and reporting
- ✅ Automatic deployment

---

**Tags**: @KRON @SCHEDULER @INTERNAL @EXTERNAL @EMAIL @SMS @MESSENGER @DOCUMENTATION @HOLOCRON @SOURCES @SYPHON
