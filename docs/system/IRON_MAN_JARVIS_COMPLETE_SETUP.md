# Iron Man Virtual Assistants & Jarvis - Complete Setup Guide

**Date:** 2026-01-13  
**Status:** 📋 **SETUP IN PROGRESS**

---

## 🦾 Iron Man Virtual Assistants Architecture

### Three Assistants (Singleton Pattern):
1. **JARVIS** - Master AI Assistant
   - Orchestration, workflow management
   - System integration
   - Intelligence feed processing

2. **Ultron** - Privacy & Autonomous Operations
   - Privacy-sensitive operations
   - Autonomous decision-making
   - Strategic planning

3. **Ultimate Iron Man** - High-Fidelity Assistant
   - Cutting-edge technology assistance
   - Innovation guidance
   - Peak performance optimization

**Rule:** Only ONE can be active at a time (managed by `IronManAssistantManager`)

---

## ⚔️ Magic Words Activation

**Required:** "Jarvis Iron Legion"

- Assistants will NOT activate without magic words
- Detection via voice/text/activation file
- Location: `data/iron_man_activation_phrase.txt`
- Manager checks on every activation attempt

---

## 🤖 Iron Legion AI Models (7 Models on KAIJU)

### Cluster Location:
- **KAIJU_NO_8:** 10.17.17.11
- **Primary Endpoint:** http://10.17.17.11:3000 (expert router)
- **Individual Models:** http://10.17.17.11:3001-3007

### The 7 Marks (Mixture of Experts):

#### Mark I - Code Expert (codellama:13b)
- **Port:** 3001
- **Status:** Working
- **Expertise:** Code generation, debugging, refactoring, architecture
- **Priority:** Highest
- **Use Cases:** Write code, fix bugs, refactor, code review

#### Mark II - General Purpose (llama3.2:11b)
- **Port:** 3002
- **Status:** Restarting
- **Expertise:** General conversation, Q&A, text generation
- **Priority:** High
- **Use Cases:** Answer questions, generate content, summarize

#### Mark III - Quick Response (qwen2.5-coder:1.5b-base)
- **Port:** 3003
- **Status:** Restarting
- **Expertise:** Quick responses, lightweight tasks
- **Priority:** Medium
- **Use Cases:** Fast answers, simple code snippets

#### Mark IV - Balanced Expert (llama3:8b)
- **Port:** 3004
- **Status:** Working
- **Expertise:** Balanced performance, versatile tasks
- **Priority:** Medium
- **Use Cases:** General tasks, balanced performance

#### Mark V - Reasoning Expert (mistral:7b)
- **Port:** 3005
- **Status:** Working
- **Expertise:** Logical reasoning, problem solving
- **Priority:** Medium
- **Use Cases:** Solve problems, analysis, decision making

#### Mark VI - Complex Expert (mixtral:8x7b)
- **Port:** 3006
- **Status:** Restarting
- **Expertise:** High complexity, advanced reasoning
- **Priority:** High
- **Use Cases:** Complex problems, multi-step analysis

#### Mark VII - Fallback Expert (gemma:2b)
- **Port:** 3007
- **Status:** Restarting
- **Expertise:** Lightweight fallback
- **Priority:** Low
- **Use Cases:** Fallback when others unavailable

---

## 🔧 Configuration Files

### 1. Iron Legion Cluster Config
- **File:** `config/iron_legion_cluster_config.json`
- **Purpose:** Cluster endpoints, failover, routing
- **Status:** ✅ Configured

### 2. Iron Legion Experts Config
- **File:** `config/iron_legion_experts_config.json`
- **Purpose:** Expert routing, keyword matching, load balancing
- **Status:** ✅ Configured

### 3. KAIJU Iron Legion Config
- **File:** `config/kaiju_iron_legion_config.json`
- **Purpose:** Local Ollama cluster on KAIJU
- **Status:** ✅ Configured

### 4. Windows Copilot Plugins
- **JARVIS:** `config/windows_copilot_plugins/jarvis_manifest.json`
- **Ultron:** `config/windows_copilot_plugins/ultron_manifest.json`
- **Ultimate Iron Man:** `config/windows_copilot_plugins/ultimate_iron_man_manifest.json`
- **Status:** ✅ Configured

---

## 🚀 Setup Steps

### Step 1: Verify KAIJU Iron Legion Cluster
```bash
# Check if KAIJU is accessible
ping 10.17.17.11

# Check Ollama on KAIJU
curl http://10.17.17.11:11437/api/tags

# Check expert router
curl http://10.17.17.11:3000/health
```

### Step 2: Verify Models on KAIJU
```bash
# Check if all 7 models are available
curl http://10.17.17.11:11437/api/tags | grep -E "codellama|llama3|qwen|mistral|mixtral|gemma"
```

### Step 3: Activate Magic Words
```python
# Create activation file
echo "Jarvis Iron Legion" > data/iron_man_activation_phrase.txt

# Or use Python
from iron_man_assistant_manager import IronManAssistantManager
manager = IronManAssistantManager()
manager.check_magic_words("Jarvis Iron Legion")
```

### Step 4: Launch Assistants
```bash
# JARVIS
python scripts/python/jarvis_desktop_assistant.py

# Ultron
python scripts/python/ultron_desktop_assistant.py

# Ultimate Iron Man
python scripts/python/ultimate_iron_man_desktop_assistant_hq.py

# Or use launcher
python scripts/python/launch_animated_virtual_assistants.py --jarvis
python scripts/python/launch_animated_virtual_assistants.py --ultron
python scripts/python/launch_animated_virtual_assistants.py --ultimate
```

### Step 5: Configure Windows Copilot
- Ensure manifests are in Windows Copilot plugins directory
- Restart Windows Copilot
- Verify plugins are loaded

---

## 📊 Expert Routing Strategy

### Intelligent Expert Selection:
1. **Code-related keywords** → Mark I (codellama:13b)
2. **Complex/advanced keywords** → Mark VI (mixtral:8x7b)
3. **Reasoning keywords** → Mark V (mistral:7b)
4. **Quick/simple keywords** → Mark III (qwen:1.5b)
5. **General purpose** → Mark IV (llama3:8b)
6. **Default** → Mark II (llama3.2:11b)
7. **Fallback** → Mark VII (gemma:2b)

### Routing Endpoints:
- **Expert Router:** http://10.17.17.11:3000/expert
- **Individual Models:** http://10.17.17.11:3001-3007
- **Failover:** http://localhost:11436 (MILLENNIUM_FALCON)

---

## 🔄 Failover Configuration

### Primary: Iron Legion (KAIJU)
- Endpoint: http://10.17.17.11:3000
- Type: Expert router
- Priority: 1

### Secondary: MILLENNIUM_FALCON (Laptop)
- Endpoint: http://localhost:11436
- Type: Failover cluster
- Priority: 2

### Auto-failover:
- Health check interval: 30 seconds
- Failover threshold: 3 failures
- Auto-failback: Enabled

---

## 🎯 Integration Points

### 1. Voice Recognition
- Detects "Jarvis Iron Legion" magic words
- Triggers activation
- Integrates with voice input systems

### 2. Windows Copilot
- Plugin manifests configured
- API endpoints defined
- Capabilities documented

### 3. Assistant Manager
- Singleton pattern enforcement
- Magic words verification
- Process lifecycle management

### 4. Expert Router
- Intelligent model selection
- Keyword-based routing
- Load balancing

---

## ✅ Status Checklist

- [x] Iron Legion cluster config created
- [x] Expert routing config created
- [x] KAIJU config created
- [x] Windows Copilot manifests created
- [x] Assistant manager implemented
- [x] Magic words system implemented
- [ ] KAIJU cluster verified (needs testing)
- [ ] All 7 models verified on KAIJU (needs testing)
- [ ] Expert router tested (needs testing)
- [ ] Assistants launch successfully (needs testing)
- [ ] Windows Copilot plugins loaded (needs testing)

---

## 📝 Next Steps

1. **Verify KAIJU Cluster:**
   - Check KAIJU is running
   - Verify Ollama is running
   - Test all 7 model endpoints

2. **Test Expert Routing:**
   - Test keyword-based routing
   - Verify failover works
   - Check load balancing

3. **Test Assistants:**
   - Activate magic words
   - Launch each assistant
   - Verify singleton pattern

4. **Windows Copilot Integration:**
   - Load plugins
   - Test API endpoints
   - Verify capabilities

---

**Tags:** #IRON_MAN #JARVIS #ULTRON #ULTIMATE_IRON_MAN #IRON_LEGION #AI_MODELS #SETUP @JARVIS @LUMINA

**Status:** 📋 **SETUP GUIDE COMPLETE - READY FOR IMPLEMENTATION**
