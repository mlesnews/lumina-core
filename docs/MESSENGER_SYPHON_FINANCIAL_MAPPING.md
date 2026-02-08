# Messenger SYPHON & Financial Profile Mapping

**Status**: ✅ **OPERATIONAL**  
**Version**: 1.0.0  
**Last Updated**: 2025-01-24

---

## Overview

Comprehensive system that:
1. **SYPHONs messenger platforms** (Telegram, Signal, WhatsApp, Discord, etc.)
2. **Maps financial profiles to digital online presence**
3. **Tracks portfolios and institutions**
4. **Stores in @HOLOCRON Archive**
5. **Sends to YouTube Library**

---

## Features

### Messenger Platform Support

- ✅ **Telegram** - API, bot, export
- ✅ **Signal** - Database, export
- ✅ **WhatsApp** - Export, backup
- ✅ **Discord** - API, bot, export
- ✅ **Slack** - API, bot, export, workspace export
- ✅ **Matrix/Element** - (Planned)

### Financial Profile Mapping

- ✅ **Profile Tracking** - Individual, institution, portfolio, entity
- ✅ **Digital Presence Mapping** - Social profiles, websites, messenger profiles
- ✅ **Portfolio Tracking** - Asset tracking, value calculation
- ✅ **Institution Mapping** - Banks, brokerages, exchanges, fintech

### Intelligence Extraction

- ✅ Actionable items
- ✅ Tasks
- ✅ Decisions
- ✅ Intelligence insights
- ✅ Pattern recognition

### Storage & Integration

- ✅ **Holocron Archive** - Permanent knowledge storage
- ✅ **YouTube Library** - Content organization
- ✅ **Financial Profiles** - Profile management
- ✅ **Portfolio Tracking** - Asset management
- ✅ **Institution Mapping** - Organization tracking

---

## Configuration

### Messenger Sources Config

**File**: `config/messenger_sources.json`

```json
{
  "sources": [
    {
      "source_id": "telegram_api",
      "source_name": "Telegram API",
      "messenger_type": "telegram",
      "connection_type": "api",
      "api_key": "...",
      "api_secret": "...",
      "enabled": true
    }
  ]
}
```

### Source Types

1. **Telegram API** - Direct Telegram API
   ```json
   {
     "messenger_type": "telegram",
     "connection_type": "api",
     "api_key": "...",
     "api_secret": "..."
   }
   ```

2. **Telegram Export** - Telegram data export
   ```json
   {
     "messenger_type": "telegram",
     "connection_type": "export",
     "export_file_path": "/path/to/telegram_export.json"
   }
   ```

3. **Signal Database** - Signal SQLite database
   ```json
   {
     "messenger_type": "signal",
     "connection_type": "database",
     "database_path": "/path/to/signal.db",
     "phone_number": "+1234567890"
   }
   ```

4. **WhatsApp Export** - WhatsApp chat export
   ```json
   {
     "messenger_type": "whatsapp",
     "connection_type": "export",
     "export_file_path": "/path/to/whatsapp_export.txt"
   }
   ```

5. **Discord Bot** - Discord bot integration
   ```json
   {
     "messenger_type": "discord",
     "connection_type": "bot",
     "bot_token": "..."
   }
   ```

6. **Slack API** - Slack Web API
   ```json
   {
     "messenger_type": "slack",
     "connection_type": "api",
     "bot_token": "xoxb-..."
   }
   ```

7. **Slack Export** - Slack workspace export
   ```json
   {
     "messenger_type": "slack",
     "connection_type": "export",
     "export_file_path": "/path/to/slack_export.zip"
   }
   ```

8. **Slack Workspace Export** - Full workspace export
   ```json
   {
     "messenger_type": "slack",
     "connection_type": "workspace_export",
     "export_file_path": "/path/to/workspace_export.zip"
   }
   ```

---

## Financial Profile Mapping

### Profile Types

1. **Individual** - Personal financial profiles
2. **Institution** - Banks, brokerages, exchanges
3. **Portfolio** - Investment portfolios
4. **Entity** - Business entities, organizations

### Digital Presence Extraction

The system automatically extracts:
- **Email addresses** from messages
- **Phone numbers** from messages
- **Websites/URLs** from messages
- **Social profiles** (Twitter, LinkedIn, etc.)
- **Messenger profiles** (Telegram, Signal, etc.)

### Portfolio Mapping

- Maps profiles to portfolios
- Tracks assets and values
- Links to institutions
- Updates automatically

### Institution Mapping

- Maps profiles to institutions
- Tracks relationships
- Links to portfolios
- Updates digital presence

---

## Usage

### Basic Usage

```python
from syphon_messengers_financial_mapping import MessengerSyphonFinancialMapping

# Initialize
syphon = MessengerSyphonFinancialMapping()

# Process all
result = syphon.process_all(max_messages_per_source=100)

print(f"Processed {result['total_messages']} messages")
print(f"SYPHON results: {result['syphon_results']}")
print(f"Mapping results: {result['mapping_results']}")
```

### Command Line

```bash
python scripts/python/syphon_messengers_financial_mapping.py
```

---

## Data Flow

```
Messenger Platforms
    ├─→ Telegram
    ├─→ Signal
    ├─→ WhatsApp
    ├─→ Discord
    └─→ Matrix
    ↓
SYPHON Extraction
    ├─→ Actionable Items
    ├─→ Tasks
    ├─→ Decisions
    └─→ Intelligence
    ↓
Financial Profile Mapping
    ├─→ Digital Presence
    ├─→ Portfolio Mapping
    └─→ Institution Mapping
    ↓
Holocron Archive
    └─→ Permanent Knowledge Storage
    ↓
YouTube Library
    └─→ Content Organization
```

---

## Output Locations

### SYPHON Results
- **Location**: `data/messenger_syphon/syphon_results.json`
- **Content**: Extracted intelligence from all messages

### Financial Profiles
- **Location**: `data/financial_profiles/financial_profiles.json`
- **Content**: Financial profile data with digital presence

### Portfolios
- **Location**: `data/financial_profiles/portfolios.json`
- **Content**: Portfolio tracking data

### Institutions
- **Location**: `data/financial_profiles/institutions.json`
- **Content**: Institution tracking data

### Digital Presence Mapping
- **Location**: `data/financial_profiles/digital_presence_mapping.json`
- **Content**: Mapping of profiles to digital presence

### Holocron Archive
- **Location**: `data/holocron/messenger_financial_intelligence/`
- **Index**: Individual JSON files per message

### YouTube Library
- **Location**: `data/youtube_library/messenger_financial_content/`
- **Content**: Message content formatted for YouTube library

---

## Financial Profile Structure

### Profile Data

```json
{
  "profile_id": "profile_001",
  "profile_name": "John Doe",
  "profile_type": "individual",
  "financial_data": {
    "total_assets": 1000000.0,
    "risk_tolerance": "moderate"
  },
  "digital_presence": {
    "email_addresses": ["john@example.com"],
    "phone_numbers": ["+1234567890"],
    "websites": ["https://johndoe.com"],
    "social_profiles": {
      "twitter": "@johndoe",
      "linkedin": "johndoe"
    },
    "messenger_profiles": {
      "telegram": "@johndoe",
      "signal": "+1234567890"
    }
  },
  "portfolios": ["portfolio_001"],
  "institutions": ["institution_001"]
}
```

### Portfolio Data

```json
{
  "portfolio_id": "portfolio_001",
  "portfolio_name": "Main Portfolio",
  "owner_profile_id": "profile_001",
  "institution_id": "institution_001",
  "assets": {
    "BTC": 1.5,
    "ETH": 10.0,
    "USD": 50000.0
  },
  "total_value": 150000.0,
  "last_updated": "2025-01-24T12:00:00"
}
```

### Institution Data

```json
{
  "institution_id": "institution_001",
  "institution_name": "Example Bank",
  "institution_type": "bank",
  "digital_presence": {
    "website": "https://examplebank.com",
    "social_profiles": {
      "twitter": "@examplebank"
    }
  },
  "portfolios": ["portfolio_001"],
  "profiles": ["profile_001"]
}
```

---

## Security

### Secure Sources

- ✅ API authentication (Telegram, Discord)
- ✅ Secure file access (exports, databases)
- ✅ Bot token security
- ✅ Credentials stored securely (not in config file)

### Best Practices

1. **Never store API keys in config file**
2. **Use environment variables for credentials**
3. **Secure export file access**
4. **Encrypt sensitive data**
5. **Limit database access**

---

## Integration

### SYPHON System

- Uses `SYPHONSystem` for intelligence extraction
- Extracts actionable items, tasks, decisions
- Pattern recognition and insights

### Holocron Archive

- Stores message intelligence permanently
- Indexed for search and retrieval
- Tagged for organization

### YouTube Library

- Formats message content for library
- Extracts intelligence for content organization
- Links to source messages

### Financial Profile System

- Integrates with existing financial workflows
- Maps to portfolios and institutions
- Tracks digital presence

---

## Examples

### Example 1: SYPHON Telegram

```python
# Configure Telegram source
source = MessengerSource(
    source_id="telegram_api",
    source_name="Telegram API",
    messenger_type="telegram",
    connection_type="api",
    api_key=os.getenv("TELEGRAM_API_KEY"),
    api_secret=os.getenv("TELEGRAM_API_SECRET"),
    enabled=True
)

# SYPHON messages
syphon = MessengerSyphonFinancialMapping()
messages = syphon.syphon_messenger(source, max_messages=100)
```

### Example 2: Map Financial Profile

```python
# Create financial profile
profile = FinancialProfile(
    profile_id="profile_001",
    profile_name="John Doe",
    profile_type="individual",
    financial_data={"total_assets": 1000000.0}
)

# Add to system
syphon.profiles[profile.profile_id] = profile

# Map to digital presence
syphon.map_financial_to_digital_presence()
```

### Example 3: SYPHON Slack

```python
# Configure Slack source
source = MessengerSource(
    source_id="slack_api",
    source_name="Slack API",
    messenger_type="slack",
    connection_type="api",
    bot_token=os.getenv("SLACK_BOT_TOKEN"),
    enabled=True
)

# SYPHON messages
syphon = MessengerSyphonFinancialMapping()
messages = syphon.syphon_messenger(source, max_messages=100)
```

### Example 4: Track Portfolio

```python
# Create portfolio
portfolio = Portfolio(
    portfolio_id="portfolio_001",
    portfolio_name="Main Portfolio",
    owner_profile_id="profile_001",
    assets={"BTC": 1.5, "ETH": 10.0},
    total_value=150000.0
)

# Add to system
syphon.portfolios[portfolio.portfolio_id] = portfolio
```

---

## Troubleshooting

### Telegram API

**Issue**: Cannot connect to Telegram API

**Solution**:
1. Verify API credentials from https://my.telegram.org/apps
2. Check phone number format
3. Complete authentication flow
4. Store credentials securely

### Signal Database

**Issue**: Cannot access Signal database

**Solution**:
1. Verify database file path
2. Check file permissions
3. Database location varies by platform
4. May require root access on Android

### WhatsApp Export

**Issue**: Cannot parse WhatsApp export

**Solution**:
1. Verify export file format
2. Check file encoding (UTF-8)
3. Verify export structure
4. Use WhatsApp's built-in export

### Discord Bot

**Issue**: Bot not receiving messages

**Solution**:
1. Verify bot token
2. Check bot permissions
3. Verify bot is in server
4. Check API rate limits

### Slack API

**Issue**: Cannot connect to Slack API

**Solution**:
1. Verify bot token from https://api.slack.com/apps
2. Check bot permissions (channels:read, im:read, mpim:read, users:read)
3. Install app to workspace
4. Check API rate limits
5. Verify token format (xoxb- for bot tokens)

### Slack Export

**Issue**: Cannot parse Slack export

**Solution**:
1. Verify export file format (ZIP or JSON)
2. Check file encoding (UTF-8)
3. Verify export structure
4. Use Slack's built-in export feature

---

## Future Enhancements

1. **Real-time SYPHON** - Continuous message monitoring
2. **Media Processing** - Extract and process media files
3. **Thread Grouping** - Group related conversations
4. **Smart Categorization** - Auto-categorize messages
5. **Contact Integration** - Link messages to contacts
6. **Location Tracking** - Extract location from messages
7. **Advanced Financial Analysis** - Portfolio analytics
8. **Institution Intelligence** - Institution research

---

## Related Documentation

- [Email SYPHON → Holocron → YouTube](./EMAIL_SYPHON_HOLOCRON_YOUTUBE.md)
- [SMS SYPHON → Holocron → YouTube](./SMS_SYPHON_HOLOCRON_YOUTUBE.md)
- [SYPHON System](../SYPHON_SYSTEM.md)
- [Holocron Archive](../HOLOCRON_ARCHIVE.md)
- [Financial Workflows](../financial/BITCOIN_WORKFLOW_IMPLEMENTATION.md)

---

**Status**: ✅ **OPERATIONAL**  
**Last Updated**: 2025-01-24

