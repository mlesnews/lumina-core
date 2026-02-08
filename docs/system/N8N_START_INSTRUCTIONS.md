# N8N Start Instructions - Permission Issue

**Status**: ⚠️ **DOCKER PERMISSION DENIED**

---

## Issue

N8N container creation failed due to Docker permission denied. The SSH user (`mlesn`) is not in the `docker` group and cannot access Docker socket directly.

---

## Solutions

### Option 1: Use Synology Container Manager (Recommended)

1. **Access DSM**: Open `https://10.17.17.32:5001` in browser
2. **Open Container Manager**: Package Center → Container Manager
3. **Create Container**:
   - Click "Container" → "Create"
   - Search for `n8nio/n8n`
   - Click "Select"
   - Configure:
     - **Container Name**: `n8n`
     - **Port Settings**: 
       - Container Port: `5678`
       - Host Port: `5678`
     - **Volume Settings**:
       - Mount Path: `/volume1/docker/n8n`
       - Container Path: `/home/node/.n8n`
     - **Environment Variables**:
       - `N8N_BASIC_AUTH_ACTIVE=true`
       - `N8N_BASIC_AUTH_USER=mlesn`
       - `N8N_BASIC_AUTH_PASSWORD=<from Azure Vault: n8n-password>`
       - `N8N_HOST=10.17.17.32`
       - `N8N_PORT=5678`
       - `N8N_PROTOCOL=http`
   - Click "Next" → "Done"
4. **Start Container**: Click "Start" on the n8n container

### Option 2: Add User to Docker Group (SSH)

```bash
# SSH to NAS as admin/root
ssh admin@10.17.17.32

# Add user to docker group
sudo synogroup --add docker mlesn
# OR
sudo usermod -aG docker mlesn

# Logout and login again for group to take effect
```

Then retry: `python scripts/python/start_n8n_nas.py`

### Option 3: Use Sudo with Password

If sudo is configured, the script can be modified to use sudo with password from Azure Vault.

---

## After N8N is Running

Once N8N is accessible at `http://10.17.17.32:5678`:

```bash
python scripts/python/deploy_n8n_with_vault_creds.py
```

This will deploy all 3 SYPHON workflows automatically.

---

**Current Blocker**: Docker permission denied - requires Container Manager GUI or adding user to docker group.
