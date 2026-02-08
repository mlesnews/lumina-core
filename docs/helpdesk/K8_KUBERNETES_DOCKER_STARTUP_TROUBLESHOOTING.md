# K8 / Kubernetes Startup in Docker – Troubleshooting

**Context:** LUMINA Collective uses K8s (K3s-based). Kubernetes can fail to start in two main ways in this setup:

1. **Docker Desktop Kubernetes** (Windows/Mac) – built-in “Enable Kubernetes” single-node cluster.
2. **K3s agent in Docker** (e.g. CUBE GAMMA on NAS) – `rancher/k3s` container run by `install-k3s-nas.sh`.

This doc captures common causes and fixes. **For RCA, always record the exact error message and where it appears.**

---

## 1. Docker Desktop Kubernetes (Windows) – “Starting…” or failed

**Symptom:** Kubernetes in Docker Desktop stays on “Starting…” or shows an error; `kubectl` fails or context is unavailable.

### Stuck on "Waiting for node to start" (no error)

Try in order:

1. **Reset Kubernetes in Docker Desktop**
   - Docker Desktop → **Settings** (gear) → **Kubernetes**.
   - Leave **Enable Kubernetes** checked.
   - Click **Reset Kubernetes cluster** → confirm.
   - Wait 5–10 minutes; the node can take a long time to show "Running".

2. **Give Docker more resources**
   - Settings → **Resources** → set **Memory** to at least **4 GB** (6–8 GB if possible).
   - **CPUs** at least 2–4.
   - Click **Apply & Restart**.

3. **Full disable then re-enable** (if reset didn't help)
   - Settings → Kubernetes → **Uncheck** "Enable Kubernetes" → **Apply**.
   - Wait until it shows "Kubernetes is disabled".
   - Restart Docker Desktop from the tray (Quit, then start again).
   - Settings → Kubernetes → **Check** "Enable Kubernetes" → **Apply**.
   - Wait again; first start can take 5–15 minutes.

4. **If still stuck:** Close other heavy apps (IDEs, browsers, WSL distros), then repeat step 3. On some machines the internal node never becomes ready due to resource contention.

### Common causes and fixes

| Cause | What to try |
|-------|-------------|
| **WSL 2 / Hyper-V / resources** | Ensure WSL 2 is default, Docker Desktop has enough CPU/RAM (e.g. 4+ GB), and no other heavy VM is starving it. |
| **Stale Kubernetes state** | Docker Desktop → Settings → Kubernetes → **Reset Kubernetes cluster** (or disable Kubernetes, apply, re-enable, apply). |
| **Corrupted kubeconfig** | Backup then remove or rename `%USERPROFILE%\.kube\config`; restart Docker Desktop and re-enable Kubernetes so it recreates config. |
| **Port conflict** | Nothing else should use typical K8s ports (e.g. 6443). Check `netstat` / Resource Monitor for conflicts. |
| **Docker Desktop version** | Update to latest stable; known issues are often fixed in newer versions. |
| **Antivirus / firewall** | Temporarily allow Docker Desktop / WSL and retry; exclude Docker data directories if needed. |

### Cluster started but shows "no pods, no deployment"

That's normal. A fresh Docker Desktop Kubernetes cluster has no workloads. You should see one node (e.g. `docker-desktop`) in **Ready** and no pods/deployments until you deploy something.

**Verify cluster is healthy:**

```powershell
kubectl get nodes
kubectl get pods -A
kubectl get deployments -A
```

You should see one node (Ready) and empty pod/deployment lists.

**Optionally deploy the LUMINA namespace and a sample workload:** From the repo root (PowerShell):

```powershell
cd containerization\k8s\scripts
.\k8s-manager.ps1 deploy all
.\k8s-manager.ps1 status
```

Or manually: create the `lumina` namespace and deploy from `containerization/k8s/manifests/` (see `k8s-manager.ps1 setup` for architecture).

### Quick checks

```powershell
# Is Docker running?
docker info

# After Kubernetes is “running” in Docker Desktop:
kubectl config current-context
kubectl get nodes
kubectl cluster-info
```

### If you need to reset (Windows)

1. Docker Desktop → Settings → Kubernetes → **Uncheck** “Enable Kubernetes” → Apply.
2. Wait until it shows “Kubernetes is disabled”.
3. Optionally: Settings → Resources → set CPU/Memory higher → Apply.
4. Enable Kubernetes again → Apply and wait (can take several minutes).

---

## 2. K3s agent in Docker (e.g. CUBE GAMMA on NAS)

**Symptom:** `k3s-agent` container exits, restarts repeatedly, or never joins the cluster. Script: `containerization/k8s/setup/install-k3s-nas.sh`.

### Common causes and fixes

| Cause | What to try |
|-------|-------------|
| **Control plane unreachable** | From NAS, ensure CUBE ALPHA (10.17.17.11) is reachable: `ping 10.17.17.11` and `curl -k https://10.17.17.11:6443` (or telnet 6443). Fix network/firewall if not. |
| **Wrong or expired token** | Get a fresh token from CUBE ALPHA: `ssh user@10.17.17.11 'sudo cat /var/lib/rancher/k3s/server/node-token'`. Set `K3S_TOKEN` and re-run `install-k3s-nas.sh`. |
| **Missing / wrong K3S_URL** | Must be `https://10.17.17.11:6443` (per `config/host_identity_registry.json`). No trailing slash. |
| **Docker / host networking** | Script uses `--network host`. On Synology, ensure Docker has permission to use host network if required; otherwise document any NAS-specific limits. |
| **Image / version** | Pin to a specific tag if `rancher/k3s:latest` is problematic, e.g. `rancher/k3s:v1.28.x` to match server. |
| **Resource limits** | Ensure NAS has enough RAM/CPU for the agent; check `docker stats k3s-agent`. |

### Quick checks (on NAS or host running the container)

```bash
# Container status and restarts
docker ps -a --filter name=k3s-agent
docker inspect k3s-agent --format '{{.State.Status}} {{.RestartCount}}'

# Agent logs (most useful for RCA)
docker logs k3s-agent
docker logs k3s-agent --tail 100

# From CUBE ALPHA: is the node visible?
kubectl get nodes
kubectl get nodes -o wide
```

### Helper script (created by install-k3s-nas.sh)

On the NAS, `$K3S_DATA_DIR/k3s-helper.sh` (e.g. `/volume1/docker/k3s/k3s-helper.sh`):

```bash
./k3s-helper.sh status   # container status
./k3s-helper.sh logs     # follow logs
./k3s-helper.sh restart  # restart container
```

---

## 3. What to capture for RCA

When opening a ticket or investigation brief, include:

1. **Which scenario:** Docker Desktop Kubernetes **or** K3s agent in Docker (and which host).
2. **Exact error message:** Full text from UI, terminal, or logs (e.g. `docker logs k3s-agent`).
3. **When it started:** After upgrade, reboot, or first-time setup.
4. **Checks already run:** e.g. `docker info`, `kubectl get nodes`, `docker logs k3s-agent`.

---

## 4. References

- **Cluster design:** `containerization/k8s/CLUSTER_ARCHITECTURE.md`
- **K8s manager (Windows):** `containerization/k8s/scripts/k8s-manager.ps1` (`status`, `nodes`, `pods`, `setup`)
- **Host identity:** `config/host_identity_registry.json` (Kaiju = 10.17.17.11, NAS = 10.17.17.32)
- **Shortag / @K8S:** `config/shortag_registry.json` (@K8S, @KUBERNETES)

---

**Tags:** `@K8S` `#TROUBLESHOOTING` `#DOCKER` `#KUBERNETES` `#K3S`
