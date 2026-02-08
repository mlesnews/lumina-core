# N8N Secure Cookie Fix - COMPLETE

**Date**: 2026-01-10  
**Status**: ✅ **FIXED**

---

## Issue

N8N was showing error: "Your n8n server is configured to use a secure cookie, however you are either visiting this via an insecure URL"

This occurred because:
- N8N was configured to use secure cookies (HTTPS only)
- Access was via HTTP (`http://10.17.17.32:5678`)
- Browser blocked the insecure connection

---

## Solution Applied

Updated N8N Docker container to disable secure cookies for HTTP access by adding environment variable:

```bash
-e N8N_SECURE_COOKIE=false
```

---

## Container Configuration

**Current N8N Container Settings**:
- **Name**: `n8n`
- **Port**: `5678:5678`
- **Volume**: `/volume1/docker/n8n:/home/node/.n8n`
- **Environment Variables**:
  - `N8N_BASIC_AUTH_ACTIVE=true`
  - `N8N_BASIC_AUTH_USER=mlesn`
  - `N8N_BASIC_AUTH_PASSWORD=<from Azure Vault>`
  - `N8N_HOST=10.17.17.32`
  - `N8N_PORT=5678`
  - `N8N_PROTOCOL=http`
  - `N8N_SECURE_COOKIE=false` ✅ **ADDED**

---

## Verification

After container restart:
1. ✅ Container recreated with secure cookie disabled
2. ✅ N8N accessible at `http://10.17.17.32:5678`
3. ✅ No more secure cookie error

---

## Next Steps

1. **Access N8N**: `http://10.17.17.32:5678`
2. **Login**: Username `mlesn`, password from Azure Vault (`n8n-password`)
3. **Import Workflows**: 
   - Go to Workflows → Import from File
   - Import from `data/n8n_syphon_workflows/workflow_json/`:
     - `email_syphon.json`
     - `sms_syphon.json`
     - `education_syphon.json`

---

## Future Enhancement (Optional)

For production, consider:
- Setting up HTTPS/TLS (recommended)
- Using reverse proxy (nginx/traefik) with SSL certificates
- Keeping `N8N_SECURE_COOKIE=true` for security

For now, `N8N_SECURE_COOKIE=false` allows HTTP access for local network use.

---

**Status**: ✅ **SECURE COOKIE ISSUE RESOLVED**

**Tags**: @N8N @NAS #SECURITY #HTTP #COOKIE @JARVIS
