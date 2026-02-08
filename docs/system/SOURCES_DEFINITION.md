# @SOURCES Definition

## Overview

**@SOURCES** refers to all data/intelligence sources that can be SYPHONed for intelligence extraction. This includes both **internal** and **external** sources.

## Source Categories

### Internal Sources

#### 📧 Email
- **All Email Accounts**: Gmail, ProtonMail, and other email accounts
- **Purpose**: Extract actionable intelligence from email communications
- **Storage**: Holocron archive
- **Scripts**: `syphon_all_emails_to_holocron_youtube.py`

#### 📱 SMS
- **All SMS Messages**: Text messages from all sources
- **Purpose**: Extract actionable intelligence from SMS communications
- **Storage**: Holocron archive
- **Scripts**: `syphon_all_sms_to_holocron_youtube.py`

#### 💬 Messenger
- **All Messenger Platforms**: Telegram, Discord, Slack, WhatsApp, Signal, etc.
- **Purpose**: Extract actionable intelligence from messenger communications
- **Storage**: Holocron archive
- **Scripts**: `syphon_all_messengers_to_holocron.py`

#### 📚 Documentation
- **All Documentation**: Project documentation, markdown files, technical docs
- **Purpose**: Extract intelligence from documentation
- **Storage**: Holocron archive
- **Scripts**: `sync_documentation_to_holocron.py`

#### 🗄️ Holocron
- **All Holocrons**: Holocron databases and archives
- **Purpose**: Extract intelligence from holocron archives
- **Storage**: Holocron archive
- **Scripts**: `backup_mariadb_holocrons.py`, `schedule_holocron_backups.py`

### External Sources

#### 🌐 Web Sources
- **Web Pages**: Websites, web content
- **Purpose**: Extract intelligence from web sources
- **Storage**: Holocron archive
- **Scripts**: `web_crawl_scheduled.py`

#### 🔌 API Sources
- **External APIs**: API endpoints for data extraction
- **Purpose**: Poll external APIs for new data
- **Storage**: Holocron archive
- **Scripts**: `api_poll_external_sources.py`

#### 📱 Social Media Sources
- **Social Platforms**: Twitter, Facebook, LinkedIn, etc.
- **Purpose**: Extract intelligence from social media
- **Storage**: Holocron archive
- **Scripts**: `syphon_social_media_external.py`

#### 📰 News Feed Sources
- **News Feeds**: News websites, RSS feeds
- **Purpose**: Extract intelligence from news sources
- **Storage**: Holocron archive
- **Scripts**: `syphon_news_feeds_external.py`

#### 📡 RSS Feed Sources
- **RSS Feeds**: RSS feed subscriptions
- **Purpose**: Extract intelligence from RSS feeds
- **Storage**: Holocron archive
- **Scripts**: `syphon_rss_feeds_external.py`

### Social-News-Education Sources

#### 📄 White Papers
- **Academic/Technical White Papers**: Research papers, technical documentation
- **Purpose**: Extract intelligence from white papers
- **Category**: External Documentation Sources
- **Storage**: Holocron archive

#### 🎓 Thesis
- **Academic Theses**: PhD theses, research theses
- **Purpose**: Extract intelligence from academic theses
- **Category**: External Documentation Sources
- **Storage**: Holocron archive

#### 📚 Education Sources
- **Educational Content**: Courses, tutorials, educational materials
- **Purpose**: Extract intelligence from educational sources
- **Category**: External Documentation Sources
- **Storage**: Holocron archive

## @SOURCES Characteristics

### Internal Sources
- **Owned/Controlled**: Sources you own or have direct access to
- **Examples**: Your email accounts, your SMS, your documentation
- **Access**: Direct access via APIs, IMAP, POP3, file systems

### External Sources
- **Public/Third-Party**: Sources from external providers
- **Examples**: Web pages, social media, news feeds, public APIs
- **Access**: Web scraping, API polling, RSS feeds

### External Sources for Internal Systems
- **External Data for Internal Categories**: External sources that feed into internal categories
- **Examples**: 
  - External email sources (public email archives)
  - External SMS sources (public SMS databases)
  - External messenger sources (public channels)
  - External documentation sources (public docs, wikis)
  - External holocron sources (public archives)

## Intelligence Extraction

### SYPHON Process
1. **Discovery**: Identify sources to SYPHON
2. **Extraction**: Extract actionable intelligence
3. **Deduplication**: Skip duplicates unless substantial updates
4. **Storage**: Store in holocron archive
5. **Queue**: Add to unified queue for processing

### Intelligence Types
- **Actionable Intelligence**: Information that can be acted upon
- **Metadata**: Source information, timestamps, categories
- **Content**: Full content extraction
- **Summaries**: Intelligent summaries of content

## Integration

### With Kron Scheduler
- **Scheduled SYPHON**: All sources scheduled via kron scheduler
- **Recurring Events**: Email (every 2h), SMS (every 3h), etc.
- **Priority-Based**: Based on triage/BAU priorities

### With Unified Queue
- **Queue Items**: All SYPHONed sources added to unified queue
- **Status Tracking**: Track processing status
- **Priority Management**: Priority-based processing

### With Holocron Archive
- **Storage**: All intelligence stored in holocron archive
- **Versioning**: Intelligence versions tracked
- **Retrieval**: Query holocron for intelligence

## Source Identification

### Source IDs
- **Format**: `{category}_{type}_{identifier}`
- **Examples**:
  - `internal_email_all`
  - `external_web_sources`
  - `external_email_sources`

### Source Metadata
- **Name**: Human-readable name
- **Category**: Internal or External
- **Type**: Email, SMS, Web, etc.
- **URL/Endpoint**: Source location
- **Priority**: 1-10 (1 is highest)
- **Scan Interval**: How often to scan

## Status

✅ **DEFINED** - @SOURCES definition complete

**@SOURCES** = All data/intelligence sources (internal and external) that can be SYPHONed for intelligence extraction, including:
- Email, SMS, Messenger (internal)
- Documentation, Holocron (internal)
- Web, API, Social, News, RSS (external)
- White Papers, Thesis, Education (external documentation)

---

**Tags**: @SOURCES @SYPHON @INTELLIGENCE @INTERNAL @EXTERNAL @EMAIL @SMS @MESSENGER @DOCUMENTATION @HOLOCRON
