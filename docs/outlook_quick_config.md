# Outlook Quick Configuration Guide

## Quick Settings Reference

**Email Address**: `mlesn@homelab.lesnewski.local`  
**IMAP Server**: `10.17.17.32:993` (SSL/TLS)  
**SMTP Server**: `10.17.17.32:587` (STARTTLS)  
**Username**: `mlesn@homelab.lesnewski.local`  
**Password**: [Your NAS Mail Hub password]

---

## Fast Setup (5 Steps)

1. **File** → **Account Settings** → **Account Settings** → **New...**
2. **Manual setup** → **POP or IMAP**
3. Enter:
   - Email: `mlesn@homelab.lesnewski.local`
   - Type: **IMAP**
   - Incoming: `10.17.17.32`
   - Outgoing: `10.17.17.32`
4. **More Settings**:
   - **Outgoing Server**: Check "requires authentication" → "Use same settings"
   - **Advanced**: IMAP port `993` (SSL/TLS), SMTP port `587` (STARTTLS)
5. **Next** → Test → **Finish**

---

## Network Info

- **Your IP**: `10.17.17.191` (Wi-Fi)
- **Server IP**: `10.17.17.32` (NAS Mail Hub)
- **Network**: `10.17.17.x/24` ✅

---

## Troubleshooting

**Can't connect?**
1. Run: `powershell -File scripts/powershell/check_nas_mail_hub_status.ps1`
2. Verify NAS Mail Hub is running
3. Check firewall allows ports 993 and 587

**Authentication failed?**
- Verify password is correct
- Check username: `mlesn@homelab.lesnewski.local`

---

*Last Updated: 2026-01-16*
