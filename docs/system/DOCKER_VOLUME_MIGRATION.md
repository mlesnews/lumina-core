# Docker Volume Migration Guide

## Task 4: Migrate Docker Volumes — Currently Blocked

**Status:** ⚠️ BLOCKED - `data/docker` share doesn't exist yet

**Script:** `scripts/python/nas_migration_auto_docker.py`

**Target:** `\\10.17.17.32\data\docker`

---

## Current Status

- ✅ Script ready: `nas_migration_auto_docker.py`
- ❌ Share missing: `\\10.17.17.32\data` does not exist
- ❌ Docker share missing: `\\10.17.17.32\data\docker` does not exist

---

## Prerequisites

Before running the migration, you must create the `data` share on the NAS:

1. **Create `data` shared folder** on Synology NAS
2. **Create `docker` subfolder** within the data share
3. **Set permissions** for user `mlesn` (Read/Write)

---

## Step 1: Create Data Share on NAS

### Method 1: DSM Web Interface (Recommended)

1. Open browser: **https://10.17.17.32:5001**
2. Log in with NAS credentials
3. Navigate to: **Control Panel > Shared Folder**
4. Click **Create** button
5. Fill in:
   - **Name:** `data`
   - **Location:** `/volume1/data`
   - **Description:** Data storage for Docker, models, media, etc.
6. Set permissions:
   - User `mlesn`: **Read/Write**
7. Click **OK** to create

### Method 2: SSH Command (Alternative)

```bash
ssh mlesn@10.17.17.32
sudo mkdir -p /volume1/data/docker
sudo chown mlesn:users /volume1/data/docker
sudo chmod 755 /volume1/data/docker
```

Then create the `data` shared folder via DSM GUI (Method 1, steps 3-7).

---

## Step 2: Create Docker Subfolder

After the `data` share is created:

1. Open **File Station** in DSM
2. Navigate to `/volume1/data`
3. Create new folder: **`docker`**
4. Set permissions: Read/Write for user `mlesn`

Or via SSH:
```bash
ssh mlesn@10.17.17.32
mkdir -p /volume1/data/docker
chmod 755 /volume1/data/docker
```

---

## Step 3: Verify Share Exists

Run the check script:

```powershell
python scripts\python\create_docker_share_and_migrate.py --check-only
```

Expected output:
```
✅ Data share (\\10.17.17.32\data): EXISTS
✅ Docker share (\\10.17.17.32\data\docker): EXISTS
```

---

## Step 4: Run Migration

Once the share exists, run the migration:

```powershell
# Option 1: Use the helper script (recommended)
python scripts\python\create_docker_share_and_migrate.py --auto-stop

# Option 2: Run migration script directly
python scripts\python\nas_migration_auto_docker.py --auto-stop
```

### Migration Details

- **Source:** `C:\Users\mlesn\AppData\Local\Docker`
- **Target:** `\\10.17.17.32\data\docker`
- **Size:** ~82 GB (estimated)
- **Method:** Robocopy (multi-threaded, resume-capable)
- **Timeout:** 1 hour

### What `--auto-stop` Does

- Automatically stops Docker Desktop before migration
- Waits 5 seconds for Docker to fully stop
- Proceeds with migration
- **Note:** Docker Desktop must be stopped for migration to work

---

## Migration Process

1. **Check Docker Status**
   - If running and `--auto-stop` not set: Migration blocked
   - If running and `--auto-stop` set: Stops Docker Desktop

2. **Verify Shares**
   - Checks if `\\10.17.17.32\data\docker` exists
   - If missing: Returns BLOCKED status

3. **Calculate Size**
   - Scans source directory
   - Reports size and file count

4. **Migrate Files**
   - Uses `robocopy` with:
     - Multi-threaded (8 threads)
     - Retry on failure (3 retries, 5s wait)
     - Resume capability
     - Log file: `data/nas_migration/docker_migration.log`

5. **Save Results**
   - JSON result file: `data/nas_migration/docker_migration_YYYYMMDD_HHMMSS.json`

---

## Troubleshooting

### Share Not Found

**Error:** `Target share does not exist: \\10.17.17.32\data\docker`

**Solution:**
1. Verify share exists: `Test-Path "\\10.17.17.32\data\docker"`
2. Check NAS connectivity: `ping 10.17.17.32`
3. Verify permissions: Ensure user `mlesn` has Read/Write access
4. Create share using instructions above

### Docker Desktop Running

**Error:** `Docker Desktop is running - must stop first`

**Solution:**
- Run with `--auto-stop` flag: `python nas_migration_auto_docker.py --auto-stop`
- Or manually stop Docker Desktop before running migration

### Migration Timeout

**Error:** `Migration timed out (1 hour)`

**Solution:**
- Migration may take longer than 1 hour for 82GB
- Check log file: `data/nas_migration/docker_migration.log`
- Robocopy can resume - run again to continue

### Permission Denied

**Error:** `Access denied` or `Permission denied`

**Solution:**
1. Verify NAS user `mlesn` has Read/Write permissions on `data/docker` share
2. Check Windows credentials for `\\10.17.17.32`
3. Try mapping drive first: `net use Z: \\10.17.17.32\data\docker`

---

## Post-Migration

After successful migration:

1. **Verify Files**
   - Check target: `\\10.17.17.32\data\docker`
   - Compare file counts and sizes

2. **Update Docker Configuration**
   - Configure Docker Desktop to use NAS location (if needed)
   - Or keep local and use NAS as backup

3. **Clean Up** (Optional)
   - Remove local Docker volumes after verification
   - Keep backup for safety

---

## Related Scripts

- `create_docker_share_and_migrate.py` - One-step share creation and migration
- `nas_migration_auto_docker.py` - Core migration script
- `nas_migration_phase1_create_shares.py` - Share creation instructions generator
- `nas_migration_auto_create_shares.py` - Automated share creation (SSH/DSM API)

---

## Next Steps

1. ✅ Create `data` share on NAS (via DSM GUI)
2. ✅ Create `docker` subfolder
3. ✅ Verify share exists
4. ✅ Run migration with `--auto-stop`
5. ✅ Verify migration completed successfully

---

**Last Updated:** 2026-01-14  
**Status:** Blocked - Waiting for share creation
