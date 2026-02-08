# 🔐 Software Repository Vault System

**Catalog and secure all your software, licenses, and related information. Not dependent on Dropbox.**

---

## 🎯 The Problem

You have a **Repository** folder with all your software and licenses, but:
- It's in Dropbox (not ideal for security)
- No centralized catalog
- No vaulting to secure locations (NAS, Azure, etc.)
- Hard to find what you have

---

## ✅ Solution: Software Repository Vault

A system to:
1. **Catalog** all your software and licenses
2. **Vault** to secure locations (NAS, Azure, local encrypted)
3. **Search** your software catalog
4. **Track** licenses, versions, purchase dates
5. **Not dependent on Dropbox** - can vault anywhere

---

## 🚀 Quick Start

### Scan Your Repository

```bash
python scripts/python/software_repository_vault.py --scan "C:\Users\mlesn\Dropbox\Repository"
```

This will:
- Find all software files
- Detect software types (VB-Audio, Voicemeeter, etc.)
- Catalog installers, licenses, archives

### Add Software Manually

```bash
python scripts/python/software_repository_vault.py --add "VB-Audio Virtual Cable"
```

### Search Your Catalog

```bash
python scripts/python/software_repository_vault.py --search "VB-Audio"
```

### Vault Software

```bash
python scripts/python/software_repository_vault.py --vault <software_id>
```

Vaults to:
- **Local**: `data/software_vault/vault/`
- **NAS**: `\\10.17.17.32\backups\MATT_Backups\software_vault\`
- **Azure**: (Coming soon)

---

## 📋 Features

### Software Catalog

Tracks:
- Name, version, vendor
- License type (Commercial, Open Source, Freeware)
- License keys (encrypted)
- Purchase/expiration dates
- Installation paths
- Related files (installers, licenses, docs)
- Vault location

### Vault Backends

1. **Local Vault** - Encrypted local storage
2. **NAS Vault** - Your NAS at `10.17.17.32`
3. **Azure Vault** - Azure Blob Storage (coming soon)

### Repository Scanning

Automatically detects:
- Installers (.exe, .msi, .dmg, .pkg)
- Archives (.zip, .rar, .7z)
- License files
- Documentation

---

## 🔍 How I Knew About VB-Audio

**Answer**: VB-Audio is a well-known tool for system audio capture on Windows. I suggested it because:
- It's commonly used for routing system audio
- It's free and reliable
- It solves the "capture what's playing" problem

**Not from your archive** - just common knowledge for audio routing on Windows.

But now we can:
1. **Check if you have it** in your repository
2. **Catalog it** if you do
3. **Vault it** for secure storage

---

## 🎯 Usage Examples

### Example 1: Scan and Catalog Everything

```bash
# Scan repository
python scripts/python/software_repository_vault.py --scan "C:\Users\mlesn\Dropbox\Repository"

# This finds all software, then you can add them to catalog
```

### Example 2: Add VB-Audio to Catalog

```bash
python scripts/python/software_repository_vault.py --add "VB-Audio Virtual Cable" --version "1.0" --license-type "Freeware"
```

### Example 3: Vault to NAS

```bash
# First, register NAS repository
# Then vault software
python scripts/python/software_repository_vault.py --vault <software_id>
```

### Example 4: Search for Software

```bash
python scripts/python/software_repository_vault.py --search "audio"
```

---

## 🔐 Security Features

### Not Dependent on Dropbox

- Can vault to NAS (your control)
- Can vault to Azure (cloud backup)
- Can vault locally (encrypted)

### License Key Protection

- License keys stored securely
- Can encrypt sensitive data
- Vaulted separately from catalog

### Multiple Backends

- Don't rely on one storage location
- Redundancy across backends
- Easy to migrate

---

## 📊 Catalog Summary

View your catalog:

```bash
python scripts/python/software_repository_vault.py --summary
```

Shows:
- Total software count
- By license type
- Vaulted vs. not vaulted
- Repository count

---

## 🎯 Next Steps

1. **Scan your repository** - Find all software
2. **Catalog important software** - Add licenses, keys, etc.
3. **Vault to NAS** - Secure storage on your NAS
4. **Search when needed** - Find software quickly
5. **Keep catalog updated** - Add new software as you get it

---

## 💡 Best Practices

1. **Scan regularly** - Keep catalog up to date
2. **Vault important licenses** - Don't lose license keys
3. **Use NAS for backup** - Not just Dropbox
4. **Document installation paths** - Know where things are installed
5. **Track expiration dates** - Don't let licenses expire

---

**Last Updated**: 2025-12-28  
**Status**: ✅ Vault System Ready | 🔍 Repository Scanning Available

