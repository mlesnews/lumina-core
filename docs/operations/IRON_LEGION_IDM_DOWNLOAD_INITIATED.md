# Iron Legion Model Download via IDM - Initiated
                    -LUM THE MODERN

**Date**: 2026-01-17  
**Status**: ✅ Downloads Queued in IDM

---

## 📥 Downloads Initiated

### 1. Llama 3.2 11B (Mark II)
- **Node**: Mark II - General Purpose (Port 3002)
- **Source**: HuggingFace (`bartowski/Llama-3.2-11B-Vision-Instruct-GGUF`)
- **File**: `llama-3.2-11b-vision-instruct.Q4_K_M.gguf`
- **Destination**: `\\10.17.17.32\backups\MATT_Backups\models\ollama\`
- **Status**: ✅ Queued in IDM

### 2. Mixtral 8x7B (Mark VI)
- **Node**: Mark VI - Complex Expert (Port 3006)
- **Source**: HuggingFace (`TheBloke/Mixtral-8x7B-v0.1-GGUF`)
- **File**: `mixtral-8x7b-v0.1.Q4_K_M.gguf`
- **Destination**: `\\10.17.17.32\backups\MATT_Backups\models\ollama\`
- **Status**: ✅ Queued in IDM

---

## 📋 Next Steps

### 1. Monitor Downloads
- Open **Internet Download Manager (IDM)**
- Check download queue for both files
- Monitor progress until completion

### 2. Verify Downloads
After downloads complete, verify files exist:
```
\\10.17.17.32\backups\MATT_Backups\models\ollama\llama-3.2-11b-vision-instruct.Q4_K_M.gguf
\\10.17.17.32\backups\MATT_Backups\models\ollama\mixtral-8x7b-v0.1.Q4_K_M.gguf
```

### 3. Deploy to KAIJU
SSH to KAIJU (10.17.17.11) and pull models into Ollama:

```bash
# SSH to KAIJU
ssh 10.17.17.11

# Pull models (Ollama will use files from shared volume if available)
ollama pull llama3.2:11b
ollama pull mixtral:8x7b
```

**Note**: If the GGUF files are already on the NAS, you may need to:
- Copy them to the Ollama models directory on KAIJU
- Or configure Ollama to use the NAS path directly
- Or convert GGUF to Ollama format

### 4. Restart Containers
Restart the affected Iron Legion containers:

```bash
# On KAIJU
cd /path/to/lumina
docker-compose -f containerization/docker-compose.iron-legion.yml restart iron-man-mark-ii
docker-compose -f containerization/docker-compose.iron-legion.yml restart iron-man-mark-vi
```

### 5. Verify Model Assignment
Run the model assignment check:

```bash
python scripts/python/fix_iron_legion_model_assignments.py
```

Expected result:
- ✅ Mark II should show `llama3.2:11b`
- ✅ Mark VI should show `mixtral:8x7b`

---

## 🔧 Alternative: Direct Ollama Pull

If GGUF import doesn't work, you can pull models directly via Ollama (will download from Ollama CDN):

```bash
# On KAIJU, inside the container or on host
docker exec -it iron-man-mark-ii-codellama-13b ollama pull llama3.2:11b
docker exec -it iron-man-mark-vi-mixtral-8x7b ollama pull mixtral:8x7b
```

---

## 📊 Expected File Sizes

- **Llama 3.2 11B (Q4_K_M)**: ~6-7 GB
- **Mixtral 8x7B (Q4_K_M)**: ~26-30 GB

**Total**: ~33-37 GB

Ensure NAS has sufficient space before downloads start.

---

## ✅ Success Criteria

- [ ] Both files downloaded to NAS
- [ ] Files verified (size and integrity)
- [ ] Models pulled into Ollama on KAIJU
- [ ] Containers restarted
- [ ] Model assignment verified (Mark II = llama3.2:11b, Mark VI = mixtral:8x7b)
- [ ] Battle test Phase 1 passes with correct models

---

*Initiated: 2026-01-17*  
*@SCOTTY @PEAK @LUMINA @DT -LUM_THE_MODERN*
