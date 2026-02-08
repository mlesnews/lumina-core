# Iron Legion Mark 1 - Container Naming Convention

**Date**: 2025-01-27  
**Status**: ✅ **IMPLEMENTED**  
**Theme**: Iron Man / Tony Stark Mark Versioning

---

## Container Naming Convention

### Pattern
- **Container Names**: `iron-man-mk{N}-{model-name}`
- **Image Names**: Actual GGUF model names (e.g., `codellama:13b`, `llama3.2:11b`)
- **Port**: 3000 (I Love You 3000!)

### Mark Versions

| Mark | Model | Container Name | Image Name | Port | Role |
|------|-------|----------------|------------|------|------|
| MK1 | Codellama 13B | `iron-man-mk1-codellama-13b` | `codellama:13b` | 3001 | Primary Code Generation |
| MK2 | Llama 3.2 11B | `iron-man-mk2-llama3-2-11b` | `llama3.2:11b` | 3002 | Secondary General |
| MK3 | Qwen 2.5 Coder 1.5B | `iron-man-mk3-qwen2-5-coder-1-5b` | `qwen2.5-coder:1.5b-base` | 3003 | Lightweight Quick |
| MK4 | Llama 3 | `iron-man-mk4-llama3` | `llama3` | 3004 | General Purpose |
| MK5 | Mistral | `iron-man-mk5-mistral` | `mistral` | 3005 | General Reasoning |
| MK6 | Mixtral 8x7B | `iron-man-mk6-mixtral-8x7b` | `mixtral-8x7b` | 3006 | High Complexity |
| MK7 | Gemma 2B | `iron-man-mk7-gemma-2b` | `gemma-2b` | 3007 | Lightweight Fallback |

### Load Balancer

- **Container Name**: `jarvis-loadbalancer`
- **Image**: `nginx:alpine`
- **Port**: 3000 (I Love You 3000!)
- **Config**: `.lumina/config/nginx/iron-legion-lb.conf`

---

## Docker Compose File

**Location**: `.lumina/containerization/docker-compose.iron-legion-mk1.yml`

### Key Features

1. **Mark Versioning**: Each container named with Iron Man Mark version
2. **Model Images**: Image names use actual GGUF model names
3. **Labels**: Docker labels for identification:
   - `iron.legion.mark={N}`
   - `iron.legion.model={model-name}`
   - `iron.legion.role={role}`

### Example Container Definition

```yaml
iron-man-mk1-codellama-13b:
  image: codellama:13b
  container_name: iron-man-mk1-codellama-13b
  ports:
    - "3001:11434"
  labels:
    - "iron.legion.mark=1"
    - "iron.legion.model=codellama:13b"
    - "iron.legion.role=primary_code_generation"
```

---

## Load Balancer Configuration

**Location**: `.lumina/config/nginx/iron-legion-lb.conf`

### Upstream Servers

All 7 Iron Man Mark containers are included in the load balancer:

```nginx
upstream iron_legion {
    least_conn;
    server iron-man-mk1-codellama-13b:11434;
    server iron-man-mk2-llama3-2-11b:11434;
    server iron-man-mk3-qwen2-5-coder-1-5b:11434;
    server iron-man-mk4-llama3:11434;
    server iron-man-mk5-mistral:11434;
    server iron-man-mk6-mixtral-8x7b:11434;
    server iron-man-mk7-gemma-2b:11434;
}
```

---

## Usage

### Start Iron Legion Cluster

```bash
cd .lumina/containerization
docker-compose -f docker-compose.iron-legion-mk1.yml up -d
```

### Check Container Status

```bash
docker ps --filter "name=iron-man-mk"
```

### View Container Labels

```bash
docker inspect iron-man-mk1-codellama-13b | grep -A 5 Labels
```

### Access Load Balancer

```bash
curl http://localhost:3000/api/tags
```

---

## Migration from Old Naming

### Old Container Names
- `lumina-ollama-primary`
- `lumina-ollama-secondary`
- `lumina-ollama-tertiary`

### New Container Names
- `iron-man-mk1-codellama-13b`
- `iron-man-mk2-llama3-2-11b`
- `iron-man-mk3-qwen2-5-coder-1-5b`
- `iron-man-mk4-llama3`
- `iron-man-mk5-mistral`
- `iron-man-mk6-mixtral-8x7b`
- `iron-man-mk7-gemma-2b`

### Migration Steps

1. Stop old containers:
   ```bash
   docker-compose -f docker-compose.ollama-cluster.yml down
   ```

2. Start new Iron Legion cluster:
   ```bash
   docker-compose -f docker-compose.iron-legion-mk1.yml up -d
   ```

3. Verify all containers running:
   ```bash
   docker ps --filter "name=iron-man-mk"
   ```

---

## Benefits

1. **Clear Versioning**: Mark numbers indicate model hierarchy
2. **Model Identification**: Container names include model names
3. **Thematic Consistency**: Iron Man theme aligns with "I Love You 3000!" port
4. **Scalability**: Easy to add new Mark versions
5. **Docker Labels**: Programmatic identification via labels

---

**Last Updated**: 2025-01-27  
**Status**: ✅ Implemented  
**Next Steps**: Load models into Iron Man containers

