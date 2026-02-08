# What's All This Vault Stuff?

**Question**: "What's all this? The vault, man."

---

## The Answer

The **Azure Key Vault** messages you're seeing are from **ecosystem integrations** that Kenny loads, not from Kenny herself.

### What's Happening

When Kenny starts, she tries to load:
1. **JARVIS Integration** → Needs NAS credentials → Uses Azure Key Vault
2. **NAS Integration** → Needs credentials → Uses Azure Key Vault  
3. **Adaptive Collaboration** → May trigger vault access

### The Vault Messages

Those authentication messages are from:
- Azure Key Vault trying to authenticate
- NAS credentials being retrieved
- JARVIS ecosystem initialization

**Kenny doesn't need the vault** - it's just the ecosystem trying to connect.

---

## Solution: Skip Heavy Integrations

I've updated Kenny to **skip heavy integrations by default**:

```bash
# Lightweight mode (no vault noise)
python scripts/python/kenny_imva_enhanced.py

# Full integration mode (if you need JARVIS/NAS)
python scripts/python/kenny_imva_enhanced.py --full-integration
```

---

## What Kenny Actually Needs

**Kenny only needs**:
- ✅ tkinter (for window)
- ✅ PIL/Pillow (for rendering)
- ✅ Ace integration (lightweight, no vault)

**Kenny doesn't need**:
- ❌ JARVIS (unless you want full ecosystem)
- ❌ NAS integration (unless you need it)
- ❌ Azure Key Vault (unless ecosystem is enabled)

---

## The Fix

**Default behavior**: Skip ecosystem integrations → No vault noise  
**Optional**: Use `--full-integration` if you need JARVIS/NAS features

---

**Tags**: #KENNY #VAULT #AZURE #EXPLANATION @JARVIS @LUMINA
