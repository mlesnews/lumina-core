# MailPlus Setup Instructions


================================================================================
📧 GMAIL OAUTH2 SETUP INSTRUCTIONS
================================================================================

Follow these steps to add Gmail to MailPlus:

1. ACCESS MAILPLUS EXTERNAL MAIL:
   - Open DSM: https://10.17.17.32:5001
   - Go to: MailPlus Server → Settings → External Mail
   - Or: MailPlus Web Client → Settings → External Mail

2. ADD GMAIL ACCOUNT:
   - Click "Add Account" or "+" button
   - Select "Gmail" from provider list

3. COMPLETE OAUTH2 FLOW:
   - You'll be redirected to Google OAuth consent page
   - Sign in with your Gmail account
   - IMPORTANT: Check the permission:
     ✅ "Read, compose, send, and permanently delete all your email from Gmail"
   - Click "Allow" or "Continue"
   - You'll be redirected back to MailPlus

4. CONFIGURE SYNC SETTINGS:
   - Sync Frequency: Every 15 minutes (or as needed)
   - Folders to Sync: All folders or selected
   - Sync Direction: Bidirectional

5. VERIFY CONNECTION:
   - Status should show "Connected" or "Active"
   - Click "Sync Now" to test
   - Check that emails appear in MailPlus

================================================================================
⚠️  MANUAL STEP REQUIRED: OAuth2 flow must be completed in browser
================================================================================



================================================================================
🔐 PROTONMAIL BRIDGE SETUP (ON HOST PC)
================================================================================

Option B: Bridge on Host PC + MailPlus Forwarding

CURRENT SETUP:
- Proton Bridge running on host PC (localhost:1143/1025)
- MailPlus on NAS (10.17.17.32)

CHALLENGE:
- MailPlus cannot directly access localhost on host PC
- Need to bridge the connection

SOLUTIONS:

1. USE N8N AS BRIDGE:
   - N8N can access Bridge on host PC (via host.docker.internal or host IP)
   - N8N processes emails and forwards to MailPlus
   - See N8N workflow configuration

2. CONFIGURE BRIDGE FOR NETWORK ACCESS:
   - Bridge Settings → Advanced
   - Configure Bridge to listen on network IP (not just localhost)
   - Update MailPlus to connect to host PC IP
   - Update firewall rules

3. MANUAL FORWARDING:
   - Set up email forwarding rules in MailPlus
   - Or use N8N workflows to sync emails

================================================================================
⚠️  DECISION NEEDED: Bridge location and connection method
================================================================================
