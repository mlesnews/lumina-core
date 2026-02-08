# YouTube API Integration

**Status**: 🔧 READY (needs API key configuration)  
**Purpose**: Use Google API key for YouTube to scan videos for deep research

---

## 🎯 Purpose

Use the configured Google API key for YouTube to search for videos and integrate with the deep research system.

---

## 🔑 API Key Configuration

The system looks for the API key in the following order:

1. **Environment Variables**:
   - `GOOGLE_API_KEY`
   - `YOUTUBE_API_KEY`

2. **Channel Config File**:
   - `data/lumina_youtube_channel/channel.json` → `api_credentials.api_key`

3. **Secrets Directory**:
   - `config/secrets/google_api_key.json` → `api_key` or `GOOGLE_API_KEY`

---

## ⚙️ Configuration

### Option 1: Environment Variable (Recommended)

```bash
# Windows PowerShell
$env:GOOGLE_API_KEY = "your_api_key_here"

# Windows CMD
set GOOGLE_API_KEY=your_api_key_here

# Linux/Mac
export GOOGLE_API_KEY=your_api_key_here
```

### Option 2: Channel Config File

Update `data/lumina_youtube_channel/channel.json`:

```json
{
  "api_credentials": {
    "api_key": "your_api_key_here"
  }
}
```

### Option 3: Helper Script

```bash
python scripts/python/configure_youtube_api_key.py <your_api_key>
```

---

## 📊 Current Status

- **API Integration**: ✅ Code implemented
- **API Key**: ⏳ Needs configuration
- **Status**: Ready to use once API key is configured

---

## 🔍 What It Does

When API key is configured, the system will:

1. Search YouTube for videos related to:
   - AI technology
   - Artificial intelligence
   - Machine learning

2. Extract real data:
   - Video titles
   - Descriptions
   - Channel names
   - Publication dates
   - Video URLs

3. Add findings to research scans:
   - Real YouTube videos
   - No simulation
   - Real data only

---

## 🛡️ Guardrail Compliance

✅ **NO SIMULATION**: Returns empty list if API key not configured (honest)
✅ **REAL DATA ONLY**: Only returns real YouTube API data
✅ **STRAIGHT UP HONEST**: Clear about what we have/don't have

---

## 📝 Usage

Once API key is configured:

```bash
# Execute research scan (will include YouTube videos)
python scripts/python/source_deep_research_missions.py --scan
```

The system will automatically:
- Detect the API key
- Connect to YouTube API
- Search for relevant videos
- Return real findings

---

## ⚠️ Notes

- API key must have YouTube Data API v3 enabled
- Search API quota: 100 units per day (default free tier)
- Each search uses 100 units
- Max 5 videos per scan to conserve quota

---

**Status**: Ready to use. Just need to configure the API key!

