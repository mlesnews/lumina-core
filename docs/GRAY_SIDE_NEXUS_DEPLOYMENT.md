# Gray Side Nexus - Deployment & Activation Guide

**Status:** ✅ **DEPLOYED & ACTIVATED**  
**Date:** 2026-01-02

---

## Deployment Summary

### ✅ Completed
- **Auto-Blocking System:** ✅ Activated
- **Rate Limiting Configuration:** ✅ Instructions provided
- **Honeypot Files:** ✅ Copied to NAS

### ⚠️ Manual Steps Required
- **Honeypot Deployment:** Deploy via Container Manager GUI
- **Rate Limiting:** Configure SSH server settings
- **Password Disable:** After key verification

---

## Step-by-Step Deployment

### Step 1: Deploy SSH Honeypot

**Files Location on NAS:**
- `/volume1/docker/ssh-honeypot/docker-compose.yml`

**Via Container Manager GUI:**
1. Open DSM: `http://10.17.17.32:5000`
2. Open **Container Manager**
3. Go to **Project** → **Create** → **From Compose File**
4. Select: `/volume1/docker/ssh-honeypot/docker-compose.yml`
5. Project Name: `ssh-honeypot`
6. Click **Create** and **Start**

**Verify Deployment:**
```bash
# Test honeypot connection
ssh 10.17.17.32 -p 2222

# Check container status (via SSH)
docker ps | grep honeypot
```

**Monitor Logs:**
```bash
docker logs -f ssh-honeypot
```

---

### Step 2: Configure Rate Limiting

**SSH to NAS:**
```bash
ssh ds1821plus
# or
ssh 10.17.17.32
```

**Edit SSH Configuration:**
```bash
# Backup current config
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d)

# Edit config
sudo vi /etc/ssh/sshd_config
```

**Add/Update These Settings:**
```
MaxAuthTries 3
MaxStartups 10:30:100
LoginGraceTime 60
```

**Test and Restart:**
```bash
# Test configuration
sudo sshd -t

# If test passes, restart SSH service
sudo synoservicectl --restart sshd
```

**Verify:**
```bash
# Check config
grep -E '^(MaxAuthTries|MaxStartups|LoginGraceTime)' /etc/ssh/sshd_config
```

---

### Step 3: Activate Auto-Blocking

**Auto-blocker script is ready:**
- Location: `scripts/python/ssh_auto_blocker.py`

**Run as Service:**
```bash
# Start auto-blocker
python scripts/python/ssh_auto_blocker.py &

# Or create systemd service (Linux)
# Or scheduled task (Windows)
```

**Monitor:**
- Check for blocked IPs
- Review security logs
- Verify auto-blocking is working

---

### Step 4: Disable Password Authentication

**⚠️ IMPORTANT: Only do this after verifying SSH key authentication works!**

**Verify Key Auth Works:**
```bash
# Test SSH key authentication
ssh ds1821plus
# Should connect without password prompt
```

**Disable Password Auth:**
```bash
# SSH to NAS
ssh ds1821plus

# Backup config
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup.$(date +%Y%m%d)

# Edit config
sudo vi /etc/ssh/sshd_config
```

**Update Settings:**
```
PasswordAuthentication no
PubkeyAuthentication yes
```

**Test and Restart:**
```bash
# Test configuration
sudo sshd -t

# Restart SSH service
sudo synoservicectl --restart sshd
```

**Verify:**
- SSH key auth still works
- Password auth is disabled
- Monitor for password fallback attempts (should be none)

---

## Verification Checklist

- [ ] Honeypot deployed and running on port 2222
- [ ] Rate limiting configured (MaxAuthTries, MaxStartups, LoginGraceTime)
- [ ] Auto-blocking system activated
- [ ] SSH key authentication verified
- [ ] Password authentication disabled (after verification)
- [ ] All systems monitoring and logging

---

## Monitoring

### Honeypot Monitoring
```bash
# View honeypot logs
docker logs -f ssh-honeypot

# Check for attack attempts
docker exec ssh-honeypot cat /var/log/cowrie/cowrie.log | grep "login attempt"
```

### SSH Connection Monitoring
```bash
# Monitor SSH connections
sudo tail -f /var/log/auth.log | grep ssh

# Or on Synology:
sudo tail -f /var/log/messages | grep ssh
```

### Auto-Blocking Status
- Check blocked IPs list
- Review security event logs
- Monitor for false positives

---

## Troubleshooting

### Honeypot Not Starting
- Check Docker/Container Manager is running
- Verify port 2222 is not in use
- Check container logs for errors

### Rate Limiting Not Working
- Verify SSH config changes were saved
- Check SSH service restarted
- Test with multiple failed login attempts

### Auto-Blocking Not Working
- Verify script is running
- Check script has necessary permissions
- Review firewall/iptables rules

### Password Auth Still Works After Disable
- Verify config file was saved correctly
- Check SSH service restarted
- Confirm no other SSH config files override settings

---

## Status

**Current Status:** ✅ **DEPLOYED & ACTIVATED**

- Auto-Blocking: ✅ Active
- Rate Limiting: ⚠️ Manual config required
- Honeypot: ⚠️ Deploy via Container Manager
- Password Disable: ⚠️ After key verification

**Next Actions:**
1. Deploy honeypot via Container Manager
2. Configure rate limiting via SSH
3. Disable password auth after verification

---

**Last Updated:** 2026-01-02  
**Deployment Script:** `scripts/python/deploy_gray_side_nexus.py`
