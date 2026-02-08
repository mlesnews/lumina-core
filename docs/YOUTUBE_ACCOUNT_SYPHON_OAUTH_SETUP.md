# YouTube Account SYPHON - OAuth Setup Required

## ⚠️ Important Note

**YouTube account data (subscriptions, watch history, likes) requires OAuth 2.0 authentication**, not just an API key.

The YouTube Data API v3 has two types of access:
1. **Public Data** (API Key): Videos, channels, playlists (public information)
2. **Private Account Data** (OAuth): Subscriptions, watch history, liked videos (requires user authorization)

## Required Setup

### 1. Google Cloud Console Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable **YouTube Data API v3**
4. Create **OAuth 2.0 credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop app" or "Web application"
   - Download the credentials JSON file

### 2. Required OAuth Scopes

The following scopes are needed:
- `https://www.googleapis.com/auth/youtube.readonly` - Read account data
- `https://www.googleapis.com/auth/youtube` - Full access (if needed)

### 3. Implementation Options

#### Option A: Use Existing OAuth Library

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=creds)
```

#### Option B: Manual Token Management

1. Get authorization URL
2. User authorizes and gets code
3. Exchange code for access token
4. Use access token for API calls

### 4. Alternative: Export YouTube Data

YouTube allows users to export their data:
1. Go to [Google Takeout](https://takeout.google.com/)
2. Select "YouTube" data
3. Choose what to export (watch history, subscriptions, etc.)
4. Download and process the exported JSON files

This exported data can then be processed by the SYPHON system without OAuth.

## Current Status

The `syphon_youtube_account_data.py` script is ready but requires:
- ✅ OAuth 2.0 credentials configured
- ✅ User authorization completed
- ✅ Access token obtained

Once OAuth is set up, the script will be able to extract:
- Subscriptions
- Watch History
- Liked Videos
- Recommendations (personalized)

## Next Steps

1. Set up OAuth 2.0 credentials
2. Implement OAuth flow in the script
3. Or use Google Takeout export as alternative
4. Process exported data through SYPHON system

---

**Status**: Framework ready, OAuth setup required  
**Alternative**: Use Google Takeout export

