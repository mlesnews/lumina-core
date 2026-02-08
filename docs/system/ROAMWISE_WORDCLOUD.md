# Roamwise Portal Word Cloud

**Date:** 2026-01-09  
**System:** Roamwise Portal Word Cloud Visualization  
**Tags:** #JARVIS @LUMINA #WORDCLOUD #ROAMWISE

---

## Overview

The Roamwise Portal Word Cloud visualizes the most popular topics currently being worked on, including:
- **Short@tags** usage
- **AI/Bio tech** topics
- **Current work areas**
- **Documentation topics**
- **Code patterns**

The word cloud "swirls around" showing the most active topics in the LUMINA ecosystem.

---

## Current Top Topics

### 🔝 Top 30 Topics (by frequency)

1. **AI** (20,936) - Artificial Intelligence, LLMs, AI systems
2. **system** (10,201) - System architecture, systems
3. **JARVIS** (7,523) - J.A.R.V.I.S. system
4. **integration** (7,284) - System integrations
5. **workflow** (5,773) - Workflow automation
6. **LUMINA** (5,281) - LUMINA project ecosystem
7. **NAS** (5,049) - Network Attached Storage
8. **API** (3,121) - API development
9. **KAIJU** (3,011) - KAIJU AI system
10. **task** (2,981) - Task management
11. **jarvis** (2,955) - JARVIS references
12. **SYPHON** (2,490) - SYPHON intelligence system
13. **voice** (1,962) - Voice control, hands-free
14. **vault** (1,808) - Azure Key Vault
15. **automation** (1,760) - Automation systems
16. **security** (1,713) - Security systems
17. **Holocron** (1,450) - Holocron notebooks
18. **Docker** (1,428) - Docker containers
19. **project** (1,423) - Project management
20. **MARVIN** (1,396) - MARVIN security specialist
21. **REST** (1,383) - REST APIs
22. **@JARVIS** (1,246) - JARVIS short@tag
23. **lumina** (1,246) - LUMINA references
24. **architecture** (1,214) - System architecture
25. **ULTRON** (941) - ULTRON AI system
26. **container** (855) - Container systems
27. **@DOIT** (842) - DOIT directive tag
28. **@MARVIN** (832) - MARVIN short@tag
29. **tags** (814) - Short@tags
30. **TODO** (793) - TODO management

---

## Categories

### Short@Tags (1,173 unique)
**Top Tags:**
- @JARVIS
- @DOIT
- @MARVIN
- @LUMINA
- @PEAK
- @SYPHON
- @ASK
- @AIQ
- @REC (Recommendations)
- @DB (Database)

### AI/Tech (306 unique)
**Top Topics:**
- AI
- KAIJU
- container
- LLM
- @AIQ
- model
- intelligence
- models
- kaiju
- email

### Database (47 unique)
**Top Topics:**
- database
- MariaDB
- data
- feedback
- mariadb
- @DB
- #DATABASE
- metadata

### Systems (108 unique)
**Top Topics:**
- system
- JARVIS
- LUMINA
- NAS
- jarvis
- Holocron
- @JARVIS
- lumina
- @LUMINA
- nas

---

## Generation

### Text Summary

```bash
python scripts/python/jarvis_roamwise_wordcloud.py --summary
```

### Visual Word Cloud

```bash
# Install dependencies first
pip install wordcloud matplotlib numpy pillow

# Generate visual word cloud
python scripts/python/jarvis_roamwise_wordcloud.py --generate
```

**Output:** `data/roamwise/wordcloud.png`

### Custom Output

```bash
python scripts/python/jarvis_roamwise_wordcloud.py --generate --output path/to/output.png --width 1600 --height 1200
```

---

## Data Sources

The word cloud analyzes:

1. **Short@Tag Registry** (`config/shortag_registry.json`)
   - All registered tags
   - Tag categories
   - Tag descriptions and intents

2. **Documentation** (`docs/`)
   - All markdown files
   - Topics and keywords
   - Tag usage

3. **Code Scripts** (`scripts/python/`)
   - File names
   - Docstrings
   - Code patterns

4. **Current Session Topics**
   - Recent work areas
   - Active projects
   - Current focus

---

## Visualization

The word cloud visualizes:
- **Size** = Frequency (larger = more popular)
- **Color** = Category (viridis colormap)
- **Position** = Random (swirling effect)
- **Words** = Top 200 most frequent topics

---

## Integration with Roamwise Portal

The word cloud can be:
- **Embedded** in Roamwise Portal dashboard
- **Updated** automatically (cron job)
- **Interactive** (click topics for details)
- **Animated** (swirling effect)

---

## Update Frequency

**Recommended:** Update daily or weekly to reflect current work focus.

**Auto-update:** Can be scheduled via cron:
```bash
# Daily update at 2 AM
0 2 * * * python /path/to/jarvis_roamwise_wordcloud.py --generate
```

---

## Summary

The Roamwise Portal Word Cloud shows:
- ✅ **8,532 unique topics** currently active
- ✅ **Top focus:** AI, JARVIS, LUMINA, NAS, integration
- ✅ **1,173 short@tags** in use
- ✅ **306 AI/Tech topics** active
- ✅ **Swirling visualization** of current work

**The word cloud "swirls around" showing the most popular topics you're currently working with!** 🌪️

---

**Tags:** #JARVIS @LUMINA #WORDCLOUD #ROAMWISE #VISUALIZATION
