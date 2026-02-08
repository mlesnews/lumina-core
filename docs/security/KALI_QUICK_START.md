# Hardened Kali Linux - Quick Start Guide

**System:** MILLENIUM_FALC (x64, 64GB RAM)  
**Status:** ✅ Building

---

## 🚀 Quick Commands

### Build Image
```bash
# Full build with all checks
python scripts/python/build_hardened_kali.py --full

# Build only (faster)
python scripts/python/build_hardened_kali.py --build
```

### Run Container
```bash
# Basic
docker run -it --rm --name kali-hardened kali-hardened-millennium-falc:latest

# With NAS volume (saves local disk space)
docker run -it --rm --name kali-hardened \
  -v M:\docker\kali:/home/kali/data \
  kali-hardened-millennium-falc:latest
```

### Security Monitoring
```bash
# Full security report
python scripts/python/kali_ai2ai_security_monitor.py --report

# Check container health
python scripts/python/kali_ai2ai_security_monitor.py --health

# Scan vulnerabilities
python scripts/python/kali_ai2ai_security_monitor.py --scan
```

---

## 📋 What's Included

### Security Features
- ✅ Non-root user (kali)
- ✅ Minimal attack surface
- ✅ Security hardening script
- ✅ Health checks
- ✅ AI2AI monitoring

### Tools Installed
- nmap, wireshark, tcpdump
- metasploit-framework
- curl, wget, git, vim, nano
- Essential system utilities

---

## 🤖 AI2AI Integration

Automated security monitoring via JARVIS:
- Real-time container health
- Vulnerability scanning
- Automated alerts
- Integration with LUMINA ecosystem

---

## 💾 NAS Storage

Save local disk space (C: drive 94% full):
- Store Docker volumes on NAS
- Use `M:\docker\kali` or `N:\docker\kali`
- 37.2 TB available on NAS

---

## 📊 Build Status

**Current:** Building image (downloading packages)  
**Image:** `kali-hardened-millennium-falc:latest`  
**Location:** `docker/kali-hardened/`

---

## 🔗 Related Files

- **Dockerfile:** `docker/kali-hardened/Dockerfile`
- **Build Script:** `scripts/python/build_hardened_kali.py`
- **Security Monitor:** `scripts/python/kali_ai2ai_security_monitor.py`
- **Full Documentation:** `docs/security/HARDENED_KALI_LINUX_BUILD.md`

---

**Last Updated:** January 10, 2025
