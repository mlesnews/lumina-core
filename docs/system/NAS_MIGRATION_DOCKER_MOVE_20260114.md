# NAS Migration - Docker Data Move

**Date**: 2026-01-14  
**Action**: Moving Docker data (133.8 GB) to NAS  
**Status**: 🔄 **IN PROGRESS**  
**Tags**: `#DOIT` `#NAS` `#DOCKER` `#MIGRATION` `@LUMINA` `@JARVIS` `#PEAK`

---

## 🎯 Action

Moving Docker data from `C:\Users\mlesn\AppData\Local\Docker` (133.8 GB) to NAS to free disk space.

---

## 📊 Docker Data Location

- **Source**: `C:\Users\mlesn\AppData\Local\Docker`
- **Size**: 133.8 GB
- **Target**: `\\10.17.17.32\homes\mlesn\docker`
- **Method**: robocopy with /MOVE

---

## ✅ Execution

Using robocopy to move Docker data to NAS:
- `/E` - Copy subdirectories including empty ones
- `/MOVE` - Move files (delete from source after copy)
- `/R:3` - Retry 3 times on errors
- `/W:5` - Wait 5 seconds between retries

---

## 📝 Notes

- Docker data is large (133.8 GB) - significant space savings
- Moving to NAS will free local disk space
- Docker Desktop will need to be configured to use NAS path after move
- May need to restart Docker Desktop after move

---

**Status**: 🔄 **MOVING DOCKER DATA TO NAS**  
**Tags**: `#DOIT` `#NAS` `#DOCKER` `#MIGRATION` `@LUMINA` `@JARVIS` `#PEAK`
