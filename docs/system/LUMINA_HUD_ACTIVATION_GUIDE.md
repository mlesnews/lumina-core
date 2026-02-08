# LUMINA HUD Activation Guide

**Quick Start: Deploy & Activate LUMINA HUD**

---

## 🚀 One-Command Activation

```bash
python scripts/python/lumina_hud_deploy_activate.py --deploy-activate
```

That's it! HUD is now active.

---

## 📱 Access HUD

### Desktop
```
http://localhost:8080
```

### Mobile (Same Network)
```
http://<your-computer-ip>:8080
```

Find your IP:
- Windows: `ipconfig`
- Mac/Linux: `ifconfig` or `ip addr`

---

## 🎯 What You'll See

### HUD Panels

1. **Status Panel** (Top Left)
   - Systems online
   - Health percentage
   - Uptime

2. **Metrics Panel** (Top Right)
   - CPU usage
   - Memory usage
   - Network usage

3. **Alerts Panel** (Middle Left)
   - Active alerts
   - Priority indicators
   - Visual animations

4. **Tactical Panel** (Middle Right)
   - Bridge status
   - Tactical status (GREEN/YELLOW/ORANGE/RED/BLACK)
   - Active threats
   - Operations

5. **Communications Panel** (Bottom Left)
   - N8N@NAS status
   - Active channels

6. **Intelligence Panel** (Bottom Right)
   - Collection status
   - Last update

---

## 🚨 Alert Types

- **INFO** (Cyan): Informational
- **WARNING** (Orange): Caution
- **ALERT** (Bright Orange): Attention
- **CRITICAL** (Red): Immediate action
- **EMERGENCY** (Red Fullscreen): Maximum priority

---

## ✅ Status Check

```bash
python scripts/python/lumina_hud_deploy_activate.py --status
```

---

## 🛑 Stop HUD

Press `Ctrl+C` in terminal

---

**Tags:** #HUD #ACTIVATION #QUICK_START #IRON_MAN
