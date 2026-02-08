# Install Tesseract OCR for Windows

**Date:** 2026-01-09
**Purpose:** Enable OCR text extraction in visual monitoring system

---

## 📥 INSTALLATION

### Option 1: Download Installer (Recommended)
1. Download Tesseract OCR installer for Windows:
   - https://github.com/UB-Mannheim/tesseract/wiki
   - Or: https://digi.bib.uni-mannheim.de/tesseract/

2. Run the installer
3. Default installation path: `C:\Program Files\Tesseract-OCR\`

### Option 2: Using Chocolatey
```powershell
choco install tesseract
```

### Option 3: Using Scoop
```powershell
scoop install tesseract
```

---

## ✅ VERIFICATION

After installation, verify it works:

```python
import pytesseract
from PIL import Image

# Test OCR
img = Image.open("test_image.png")
text = pytesseract.image_to_string(img)
print(text)
```

---

## 🔧 CONFIGURATION

If Tesseract is installed in a non-standard location, set the path:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Path\To\Tesseract-OCR\tesseract.exe"
```

The visual monitoring system will automatically try common installation paths.

---

## 📋 STATUS

- **Python library (pytesseract):** ✅ Installed
- **Tesseract OCR engine:** ⚠️ Needs installation
- **Computer Vision:** ✅ Working
- **Intent Detection:** ✅ Working (CV-based, OCR pending)

---

**Tags:** #TESSERACT #OCR #INSTALLATION #WINDOWS @JARVIS @LUMINA
