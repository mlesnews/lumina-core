# JARVIS HUD - Quick Reference

**Iron Man Style Heads-Up Display**

---

## 🚀 Quick Start

### Start Server

```bash
python scripts/python/jarvis_hud_web_server.py --start --port 8080
```

### Access HUD

Open browser: `http://localhost:8080`

---

## 🚨 Create Alert

```python
from jarvis_hud_system import JARVISHUDSystem, AlertPriority, HUDDisplayType

hud = JARVISHUDSystem()

alert = hud.create_alert(
    title="Alert Title",
    message="Alert message",
    priority=AlertPriority.CRITICAL,
    display_type=HUDDisplayType.ALERTS
)
```

---

## 📊 Alert Priorities

- **INFO**: Blue/Cyan - Informational
- **WARNING**: Orange - Caution
- **ALERT**: Bright Orange - Attention
- **CRITICAL**: Red - Immediate action
- **EMERGENCY**: Red Fullscreen - Maximum priority

---

## 📱 Access

- **Desktop**: `http://localhost:8080`
- **Mobile**: `http://[server-ip]:8080`
- **API**: `http://localhost:8080/api/hud/data`

---

## 🎨 HUD Panels

- **Status Panel**: System status
- **Metrics Panel**: Performance metrics
- **Alerts Panel**: Active alerts
- **Tactical Panel**: Tactical status
- **Communications Panel**: Communication status
- **Intelligence Panel**: Intelligence status

---

**Tags:** #JARVIS #HUD #QUICK_REFERENCE #IRON_MAN
