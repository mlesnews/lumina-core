# Finding Armoury Crate and Handling App Linking

## ✅ Found Your Installation

**Armoury Crate is installed at:**
```
C:\Users\mlesn\AppData\Local\Microsoft\WindowsApps\ArmouryCrate.exe
```

You can access it directly from this path, or search for "Armoury Crate" in the Start menu.

---

## 🔗 About the App Linking Popup

When you open Armoury Crate, you may see a popup asking to **link the app with your Microsoft account**. Here's what you need to know:

### **The Popup is OPTIONAL**

- **You can safely click "Skip", "Cancel", or "Not Now"**
- Armoury Crate will work perfectly fine without linking
- All features (lighting, performance, etc.) work without Microsoft account linking

### **What Linking Does (Optional)**

If you choose to link:
- ✅ Syncs your settings across devices (if you have multiple ASUS devices)
- ✅ Enables cloud backup of profiles
- ✅ Allows remote access to settings (if supported)

**If you don't link:**
- ✅ All features still work
- ✅ Settings are saved locally on your laptop
- ✅ No cloud sync (which some users prefer for privacy)

### **How to Handle the Popup**

1. **To Skip Linking:**
   - Click "Skip", "Cancel", "Not Now", or "Maybe Later"
   - The app will open normally
   - You can always link later in Settings if you change your mind

2. **To Link (Optional):**
   - Click "Link", "Sign In", or "Connect"
   - Sign in with your Microsoft account
   - Follow the prompts to complete linking

3. **To Link Later:**
   - Open Armoury Crate
   - Go to Settings (usually gear icon)
   - Look for "Account" or "Microsoft Account" option
   - Click to link your account

---

## 📥 Finding Armoury Crate in Microsoft Store

If you're having trouble finding it in the Microsoft Store:

### **Method 1: Direct Store Link**
Open this URL in your browser:
```
ms-windows-store://pdp/?ProductId=9NBLGGH4Z1SP
```

Or search for: **"Armoury Crate"** in the Microsoft Store app.

### **Method 2: Direct Download from ASUS**
If the Store doesn't work:

1. Go to: **https://www.asus.com/support/download-center/**
2. Enter your laptop model number
3. Navigate to **Utilities** section
4. Download **"Armoury Crate"**
5. Run the installer
6. Restart if prompted

### **Method 3: Check if Already Installed**
Since we found it at:
```
C:\Users\mlesn\AppData\Local\Microsoft\WindowsApps\ArmouryCrate.exe
```

You can:
- Press **Windows Key** and type "Armoury Crate"
- Or open it directly from the path above
- Or use our Lumina integration to open it

---

## 🎮 Using Lumina to Open Armoury Crate

You can use the Lumina integration to open Armoury Crate:

```python
from src.cfservices.services.jarvis_core.integrations.armoury_crate import create_armoury_crate_integration
import asyncio

integration = create_armoury_crate_integration()
result = asyncio.run(integration.process_request({
    'action': 'open_app'
}))
```

Or use the CLI:
```bash
python scripts/python/lumina_armoury_crate_control.py
```

Then select option **1** to open Armoury Crate.

---

## ❓ Troubleshooting

### **Can't Find in Microsoft Store**
- The Store search can be finicky
- Try the direct link above
- Or download directly from ASUS website

### **App Linking Popup Keeps Appearing**
- You can dismiss it each time
- Or link your account once to stop the prompts
- Check Settings → Account to manage linking

### **Armoury Crate Won't Open**
1. Check if it's running: Task Manager → Look for "ArmouryCrate.exe"
2. Restart the service: Use Lumina integration `stop_lighting_service` then try again
3. Reinstall from ASUS website if needed

---

## 📝 Summary

- ✅ **Armoury Crate is installed** at the WindowsApps location
- ✅ **App linking is OPTIONAL** - you can skip it
- ✅ **All features work** without linking
- ✅ **You can link later** in Settings if desired
- ✅ **Use Lumina integration** to control it programmatically

The popup is just asking if you want cloud sync - it's completely optional!
