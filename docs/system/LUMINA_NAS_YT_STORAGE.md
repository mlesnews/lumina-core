# LUMINA NAS YouTube Storage System

**Status**: 🟢 INITIALIZED  
**NAS IP**: 10.17.17.32  
**Share**: LUMINA-YT  
**Mount Point**: Y: (Windows)

---

## 🎯 Mission

**"USE NAS NETWORK STORAGE FOR AND MAP OUT THE DRIVE FOR LUMINA-YT"**

Map NAS network storage and configure storage paths for all LUMINA YouTube content, 
including trailers, episodes, raw footage, edited content, and assets.

---

## 💾 Storage Structure

### Base Path

```
NAS Share: LUMINA-YT
Mount Point: Y: (Windows)
Base Path: /volume1/LUMINA-YT (on NAS)
```

### Storage Types

1. **Trailers** (`Y:\trailers\`)
   - All 7 pilot episode trailers
   - Generated video files
   - Thumbnails

2. **Episodes** (`Y:\episodes\`)
   - Complete 40-60 minute episodes
   - Final edited videos
   - Episode metadata

3. **Raw Footage** (`Y:\raw_footage\`)
   - Original video recordings
   - Unedited segments
   - Source materials

4. **Edited Content** (`Y:\edited_content\`)
   - Post-production videos
   - Edited segments
   - Intermediate edits

5. **1980s Segments** (`Y:\eighties_segments\`)
   - 15-minute 1980s-style programming/advertising
   - Retro-style content
   - Commercial breaks

6. **Thumbnails** (`Y:\thumbnails\`)
   - Video thumbnails
   - Episode covers
   - Channel artwork

7. **Assets** (`Y:\assets\`)
   - Graphics and logos
   - Music and audio
   - Branding materials

8. **Archive** (`Y:\archive\`)
   - Old episodes
   - Backups
   - Historical content

---

## 🔌 Network Drive Mapping

### Windows Mapping

**Command:**
```cmd
net use Y: \\10.17.17.32\LUMINA-YT /user:backupadm <password> /persistent:yes
```

**Using Script:**
```bash
python scripts/python/lumina_nas_yt_storage.py --map
```

### Manual Mapping Steps

1. **Open File Explorer**
2. **Right-click "This PC"** → "Map network drive"
3. **Select drive letter**: Y:
4. **Folder**: `\\10.17.17.32\LUMINA-YT`
5. **Check "Reconnect at sign-in"**
6. **Check "Connect using different credentials"**
7. **Enter credentials**:
   - Username: `backupadm`
   - Password: (from Azure Key Vault)

### Check Mapping Status

```bash
python scripts/python/lumina_nas_yt_storage.py --check
```

---

## 📁 Storage Paths

### Access via Python

```python
from lumina_nas_yt_storage import LuminaNASYTStorage, StorageType

storage = LuminaNASYTStorage()

# Get storage path for trailers
trailers_path = storage.get_storage_path(StorageType.TRAILERS)
# Returns: Y:\trailers\ (Windows) or /mnt/nas/trailers (Linux)

# Get storage path for episodes
episodes_path = storage.get_storage_path(StorageType.EPISODES)
# Returns: Y:\episodes\
```

### Available Storage Types

- `StorageType.TRAILERS`
- `StorageType.EPISODES`
- `StorageType.RAW_FOOTAGE`
- `StorageType.EDITED_CONTENT`
- `StorageType.EIGHTIES_SEGMENTS`
- `StorageType.THUMBNAILS`
- `StorageType.ASSETS`
- `StorageType.ARCHIVE`

---

## 🔗 Integration with Video Production

### Video Production System

```python
from lumina_ai_video_production import LuminaAIVideoProduction
from lumina_nas_yt_storage import LuminaNASYTStorage, StorageType

# Initialize systems
production = LuminaAIVideoProduction()
storage = LuminaNASYTStorage()

# Generate video
video_path = production.generate_video_segment(segment)

# Move to NAS storage
nas_trailers_path = storage.get_storage_path(StorageType.TRAILERS)
nas_video_path = nas_trailers_path / video_path.name

# Copy to NAS (implement copy logic)
# shutil.copy2(video_path, nas_video_path)
```

### Episode Storage

```python
# After stitching episode
final_episode_path = production.stitch_episode("episode_001")

# Move to NAS episodes directory
nas_episodes_path = storage.get_storage_path(StorageType.EPISODES)
nas_episode_path = nas_episodes_path / f"episode_001_final.mp4"

# Copy to NAS
```

---

## 🔐 Security & Credentials

### Azure Key Vault Integration

NAS credentials are stored in Azure Key Vault:
- **Vault**: jarvis-lumina
- **Secrets**:
  - `nas-username` → Username (backupadm)
  - `nas-password` → Password

### Access

The system automatically retrieves credentials from Azure Key Vault when available.

---

## 📋 Usage

### Map Network Drive

```bash
python scripts/python/lumina_nas_yt_storage.py --map
```

### Check Mapping Status

```bash
python scripts/python/lumina_nas_yt_storage.py --check
```

### Unmap Network Drive

```bash
python scripts/python/lumina_nas_yt_storage.py --unmap
```

### Ensure Storage Directories

```bash
python scripts/python/lumina_nas_yt_storage.py --ensure-paths
```

This creates all storage directories if they don't exist.

### View Configuration

```bash
python scripts/python/lumina_nas_yt_storage.py --summary
```

---

## 🗂️ Directory Structure Example

```
Y:\ (LUMINA-YT)
├── trailers\
│   ├── trailer_001_main.mp4
│   ├── trailer_002_elevator_pitch.mp4
│   ├── trailer_003_mission.mp4
│   ├── trailer_004_philosophy.mp4
│   ├── trailer_005_product.mp4
│   ├── trailer_006_concept.mp4
│   └── trailer_007_personal_journey.mp4
│
├── episodes\
│   ├── episode_001_pilot.mp4
│   ├── episode_002.mp4
│   └── ...
│
├── raw_footage\
│   ├── episode_001\
│   │   ├── segment_001.mp4
│   │   └── segment_002.mp4
│   └── ...
│
├── edited_content\
│   ├── episode_001\
│   │   ├── edited_segment_001.mp4
│   │   └── edited_segment_002.mp4
│   └── ...
│
├── eighties_segments\
│   ├── episode_001_eighties_001.mp4
│   └── ...
│
├── thumbnails\
│   ├── episode_001_thumbnail.jpg
│   └── ...
│
├── assets\
│   ├── logos\
│   ├── music\
│   └── graphics\
│
└── archive\
    └── old_episodes\
```

---

## 🚀 Setup Process

### Initial Setup

1. **Configure NAS Share**
   - Create `LUMINA-YT` share on NAS (10.17.17.32)
   - Set permissions for `backupadm` user

2. **Map Network Drive**
   ```bash
   python scripts/python/lumina_nas_yt_storage.py --map
   ```

3. **Create Storage Directories**
   ```bash
   python scripts/python/lumina_nas_yt_storage.py --ensure-paths
   ```

4. **Verify Setup**
   ```bash
   python scripts/python/lumina_nas_yt_storage.py --summary
   ```

### Integration

1. **Video Production**
   - Videos automatically save to NAS
   - Episodes stored in `Y:\episodes\`
   - Trailers stored in `Y:\trailers\`

2. **Asset Management**
   - Graphics stored in `Y:\assets\`
   - Thumbnails in `Y:\thumbnails\`
   - Music/audio in `Y:\assets\music\`

---

## 💡 Key Features

1. **Centralized Storage**: All YouTube content on NAS
2. **Organized Structure**: Separate directories for each content type
3. **Network Access**: Accessible from any device on network
4. **Backup**: NAS provides automatic backup
5. **Scalability**: Large storage capacity for many episodes
6. **Integration**: Works with video production system

---

**Status**: System initialized and ready  
**Next**: Map network drive and ensure storage directories exist

