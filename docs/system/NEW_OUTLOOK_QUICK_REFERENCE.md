# New Outlook Setup - Quick Reference

**Remove Gmail, Add NAS Company Email**

---

## ⚡ Quick Steps

### Remove Gmail
1. New Outlook → `Ctrl+Shift+A` (Account Settings)
2. Select Gmail → **Remove** → Confirm

### Add NAS Email
1. New Outlook → File → **Add Account**
2. **Advanced setup** → **IMAP**
3. Email: `mlesn@homelab.lesnewski.local`
4. IMAP: `10.17.17.32:993` (SSL/TLS)
5. SMTP: `10.17.17.32:587` (STARTTLS)
6. **Connect**

---

## 📋 Settings

```
Email: mlesn@homelab.lesnewski.local
IMAP: 10.17.17.32:993 (SSL/TLS)
SMTP: 10.17.17.32:587 (STARTTLS)
Password: [From Azure Vault: n8n-password]
```

---

**Full instructions**: `docs/system/NEW_OUTLOOK_SETUP_STEPS.md`
