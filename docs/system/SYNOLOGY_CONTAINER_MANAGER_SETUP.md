# Synology Container Manager Setup Guide

**Date**: 2026-01-09
**Protocol**: @DOIT @BAU @TRIAGE @END2END @REPORT @JARVIS
**Status**: ✅ **SETUP GUIDE CREATED**

## Synology Container Manager

Synology uses **Container Manager** (formerly Docker) package. Docker commands may not be in standard PATH.

### Finding Docker on Synology

1. **Package Location**: `/var/packages/ContainerManager/`
2. **Docker Binary**: Usually in `/var/packages/ContainerManager/target/usr/bin/docker`
3. **Service**: `pkg-ContainerManager-dockerd.service`
4. **Socket**: `/var/run/docker.sock` (if accessible)

### Access Methods

#### Method 1: Via Container Manager GUI
- Open DSM (DiskStation Manager)
- Go to **Package Center**
- Open **Container Manager**
- Use GUI to create containers

#### Method 2: Via SSH with Full Path
```bash
# Set PATH
export PATH=/var/packages/ContainerManager/target/usr/bin:$PATH

# Use docker
docker --version
docker ps
```

#### Method 3: Via Docker Socket (if accessible)
```bash
# Check socket
ls -la /var/run/docker.sock

# Use docker client from another machine
docker -H ssh://user@10.17.17.32 ps
```

### Recommended Approach

**Use Container Manager GUI** for initial setup, then access via:
1. SSH with full path to docker binary
2. Or configure PATH in SSH session
3. Or use docker-compose if available

### Next Steps

1. ✅ Container Manager is installed (confirmed)
2. ⏳ Find docker binary path
3. ⏳ Set up router directory on NAS
4. ⏳ Deploy router container
5. ⏳ Configure networking

---

**Last Updated**: 2026-01-09
**Status**: ✅ **GUIDE CREATED - FINDING DOCKER PATH**
