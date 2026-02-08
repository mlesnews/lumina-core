# 🤖 UI Automation Setup for Armoury Crate

## ✅ Complete Automation Solution

This guide covers **BOTH** approaches:
1. **UI Automation** - Fully hands-off control
2. **Manual Setup** - One-time configuration for automation

---

## 🚀 Quick Start: UI Automation

### **Step 1: Install UI Automation Packages**

```bash
python scripts/python/setup_ui_automation.py
```

Or manually:
```bash
pip install pyautogui pygetwindow Pillow
```

### **Step 2: Run UI Automation**

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration
import asyncio

integration = create_armoury_crate_integration()
result = asyncio.run(integration.process_request({
    'action': 'disable_all_lighting_ui'
}))

print(result['message'])  # ✅ ALL hardware lighting disabled via UI automation!
```

### **Step 3: Or Use Command Line**

```bash
python scripts/python/jarvis_disable_all_lighting.py
# Then select UI automation option
```

---

## 📋 Manual Setup (One-Time, Then Automation Works)

If UI automation doesn't work perfectly, do this **once**:

### **Step 1: Open Armoury Crate**
- Press Windows key, type "Armoury Crate", press Enter
- Or use: `python -c "from src.cfservices... import create_armoury_crate_integration; import asyncio; integration = create_armoury_crate_integration(); asyncio.run(integration.process_request({'action': 'open_app'}))"`

### **Step 2: Navigate to Lighting**
1. Click **"Device"** tab (left sidebar)
2. Select your laptop model
3. Click **"Lighting"** or **"Aura Sync"** section

### **Step 3: Turn OFF All Zones**
For **EACH** lighting zone (Keyboard, Logo, etc.):
- Set effect to **"Off"** OR
- Set effect to **"Static"** with brightness **0**
- Disable all effects

### **Step 4: Save Profile**
1. Click **"Save"** or **"Apply"**
2. Create a profile named **"sleep"** or **"all_off"**
3. Save it

### **Step 5: Automation Now Works!**
After this one-time setup, automation can apply the profile:
```python
await integration.process_request({
    'action': 'apply_profile',
    'profile_name': 'sleep'
})
```

---

## 🔧 How UI Automation Works

The UI automation:
1. **Opens Armoury Crate** automatically
2. **Finds the window** using pygetwindow
3. **Navigates to Lighting** section (keyboard navigation)
4. **Turns off all zones** (keyboard navigation)
5. **Saves settings** (Ctrl+S or button click)
6. **Also runs service disable** for complete control

### **Current Implementation**
- Uses **keyboard navigation** (Tab, Enter, Arrow keys)
- **Simplified approach** - works for most cases
- **Production version** would use image recognition for precise control

### **Future Enhancements**
- Image recognition for precise button clicking
- Screenshot analysis for zone detection
- More robust navigation logic
- Support for different Armoury Crate versions

---

## 🎯 Available Actions

| Action | Description | Automation Level |
|--------|-------------|------------------|
| `disable_all_lighting_ui` | **UI Automation** - Full hands-off | ✅ Full |
| `disable_all_lighting` | Service-based automation | ⚠️ Partial (needs profile) |
| `apply_profile` | Apply saved profile | ✅ Full (after setup) |

---

## ⚠️ Troubleshooting

### **UI Automation Not Working?**
1. **Install packages**: `pip install pyautogui pygetwindow Pillow`
2. **Check window**: Make sure Armoury Crate window is visible
3. **Try manual setup**: Do one-time setup, then use profile automation
4. **Check logs**: Look for error messages in automation output

### **Hardware Lights Still On?**
1. **Do manual setup once** (see above)
2. **Then automation will work** via profile application
3. **Or use UI automation** for full control

### **Services Restart?**
- Automation disables auto-start
- If they restart, lighting should stay off due to profile
- Check verification status in automation results

---

## 📝 Example: Complete Automation Script

```python
#!/usr/bin/env python3
"""Complete lighting automation with UI fallback"""

import asyncio
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration

async def main():
    integration = create_armoury_crate_integration()
    
    # Try UI automation first
    print("🤖 Attempting UI automation...")
    result = await integration.process_request({
        'action': 'disable_all_lighting_ui'
    })
    
    if result.get('success'):
        print("✅ UI automation successful!")
        return
    
    # Fallback to service-based + profile
    print("⚠️ UI automation failed, using service-based + profile...")
    result = await integration.process_request({
        'action': 'disable_all_lighting'
    })
    
    if result.get('success'):
        print("✅ Service-based automation successful!")
    else:
        print("⚠️ Automation partial. Manual setup may be needed.")
        print("See: docs/integrations/ARMOURY_CRATE_UI_AUTOMATION_SETUP.md")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🎉 Success!

**You now have BOTH:**
- ✅ **UI Automation** - Fully hands-off control
- ✅ **Manual Setup** - One-time, then automation works

Choose the approach that works best for you!
