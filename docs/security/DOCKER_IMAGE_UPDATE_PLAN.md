# Docker Image Update Plan - Migrate to Hardened Images

**Date:** January 10, 2025  
**Status:** 📋 Evaluation Complete | 🔄 Update Pending

---

## Executive Summary

**Current State:**
- ✅ Hardened Kali image created: `kali-hardened-millennium-falc:latest`
- ⚠️ 2 other Kali Dockerfiles need updating to use hardened version
- ⚠️ 12 Dockerfiles need security hardening
- 📊 15 Dockerfiles total, 17 docker-compose files

**Goal:**
Migrate all Linux/Kali-based images to use hardened versions for maximum security.

---

## Evaluation Results

### Dockerfiles Found: 15

**Kali-based (3):**
1. ✅ `docker/kali-hardened/Dockerfile` - Already hardened
2. ⚠️ `containerization/services/kaju-remote-admin/Dockerfile.kali` - Needs update
3. ⚠️ `containerization/services/kaju_remote_admin/Dockerfile.kali` - Needs update

**Other Linux-based (12):**
- Various Dockerfiles using Ubuntu, Debian, Alpine, etc.
- All need security hardening evaluation

### Docker Compose Files: 17
- Need review for Kali image references
- Update to use hardened image where applicable

### Running Images: 13
- `kali-hardened-millennium-falc:latest` ✅ (hardened)
- `kali-hardened-millennium-falc:fixed-20260110` ✅ (hardened)
- Others need evaluation

---

## Update Plan

### Phase 1: Update Kali Dockerfiles (HIGH PRIORITY)

**Files to Update:**
1. `containerization/services/kaju-remote-admin/Dockerfile.kali`
2. `containerization/services/kaju_remote_admin/Dockerfile.kali`

**Action:**
Replace `FROM kalilinux/kali-rolling:latest` with `FROM kali-hardened-millennium-falc:latest`

### Phase 2: Update Docker Compose Files

**Action:**
Review all 17 docker-compose files and update Kali image references to hardened version.

### Phase 3: Evaluate Other Linux Images

**Action:**
- Review all non-Kali Linux images
- Apply security hardening where appropriate
- Consider creating hardened base images for other distributions

---

## Automated Update System

### Evaluation System
```bash
# Evaluate all Docker images
python scripts/python/evaluate_all_docker_images.py --evaluate
```

### Update System
```bash
# Dry run (see what would be updated)
python scripts/python/update_all_docker_images_to_hardened.py --dry-run

# Actual update
python scripts/python/update_all_docker_images_to_hardened.py --update
```

---

## Current Status

### ✅ Completed
- Hardened Kali image created and tested
- Comprehensive evaluation system created
- Update automation system created

### 🔄 Pending
- Update 2 Kali Dockerfiles to use hardened version
- Review and update docker-compose files
- Evaluate other Linux images for hardening

---

## Recommendations

### Immediate Actions
1. **Update Kali Dockerfiles** - Replace with hardened version
2. **Review docker-compose files** - Update image references
3. **Rebuild affected images** - Test after updates

### Long-term Actions
1. **Create hardened base images** for other Linux distributions
2. **Set up automated scanning** for all images
3. **Implement CI/CD checks** to prevent unhardened images

---

## Files Created

1. **Evaluation System:** `scripts/python/evaluate_all_docker_images.py`
2. **Update System:** `scripts/python/update_all_docker_images_to_hardened.py`
3. **Evaluation Reports:** `data/docker_image_evaluation/`
4. **Update Reports:** `data/docker_image_updates/`

---

## Next Steps

1. Run evaluation to see current state
2. Review high-priority recommendations
3. Execute updates (dry-run first, then live)
4. Rebuild and test updated images
5. Verify security improvements

---

**Last Updated:** January 10, 2025  
**Status:** 📋 Ready for Updates  
**Priority:** HIGH - Update Kali Dockerfiles immediately
