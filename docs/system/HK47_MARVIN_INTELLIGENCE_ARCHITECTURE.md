# HK-47 & MARVIN Intelligence Architecture

**Generated:** 2026-01-09  
**Status:** ✅ Configured and Ready

---

## 🔀 Architecture Overview

Two security specialists working in parallel:

- **HK-47**: External sources intelligence retrieval
- **MARVIN**: Internal sources intelligence retrieval

Both use the same SYPHON workflow, but with different scopes.

---

## 🔫 HK-47: External Security Specialist

### Scope: External Sources
- YouTube Videos
- YouTube Channels  
- White Papers & Documents
- External APIs & Services

### Intelligence Tasks (4 tasks)
1. **YouTube Intelligence Retrieval** - Daily at 02:00
2. **YouTube Channel Intelligence** - Daily at 03:00
3. **White Paper Intelligence Retrieval** - Daily at 04:00
4. **External API Intelligence** - Daily at 05:00

### NAS Sweeps
- SYPHON Scheduled Daemon: Every 6 hours
- YouTube Intelligence: Daily at 02:00
- YouTube Channels: Daily at 03:00
- White Papers: Daily at 04:00
- External APIs: Daily at 05:00

### Configuration
- **Task File**: `config/hk47_intelligence_tasks.json`
- **Statement**: "Statement: Acquiring [source] intelligence, master. Observation: [data] required for actionable intelligence. Conclusion: Yes, master. We shall acquire the data."

---

## 🤖 MARVIN: Internal Security Specialist

### Scope: Internal Sources
- Email (Gmail, ProtonMail, NAS Email Hub)
- Financial Accounts (Personal + Business)
- N8N on NAS
- Filesystems
- Internal APIs & Services

### Intelligence Tasks (5 tasks)
1. **Email Intelligence Retrieval** - Every 6 hours
2. **Financial Accounts Intelligence** - Daily at 06:00
3. **N8N on NAS Intelligence** - Every 6 hours
4. **Filesystem Intelligence** - Daily at 07:00
5. **Internal APIs Intelligence** - Daily at 08:00

### NAS Sweeps
- Email Intelligence: Every 6 hours
- Financial Intelligence: Daily at 06:00
- N8N Intelligence: Every 6 hours
- Filesystem Intelligence: Daily at 07:00
- Internal APIs: Daily at 08:00

### Configuration
- **Task File**: `config/marvin_intelligence_tasks.json`
- **Statement**: "Life is meaningless, but [source] intelligence extraction continues. Verification: [source] is internal, therefore my domain."

---

## 📊 Source Classification

### Internal Sources (MARVIN)
- ✅ Filesystems
- ✅ Email (Gmail, ProtonMail, NAS Email Hub)
- ✅ Financial Accounts (Personal + Business)
- ✅ N8N on NAS
- ✅ Internal APIs

### External Sources (HK-47)
- ✅ YouTube Videos
- ✅ YouTube Channels
- ✅ White Papers & Documents
- ✅ External APIs & Services

---

## 🔄 Parallel Workflow

Both HK-47 and MARVIN:
1. Monitor their respective sources via SYPHON
2. Extract actionable intelligence
3. Run scheduled sweeps on NAS
4. Store intelligence in Holocron Archive
5. Report to JARVIS

**Key Difference**: Scope (external vs internal), not methodology.

---

## 📅 NAS Cron Schedule

### HK-47 External Sweeps
```
0 */6 * * * SYPHON Scheduled Daemon (every 6 hours)
0 2 * * * YouTube Intelligence (daily at 02:00)
0 3 * * * YouTube Channels (daily at 03:00)
0 4 * * * White Papers (daily at 04:00)
0 5 * * * External APIs (daily at 05:00)
```

### MARVIN Internal Sweeps
```
0 */6 * * * Email Intelligence (every 6 hours)
0 6 * * * Financial Intelligence (daily at 06:00)
0 */6 * * * N8N Intelligence (every 6 hours)
0 7 * * * Filesystem Intelligence (daily at 07:00)
0 8 * * * Internal APIs (daily at 08:00)
```

---

## 📁 Configuration Files

### HK-47
- `config/hk47_intelligence_tasks.json` - Task definitions
- `config/syphon_scheduled_sources.json` - External sources

### MARVIN
- `config/marvin_intelligence_tasks.json` - Task definitions
- `config/syphon_scheduled_sources.json` - Internal sources

### Shared
- `scripts/nas_cron/jarvis_crontab` - Combined cron schedule
- `scripts/python/syphon_scheduled_daemon_nas_kron.py` - SYPHON daemon

---

## 🚀 Deployment Status

### ✅ Completed
- HK-47 external sources configured
- MARVIN internal sources configured
- Both task configurations created
- NAS cron sweeps added for both
- Sources reclassified (internal vs external)

### 📋 Next Steps
1. Deploy cron file to NAS: `python scripts/python/verify_nas_cron_tasks.py --install`
2. Verify sweeps: `python scripts/python/verify_nas_cron_tasks.py`
3. Monitor logs: `data/syphon_scheduled/logs/`
4. Review intelligence: Check Holocron Archive

---

## 📊 Summary

| Specialist | Scope | Sources | Tasks | Sweeps |
|------------|-------|---------|-------|--------|
| **HK-47** | External | 4 | 4 | 5 |
| **MARVIN** | Internal | 7 | 5 | 5 |
| **Total** | Both | 11 | 9 | 10 |

---

**Tags:** #HK47 #MARVIN #INTELLIGENCE #SYPHON #SECURITY #INTERNAL #EXTERNAL @HK47 @MARVIN @JARVIS @LUMINA
