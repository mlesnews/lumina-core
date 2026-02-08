# Outlook IMAP Configuration Guide

## Company Email Setup - NAS Mail Hub

### Quick Configuration Details

**IMAP Server Settings:**
- **Server**: `10.17.17.32`
- **Port**: `993`
- **Encryption**: `SSL/TLS`
- **Username**: `mlesn@homelab.lesnewski.local`
- **Password**: (Your NAS Mail Hub password)

**SMTP Server Settings:**
- **Server**: `10.17.17.32`
- **Port**: `587`
- **Encryption**: `STARTTLS`
- **Username**: `mlesn@homelab.lesnewski.local`
- **Password**: (Your NAS Mail Hub password)

---

## Step-by-Step Outlook Configuration

### Method 1: Automatic Setup (Recommended)

1. **Open Outlook**
   - Launch Microsoft Outlook

2. **Add Account**
   - Go to **File** → **Account Settings** → **Account Settings**
   - Click **New...** button

3. **Choose Manual Setup**
   - Select **Manual setup or additional server types**
   - Click **Next**

4. **Choose Service**
   - Select **POP or IMAP**
   - Click **Next**

5. **Enter Account Information**
   ```
   Your Name: [Your Display Name]
   Email Address: mlesn@homelab.lesnewski.local
   Account Type: IMAP
   Incoming mail server: 10.17.17.32
   Outgoing mail server (SMTP): 10.17.17.32
   ```

6. **Click "More Settings"**

7. **Outgoing Server Tab**
   - Check **"My outgoing server (SMTP) requires authentication"**
   - Select **"Use same settings as my incoming mail server"**

8. **Advanced Tab**
   - **Incoming server (IMAP)**: `993`
   - **Use the following type of encrypted connection**: `SSL/TLS`
   - **Outgoing server (SMTP)**: `587`
   - **Use the following type of encrypted connection**: `STARTTLS`
   - Click **OK**

9. **Test Account Settings**
   - Click **Next**
   - Outlook will test the connection
   - If successful, click **Finish**

---

### Method 2: Manual Configuration via Control Panel

1. **Open Mail (32-bit)**
   - Press `Win + R`
   - Type: `control /name Microsoft.Mail`
   - Press Enter

2. **Add Account**
   - Click **Email Accounts...**
   - Click **New...**

3. **Follow steps 3-9 from Method 1 above**

---

## Network Configuration

**Your Internal IP**: `10.17.17.191` (Wi-Fi adapter)
**Email Server**: `10.17.17.32` (NAS Mail Hub)
**Network**: Both on `10.17.17.x/24` subnet ✅

**Note**: VPN connections (like `10.2.0.2`) don't interfere with local network access. Your internal IP on the 10.17.17.x network remains active and can access the NAS Mail Hub directly.

## Troubleshooting

### Connection Issues

**Problem**: Cannot connect to server
- **Solution**: 
  - Verify you're on the same network as `10.17.17.32` (you are: `10.17.17.191`)
  - Check if NAS Mail Hub is running on `10.17.17.32`
  - Verify firewall allows connections on ports 993 (IMAP) and 587 (SMTP)
  - VPN should not block local network access - internal IP remains `10.17.17.191`

**Problem**: Authentication failed
- **Solution**: 
  - Verify username: `mlesn@homelab.lesnewski.local`
  - Check password is correct
  - Ensure account exists on NAS Mail Hub

**Problem**: SSL/TLS errors
- **Solution**:
  - Verify certificate is trusted
  - Try changing encryption to "None" temporarily to test, then re-enable SSL/TLS

### Port Issues

**Problem**: Connection timeout
- **Solution**: 
  - Verify ports 993 and 587 are not blocked
  - Check Windows Firewall settings
  - Verify NAS Mail Hub is listening on these ports

---

## Additional Accounts

### ProtonMail (via Bridge)

If you want to add ProtonMail account:

**IMAP Settings:**
- Server: `127.0.0.1`
- Port: `1143`
- Encryption: `STARTTLS`
- Username: `mlesnews@protonmail.com`
- Password: (Proton Bridge password)

**SMTP Settings:**
- Server: `127.0.0.1`
- Port: `1025`
- Encryption: `STARTTLS`

**Note**: Proton Bridge must be running on your PC before adding this account.

---

## Verification Checklist

After configuration, verify:

- [ ] Can receive emails
- [ ] Can send emails
- [ ] Folders sync correctly
- [ ] Sent items appear in Sent folder
- [ ] Connection is stable
- [ ] SSL/TLS encryption is active

---

## Configuration File Reference

Your configuration is stored in:
- `config/outlook/hybrid_email_config.json`
- `config/outlook/email_sync_to_nas_config.json`

---

*Last Updated: 2026-01-16*
